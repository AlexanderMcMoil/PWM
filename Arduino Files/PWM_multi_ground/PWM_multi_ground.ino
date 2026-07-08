// int parameters[8][3] = {
//   {50, 20, 0},
//   {0, 0, 0},
//   {0, 0, 0},
//   {0, 0, 0},
//   {0, 0, 0},
//   {0, 0, 0},
//   {0, 0, 0},
//   {0, 0, 0}
// };

int parameters[7][8] = {
  { 0, 0, 0, 0, 0, 0, 0, 0 },  // channel address       0-7       3 bits
  { 0, 0, 0, 0, 0, 0, 0, 0 },  // ground address        0-3       2 bits
  { 0, 0, 0, 0, 0, 0, 0, 0 },  // pulse width           0-~1000   ~10 bits
  { 0, 0, 0, 0, 0, 0, 0, 0 },  // frequency             0-~200    ~8 bits
  { 0, 0, 0, 0, 0, 0, 0, 0 },  // amplitude             0-31      5 bits
  { 0, 0, 0, 0, 0, 0, 0, 0 },  // falling amplitude     0-31      5 bits
  { 0, 0, 0, 0, 0, 0, 0, 0 },  // falling pulse width   
};

#define us_per_sec 1000000L
#define active_address parameters[0]
#define ground_address parameters[1]
#define pulse_width parameters[2]
#define freq parameters[3]
#define amp parameters[4]
#define amp_2 parameters[5]
#define pulse_width_2 parameters[6]

// #define period us_per_sec/freq

const int channels = 8;

long periods[channels] = { us_per_sec / freq[0] , 0, 0, 0, 0, 0, 0, 0 };
// int enable_pin = 7;

const int in_size = 5;
uint8_t valin[in_size] = { 0 };

unsigned long time_diff_pwm[channels] = { 0, 0, 0, 0, 0, 0, 0, 0 };
unsigned long time_curr_pwm[channels] = { 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L };

// unsigned long time_of_last_pulse[channels] = { 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L };
// unsigned long time_since_last_pulse[channels] = { 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L };
unsigned long time_of_next_pulse[channels] = { 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L };


unsigned long time_total = 0L;
bool exit_program = false;

const int cath_pin = 7;
const int anode_pin = 8;
// const int amp_pin = 9;  //Arduino DAC is 10 bits ie 0-1023


const int address_pins[3] = { 6, 5, 4 };  // A, B, C
const int address_ground_pins[2] = {3, 2};   // A, B
const int amplitude_pin_num = 5;
const int amplitude_pins[amplitude_pin_num] = { A1, A2, A3, A5, A4 };



bool is_pulse_ready = false;
long max_wait_time = 0;
int max_wait_time_index = 0;

int fes_channel = 0;
bool fes_on = true;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  while (!Serial);
  Serial.println("Arduino Ready!");
  pinMode(cath_pin, OUTPUT);
  pinMode(anode_pin, OUTPUT);
  // pinMode(enable_pin, OUTPUT);
  // pinMode(6, OUTPUT);
  // digitalWrite(6, HIGH);
  for (int i = 0; i < 3; i++) {
    pinMode(address_pins[i], OUTPUT);
    digitalWrite(address_pins[i], LOW);
  }
  for(int i = 0; i < 2; i++){
    pinMode(address_ground_pins[i], OUTPUT);
    digitalWrite(address_ground_pins[i], LOW);
  }
  for (int i = 0; i < amplitude_pin_num; i++) {
    pinMode(amplitude_pins[i], OUTPUT);
    digitalWrite(amplitude_pins[i], LOW);
  }
  digitalWrite(cath_pin, LOW);
  digitalWrite(anode_pin, LOW);
  // digitalWrite(enable_pin, LOW);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (exit_program) {
    while (true) {}
    return;
  }

  if (Serial.available()) {  //check to see if new parameters have been input
    // channel  pulse_width frequency amplitude lagging_amplitude
    Serial.readBytes(valin, in_size);
    // Serial.println("You entered: ");
    tokenize(valin);
    time_of_next_pulse[fes_channel] = time_total + periods[fes_channel];
    // Serial.println("Channel: " + String(fes_channel));
    // Serial.println("Pulse Width: " + String(parameters[0][fes_channel]));
    // Serial.println("Frequency: " + String(parameters[1][fes_channel]));
    // Serial.println("Amplitude: " + String(parameters[2][fes_channel]));
    // Serial.println("Falling Amplitude: " + String(parameters[3][fes_channel]));
    // Serial.println("Falling Pulse Width: " + String(parameters[4][fes_channel]));
    // Serial.println("Period: " + String(periods[fes_channel]));
  }


  time_total = micros();
  for(int i = 0; i < channels; i++) {
    if (freq[i] != 0 && amp[i] != 0 && pulse_width[i] != 0) {
      // time_diff_pwm[i] = time_total - time_curr_pwm[i];
      if(time_total > time_of_next_pulse[i] && fes_on) {
        if(time_total - time_of_next_pulse[i] >= max_wait_time){
          max_wait_time = time_total - time_of_next_pulse[i];
          max_wait_time_index = i;
          is_pulse_ready = true;
        }
      }
    }
  }

  if(is_pulse_ready){
    time_of_next_pulse[max_wait_time_index] += periods[max_wait_time_index];
    send_pulse(max_wait_time_index);
    is_pulse_ready = false;
    max_wait_time = 0L;
  }
}


void send_pulse(int address) {
  // digitalWrite(enable_pin, LOW);
  for (int i = 0; i < 3; i++) {
    digitalWrite(address_pins[i], (active_address[address] >> i) & 1);
  }
  for(int i = 0; i < 2; i++){
    digitalWrite(address_ground_pins[i], (ground_address[address] >> i) & 1);
  }
  for (int i = 0; i < amplitude_pin_num; i++) {
    digitalWrite(amplitude_pins[i], (amp[address] >> i) & 1);
  }
  delayMicroseconds(50);
  digitalWrite(cath_pin, HIGH);
  delayMicroseconds(pulse_width[address]);
  digitalWrite(cath_pin, LOW);
  for (int i = 0; i < amplitude_pin_num; i++) {
    digitalWrite(amplitude_pins[i], (amp_2[address] >> i) & 1);
  }
  // delayMicroseconds(50);
  digitalWrite(anode_pin, HIGH);
  delayMicroseconds(pulse_width_2[address]);
  digitalWrite(anode_pin, LOW);
  delayMicroseconds(50);
}

void tokenize(uint8_t* buffer) {
  // if (*str == 'q') {
  //   Serial.println("Exiting");
  //   exit_program = true;
  //   return;
  // }
  // char* token = strtok(str, " ");
  // fes_channel = atoi(token);
  // token = strtok(NULL, " ");
  // for (int i = 0; i < 6; i++) {
  //   parameters[i][fes_channel] = atoi(token);
  //   token = strtok(NULL, " ");
  // }
  fes_channel               = (buffer[4])          & 0x07;   // Mask: 3 bits  (max 7)
  amp[fes_channel]          = (buffer[4] >> 3)     & 0x1F;   // Mask: 5 bits  (max 31)
  pulse_width[fes_channel]  = (buffer[3])          & 0xFF;  // Mask: 10 bits (max 1023)
  pulse_width[fes_channel]  |= (buffer[2] & 0x03) << 8;
  freq[fes_channel]         = (buffer[2] >> 2)     & 0x3F;   // Mask: 6 bits  (max 63)
  amp_2[fes_channel]        = (buffer[1])          & 0x1F;   // Mask: 5 bits  (no shift needed)
  active_address[fes_channel] = (buffer[1] >> 5)  & 0x07    // 3 bits
  ground_address[fes_channel] = (buffer[0])         & 0x03    // 2 bits

  if(amp_2[fes_channel] == 0){
    pulse_width_2[fes_channel] = 0;
  }
  else{
    pulse_width_2[fes_channel] = pulse_width[fes_channel] * amp[fes_channel] / amp_2[fes_channel];
  }
  if(freq[fes_channel] != 0){
    // Serial.println(freq[fes_channel]);
    periods[fes_channel] = us_per_sec / freq[fes_channel];
  }
  else{
    periods[fes_channel] = 0;
  }
}
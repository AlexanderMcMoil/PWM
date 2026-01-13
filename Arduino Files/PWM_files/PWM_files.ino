
int parameters[3] = {50, 20, 0};    //pulse width, frequency, amplitude

#define us_per_sec 1000000
#define pulse_width parameters[0]
#define freq parameters[1]
#define amp parameters[2]
#define period us_per_sec/freq


const int in_size = 32;
char valin[in_size] = {0};


unsigned long time_diff_pwm = 0;
unsigned long time_curr_pwm = 0;

unsigned long time_total = 0;
bool exit_program = false;

const int cath_pin = 9;
const int anode_pin = 8;
const int amp_pin = DAC0;   //Arduino DAC is 10 bits ie 0-1023

bool fes_on = true;


void setup() {
  // put your setup code here, to run once:
    Serial.begin(115200);
  while(!Serial);
  Serial.println("Arduino Ready!");
  pinMode(cath_pin, OUTPUT);
  pinMode(anode_pin, OUTPUT);
  digitalWrite(cath_pin, LOW);
  digitalWrite(anode_pin, LOW);
  pinMode(DAC0, OUTPUT);
  analogWriteResolution(10);
  analogWrite(amp_pin, 0);

  // noInterrupts();


}

void loop() {
  // put your main code here, to run repeatedly:
  if(exit_program){
    while(true){}
    return;
  }

  if(Serial.available()){ //check to see if new parameters have been input
  
    Serial.readBytes(valin, in_size);
    Serial.println("You entered: ");
    tokenize(valin, ' ');
    Serial.println("Pulse Width: " + String(parameters[0]));
    Serial.println("Frequency: " + String(parameters[1]));
    Serial.println("Amplitude: " + String(parameters[2]));
    analogWrite(amp_pin, amp);
  }


  time_diff_pwm = micros() - time_curr_pwm;
  if(freq > 0){
    if(time_diff_pwm > period && fes_on){
      time_curr_pwm = micros();
      send_pulse();
    }
  }
}

void send_pulse(){
  digitalWrite(cath_pin, HIGH);
  delayMicroseconds(pulse_width);
  digitalWrite(cath_pin, LOW);
  delayMicroseconds(50);
  digitalWrite(anode_pin, HIGH);
  delayMicroseconds(pulse_width);
  digitalWrite(anode_pin, LOW);
}

void tokenize(char* str, char delimiter){
  if(*str == 'q'){
    Serial.println("Exiting");
    exit_program = true;
    return;
  }
  char* token = strtok(str, " ");
  for(int i = 0; i < 3; i++){
    parameters[i] = atoi(token);
    token = strtok(NULL, " ");
  }
}
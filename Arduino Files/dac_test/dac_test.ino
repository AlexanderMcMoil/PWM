const int amplitude_pins[4] = { A1, A2, A3, A4 };
int amplitude = 0;
int voltage_val = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  for (int i = 0; i < 4; i++) {
    pinMode(amplitude_pins[i], OUTPUT);
    digitalWrite(amplitude_pins[i], LOW);
  }
  delay(200);
}

void loop() {
  // put your main code here, to run repeatedly:
  send_pulse(amplitude);
  amplitude++;
  if(amplitude >= 16){
    amplitude = 0;
  }
  delay(1000);
  voltage_val = analogRead(A0);
  Serial.print("Setting: ");
  Serial.println(amplitude);
  Serial.println(voltage_val);
}

void send_pulse(int address) {
  // analogWrite(amp_pin, amp[address]);
  for (int i = 0; i < 4; i++) {
    digitalWrite(amplitude_pins[i], (amplitude >> i) & 1);
  }
}
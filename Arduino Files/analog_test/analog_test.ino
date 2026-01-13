
int amp_pin = A0;
const int in_size = 32;
char valin[in_size] = {0};


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // pinMode(amp_pin, OUTPUT);
  // analogWrite()
  // analogWrite(amp_pin, 255);
  // analogWriteResolution(10);
  // analogWrite(amp_pin, 50);
  // for(int i = A1; i <= A7; i++){
  //   analogWrite(i, 100 + 10*i);
  // }
  // pinMode(9, OUTPUT);

  noInterrupts();
  TCCR1A = 
    1 << COM1A1 |
    1 << WGM10;
  TCCR1B = 
    1 << WGM12 |
    1 << CS10;
  DDRB = 
    1 << DDB1;
  OCR1A = 100;
  interrupts();
}

void loop() {
  // put your main code here, to run repeatedly:
  // if(Serial.available()){
  //   Serial.readBytes(valin, in_size);
  //   int val = atoi(valin);
  //   Serial.println(val);
  //   OCR1A = val;
    // analogWrite(amp_pin, val);
  // }
  // OCR1A = 0;
  // delay(15);
  // OCR1A = 255;
  // delay(15);

  // analogWrite(amp_pin, 255);
}
// void myPwm(unsigned char duty, float freq) {
//   TCCR1A = 0x21;
//   TCCR1B = 0x14;
//   OCR1A = 0x7A12 / freq;
//   OCR1B = OCR1A * (duty / 255.0);
// }
#include "Adafruit_GFX.h"

Adafruit_GFX screen = Adafruit_GFX(480, 320);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  screen.fillRect(10, 10, 5, 5);
}

void loop() {
  // put your main code here, to run repeatedly:

}

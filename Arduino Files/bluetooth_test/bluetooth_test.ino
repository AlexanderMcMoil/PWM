#include <ArduinoBLE.h>


BLEService fesService("19B10010-E8F2-537E-4F6C-D104768A1214");
BLEIntCharacteristic fesCharacteristic("19B10011-E8F2-537E-4F6C-D104768A1214", BLEWrite);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while (!Serial);
  if( !BLE.begin()){
    Serial.println("bluetooth failed uh oh");
    while(1){}
    
  }
  BLE.setLocalName("FES");

}

void loop() {
  // put your main code here, to run repeatedly:

  
}

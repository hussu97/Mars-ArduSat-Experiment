#include <Wire.h>
#include <ArdusatSDK.h>


ArdusatSerial serialConnection(SERIAL_MODE_HARDWARE_AND_SOFTWARE, 8, 9);

Acceleration accel;
Magnetic mag;
Orientation orient(accel,mag);
TemperatureMLX irtemp;
UVLight uv;
Gyro gyr;

void setup(){
  serialConnection.begin(9600);

  accel.begin();
  mag.begin();
  orient.begin();
  irtemp.begin();
  uv.begin();
}

void loop(){

  accel.read();
  mag.read();
  orient.read();
  irtemp.read();
  uv.read();
  
  serialConnection.println(valuesToCSV('reading',mag.x,mag.y,mag.z,irtemp.t,uv.uvindex,orient.roll,orient.pitch));
  
  delay(1000);
}



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
  gyr.begin();
}

void loop(){

  serialConnection.println(accel.readToJSON("accel"));
  serialConnection.println(irtemp.readToJSON("irtemp"));
  serialConnection.println(uv.readToJSON("uv"));
  serialConnection.println(orient.readToJSON("orient"));
  serialConnection.println(gyr.readToJSON("gyr"));
  serialConnection.println(irtemp.readToJSON("irtemp"));
  
  delay(1000);
}



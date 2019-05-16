/*
 * =====================================================================================
 *
 *       Filename:  example_template.ino
 *
 *    Description:  A template for how to design an example sketch.
 *
 *                  Use the Ardusat Experiment Platform to visualize your data!
 *                  http://experiments.ardusat.com
 *
 *                  This example uses many third-party libraries available from
 *                  Adafruit (https://github.com/adafruit). These libraries are
 *                  mostly under an Apache License, Version 2.0.
 *
 *                  http://www.apache.org/licenses/LICENSE-2.0
 *
 *        Version:  1.0
 *        Created:  09/01/2015
 *
 *         Author:  Hussain Abbasi
 *   Organization:  American University of Sharjah
 *
 * =====================================================================================
 */
 
/*-----------------------------------------------------------------------------
 *  Includes
 *-----------------------------------------------------------------------------*/
#include <Wire.h>
#include <ArdusatSDK.h>

/*-----------------------------------------------------------------------------
 *  Setup Software Serial to allow for USB communication
 *-----------------------------------------------------------------------------*/
ArdusatSerial serialConnection(SERIAL_MODE_HARDWARE_AND_SOFTWARE, 8, 9);

Acceleration accel;
Magnetic mag;
Orientation orient(accel,mag);
TemperatureMLX irtemp;
UVLight uv;
Gyro gyr;


/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  setup
 *  Description:  This function runs when the Arduino first turns on/resets. This is 
 *                our chance to take care of all one-time configuration tasks to get
 *                the program ready to begin logging data.
 * =====================================================================================
 */

 
void setup(){
  serialConnection.begin(9600);

  //begin required sensors
  accel.begin();
  mag.begin();
  orient.begin();
  irtemp.begin();
  uv.begin();
}

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  loop
 *  Description:  After setup runs, this loop function runs until the Arduino loses 
 *                power or resets. We go through and read from each of the attached
 *                sensors, write out the corresponding sounds in CSV format, then
 *                delay before repeating the loop again.
 * =====================================================================================
 */
 
void loop(){

  //read required sensors
  mag.read();
  orient.read();
  irtemp.read();
  uv.read();

  serialConnection.println(mag.readToCSV("Magnetometer"));
  serialConnection.println(orient.readToCSV("TEST_ORIENT"));
  
  serialConnection.println(valuesToCSV('reading',mag.x,mag.y,mag.z,irtemp.t,uv.uvindex,orient.roll,orient.pitch));
  
  delay(1000);
}



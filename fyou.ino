#include <SerialCommand.h>
#include <Servo.h>

Servo myServo;
SerialCommand sCmd;

void setup() {

    myServo.attach(9);

    Serial.begin(9600);
    sCmd.addCommand("P", setServoPosition);
    sCmd.setDefaultHandler(unrecognized);

    myServo.write(0);
    Serial.println("Ready.");
}

void loop() {
    sCmd.readSerial();
}

void setServoPosition()
{
    char *arg;
    arg = sCmd.next();
    if (arg != NULL)
    {
        myServo.write(atoi(arg));
    }
}

void unrecognized(const char *command) {
    Serial.println("What?");
}

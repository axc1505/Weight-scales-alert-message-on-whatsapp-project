#include <HX711.h> //library dedicated for my sensor
Hx711 scale(A2,A3);


void setup()
{
Serial.begin(9600);
}

void loop()
{
int grame=(scale.getGram());
Serial.println(grame);
}

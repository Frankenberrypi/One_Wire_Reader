int lightPin = 1;
float lightValue;

void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600);
  pinMode(lightPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  lightValue = analogRead(lightPin);
  Serial.println(lightValue);
  delay(1000);
}

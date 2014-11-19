int led = 10;

byte mail;

void setup() {

  Serial.begin(9600);
  pinMode(led, OUTPUT);
  
}

void loop() {
  int mail = Serial.read();
  if(mail == '1') {
    digitalWrite(led, HIGH);
  }
  else if(mail == '0') {
    digitalWrite(led, LOW);
  }
  while(mail == '2') {
    digitalWrite(led, HIGH);
    delay(500);
    digitalWrite(led, LOW);
    delay(500);
    if(mail != '2') {
      digitalWrite(led, HIGH);
      delay(1000);
      break;
    }
    else {
    }
  }
}

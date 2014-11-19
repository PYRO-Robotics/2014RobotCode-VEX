int m1 = 2;
int m2 = 3;
int m3 = 4;
int m4 = 5;
int s1 = 7;
int s2 = 8;
int s3 = 9;
int s4 = 10;

void setup() {
  
  pinMode(m1, OUTPUT);
  pinMode(m2, OUTPUT);
  pinMode(m3, OUTPUT);
  pinMode(m4, OUTPUT);
  pinMode(s1, INPUT);
  pinMode(s2, INPUT);
  pinMode(s3, INPUT);
  pinMode(s4, INPUT);
  
}

void motor1fwd() {
  
  digitalWrite(m1, HIGH);
  digitalWrite(m2, LOW);
  
}
  
void motor1bwd() {
  
  digitalWrite(m1, LOW);
  digitalWrite(m2, HIGH);
  
}

void motor1stp() {
  
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
  
}

void motor2fwd() {
  
  digitalWrite(m3, HIGH);
  digitalWrite(m4, LOW);
  
}

void motor2bwd() {
  
  digitalWrite(m3, LOW);
  digitalWrite(m4, HIGH);
  
}

void motor2stp() {
  
  digitalWrite(m3, LOW);
  digitalWrite(m4, LOW);
  
}

void loop() {
  
  if(s1 == 1) {
    motor1fwd();
  }
  
  else if(s2 == 1) {
    motor1bwd();
  }
  
  else if(s3 == 1) {
    motor2fwd();
  }
  
  else if(s4 == 1) {
    motor2bwd();
  }
  
  else {
    motor1stp();
    motor2stp();
  }

}

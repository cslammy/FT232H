
//show me what is coming into RX port

int incomingByte = 0; // for incoming serial data
int p = 0;


void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
}

void loop() {
  // reply only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
   
    p = (incomingByte);
    char c = p;
    Serial.print(c);
  }
}

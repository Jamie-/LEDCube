/*
  Name:			cube_layer_chase.ino
  Description:	Layers of the cube chasing.
  Build:		0.1
*/
 
// Speed for wait times.
int wait = 250;
 
// Naming and declaring the pins for the LED cube.
int topLayer = 0;
int midLayer = 1;
int botLayer = 2;

int col1 = 3;
int col2 = 4;
int col3 = 5;
int col4 = 6;
int col5 = 7;
int col6 = 8;
int col7 = 9;
int col8 = 10;
int col9 = 11;

void setup() {                
  // Setting up the pins.
  pinMode(topLayer, OUTPUT); 
  pinMode(midLayer, OUTPUT);
  pinMode(botLayer, OUTPUT);
  
  pinMode(col1, OUTPUT);
  pinMode(col2, OUTPUT);
  pinMode(col3, OUTPUT);
  pinMode(col4, OUTPUT);
  pinMode(col5, OUTPUT);
  pinMode(col6, OUTPUT);
  pinMode(col7, OUTPUT);
  pinMode(col8, OUTPUT);
  pinMode(col9, OUTPUT);

 //Turns all LED columns on.
  digitalWrite(col1, HIGH);
  digitalWrite(col2, HIGH);
  digitalWrite(col3, HIGH);
  digitalWrite(col4, HIGH);
  digitalWrite(col5, HIGH);
  digitalWrite(col6, HIGH);
  digitalWrite(col7, HIGH);
  digitalWrite(col8, HIGH);
  digitalWrite(col9, HIGH);

}

void loop() {
  
  // Main Program for the cube.
  
  // Bottom layer.
  digitalWrite(botLayer, HIGH);
  delay(wait);
  digitalWrite(botLayer, LOW);
  
  // Middle layer.
  digitalWrite(midLayer, HIGH);
  delay(wait);
  digitalWrite(midLayer, LOW);

  // Top layer.
  digitalWrite(topLayer, HIGH);
  delay(wait);
  digitalWrite(topLayer, LOW);
  
  // Middle layer.
  digitalWrite(midLayer, HIGH);
  delay(wait);
  digitalWrite(midLayer, LOW);
}

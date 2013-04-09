3x3x3 LED Cube Code
================

Code for running a 3x3x3 LED cube with an Arduino Uno. Uses 12 I/O out of 14 on the Uno.

See 'cube_chase' in action: http://youtu.be/KalYkLarVPs

Setup
-------------

1) Wire up the cube layer transistors first.
    	Use pin 0 for the top layer.
	Use pin 1 for the middle layer.
	Use pin 2 for the bottom layer.

2) Then wire up the cube faces directly.	
	Use pins 3,4 and 5 for the rear cube face.
	Use pins 6,7 and 8 for the middle cube face.
	Use pins 9,10 and 11 for the front face.
	

Install
-------------

1) Choose which program you want to use from the list below.
2) Open the project in the Arduino editor.
3) Under the tools menu, select your Arduino board, and select its port number.
4) Plug in your Arduino
5) Download the program to the board.
6) Watch the pretty cube!

(Note: At the top of each program, there is a variable named 'wait' this is the speed in milliseconds that the cube chases at, change this to run it at different speeds.)

Programs and Descriptions
-------------

cube_layer_chase = Layers of the cube chasing.
cube_face_chase = Faces of the cube chasing.
cube_alternate_chase = Layers then faces of the cube chasing.
cube_chase = Multi-cube chase (rather hard to describe really).

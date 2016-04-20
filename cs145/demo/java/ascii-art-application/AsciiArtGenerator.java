// AsciiArtGenerator.java

/* This class is used to start the program but do note that the main 
	method immediately attempts to CONSTRUCT an AsciiRectangle OBJECT.
	You should understand how both files are working together.
*/

class AsciiArtGenerator {

	public static void main(String[] args) {

		AsciiRectangle rect_1 = new AsciiRectangle(10, 5, 0, 0);
		rect_1.displayRectangle();
		
	}
}
// AsciiArtGenerator.java

/* This class is used to start the program but do note that the main 
	method immediately attempts to CONSTRUCT an AsciiRectangle OBJECT.
	You should understand how both files are working together.
*/

class AsciiArtGenerator {

	public static void main(String[] args) {

		// CONSTRUCTOR gives us an OBJECT called rect_1
		AsciiRectangle rect_1 = new AsciiRectangle(10, 5);
		AsciiRectangle rect_0 = new AsciiRectangle(5, 10);

		rect_0.displayRectangleFilled();
		rect_0.getWidth();


	
	}
}
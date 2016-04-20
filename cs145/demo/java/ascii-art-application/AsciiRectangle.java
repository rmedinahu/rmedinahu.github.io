// AsciiRectangle.java

/* Simple example of a CLASS definition. An AsciiRectangle object
	MODELS a simple rectangle that can be drawn using ascii characters.
 	Make sure you can find the PROPERTIES and BEHAVIORS.
*/
class AsciiRectangle {
	double width;
	double height;
	double xcoord;
	double ycoord;

	// Constructor: A special method that creates an AsciiRectangle OBJECT by setting its properties.
	public AsciiRectangle(double w, double h, double x, double y) {
		width = w;
		height = h;
		xcoord = x;
		ycoord = y;
	}

	// Method (behavior) designed to print the rectangle on the screen using ascii characters.
	
	public void displayRectangle() {
		String top_bottom = "";
		String sides = "";
		String display_char = ".";

		System.out.println("\nRectangle ==> width = " + width + " height = " + height);
		for(int i = 0; i < width; i++) {
			top_bottom += display_char;
			if (i == 0) {
				sides += display_char;
			} else if (i == width-1) {
				sides += display_char;
			} else {
				sides += " ";
			}
		}

		for(int i = 0; i < height; i++) {
			if (i == 0 || i == height-1) {
				System.out.println(top_bottom);
			} else {
				System.out.println(sides);
			}
		}
	}

}
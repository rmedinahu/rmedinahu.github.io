class AsciiRectangle {
	double width;
	double height;
	double xcoord;
	double ycoord;

	// Construct a rectangle object
	public AsciiRectangle(double w, double h, double x, double y) {
		width = w;
		height = h;
		xcoord = x;
		ycoord = y;
	}

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
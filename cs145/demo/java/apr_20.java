// apr_20.java

class apr_20 {

	static double[] constructRectangle(double w, double h, double x, double y) {
		// Model a rectangle using four properties grouped in an array:
		// width, height, xcoord, ycoord
		double[] rectangle = new double[4];
		rectangle[0] = w;
		rectangle[1] = h;
		rectangle[2] = x;
		rectangle[3] = y;

		return rectangle;
	}

	static void displayRectangle(double[] r) {
		String top_bottom = "";
		String sides = "";
		String display_char = ".";

		System.out.println("\nRectangle ==> width = " + r[0] + " height = " + r[1]);
		for(int i = 0; i < r[0]; i++) {
			top_bottom += display_char;
			if (i == 0) {
				sides += display_char;
			} else if (i == r[0]-1) {
				sides += display_char;
			} else {
				sides += " ";
			}
		}

		for(int i = 0; i < r[1]; i++) {
			if (i == 0 || i == r[1]-1) {
				System.out.println(top_bottom);
			} else {
				System.out.println(sides);
			}
		}
	}

	public static void main(String[] args) {
		double[] rect_1 = constructRectangle(20, 5, 10, 10);
		System.out.println();
		displayRectangle(rect_1);
		System.out.println();
	}
}
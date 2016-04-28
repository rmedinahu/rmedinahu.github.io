class Worm {
	String name;
	int length;
	String color;


	public Worm(String n, int l, String c) {
		name = n;
		length = l;
		color = c;
	}
/* Getter and Setters */
	public int getLength() {
		return length;
	}

	public String getColor() {
		return color;
	}

	public void setLength(int l) {
		length = l;
	}

	public void setColor(String c) {
		color = c;
	}

/* End getters and setters */


	public String aboutThisWorm() {
		String d = "\n\t" + name + " is a " + color + " worm " + length + " cm long.\n";
		return d;
	}


/* A static method useful for the CLASS Worm (not any Worm in particular). */

	public static String aboutWorms() {
		String description = "A worm object has a name and is described by its length and color.";
		return description;
	}
}







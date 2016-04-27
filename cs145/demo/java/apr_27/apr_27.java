class apr_27 {
	
	public static void main(String[] args) {
		System.out.println("\n<==== Welcome to the Worm Hole ====>\n\n");

		// Use a static method to get information about ALL worms.
		System.out.println( Worm.aboutWorms() );

		// Construct a Worm object using the CONSTRUCTOR.
		Worm alice = new Worm();

		String s = alice.aboutThisWorm();
		System.out.println(s);

		System.out.println();
	}
}
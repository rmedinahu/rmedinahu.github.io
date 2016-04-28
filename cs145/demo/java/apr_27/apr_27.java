class apr_27 {
	
	public static void main(String[] args) {
		System.out.println("\n<==== Welcome to the Worm Hole ====>\n\n");

		// Construct a Worm object using the CONSTRUCTOR.
		Worm alice = new Worm("alice", 30, "purple");
		Worm richard = new Worm("richard", 18, "green");
		

		String s = alice.aboutThisWorm();
		System.out.println(s);
		s = richard.aboutThisWorm();
		System.out.println(s);


		// Use a static method to get information about ALL worms.
		System.out.println( Worm.aboutWorms() );
		System.out.println();
	}
}









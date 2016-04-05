class SnakeEyesJava {

	public static void main(String[] args) {
		
		int result = 0; // variable to hold the result of each roll.
		int rolls = 1;	// variable to track the number of rolls.

		while (result != 2) {
		
			// Roll the dice!
			int die_1 = (int)(Math.random() * 6) + 1;
			int die_2 = (int)(Math.random() * 6) + 1;
			
			result = die_1 + die_2;	// calculate the result
			rolls = rolls + 1;		// increment the roll count.
		
		} // End of the while loop block
	
		// Print the number of rolls.
		System.out.println("Number of rolls to get Snake Eyes ==> " + rolls);
	}
}
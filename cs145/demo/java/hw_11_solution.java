class hw_11_solution {
	
	public static void main(String[] args) {
		// BEGIN SNAKE EYES...Yay!!!!

		// we're going to count up our rolls.
		int roll_count = 0;

		// random num between 1 and 6
		int die_1 = (int)(Math.random()*6) + 1;
		int die_2 = (int)(Math.random()*6) + 1;
		int roll;

		// we just "rolled" so increment our counter.
		roll_count++; 
		
		// capture the result of the roll. 2 means snake eyes were rolled.
		roll = die_1 + die_2;
		
		while (roll != 2) {
			die_1 = (int)(Math.random()*6) + 1;
			die_2 = (int)(Math.random()*6) + 1;
			roll_count++;
			roll = die_1 + die_2;
		}

		System.out.println("Snake eyes rolled! It took " + roll_count + " rolls.");

	}

}
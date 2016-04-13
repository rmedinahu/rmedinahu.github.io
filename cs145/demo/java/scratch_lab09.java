// Solutions to lab 09 (Apr 8) exercises.
import java.util.Scanner;  // Make the Scanner class available.

class scratch_lab09 {
	
	public static void main(String[] args) {
		// Hook up Scanner to console input.
		Scanner user_input_scanner = new Scanner( System.in );

/* 
Exercise 1: Using scanner with try/catch block to handle invalid input.
*/

		int my_num = 0;
		boolean continue_prompting = true;

		while(continue_prompting) {
			try {
				// Prompt for information:
				System.out.print("Enter a number please:");
				my_num = user_input_scanner.nextInt();

				// We can assume no exceptions were thrown. Flip our flag to stop looping.
				continue_prompting = false;
			
			} catch (Exception e) {
				String flushed = user_input_scanner.next(); //CLEAR the SCANNER!!!
				System.out.println("You entered a value that cannot be an integer.");
			}
		}

		//Print the user's input...
		System.out.println("Your number is: " + my_num);
		

/* 
Exercise 2: 
	a. Make an array of length determined by user.
	b. Populate array with random doubles between 1 and 100 inclusive.
	c. Print each random num as it is assigned to the array.
*/
		

		System.out.println("\n\nHere is an array of doubles.");

		// Make an array of size determined by my_num:
		double[] nums = new double[my_num];

		for(int index = 0; index < nums.length; index++) {
			// add random double to each element.
			nums[index] = (Math.random()*100) + 1;
			System.out.print(nums[index] + " ");
		}

/* 
Exercise 3: 
	a. Build a new string by asking the user for successive characters until they choose to stop.
	b. Print the newly built string.
*/
		String str = ""; // Start with an empty string.
		String users_char = "";
		boolean continue_looping = true;
		
		
		while (continue_looping) {
			str += users_char;
			
			System.out.print("\n\nPlease enter a single letter or enter an asterisk to stop. ==> ");
			users_char = user_input_scanner.next(); // Read in the entered character.			
			
			// User .equals to compare strings. It will return a boolean value.
			continue_looping = !users_char.equals("*");
		}

		System.out.println("\n\nHere is your string ==> " + str);
		
	}

}


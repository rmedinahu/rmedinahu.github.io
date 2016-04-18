// apr_15.java

import java.util.Scanner;

class lab_10_solution {

/* 
Exercise 1: A method the prints n stars on a single line.
*/

	static void stars (int n) {
		for (int i = 0; i < n; i++) {
			System.out.print("*");
		}
		// Print a line break after all stars have printed
		System.out.print("\n");
	}

/*
Exercise 2: Refer to main.
*/

/*
Exercise 3: A method to counts the frequence of query
			in searchString.
*/
	static int countChars (String searchString, char query) {
		/* the plan for summation...
			
			1. set total to 0
			2. for every character in searchString
				a. get character at current index
				b. if character is equal to query
					add 1 to total
		
		*/

		int total = 0;
		for(int i = 0; i < searchString.length(); i++) {
			char current_char = searchString.charAt(i);
			if (query == current_char) {
				total = total + 1;
			}			
		}

		return total;
	}

/*
Exercise 4: A method to finds and returns the smallest of
			three integers given as arguments.
*/

	static int findMin(int a, int b, int c) {

		if (a <= b && a <= c) {
			return a;
		} else if (b <= a && b <= c) {
			return b;
		}
		// Clearly NOT a and NOT b so c must be smallest
		return c;
	}

	public static void main(String[] args) {
		// Call the stars method with argument 7
		stars(7);

		// Call the stars method 10 times.
		for (int i = 0; i < 10; i++) {
			stars(i+1);
		}

		// Gather user input to use as arguments for countChars method. 
		Scanner input_scanner = new Scanner(System.in);
		System.out.print("Enter a string: ");
		String user_str = input_scanner.next();

		System.out.print("Enter a character:");
		String char_str = input_scanner.next();
		char input_char = char_str.charAt(0);

		// Ready to call the countChars method...
		int result = countChars(user_str, input_char);
		System.out.println(input_char + " appears " + result + " times in " + user_str);

		// Create and declare variables for the findMin method.
		int x = 0;
		int y = 0;
		int z = 0;
		
		// loop prime
		boolean continue_prompting = true;

		// keep asking for input if user enters incompatible information.
		while(continue_prompting) {
			try {
				System.out.print("Enter integer 1: ");
				x =	input_scanner.nextInt();
				
				System.out.print("Enter integer 2: ");
				y =	input_scanner.nextInt();
				
				System.out.print("Enter integer 3: ");
				z =	input_scanner.nextInt();

				// Made it to here without exception so all is good. Stop looping.
				continue_prompting = false;

			} catch (Exception e) {
				String flushme = input_scanner.next();
				System.out.println("Please enter INTEGERS! Try again.\n");
			}
		} // End of while loop to gather user input...

		// Call the findMin method with collected values for x, y, and z.
		// Store the result of the method call in variable min then print it.
		int min = findMin(x, y, z);
		System.out.println ("min of " + x + " " + y + " " + z + " is ==> " + min);
	}

}
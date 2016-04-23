// hw_13_solution

import java.util.Scanner;

class hw_13_solution {

	public static void main(String[] args) {
		Scanner user_input_scanner = new Scanner(System.in);
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

		// Make an array of size determined by my_num:
		double[] nums = new double[my_num];

		for(int index = 0; index < nums.length; index++) {
			// add random double to each element.
			nums[index] = (Math.random()*100) + 1;
		}

		// Now loop (again) through the array counting up where each value falls.
		// Ranges: 1-40, 41-60, 61-80, 81-100

		// Set up counters but use strings!
		String range1 = "";
		String range2 = "";
		String range3 = "";
		String range4 = "";

		for (int index =0; index < nums.length; index++) {
			if (nums[index] <= 40) {
				range1 += ".";

			} else if (nums[index] <= 60) {
				range2 += ".";

			} else if (nums[index] <= 80) {
				range3 += ".";

			} else {
				range4 += ".";	
			}
		}

		// Display a "histogram"
		System.out.println(" 1-40  ==> " + range1.length() + " =\t" + range1);
		System.out.println("41-60  ==> " + range2.length() + " =\t" + range2);
		System.out.println("61-80  ==> " + range3.length() + " =\t" + range3);
		System.out.println("81-100 ==> " + range4.length() + " =\t" + range4);
	}
}
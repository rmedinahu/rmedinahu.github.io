import java.util.Scanner;  // Make the Scanner class available.

/*
1. Ask the user for an integer.
2. Print the integer entered by the user to verify it.
*/


class scratch_lab09 {
	
	public static void main(String[] args) {
		// Hook up Scanner to console input.
		Scanner user_input = new Scanner( System.in );
		int my_num = 0;
		boolean prompt_flag = true;

		while(prompt_flag) {
			try {
				// Prompt for information:
				System.out.println("Enter a number please:");
				my_num = user_input.nextInt();
				prompt_flag = false;
			
			} catch (Exception e) {
				user_input.next(); //CLEAR the SCANNER!!!
				System.out.println("BAD INPUT!!!!");
			}
		}

		//Print the user's input...
		System.out.println(my_num);

		// Make an array of size MY_NUM:
		double[] nums = new double[my_num];

		for(int index = 0; index < nums.length; index++) {
			// add random double to each element.
			nums[index] = (Math.random()*100) + 1;
			System.out.print(nums[index] + " ");
		}

		String str = "";
		String user_char = "a";

		if(user_char == "a") {
			System.out.println("matched");
		}

		// while (user_char != "*") {


		// }
	}

}


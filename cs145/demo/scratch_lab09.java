import java.util.Scanner;  // Make the Scanner class available.


class scratch_lab09 {
	public static void main(String[] args) {
		Scanner user_input = new Scanner( System.in );

		try {
			System.out.print("Enter a number:");
			int var_1 = user_input.nextInt();
		
		} catch (Exception e) {
			System.out.println("bad input");
		}

		int[] list_1 = new int[10];

		for (int i = 0; i < list_1.length; i++) {
			list_1[i] = (int)(Math.random()*20) + 1;
		}

		System.out.println(Math.random()*100);

		String row_1 = "";

		row_1 += "a";
		row_1 += "b";

		System.out.println(row_1);

	}
}
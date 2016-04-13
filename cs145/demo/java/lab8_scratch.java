import java.util.Scanner;  // Make the Scanner class available.


class lab8_scratch {
	
	public static void main (String[] args) {
		System.out.println("Hello World!");
		int my_fav_num = 0;

		String my_name = "";

		// Create the Scanner.
		Scanner user_input = new Scanner( System.in );

		//Prompt
		System.out.print("Enter your name please: ");
		my_name = user_input.next();

		System.out.println("Hello " + my_name);


		int random_num = (int)(Math.random()*20) + 1;  //num between 1 and 20 inclusive
		System.out.println("Random==> " + random_num);

		int count = 1;
		
		while (count <= random_num) {
			if (count % 2 == 0) {
				System.out.println(count);
			}
			count = count + 1;
		}
	}
}















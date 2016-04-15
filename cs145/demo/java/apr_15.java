// apr_15.java

import java.util.Scanner;

class apr_15 {

	// Example static function ...
	static void printmsg(String m) {
		System.out.println("Message ==>\n" + m);
	}

	static void stars (int n) {

		System.out.println("\n");
	}

	static int countChars (String searchString, char query) {
		/*
			a. set total to 0
			b. for every char in searchString
				1. get char at current index
				2. if char is equal to query
					add 1 to total

		*/

		if (query == current_char) {
			total = total + 1;
		}

		return total?????
	}

	public static void main(String[] args) {
		printmsg("Hey!");
		stars(20);

		Scanner input_scanner = new Scanner(System.in);
		System.out.print("Enter a string: ");
		String user_str = input_scanner.next();

		System.out.print("Enter a character:");
		String char_str = input_scanner.next();
		char input_char = char_str.charAt(0);

		//Ready to call the countChars method...
		int result = countChars(user_str, input_char);
		
	}





}
// apr_13.java

class apr_13 {

	// A method definition that can be called from "main"
	
	// MODIFIERS - RETURN_TYPE - NAME - PARAMETERS
	static void printMessage() {
		System.out.println("I'm a function, or a subroutine, or a method...");
	}

	static void printMessage(String msg) {
		System.out.println(msg);	
	}

	static int countUp(int limit) {
		int count = 0;
		for (int i = 0; i < limit; i++) {
			count = count + i;
		}
		return count;
	}

	// Main execution begins here:
	public static void main(String[] args) {
		printMessage();
		printMessage("55");	
		int c = countUp(5);
		System.out.println( c );

		String s = "Hello World";
		System.out.println( s.charAt(0) );

	}

}
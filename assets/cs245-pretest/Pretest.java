import java.util.Scanner;

/**
 *  v.20160818
 *  This class contains only STATIC methods. Each method below executes a 
 * 	a basic aspect of programming (loops, conditionals, arrays, variables, 
 *	simple math computations, etc.). Your task is to implement each method
 *	below as indicated in the comments. You will use another file 
 *	(e.g., PretestApp.java) to run and test your method implementations.
 */
class Pretest {

    /**
     * Prompts the user for their name. This method should use a Scanner object
     * to retrieve the name. It shoud return the collected string.
     */
	static String getFirstName() {
        Scanner scnr = new Scanner(System.in);
        System.out.print("Enter your first name please: ");
        String name = scnr.next();
		return name;
	}


    /**
     * Accepts a list of integers as an argument and prints the integers to 
     * the screen on one line.
     */	
	static void printIntegerList(int[] values) {

	}


    /**
     * Accepts a list of integers as an argument and prints the integers IN REVERSE 
     * ORDER to the screen on one line.
     */	
	static void printIntegerListReversed(int[] values) {

	}



    /**
     * Accepts a list of integers as an argument and swaps the first value 
     * with the last value in the list. This method return
     * swapped version of the array that was passed in as the argument.
     */	
	static int[] swapFirstWithLast(int[] values) {

		return values;
	}

    /**
     * Accepts a list of integers as an argument and returns the smallest value
     * found in the list.
     */	
	static int min(int[] values) {

		return 0;
	}

    /**
     * Accepts a list of integers as an argument and returns the largest value
     * found in the list.
     */	
	static int max(int[] values) {
        int max = values[0];

        for (int index=1; index < values.length; index++) {

            if (values[index] > max) {
                max = values[index];
            }

            // System.out.print(values[index]);
        }

		return max;
	}

    /**
     * Accepts a list of integers as an argument and returns the average of all the
     * values found in the list.
     */	
	static int findAverage(int[] values) {
        int sum = 0;
        for (int i = 0; i < values.length; i++) {
            sum = sum + values[i];
        }
        
        int avg = sum/values.length;
		return avg;
	}

    /**
     * Accepts a list of integers and an integer value as arguments and returns 
     * the number of times the integer is found in the list.
     */	
	static int frequencyCount(int[] values, int val) {
        int count  = 0;
        for(int i = 0; i < values.length; i++) {
            if(val == values[i]) {
                count++;
            }
        }
		return count;
	}

    /**
     * Accepts a String argument and returns the argument in reverse order.
     */	
	static String reverseString(String chars) {
        char[] revchars = chars.toCharArray();
        String revstr = "";
        for(int i=revchars.length-1; i > -1; i--) {
            revstr += revchars[i];
        }
		return revstr;
	}
}












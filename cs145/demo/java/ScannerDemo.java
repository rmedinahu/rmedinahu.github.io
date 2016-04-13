import java.util.Scanner;  // Make the Scanner class available.

public class ScannerDemo {
   
   public static void main(String[] args) {
      
      Scanner stdin = new Scanner( System.in );  // Create the Scanner.
      System.out.print("Enter your name: ");
      String name = stdin.next();
      System.out.println("hello " + name);
      
   } // end of main()
   
} // end of class Interest2With Scanner

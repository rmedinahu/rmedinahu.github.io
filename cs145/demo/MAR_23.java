
// mar-23-java-00.java

class MAR_23 {
	
	public static void main(String[] args) {
		System.out.println("Hello World");

		int a = 89;
		int b = 900;
		int c = 89 + 900;
		System.out.println(c);
	
		int count = 1;
		while(count <= 10) {
			if (count % 2 == 0) {
				System.out.println("Count" + count);
			}
			
			count = count + 1;
		}
	}
}
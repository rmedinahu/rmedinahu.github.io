class apr_6 {
	public static void main(String[] args) {
		// Main thread...
		int snake = 0; // Reserving a memory location
		int dog = 9;

		if (snake < 10) {
			snake = snake - 1;
			dog++;
			System.out.println("DOG==>" + dog);
		}

		int limit = 20;
		int index = 0;
		while (index < limit) {
			index++;
			dog++;
		}
		System.out.println("LAST dog: " + dog);

	}
}
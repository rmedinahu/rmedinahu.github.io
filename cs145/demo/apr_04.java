class apr_04 {

	public static void main(String[] args) {

		/*
		Arrays have a size (or length) and a type
		*/
		
		int[] nums = new int[10];

		// SEQUENTIAL ACCESS TO ARRAYS ==> for loops!
		for (int i = 0; i < nums.length; i++) {
			nums[i] = (int)(Math.random()*20) + 1;
		}

		// RANDOM ACCESS INTO ARRAYS
		// Get the 2nd item in the array:

		System.out.println(nums[1]);


		int max;  			// The largest number seen so far.
		max = nums[0];   	// At first, the largest number seen is nums[0].
		
		int i;
		for ( i = 1; i < nums.length; i++ ) {
		    if (nums[i] > max) {
		       max = nums[i];
		    }
		}
		// at this point, max is the largest item in nums
	}

}
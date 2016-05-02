class may_2 {
	
	static int[] nums = {1, 2, 3, 4};

	public static void main(String[] args) {
		Gradebook g = new Gradebook();
		g.flipEnds(nums);
		System.out.println(nums);
		for(int i = 0; i < nums.length; i++) {
			System.out.print(nums[i] + ", ");
		}

		int x = 4;
		g.passByValue(x);
		System.out.println(x);
	}
}

class Gradebook {

	public void flipEnds(int[] values) {
		System.out.println(values);
		int last_index = values.length-1;
		int tmp = values[0];
		values[0] = values[last_index];
		values[last_index] = tmp;


	}

	public void passByValue(int x) {
		x = x * x;
		System.out.println(x);
	}

	public void printArray(int[] values) {
		for(int i = 0; i < values.length; i++) {
			System.out.print(values[i] + ", ");
		}
	}

}
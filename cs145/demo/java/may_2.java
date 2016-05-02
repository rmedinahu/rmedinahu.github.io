class may_2 {
	
	static int[] nums = {5, 10, 15, 20};

	public static void main(String[] args) {
		DemoClass demo_object = new DemoClass();
		demo_object.flipEnds(nums);
		System.out.println(nums);
		for(int i = 0; i < nums.length; i++) {
			System.out.print(nums[i] + ", ");
		}

		int x = 4;
		demo_object.passByValueSquared(x);
		System.out.println(x);
	}
}

class DemoClass {

	public void flipEnds(int[] values) {
		System.out.println(values);
		int last_index = values.length-1;
		int tmp = values[0];
		values[0] = values[last_index];
		values[last_index] = tmp;


	}

	public void passByValueSquared(int x) {
		x = x * x;
		System.out.println(x);
	}

	public void printArray(int[] values) {
		for(int i = 0; i < values.length; i++) {
			System.out.print(values[i] + ", ");
		}
	}

}
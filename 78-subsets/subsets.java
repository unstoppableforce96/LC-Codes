class Solution {
    public static void generate(int index, int[] nums, List<Integer> current,
        List<List<Integer>> result) {
            if (index == nums.length) {
                result.add(new ArrayList<>(current));
                return;
            }
            current.add(nums[index]);
            generate(index + 1, nums, current, result); // pick

            current.remove(current.size() - 1); // backtrack (undo)

            generate(index + 1, nums, current, result); // non pick
    }
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        generate(0, nums, current, result);    
        return result;
    }
}
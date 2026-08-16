class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i: arr) {
            if (map.containsKey(i)) {
                map.put(i, map.get(i) + 1);
            } else {
                map.put(i, 1);
            }
        }
        HashMap<Integer, Integer> map1 = new HashMap<>();
        for (Integer val: map.values()) {
            if (map1.containsKey(val)) {
                map1.put(val, map1.get(val) + 1);
            } else {
                map1.put(val, 1);
            }
        }
        System.out.println(map);
        System.out.println(map.values());
        System.out.println(map1);
        for (Integer val: map1.values()) {
            if (val != 1) {
                return false;
            }
        }
        return true;
    }
}
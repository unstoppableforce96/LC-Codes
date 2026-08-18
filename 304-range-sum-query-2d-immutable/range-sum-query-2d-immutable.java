class NumMatrix {
    int[][] matrix;
    int[][] prefix;
    public NumMatrix(int[][] matrix) {
        this.matrix = matrix;
        int rows = matrix.length;
        int cols = matrix[0].length;
        this.prefix = new int[rows + 1][cols + 1];
        // Building prefix arrays
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int top = prefix[i][j + 1];
                int left = prefix[i + 1][j];
                int overlap = prefix[i][j];
                int current = matrix[i][j];
                prefix[i + 1][j + 1] = top + left - overlap + current;
            }
        }
        // System.out.println(Arrays.deepToString(prefix));
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int whole = this.prefix[row2 + 1][col2 + 1];
        int topRemove = this.prefix[row1][col2 + 1];
        int leftRemove = this.prefix[row2 + 1][col1];
        int overlap = this.prefix[row1][col1];
        return whole - topRemove - leftRemove + overlap;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
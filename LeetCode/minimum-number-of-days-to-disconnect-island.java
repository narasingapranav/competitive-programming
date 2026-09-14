class Solution {
    private int[] rowDir = {-1, 0, 1, 0};
    private int[] colDir = {0, 1, 0, -1};
    private boolean isValidCell(int r, int c, int rows, int cols) {
        return r >= 0 && c >= 0 && r < rows && c < cols;
    }
    private void DFS(int r, int c, int[][] matrix, boolean[][] visited) {
        visited[r][c] = true;
        for (int d = 0; d < 4; d++) {
            int newRow = r + rowDir[d];
            int newCol = c + colDir[d];
            if (isValidCell(newRow, newCol, matrix.length, matrix[0].length)
                    && matrix[newRow][newCol] == 1
                    && !visited[newRow][newCol]) {

                DFS(newRow, newCol, matrix, visited);
            }
        }
    }
    private int countComponents(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int islandCount = 0;
        boolean[][] visited = new boolean[rows][cols];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {

                if (matrix[r][c] == 1 && !visited[r][c]) {
                    islandCount++;
                    DFS(r, c, matrix, visited);
                }
            }
        }
        return islandCount;
    }
    public int minDays(int[][] grid) {
        if (countComponents(grid) != 1)
            return 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == 1) {

                    grid[r][c] = 0;

                    if (countComponents(grid) != 1)
                        return 1;

                    grid[r][c] = 1;
                }
            }
        }
        return 2;
    }
}
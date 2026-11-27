import java.util.*;
public class IsValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        

        for (char[] row : board) {
            Map<Character, Integer> check = new HashMap<>();
            for (char c : row) {
                if (c == '.') {continue;}
                else {
                    if (check.containsKey(c)) {return false;}
                    else {
                        check.put(c, 1);
                    }
                }
            }
        }

        for (int r = 0; r < 9; r++) {
            Map<Character, Integer> check = new HashMap<>();
            for (int c = 0; c < 9; c++) {
                if (board[c][r] == '.') {continue;}
                else {
                    if (check.containsKey(board[c][r])) {return false;}
                    else {
                        check.put(board[c][r], 1);
                    }
                }
            }
        }
        for (int startRow = 0; startRow < 9; startRow += 3) {
            for (int startCol = 0; startCol < 9; startCol += 3) {
                Map<Character, Integer> check = new HashMap<>();
                for (int i = 0; i<3; i++) {
                    for (int j = 0; j<3; j++) {
                        if (board[startRow + i][startCol + j] == '.') {continue;}
                        else {
                            if (check.containsKey(board[startRow + i][startCol + j])) {return  false;}
                            else {
                                check.put(board[startRow + i][startCol + j], 1);
                            }
                        }
                    }
                }
            }
        }

        return true;


    }

    public static void main(String[] args) {
        var sol = new IsValidSudoku();
        char[][] board = {
            {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
            {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
            {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
            {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
            {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
            {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
            {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
            {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
            {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };
        var res = sol.isValidSudoku(board);
        System.out.println(res);
    }
}

# NQueen-
Solving NQueen problem using backtracking
CONSTRAINS TO TRACK
-A queen cannot share a column,row and a diagonal with other queen
BACKTRACKING
-Start with row 0
-From each column in a row
skip if column,row and diagonal is occupied
place queen,mark constarins
remove queen,and unmark constrains
-If all rows filled ,record solution
TIME COMPLEXITY:O(n)

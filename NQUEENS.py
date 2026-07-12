def print_board(board, n):
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i] == j:
                row += " Q "
            else:
                row += " . "
        print(row)
    print()


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, n):
    if row == n:
        print(" Solution found:")
        print_board(board, n)
        return True

    res = False
    for col in range(n):
        print(f"Trying to place queen at row {row}, col {col}...")
        if is_safe(board, row, col):
            print(f" Safe! Placing queen at row {row}, col {col}")
            board[row] = col
            res = solve_nqueens(board, row + 1, n) or res
            print(f"Backtracking from row {row}, col {col}")
        else:
            print(f" Conflict at row {row}, col {col}, skipping...")
    return res


def menu():
    while True:
        print("\n--- N Queens Problem ---")
        print("1. Solve N Queens")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter value of N: "))
            board = [-1] * n
            print(f"\nSolving {n}-Queens...\n")
            if not solve_nqueens(board, 0, n):
                print(f"No solution exists for N = {n}")
        elif choice == "2":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

menu()

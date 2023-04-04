class PieceMovement:
    def __init__(self):
        pass

    
    def is_pawn_move_legal(self, start_row, start_col, end_row, end_col, is_white):
        # Pawn can only move forward by one square
        if (end_col == start_col) and ((end_row == start_row + 1) if is_white else (end_row == start_row - 1)):
            return True
        # Pawn can move forward by two squares on its first move
        if (end_col == start_col) and ((end_row == start_row + 2) if is_white else (end_row == start_row - 2)):
            if start_row == (1 if is_white else 6):
                return True
        # Pawn can capture diagonally
        if abs(end_col - start_col) == 1 and ((end_row == start_row + 1) if is_white else (end_row == start_row - 1)):
            return True
        # Otherwise, the move is illegal
        return False


pm = PieceMovement()

# Test a legal pawn move
print(pm.is_pawn_move_legal(1, 1, 2, 0, True))


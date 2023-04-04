from tkinter import *


class ChessBoardController:
    def __init__(self, canvas, board):
        self.canvas = canvas
        self.board = board
        self.selected_piece_id = None
        self.selected_piece_pos = None
        self.canvas.tag_bind("piece", "<ButtonPress-1>", self.on_piece_click)
        self.canvas.tag_bind("piece", "<B1-Motion>", self.on_piece_drag)
        self.canvas.tag_bind("piece", "<ButtonRelease-1>", self.on_piece_release)

    def on_piece_click(self, event):
        self.selected_piece_id = event.widget.find_closest(event.x, event.y)[0]
        self.selected_piece_pos = tuple(map(int, self.canvas.gettags(self.selected_piece_id)[1].split(',')))
        self.canvas.scale(self.selected_piece_id, 0, 0, 1.2, 1.2)

    def on_piece_drag(self, event):
        x, y = event.x, event.y
        self.canvas.coords(self.selected_piece_id,
                            x - SQUARE_SIZE // 2, y - SQUARE_SIZE // 2,
                            x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2)

    def on_piece_release(self, event):
        r, c = self.selected_piece_pos
        x, y = event.x, event.y
        new_r, new_c = y // SQUARE_SIZE, x // SQUARE_SIZE
        if (new_r, new_c) in get_valid_moves(self.board, r, c):
            self.board[new_r][new_c] = self.board[r][c]
            self.board[r][c] = None
            self.canvas.coords(self.selected_piece_id,
                                new_c * SQUARE_SIZE, new_r * SQUARE_SIZE,
                                (new_c + 1) * SQUARE_SIZE, (new_r + 1) * SQUARE_SIZE)
        else:
            self.canvas.coords(self.selected_piece_id,
                                c * SQUARE_SIZE, r * SQUARE_SIZE,
                                (c + 1) * SQUARE_SIZE, (r + 1) * SQUARE_SIZE)
        self.canvas.scale(self.selected_piece_id, 0, 0, 1/1.2, 1/1.2)
        self.selected_piece_id = None
        self.selected_piece_pos = None

from tkinter import *

# Create the canvas
canvas = Canvas(width=500, height=500)
canvas.pack()
# Draw the chess board
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            color = "white"
        else:
            color = "gray"
        canvas.create_rectangle(col * 50, row * 50, (col + 1) * 50, (row + 1) * 50, fill=color)

# Define the event handlers
selected_piece = None

def handle_mouse_click(event):
    global selected_piece
    if selected_piece:
        canvas.itemconfig(selected_piece, outline="", width=1)
    piece = canvas.find_withtag(CURRENT)
    canvas.itemconfig(piece, outline="red", width=2)
    canvas.tag_raise(piece)
    selected_piece = piece

def handle_mouse_drag(event):
    x, y = event.x, event.y
    piece = canvas.find_withtag(CURRENT)
    canvas.coords(piece, x-25, y-25, x+25, y+25)

def handle_mouse_release(event):
    global selected_piece
    piece = canvas.find_withtag(CURRENT)
    col = int(canvas.coords(piece)[0] / 50)
    row = int(canvas.coords(piece)[1] / 50)
    x = col * 50 + 25
    y = row * 50 + 25
    canvas.coords(piece, x-25, y-25, x+25, y+25)
    canvas.itemconfig(piece, outline="", width=1)
    selected_piece = None

# Bind the mouse events to the canvas
canvas.tag_bind("piece", "<Button-1>", handle_mouse_click)
canvas.tag_bind("piece", "<B1-Motion>", handle_mouse_drag)
canvas.tag_bind("piece", "<ButtonRelease-1>", handle_mouse_release)

# Add the chess pieces to the canvas and tag them with "piece"
pieces = []

for i in range(8):
    piece = canvas.create_oval(i * 50 + 5, 1 * 50 + 5, (i + 1) * 50 - 5, 2 * 50 - 5, fill="black", tags="piece")
    pieces.append(piece)
    canvas.create_oval(i * 50 + 5, 6 * 50 + 5, (i + 1) * 50 - 5, 7 * 50 - 5, fill="white", tags="piece")


# Start the main event loop
mainloop()

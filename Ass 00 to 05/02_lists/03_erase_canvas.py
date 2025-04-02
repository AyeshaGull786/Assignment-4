# 03_erase_canvas

# Problem Statement
# Implement an 'eraser' on a canvas.
# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen.
# We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

# Canvas size
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 50  # Size of each grid cell

class EraserCanvas:  
    def __init__(self, root):  
        # Constructor method (__init__) is automatically called when an object of this class is created.
        # It initializes the main window and sets up the canvas.
        # Parameters:
        # root (Tk): The main Tkinter window that will hold the canvas.
        # 'self' refers to the instance of the class, allowing access to its attributes and methods.
        
        self.root = root  # Store the root window reference inside the class.
        self.root.title("Eraser on Canvas")           # Set the title of the window to "Eraser on Canvas"


        # Create a canvas widget inside the root window
                         #Creates a canvas (a drawable area) inside root, width=WIDTH, height=HEIGHT: Sets the canvas size,  bg="white": Sets the background color to white.
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        
        #places the canvas inside the window using the pack() layout manager. Ensures it appears when the program runs.
        self.canvas.pack()

        # Draw grid of blue squares
        self.cells = []         # List to store all cell (square) objects  
        for row in range(0, WIDTH, CELL_SIZE):              # Loop through rows with step size CELL_SIZE  
            for col in range(0, HEIGHT, CELL_SIZE):            # Loop through columns with step size CELL_SIZE 
                cell = self.canvas.create_rectangle(row, col, row + CELL_SIZE, col + CELL_SIZE, fill="blue", outline="black")   # Create a blue rectangle (cell) at (row, col) position  
                self.cells.append(cell)                # Store the created cell in the list  

        # Bind mouse drag event to eraser
        self.canvas.bind("<B1-Motion>", self.erase)

    def erase(self, event):
        """ Erases cells by turning them white when dragged over them. """
        x, y = event.x, event.y
        overlapping = self.canvas.find_overlapping(x, y, x + 1, y + 1)  # Find objects under cursor
        for item in overlapping:
            self.canvas.itemconfig(item, fill="white")  # Change color to white

# Run the application
root = tk.Tk()
app = EraserCanvas(root)
root.mainloop()

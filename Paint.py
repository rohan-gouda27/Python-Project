import tkinter as tk
from tkinter import colorchooser, filedialog

def draw(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

def choose_color():
    global color
    color = colorchooser.askcolor(color=color)[1]

def clear_canvas():
    canvas.delete("all")

def change_brush_size(size):
    global brush_size
    brush_size = size

def save_canvas():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if file_path:
        canvas.postscript(file=file_path + ".eps")

def use_eraser():
    global color
    color = "white"

def shortcut_handler(event):
    if event.keysym == "c":
        choose_color()
    elif event.keysym == "e":
        use_eraser()
    elif event.keysym == "s":
        save_canvas()
    elif event.keysym == "x":
        clear_canvas()

# Initialize main window
root = tk.Tk()
root.title("Advanced Paint App")
root.geometry("700x500")
root.configure(bg="#f0f0f0")

color = "black"  # Default color
brush_size = 2  # Default brush size
canvas = tk.Canvas(root, bg="white", width=600, height=400, relief=tk.SUNKEN, borderwidth=2)
canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas.bind("<B1-Motion>", draw)  # Bind left mouse drag to draw
root.bind("<KeyPress>", shortcut_handler)  # Bind keyboard shortcuts

# Toolbar
toolbar = tk.Frame(root, bg="#d9d9d9", padx=5, pady=5)
toolbar.pack(fill=tk.X)

btn_color = tk.Button(toolbar, text="🎨 Color (C)", command=choose_color, bg="lightgray")
btn_color.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(toolbar, text="🗑 Clear (X)", command=clear_canvas, bg="lightgray")
btn_clear.pack(side=tk.LEFT, padx=5)

btn_save = tk.Button(toolbar, text="💾 Save (S)", command=save_canvas, bg="lightgray")
btn_save.pack(side=tk.LEFT, padx=5)

btn_eraser = tk.Button(toolbar, text="🧼 Eraser (E)", command=use_eraser, bg="lightgray")
btn_eraser.pack(side=tk.LEFT, padx=5)

brush_size_frame = tk.Frame(toolbar, bg="#d9d9d9")
brush_size_frame.pack(side=tk.RIGHT)

sizes = [2, 5, 10, 20]
for size in sizes:
    btn = tk.Button(brush_size_frame, text=f"⚫ {size}", command=lambda s=size: change_brush_size(s), bg="lightgray")
    btn.pack(side=tk.LEFT, padx=2)

root.mainloop()
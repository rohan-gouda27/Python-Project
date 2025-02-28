import tkinter as tk
from tkinter import filedialog, colorchooser, font, messagebox, simpledialog


class WordPad:
    def __init__(self, root):
        self.root = root
        self.root.title("WordPad")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill="both")

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        self.file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X",
                                   command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C",
                                   command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V",
                                   command=lambda: self.text_area.event_generate("<<Paste>>"))
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z",
                                   command=lambda: self.text_area.event_generate("<<Undo>>"))
        self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y",
                                   command=lambda: self.text_area.event_generate("<<Redo>>"))
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.format_menu.add_command(label="Font", command=self.choose_font)
        self.format_menu.add_command(label="Text Color", command=self.choose_color)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)

        self.root.bind_all("<Control-n>", lambda event: self.new_file())
        self.root.bind_all("<Control-o>", lambda event: self.open_file())
        self.root.bind_all("<Control-s>", lambda event: self.save_file())
        self.root.bind_all("<Control-q>", lambda event: self.root.quit())
        self.root.bind_all("<Control-x>", lambda event: self.text_area.event_generate("<<Cut>>"))
        self.root.bind_all("<Control-c>", lambda event: self.text_area.event_generate("<<Copy>>"))
        self.root.bind_all("<Control-v>", lambda event: self.text_area.event_generate("<<Paste>>"))
        self.root.bind_all("<Control-z>", lambda event: self.text_area.event_generate("<<Undo>>"))
        self.root.bind_all("<Control-y>", lambda event: self.text_area.event_generate("<<Redo>>"))

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def save_as_file(self):
        self.save_file()

    def choose_font(self):
        font_family = simpledialog.askstring("Font", "Enter font family (e.g., Arial, Times New Roman):")
        font_size = simpledialog.askinteger("Font Size", "Enter font size:")
        if font_family and font_size:
            self.text_area.configure(font=(font_family, font_size))

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.configure(fg=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = WordPad(root)
    root.mainloop()

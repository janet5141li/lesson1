from tkinter import *

if __name__ == "__main__":
    root = Tk();
    root.title("new window");
    Label(root, text = "This is the main topLevel").pack(pady=10,padx = 100);
    root.mainloop();
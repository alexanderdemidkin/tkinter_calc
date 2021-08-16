from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style
import frame


def main():
    mem = []
    i = 0
    root = Tk()
    app = frame.Example(root,mem)

    root.mainloop()


if __name__ == '__main__':
    main()
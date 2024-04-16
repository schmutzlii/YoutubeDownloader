import tkinter as tk
import os
from pathlib import Path
from tkinter import ttk
from download import Downloader
from gui import GUI


PATH_SAVE = os.path.join(Path.home(), "Downloads")
EXTENSION = ".wav"

def main():
    root = tk.Tk()
    root.title("YouTube Downloader")
    downloader = Downloader(PATH_SAVE, EXTENSION)
    gui = GUI(root, downloader)

    root.mainloop()

if __name__ == "__main__":
    main()

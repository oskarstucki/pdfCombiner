from PyPDF2 import PdfFileMerger


def read_files(file_path=None):
    try:
        if file_path is None:

            import tkinter as tk
            from tkinter import filedialog

            root = tk.Tk()
            root.withdraw()

            return filedialog.askopenfilenames()

    except FileNotFoundError:
        print("File couldn't be found")
        return 0


files_array = read_files()

merger = PdfFileMerger()

for pdf in files_array:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()

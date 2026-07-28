import sys
from tkinterdnd2 import TkinterDnD
from gui import HDRConverterGUI
from utils import setup_dpi_awareness

if __name__ == "__main__":
    setup_dpi_awareness()
    root = TkinterDnD.Tk()
    root.withdraw()
    _gui = HDRConverterGUI(root)
    root.deiconify()
    root.mainloop()

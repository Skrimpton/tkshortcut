import sys
try:    import tkinter as tk
except: print("no tkinter :("),sys.exit(1)
else:   from MainWindow import MainWindow
# --------------------------------------------------------------------------
#                                                  MAKE AND SPAWN NEW WINDOW
if __name__ == "__main__":

    app             = MainWindow()
    app.show()

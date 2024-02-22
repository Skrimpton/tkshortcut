#!/bin/env python3

import sys

def error_exit(module=""):
    if module == "":
        module = "A"

    print(f":: IMPORT ERROR :: in {__file__}\n{module} is not installed")
    sys.exit(1)

try:
    import importlib
except:
    error_exit("'importlib'")

# Check rquirements
c_tk        = importlib.util.find_spec('tkinter')
c_signal    = importlib.util.find_spec('signal')

if c_tk == None:
    error_exit("'tkinter'")
elif c_signal == None:
    error_exit("'signal'")
else:
    # import signal
    from MainWindow import MainWindow


# --------------------------------------------------------------------------
#                                                          HANDLE <CTRL + C>
# def keyboard_interrupt_handler(sig, frame):
#     print(':: MAIN :: You pressed Ctrl+C!',"Exiting...")
#     sys.exit(0)

# --------------------------------------------------------------------------
#                                                  MAKE AND SPAWN NEW WINDOW


if __name__ == "__main__":

    # signal.signal(
    #     signal.SIGINT,
    #     keyboard_interrupt_handler
    # );

    app             = MainWindow()
    # app.self_ref    = app
    app.show()

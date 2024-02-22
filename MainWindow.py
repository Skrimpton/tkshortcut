#!/bin/env python

import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import filedialog as fd
import os,sys, signal
from TweakedEntry import CEntry as TweakedEntry
from Styler import  Styler

# HIGHLIGHTBACKGROUND     =
def keyboard_interrupt_handler(sig, frame):
    print(":: WINDOW :: You pressed Ctrl+C! Exiting...")
    if __name__ == "__main__":
        app.quit()
    else:
        MainWindow().quit()
    sys.exit(0)

class MainWindow:

    signal.signal(
        signal.SIGINT,
        keyboard_interrupt_handler
    );
    def __init__(self): #                   ### BEGIN ###

        self.ctrl_c_timer                   = None

        # --- Set root
        self.root                           = tk.Tk()
        self.styler                         = Styler(self.root) # comment out this to remove styling
        self.root.title                     ("Create Desktop Shortcut")

        # --- Hook up x-button to quit-function. Not needed, but maybe a nifty snippet.
        self.root.protocol                  ( "WM_DELETE_WINDOW", self.quit );
        # ---
        self.declareUi                      ()
        self.do_geometry_management         ()

    # ------------------------------------------------------------------------------
    #                                                         Construction functions
    def declareUi(self):
        self.main_frame =                   ttk.Frame(self.root)
        self.titleframe =                   ttk.Frame(self.main_frame)
        # self.titleframe.columnconfigure     (0, weight=0)
        self.titleframe.columnconfigure     (1, weight=1)

        self.buttonframe                    = ttk.Frame(self.main_frame)
        self.buttonframe.columnconfigure    (0, weight=1)
        self.buttonframe.columnconfigure    (1, weight=1)

        self.frame                          = ttk.Frame(self.main_frame)
        # self.frame.columnconfigure          (0, weight=0)
        self.frame.columnconfigure          (1, weight=1)
        # self.frame.columnconfigure          (2, weight=0)
        self.namelabel                      = ttk.Label     (   self.titleframe, text = "Title:",justify='left')
        self.nametext                       = TweakedEntry  (   self.titleframe,font=('Arial',10))


        self.filenamelabel                  = ttk.Label     (   self.frame, text = "Filename *:",justify='left')
        self.filenametext                   = TweakedEntry  (   self.frame,font=('Arial',10),enabled=False)
        self.filenametext.bind              ('<<FieldChanged>>',self.on_changes_name)

        # self.filenametext.insert            (0, )
        self.choose_filename_button         = ttk.Button    (   self.frame, text = "Choose",
                                                                command    = self.choose_filename
                                            );

        self.execlabel                      = ttk.Label     (   self.frame, text = "Path to Executable *:",justify='left')
        self.exectext                       = TweakedEntry  (   self.frame,font=('Arial',10))
        self.exectext.bind                  ('<<FieldChanged>>',self.on_changes_exec)
        # self.exectext.insert                (0, "Path to Executable")

        self.iconlabel                      = ttk.Label     (   self.frame, text = "Icon:")
        self.icontext                       = TweakedEntry  (   self.frame,font=('Arial',10))
        self.choose_icon_button             = ttk.Button    (   self.frame, text="Choose",
                                                                command = self.choose_icon
                                            );

        self.choosebutton                   = ttk.Button    (   self.frame, text="Choose",
                                                                command = self.choose_file
                                            );


        self.okbutton                       = ttk.Button    (   self.buttonframe, text="Ok",state='disabled',
                                                                command = self.click_ok
                                            );
        self.cancelbutton                   = ttk.Button    (   self.buttonframe, text="Cancel",
                                                                command = self.quit
                                            );

    def on_changes_exec(self,event=None): # event info of no value

        if os.path.isfile(self.exectext.entry_text.get()):
            self.filenametext.configure(state='enabled')
        else:
            self.filenametext.configure(state='disabled')

    def on_changes_name(self,event=None): # event info of no value
        if self.filenametext.entry_text.get() != "":
            self.okbutton.configure(state='enabled')
        else:
            self.okbutton.configure(state='disabled')


    def do_geometry_management(self):
        # --- GRID
        self.namelabel.grid                 (row=0, column=0,sticky="we",           pady=3)
        self.nametext.grid                  (row=0, column=1,sticky="we",   padx=3, pady=3)

        self.filenamelabel.grid             (row=0, column=0,sticky="we")
        self.filenametext.grid              (row=0, column=1,columnspan=2,sticky="we",
                                                                            padx=3)
        # self.choose_filename_button.grid    (row=0, column=2)

        self.execlabel.grid                 (row=1, column=0,sticky="we",           pady=1)
        self.exectext.grid                  (row=1, column=1,sticky="we",   padx=3, pady=1)
        self.choosebutton.grid              (row=1, column=2,               padx=3, pady=1)

        self.iconlabel.grid                 (row=2, column=0,sticky="we")
        self.icontext.grid                  (row=2, column=1,sticky="we",   padx=3)
        self.choose_icon_button.grid        (row=2, column=2,               padx=3)

        self.okbutton.grid                  (row=0, column=0,sticky="we")
        self.cancelbutton.grid              (row=0, column=1,sticky="we")

        # --- PACK
        self.main_frame.pack                (fill='both',expand=1)
        self.titleframe.pack                (fill="x")
        self.frame.pack                     (fill="x",pady=5)
        self.buttonframe.pack               (fill="x",side='bottom')

    # ------------------------------------------------------------------------------
    #                                                           Functional functions
    def quit(self):
        print("Doin' some cleaning up...")
        self.root.destroy()
        print("All done!")

    def click_ok(self):
        filename                            = self.filenametext.get()
        if os.path.exists(self.exectext.get()):
            parent_dir_of_executable            = os.path.dirname(os.path.realpath(self.exectext.get()))
        if filename != "":
            filename = os.path.join(parent_dir_of_executable,f"{filename}.desktop")
            try:
                with open(filename, "w") as my_file:

                    my_file.write               ("[Desktop Entry]\n")
                    my_file.write               ("Name=" + self.nametext.get() + "\n")
                    my_file.write               ("Exec=" + self.exectext.get() + "\n")
                    my_file.write               ("Icon=" + self.icontext.get() + "\n")
                # self.after(10,lambda e: messagebox.shoinfo(message="Shortcut Created"))
                messagebox.showinfo(title="Desktop-file creator:",
                                    message="Shortcut Created")
                self.root.destroy               ()
            except:
                self.after(10,lambda e: messagebox.showerror(title="Desktop-file creator:",
                                     message="SHORTCUT WAS NOT CREATED")
                );


            # # file.close                        ()

    def choose_file(self):
        self.exectext.delete                (0, tk.END)
        self.exectext.insert                (0, fd.askopenfilename())
        # self.exectext.entry_text.set(fd.askopenfilename())

    def choose_filename(self):
        self.filenametext.delete            (0, tk.END)
        # self.filenametext.insert            (0, fd.askdirectory())
        self.filenametext.insert            (0, fd.askopenfilename())

    def choose_icon(self):
        self.icontext.delete                (0, tk.END)
        self.icontext.insert                (0, fd.askopenfilename())

    def show(self):
        self.toggleCtrlCTimer               ()
        self.root.mainloop                  ()


    # --- ### INFINTE LOOP ### ---------------------------------------------------------------------------------
    # DECLARE AND START THE TIMER THAT LETS < CTRL + C > IN THE TERMINAL CLOSE THE WINDOW
    #
    def startCtrlCTimer(self): # <⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅    START "KEEP ACTIVE"-TIMER ON/OFF
                                                      #         I LIKE TO KEEP A 'self.'-REFERENCE OF '.after()'
        self.ctrl_c_timer = self.root.after (         #     THIS WAY WE CAN STOP THE TIMER AND AVOID ERRORS LIKE
            80,self.startCtrlCTimer                   #   "NO COMMAND FOUND", IF TIMER FIRES AFTER / WHILE DOING
        );                                            #                                    'self.root.destroy()'


    def toggleCtrlCTimer(self): # <⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅  TOGGLE "KEEP ACTIVE"-TIMER ON/OFF
        if self.ctrl_c_timer is None:
            self.startCtrlCTimer            ()

        else:
            self.root.after_cancel          (self.ctrl_c_timer)
            self.ctrl_c_timer               = None



if __name__ == "__main__":

    app = MainWindow()
    app.show()

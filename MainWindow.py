#!/bin/env python

import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import filedialog as fd
import os,sys, signal
from TweakedEntry import CEntry as TweakedEntry
from Styler import  Styler

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
        self.passed_file                    = None
        self.ctrl_c_timer                   = None
        self.style_toggled                  = False
        # --- Set root
        self.root                           = tk.Tk()
        self.styler                         = Styler(self.root) # comment out this to remove styling
        self.root.title                     ("Create Desktop Shortcut")
        self.root.minsize                   (300,180)
        # --- Hook up x-button to quit-function. Not needed, but maybe a nifty snippet.
        self.root.protocol                  ( "WM_DELETE_WINDOW", self.quit );
        # ---
        self.declareUi                      ()
        self.do_geometry_management         ()
        self.root.bind                  ('<Alt-Shift-C>',self.toggle_style)
    # ------------------------------------------------------------------------------
    #                                                         Construction functions
    def declareUi(self):
        if self.passed_file == None:
            self.main_frame                     = ttk.Frame     (   self.root)
            self.filenameframe                  = ttk.Frame     (   self.main_frame)
            self.buttonframe                    = ttk.Frame     (   self.main_frame)
            self.frame                          = ttk.Frame     (   self.main_frame)


            self.filenamelabel                  = ttk.Label     (   self.filenameframe, text = "Filename *:",justify='left',state='disabled')
            self.filenametext                   = TweakedEntry  (   self.filenameframe,font=('Arial',10),enabled=False)
            self.filenametext.bind              ('<<FieldChanged>>',self.on_changes_name)

            self.choose_filename_button         = ttk.Button    (   self.filenameframe, text = "Choose",
                                                                    command    = self.choose_filename
                                                );

            self.namelabel                      = ttk.Label     (   self.frame, text = "Title:",justify='left')
            self.nametext                       = TweakedEntry  (   self.frame,font=('Arial',10))


            self.outlabel                      = ttk.Label     (   self.frame, text = "Output dir:",justify='left')
            self.outtext                       = TweakedEntry  (   self.frame,font=('Arial',10))
            self.outtext.bind                  ('<<FieldChanged>>',self.on_changes_exec)
            self.btn_sel_out                   = ttk.Button    (   self.frame, text="Choose",
                                                                    command = self.choose_savepath
                                                );

            self.execlabel                      = ttk.Label     (   self.frame, text = "Path to Executable *:",justify='left')
            self.exectext                       = TweakedEntry  (   self.frame,font=('Arial',10))
            self.exectext.bind                  ('<<FieldChanged>>',self.on_changes_exec)
            self.btn_sel_exec                   = ttk.Button    (   self.frame, text="Choose",
                                                                    command = self.choose_file
                                                );

            self.iconlabel                      = ttk.Label     (   self.frame, text = "Icon:")
            self.icontext                       = TweakedEntry  (   self.frame,font=('Arial',10))
            self.choose_icon_button             = ttk.Button    (   self.frame, text="Choose",
                                                                    command = self.choose_icon
                                                );


        self.btn_ok                       = ttk.Button    (   self.buttonframe, text="Ok",state='disabled',
                                                                command = self.click_ok
                                            );
        self.cancelbutton                   = ttk.Button    (   self.buttonframe, text="Cancel",
                                                                command = self.quit
                                            );
        self.buildStylegroups()
    def buildStylegroups(self):
        for f in (  self.main_frame,
                    self.filenameframe,
                    self.buttonframe,
                    self.frame,
        ):
            self.styler.stylegroup_frames.append(f)

        for b in (  self.choose_icon_button,
                    self.btn_sel_out,
                    self.btn_sel_exec,
                    self.btn_ok,
                    self.cancelbutton,
                    self.choose_filename_button,
        ):
            self.styler.stylegroup_buttons.append(b)

        for e in (  self.filenametext,
                    self.nametext,
                    self.outtext,
                    self.exectext,
                    self.icontext,
        ):
            self.styler.stylegroup_entries.append(e)

        for l in (
            self.namelabel,
            self.outlabel,
            self.filenamelabel,
            self.execlabel,
            self.iconlabel,
        ):
            self.styler.stylegroup_labels.append(l)



    def toggle_style(self,_):
        self.style_toggled = not self.style_toggled

        if self.style_toggled:


            for f in self.styler.stylegroup_frames:
                f.configure(style='C.TFrame')

            for l in self.styler.stylegroup_labels:
                l.configure(style='C.TLabel')

            for e in self.styler.stylegroup_entries:
                e.configure(style='C.TEntry')

            for b in self.styler.stylegroup_buttons:
                b.configure(style='C.TButton')


        else:

            for f in self.styler.stylegroup_frames:
                f.configure(style='TFrame')

            for l in self.styler.stylegroup_labels:
                l.configure(style='TLabel')

            for e in self.styler.stylegroup_entries:
                e.configure(style='TEntry')

            for b in self.styler.stylegroup_buttons:
                b.configure(style='TButton')


    def do_geometry_management(self):

        # --- GRID
        self.filenameframe.columnconfigure  (1, weight=1)
        self.buttonframe.columnconfigure    (0, weight=1)
        self.buttonframe.columnconfigure    (1, weight=1)
        self.frame.columnconfigure          (1, weight=1)

        self.filenamelabel.grid             (row=0, column=0,sticky="we",           pady=3)
        self.filenametext.grid              (row=0, column=1,sticky="we",   padx=3, pady=3)

        self.execlabel.grid                 (row=0, column=0,sticky="we")
        self.exectext.grid                  (row=0, column=1,sticky="we",   padx=3)
        self.btn_sel_exec.grid              (row=0, column=2,               padx=3)

        self.outlabel.grid                  (row=1, column=0,sticky="we",           pady=1)
        self.outtext.grid                   (row=1, column=1,sticky="we",   padx=3, pady=1)
        self.btn_sel_out.grid               (row=1, column=2,               padx=3, pady=1)

        self.namelabel.grid                 (row=2, column=0,sticky="we",           pady=3)
        self.nametext.grid                  (row=2, column=1,sticky="we",   padx=3, pady=3, columnspan=2,)


        self.iconlabel.grid                 (row=3, column=0,sticky="we")
        self.icontext.grid                  (row=3, column=1,sticky="we",   padx=3)
        self.choose_icon_button.grid        (row=3, column=2,               padx=3)

        self.btn_ok.grid                    (row=0, column=0,sticky="we")
        self.cancelbutton.grid              (row=0, column=1,sticky="we")

        # --- PACK
        self.main_frame.pack                (fill='both',expand=1)
        self.filenameframe.pack             (fill="x")
        self.frame.pack                     (fill="x",pady=5)
        self.buttonframe.pack               (fill="x",side='bottom')

    # ------------------------------------------------------------------------------
    #                                                           Functional functions

    def on_changes_exec(self,event=None): # event info of no value

        if os.path.isfile(self.exectext.entry_text.get()):

            self.filenametext.configure     (state='enabled')
            self.filenamelabel.configure    (state='enabled')

            content                     = os.path.basename(self.exectext.entry_text.get())
            filename_minus_extension    = os.path.splitext(content)[0]
            content                     = f"{filename_minus_extension}.desktop"

            self.filenametext.delete        (0, tk.END)
            self.filenametext.insert        (0, content)

        else:
            self.filenametext.configure     (state='disabled')
            self.filenamelabel.configure    (state='disabled')

    def on_changes_name(self,event=None): # event info of no value

        if self.filenametext.entry_text.get() != "":
            self.btn_ok.configure           (state='enabled')
        else:
            self.btn_ok.configure           (state='disabled')


    def quit(self):
        print("Doin' some cleaning up...")
        if self.ctrl_c_timer != None:
            print("This one time, killing time might stop a crime. Apologies to mr. Elliott Smith")
            self.root.after_cancel          (self.ctrl_c_timer)
            self.ctrl_c_timer               = None
        self.root.destroy                   ()
        print("All done!")

    def click_ok(self):
        filename                            = self.filenametext.get()
        if os.path.isfile(self.exectext.get()):
            # if self.outtext.entry_text.get() != "":
            parent_dir_of_executable            = os.path.dirname(os.path.realpath(self.exectext.get()))

            # if not os.access(parent_dir_of_executable, os.W_OK):
            #      # https://docs.python.org/3/library/os.html#os.access
            #     self.root.after(10,lambda: messagebox.showerror(title="Desktop-file creator:",
            #                          message="Directory is not writable")
            #     );
            #     return
            if filename.endswith(".desktop"):
                filename = os.path.join(parent_dir_of_executable,filename)
            else:
                filename = os.path.join(parent_dir_of_executable,f"{filename}.desktop")

            try:
                with open(filename, "w") as my_file:

                    my_file.write               ("[Desktop Entry]\n")
                    my_file.write               ("Name=" + self.nametext.get() + "\n")
                    my_file.write               ("Exec=" + self.exectext.get() + "\n")
                    my_file.write               ("Icon=" + self.icontext.get() + "\n")

                msg = messagebox.showinfo       (title="Desktop-file creator:",
                                                message="Shortcut Created")
                print(msg)
                self.root.destroy               ()

            except PermissionError as e:
                # https://docs.python.org/3/library/os.html#os.access
                self.root.after(10,lambda: messagebox.showerror(title="Desktop-file creator:",
                                     message=f"Permission Error! Can't write to:\n{parent_dir_of_executable}")
                );
            except:
                self.root.after(10,lambda: messagebox.showerror(title="Desktop-file creator:",
                                     message="SHORTCUT WAS NOT CREATED")
                );


    def choose_file(self):
        self.exectext.delete                (0, tk.END)
        self.exectext.insert                (0, fd.askopenfilename())
        # self.exectext.entry_text.set(fd.askopenfilename())

    def choose_savepath(self):
        self.outtext.delete                (0, tk.END)
        self.outtext.insert                (0, fd.askdirectory())
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
    # DECLARE AND START THE TIMER THAT LETS <CTRL+C> IN THE TERMINAL CLOSE THE WINDOW
    #
    def startCtrlCTimer(self): # <⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅               START <CTRL+C>-TIMER
                                                      #         I LIKE TO KEEP A 'self.'-REFERENCE OF '.after()'
        self.ctrl_c_timer = self.root.after (         #     THIS WAY WE CAN STOP THE TIMER AND AVOID ERRORS LIKE
            80,self.startCtrlCTimer                   #   "NO COMMAND FOUND", IF TIMER FIRES AFTER / WHILE DOING
        );                                            #                                    'self.root.destroy()'


    def toggleCtrlCTimer(self): # <⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅       TOGGLE <CTRL+C>-TIMER ON/OFF
        if self.ctrl_c_timer is None:
            self.startCtrlCTimer            ()

        else:
            self.root.after_cancel          (self.ctrl_c_timer)
            self.ctrl_c_timer               = None

    # --- END INFINTE LOOP END ---------------------------------------------------------------------------------


if __name__ == "__main__":

    app = MainWindow()
    app.show()

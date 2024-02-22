#!/bin/env python

import  re, sys, signal

import  tkinter     as      tk
from    tkinter     import  ttk


from collections import deque


class CEntry(ttk.Entry):

    def __init__(self, parent=None, font=None, enabled=True, *args, **kwargs):
        ttk.Entry.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self._undo_stack = deque(maxlen=100)
        self._redo_stack = deque(maxlen=100)
        # self.entry_text = parent.entry_text
        self.changes = [""]
        self.steps = int()
        self.keep_active_timer = None

        self.entry_text                 =   tk.StringVar    ( );
        if font == None:
            _font = ("Arial",18)
        else:
            _font = font
        if enabled:
            _state = "enabled"
        else:
            _state = "disabled"
        self.configure(
            font                = _font,
            text                = self.entry_text,
            state               = _state
            # highlightbackground = ENTRY_HIGH_BG,
            # highlightcolor      = ENTRY_HIGH_COLOR,
            # disabledbackground  = WINDOW_COLOR,
            # insertbackground    = FOREGROUND_ENTRY,
            # background          = WINDOW_COLOR,
            # foreground          = "#ffaa00",
            # foreground          = FOREGROUND_ENTRY,
            # selectforeground    = FOREGROUND_ENTRY,
            # selectbackground    = C333,
            # borderwidth         = '0',
        );
        # self.element_options(self.context_menu)
        self.context_menu = tk.Menu(self,
            tearoff=0,
            bg="#000000",
            fg="#ffffff",
            relief="flat",
            bd=6,
            font=('',11),
        );
        # print(self.context_menu.winfo_class())
        self.context_menu.add_command(label="Cut")
        self.context_menu.add_command(label="Copy")
        self.context_menu.add_command(label="Paste")
        self.context_menu.add_command(label="Select all")
        self.set_bindings()
        # self.pack(fill='both')
        # self.after(20, self.toggleKeepActiveTimer)

    #     self._xview = {}
    #     self.watch_xview(self)
    #     self.bind("<<XviewChanged>>", lambda e: print(e))
    #
    # def watch_xview(self, widget):
    #     xview = widget.xview()
    #     print(xview)
    #     prev_xview = self._xview.get(widget, "")
    #     self._xview[widget] = xview
    #     if xview != prev_xview:
    #         widget.event_generate("<<XviewChanged>>")
    #     widget.after(100, self.watch_xview, widget)

    def set_bindings(self):
        self.bind("<FocusOut>",self.handlePopupClose)

        self.bind("<Button>", self.onMouse)

        self.bind("<Button-3>", self.popup)

        # self.bind("<Motion>",self.onWheel)

        self.bind   ("<Shift-Up>",          self._shift_up_down)
        self.bind   ("<Shift-Down>",        self._shift_up_down)
        # self.bind   ("<Alt-Left>",          lambda e:self.scrollHandler(1))
        self.bind   ("<Alt-Left>",          lambda e:self.scrollHandler(2))
        self.bind   ("<Alt-Right>",         lambda e:self.scrollHandler(1))
        # self.bind   ("<Alt-Right>",         lambda e:self.scrollHandler(2))
        self.bind   ("<Control-A>",         self.select_all)
        self.bind   ("<Control-a>",         self.select_all)

        self.bind   ("<Control-z>",         self.undo)
        self.bind   ("<Control-Z>",         self.undo)
        #
        self.bind   ("<Control-y>",         self.redo)
        self.bind   ("<Control-Y>",         self.redo)
        self.bind   ("<Control-Shift-z>",   self.redo)
        self.bind   ("<Control-Shift-Z>",   self.redo)

        # self.bind   ("<Key>", self.add_changes)
        self.trace_id = self.entry_text.trace("w", self.on_changes)
        self.bind   ('<Control-BackSpace>', self.entry_ctrl_bs)

    def handlePopupClose(self,e=None):
        self.context_menu.unpost()

    def _wordAtIndex(self,string,index):
        sp = string.split(' ')
        total_len = 0
        for word in sp:
            total_len += (len(word) + 1)    #The '+1' accounts for the underscore
            if index < total_len:
                result = word
                break

        # _s = string.index(result)

        end_idx         = self.index(tk.INSERT)
        start_idx       = (self.get().rfind(" ", None, end_idx)+1) # magic word-boundary finder <3
        _s              = start_idx
        _e = _s + len(result)
        # return (_s,_e,result)
        return (_s,_e)

    def select_all(self,e):
        # print(self._wordAtIndex(e.widget.get(),self.index(tk.INSERT)))
        if self.select_present():
            # print(e.widget.get())
            # print(self.selection_get()) # get the selected text
            # print(e.widget.get()) # get the selected text
            if self.selection_get() == e.widget.get():
                self.select_range(0,0)
            else:
                self.select_range(0,tk.END)

        else:
            self.select_range(0,tk.END)
            # self.select_range(0,tk.END)
        return "break"

    def _shift_up_down(self,e):
        index_pack = self._wordAtIndex(e.widget.get(),self.index(tk.INSERT))
        # print(self._wordAtIndex(e.widget.get(),self.index(tk.INSERT)))
        if self.select_present():
            # print(e.widget.get())
            # print(self.selection_get()) # get the selected text
            # print(e.widget.get()) # get the selected text
            if self.selection_get() == e.widget.get():
                self.select_range(index_pack[0],index_pack[1])
                # self.select_range(0,0)
            else:
                self.select_range(0,tk.END)

        else:
            # print("GETTING INDEX PACK")
            self.select_range(index_pack[0],index_pack[1])
            # self.select_range(0,tk.END)
        return "break"

    def onMouse(self,e):
        self.handlePopupClose()
        # print(e.num,e.y)
        if e.num==5 or e.num ==6:
            self.scrollHandler(1)
            return "break"
        elif e.num==4 or e.num==7:
            self.scrollHandler(2)
            return "break"



    def scrollHandler(self,mode):
        if mode == 2:
            self.xview_scroll(-2, "units")
        else:
            self.xview_scroll(2, "units")
        return "break"


    def entry_ctrl_bs(self, event):
        # print()
        if not self.select_present():
            end_idx         = self.index(tk.INSERT)
            start_idx       = (self.get().rfind(" ", None, end_idx)+1) # magic word-boundary finder <3
            if end_idx != start_idx:
                self.selection_range(start_idx, end_idx)


    def popup(self, event):
        self.context_menu.entryconfigure("Cut", command=lambda: self.event_generate("<<Cut>>"))
        self.context_menu.entryconfigure("Copy", command=lambda: self.event_generate("<<Copy>>"))
        self.context_menu.entryconfigure("Paste", command=lambda: self.event_generate("<<Paste>>"))
        self.context_menu.entryconfigure("Select all", command=lambda: self.select_all(""))
        self.context_menu.post(event.x_root, event.y_root)
        # self.context_menu.focus_set()
    #

    def undo(self, event=None):  # noqa
        # print(len(self._undo_stack))
        # print(self.trace_id)
        if len(self._undo_stack) <= 1:
            # self.entry_text.trace_vdelete("w", self.trace_id)
            # if len(self._undo_stack) > 0:
            #     content = self._undo_stack.pop()
            # # self._redo_stack.append(content)
            #     content = ""
            #     self.entry_text.trace_vdelete("w", self.trace_id)
            #     self.delete(0, tk.END)
            #     self.insert(0, content)
            #
            #     self.event_generate('<<FieldChanged>>')
            #     self.trace_id = self.entry_text.trace("w", self.on_changes)
            return "break"
        else:
            old_view =  self.xview()
            # print(old_view)
            old_index = self.index(tk.INSERT)
            if old_index < self.index(tk.END):
                reset_index = True
            else:
                reset_index = False
            content = self._undo_stack.pop()
            self._redo_stack.append(content)
            content = self._undo_stack[-1]
            self.entry_text.trace_vdelete("w", self.trace_id)
            self.delete(0, tk.END)
            self.insert(0, content)

            self.event_generate('<<FieldChanged>>')
            if reset_index == False:
                self.icursor(len(content))
                # self.xview_moveto(1.0)
            else:
                self.icursor(old_index)
            self.trace_id = self.entry_text.trace("w", self.on_changes)
            # self.see(tk.INSERT)
            if old_index == (len(self.get())+1):
                # if self.xview()[1] != 1.0:
                self.xview(100)
                # print("pop")
            else:
                self.xview_moveto(old_view[0])
            return "break"

    def redo(self, event=None):  # noqa
        if not self._redo_stack:
            return

        old_view =  self.xview()
        old_index = self.index(tk.INSERT)
        if old_index < self.index(tk.END):
            reset_index = True
        else:
            reset_index = False
        content = self._redo_stack.pop()
        self._undo_stack.append(content)
        self.entry_text.trace_vdelete("w", self.trace_id)
        self.delete(0, tk.END)
        self.insert(0, content)

        self.event_generate('<<FieldChanged>>')
        # self.icursor(len(content))
        self.trace_id = self.entry_text.trace("w", self.on_changes)
        if reset_index:
            self.icursor(old_index)
        if old_index == (len(self.get())-1):
            # if self.xview()[1] != 1.0:
            self.xview(100)
            # print("pop")
        else:
            self.xview_moveto(old_view[0])
        # self.xview_scroll(old_view[0])
        # self.see(tk.INSERT)
        return "break"


    def on_changes(self, a=None, b=None, c=None):  # noqa
        # Event.VirtualEventData = "poop"
        self.event_generate('<<FieldChanged>>')
        self._undo_stack.append(self.entry_text.get())
        self._redo_stack.clear()

    def reset_undo_stacks(self):
        self._undo_stack.clear()
        self._redo_stack.clear()
        self._undo_stack.append(self.entry_text.get())


# --------------------------------------------------------------------------
#                                                          HANDLE <CTRL + C>
def keyboard_interrupt_handler(sig, frame):
    print('You pressed Ctrl+C!',"Exiting...")
    sys.exit(0)

# --------------------------------------------------------------------------
#                                                  MAKE AND SPAWN NEW WINDOW


if __name__ == "__main__":


    signal.signal(
        signal.SIGINT,
        keyboard_interrupt_handler
    );

    app = CEntry()
    app.mainloop()

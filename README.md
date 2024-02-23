Based on tkshortcut by Roger Savage:
---

### [tkshortcut](https://github.com/rogersavage/tkshortcut)
Trivial Linux desktop entry creator in Tkinter

My first learning exercise in Tkinter, just a few text entry boxes and file pickers that output a Linux desktop entry in the form:

[Desktop Entry]<br>
Name={name}<br>
Exec={executable}<br>
Icon={icon}<br>

The code is completely unstructured and hardcoded, there is no error checking or handling, and the file picker doesn't generate thumbnails. 
This is the result of two hours of work after starting my first Tkinter tutorial. But it does what I want it to do.

---

### Changelog / Additions / Differences:
- class-based approach
- entry-fields:
  - undo/redo functionality added
  - entry-fields are scrollable
  - <Shift+Up> / <Shift+Down> toggles selection of either the closest word to the cursor or all text (if entry has selection present)
- some slight differences in geometry management
- hardcoded black color-scheme (TODO 1)
- autosuggestion of filename for .desktop file based on executable
- creation of the desktop file in the same directory as the selected executable (TODO 2)
- some checks and balances for the selected executable
- poop jokes hidden in the source-code

### TODO:
1. Add toggle on/off, color-scheme selector, or something like that
2. Select output directory
3. Add (way) more entry-rows
4. Add edit-functionality to existing files and autofill of fields
   - Maybe provide a collection of desktop files and instructions on how to add context-menu option in different DE's?  
5. Learn how to make right-click-menu items in other DE's than KDE.
 

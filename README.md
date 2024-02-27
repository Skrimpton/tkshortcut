# Based on tkshortcut by Roger Savage:
#### Thanks again for a fun project and being a real cool guy about the fork 😃👍
---

### [tkshortcut](https://github.com/rogersavage/tkshortcut)
Trivial Linux desktop entry creator in Tkinter

My first learning exercise in Tkinter, just a few text entry boxes and file pickers that output a Linux desktop entry in the form:

```
[Desktop Entry]
Name={name}
Exec={executable}
Icon={icon}
```

The code is completely unstructured and hardcoded, there is no error checking or handling, and the file picker doesn't generate thumbnails. 
This is the result of two hours of work after starting my first Tkinter tutorial. But it does what I want it to do.

---

### Additions / Differences:
- Class-based approach
- Entry-fields:
  - Undo/Redo functionality added
  - Entry-fields are scrollable
  - <Shift+Up> / <Shift+Down> : Rudimentary and buggy "word"/select-all shortcut
    - <Alt+Shit+/>, <Alt+Shit+;> and <Alt+Shit+Spacebar> sets text-separator for Shift-select 
    - Toggles selection of either the closest space-enclosed text (single letter or word) to the cursor<br>( if the cursor is touching text )
    - Toggles select all text if there is selection present
- Some slight differences in geometry management
- Black color-scheme - NOW WITH TOGGLE :heart_eyes:
  - <Alt+Shift+C>
- Select output directory
- Autosuggestion of filename for .desktop file based on executable
- Creation of the desktop file in the same directory as the selected executable (TODO 2)
- Some checks and balances for the selected executable
- Poop jokes hidden in the source-code<br>(Only color names, nothing functional. I ran out of descriptive imagination)

### TODO:
1. ~~Add toggle on/off~~,
2. Add color-scheme selector
3. ~~Select output directory : Add actual functionality (just a dummy for now)~~
4. Add (way) more entry-rows
5. Add edit-functionality to existing files and autofill of fields: 
   - Maybe provide a collection of desktop files and instructions on how to add context-menu option in different DE's for easy intergration.
6. Learn how to make right-click-menu items in other DE's than KDE.

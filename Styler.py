import tkinter as tk
from tkinter import ttk


C000                    = "#000000"
C101                    = "#101010"
C181                    = "#181818"
C222                    = "#222222"
C333                    = "#333333"
C444                    = "#444444"
Cba8                    = "#ba8404"
Cffa                    = "#ffaa00" # yellowish orange
Cfff                    = "#ffffff"
Cff1c                   = "#ffff1c" # bright yellow, more pale/white
Cff00                   = "#ffff00" # bright yellow, least pale/white
C55f                    = "#55ff7f" # bright/pale green
C313                    = "#313100" # poop
C391                    = "#391d00" # also poop, but different
C4c3                    = "#4c3401" # also poop, but a darker roast
C6f4                    = "#6f4e02" # too-much-fiber diarrhoea, and you had 2 glasses of milk
C4c4                    = "#4c4c00" # too-much-fiber diarrhoea, but only 1 glass
C2e1                    = "#2e1581" # blue
C002                    = "#002839" # dark greenish-blue / blueish-green
C013                    = "#01392d" # green that isn't trying too hard and is a little bit depressed
C3f4                    = "#3f452a" # GREENISH BROWNISH

WINDOW_COLOR            = C000 # BLACK
ENTRY_FOCUSED           = Cffa
ENTRY_UNFOCUSED         = Cfff

class Styler:

    def __init__(self, root):
        self.root = root

        self.style=ttk.Style(self.root)
        self.style.theme_use            ("alt")
        self.style.theme_create("user_theme", parent="clam")
        # style.theme_use("user_theme")

        # self.style.theme_use          ("clam")                            # use "clam"-theme
        # self.style.theme_use          ("classic")                         # use "classic"-theme
        # self.style.theme_use          ("vista")                           # use "vista"-theme (not available on linux)
        self.become_stylish             ()

    def become_stylish(self):
        self.style.layout(      "TEntry",
            [
                (   'Entry.plain.field', {
                        'children':
                        [(  'Entry.background', {'children':
                            [(  'Entry.padding', {'children': [( 'Entry.textarea', {'sticky': 'nswe'} )], 'sticky': 'nswe'} )],
                            'sticky': 'nswe'}
                        )],
                        'border':'1', 'sticky': 'nswe'
                    }
                )
            ]
        );

        self.style.map(         'C.TEntry',

            foreground          = [ ('!focus',ENTRY_UNFOCUSED), ('focus',ENTRY_FOCUSED)    ],
            background          = [ ('disabled',C333),('focus',C181), ('!focus',WINDOW_COLOR)    ],
            bordercolor         = [ ('disabled',C444),('focus',C444), ('!focus',WINDOW_COLOR)    ],
            insertcolor         = [ ('focus',Cfff),('!focus',Cff1c)    ],
            fieldbackground     = [ ('disabled',C333),('focus',WINDOW_COLOR),('!focus',WINDOW_COLOR)    ],
        );

        self.style.map(         'C.TLabel',
            background          = [ ('disabled',WINDOW_COLOR),('active',C101), ('!active',WINDOW_COLOR) ],
            foreground          = [ ('disabled',C101),('!active',Cfff),('active',Cffa)    ],
        );
        self.style.map(         'C.TButton',
            foreground          = [ ('disabled',C101),('!active',Cfff),('active',Cffa)    ],
            background          = [ ('disabled',C333),('active',C101), ('!active',WINDOW_COLOR) ],
        );

        self.style.configure(   'C.TLabel',
            background=WINDOW_COLOR,
            foreground=Cfff,

        );
        self.style.configure(   'C.TFrame',
            background=WINDOW_COLOR,
        );




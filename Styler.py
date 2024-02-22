import tkinter as tk
from tkinter import ttk


C000                    = "#000000"
C101                    = "#101010"
C181                    = "#181818"
C222                    = "#222222"
C333                    = "#333333"
C444                    = "#444444"
Cba8                    = "#ba8404"
C6f4                    = "#6f4e02"
C4c3                    = "#4c3401"
C4c4                    = "#4c4c00"
Cffa                    = "#ffaa00"
Cfff                    = "#ffffff"
Cffff1c                 = "#ffff1c"
Cffff00                 = "#ffff00"
C55f                    = "#55ff7f"
C313                    = "#313100"
C4c4                    = "#4c4c00"
C2e1                    = "#2e1581"
C391                    = "#391d00"
C002                    = "#002839"
C013                    = "#01392d"
C3f4                    = "#3f452a" # GREENISH BROWNISH

WINDOW_COLOR            = C000 # BLACK
ENTRY_FOCUSED           = Cffa
ENTRY_UNFOCUSED         = Cfff

class Styler:

    def __init__(self, root):
        self.root = root

        self.style=ttk.Style(self.root)
        self.style.theme_use            ("alt")

        # self.style.theme_use          ("clam")                            # use "clam"-theme
        # self.style.theme_use          ("classic")                         # use "classic"-theme
        # self.style.theme_use          ("vista")                           # use "vista"-theme (not available on linux)
        self._style_entry               ()                                  

    def _style_entry(self):

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

        self.style.map(         'TEntry',

            foreground          = [ ('!focus',ENTRY_UNFOCUSED), ('focus',ENTRY_FOCUSED)    ],
            background          = [ ('disabled',C333),('focus',C3f4), ('!focus',WINDOW_COLOR)    ],
            bordercolor         = [ ('disabled',C444),('focus',C444), ('!focus',WINDOW_COLOR)    ],
            insertcolor         = [ ('focus',Cfff),('!focus','#ffff1c')    ],
            fieldbackground     = [ ('disabled',C333),('focus',WINDOW_COLOR),('!focus',WINDOW_COLOR)    ],
        );

        self.style.map(         'TLabel',
            background          = [ ('disabled',WINDOW_COLOR),('active',C101), ('!active',WINDOW_COLOR) ],
            foreground          = [ ('disabled',C101),('!active',Cfff),('active',Cffa)    ],
        );
        self.style.map(         'TButton',
            foreground          = [ ('disabled',C101),('!active',Cfff),('active',Cffa)    ],
            background          = [ ('disabled',C333),('active',C101), ('!active',WINDOW_COLOR) ],
        );

        self.style.configure(   'TLabel',
            background=WINDOW_COLOR,
            foreground=Cfff,

        );
        self.style.configure(   'TFrame',
            background=WINDOW_COLOR,
        );




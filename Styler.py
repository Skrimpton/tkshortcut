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

BUTTON_DISABLED_FG      = C55f
SIDEBAR_COLOR           = C101 # DARK GREY
MAINFRAME_COLOR         = C000 # BLACK
WINDOW_COLOR            = C000 # BLACK
TEXT_COLOR              = Cba8 # YELLOWISH ORANGE
ENTRY_HIGH_BG           = C222 # DARK GREY
ENTRY_HIGH_COLOR        = C444 # LIGHTER DARK GREY
# ENTRY_HIGH_BG           = "#ffaa00"
# FOREGROUND_ENTRY        = "#ffaa00"
ENTRY_FOCUSED           = C55f
ENTRY_UNFOCUSED         = Cfff


SCROLLBAR_THROUGHCOLOR  = C000


ODD_COLOR               = C181
EVEN_COLOR              = C101
ITEM_SEL_FOCUS          = C013
ITEM_SEL_NOTFOCUS       = C002
ITEM_SEL_FOCUS_TXT      = Cfff

class Styler:

    def __init__(self, root):
        self.root = root

        self.style=ttk.Style(self.root)
        self.style.theme_use            ("alt")

        # self.style.theme_use          ("clam")                            # use "clam"-theme
        # self.style.theme_use          ("classic")                         # use "classic"-theme
        # self.style.theme_use          ("vista")                           # use "vista"-theme (not available on linux)
        # self.style.element_create     ("Plain.Field", "from", "clam")     # create element
        self._style_entry                ()                                  #

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
            background          = [ ('disabled',C333),('focus',C3f4), ('!focus',C000)    ],
            bordercolor         = [ ('disabled',C444),('focus',C444), ('!focus',C000)    ],
            insertcolor         = [ ('focus','#ffffff'),('!focus','#ffff1c')    ],
            fieldbackground     = [ ('disabled',C333),('focus',C000),('!focus',C000)    ],
        );

        self.style.map(         'TLabel',
            background          = [ ('disabled',C000),('active',"#101010"), ('!active',"#000000") ],
            foreground          = [ ('disabled',C101),('!active',Cfff),('active',Cffa)    ],
        );
        self.style.map(         'TButton',
            foreground          = [ ('disabled',C101),('!active',Cfff),('active',Cffa)    ],
            background          = [ ('disabled',C333),('active',"#101010"), ('!active',"#000000") ],
            relif               = [('disabled','sunken'),('!disabled','flat')],
        );

        self.style.configure(   'TLabel',
            background=C000,
            foreground=Cfff,

        );
        self.style.configure(   'TFrame',
            background="#000000",
        );




from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Literal, Text, Other, Whitespace, Punctuation

BACKGROUND = "#2f1e2e"
CURRENT_LINE = "#41323f"
SELECTION = "#4f424c"
FOREGROUND = "#e7e9db"
COMMENT = "#776e71"
RED = "#ef6155"
ORANGE = "#f99b15"
YELLOW = "#fec418"
GREEN = "#48b685"
AQUA = "#5bc4bf"
BLUE = "#06b6ef"
PURPLE = "#815ba4"

class Flagbot(Style):
    default_style = ""
    background_color = BACKGROUND
    highlight_color = SELECTION

    styles = {
        # No corresponding class for the following:
        Text:                      FOREGROUND,  # class:  ''
        # TODO: keep in sync with codeboxforeground in theme/flagbot.sty
        # This should be applied as the default color automatically for any text,
        # but minted doesn't want to do that for some reason.
        # In languages like python, where pygments basically highlights every token, this doesn't seem to be an issue,
        # but for e.g. bash, where many tokens don't get any class assigned, this would result in black text
        # if we didn't set the text color again in flagbot.sty

        Whitespace:                "",          # class: 'w'
        Error:                     RED,         # class: 'err'
        Other:                     "",          # class 'x'

        Comment:                   COMMENT,   # class: 'c'
        Comment.Multiline:         "",        # class: 'cm'
        Comment.Preproc:           "",        # class: 'cp'
        Comment.Single:            "",        # class: 'c1'
        Comment.Special:           "",        # class: 'cs'

        Keyword:                   PURPLE,    # class: 'k'
        Keyword.Constant:          "",        # class: 'kc'
        Keyword.Declaration:       "",        # class: 'kd'
        Keyword.Namespace:         AQUA,      # class: 'kn'
        Keyword.Pseudo:            "",        # class: 'kp'
        Keyword.Reserved:          "",        # class: 'kr'
        Keyword.Type:              YELLOW,    # class: 'kt'

        Operator:                  AQUA,      # class: 'o'
        Operator.Word:             "",        # class: 'ow' - like keywords

        Punctuation:               FOREGROUND,  # class: 'p'

        Name:                      FOREGROUND,  # class: 'n'
        Name.Attribute:            BLUE,        # class: 'na' - to be revised
        Name.Builtin:              "",          # class: 'nb'
        Name.Builtin.Pseudo:       "",          # class: 'bp'
        Name.Class:                YELLOW,      # class: 'nc' - to be revised
        Name.Constant:             RED,         # class: 'no' - to be revised
        Name.Decorator:            AQUA,        # class: 'nd' - to be revised
        Name.Entity:               "",          # class: 'ni'
        Name.Exception:            RED,         # class: 'ne'
        Name.Function:             BLUE,        # class: 'nf'
        Name.Property:             "",          # class: 'py'
        Name.Label:                "",          # class: 'nl'
        Name.Namespace:            YELLOW,      # class: 'nn' - to be revised
        Name.Other:                BLUE,        # class: 'nx'
        Name.Tag:                  AQUA,        # class: 'nt' - like a keyword
        Name.Variable:             RED,         # class: 'nv' - to be revised
        Name.Variable.Class:       "",          # class: 'vc' - to be revised
        Name.Variable.Global:      "",          # class: 'vg' - to be revised
        Name.Variable.Instance:    "",          # class: 'vi' - to be revised

        Number:                    ORANGE,    # class: 'm'
        Number.Float:              "",        # class: 'mf'
        Number.Hex:                "",        # class: 'mh'
        Number.Integer:            "",        # class: 'mi'
        Number.Integer.Long:       "",        # class: 'il'
        Number.Oct:                "",        # class: 'mo'

        Literal:                   ORANGE,    # class: 'l'
        Literal.Date:              GREEN,     # class: 'ld'

        String:                    GREEN,       # class: 's'
        String.Backtick:           "",          # class: 'sb'
        String.Char:               FOREGROUND,  # class: 'sc'
        String.Doc:                COMMENT,     # class: 'sd' - like a comment
        String.Double:             "",          # class: 's2'
        String.Escape:             ORANGE,      # class: 'se'
        String.Heredoc:            "",          # class: 'sh'
        String.Interpol:           ORANGE,      # class: 'si'
        String.Other:              "",          # class: 'sx'
        String.Regex:              "",          # class: 'sr'
        String.Single:             "",          # class: 's1'
        String.Symbol:             "#27feff",          # class: 'ss'

        Generic:                   "",                    # class: 'g'
        Generic.Deleted:           RED,                   # class: 'gd',
        Generic.Emph:              "italic",              # class: 'ge'
        Generic.Error:             "",                    # class: 'gr'
        Generic.Heading:           "bold " + FOREGROUND,  # class: 'gh'
        Generic.Inserted:          GREEN,                 # class: 'gi'
        Generic.Output:            "",                    # class: 'go'
        Generic.Prompt:            "bold " + COMMENT,     # class: 'gp'
        Generic.Strong:            "bold",                # class: 'gs'
        Generic.Subheading:        "bold " + AQUA,        # class: 'gu'
        Generic.Traceback:         "",                    # class: 'gt'
    }

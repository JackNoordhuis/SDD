from src.pype.utils.Logger import Logger

"""Simple class to handle Terminal colors"""


class Terminal(object):

    format_bold = ""
    format_obfuscated = ""
    format_italic = ""
    format_underline = ""
    format_strike_through = ""

    format_reset = ""

    format_color_black = ""
    format_color_dark_blue = ""
    format_color_dark_green = ""
    format_color_dark_aqua = ""
    format_color_dark_red = ""
    format_color_purple = ""
    format_color_gold = ""
    format_color_gray = ""
    format_color_dark_gray = ""
    format_color_blue = ""
    format_color_green = ""
    format_color_aqua = ""
    format_color_red = ""
    format_color_light_purple = ""
    format_color_yellow = ""
    format_color_white = ""

    has_formatting_codes = True

    @staticmethod
    def init():
        Logger.warning("Terminal colors are not implemented yet")
        # TODO
        # Terminal.get_escape_codes()
        # Terminal.get_fallback_codes()

    @staticmethod
    def get_fallback_codes():
        Terminal.format_bold = "\x1b[1m"
        Terminal.format_obfuscated = ""
        Terminal.format_italic = "\x1b[3m"
        Terminal.format_underline = "\x1b[4m"
        Terminal.format_strike_through = "\x1b[9m"

        Terminal.format_reset = "\x1b[m"

        Terminal.format_color_black = "\x1b[38;5;16m"
        Terminal.format_color_dark_blue = "\x1b[38;5;19m"
        Terminal.format_color_dark_green = "\x1b[38;5;34m"
        Terminal.format_color_dark_aqua = "\x1b[38;5;37m"
        Terminal.format_color_dark_red = "\x1b[38;5;124m"
        Terminal.format_color_purple = "\x1b[38;5;127m"
        Terminal.format_color_gold = "\x1b[38;5;214m"
        Terminal.format_color_gray = "\x1b[38;5;145m"
        Terminal.format_color_dark_gray = "\x1b[38;5;59m"
        Terminal.format_color_blue = "\x1b[38;5;63m"
        Terminal.format_color_green = "\x1b[38;5;83m"
        Terminal.format_color_aqua = "\x1b[38;5;87m"
        Terminal.format_color_red = "\x1b[38;5;203m"
        Terminal.format_color_light_purple = "\x1b[38;5;207m"
        Terminal.format_color_yellow = "\x1b[38;5;227m"
        Terminal.format_color_white = "\x1b[38;5;231m"

    @staticmethod
    def get_escape_codes():

        Terminal.format_bold = "tput bold"
        Terminal.format_obfuscated = "tput smacs"
        Terminal.format_italic = "tput sitm"
        Terminal.format_underline = "tput smul"
        Terminal.format_strike_through = "\x1b[9m"

        Terminal.format_reset = "tput sgr0"

        colors = 256
        if colors > 8:
            if colors >= 256:
                Terminal.format_color_black = "tput setaf 16"
                Terminal.format_color_dark_blue = "tput setaf 19"
                Terminal.format_color_dark_green = "tput setaf 34"
                Terminal.format_color_dark_aqua = "tput setaf 37"
                Terminal.format_color_dark_red = "tput setaf 124"
                Terminal.format_color_purple = "tput setaf 127"
                Terminal.format_color_gold = "tput setaf 214"
                Terminal.format_color_gray = "tput setaf 145"
                Terminal.format_color_dark_gray = "tput setaf 59"
                Terminal.format_color_blue = "tput setaf 63"
                Terminal.format_color_green = "tput setaf 83"
                Terminal.format_color_aqua = "tput setaf 87"
                Terminal.format_color_red = "tput setaf 203"
                Terminal.format_color_light_purple = "tput setaf 207"
                Terminal.format_color_yellow = "tput setaf 227"
                Terminal.format_color_white = "tput setaf 231"
            else:
                Terminal.format_color_black = "tput setaf 0"
                Terminal.format_color_dark_blue = "tput setaf 4"
                Terminal.format_color_dark_green = "tput setaf 2"
                Terminal.format_color_dark_aqua = "tput setaf 6"
                Terminal.format_color_dark_red = "tput setaf 1"
                Terminal.format_color_purple = "tput setaf 5"
                Terminal.format_color_gold = "tput setaf 3"
                Terminal.format_color_gray = "tput setaf 7"
                Terminal.format_color_dark_gray = "tput setaf 8"
                Terminal.format_color_blue = "tput setaf 12"
                Terminal.format_color_green = "tput setaf 10"
                Terminal.format_color_aqua = "tput setaf 14"
                Terminal.format_color_red = "tput setaf 9"
                Terminal.format_color_light_purple = "tput setaf 13"
                Terminal.format_color_yellow = "tput setaf 11"
                Terminal.format_color_white = "tput setaf 15"
        else:
            Terminal.format_color_black = Terminal.format_color_dark_gray = "tput setaf 0"
            Terminal.format_color_red = Terminal.format_color_dark_red = "tput setaf 1"
            Terminal.format_color_green = Terminal.format_color_dark_green = "tput setaf 2"
            Terminal.format_color_yellow = Terminal.format_color_gold = "tput setaf 3"
            Terminal.format_color_blue = Terminal.format_color_dark_blue = "tput setaf 4"
            Terminal.format_color_light_purple = Terminal.format_color_purple = "tput setaf 5"
            Terminal.format_color_aqua = Terminal.format_color_dark_aqua = "tput setaf 6"
            Terminal.format_color_gray = Terminal.format_color_dark_gray = "tput setaf 7"


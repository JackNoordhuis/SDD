import re

"""Simple class to handle Minecraft chat formatting"""


class TextFormat(object):

    @staticmethod
    def escape():
        return "\xc2\xa7"

    @staticmethod
    def black():
        return TextFormat.escape() + "0"

    @staticmethod
    def dark_blue():
        return TextFormat.escape() + "1"

    @staticmethod
    def dark_green():
        return TextFormat.escape() + "2"

    @staticmethod
    def dark_aqua():
        return TextFormat.escape() + "3"

    @staticmethod
    def dark_red():
        return TextFormat.escape() + "4"

    @staticmethod
    def dark_purple():
        return TextFormat.escape() + "5"

    @staticmethod
    def gold():
        return TextFormat.escape() + "6"

    @staticmethod
    def gray():
        return TextFormat.escape() + "7"

    @staticmethod
    def dark_gray():
        return TextFormat.escape() + "8"

    @staticmethod
    def blue():
        return TextFormat.escape() + "9"

    @staticmethod
    def green():
        return TextFormat.escape() + "a"

    @staticmethod
    def aqua():
        return TextFormat.escape() + "b"

    @staticmethod
    def red():
        return TextFormat.escape() + "c"

    @staticmethod
    def light_purple():
        return TextFormat.escape() + "d"

    @staticmethod
    def yellow():
        return TextFormat.escape() + "e"

    @staticmethod
    def white():
        return TextFormat.escape() + "f"

    @staticmethod
    def obfuscated():
        return TextFormat.escape() + "k"

    @staticmethod
    def bold():
        return TextFormat.escape() + "l"

    @staticmethod
    def strike_through():
        return TextFormat.escape() + "m"

    @staticmethod
    def underline():
        return TextFormat.escape() + "n"

    @staticmethod
    def italic():
        return TextFormat.escape() + "o"

    @staticmethod
    def reset():
        return TextFormat.escape() + "r"

    @staticmethod
    def clean(string):
        return re.sub(r"" + TextFormat.escape() + ".", "", string)

    @staticmethod
    def to_ansi(string):
        # TODO: Fix
        # string = string.replace(TextFormat.bold(), Terminal.format_bold)
        # string = string.replace(TextFormat.obfuscated(), Terminal.format_obfuscated)
        # string = string.replace(TextFormat.italic(), Terminal.format_italic)
        # string = string.replace(TextFormat.underline(), Terminal.format_underline)
        # string = string.replace(TextFormat.strike_through(), Terminal.format_strike_through)
        # string = string.replace(TextFormat.reset(), Terminal.format_reset)
        #
        # string = string.replace(TextFormat.black(), Terminal.format_color_black)
        # string = string.replace(TextFormat.dark_blue(), Terminal.format_color_dark_blue)
        # string = string.replace(TextFormat.dark_green(), Terminal.format_color_dark_green)
        # string = string.replace(TextFormat.dark_aqua(), Terminal.format_color_dark_aqua)
        # string = string.replace(TextFormat.dark_red(), Terminal.format_color_dark_red)
        # string = string.replace(TextFormat.dark_purple(), Terminal.format_color_purple)
        # string = string.replace(TextFormat.gold(), Terminal.format_color_gold)
        # string = string.replace(TextFormat.gray(), Terminal.format_color_gray)
        # string = string.replace(TextFormat.dark_gray(), Terminal.format_color_dark_gray)
        # string = string.replace(TextFormat.blue(), Terminal.format_color_blue)
        # string = string.replace(TextFormat.green(), Terminal.format_color_green)
        # string = string.replace(TextFormat.aqua(), Terminal.format_color_aqua)
        # string = string.replace(TextFormat.red(), Terminal.format_color_red)
        # string = string.replace(TextFormat.light_purple(), Terminal.format_color_light_purple)
        # string = string.replace(TextFormat.yellow(), Terminal.format_color_yellow)
        # string = string.replace(TextFormat.white(), Terminal.format_color_white)

        return TextFormat.clean(string)

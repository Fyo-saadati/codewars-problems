"""In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"
NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters."""
import re


def decode_morse(morse_code):
    dict = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        ".----": "1",
        ".-.-.-": ".",
        ".-...": "&",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "..---": "2",
        "--..--": ",",
        "---...": ":",
        "--.": "G",
        "....": "H",
        "..": "I",
        "...--": "3",
        "..--..": "?",
        "-.-.-.": ";",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "....-": "4",
        ".----.": "'",
        "-...-": "=",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".....": "5",
        "-.-.--": "!",
        ".-.-.": "+",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "-....": "6",
        "-..-.": "/",
        "-....-": "-",
        "...": "S",
        "-": "T",
        "..-": "U",
        "--...": "7",
        "-.--.": "(",
        "..--.-": "_",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "---..": "8",
        "-.--.-": ")",
        ".-..-.": '"',
        "-.--": "Y",
        "--..": "Z",
        " ": " ",
        "----.": "9",
        "-----": "0",
        "...-..-": "$",
        ".--.-.": "@",
        "...---...": "SOS",
        "   ": " ",
        " ": "",
        "": "",
    }
    string = ""
    morse_code = morse_code.strip()
    list2 = re.findall(r"([.-]+)(\s*)", morse_code)
    for tup in list2:
        for code in tup:
            string += dict[code]
    return string


print(decode_morse(".... . -.--   .--- ..- -.. ."))

from gpiozero import LED
import time


CODE = {
    " ": " ",
    "'": ".----.",
    "(": "-.--.-",
    ")": "-.--.-",
    ",": "--..--",
    "-": "-....-",
    ".": ".-.-.-",
    "/": "-..-.",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ":": "---...",
    ";": "-.-.-.",
    "?": "..--..",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "_": "..--.-",
}

def check_letter(letter):
    for symbol in CODE[leeter.upper()]:
        if symbol == '-':
            dash()
        elif symbol == '.':
            dot()
        else:
            time.sleep(.5)

def dash(led):
    led.on()
    time.sleep(.5)
    led.off()
    time.sleep(.2)


def dot(led):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(.2)


while True:
    input = raw_input("What would you like to send?\n")

    for letter in input:

#  blink(self, on_time=1, off_time=1, n=None, background=True)
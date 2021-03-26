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
    for symbol in CODE[letter.upper()]:
        if symbol == "-":
            dash(led)
        elif symbol == ".":
            dot(led)
        else:
            time.sleep(0.5)


def dash(led):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.2)


def dot(led):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(0.2)


led = LED(17)

while True:
    user_input = input("What would you like to send?\n")

    for letter in user_input:
        check_letter(letter)

#  blink(self, on_time=1, off_time=1, n=None, background=True)

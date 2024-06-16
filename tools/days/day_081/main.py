from days.day_081.files.helpers import *


def string_to_morse_text(input):
    morse_code = []
    for char in input.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append("?")  # Unknown characters are marked as '?'
    return " ".join(morse_code)


# def string_to_morse_sound(input):
#     new_sound = SoundWaves()
#     str_list = list(input)


#     for char in str_list:
#         char = char.capitalize()
#         if char in MORSE_CODE_SOUND_DICT:
#             value = MORSE_CODE_SOUND_DICT[char]
#             new_sound.save_char(value)
#         else:
#             new_sound.add_longer_pause()
def string_to_morse_sound(input_string):
    dir = os.path.join(os.path.dirname(__file__), "files")
    ensure_beep_files(dir)
    new_sound = SoundWaves(directory=dir)
    str_list = list(input_string)

    for char in str_list:
        char = char.upper()
        if char in MORSE_CODE_SOUND_DICT:
            value = MORSE_CODE_SOUND_DICT[char]
            new_sound.save_char(value)
        else:
            new_sound.add_longer_pause()
    return new_sound


def day_081():
    title("TEXT TO MORSE")
    mode = ""
    while mode != "s" and mode != "t":
        mode = nli(
            "Would you like to convert text to morse text or sound? (s for sound, t for text)"
        )

    if mode == "t":
        while True:
            user_input = nli(
                "Enter a string to convert to Morse code (or simply 'q' then enter to quit): "
            )
            if user_input.lower() == "q":
                nls("Bye!")
                break
            else:
                morse_code = string_to_morse_text(user_input)
                nls(f"Morse Code: {morse_code}")
    else:
        while True:
            user_input = nli(
                "Enter a string to convert to Morse code (or simply 'q' then enter to quit): "
            )
            if user_input.lower() == "q":
                nls("Bye!")
                break
            else:
                new_sound = string_to_morse_sound(user_input)
                new_sound.save_wav_format()
                nls("Morse generated - see output.wav")

                # nls(f"Morse Code: {morse_code}")

from days.day_085.files.helpers import *


def day_085():
    title("TYPING SPEED")
    import tkinter as tk
    from tkinter import messagebox
    import time
    import random

    # List of sample sentences for typing
    sample_sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is an awesome programming language.",
        "Typing speed tests are fun to do.",
        "Practice makes perfect.",
        "This is a simple typing speed test.",
    ]

    class TypingSpeedTest:
        def __init__(self, root):
            self.root = root
            self.root.title("Typing Speed Test")

            self.sample_sentence = random.choice(sample_sentences)

            self.label = tk.Label(root, text="Type the following sentence:")
            self.label.pack()

            self.sample_label = tk.Label(
                root, text=self.sample_sentence, wraplength=400
            )
            self.sample_label.pack()

            self.entry = tk.Entry(root, width=50)
            self.entry.pack()
            self.entry.bind("<Return>", self.calculate_speed)

            self.result_label = tk.Label(root, text="")
            self.result_label.pack()

            self.start_button = tk.Button(root, text="Start", command=self.start_test)
            self.start_button.pack()

            self.reset_button = tk.Button(root, text="Reset", command=self.reset_test)
            self.reset_button.pack()

            self.start_time = None

        def start_test(self):
            self.sample_sentence = random.choice(sample_sentences)
            self.sample_label.config(text=self.sample_sentence)
            self.entry.delete(0, tk.END)
            self.result_label.config(text="")
            self.start_time = time.time()
            self.entry.focus()

        def calculate_speed(self, event):
            end_time = time.time()
            time_taken = end_time - self.start_time
            typed_text = self.entry.get()

            if typed_text == self.sample_sentence:
                words = len(typed_text.split())
                wpm = words / (time_taken / 60)
                self.result_label.config(
                    text=f"Your typing speed is {wpm:.2f} words per minute."
                )
            else:
                self.result_label.config(
                    text="The typed text does not match the sample sentence."
                )

        def reset_test(self):
            self.entry.delete(0, tk.END)
            self.result_label.config(text="")
            self.sample_sentence = random.choice(sample_sentences)
            self.sample_label.config(text=self.sample_sentence)
            self.start_time = None

    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()

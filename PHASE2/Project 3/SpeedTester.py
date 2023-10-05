import tkinter as tk
import random
import time

class TypingSpeedTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Type Tester")

        self.sentences = [
            "CodersCave",
            "Jai Hind Jai Bharat.",
            "Have a Nice Day "
        ]

        self.current_sentence = ""
        self.user_input = tk.StringVar()
        self.start_time = None

        self.setup_ui()

    def setup_ui(self):
        self.sentence_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.sentence_label.pack(pady=30)

        self.entry = tk.Entry(self.root, textvariable=self.user_input, font=("Arial", 14))
        self.entry.pack(pady=30)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=30)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_test)
        self.start_button.pack(pady=30)

    def start_test(self):
        self.current_sentence = random.choice(self.sentences)
        self.sentence_label.config(text=self.current_sentence)
        self.user_input.set("")
        self.result_label.config(text="")
        self.start_time = time.time()
        self.entry.focus_set()
        self.start_button.config(state="disabled")
        self.entry.bind("<Return>", self.check_result)

    def check_result(self, event=None):
        if self.start_time is not None:
            user_text = self.user_input.get()
            elapsed_time = time.time() - self.start_time
            words = len(self.current_sentence.split())
            speed = words / (elapsed_time / 60)
            accuracy = self.calculate_accuracy(self.current_sentence, user_text)

            result_text = f"Speed: {speed:.2f} WPM | Accuracy: {accuracy:.2f}%"
            self.result_label.config(text=result_text)
            self.start_time = None
            self.start_button.config(state="normal")
            self.entry.unbind("<Return>")

    def calculate_accuracy(self, original, user_text):
        original_words = original.split()
        user_words = user_text.split()

        correct_words = sum(1 for orig_word, user_word in zip(original_words, user_words) if orig_word == user_word)
        accuracy = (correct_words / len(original_words)) * 100
        return accuracy

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestGUI(root)
    root.mainloop()
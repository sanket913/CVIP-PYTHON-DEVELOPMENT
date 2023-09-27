import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    elif text == "D":
        current_text = screen.get()
        if current_text:
            new_text = current_text[:-1]  # Remove the last character
            screen.set(new_text)
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 30 bold")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_dict = {
    (1, 0): "7",
    (1, 1): "8",
    (1, 2): "9",
    (1, 3): "*",
    (2, 0): "4",
    (2, 1): "5",
    (2, 2): "6",
    (2, 3): "+",
    (3, 0): "1",
    (3, 1): "2",
    (3, 2): "3",
    (3, 3): "-",
    (4, 0): "0",
    (4, 1): "00",
    (4, 2): ".",
    (4, 3): "=",
    (0, 0): "C",
    (0, 1): "%",
    (0, 2): "D",
    (0, 3): "/"
}

row_num, col_num = 1, 0

for (row, col), text in button_dict.items():
    button = tk.Button(root, text=text, padx=20, pady=20, font="lucida 20 bold")
    button.grid(row=row_num, column=col_num, padx=5, pady=5)
    button.bind("<Button-1>", on_click)

    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()

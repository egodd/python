from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
FLIPPED = False
current_card = {}
to_learn = {}


# -------------------- PANDAS -------------------------
try:
    df = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_df = pd.read_csv("data/french_words.csv")
    to_learn = original_df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def known_func():
    next_card()
    to_learn.remove(current_card)

    df2 = pd.DataFrame(to_learn)
    df2.to_csv("data/words_to_learn.csv", index=False)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(word_l, text=current_card['French'], fill="black")
    canvas.itemconfig(language_l, text="French", fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language_l, text="English", fill="white")
    canvas.itemconfig(word_l, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back_img)



# ------------------ TKINTER ---------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
language_l = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
word_l = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)



# buttons
unknown_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_img, highlightthickness=0, command=known_func)
known_button.grid(row=1, column=1)


next_card()


window.mainloop()
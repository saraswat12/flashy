from tkinter import *
from tkinter import PhotoImage
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}


try:
    data = pd.read_csv(r"data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(r"data/french_words.csv")    
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    frnch_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text = frnch_word, fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)
    

        
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card) # remove the word when user click known (right) buuton
    data = pd.DataFrame(to_learn) # than we have a new list without that words than we create
    data.to_csv("data/words_to_learn.csv", index=False) # a csv file
    next_card()
    


window = Tk()
window.title("Flashy")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height= 526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file=r"D:\python_new projects\flash card\images\card_front.png")
card_back_image = PhotoImage(file=r"D:\python_new projects\flash card\images\card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



right_image= PhotoImage(file=r"D:\python_new projects\flash card\images\right.png")
right_button = Button(image=right_image,  highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_image= PhotoImage(file=r"D:\python_new projects\flash card\images\wrong.png")
wrong_button = Button(image=wrong_image,  highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)



next_card() # when we start ui already data fetched and shown onto ui



window.mainloop()

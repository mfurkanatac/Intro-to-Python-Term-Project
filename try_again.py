from tkinter import *
import pandas, random, csv


BACKGROUND_COLOR = "#fbeeff" # https://www.the215guys.com/blog/soft-background-colors/
current_card= {}
total_points = 0

"""
NOTE: This is the same page of the main game
so it will not be explained except few parts.
"""


original_data = pandas.read_csv("data/words_to_learn.csv")
to_learn = original_data.to_dict(orient="records") # the format: [{a:b, c:d}, ...]


header = ["English", "Türkçe", "Check"]


def is_known():
    to_learn.remove(current_card)
    next_card()
    
def is_not_known():
    next_card()
    

def next_card():
    global current_card 
    if len(to_learn) > 0:
        current_card = random.choice(to_learn) # with the help of the random library, we pick a card
        canvas.itemconfig(card_title, text=current_card["English"], fill="black")
        canvas.itemconfig(card_word, text=current_card["Türkçe"], fill="black")
        canvas.itemconfig(card_background, image=card_img)
    else:
        # if there are no cards in the game:
        canvas.itemconfig(card_title, text="No words to repeat.", fill="black")
        canvas.itemconfig(card_word, text="Close the game if you want.", fill="black")
        canvas.itemconfig(card_background, image=card_img)


def checker_for_true():
    if current_card["Check"] == True:
        is_known()
    elif current_card["Check"] == False:
        is_not_known()


def checker_for_false():
    if current_card["Check"] == False:
        is_known()
    elif current_card["Check"] == True:
        is_not_known()


window = Tk()
window.title("Flash Card Study App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=550)


card_img = PhotoImage(file="images/card.png")
card_background = canvas.create_image(400, 263, image=card_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=checker_for_false)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=checker_for_true)
known_button.grid(row=1, column=1)

quit_image = PhotoImage(file="images/quit.png")
quit_button = Button(image=quit_image, command=quit)
quit_button.grid(row=1, column=2)


next_card()
window.mainloop()




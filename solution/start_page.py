# Furkan Atac
# 150210304
from tkinter import *
import pandas, random


"""
NOTE:
The aim of the project is to help students memorize flash cards in their exams.
Steps for the project are:
1- Prepare the csv file/files for the words and more
2- Get used to tkinter
3- Create windows and switch cards
4- Make cards function

In the first step, I had few options. Two of them were just
getting the most used words on wikipedia and putting them on
a google docs. Then with the built-in "=GOOGLETRANSLATE" method
we would be able to get the translation of the words.

There are two ways for this, one is to use the google docs
directly and second is to use the API of Google Docs for Python.

https://developers.google.com/docs/api/quickstart/python

Since the API needing many libraries and customizations, I will
be using the traditional way. The main idea was not to fetch the
words so I do not consider as a problem in the code since there are
both Data Engineers and Data Scientists.
"""


"""
NOTE:
The definitions, variables and functions will be done in 
every page so they will not be explained again and again 
"""


BACKGROUND_COLOR = "#fbeeff" # https://www.the215guys.com/blog/soft-background-colors/
start_text = """
Hello, this is an app to help you memorize words or even
other things for your exam. The questions are true false
questions. If you want to proceed, please click the tick.
"""

# we config the variables to say the text we want them to say
def start_page():
    canvas.itemconfig(card_title, text="Flash Card Study Game", fill="black")
    canvas.itemconfig(card_word, text=start_text, fill="blue", font=("Ariel", 20))
    canvas.itemconfig(card_background, image=card_img)

# to the main page
def maingame():
    window.destroy()
    import game_page

# to play again
def replay_page():
    window.destroy()
    import try_again


# we create a window and a canvas
window = Tk()
window.title("Flash Card Study App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=600)

# we define variables for text and images
card_img = PhotoImage(file="images/card.png")
card_background = canvas.create_image(400, 263, image=card_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
total_counter = canvas.create_text(400, 400, text="Total Points: 0", font=("Ariel", 30))

# we config the canvas grids and colors
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

# we set the images
# NOTE: IMAGES HAVE COMMANDS (they are buttons)
replay_image = PhotoImage(file="images/replay.png")
unknown_button = Button(image=replay_image, highlightthickness=0, command=replay_page)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=maingame)
known_button.grid(row=1, column=1)

quit_image = PhotoImage(file="images/quit.png")
quit_button = Button(image=quit_image, highlightthickness=0, command=quit)
quit_button.grid(row=1, column=2)

# start the function at the end
start_page()
# to start the first card
window.mainloop()

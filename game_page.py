from tkinter import *
import pandas, random, csv, os


BACKGROUND_COLOR = "#fbeeff" # https://www.the215guys.com/blog/soft-background-colors/
current_card, practice = {}, []
total_points = 0
practice_start = False # this is to save the practice cards to a csv file


original_data = pandas.read_csv("data/study_words.csv")
to_learn = original_data.to_dict(orient="records") # the format: [{a:b, c:d}, ...]

# we set the headers to put to the words to learn csv
header = ["English","Türkçe","Check"]


# if the word is known (main words, not practice)
# once the words are finished, the practice section will start.
# the only difference in them is points and practice list addition.
def is_known():
    global total_points

    if len(to_learn) > 1:
        to_learn.remove(current_card)
        total_points += 25
        next_card()

    elif len(to_learn) == 1:
        total_points += 25
        to_learn.remove(current_card)

        if len(practice) >= 1:
            next_card_for_practice()

        elif len(practice) == 0:
            leaderboard_page()
    
# if it is not known
def is_not_known():
    global total_points

    total_points = total_points - 10
    practice.append(current_card)
    if len(to_learn) > 1:
        to_learn.remove(current_card)
        next_card()
    
    elif len(to_learn) == 1:
        to_learn.remove(current_card)

        if len(practice) >= 1:
            next_card_for_practice()

        elif len(practice) == 0:
            leaderboard_page()


# these do not include points, only for practice.
def is_known_for_practice():
    if len(practice) > 1:
        practice.remove(current_card)
        next_card_for_practice()

    if len(practice) == 1:
        leaderboard_page()
    

def is_not_known_for_practice():
    next_card_for_practice()
    
        
# this leads to leaderboard page
def leaderboard_page():
    # creating a points txt and deleting it
    # there is an exploit in the game if there is an existing
    # points file it is possible to cheat
    # so we edit one and delete it to recreate
    open("data/points.txt", "a").write(str(total_points))

    os.remove("data/points.txt")

    open("data/points.txt", "a").write(str(total_points))
    window.destroy()
    import leaderboard_page

# next card but for practice (next_card function will be explained)
def next_card_for_practice():
    global current_card, practice_start, try_enable
    if practice_start == False:
        # THIS MEANS THAT THE PRACTICE WORDS JUST STARTED SO WE SAVE IT TO
        # A CSV FILE TO A REPLAY IF WANTED FOR FURTHER PRACTICE
        try_enable = True
        with open('data/words_to_learn.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            for elem in practice:
                writer.writerow(list(elem.values()))
    practice_start = True

    current_card = random.choice(practice) # with the help of the random library, we pick a card
    canvas.itemconfig(card_title, text=current_card["English"], fill="black")
    canvas.itemconfig(card_word, text=current_card["Türkçe"], fill="black")
    canvas.itemconfig(total_counter, text=f"Total Points: {total_points}", fill="black")
    canvas.itemconfig(card_background, image=card_img)


def next_card():
    # we pick a card with random and display it
    global current_card 
    current_card = random.choice(to_learn) # with the help of the random library, we pick a card
    canvas.itemconfig(card_title, text=current_card["English"], fill="black")
    canvas.itemconfig(card_word, text=current_card["Türkçe"], fill="black")
    canvas.itemconfig(total_counter, text=f"Total Points: {total_points}", fill="black")
    canvas.itemconfig(card_background, image=card_img)



"""
This is a checker system as there are both true and wrong answers
in the game.

This includes practice cards too
"""
def checker_for_true():
    if len(to_learn) == 0:
        if current_card["Check"] == True:
            is_known_for_practice()
        elif current_card["Check"] == False:
            is_not_known_for_practice()

    else:
        if current_card["Check"] == True:
            is_known()
        elif current_card["Check"] == False:
            is_not_known()


def checker_for_false():
    if len(to_learn) == 0:
        if current_card["Check"] == False:
            is_known_for_practice()
        elif current_card["Check"] == True:
            is_not_known_for_practice()

    else: 
        if current_card["Check"] == False:
            is_known()
        elif current_card["Check"] == True:
            is_not_known()





# same stuff on start page

window = Tk()
window.title("Flash Card Study App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=550)


card_img = PhotoImage(file="images/card.png")
card_background = canvas.create_image(400, 263, image=card_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
total_counter = canvas.create_text(400, 400, text="Total Points: 0", font=("Ariel", 30))


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




import tkinter as tk
import csv, random, os

BACKGROUND_COLOR = "#fbeeff"  # https://www.the215guys.com/blog/soft-background-colors/
text_color = "blue"

# we read the leaderboard list and get points from previous game
with open('data/leaderboard.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
points = int(open("data/points.txt", "r").read())

empty = False 
header = data.pop(0)

if len(data) < 5:
    while len(data) < 5:
        data.append(["", 0])

# if the file is empty, the first element will not be there so we fix that
if data[0] == []:
    data[0] = ["", 0]

# if there are less than 5 players in the leaderboard (means the leaderboard is empty)
for elem in data:
    elem[1] = int(elem[1])
    if elem[1] == 0:
        empty = True

# we sort it with points
data.sort(key=lambda x: (x[1]), reverse=True)


def leaderboard_page():
    canvas.itemconfig(card_title, text="Leaderboard", fill="black")
    canvas.itemconfig(first, text=f"First: {data[0][0]} - {data[0][1]}", fill=text_color, font=("Ariel", 20))
    canvas.itemconfig(second, text=f"Second: {data[1][0]} - {data[1][1]}", fill=text_color, font=("Ariel", 20))
    canvas.itemconfig(third, text=f"Third: {data[2][0]} - {data[2][1]}", fill=text_color, font=("Ariel", 20))
    canvas.itemconfig(fourth, text=f"Fourth: {data[3][0]} - {data[3][1]}", fill=text_color, font=("Ariel", 20))
    canvas.itemconfig(fifth, text=f"Fifth: {data[4][0]} - {data[4][1]}", fill=text_color, font=("Ariel", 20))

    # if the points are not enough 
    if int(points) <= int(data[-1][1]):
        canvas.itemconfig(name, text="You did not make it to the leaderboard :(", font=("Ariel", 20))
        os.remove("data/points.txt")

def empty_check():
    name_check = False
    global empty
    for elem in data:
        if name_info.get() == elem[0]:
            # if the name is in the leaderboard
            # NOTE: the name can be empty (only once)
            # to let an anonymous player in
            canvas.itemconfig(name, text="Please choose another name", font=("Ariel", 20))
            name_check = True

    if not name_check:
        # name successfully implied
        # we set the points and name to the leaderboard
        # and get rid of the points file
        canvas.itemconfig(name, text="Name is in the leaderboard.", font=("Ariel", 20))
        if empty == True:
            data[-1][0] = name_info.get()
            data[-1][1] = points
            data.sort(key=lambda x: (x[1]), reverse=True)
            os.remove("data/points.txt")

        elif empty == False:
            if int(points) > int(data[-1][1]):
                data[-1][0] = name_info.get()
                data[-1][1] = points
                data.sort(key=lambda x: (x[1]), reverse=True)
                os.remove("data/points.txt")
        print(data)
        # we update the board
        canvas.itemconfig(first, text=f"First: {data[0][0]} - {data[0][1]}", fill=text_color, font=("Ariel", 20))
        canvas.itemconfig(second, text=f"Second: {data[1][0]} - {data[1][1]}", fill=text_color, font=("Ariel", 20))
        canvas.itemconfig(third, text=f"Third: {data[2][0]} - {data[2][1]}", fill=text_color, font=("Ariel", 20))
        canvas.itemconfig(fourth, text=f"Fourth: {data[3][0]} - {data[3][1]}", fill=text_color, font=("Ariel", 20))
        canvas.itemconfig(fifth, text=f"Fifth: {data[4][0]} - {data[4][1]}", fill=text_color, font=("Ariel", 20))

        # we delete and recreate the leaderboard

        os.remove("data/leaderboard.csv") 

        # open the file in the write mode
        with open('data/leaderboard.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for elem in data:
                writer.writerow(elem)

# to play again
def replay_page():
    window.destroy()
    import try_again

# same stuff in start page
window = tk.Tk()
window.title("Flash Card Study App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = tk.Canvas(width=800, height=600)

card_img = tk.PhotoImage(file="images/card.png")
card_background = canvas.create_image(400, 263, image=card_img)
card_title = canvas.create_text(400, 50, text="", font=("Ariel", 40, "bold"))

first = canvas.create_text(400, 100, text="", font=("Ariel", 30, "bold"))
second = canvas.create_text(400, 130, text="", font=("Ariel", 30, "bold"))
third = canvas.create_text(400, 160, text="", font=("Ariel", 30, "bold"))
fourth = canvas.create_text(400, 190, text="", font=("Ariel", 30, "bold"))
fifth = canvas.create_text(400, 220, text="", font=("Ariel", 30, "bold"))

name = canvas.create_text(400, 275, text="Please choose a name and click tick:", font=("Ariel", 20))
name_info = tk.StringVar()
e1 = tk.Entry(canvas, textvariable=name_info).place(x=300, y=300)

total_counter = canvas.create_text(400, 350, text=f"Total Points: {points}", font=("Ariel", 30))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

replay_image = tk.PhotoImage(file="images/replay.png")
unknown_button = tk.Button(image=replay_image, highlightthickness=0, command=replay_page)
unknown_button.grid(row=1, column=0)

check_image = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=check_image, highlightthickness=0, command=empty_check)
known_button.grid(row=1, column=1)

quit_image = tk.PhotoImage(file="images/quit.png")
quit_button = tk.Button(image=quit_image, highlightthickness=0, command=quit)
quit_button.grid(row=1, column=2)

leaderboard_page()
window.mainloop()

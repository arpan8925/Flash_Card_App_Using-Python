from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"

flip_timer = None

result = None

try:     
    df = read_csv("data/words_to_learn.csv")    

except FileNotFoundError:
    orginal_data = read_csv("data/french_words.csv")
    result = orginal_data.to_dict(orient='records')

else:
     result = df.to_dict(orient='records')
  




def next_card():

    global flip_timer, current_card

    if flip_timer is not None:
          window.after_cancel(flip_timer)
          flip_timer = None
    
    current_card = random.choice(result)
    random_french = current_card["French"]
    random_english = current_card["English"]

    canvas.itemconfig(card_title, text="French" )
    canvas.itemconfig(card_word, text=random_french )
    canvas.itemconfig(green_bg, image=card_front_img)
    canvas.itemconfig(card_title, fill="#000000")
    canvas.itemconfig(card_word, fill="#000000")

    flip_timer = window.after(3000, english_card, random_english)

    

def english_card(random_english):
        canvas.itemconfig(card_title, text="English" )
        canvas.itemconfig(card_word, text=random_english )
        canvas.itemconfig(green_bg, image=English_background_green)
        canvas.itemconfig(card_title, fill="#ffffff")
        canvas.itemconfig(card_word, fill="#ffffff")
    


def is_known():

      result.remove(current_card)
      next_card()

      data = DataFrame(result)
      data.to_csv("data/words_to_learn.csv", index=False)



window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
English_background_green = PhotoImage(file="images/card_back.png")


green_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text=" ", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=" ", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")

unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)





next_card()

window.mainloop()


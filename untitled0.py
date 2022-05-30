from tkinter import *
import random

root = Tk()
root.title("ColorRandomizer")
root.geometry("400x400")
root.configure(background = "lightblue")

label_score = Label(root, text = "Score : 0", font = ("Bahnschrift Light",12))
label_score.place(relx = 0.1, rely = 0.1, anchor = CENTER)

input_value = Entry(root)
input_value.place(relx = 0.5, rely = 0.5, anchor = CENTER)

randomcolor = Label(root, font = ("times", 15), bg = "lightblue")
randomcolor.place(relx = 0.5, rely = 0.4, anchor = CENTER)

class game:
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["ORANGE","YELLOW","BLUE","GREEN","PURPLE"]
        self.randomtext = random.randint(0,4)
        self.color = ["orange","yellow","blue","green","purple"]
        self.randomcolor = random.randint(0,4)
        randomcolor["text"] = self.text[self.randomtext]
        randomcolor["fg"] = self.color[self.randomcolor]
    def __update_score(self, input_value):
        if(input_value == self.color[self.randomcolor]):
            print(self.color[self.randomcolor])
            self.__score = self.__score + 1
            label_score["text"] = "Score : " + str(self.__score)
    def get_user_value(self, input_value):
        self.__update_score(input_value)
    
        
obj1 = game()

def getInput():
    value = input_value.get()
    obj1.get_user_value(value)
    obj1.updateGame()
    input_value.delete(0, END)
    
check = Button(root, text = "Check", command = getInput, bg = "pink", fg = "white", relief = FLAT, padx = 10, pady = 5, font = ("arial", 10))
check.place(relx = 0.4, rely = 0.6, anchor = CENTER)
btn = Button(root, text = "Start", command = obj1.updateGame, bg = "purple", fg = "white", relief = FLAT, padx = 10, pady = 5, font = ("arial", 10))
btn.place(relx = 0.6, rely = 0.6, anchor = CENTER)
root.mainloop()
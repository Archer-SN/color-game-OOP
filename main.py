from tkinter import *
import random
from time import sleep

class Game:

    def __init__(self,root):
        self.root = root
        self.colors = ['Red','Blue','Green','Pink','Black',
              'Yellow','Orange','White','Purple','Brown']
        #Points and Timer
        self.points = 0
        self.str_points = StringVar()
        self.str_points.set("Points: 0")
        self.points_counter = Label(root,textvariable=self.str_points)
        self.time = 30
        self.str_time = StringVar()
        self.str_time.set("Time: 30")
        self.time_counter = Label(root,textvariable=self.str_time)

        self.current_color = "White"
        self.input_color = Entry(root)
        self.enter_button = Button(root,command=self.enter,width=10,height=1,text="Enter")
        self.screen_color = Label(root,text="What is this color????",width=50,height=20,bg=self.current_color)

        self.time_counter.grid(column=0, row=2)
        self.points_counter.grid(column=0,row=3)
        self.screen_color.grid(column=1,row=0)
        self.input_color.grid(column=1,row=2)
        self.enter_button.grid(column=1,row=3)

        self.root.after(1000,self.timer)
        self.start()

    def timer(self):
        if self.time > 0:
            self.time -= 1
            self.str_time.set("Time: " + str(self.time))
        else:
            self.points -= 1
            self.str_points.set("Points: " + str(self.points))
            self.start()

        self.root.after(1000,self.timer)

    def start(self):
        self.time = 30
        self.current_color = random.choice(self.colors)
        self.screen_color.configure(bg=self.current_color)

    def enter(self):
        answer = self.input_color.get()
        if answer.upper() == self.current_color.upper():
            self.points += 1
            self.str_points.set("Points: " + str(self.points))
            self.start()

def main():
    root = Tk()
    game = Game(root)
    root.mainloop()

main()
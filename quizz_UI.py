from tkinter import *
from Fetch_use import Question
import html


class InterFace:
    def __init__(self):
        """Initial Black Screen"""
        self.screen_color = "#DFCB90"
        self.canvas_color = "#191E34"
        self.score = 0
        self.question = ''

        self.screen = Tk()
        self.screen.configure(bg=self.screen_color, height=500, width=400)

        self.canvas = Canvas(bg="black", height=400, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)
        self.canvas.create_text(150, 125, text=f"LET'S GO!!!!", fill="white", font=("Ariel", 20, "bold"))

        self.next_button = Button(width=10, height=5, borderwidth=0, text="Next----->")
        self.next_button.grid(column=0, row=2, pady=10, columnspan=2)
        self.next_button.configure(command=self.initial_screen)

        self.screen.mainloop()

    def initial_screen(self):
        """First Question Screen"""
        self.question = Question()
        self.qustn_text = html.unescape(self.question.qstn[0])

        self.score = self.score
        self.next_button.grid_forget()

        self.screen.configure(bg=self.screen_color, height=500, width=400)

        #question canvas
        self.canvas = Canvas(bg=self.canvas_color, height=400, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)
        self.canvas.create_text(150, 200, text=f"Q.{self.qustn_text}", fill="white", font=("Ariel", 17, "italic"),
                                width=250)


        #score text
        self.canvas.create_text(200, 25, text=f"Score:{self.score}", fill="white", font=("Ariel", 20, "italic"))

        # right button
        self.left_button = Button(width=10, height=5,borderwidth=0,text="True",command=self.check_true)
        self.left_button.grid(column=0, row=2, pady=10)


        # wrong button
        self.right_button = Button(width=10, height=5,borderwidth=0,text="False",command=self.check_false)
        self.right_button.grid(column=1, row=2, pady=10)


        self.screen.mainloop()

    def change_if_wrong(self):
        """After checking Screen if entered answer is wrong."""
        self.right_color = "#0FFA1A"
        self.wrong_color = "#FA0112"

        self.screen.configure(bg="#DFCB90", height=500, width=400)
        self.canvas_later = Canvas(bg=self.wrong_color, height=400, width=300)
        self.canvas_later.grid(column=0, row=1, columnspan=2, pady=20, padx=20)
        self.canvas_later.create_text(150, 125, text="NO!!!\nYou got it wrong.", fill="white",
                                      font=("Ariel", 20, "italic"))
        self.canvas_later.create_text(150, 175, text=f"Score:{self.score}", fill="white", font=("Ariel", 20, "italic"))
        self.right_button.grid_forget()
        self.left_button.grid_forget()

        self.next_button = Button(width=10, height=5, borderwidth=0, text="Next----->")
        self.next_button.configure()
        # self.next_button.configure(bg="black")
        self.next_button.grid(column=0, row=2, pady=10, columnspan=2)
        self.next_button.configure(command=self.initial_screen)
        self.canvas_later.mainloop()

    def change_if_right(self):
        """After checking Screen if entered answer is Right."""
        self.right_color = "#0FFA1A"
        self.wrong_color = "#FA0112"
        self.score += 1

        self.right_button.grid_forget()
        self.left_button.grid_forget()
        self.screen.configure(bg="#DFCB90", height=500, width=400)

        self.canvas_later = Canvas(bg=self.right_color, height=400, width=300)
        self.canvas_later.grid(column=0, row=1, columnspan=2, pady=20, padx=20)
        self.canvas_later.create_text(150, 125, text="YAY!!!!\nYou got it right. +1", fill="white",
                                      font=("Ariel", 20, "italic"))
        self.canvas_later.create_text(150, 175, text=f"Score:{self.score}", fill="white", font=("Ariel", 20, "italic"))

        self.next_button = Button(width=10, height=5, borderwidth=0, text="Next----->")


        self.next_button.grid(column=0, row=2, pady=10, columnspan=2)
        self.next_button.configure(command=self.initial_screen)
        self.canvas_later.mainloop()

    def check_true(self):
        """Right or wrong logic"""
        if self.question.answer[0] == "True":
            self.change_if_right()


        elif self.question.answer[0] == 'False':
            self.change_if_wrong()

    def check_false(self):
        """Right or wrong logic"""
        if self.question.answer[0] == 'False':
            self.change_if_right()

        elif self.question.answer[0] == "True":
            self.change_if_wrong()

    def next_bit(self):
        """Next Question"""
        self.initial_screen()

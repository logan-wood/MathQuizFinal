from tkinter import *
from random import *

class MathQuiz:

    def __init__(self, parent):

        self.frame1 = Frame(parent)
        self.frame1.grid(row=0, column=0)

        self.TitleLabel = Label(self.frame1, bg = "black", fg = "white", width = 20, padx = 30, pady = 10, text = "Welcome to Math Quiz", font=("Times", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)

        self.NameLabel = Label(self.frame1, text="Name: ", pady = 5)
        self.NameLabel.grid(row = 1, column = 0)

        self.name = StringVar()
        self.name.set("")
        self.NameEntry = Entry(self.frame1, textvariable = self.name, bg="white", fg="black")
        self.NameEntry.grid(row = 1, column = 1)

        self.AgeLabel = Label(self.frame1, text = "Age: ", pady = 5)
        self.AgeLabel.grid(row = 2, column = 0)

        self.age = IntVar()
        self.age.set("") 
        self.AgeEntry = Entry(self.frame1, textvariable = self.age, bg = "white", fg = "black")
        self.AgeEntry.grid(row = 2, column = 1)

        self.WarningLabel = Label(self.frame1, fg = "black", text ="")
        self.WarningLabel.grid(row = 3, column = 0, columnspan = 2)

        self.diff = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.diff)):
            rb = Radiobutton(self.frame1, variable = self.diff_lvl, value = i, text = self.diff[i], width = "10", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row = i+4, column = 0)

        self.button1 = Button(self.frame1, text = "Next", anchor = W, command = self.show_frame2)
        self.button1.grid(row = 4, column = 1)


        self.index = 0
        self.score = 0

        self.frame2 = Frame(parent)

        self.questions = Label(self.frame2, bg = "black", fg ="white", width = 20, padx = 30, pady = 10, text = "Answer Quiz Questions", font=("Times", "14", "bold italic"))
        self.questions.grid(columnspan = 2)

        self.QuestionNumber = Label(self.frame2, text="", width = 15, height = 3)
        self.QuestionNumber.grid(row = 2, column = 0)

        self.QuestionLabel = Label(self.frame2, text="", width = 15, height = 3)
        self.QuestionLabel.grid(row = 1, column = 0)
        
        self.AnswerEntry = Entry(self.frame2, text = "Answer...")
        self.AnswerEntry.grid(row = 1, column = 1)

        self.home = Button(self.frame2, text = "Home", command = self.show_frame1, pady = 5)
        self.home.grid(row = 3, column = 0)

        self.next_btn = Button(self.frame2, text = "Next", width = 5, command = self.next_problem, relief = RIDGE, pady = 5)
        self.next_btn.grid(row = 3, column = 1, sticky = E)

        self.check_btn = Button(self.frame2, text = "Check Answer", width= 12, command = self.check_answer, pady = 5)
        self.check_btn.grid(row = 3, column = 1, sticky = W)

        self.feedback = Label(self.frame2, fg = "black", text = "")
        self.feedback.grid(row = 2, column = 1)

        self.report_frame = Frame(parent, height = "450", width = "400")
        self.report_frame.grid_propagate(0)
        report_page = ["Name", "Age", "Score"]
        self.report_labels = []

        for i in range(len(report_page)):
            lb = Label(self.report_frame, text = report_page[i], width = "7", height = "2", font = ("Times", "22", "bold"))
            self.report_labels.append(lb)
            lb.grid(row = 1, column = i+1)

        self.report_name = Label(self.report_frame, textvariable = self.name)
        self.report_name.grid(row = 3 , column = 1)

        self.report_age = Label(self.report_frame, textvariable = self.age)
        self.report_age.grid(row = 3, column = 2)

        self.report_score = Label(self.report_frame, text = "")
        self.report_score.grid(row = 3, column = 2)

        self.home = Button(self.report_frame, text = "Home", command = self.show_frame1, pady = 10, width = 15)
        self.home.grid(row = 4, columnspan = 4)


    def show_frame2(self):
        try:
            
            if self.name.get() == "":
                self.WarningLabel.configure(text = "Please enter your name")
                self.NameEntry.focus()
            elif self.name.get().isalpha() == False:
                self.WarningLabel.configure(text = "Please enter text")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()

            elif self.AgeEntry.get() == "" :
                self.WarningLabel.configure(text = "Please enter a number")
                self.AgeEntry.delete(0, END)
            elif self.age.get() > 12:
                self.WarningLabel.configure(text = "You are too old to play this game")
                self.AgeEntry.delete(0, END)
            elif self.age.get() <= 0:
                self.WarningLabel.configure(text = "Please enter a number greater than 0")
                self.AgeEntry.delete(0, END)
            elif self.age.get() <=7:
                self.WarningLabel.configure(text = "You are too young to play this game")
            elif self.AgeEntry.get().isalpha() == True:
                self.WarningLabel.configure(text = "test")
                self.AgeEntry.delete(0, END)
            else:
                self.frame1.grid_remove()
                self.frame2.grid(row = 1, columnspan = 4)
                self.next_problem()


        except:
            self.WarningLabel.configure(text = "Please enter a number")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()

    def check_answer(self):
        try:
            ans = int(self.AnswerEntry.get())

            if ans == self.answer:
                self.feedback.configure(text = "Correct")
                self.score += 1
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_problem()

            else:
                self.feedback.configure(text ="Incorrect")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_problem()
                
        except:
            self.feedback.configure(text = "Please enter a number")
            self.AnswerEntry.delete(0, END)
            self.AnswerEntry.focus()

        if self.score <=5:
            self.report_score.configure(text = str(self.score))

    

    def show_frame1(self):
        self.frame2.grid_remove()
        self.frame1.grid()

    def next_problem(self):
        x = randrange(10)
        y = randrange(10)
        self.select = self.diff_lvl.get()

        if self.select == "0":
            easy_text = str(x) + " + " + str(y) + " = "
            
            self.answer = x + y
            self.index += 1

            self.QuestionLabel.configure(text = easy_text)
            self.QuestionNumber.configure(text = "Question " + str(self.index)+ "/5")

        elif self.select == "1":
            medium_text = str(x) + " - " + str(y) + " = "

            self.answer = x - y
            self.index += 1

            self.QuestionLabel.configure(text = medium_text)
            self.QuestionNumber.configure(text = "Question " + str(self.index)+ "/5")

        else:

            hard_text = str(x) + " * " + str(y) + " = "

            self.answer = x * y
            self.index += 1

            self.QuestionLabel.configure(text = hard_text)
            self.QuestionNumber.configure(text = "Question " + str(self.index)+ "/5")

        if self.index >= 6:
            self.frame2.grid_remove()
            self.report_frame.grid(row = 1, columnspan = 4)



if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Math Quiz")
    root.mainloop()

import json
import tkinter as tk
from random import randint

score = 0
answeredQues = -1


def loadData(quizType):
    quesAns = {}

    if quizType:
        quizFile = "Questions.json"

    else:
        quizFile = "Questions2.json"

    with open(quizFile) as data:
        for no, dataset in enumerate(json.load(data)["results"], start=1):
            quesAns.update({no: {dataset["question"]: dataset["answer"]}})

    no = randint(1, 50)
    ques = quesAns[no]
    quesAns.pop(no)
    for k, v in dict(ques).items():
        return k, v


def titleMenu(root2=None):
    global answeredQues
    global score

    try:
        answeredQues = 0
        score = 0
        root2.destroy()

    except:
        pass

    root = tk.Tk()
    bg = tk.PhotoImage(file="Quiz.gif")
    root.geometry("%dx450+500+200" % (bg.width()))
    root.iconbitmap("Quiz.ico")
    root.title("Quiz Maker")
    root.config(bg="black")
    root.resizable(False, False)

    topFrame = tk.Frame(root)
    topFrame.pack()

    cv = tk.Canvas(width=bg.width(), height=bg.height())
    cv.pack(side="top", fill="both", expand="yes")

    cv.create_image(0, 0, image=bg, anchor="nw")

    title = tk.Label(
        topFrame, text="Quiz Maker", fg="white", bg="black", font=("Calbri", "40")
    )
    title.pack(side=tk.TOP, anchor="n")

    mcqQ = tk.Button(
        cv,
        text="MCQ Quiz",
        fg="black",
        font=("Calbri", "18"),
        command=lambda: mcqQuiz(root),
    )
    mcqQ.pack(side=tk.LEFT, anchor="center")

    boolQ = tk.Button(
        cv,
        text="Bool Quiz",
        fg="black",
        font=("Calbri", "18"),
        command=lambda: boolQuiz(root),
    )
    boolQ.pack(side=tk.RIGHT, anchor="center")

    destroy = tk.Button(
        cv,
        text="Quit",
        fg="black",
        font=("Calbri", "21"),
        command=lambda: root.destroy(),
    )
    destroy.pack(side=tk.BOTTOM, anchor="center")

    root.mainloop()


def boolQuiz(root2=None):
    global answeredQues

    try:
        root2.destroy()
    except:
        pass

    answeredQues += 1

    root = tk.Tk()
    root.geometry("1400x100+75+300")
    root.iconbitmap("Quiz.ico")
    root.title("Bool Quiz")
    root.config(bg="black")
    root.resizable(False, False)

    topFrame = tk.Frame(root)
    topFrame.pack()

    bottomFrame = tk.Frame(root)
    bottomFrame.pack(side=tk.BOTTOM)

    quesText, ansText = loadData(True)

    ques = tk.Label(
        topFrame, text=quesText, bg="black", fg="white", font=("Calbri", "18")
    )
    ques.pack()

    true = tk.Button(
        bottomFrame,
        text="         \u2714 True         ",
        bg="black",
        fg="white",
        font=("Calbri", "18"),
        command=lambda: check(True, root, "True", ansText),
    )
    true.pack(side=tk.LEFT)

    false = tk.Button(
        bottomFrame,
        text="         \u2718 False        ",
        bg="black",
        fg="white",
        font=("Calbri", "18"),
        command=lambda: check(True, root, "False", ansText),
    )
    false.pack(side=tk.RIGHT)

    root.mainloop()


def mcqQuiz(root2=None):
    global answeredQues

    try:
        root2.destroy()
    except:
        pass

    answeredQues += 1

    root = tk.Tk()
    root.geometry("1400x100+75+300")
    root.iconbitmap("Quiz.ico")
    root.title("Bool Quiz")
    root.config(bg="black")
    root.resizable(False, False)

    topFrame = tk.Frame(root)
    topFrame.pack()

    bottomFrame = tk.Frame(root)
    bottomFrame.pack(side=tk.BOTTOM)

    quesText, options = loadData(False)
    correct = options[0]
    incorrect1 = options[1]
    incorrect2 = options[2]

    ques = tk.Label(
        topFrame, text=quesText, bg="black", fg="white", font=("Calbri", "18")
    )
    ques.pack()

    opt1 = tk.Button(
        bottomFrame,
        text=f"     {incorrect1}     ",
        bg="black",
        fg="white",
        font=("Calbri", "18"),
        command=lambda: check(False, root, incorrect1, correct),
    )
    opt1.pack(side=tk.LEFT)

    opt2 = tk.Button(
        bottomFrame,
        text=f"     {correct}     ",
        bg="black",
        fg="white",
        font=("Calbri", "18"),
        command=lambda: check(False, root, correct, correct),
    )
    opt2.pack(side=tk.LEFT)

    opt3 = tk.Button(
        bottomFrame,
        text=f"     {incorrect2}     ",
        bg="black",
        fg="white",
        font=("Calbri", "18"),
        command=lambda: check(False, root, incorrect2, correct),
    )
    opt3.pack(side=tk.RIGHT)

    root.mainloop()


def check(quizType, root, opt, ans):
    global score
    global answeredQues

    if quizType:
        quiz = boolQuiz

    else:
        quiz = mcqQuiz

    if answeredQues <= 4:
        if opt == ans:
            score = score + 1
            root.destroy()
            quiz()

        else:
            root.destroy()
            quiz()
    else:
        root.destroy()
        scoreCard()


def scoreCard():
    global score

    root = tk.Tk()
    root.geometry("600x200+500+350")
    root.iconbitmap("Quiz.ico")
    root.title("Score")
    root.resizable(False, False)

    topFrame = tk.Frame(root)
    topFrame.pack()

    title = tk.Label(
        topFrame,
        text=f"You Have Scored {score}/5 Points",
        fg="black",
        bg="white",
        font=("Calbri", "35"),
    )
    title.pack(side=tk.TOP, anchor="center")

    restart = tk.Button(
        topFrame,
        text="Try Again",
        fg="white",
        bg="black",
        font=("Calbri", "18"),
        command=lambda: titleMenu(root),
    )
    restart.pack(side=tk.TOP, anchor="center", padx=10, pady=10)

    destroy = tk.Button(
        topFrame,
        text="Quit",
        fg="white",
        bg="black",
        font=("Calbri", "21"),
        command=lambda: root.destroy(),
    )
    destroy.pack(side=tk.BOTTOM, anchor="center", padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    titleMenu()

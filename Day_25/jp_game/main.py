import turtle
import pandas

screen = turtle.Screen()
screen.title("J.P. States Game")

image = "jp.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("japan-prefectures.csv")
all_prefectures = data.prefecture.to_list()
guessed_prefectures = []

while len(guessed_prefectures) < 47:
    answer_prefectures = screen.textinput(title=f"{len(guessed_prefectures)}/47 Prefectures Correct", prompt="What's another prefecture's name").title()
    if answer_prefectures == "Exit":
        missing_prefctures = []
        for prefecture in all_prefectures:
            if prefecture not in guessed_prefectures:
                missing_prefctures.append(prefecture)
        new_data = pandas.DataFrame(missing_prefctures)
        new_data.to_csv("prefecture_to_learn.csv")
        break
    if answer_prefectures in all_prefectures:
        guessed_prefectures.append(answer_prefectures)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        prefecture_data = data[data.prefecture == answer_prefectures]
        t.goto(prefecture_data.x.item(), prefecture_data.y.item())
        t.write(answer_prefectures)


screen.exitonclick()
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high_score_records:
            self.high_score = int(high_score_records.read())
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    #def game_over(self):
        #self.goto(0, 0)
        #self.write(f"Game Over!", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as high_score_records:
                high_score_records.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_scores(self):
        self.score += 1
        self.update_scoreboard()


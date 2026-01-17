from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,250)
        self.increase_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f'GAME OVER \n SCORE : {self.score}',align='center',font= ('Arial',30,'bold'))
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False,
                   align=ALIGNMENT, font= FONT)
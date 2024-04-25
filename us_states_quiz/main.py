import turtle
from quizbrain import QuizBrain


brain = QuizBrain()

screen = turtle.Screen()
screen.title('US States Game')
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)



states_found = 0
while states_found < 50:
    answer_state = screen.textinput(title=f"Guess the State ({states_found}/50 found)", prompt="What's another state's name?").title()

    if answer_state == 'Check':
        brain.remaining_states()
        break
    check = brain.check_answer(answer_state)
    if check:
        states_found += 1
turtle.mainloop()

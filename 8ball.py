import random

#8 ball random value
r = random.randint(1, 9)

#Shake ball
def shake_ball():
       print("Shaking ....")

#8 ball answer
def eight_ball_answer(answer):
    if answer == 1:
           return 'It is certain'
    elif answer == 2:
           return 'It is decidedly so'
    elif answer == 3:
           return 'Yes'
    elif answer == 4:
           return 'Reply hazy try again'
    elif answer == 5:
           return 'Ask again later'
    elif answer == 6:
           return 'Concentrate and ask again'
    elif answer == 7:
           return 'My reply is no'
    elif answer == 8:
           return 'Outlook not so good'
    elif answer == 9:
           return 'Very doubtful'

# Call shake ball
shake_ball()

# Output eight ball result
print(eight_ball_answer(r))

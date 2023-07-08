print("Welcome to high score calculator")

scores = list(map(int, input(
    "Please enter all the scores in a comma seperated format. ").split(',')))

highest_score = 0 
for score in scores:
    if score > highest_score:
        highest_score = score

print("The highest score is {0}".format(highest_score))

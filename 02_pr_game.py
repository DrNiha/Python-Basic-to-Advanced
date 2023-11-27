def game():
    return 5258

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()

if int(hiScoreStr)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
elif hiScoreStr == '':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

    
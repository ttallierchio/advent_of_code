file = "input"
data = ""

WIN_PAIRS = {"A":"Y","B":"Z","C":"X"}
LOSS_PAIRS = {"A":"Z","B":"X","C":"Y"}
SHAPE_POINTS = {"X":1,"Y":2,"Z":3}

win = 6
loss = 0
draw = 3
with open(file,"r") as f:
    data = f.read()
score = 0
for x in data.split("\n"):
    op,me = x.split(" ")

    if WIN_PAIRS[op] == me:
        print("win")
        score += win + SHAPE_POINTS[me]
    elif LOSS_PAIRS[op] == me:
        print("lose")
        score += loss + SHAPE_POINTS[me]
    else:
        print("draw")
        score += draw + SHAPE_POINTS[me]
print(score)
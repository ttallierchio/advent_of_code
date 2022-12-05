file = "input"
data = ""

def win(op):
    me = WIN_PAIRS[op]
    return SHAPE_POINTS[me] + 6

def loss(op):
    me = LOSS_PAIRS[op]
    return SHAPE_POINTS[me]

def draw(op):
    me = DRAW_PAIRS[op]
    return SHAPE_POINTS[me] + 3

WIN_PAIRS = {"A":"Y","B":"Z","C":"X"}
LOSS_PAIRS = {"A":"Z","B":"X","C":"Y"}
DRAW_PAIRS = {"A":"X","B":"Y","C":"Z"}
SHAPE_POINTS = {"X":1,"Y":2,"Z":3}
ACTION = {"X":loss,"Y":draw,"Z":win}


win = 6
loss = 0
draw = 3
with open(file,"r") as f:
    data = f.read()

score = 0
for x in data.split("\n"):
    op,me = x.split(" ")
    score += ACTION[me](op)
print(score)
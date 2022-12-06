import string
file = "input"
data = ""

points = string.ascii_lowercase+string.ascii_uppercase
def calc_score(letter):
    return points.index(letter) + 1

with open(file,"r") as f:
    data = f.read()

sacks = data.split("\n")
total_doubles = 0
for sack in sacks:
    comp_1,comp_2 = sack[:len(sack)//2],sack[len(sack)//2:]
    letter = set(comp_1) & set(comp_2)
    print(letter)
    total_doubles += calc_score(list(letter)[0])
print(total_doubles)
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
i = 0 
while i < len(sacks):
    sack_1,sack_2,sack_3 = sacks[i],sacks[i+1],sacks[i+2]
    letter = set(sack_1) & set(sack_2) & set(sack_3)
    print(letter)
    total_doubles += calc_score(list(letter)[0])
    i += 3
print(total_doubles)
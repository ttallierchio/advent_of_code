file = "input"
data = ""
count = 0
with open(file,"r") as f:
    data = f.read()
for sections in data.split("\n"):
    section_1, section_2 = sections.split(",")
    a,b,c,d = section_1.split("-") +section_2.split("-")
    set_1 = set(range(int(a),int(b)+1))
    set_2 = set(range(int(c),int(d)+1))
    if len(set_1 - set_2) == 0 or len(set_2 - set_1) == 0:
        count += 1
print(count)

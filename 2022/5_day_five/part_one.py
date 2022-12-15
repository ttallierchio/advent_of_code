file = "input"
data = ""
count = 0
with open(file,"r") as f:
    data = f.read()

data_1,data_2 = data.split("\n\n")

lines = data_1.split("\n")

lines[-1] = lines[-1].replace("  ",",").replace(" ","")
max_col = max([int(x) for x in lines[-1].split(',')])

max_length = [len(x) for x in lines][0]


col_spots =  list(range(0,max_col))
col_spots = [1+ spot * 4 for spot in col_spots]

arrs = [""] * max_col
ld = ""
for x in lines[:len(lines)-1]:
    line_data = [ x[y] for y in col_spots]
    ld += ''.join(line_data) + "\n" 
    for idx,val in enumerate(line_data):
        if val != ' ':
            arrs[idx] += val
print(lines)
step = 0
for x in data_2.split("\n"):
    new_val = x.replace("move ","").replace(" from ",",").replace(" to ",",")
    instructions = [int(x) for x in new_val.split(",")]
    cnt = instructions[0]
    start = instructions[1] -1
    target = instructions[2] -1
    if start == 4 or target == 4:
        print(arrs,step,cnt,start,target)
    val = ""
    if  len(arrs[start]) - cnt < 0:
        print(start,cnt,target,x,arrs[start])

    val = arrs[start][:cnt]

    arrs[start] = arrs[start].replace(val,"",1)
    val = val[::-1]
    arrs[target] = val + arrs[target]
    
    step += 1

print(''.join([x[0] for x in arrs if len(x) > 0]))

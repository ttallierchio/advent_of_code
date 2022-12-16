file = "input"
data = ""
count = 0
with open(file,"r") as f:
    data = f.read().split("\n")
    
ROWS = len(data)
COLS = len(data[0])

EDGES = ROWS * 2 + (COLS-2) * 2
total = EDGES
for y in range(1,ROWS-1):
    for x in range(1,COLS-1):
        data_val = data[y][x]
        up = [data[y - i][x] for i in range(1,y +1)]
        down = [data[y + i][x] for i in range(1,ROWS-y)]
        left = [data[y][x-i] for i in range(1,x +1)]
        right = [data[y][x+ i] for i in range(1,COLS-x)]

        if max(up) < data_val or max(down) < data_val or max(left) < data_val or max(right) < data_val:
            total += 1
print(total)
        
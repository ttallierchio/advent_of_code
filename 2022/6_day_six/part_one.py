file = "input"
data = ""
count = 0
with open(file,"r") as f:
    data = f.read()
    
start = 0
while start <= len(data) -4:
    if len(set(data[start:start+4])) == 4:
       break
    start += 1
print(start + 4  )
    
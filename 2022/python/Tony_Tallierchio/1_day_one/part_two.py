file = "input"
data = ""


        
with open(file,"r") as f:
    data = f.read()

out = [sum(map(int,x.split("\n"))) for x in data.split("\n\n")]
print(sum(sorted(out,reverse=True)[:3]))
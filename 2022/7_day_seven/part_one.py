from typing import List

file = "input"
data = ""
count = 0
with open(file,"r") as f:
    data = f.read()

# oop for ease of access
class Node:
    pass

class Directory(Node):
    name:str
    files:List[Node]
    dirs:List[Node]
    parent_dir:Node
    
    def __init__(self,name,parent_dir=None):
        self.name = name
        self.parent_dir = parent_dir
        self.files = []
        self.dirs = []
        
    def get_dir(self,name) -> Node:
        return [x for x in self.dirs if x.name == name][0]
    
    def get_size(self) -> int:
        file_size = 0
        file_size = sum([x.size for x in self.files])
        file_size += sum([x.get_size() for x in self.dirs])
        return file_size
    
    def __repr__(self) -> str:
        return f"name:{self.name} - dirs:{len(self.dirs)} - files:{len(self.files)} parent - { self.parent_dir.name if self.parent_dir else 'None'}" 
      
class File():
    name:str
    size:int
    parent_dir:Node
    
    def __init__(self,name,size,parent_dir):
        self.name = name
        self.size = size
        self.parent_dir = parent_dir
    

# load the data
solve = Directory(name="/")
current_node = solve

for x in data.split("\n")[1:]:
    
    if x[0] =='$':
        if "cd " in x:
            if ".." in x:
                current_node = current_node.parent_dir
            else:
                current_node = current_node.get_dir(x.replace("$ cd ",""))
                
    elif x[:3] == "dir":
        current_node.dirs.append(Directory(name= x[4:],parent_dir=current_node))
        
    else:
        size,file_name =x.split(" ")
        current_node.files.append(File(name=file_name,size=int(size),parent_dir=current_node))

#solving
def navigate(root)-> int:
    return_val = 0
    for x in root.dirs:
        size = x.get_size()
        if size <= 100000:

            return_val += size
        return_val += navigate(x)
    return return_val

print(navigate(solve))
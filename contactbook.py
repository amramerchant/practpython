cb={"police":100}
def add(name,number):
    if name in cb:
        print("contact already exit")
    else:
        print("contact add sucessfully")
def delete(name):
    if name in cb:
        del cb[name]
        print("conctact delete sucessfully")
    else:
        print("no such contact found")
def update(name,newnumber):
    if name in cb:
        cb[name]=newnumber
        print("contact updated sucessfully")
    else:
        print("no such conctact exist")

def search(name):
    if name in cb:
        print(name, cb[name])
    else:
        print("no such contact found")
def display ():
    for k,v in cb.items():
        print(k,v)

#display()
add("amra",9900033448)
#delete("amra")
update("amra",77000234888)
search("amra")
display()
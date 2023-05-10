Nil=None

class File:
    def __init__(self,ndata) -> None:
        self.name = ndata[:ndata.find(".")]
        self.ext = ndata[ndata.find(".")+1:ndata.find(" ")+1]
        self.size = ndata[ndata.find(" ")+1:]
    
    def getWhole(self): 
        return self.name + "." + self.ext +self.size
    
class Directory:
    def __init__(self,nname:str) -> None:
        self.name=nname
        self.open=4

    def getWhole(self):
         return self.name
        
        
def Cons(x,n1=Nil,n2=Nil,n3=Nil,n4=Nil):
      return (x,n1,n2,n3,n4)

def data(xs):
        return xs[0]

def n1(xs):
        return xs[1]
    
def n2(xs):
        return xs[2]
 
def n3(xs):
        return xs[3]

def n4(xs):
        return xs[4]

def isEmpty(xs):
    if xs is Nil or xs is None:
        return True
    return False

def addC(ndata,xs:tuple)->tuple:
    if isEmpty(xs):
        return Cons(ndata,Nil,Nil,Nil,Nil)
    elif (n1(xs) and n2(xs) and n3(xs) and n4(xs)):
          return Cons(data(xs),addC(ndata,n1(xs)),n2(xs),n3(xs),n4(xs))
    else:
          if not n1(xs):
                return Cons(data(xs),addC(ndata,n1(xs)),n2(xs),n3(xs),n4(xs))
          elif not n2(xs):
                return Cons(data(xs),n1(xs),addC(ndata,n2(xs)),n3(xs),n4(xs))
          elif not n3(xs):
                return Cons(data(xs),n1(xs),n2(xs),addC(ndata,n3(xs)),n4(xs))
          elif not n4(xs):
                return Cons(data(xs),n1(xs),n2(xs),n3(xs),addC(ndata,n4(xs)))



def searchDir(xs:tuple,sname:str)->bool:
     if(xs):
          if data(xs).name==sname and type(data(xs)) == Directory:
               return True
          elif searchDir(n1(xs),sname) is True:
               return True
          elif searchDir(n2(xs),sname) is True:
               return True
          elif searchDir(n3(xs),sname) is True:
               return True
          elif searchDir(n4(xs),sname) is True:
               return True
          else:
               return False
          
def findDir(xs:tuple,sname:str)->tuple:
    if data(xs).name == sname and type(data(xs)) == Directory:
        return xs
    else:
        if n1(xs):
            return findDir(n1(xs),sname)
        if n2(xs):
            return findDir(n2(xs),sname)
        if n3(xs):
             return findDir(n3(xs),sname)
        if n4(xs):
             return findDir(n4(xs),sname)
            
               
          
     


def addB(ndata,xs:tuple,type:int,pardir:str)->tuple:
    def addFile(ndata,xs,pardir):
         if searchDir(xs,pardir):
              xss=findDir(xs,pardir)
              f = File(ndata)
              xsy = addC(f,xss)
              return xsy
    if type == 1:
         return addFile(ndata,xs,pardir)

              
         



def printTree(xs, prefix="", is_last=True):
    if xs is Nil:
        return

    # Print current node
    print(prefix, end="")
    print("└── " if is_last else "├── ", end="")
    print(data(xs).getWhole())

    # Print child nodes
    if n1(xs) and n2(xs) and n3(xs) and n4(xs):
        printTree(n1(xs), prefix + ("    " if is_last else "│   "), False)
        printTree(n2(xs), prefix + ("    " if is_last else "│   "), False)
        printTree(n3(xs), prefix + ("    " if is_last else "│   "), False)
        printTree(n4(xs), prefix + ("    " if is_last else "│   "), True)
    else:
        if n1(xs):
            printTree(n1(xs), prefix + ("    " if is_last else "│   "), (not n2(xs)))
        if n2(xs):
            printTree(n2(xs), prefix + ("    " if is_last else "│   "), (not n3(xs)))
        if n3(xs):
            printTree(n3(xs), prefix + ("    " if is_last else "│   "), (not n4(xs)))
        if n4(xs):
            printTree(n4(xs), prefix + ("    " if is_last else "│   "), True)





if __name__ == '__main__':
    X = Cons(Directory("Root"),Cons(Directory("Dir1"),Cons(File("file1.txt 42")),Cons(File("fil.cpp 1"))),Cons(File("ss.html 12")),Cons(File("aa.jpeg 52")))
    Y = addB("aa.txt 12",X,1,"Dir1")
    printTree(Y)      
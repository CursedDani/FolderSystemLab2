Nil=None

class Node:


    def __init__(self, data:str):
        self.name=data
        self.size=None
        self.ext=None
        
        
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

def add(ndata:int,xs:tuple):
    if isEmpty(xs):
        return Cons(ndata,Nil,Nil,Nil,Nil)
    elif (n1(xs) and n2(xs) and n3(xs) and n4(xs)):
          return Cons(data(xs),add(ndata,n1(xs)),n2(xs),n3(xs),n4(xs))
    else:
          if not n1(xs):
                return Cons(data(xs),add(ndata,n1(xs)),n2(xs),n3(xs),n4(xs))
          if not n2(xs):
                return Cons(data(xs),n1(xs),add(ndata,n2(xs)),n3(xs),n4(xs))
          if not n3(xs):
                return Cons(data(xs),n1(xs),n2(xs),add(ndata,n3(xs)),n4(xs))
          if not n4(xs):
                return Cons(data(xs),n1(xs),n2(xs),n3(xs),add(ndata,n4(xs)))

def printTree(xs, indent=0, is_last=False):
   if xs is Nil:
      return

   # Print current node
   print(" " * indent, end="")
   if is_last:
      print("└──", end="")
   else:
      print("├──", end="")
   print(data(xs))

   # Print child nodes
   if n1(xs) and n2(xs) and n3(xs) and n4(xs):
      printTree(n1(xs), indent=indent+4, is_last=False)
      printTree(n2(xs), indent=indent+4, is_last=False)
      printTree(n3(xs), indent=indent+4, is_last=False)
      printTree(n4(xs), indent=indent+4, is_last=True)
   else:
      if n1(xs):
         printTree(n1(xs), indent=indent+4, is_last=(not n2(xs)))
      if n2(xs):
         printTree(n2(xs), indent=indent+4, is_last=(not n3(xs)))
      if n3(xs):
         printTree(n3(xs), indent=indent+4, is_last=(not n4(xs)))
      if n4(xs):
         printTree(n4(xs), indent=indent+4, is_last=True)


if __name__ == '__main__':
        X = Nil
        b =add(1,X)
        c = add(2,b)
        d = add(3,c)
        X = add(4,X)
        X = add(5,d)
        X = add(6,X)
        X = add(7,X)
        X = add(8,X)
        X = add(9,X)
        X = add(10,X)
        X = add(11,X)
        printTree(b)
        print()        
        printTree(c)
        print()        
        printTree(d)
        print()        
        printTree(X)        
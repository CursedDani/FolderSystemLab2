Nil=None

class Node:


    def __init__(self, data:str):
        self.data = data



def Cons(x,n1,n2,n3,n4):
        return (x,n1,n2,n3,n4)

def head(xs):
        return xs[0]

def next1(xs):
        return xs[1]
    
def next2(xs):
        return xs[2]
 
def next3(xs):
        return xs[3]

def next4(xs):
        return xs[4]

def isEmpty(xs):
    if xs is Nil:
        return True
    return False

def add(self,ndata:int,xs:tuple):
    if isEmpty(xs):
        return Cons(ndata,Nil,Nil,Nil,Nil)
    else:

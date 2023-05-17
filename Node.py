Nil=None

def File(ndata:str)->tuple:
    name = ndata[:ndata.find(".")]
    ext = ndata[ndata.find("."):ndata.find(" ")]
    size = ndata[ndata.find(" "):]
    return (ndata,name,ext,size)
    
def Directory(nname:str,open=4) -> tuple:
    name=nname + "*"
    vopen=open
    return (name,vopen)
        
        
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


def searchDir(xs:tuple,sname:str)->bool:
     if(xs):
          if data(data(xs))==sname and isDir(xs):
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
          
def searchFile(xs,sname):
     if(xs):
          print(data(data(xs)))
          if n1(data(xs))==sname and isFile(xs):

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



def printTree(xs, prefix="", is_last=True):
    if xs is Nil:
        return

    # Print xs node
    print(prefix, end="")
    print("└── " if is_last else "├── ", end="")
    print(data(data(xs)))

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


def isDir(xs:tuple)->bool:
        if len(data(xs)) == 2:
             return True
        return False
        
def isFile(xs)->bool:
     if len(data(xs)) == 4:
          return True
     return False

    
def addDirectory(fxs,fparDir,nDirectory):
        def addOnDir(fxsa,nDirectorya):
            if not n1(fxsa):
                return Cons(data(fxsa),Cons(Directory(nDirectorya)),n2(fxsa),n3(fxsa),n4(fxsa))
            elif not n2(fxsa):
                return Cons(data(fxsa),n1(fxsa),Cons(Directory(nDirectorya)),n3(fxsa),n4(fxsa))
            elif not n3(fxsa):
                return Cons(data(fxsa),n1(fxsa), n2(fxsa) , Cons(Directory(nDirectorya)),n4(fxsa))
            elif not n4(fxsa):
                return Cons(data(fxsa),n1(fxsa),n2(fxsa),n3(fxsa),Cons(Directory(nDirectorya)))
            else:
                 print("Directory Full")
            
        if fxs and searchDir(fxs,fparDir):
            if data(data(fxs)) == fparDir and isDir(fxs):
                return addOnDir(fxs,nDirectory)
            elif searchDir(n1(fxs),fparDir):
                return Cons(data(fxs),addDirectory(n1(fxs),fparDir,nDirectory),n2(fxs),n3(fxs),n4(fxs))
            elif searchDir(n2(fxs),fparDir):
                return Cons(data(fxs),n1(fxs),addDirectory(n2(fxs),fparDir,nDirectory),n3(fxs),n4(fxs))
            elif searchDir(n3(fxs),fparDir):
                return Cons(data(fxs),n1(fxs),n2(fxs),addDirectory(n3(fxs),fparDir, nDirectory),n4(fxs))
            elif searchDir(n4(fxs),fparDir):
                return Cons(data(fxs),n1(fxs),n2(fxs),n3(fxs),addDirectory(n4(fxs),fparDir,nDirectory))

        
def addFile(fxs,fparDir,nFile):
        def addOnDir(fxsa,nFilea):
            if not n1(fxsa):
                return Cons(data(fxsa),Cons(File(nFilea)),n2(fxsa),n3(fxsa),n4(fxsa))
            elif not n2(fxsa):
                return Cons(data(fxsa),n1(fxsa),Cons(File(nFilea)),n3(fxsa),n4(fxsa))
            elif not n3(fxsa):
                return Cons(data(fxsa),n1(fxsa), n2(fxsa) , Cons(File(nFilea)),n4(fxsa))
            elif not n4(fxsa):
                return Cons(data(fxsa),n1(fxsa),n2(fxsa),n3(fxsa),Cons(File(nFilea)))
            else:
                 print("Directory Full")
            
        if fxs and searchDir(fxs,fparDir):
            if data(data(fxs)) == fparDir and isDir(fxs):
                return addOnDir(fxs,nFile)
            elif searchDir(n1(fxs),fparDir):
                return Cons(data(fxs),addFile(n1(fxs),fparDir,nFile),n2(fxs),n3(fxs),n4(fxs))
            elif searchDir(n2(fxs),fparDir):
                return Cons(data(fxs),n1(fxs),addFile(n2(fxs),fparDir,nFile),n3(fxs),n4(fxs))
            elif searchDir(n3(fxs),fparDir):
                return Cons(data(fxs),n1(fxs),n2(fxs),addFile(n3(fxs),fparDir, nFile),n4(fxs))
            elif searchDir(n4(fxs),fparDir):
                return Cons(data(fxs),n1(fxs),n2(fxs),n3(fxs),addFile(n4(fxs),fparDir,nFile))


def delete(xs,name):
     if xs and searchDir(xs,name):
          if data(data(xs)) == name:
               return Nil
          elif searchDir(n1(xs),name):
               return Cons(data(xs),delete(n1(xs),name),n2(xs),n3(xs),n4(xs))
          elif searchDir(n2(xs),name):
               return Cons(data(xs),n1(xs),delete(n2(xs),name),n3(xs),n4(xs))
          elif searchDir(n3(xs),name):
               return Cons(data(xs),n1(xs),n2(xs),delete(n3(xs),name),n4(xs))
          elif searchDir(n4(xs),name):
               return Cons(data(xs),n1(xs),n2(xs),n3(xs),delete(n4(xs),name))   


def Modify(xs,oName):
     def modFile(fxsa,nFilea):
            if not n1(fxsa):
                return Cons(data(fxsa),Cons(File(nFilea)),n2(fxsa),n3(fxsa),n4(fxsa))
            elif not n2(fxsa):
                return Cons(data(fxsa),n1(fxsa),Cons(File(nFilea)),n3(fxsa),n4(fxsa))
            elif not n3(fxsa):
                return Cons(data(fxsa),n1(fxsa), n2(fxsa) , Cons(File(nFilea)),n4(fxsa))
            elif not n4(fxsa):
                return Cons(data(fxsa),n1(fxsa),n2(fxsa),n3(fxsa),Cons(File(nFilea)))
     
     


def showPath(name: str, xs, path="/"):
  
  l = []
  if (xs):

    if (data(data(xs)) == name):
      l.append( path + data(data(xs)))
    else:
      n1S = showPath(name, n1(xs),
                             f'{ path}{data(data(xs))}/')
      if (n1S):
        l.append(n1S)

      n2S = showPath(name, n2(xs),
                              f'{path}{data(data(xs))}/')
      if (n2S):
        l.append(n2S)

      n3S = showPath(name, n3(xs),
                              f'{path}{data(data(xs))}/')

      if (n3S):
        l.append(n3S)
      n4S = showPath(name, n4(xs),
                              f'{path}{data(data(xs))}/')
      if (n4S):
        l.append(n4S)
    return l
    
          
             
             
             
            
     



if __name__ == '__main__':
    X = Cons(Directory("Root"),Cons(Directory("Dir1"),Cons(File("file1.txt 42")),Cons(File("fil.cpp 1"))),Cons(Directory("Dir2")),Cons(File("aa.jpeg 52")))
    Y = addDirectory(X,"Root*","aaaa")
    Z = addFile(Y,"aaaa*","asasa.aa 12")
    W = addDirectory(Z,"Dir2*","Dir1")
    a = delete(W,"Dir1*")
    print(showPath("Dir1*",W))
    printTree(a)      
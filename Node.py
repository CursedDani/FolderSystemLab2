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
          if data(data(xs))==sname and len(data(xs)) == 2:
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
'''        
def findDir(xs:tuple,sname:str)->tuple:
    if data(data(xs)) == sname and len(data(xs)) == 2:
        return xs
    else:
        if n1(xs):
            return xs + findDir(n1(xs),sname)
        if n2(xs):
            return xs + findDir(n2(xs),sname)
        if n3(xs):
             return xs + findDir(n3(xs),sname)
        if n4(xs):
             return xs + findDir(n4(xs),sname)
'''        



            
               
          
     

'''
def addB(ndata,xs:tuple,type:int,pardir:str)->tuple:
    def isDir(xs:tuple)->bool:
        if len(data(xs)) == 2:
             return True
        else:
             return False
    
    def isFile(xs:tuple)->bool:
         if len(xs) == 4:
              return True
         else:
              return False
          
    def addFile(nFile,fxs,fpardir):
         if searchDir(fxs,fpardir):
            if fxs:
                if isFile(nFile):
                    if data(data(fxs)) == fpardir:
                           if(n1(fxs)):
                                addFile(nFile,n1(fxs),fpardir)
                           else:
                                return Cons(data(fxs),Cons(nFile),n2(fxs),n3(fxs),n4(fxs))
                           if n2(fxs):
                                addFile(nFile,n2(fxs),fpardir)
                           else:
                                return Cons(data(fxs),n1(fxs),Cons(nFile),n3(fxs),n4(fxs))
                           if n3(fxs):
                                addFile(nFile,n3(fxs,fpardir))
                           else:
                                return Cons(data(fxs),n1(fxs),n2(fxs),Cons(nFile),n4(fxs))
                           if n4(fxs):
                                addFile(nFile,n4(fxs,fpardir))
                           else:
                                return Cons(data(fxs),n1(fxs),n2(fxs),n3(fxs),Cons(nFile))
                    elif addFile(nFile,n1(fxs),fpardir):
                         return Cons(data(fxs),addFile(nFile,n1(fxs),fpardir))
                    elif addFile(nFile,n2(fxs),fpardir):
                         return Cons(data(fxs),addFile(nFile,n2(fxs),fpardir))
                    elif addFile(nFile,n3(fxs),fpardir):
                         return Cons(data(fxs),addFile(nFile,n3(fxs),fpardir))
                    elif addFile(nFile,n4(fxs),fpardir):
                         return Cons(nFile,n4(fxs),fpardir)
                           

    if type == 1:
         return addFile(File(ndata),xs,pardir)
'''   



def printTree(xs, prefix="", is_last=True):
    if xs is Nil:
        return

    # Print current node
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
        else:
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



'''
def add_folder_on_folder(sub_tree, new_node):
  if(left(sub_tree) is Nil):
    return Node(update_elements(sub_tree),Node(Folder(new_node)),midleft(sub_tree),midright(sub_tree),right(sub_tree))
  elif(midleft(sub_tree) is Nil):
    return Node(update_elements(sub_tree),left(sub_tree),Node(Folder(new_node)),midright(sub_tree),right(sub_tree))
  elif(midright(sub_tree) is Nil):
    return Node(update_elements(sub_tree), left(sub_tree),midleft(sub_tree), Node(Folder(new_node)),right(sub_tree))
  elif(right(sub_tree) is Nil):
    return Node(update_elements(sub_tree), left(sub_tree),midleft(sub_tree),midright(sub_tree), Node(Folder(new_node)))

def add_file_on_folder(sub_tree: tuple, new_file_name: str, weight: int):
  data_file= data_name_file(new_file_name)
  if(left(sub_tree) is Nil):
    return Node(object(sub_tree), Node(File(data_file[0],data_file[1],weight)),midleft(sub_tree),midright(sub_tree),right(sub_tree))
  elif(midleft(sub_tree) is Nil):
    return Node(object(sub_tree),left(sub_tree),Node(File(data_file[0],data_file[1],weight)),midright(sub_tree),right(sub_tree))
  elif( midright(sub_tree) is Nil):
    return Node(object(sub_tree), left(sub_tree),midleft(sub_tree), Node(File(data_file[0],data_file[1],weight)),right(sub_tree))
  elif(right(sub_tree) is Nil):
    return Node(object(sub_tree), left(sub_tree),midleft(sub_tree),midright(sub_tree), Node(File(data_file[0],data_file[1],weight)))

def add_folder(sub_tree, folder_name, new_name, choice):
  if(sub_tree and search_node(sub_tree,folder_name)):
      if(name_object(sub_tree)==folder_name and is_folder(sub_tree)):
        return add_folder_on_folder(sub_tree,new_name)
      elif(search_node(left(sub_tree), folder_name)):
        return Node(object(sub_tree), add_folder(left(sub_tree), folder_name, new_name,choice),midleft(sub_tree),midright(sub_tree),right(sub_tree))
      elif(search_node(midleft(sub_tree),folder_name)):
        return Node(object(sub_tree), left(sub_tree), add_folder(midleft(sub_tree), folder_name,new_name,choice),midright(sub_tree),right(sub_tree))
      elif(search_node(midright(sub_tree),folder_name)):
        return Node(object(sub_tree), left(sub_tree), midleft(sub_tree),add_folder(midright(sub_tree), folder_name, new_name,choice),right(sub_tree))
      elif((search_node(right(sub_tree), folder_name))):
        return Node(object(sub_tree), left(sub_tree), midleft(sub_tree),midright(sub_tree),add_folder(right(sub_tree),folder_name,new_name,choice))
  else:
      return
    
def add_file(sub_tree, folder_name, new_file_name, weight):
  if(sub_tree and search_node(sub_tree,folder_name)):
      if(name_object(sub_tree)==folder_name and is_folder(sub_tree)):
        return add_file_on_folder(sub_tree, new_file_name,weight)
      elif(search_node(left(sub_tree), folder_name)):
        return Node(object(sub_tree), add_file(left(sub_tree), folder_name, new_file_name,weight),midleft(sub_tree),midright(sub_tree),right(sub_tree))
      elif(search_node(midleft(sub_tree),folder_name)):
        return Node(object(sub_tree), left(sub_tree), add_file(midleft(sub_tree), folder_name, new_file_name,weight),midright(sub_tree),right(sub_tree))
      elif(search_node(midright(sub_tree),folder_name)):
        return Node(object(sub_tree), left(sub_tree), midleft(sub_tree),add_file(midright(sub_tree), folder_name, new_file_name,weight),right(sub_tree))
      elif((search_node(right(sub_tree), folder_name))):
        return Node(object(sub_tree), left(sub_tree), midleft(sub_tree),midright(sub_tree),add_file(right(sub_tree),folder_name,new_file_name, weight))
  else:
      return

'''



if __name__ == '__main__':
    X = Cons(Directory("Root"),Cons(Directory("Dir1"),Cons(File("file1.txt 42")),Cons(File("fil.cpp 1"))),Cons(Directory("Dir2")),Cons(File("aa.jpeg 52")))
    Y = addDirectory(X,"Root*","aaaa")
    Z = addFile(Y,"aaaa*","asasa.aa 12")
    printTree(Z)      
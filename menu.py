def Menu():
    print("*************** WELCOME ***************")
    while True:
        print("Select an option\n1)Show all files/directories\n2)Add new file\n3)Add new directory\n4)Modify existing file\n5)Modify existing directory\n0)Exit")
        menuOption = input()
        if menuOption is 0:
            print("Closing system...\n")
            break
        elif menuOption is 1:
            pass
        elif menuOption is 2:
            pass
        elif menuOption is 3:
            pass
        elif menuOption is 4:
            while True:
                print("**** Select an option ****\n1)Delete a file\n2)Change file attributes\n0)Cancel")
                fileMenuOption = input()
                if fileMenuOption is 0:
                    print("Cancelling...")
                    break
                elif fileMenuOption is 1:
                    pass
                elif fileMenuOption is 2:
                    pass
                else:
                    print("//////ERROR////// \n invalid option, please select a valid one")
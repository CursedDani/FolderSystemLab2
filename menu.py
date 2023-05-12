def Menu():
    print("*************** WELCOME ***************")
    while True:
        print("Select an option\n1)Show all files/directories\n2)Add new file\n3)Add new directory\n4)Modify existing file\n5)Modify existing directory\n0)Exit")
        menuOption = input()
        if menuOption == 0:
            print("Closing system...\n")
            break
        elif menuOption == 1:
            pass
        elif menuOption == 2:
            pass
        elif menuOption == 3:
            pass
        elif menuOption == 4:
            while True:
                print("**** Select an option ****\n1)Delete a file\n2)Change file attributes\n0)Cancel")
                fileMenuOption = input()
                if fileMenuOption == 0:
                    print("Cancelling...")
                    break
                elif fileMenuOption == 1:
                    pass
                elif fileMenuOption == 2:
                    pass
                else:
                    print("//////ERROR////// \n invalid option, please select a valid one")
        elif menuOption == 5:
            while True:
                print("**** Select an option ****\n1)Delete a directory\n2)Change directory name\n0)Cancel")
                dirMenuOption = input()
                if dirMenuOption == 0:
                    print("Cancelling...")
                    break
                elif dirMenuOption == 1:
                    pass
                elif dirMenuOption == 2:
                    pass
                else:
                    print("//////ERROR////// \n invalid option, please select a valid one")
        else:
            print("//////ERROR////// \n invalid option, please select a valid one")


if __name__ == '__main__':
    Menu()
#Open a text file
with open("personal_info.txt", "a") as info_lib:
    personne= []
    while True:
        while True:
            while True:
                info= input("Provide us a minimum of five personal information about you: ")
                personne.append(info)
                if len(personne) >=5:
                    break

            add = input("Would you like to input more data (y/n)? ")
            while True:
                if add == "y":
                    print ("Add more data")
                    break
                elif add == "n":
                    break
                elif add != "y" and add != "n":
                    print ("Wrong Format, try again")
            if add == "n":
                break


        entry= input("Would you like to store another set of information (y/n)? ")
        while True:
            if entry == "y":
                print("Please store another set of info")
                break
            elif entry == "n":
                break
            elif entry != "y" and entry != "n":
                print ("Wrong format")
        if entry == "n":
            break

    for pers in personne:
        info_lib.write(pers)

#Place a loop
#Create five input statements
#Create conditions to end the loop
#Place a command that ask users if they want to input a new entry, if yes, new loop, if no, end the loop and write entry on the text file


'''
       __________________________________________________________
       This was actually a very fun one to work on. 
       This is a bank with drawl system 
       features: withdrawl no overdraw reciept/no reciept and rembering old bank balance
       though of note this code can be very voilitile as writing to it self can be risky
       __________________________________________________________
       '''
# Line below should remain empty

bl = 10000.0                                                          #---------------------------- look here for current info
# the line above this one represents the balance in your acount.
# this is remebered in between sessions of banking.
# this is done by modefing the python file it self.
print()
print()
# formating and gathering user inputs
print("___________________________________________________")
print(("Current Funds                              ${:.2f}").format(bl))
# withdrawl amount
wth = float(input("Please Enter Funds You Wish To Withdraw $"))

# reciept || yes or no
receipt = input("Do You Want A Reciept Yes/No ")
# quickly lowercases everything so no issues arrise from some one saying YeS
receipt = receipt.lower()
print("___________________________________________________")
# if some one tries to withdraw more money than they have
if wth > bl:
    print("                   Insuficint Funds")
    print("___________________________________________________")
    print("    We Thank You For Your Continued Business")
# if the user asked for a reciept and has enough money
elif wth < bl and receipt == "yes":
    # the next few lines are just formating and telling you balance
    print("                  Digital Receipt")
    print("___________________________________________________")
    print(("Past Funds                                 ${:.2f}").format(bl))
    total = bl - wth
    print('Funds Withdrawn                            $%7.2f' % (wth))
    print(("New Total Funds                            ${:.2f}").format(total))
    print("___________________________________________________")
    print("    We Thank You For Your Continued Business")
    # now this is the fun thing i found
    # first it creats a list

    # ------ Read Portion
    content = []
    with open(__file__, "r") as f:
        for line in f:
            # then line by line it adds it into the list until it gets through whole list
            content.append(line)

    with open(__file__, "w") as f:
        # for content to work you must go 1 below where you want the new edited line
        # this simply takes the infromation from the user and puts into into the list
        # which it will then be written to the document again
        # the line is so it sticks out more when writting as it needs to be changed if the spacing gets thrown off
        content[10] = "        bl = {n}\n".format(n=bl - wth)  # ______________________________
        for i in range(len(content)):
            # begins writting te docoument
            f.write(content[i])
    # the all import close
    f.close()
elif wth < bl and receipt == "no":
    # prints " nothing " as requested
    print("            No Digital Receipt Requested")
    print("___________________________________________________")
    print("    We Thank You For Your Continued Business")
    # refer to comments at line 302 as the following code is the exact same
    content = []
    with open(__file__, "r") as f:
        for line in f:
            content.append(line)

    with open(__file__, "w") as f:

        content[10] = "        bl = {n}\n".format(n=bl - wth)  # ______________________________
        for i in range(len(content)):
            f.write(content[i])
    # the all import close
    f.close()
    # finished of by printinga  simple dash
print("___________________________________________________")

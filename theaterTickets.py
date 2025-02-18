seating=[ #prices of all 46 seats.
    [40, 50, 50, 50, 50, 50, 50, 40],
    [30, 30, 40, 50, 50, 40, 30, 30],
    [20, 30, 30, 40, 40, 30, 30, 20],
    [10, 20, 20, 20, 20, 20, 20, 10],
    [10, 20, 20, 20, 20, 20, 20, 10],
    [10, 20, 20, 20, 20, 20, 20, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10]]

while True: #main loop
    print("")
    itr=0
    for i in range(len(seating)):
        print("[$",seating[i][0],"]","[$",seating[i][1],"]","[$",seating[i][2],"]","[$",seating[i][3],"]","[$",seating[i][4],"]","[$",seating[i][5],"]","[$",seating[i][6],"]","[$",seating[i][7],"]",sep="")
    if seating==[["00"]*8]*9: #if all seats are taken, exit
        print("Sorry, we're booked.")
        print("Have a nice day!")
        exit()
    seatCol=(input("Welcome to the theater! Please enter the column of the seat you want. (0-7) "))
    if seatCol=="sold": #shortcut to sell all seats
        seating=[["00"]*8]*9
        print ("all seats are now sold out.")
        continue
    seatCol=int(seatCol) #shortcut is a string, so we need to convert to an integer after we check for it.
    seatRow=int(input("Now, input the row of the seat you want. (0-8) ")) #for the collumn, since we aren't checking for a shortcut anymore, we can set the variable to an integer immediately.
    if seatCol>7 or seatCol<0 or seatRow>8 or seatRow<0: #detect bad seat coordinates
        print("Sorry, we don't have that many seats.")
        continue
    if seating[seatRow][seatCol]=="00": #detect taken seat
        print("Sorry, that seat's taken.")
        continue
    print("Okay! That'll be ","$",seating[seatRow][seatCol],".",sep="") #update seating chart
    seating[seatRow][seatCol]="00"
    print("Next in line, please!")
    continue


    

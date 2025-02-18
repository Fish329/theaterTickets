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
    itr=0
    nxt=7
    for i in seating:
        pass
    #unfinished. TODO: print an aesthetically pleasing seating chart
    print("")
    if seating==[[0]*8]*9: #if all seats are taken, exit
        print("Sorry, we're booked.")
        exit()
    seatCol=(input("Welcome to the theater! Please enter the column of the seat you want. (0-7) "))
    if seatCol=="sold": #cheat
        seating=[[0]*8]*9
        print ("all seats are now sold out.")
        continue
    seatCol=int(seatCol)
    seatRow=int(input("Now, input the row of the seat you want. (0-8) "))
    if seatCol>7 or seatCol<0 or seatRow>8 or seatRow<0:
        print("Sorry, we don't have that many seats.")
        continue
    if seating[seatCol][seatRow]==0:
        print("Sorry, that seat's taken.")
        continue

    

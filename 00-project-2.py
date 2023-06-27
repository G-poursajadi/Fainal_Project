print("priject2-gol ya pouch")

number_faild = 0
UniNmber = input("lotfan Shomare Daneshjoie khod ra vared konid:")
password = input("lotfan password khod ra vared konid:")
while UniNmber != 1234 and password != "5678" :
    print("password ya Shomare Daneshjoie shoma eshtebahe ")
    number_faild =+  1
    
    UniNmber = input("dobare Shomare Daneshjoie khod ra vared konid:")    
    password = input("dobare passwoed khod ra vared konid:")
print("vared shodid")
print("------------------------------------------------------------")
print("\n")

Emtiazp1 = 0
Emtiazp2 = 0

while Emtiazp1<6 and Emtiazp2<6:
    import random
    randomnum = random.randint(1,2)
    if randomnum == 1 :
        player2 = "rast"
    elif randomnum == 2 :
        player2 = "chap"

    print("daste rast ya chap")
    player1 = input ("gol kojasat? Rast ya chap  ? -- ").lower()

    if player1 == player2:
        print(f"dorost gofti {player2}")
        Emtiazp1 +=1
        print(f"emtiaze shoma: {Emtiazp1} va emtize computer: {Emtiazp2}")
        print("\n")

        # print("nobat shoma ast:")
        # hand_player1 = input("gol ro to kodom dast migiri? - rast ya chap - ")

        # if randomnum == 1 :
        #     player2 = "rast"
        # elif randomnum == 2 :
        #     player2 = "chap"

        # while hand_player1 != player2:
        #     print("computer eshtebah goft emtiaz migiri ")
        #     Emtiazp1 +=1
        #     print(f"emtiaze shoma: {Emtiazp1} va emtize computer: {Emtiazp2}")
        #     print("\n")
            

        # print("computer dorost goft emtiz nemigiri")
        # Emtiazp2 +=1
        # print(f"emtiaze shoma: {Emtiazp1} va emtize computer: {Emtiazp2}")
        # print("\n")


    elif player1 != player2 :
        print(f"eshtebah gofti emtiaz nemighiri")
        Emtiazp2 +=1
        print(f"emtiaze shoma: {Emtiazp1} va emtize computer: {Emtiazp2}")
        print("\n")
    

    else :
        print("eshtebah nevshti do bare emtehan kon")

print(f"emtiaze shoma: {Emtiazp1} va emtize computer: {Emtiazp2}")
print("bazi tamom shod")

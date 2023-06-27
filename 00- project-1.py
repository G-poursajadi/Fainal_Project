print("priject1-Sang-Kaghaz-gheichi")

number_faild = 0
UniNmber = input("lotfan Shomare Daneshjoie khod ra vared konid--")
password = input("lotfan password khod ra vared konid--")
while UniNmber != 1234 and password != "5678" :
    print("password ya Shomare Daneshjoie shoma eshtebahe ")
    number_faild =+  1
    
    UniNmber = input("dobare Shomare Daneshjoie khod ra vared konid--")    
    password = input("dobare passwoed khod ra vared konid--")
print("vared shodid")

# 
print("------------------------------------------------------------")
print("\n")
# 

emtiazeP1 = 0
emtiazeP2 = 0

while emtiazeP1 <3 and emtiazeP2 <3:
    import random
    print("Sang-Kaghaz-gheichi")
    player1 = input ("Harekat khod ra vared konid:").lower()
    randomnum = random.randint(1,3)
    if randomnum == 1 :
        player2 = "sang"
    elif randomnum == 2 :
        player2 = "kaghaz"
    elif randomnum == 3 :
        player2 = "gheichi"
    print(player2)

    if player1 == player2 :
        print("Mosavi")

        print(f"emtiaze player1={emtiazeP1} va emtiaze computer={emtiazeP2}")
        print("-------------------------------------------------")
        print("\n")
    elif player1 == "sang" and player2 =="kaghaz" :
        print("Player2 win")
        emtiazeP2 = emtiazeP2+1
        print(f"emtiaze player1={emtiazeP1} va emtiaze computer={emtiazeP2}")
        print("-------------------------------------------------")
        print("\n")
    elif player1 == "sang" and player2 =="gheichi" :
        print("Player1 win")
        emtiazeP1 = emtiazeP1+1
        print(f"emtiaze player1={emtiazeP1} va emtiaze computer={emtiazeP2}")
        print("-------------------------------------------------")
        print("\n")
    elif player1 == "kaghaz" and player2 =="sang" :
        print("Player1 win")
        emtiazeP1 = emtiazeP1+1
        print(f"emtiaze player1={emtiazeP1} va emtiaze computer={emtiazeP2}")
        print("-------------------------------------------------")
        print("\n")
    elif player1 == "kaghaz" and player2 =="gheichi" :
        print("Player2 win")
        emtiazeP2 = emtiazeP2+1
        print(f"emtiaze player1={emtiazeP1} va emtiaze computer={emtiazeP2}")
        print("-------------------------------------------------")
        print("\n")
    elif player1 == "gheichi" and player2 =="sang" :
        print("Player2 win")
        emtiazeP2 = emtiazeP2+1
        print(f"emtiaze player1={emtiazeP1} va emtiaze computer={emtiazeP2}")
        print("-------------------------------------------------")
        print("\n")
    elif player1 == "gheichi" and player2 =="kaghaz" :
        print("Player1 win")
        emtiazeP1 = emtiazeP1+1
        print(f"emtiaze player1={emtiazeP1} va emtiaze computer={emtiazeP2}")
        print("-------------------------------------------------")
        print("\n")
    else :
        print("Harekat shoma eshtebah mibashad")
        print("-------------------------------------------------")
        print("\n")

print("\n")
print(f"emtize player 1 : {emtiazeP1}")
print(f"emtize player 2 : {emtiazeP2}")
print("bazi tamom shod")
from random import randint

players_hand = randint(1, 21)
dealers_hand = randint(1, 21)

print("You have $1000!")
print(f"Your hand is {players_hand} and the dealers hand is {dealers_hand}...")
bet = int(input("How much money do you want to bet? "))
win = bet * 2
money = 1000
loose = -bet
if bet > money:
    print("You dont have that much money:")
    bet = int(input("How much money do you want to bet? "))
    print(f"Your hand is {players_hand} and the dealers hand is {dealers_hand}...")

while 1 == 1:
    ask1 = int(input("Do you want to (1) hit or (2) stand? "))
    if ask1 == 1:
        players_hand = players_hand + randint(2, 10)
        print(
            f"Your hand is now {players_hand} and the dealers hand is now {dealers_hand}..."
        )
        if players_hand > 21:
            print("You lost...")
            print(
                f"Your hand is now {players_hand} and the dealers hand is now {dealers_hand}..."
            )
            money = money + loose
            break
        if players_hand == 21:
            print("You got a BlackJack!!!")
            money = money + 2 * win
            break
    elif ask1 == 2 and dealers_hand < 18:
        dealers_hand = dealers_hand + randint(2, 10)
        print(
            f"Your hand is now {players_hand} and the dealers hand is now {dealers_hand}..."
        )
        if dealers_hand > 21:
            print("The dealer bust...")
            print("You win!!!")
            print(
                f"Your hand is now {players_hand} and the dealers hand is now {dealers_hand}..."
            )
            money = money + win
            break
        if dealers_hand > 18:
            break
print(
    f"Your hand is now {players_hand} and the dealers hand is now {dealers_hand}..."
)
while dealers_hand < 22 and players_hand < 22:
    player_acuracy = 21 - players_hand
    dealer_acuracy = 21 - dealers_hand
    if player_acuracy < dealer_acuracy:
        print("You win!!!")
        print(f"You earned ${win}")
        money = money + win
    if player_acuracy == dealer_acuracy:
        print("You tied the dealer...")
        money = money + bet
    if player_acuracy > dealer_acuracy:
        print("You lost...")
        money = money + loose
print(money)

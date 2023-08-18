import random
from art import logo

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def stat_print(player,dealer):
    print(f"Your cards : {player}, current score : {sum(player)}")
    print(f"Computer's first card : {dealer[0]}")

def final_print(player,dealer):
    print(f"Your final hand : {player}, final score : {sum(player)}")
    print(f"Computer's final hand : {dealer}, final score : {sum(dealer)}")

def check_winner(player,dealer):
    
    if sum(player)<21:
        if sum(player)> sum(dealer):
            print("You win")
        elif sum(dealer)>21:
            print("You win")
        else:
            print("You lose")
    elif sum(player)>21:
        print("You lose")
    elif sum(player)==sum(dealer):
        print("It's a draw")


def blackjack():
    print(logo)
    dealer = []
    player = []

    for _ in range(2):
        dealer.append(deal_cards())
        player.append(deal_cards())

    stat_print(player,dealer)
    flag = False
    game_continue = True
    while game_continue:
        if input("type 'y' to get another card, type 'n' to pass : ") == 'y':
            player.append(deal_cards())
            if sum(player)>21 and 11 in player:
                idx = player.index(11)
                player[idx] = 1
            
            if sum(player) == 21 or sum(dealer)>21:
                final_print(player,dealer)
                print("You win")
                flag = True
            elif sum(dealer) == 21 or sum(player)>21:
                final_print(player,dealer)
                print("You lose")
                flag = True
            
            else:
                stat_print(player,dealer)


        else:
            while  sum(dealer)<17:
                dealer.append(deal_cards())
                if sum(dealer)>=21 and 11 in player:
                    idx = player.index(11)
                    player[idx] = 1
                    
            final_print(player,dealer)
            check_winner(player,dealer)
            flag = True

        if flag:
            if input("type 'y' to play another game, type 'n' to end : ") == 'y':
                game_continue = False
                blackjack()
            else:
                return
            
if input("type 'y' to play a game of blackjack, type 'n' to exit : ") == 'y':
    blackjack()
                
                
    



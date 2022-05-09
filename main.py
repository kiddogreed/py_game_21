import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    return random.choice(cards)


def calculated_score(cards):
    if sum == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, bot_score):
    if user_score == bot_score:
        return "Draw"
    elif bot_score == 0:
        return "You lose , bot has 21"
    elif user_score == 0:
        return "You win with 21"
    elif user_score > 21:
        return "you bust"
    elif bot_score > 21:
        return "bot bust"
    elif user_score > bot_score:
        return "You win "
    elif user_score < bot_score:
        return "You lose"
    else:
        return "You lose"


def playgame():
    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculated_score(user_cards)
    bot_score = calculated_score(computer_cards)

    while not game_over:

        print(f"Your cards:{user_cards}, current score: {user_score}")
        print(f"bot cards:{computer_cards[0]}")
        if user_score == 0 or bot_score == 0 or user_score > 21:
            game_over = True
        else:
            user_continue = input("Type 'y' to draw another card and 'n' if not")
            if user_continue == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while bot_score != 0 and bot_score < 17:
        computer_cards.append(deal_card())
        bot_score = calculated_score(computer_cards)

    print(f"Your final cards:{user_cards} and your score:{user_score}")
    print(f"botl cards:{computer_cards} and score:{bot_score}")
    print(compare(user_score, bot_score))


while input("Do you want to play 21 'y' to yes and 'n' to no:") == "y":

    playgame()
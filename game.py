# Write your code here
import random


def choose_game() -> list[str]:
    game_choice = input()
    if game_choice == '':
        return ['paper', 'scissors', 'rock']
    else:
        options = game_choice.split(',')
        return options


def get_results(game_choice: list[str], players_choice: str, player_rating: int) -> int:
    computer_choice = random.choice(game_choice)
    chosen_index = game_choice.index(players_choice)
    # index for amount of losing/winning options
    index_range = int((len(game_choice) - 1) / 2)
    # all winning options in a list
    winning_options = [game_choice[chosen_index - i] for i in range(1, index_range + 1)]
    if computer_choice == players_choice:
        print(f'There is a draw ({computer_choice})')
        player_rating += 50
    elif computer_choice in winning_options:
        print(f'Well done. The computer chose {computer_choice} and failed')
        player_rating += 100
    else:
        print(f'Sorry, but the computer chose {computer_choice}')
    return player_rating


def get_player_name() -> str:
    player_name = input('Enter your name: ')
    print(f'Hello, {player_name}')
    return player_name


def get_player_rating(player_name: str) -> int:
    player_rating = 0

    # Read lines until player's name found, get his/her rating
    file = open('rating.txt', 'r')
    for line in file:
        name_rating = line.strip().split(sep=' ')
        if player_name == name_rating[0]:
            player_rating = int(name_rating[1])
            break
    file.close()

    return player_rating


def play_game(player_rating: int, game_choice: list[str]) -> None:
    print('Okay, let\'s start')
    while True:
        players_choice = input()
        if players_choice == '!exit':
            print('Bye!')
            break
        elif players_choice == '!rating':
            print(f'Your rating: {player_rating}')
        elif players_choice in game_choice:
            player_rating = get_results(game_choice, players_choice, player_rating)
        else:
            print('Invalid input')


if __name__ == '__main__':
    name = get_player_name()
    rating = get_player_rating(name)
    choice = choose_game()
    play_game(rating, choice)

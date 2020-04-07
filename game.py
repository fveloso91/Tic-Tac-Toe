# write your code here
import random
from math import inf as infinity


def easy():
    coord1 = random.randint(1, 3)
    coord2 = random.randint(1, 3)
    return coord1, coord2


def medium(a, b, c, d, e, f, g, h, i):
    inputs = [a, b, c, d, e, f, g, h, i]
    words = ["X", "O"]
    for _ in range(len(inputs)):
        if inputs[_] == " ":
            for word in words:
                inputs[_] = word
                a, b, c, d, e, f, g, h, i = inputs
                if wins_loses(word, a, b, c, d, e, f, g, h, i) == "{} wins".format(word.upper()):
                    if _ == 0: return 1, 3
                    elif _ == 1: return 2, 3
                    elif _ == 2: return 3, 3
                    elif _ == 3: return 1, 2
                    elif _ == 4: return 2, 2
                    elif _ == 5: return 3, 2
                    elif _ == 6: return 1, 1
                    elif _ == 7: return 2, 1
                    elif _ == 8: return 3, 1

    coord1 = random.randint(1, 3)
    coord2 = random.randint(1, 3)
    return coord1, coord2


def hard(a, b, c, d, e, f, g, h, i):
    return medium(a, b, c, d, e, f, g, h, i)


def wins_loses(word, a, b, c, d, e, f, g, h, i):
    if word == a == b == c:
        return "{} wins".format(word.upper())
    elif word == d == e == f:
        return "{} wins".format(word.upper())
    elif word == g == h == i:
        return "{} wins".format(word.upper())
    elif word == a == e == i:
        return "{} wins".format(word.upper())
    elif word == c == e == g:
        return "{} wins".format(word.upper())
    elif word == a == d == g:
        return "{} wins".format(word.upper())
    elif word == b == e == h:
        return "{} wins".format(word.upper())
    elif word == c == f == i:
        return "{} wins".format(word.upper())


def win_loose_condition(a, b, c, d, e, f, g, h, i):
    inputs = [a, b, c, d, e, f, g, h, i]
    count_x = inputs.count("X")
    count_o = inputs.count("O")
    count_space = inputs.count(" ")
    if wins_loses("X", a, b, c, d, e, f, g, h, i) == "X wins" and wins_loses("O", a, b, c, d, e, f, g, h, i) == "O wins":
        return "Impossible"
    elif wins_loses("X", a, b, c, d, e, f, g, h, i) == "X wins":
        return "X wins"
    elif wins_loses("O", a, b, c, d, e, f, g, h, i) == "O wins":
        return "O wins"
    elif count_o >= count_x + 2 or count_x >= count_o + 2:
        return "Impossible"
    # elif count_space > 0:
    #    print("Game not finished")
    elif count_x == count_o and count_x + count_o == 9:
        return "Draw"
    elif count_x + count_o == 9:
        return "Draw"


while True:
    a, b, c, d, e, f, g, h, i = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    dictionary_fields = {
        (1, 3): a,
        (2, 3): b,
        (3, 3): c,
        (1, 2): d,
        (2, 2): e,
        (3, 2): f,
        (1, 1): g,
        (2, 1): h,
        (3, 1): i
    }
    coord_possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    last_input = "O"

    game_starting = input("Input command: ").split()

    if len(game_starting) == 3 and game_starting[0] == "start":
        user1 = game_starting[1]
        user2 = game_starting[2]

        while True:
            a = dictionary_fields[(1, 3)]
            b = dictionary_fields[(2, 3)]
            c = dictionary_fields[(3, 3)]
            d = dictionary_fields[(1, 2)]
            e = dictionary_fields[(2, 2)]
            f = dictionary_fields[(3, 2)]
            g = dictionary_fields[(1, 1)]
            h = dictionary_fields[(2, 1)]
            i = dictionary_fields[(3, 1)]

            print("""
                    ---------
                    | {} {} {} |
                    | {} {} {} |
                    | {} {} {} |
                    ---------
                    """.format(a, b, c, d, e, f, g, h, i))

            if win_loose_condition(a, b, c, d, e, f, g, h, i):
                print(win_loose_condition(a, b, c, d, e, f, g, h, i))
                break

            else:
                if last_input == "O":
                    user = user1
                else:
                    user = user2

                if user == "easy":
                    print('Making move level "easy"')
                elif user == "medium":
                    print('Making move level "medium"')
                elif user == "hard":
                    print('Making move level "hard"')

                while True:
                    if user == "easy":
                        # user_input = [int(x) for x in input("Enter the coordinates {}: ".format(user)).split()]
                        # coord1, coord2 = user_input
                        coord1, coord2 = easy()

                    elif user == "medium":
                        coord1, coord2 = medium(a, b, c, d, e, f, g, h, i)

                    elif user == "hard":
                        coord1, coord2 = hard(a, b, c, d, e, f, g, h, i)

                    else:
                        user_input = [int(x) for x in input("Enter the coordinates {}: ".format(user)).split()]
                        try:
                            coord1, coord2 = user_input
                        except ValueError:
                            print("You should enter two coordinates!")
                            continue

                    if (coord1 or coord2) not in coord_possibilities:
                        if user != "easy" and user != "medium" and user != "hard":
                            print("You should enter numbers!")
                        continue
                    elif (coord1 or coord2) > 3:
                        if user != "easy" and user != "medium" and user != "hard":
                            print("Coordinates should be from 1 to 3!")
                        continue
                    elif dictionary_fields[(coord1, coord2)] != " ":
                        if user != "easy" and user != "medium" and user != "hard":
                            print("This cell is occupied! Choose another one!")
                        continue
                    else:
                        if last_input == "O":
                            dictionary_fields[(coord1, coord2)] = "X"
                            last_input = "X"
                            break
                        elif last_input == "X":
                            dictionary_fields[(coord1, coord2)] = "O"
                            last_input = "O"
                            break

    elif game_starting[0] == "exit":
        break

    else:
        print("Bad parameters!")

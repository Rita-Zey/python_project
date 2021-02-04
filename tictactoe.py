# write your code here
x_or_o = list("         ")  # получаем лист с данными о ячейках
# лист с "ключами" для нахождения соответсвия между ячейкой и вводом игрока
my_list = [[0, "1 1"], [1, "1 2"], [2, "1 3"],
           [3, "2 1"], [4, "2 2"], [5, "2 3"],
           [6, "3 1"], [7, "3 2"], [8, "3 3"]]


def print_result():
    print("---------")
    print("|", x_or_o[0], x_or_o[1], x_or_o[2], "|")
    print("|", x_or_o[3], x_or_o[4], x_or_o[5], "|")
    print("|", x_or_o[6], x_or_o[7], x_or_o[8], "|")
    print("---------")


wins_x = [3, 3, 3, 3, 3, 3, 3, 3]
wins_o = [3, 3, 3, 3, 3, 3, 3, 3]


print_result()

number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
number3 = ["1", "2", "3"]
count = 0
move = "X"

while count == 0:
    coordinates = input("Enter the coordinates: ")
    if coordinates[0] not in number and coordinates[2] not in number:
        print("You should enter numbers!")
        continue
    if coordinates[0] not in number3 or coordinates[2] not in number3:
        print('Coordinates should be from 1 to 3!')
        continue
    for n in my_list:
        if coordinates == n[1]:
            i = n[0]
            if x_or_o[i] == "X" or x_or_o[i] == "O":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                if move == "X":
                    x_or_o.pop(i)
                    x_or_o.insert(i, "X")
                    print_result()
                    move = "O"
                    if i == 0 or i == 1 or i == 2:
                        wins_x[0] -= 1
                    if i == 3 or i == 4 or i == 5:
                        wins_x[1] -= 1
                    if i == 6 or i == 7 or i == 8:
                        wins_x[2] -= 1
                    if i == 0 or i == 3 or i == 6:
                        wins_x[3] -= 1
                    if i == 1 or i == 4 or i == 7:
                        wins_x[4] -= 1
                    if i == 2 or i == 5 or i == 8:
                        wins_x[5] -= 1
                    if i == 2 or i == 4 or i == 6:
                        wins_x[6] -= 1
                    if i == 0 or i == 4 or i == 8:
                        wins_x[7] -= 1
                    if 0 in wins_x:
                        print("X wins")
                        count = 1
                        break
                else:
                    x_or_o.pop(i)
                    x_or_o.insert(i, "O")
                    print_result()
                    move = "X"
                    if i == 0 or i == 1 or i == 2:
                        wins_o[0] -= 1
                    if i == 3 or i == 4 or i == 5:
                        wins_o[1] -= 1
                    if i == 6 or i == 7 or i == 8:
                        wins_o[2] -= 1
                    if i == 0 or i == 3 or i == 6:
                        wins_o[3] -= 1
                    if i == 1 or i == 4 or i == 7:
                        wins_o[4] -= 1
                    if i == 2 or i == 5 or i == 8:
                        wins_o[5] -= 1
                    if i == 2 or i == 4 or i == 6:
                        wins_o[6] -= 1
                    if i == 0 or i == 4 or i == 8:
                        wins_o[7] -= 1
                    if 0 in wins_o:
                        print("O wins")
                        count = 1
                        break
            if " " not in x_or_o:
                print("Draw")
                count = 1

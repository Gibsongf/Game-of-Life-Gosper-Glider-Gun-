import copy


def edge_cells(original, modificado):
    x = original
    uno = [x[0][0], x[0][1], x[1][0], x[1][1]].count(1)
    t_count = [x[0][-1], x[0][-2], x[1][-1], x[1][-2]].count(1)
    ult = [x[-1][0], x[-1][1], x[-2][0], x[-2][1]].count(1)
    mos = [x[-1][-1], x[-1][-2], x[-2][-1], x[-2][-2]].count(1)
    check(original, modificado, uno, row=0, colum=0)
    check(original, modificado, uno, row=0, colum=-1)
    check(original, modificado, ult, row=-1, colum=0)
    check(original, modificado, mos, row=-1, colum=-1)
def slic(board, copy):  # slice and send to another function
    c = 0
    first_time = True
    for n in range(len(board)):
        last_num = len(board)-1
        if n >= 3:
            three_lst = board[c:n]
            c = c+1
            send_tocheck(board, copy, three_lst, c)
            if first_time:
                top_bot(board, copy, lst=three_lst[:2], lst_indx=0)
                first_time = False
        if n == last_num:
            last_two_lst_three = board[c:]
            c = c+1
            top_bot(board, copy, lst=last_two_lst_three[:2], lst_indx=-1)
            send_tocheck(board, copy, last_two_lst_three, c)
def top_bot(board, copy, lst, lst_indx):
    indx = 0
    last_index = 3
    while True:
        count_lst = []
        for i in lst:
            count_lst.extend(i[indx:last_index])

        if len(count_lst) < 6:
            break
        count_one = count_lst.count(1)
        indx += 1
        last_index += 1
        check(board, copy, count_one, lst_indx, indx)
def send_tocheck(original, copia, three_lst, lst_indx):

    num_index = 0
    row = 3
    first_check = 0
    last_check = 0
    while True:
        middle = []
        first_two = []
        last_two = []
        for k, v in enumerate(three_lst):
            if k <= 2:
                first_two.extend(v[:2])
                last_two.extend(v[-2:])
                middle.extend(v[num_index:row])

        if len(first_two) < 9 and first_check == 0:  # sending to check first and second colum
            first_check += 1
            count_one = first_two.count(1)
            check(original, copia, count_one, lst_indx, 0)
        if len(last_two) < 9 and last_check == 0:  # sending to check last two colum
            last_check += 1
            count_one = last_two.count(1)
            check(original, copia, count_one, lst_indx, -1)

        elif len(middle) < 9:
            break
        num_index = num_index+1
        row = row+1
        count_one = middle.count(1)
        # sending to check the middle of the board
        check(original, copia, count_one, lst_indx, num_index)
def check(lst, copy, count_one, row, colum):
    if lst[row][colum] == 1 and count_one > 4:
        copy[row][colum] = 0

    elif lst[row][colum] == 1 and count_one == 3 or lst[row][colum] == 1 and count_one == 4:
        copy[row][colum] = 1

    elif lst[row][colum] == 1 and count_one == 2 or lst[row][colum] == 1 and count_one == 1:
        copy[row][colum] = 0

    elif lst[row][colum] == 0 and count_one == 3:
        copy[row][colum] = 1

def render(board):
    x = []
    c = 0
    while c != len(board):
        t = ['▀'if x == 0 else ' 'for x in board[c]]
        x.append(t)
        c = c+1
    for i in range(len(x)):
        rend = ' '.join(x[i])
        print('', rend.rjust(len(x), ' '), '')

life =[ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
copy_life = copy.deepcopy(life)
edge_cells(life, copy_life)
slic(life, copy_life)
render(life)
for n in range(0, 50):
    life_c = copy.deepcopy(copy_life)
    edge_cells(life_c, copy_life)
    slic(life_c, copy_life)
    render(copy_life)

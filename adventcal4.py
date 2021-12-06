import csv

bingo = csv.reader(open('bingotest.csv'))
bingo_list = list(bingo)
bingo_draw = [num[0] for num in bingo_list[0]]
bingo_cards = []


i = 2
while i < len(bingo_list):
    bingo_cards.append(bingo_list[i])
    i = i + 1

def position_cards():
    count_cards = 0
    index_cards = []
    for row in bingo_cards:
        count_cards = count_cards + 1
        #empty array = new card
        if not row:
            index_cards.append(count_cards - 6)
    return index_cards
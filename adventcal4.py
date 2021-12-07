import csv

bingo = csv.reader(open('bingotest.csv'))
bingo_list = list(bingo)
bingo_draw = [num[0] for num in bingo_list[0]]
bingo_cards = []

#construct a list with only bingo cards
i = 2
while i < len(bingo_list):
    bingo_cards.append(bingo_list[i])
    i += 1

def position_cards():
    count_cards = 0
    index_cards = []
    for row in bingo_cards:
        count_cards +=  1
        #empty array = new card
        if not row:
            index_cards.append(count_cards - 6)
    return index_cards

def one_card(index):
    card = []
    for i in range(5):
        row = bingo_cards[index][0].split(' ')
        card.append(row)
        index += 1
    return card

def find_draw(list_index):
    card = one_card(0)
    for draw in bingo_draw:
        for row in card:
            if draw in row:
                print("test")

find_draw(position_cards)
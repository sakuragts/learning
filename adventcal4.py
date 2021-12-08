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

#makes an array containing the first index of each card
def position_cards():
    count_cards = 0
    index_cards = []
    for index, row in enumerate(bingo_cards):
        count_cards +=  1
        #empty array = new card
        if not row:
            index_cards.append(count_cards - 6)
        if index + 5 == len(bingo_cards):
            index_cards.append(index)
    return index_cards

#configure each number to individual string in each row 
# of a card and returns in as an array 
def one_card(index):
    card = []
    for i in range(5):
        row = bingo_cards[index][0].split(' ')
        while '' in row:
            row.remove('')
        card.append(row)
        index += 1
    return card

def find_draw(draw, card):
    list_found_in_card = []
    found_in_card = []
    index_cards = position_cards()
       
    for row in card:
        for num in row:
            if draw == num:
                found_in_card.append(True)
            else:
                found_in_card.append(False)
        list_found_in_card.append(found_in_card.copy())
        found_in_card.clear()
    return list_found_in_card
    
print(find_draw('7', one_card(0)))
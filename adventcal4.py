import csv

bingo = csv.reader(open('bingotest.csv'))
bingo_list = list(bingo)
bingo_draw = [num[0] for num in bingo_list[0]]
bingo_cards = []

i = 2
while i < len(bingo_list):
    bingo_cards.append(bingo_list[i])
    i = i + 1

for i in range(5):
    for row in bingo_cards:
        print(row)
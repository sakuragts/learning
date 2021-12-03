import csv

horizontal = 0
depth = 0

direction_file = csv.reader(open('directions.csv'))
directions = list(direction_file)

#transforme en liste de string
strdirections = []
for string in directions:
    strdirections.append(string[0])

def forward(steps):
    global horizontal
    horizontal = horizontal + steps

def down(steps):
    global depth
    depth = depth + steps

def up(steps):
    global depth
    depth = depth - steps

def multiply(hor, dep):
    return hor * dep


def convert_dir(direction):
    for word in direction.split():
        if word.isdigit():
            step = int(word)
        else:
            dir = word
    if "forward" in dir:
        forward(step)
    if "down" in dir:
        down(step)
    if "up" in dir:
        up(step)

for i in range(len(strdirections)):
    convert_dir(strdirections[i])

print(multiply(horizontal, depth))
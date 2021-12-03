import csv

horizontal = 0
depth = 0

direction_file = csv.reader(open('directions.csv'))
directions = list(direction_file)
directions = [str(direction) for direction in directions]

print(directions)

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

forward(5)
down(5)
forward(8)
up(3)
down(8)
forward(2)
print(multiply(horizontal, depth))
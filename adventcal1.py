import csv

def day1_1():
    entry = csv.reader(open('entries.csv'))
    results = list(entry)

    i = 0
    increase = 0
    issame = 0
    
    for data in results:
        if i < len(results) - 1:
            if data < results[i + 1]:
                increase = increase + 1
        i = i + 1  
    print(increase)
    
day1_1()
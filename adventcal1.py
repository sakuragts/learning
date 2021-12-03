import csv

entry = csv.reader(open('entries.csv'))
results = list(entry)
#change les valeurs de str à int
results = [int(elem[0]) for elem in results] 

def day1_1():
    i = 0
    increase = 0
    
    for data in results:
        if i < len(results) - 1:
            if data < results[i + 1]:
                increase = increase + 1
        i = i + 1  
    print(increase)


def day1_2():
    listsums = []
    increase = 0
    for i in range(len(results) - 2):
        sum = results[i] + results[i+1] + results[i+2]
        listsums.append(sum)
    for i in range(len(listsums) - 1):
        if listsums[i] < listsums[i + 1]:
            increase = increase + 1
            
    print(increase)

day1_2()
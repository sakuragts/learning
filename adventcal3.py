import csv

diagnostic = csv.reader(open('diagnostic.csv'))
results = list(diagnostic)
strresults = []
for string in results:
    strresults.append(string[0])

gamma = ''
epsilon = ''

def convert_entry(results):
    global gamma
    global epsilon
    zero = 0
    one = 0
    for i in range(len(results[0])):
        for j in range(len(results)):
            if results[j][i] == '0':
                zero = zero + 1
            else:
                one = one + 1
        if zero < one:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        zero = 0
        one = 0

def multi_decimal():
    global gamma
    global epsilon
    deci_gamma = int(gamma, 2)
    deci_epsilon = int(epsilon, 2)
    return deci_gamma * deci_epsilon

    

test = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

convert_entry(strresults)
print(multi_decimal())
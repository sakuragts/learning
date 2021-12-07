import csv

diagnostic = csv.reader(open('diagnostic.csv'))
binaries = list(diagnostic)
strresults = []
for string in binaries:
    strresults.append(string[0])

gamma = ''
epsilon = ''
o2gen = ''
co2scrub = ''
most = True

def compare_bit(binaries, bit):
    zero = 0
    one = 0
    for binary in binaries:
        if binary[bit] == '0':
            zero += 1
        else:
            one += 1
    if zero <= one:
        return 1
    else:
        return 0

def add_bit(binaries, ind, value):
    temp = []
    for binary in binaries:
        if binary[ind] == value:
            temp.append(binary)
    return temp

def multi_decimal():
    global gamma
    global epsilon
    deci_gamma = int(gamma, 2)
    deci_epsilon = int(epsilon, 2)
    return deci_gamma * deci_epsilon

def compiled_results(binaries, ind, most):
    temp = []
    
    if compare_bit(binaries, ind) == 0:
        if most:                
            temp = add_bit(binaries, ind, '0')
        else:
            temp = add_bit(binaries, ind, '1')
    if compare_bit(binaries, ind) == 1:
        if most:
            temp = add_bit(binaries, ind, '1')
        else:
            temp = add_bit(binaries, ind, '0')
    return temp
 
def o2results(binaries):
    global o2gen
    temp = []
    for i in range(len(binaries[0]) + 1):
        if not temp:
            temp = compiled_results(binaries, i, True)
        elif len(temp) == 1:
            o2gen = temp[0]
        else:
            temp = compiled_results(temp, i, True)
    

def co2results(results):
    global co2scrub
    temp = []
    for i in range(len(results[0])):
        if not temp:
            temp = compiled_results(results, i, False)
        elif len(temp) == 1:
            co2scrub = temp[0]
        else:
            temp = compiled_results(temp, i, False)


test = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

o2results(strresults)
co2results(strresults)
print(int(o2gen, 2) * int(co2scrub, 2))

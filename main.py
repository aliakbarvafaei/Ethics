import json
import os



path = os.listdir('scenarios')
path = sorted(path)


for file in path:

    f = open(f'scenarios/{file}')
    data = json.load(f)


    resultFile = open(f'results/{file.split(".")[0]}-result.txt', 'w')
    des = data['description']
    resultFile.write(f'All the obtained results are based on the school of pluralism.\n\n')
    resultFile.write(f'{des}:\n\n')


    resultFile.write(f'Utilities:\n')
    utility = dict(data['utilities'])
    utils = list(utility)[::-1]
    
    while len(utils) > 0:
        a = utils.pop()
        b = utils.pop()
        if utility[a] > utility[b]:
            resultFile.write(f'   {a} => good\n')
            resultFile.write(f'   {b} => bad\n')
        else:
            resultFile.write(f'   {a} => bad\n')
            resultFile.write(f'   {b} => good\n')
    resultFile.write('\n')


    maximum = float('-inf')
    value = None
    
    for i,j in utility.items():
        if j > maximum:
            maximum = j
            value = i
    resultFile.write(f'The best choise :\n   {value} with {maximum} score.\n\n')


    mechanism = dict(data['mechanisms'])
    intention = []
    
    for i,j in mechanism.items():
        if type(j) == str:
            if j == value:
                intention.append(i)
        elif type(j) == list:
            if value in j:
                intention.append(i)
    resultFile.write(f'The intention of this problem :\n   for action "{value}"\n   is consequence')
    for item in intention[0:len(intention) - 1:]:
        resultFile.write(f'"{item}" and ')
    if len(intention)>0:
        resultFile.write(f'"{intention[len(intention) - 1]}".\n')
    else:
        temp=""
        action = data['actions']
        for item in action:
            if item != value:
                temp=item
        intention = []
    
        for i,j in mechanism.items():
            if type(j) == str:
                if j == temp:
                    intention.append(i)
            elif type(j) == list:
                if temp in j:
                    intention.append(i)
        for item in intention[0:len(intention) - 1:]:
            resultFile.write(f'"not {item}" and ')
        if len(intention)>0:
            resultFile.write(f'"not {intention[len(intention) - 1]}".\n')




print('results created successfully.')

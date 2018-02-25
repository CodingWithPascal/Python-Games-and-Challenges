def multiguy(n1, n2):
    return n1 * n2
def addguy(n1, n2):
    return n1 + n2
def subguy(n1, n2):
    return n1 - n2
def divideguy(n1, n2):
    return n1 / n2
answer = input('What do you want to do?: ')
n1 = float(input('Number 1: '))
n2 = float(input('Number 2: '))
if answer == 'multiply':
    print(multiguy(n1, n2))
if answer == 'add':
    print(addguy(n1, n2))
if answer == 'subtract':
    print(subguy(n1, n2))
if answer == 'divide':
    print(divideguy(n1, n2))
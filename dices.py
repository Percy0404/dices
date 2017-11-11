import random
red = [1, 4]

def printuseage():
    print('q = stop')
    print('s = shuffle')
    print('1 = remove big')
    print('2 = remove small')
    print('3 = remove red')
    print('4 = remove black')
    print('5 = remove odd')
    print('6 = remove even')












def shuffle(dices) :
    long = len(dices)
    dices = []
    for i in range(long):
        r = random.randint(1, 6)
        dices.append(r)
    print('Finish shuffle', dices)
    return dices


def removebig(dices):
    newlist = []
    for i in dices:
        if i <= 3:
            newlist.append(i)

    dices = newlist
    print('Now the dices are:', dices)
    return dices


def removesmall(dices):
    newlist = []
    for i in dices:
        if i >= 4:
            newlist.append(i)

    dices = newlist
    print('Now the dices are:', dices)
    return dices


def removered(dices):
    newlist = []
    for i in dices:
        if i not in red:
            newlist.append(i)

    dices = newlist
    print('Now the dices are:', dices)
    return dices


def removeblack(dices):
    newlist = []
    for i in dices:
        if i  in red:
            newlist.append(i)

    dices = newlist
    print('Now the dices are:', dices)
    return dices


def removeodd(dices):
    newlist = []
    for i in dices:
        if i % 2 == 0:
            newlist.append(i)

    dices = newlist
    print('Now the dices are:', dices)
    return dices


def removeeven(dices):
    newlist = []
    for i in dices:
        if i % 2 == 1:
            newlist.append(i)
    dices = newlist
    print('Now the dices are:', dices)
    return dices
def gendices():
      dices = []
      for i in range(6):
          r = random.randint(1, 6)
          dices.append(r)
      print('First dices is :', dices)
      return dices

printuseage()
dices = gendices()

while True:
    mode = input('What do you want to play?')
    if mode == 'q':
        break
    elif mode == 's':
        dices = shuffle(dices)
    elif mode == '1':
        dices = removebig(dices)
    elif mode == '2':
        dices = removesmall(dices)
    elif mode == '3':
        dices = removered(dices)
    elif mode == '4':
        dices = removeblack(dices)
    elif mode == '5':
        dices = removeodd(dices)
    elif mode == '6':
        dices = removeeven(dices)




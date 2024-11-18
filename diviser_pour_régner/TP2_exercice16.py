def piramy(x):
    print("piramy")
    for i in range(x):

        for k in range(i):
            print(end='*')

        print('\n')

def carre(x):
    print("square")
    for i in range(x):

        for k in range(x):
            print(end='*')

        print('\n')

def carre_vide(x):
    print("emty square")
    for i in range(x+1):

        if i == 0 or i == x:
            for k in range(x + 1):
                print(end='*')
        else:
            for k in range(x + 1):
                if k == 0 or k == x:
                    print(end='*')
                else:
                    print(end=' ')


        print('\n')

def piramy_vide(x):

    """ hello he is right """
    """ ok don't push it """

    print("empty piramy")
    for i in range(x):

        for k in range(i):
            if k == 0 or k == i-1:
                print(end='*')
            else:
                print(end=' ')

        print('\n')


piramy(5)
print("______________________________________________________________")
carre(5)
print("______________________________________________________________")
carre_vide(5)
print("______________________________________________________________")
piramy_vide(5)
print(piramy_vide.__doc__)
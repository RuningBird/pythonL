import random as rd
print("-------------------")
guess = 0
rdnum = rd.randint(1,10)
while guess != rdnum:
    temp = input("心中数字:")
    guess = int(temp)
    if guess == rdnum:
        print("right")
        guess = rdnum
    else:
        if guess > rdnum:
            print("big")
        else:
            print("little")

print('game over')

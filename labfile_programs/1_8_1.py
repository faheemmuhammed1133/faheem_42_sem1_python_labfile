#WAP to print half pyramid star pattern
'''
*
* *
* * *
* * * *
* * * * *
'''
for i in range(1,7): #ascending half pyramid
    for j in range(i):
        print(" * ",end='')
    print("\n")
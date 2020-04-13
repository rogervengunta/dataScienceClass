#print("test")
#a = 'john'
#b = 10.5
#print(a)
#print(b)

x=8; Today = 'thursday'
print('I just bought %s apples because it is %s'%(x,Today))
print('I just bought {x} apples because it is {Today}'.format(x=9, Today='Friday'))

#following will give "tuple index out of range" error
#print('I just bought {} apples because it is {}'.format(x=10, Today='Saturday'))

###F-strings
#h=8; s=9
print(f"there are {1} planets and {0} directions".format(8,9))

#h=7; s=5
#print("There are {s} planets and {h} directions in universe")

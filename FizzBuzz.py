# Let's play Fizz-Buzz

# Fizz buzz is an elementary school game where kids count,
# but they substitute "Fizz" for every multiple of 3
# and "buzz" for every multiple of 5.
# for example --- 1, 2, fizz, 4, buzz, fizz...
#
# Following this, any multiple of both gets "fizzbuzz"

#let's count to a random number

import random

g = random.randint(100, 999)
print(g)

i = 1
while i < g:
    if i%3 == 0 and i%5 == 0:     #test for both multiple of 5 and 3
        print("fizzbuzz")
    elif i%3 ==0:                  # test if only multiple of 3
        print ("fizz")
    elif i%5 == 0:                  # test if only multiple of 5
        print ("buzz")
    else:                           #for everything else, we print the number
        print (i)
    i +=1                           # and interate through

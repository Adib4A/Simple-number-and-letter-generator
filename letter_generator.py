import itertools
import sys
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [0,1,2,3,4,5,6,7,8,9]
four_letter = itertools.permutations(alphabet, 4)
four_num = itertools.permutations(numbers, 4)

four_num = list(four_num)
four_letter = list(four_letter)
with open("Passwords.json","w") as text_file:
    for i in four_letter:
        answer =''.join(i)
        for x in four_num:
            num = ''
            for z in x:
                num += str(z)
            print((answer + num).capitalize(), file=text_file)

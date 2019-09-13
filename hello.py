# list = ['a','b','c','d','e']
# list.reverse()
# display=""
# for result in list:
#     print(display.join(result))
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess= int(input('Guess: '))
    guess_count +=1
    if(guess == secret_number):
        print('You Win!')
        break
else:
    print('Sorry, You failed!')






#This program provides room for the user to guess the right number only on 5 trials !!


print ("Human please guess the right number from from (1 - 10)")
guessing_allowance = 0
while guessing_allowance < 5:
     guess = int(input('Guess:  '))
     guessing_allowance += 1
     if guess == 9 and guessing_allowance == 1:
         print('Thats CORRECT are you a Psychic ?')
         break
     elif guess == 9:
         print ('WINNER  you are human')
         break

     else:
         print('L O S E R !!!')

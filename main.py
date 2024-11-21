import random
playing = True
number=str(random.randint(20,30))
print("I WILL GENERATE A NUMBER FROM 20 30, AND YOU HAVE TO GUESS A NUMBER ONE DIGIT AT A TIME")
print("THE GAME ENDS, WHEN YOU GET 1 HERO")
while playing:
    guess=input("GIVE ME YOUR BEST GUESS! \n")
    if number == guess:
      print("YOU WIN THE GAME") 
      print("THE NUMBER WAS,number")
      break
    else:
       print("YOUR GUESS ISNT QITE RIGHT,TRY AGAIN.\n")
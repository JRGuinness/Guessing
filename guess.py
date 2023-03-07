from random import randint
import os
max_level=1

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   BLINK = '\033[5m'
   FGBLACK = '\033[30m'
   FGRED = '\033[31m'
   FGGREEN = '\033[32m'
   FGYELLOW = '\033[33m'
   FGBLUE = '\033[34m'
   FGMAGENTA = '\033[35m'
   FGCYAN = '\033[36m'
   FGWHITE = '\033[37m'
   BGBLACK = '\033[40m'
   BGRED = '\033[41m'
   BGGREEN = '\033[42m'
   BGYELLOW = '\033[43m'
   BGBLUE = '\033[44m'
   BGMAGENTA = '\033[45m'
   BGCYAN = '\033[46m'
   BGWHITE = '\033[47m'
   END = '\033[0m'

#os.system('clear')
playlevel=False
guesstype=False
while playlevel == False:
	os.system('clear')
	print(color.CYAN + color.UNDERLINE + color.BOLD + "Let's play a guessing game. What difficulty do you want to play?" + color.END)
	print(color.BOLD + "----------------------------------------------------------------" + color.END)
	print(color.GREEN + color.BOLD +  "1. Easy (a number between 1 and 15)" + color.END)
	print(color.YELLOW + color.BOLD + "2. Medium (a number between 1 and 50)" + color.END)
	print(color.RED + color.BOLD + "3. Hard (a number between 1 and 100)" + color.END)
	answer = input('Enter the number of the difficulty : ')
	try:
		int(answer)
	except ValueError:
		print(color.RED + "That's not even a number. Try Again!" + color.END)
		os.system('sleep 1')
		playlevel = False
	else:
		playlevel = True

#print answer
os.system('clear')
if int(answer) == 1:
	max_level = 15
	print(color.DARKCYAN + "Playing at the Easy level: (1-15)" + color.END)
elif int(answer) == 2:
	max_level = 50
	print(color.DARKCYAN + "Playing at the Medium level: (1-50)" + color.END)
elif int(answer) == 3:
	max_level = 100
	print(color.DARKCYAN + "Playing at the Hard level: (1-100)" + color.END)
else:
	print(color.RED + color.BOLD + "That's not a choice. You have to guess between 1 and 1,000!" + color.END)
	max_level = 1000

number = randint(1, max_level)
running = True
tries=0
print(color.YELLOW + "Try to guess the number that I'm thinking of between 1 and {}." .format(max_level) + color.END)

while running:
	while guesstype == False:
		guess = input('Enter an integer : ')
		try:
			int(guess)
		except ValueError:
			print("That's not even an integer. Try again. (We won't add this to your number of tries.)")
			guesstype = False
		else:
			guesstype = True
	
	if int(guess) > max_level:
		print(color.RED + color.BOLD + "That's not between 1 and {}, but I won't count that as a guess." .format(max_level) + color.END)
		guesstype = False
	else:
		if int(guess) == number:
			print(color.BLUE + 'Congratulations, you guessed it.' + color.END)
			tries += 1
			if tries > 1:
				print("You guessed the number in " + color.YELLOW + "{} " .format(tries) + color.END + "tries!")
			else:
				print("You guessed the number in " +color.YELLOW + "{} " .format(tries) + color.END + " try!")
			# this causes the while loop to stop
			guesstype = True
			running = False
		elif int(guess) < number:
			print('No, it is a little higher than that.')
			guesstype = False
			tries+=1
		else:
			print('No, it is a little lower than that.')
			guesstype = False
			tries+=1
else:
    print('Thanks for playing!')

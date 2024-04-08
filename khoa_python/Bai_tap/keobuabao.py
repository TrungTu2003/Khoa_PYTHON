from random import randint

print("Nhap Keo , Bua , Bao:")

you = input()
computer = randint(0,2)

if computer == 0:
	 computer = "Bua"
if computer == 1:
	 computer = "Keo"
if computer == 2:
	 computer = "Bao"

print("-----")
print("You:" + you)
print("Computer:" + computer)
print("-----")


if you == computer:
	print("Draw")
else:
		if you == "Keo":
			if computer == "Bao":
				print("Win")
			else:
				print("Lose")


		elif you == "Bua":
			if computer == "Bao":
				print("Lose")
			else:
				print("Win")


		elif you == "Bao":
			if computer == "Bua":
				print("Lose")
			else:
				print("Win")

		else:
			print("Nhap Sai!")
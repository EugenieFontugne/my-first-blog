volume = 18
if volume < 20:
	print("It's kinda quiet.")
elif 20 <= volume < 40:
	print("It's nice for background music")
elif 40 <= volume < 60:
	print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
	print("Nice for parties")
elif 80 <= volume < 100:
	print("A bit loud!")
else:
	print("My hears are hurting!")

# Change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
	volume = 50
	print("That's better!")

def hi():
	print("Hi there!")
	print("How are you?")
hi()

def hi(name):
	if name == "Ola":
		print("Hi Ola!")
	elif name == "Sonja":
		print("Hi Sonja")
	else:
		print("Hi anonymous")
hi("Ola")
hi("Eugenie")

def hi(name):
	print("Hi" + name + "!")
girls = ["Rachel", "Monica", "Phoebe", "Ola", "You"]
for name in girls: 
	hi(name)
	print("next girl")

for i in range(1, 6):
	print(i)


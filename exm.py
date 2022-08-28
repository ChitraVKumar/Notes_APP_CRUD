def shout(text):
	return text.upper()

print(shout('Hello'))

yell = shout
print(type(shout), type(yell))
print(yell('Hello'))
print("")
inp = input("Please enter a sequence of keystrokes: ")
alph = 0
for x in inp:
    if x.isalpha():
        alph = 1
print("")
if alph > 0:
    print("That would be likely entered as a string.")
if alph == 0:
    print("That would be likely entered not as a string.")
print("")

# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
word = input("Enter a word(or type'quit' to exit):")
if word.lower() == 'quit':
    print("Goodbye")
    exit()

howLong = len(word)
print("The word "+ word+ "is ", howLong, "characters long.")
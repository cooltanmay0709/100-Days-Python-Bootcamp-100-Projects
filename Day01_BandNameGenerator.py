#1 Create a greeting for your program.
#2 Ask the user for the city that they grew up in.
#3 Ask the user for the name of a pet.
#4 Combine the name of their city and pet and show them their band name.
#5 Make sure the input cursor shows on a new line, see the example at:
# Repl Link -
# Github Link -

print("Welcome To The Band Name Generator !!!")

cityName = input("What's name of the city you grew up in?\n")
petName = input("What's your pet's name?\n")

bandName = cityName + " " + petName;
print("Your band name could be : " + bandName);
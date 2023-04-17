# This will print the welcome message to the terminal
print("Welcome Adventurers, to the Guild Hall!  We will sort out your future shortly.")

# Ask the user for their name to begin the class sorting
name = input("What is your name, Adventurer?  Anonymity will not be accepted here. Enter your name here: ")

# Ask the user a series of questions in order to determine their profession.  You must answer with one of the answers in brackets.  For instance for (attack/hide) you could answer attack or hide
answer1 = input("You encounter a group of orcs resting by a fire on your travels, do your attack or hide? (attack/hide) ")
answer2 = input("While walking in a village you notice a noble drop something of value.  Do you return it, or pick it up when no one is looking? (notify/steal) ")
answer3 = input("Do you prefer bashing your enemies on the head, or sneaking up from behind? (bash/sneak) ")
answer4 = input("Do you set off on a quest with purpose, or prefer to lounge in the tavern listening to whispers? (quest/tavern) ")
answer5 = input("When you hear the cathedrals bell swing, are you overwhelmed with zealous fervor? (yes/no) ")

# Calculate the user's profession based on their answers.  Each answer will either give a +1 or 0 to the score
score = 0
if answer1 == "attack":
    score += 1
if answer2 == "notify":
    score += 1
if answer3 == "bash":
    score += 1
if answer4 == "quest":
    score += 1
if answer5 == "yes":
    score += 1

# Below are the three different profession types based on the score you have above
if score == 5:
    profession_type = "You are a holy warrior, a paladin who swears to uphold justice and righteousness, to stand with the good things of the world against the encroaching darkness, and to hunt the forces of evil wherever they lurk."
elif 1 <= score <= 4:
    profession_type = "You will be a valiant warrior, utilizing unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat."
else:
    profession_type = "You are a rogue, a scoundrel who makes their living off of the work of others.  You have no qualms with theft and would rather slice someones neck while they're sleeping than enter into an honest battle"

# Prints the user's profession in the terminal with their name and description
print(f"\n{name}, {profession_type}")
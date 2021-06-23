import random

print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\t|||  Welcome to Thesaurus App  |||")
print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

thesaurus = {"hot":["balmy", "summary", "tropical", "boiling", "scorching"],
            "cold":["chilly", "cool", "freezing", "frigid", "polar"],
            "happy":["content", "cherry", "merry", "jovial", "jocular"],
            "sad":["unhappy", "downcast", "miserable", "glum", "melancholy"]}

print("Choose a word from the thesaurus and I will give you a synonym.")
print("\nHere are the words in the thesaurus:")
for key in thesaurus:
    print("\t\t-" + str(key))
word = input("\nWhat word would you like a synonym for: ").lower()
synonym_id = random.randint(0, 4)
print("A synonym for {} is {}.".format(word, thesaurus[word][synonym_id]))
choice = input("\nWould you like to see the whole thesaurus (yes/no): ").lower()
if choice == "yes":
    for key, value in thesaurus.items():
        print("\n{} synonyms are:".format(key))
        for word in value:
            print("\t\t- " + word)

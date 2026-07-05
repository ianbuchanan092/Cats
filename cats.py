cats = ["Pumpkin", "Mittens", "Whiskers", "Shadow", "Luna", "Simba", "Oliver", "Chloe", "Bella", "Max"]

input_name = input("Enter a cat's name: ")
if input_name in cats:
    print(f"{input_name} is in the list of cats.")
else:
    print(f"{input_name} is not in the list of cats.")

#Now we're going to ask the user if they would like to add a new cat to the list.
#If they say yes, we'll prompt them for the new cat's name and add it to the list. 
#If they say no, we'll simply print the final list of cats.

add_cat = input("Would you like to add a new cat to the list? (yes/no): ")
if add_cat == "yes":
    new_cat = input("Enter the name of the new cat: ")
    cats.append(new_cat)
    print(f"{new_cat} has been added to the list of cats.")
print("Final list of cats:")
for cat in cats:
    print(cat)
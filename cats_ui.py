import tkinter as tk
from tkinter import simpledialog, messagebox
root = tk.Tk()
root.withdraw()  # Hide the main window

cat_file = open("cats.txt", "r")
cats = cat_file.readlines()
cat_file.close()
cats = [cat.strip() for cat in cats]  # Remove any leading/trailing whitespace

input_name = simpledialog.askstring("Cat Name", "Enter a cat's name:")
if input_name in cats:
    messagebox.showinfo("Cat Name", f"{input_name} is already in the list of cats.")
else:
    messagebox.showinfo("Cat Name", f"{input_name} is not in the list of cats.")

#Now we're going to ask the user if they would like to add a new cat to the list.
#If they say yes, we'll ask them for the new cat's name and add it to the list. 
#If they say no, we'll print the final list of cats.

add_cat = messagebox.askyesno("Add Cat", 
                              "Would you like to add a new cat to the list?")
if add_cat:
    new_cat = simpledialog.askstring("New Cat", "Enter the name of the new cat:")
    cats.append(new_cat)
cat_file = open("cats.txt", "w")
for cat in cats:
    cat_file.write(cat + "\n")
    
cat_file.close()
messagebox.showinfo("Cat Name", f"{new_cat} has been added to the list of cats.")
cat_list_text = "\n".join(cats)
messagebox.showinfo(
    "Final List of Cats",
    f"Final list of cats:\n{cat_list_text}"
)

root.destroy()

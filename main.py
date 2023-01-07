from tkinter import *

# WINDOW
# Create and configure window
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=400)

# LABEL
# Create a label
label = Label(text="I am a label", font=("Arial", 24, "bold"))
label.pack()  # The packer is what lays out the components

# Change the label text after instantiation using:
label["text"] = "New Text"
# or
label.config(text="New Text")


# BUTTON
# Create button action
def button_clicked():
    # Get text from entry field
    new_text = entry.get()
    # Change label text to input text
    label.config(text=new_text)


# Create button using button action
button = Button(text="Click Me!", command=button_clicked)
button.pack()

# ENTRY FIELD
# Create a data entry field
entry = Entry(width=30)
# Add text to populate field
entry.insert(END, string="Some text to begin with.")
entry.pack()

# TEXT BOX
# Creates a text box
text = Text(height=5, width=30)
# Puts cursor in textbox
text.focus()
# Adds some text to begin with
text.insert(END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# SPINBOX
def spinbox_used():
    # Gets the current value in spinbox
    print(spinbox.get())


# Create spinbox
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# SCALE
# Called with current scale value
def scale_used(value):
    print(value)


# Create scale
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# CHECKBOX BUTTON
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0
    print(checked_state.get())


# Variable to hold on to checked state, 0 is off, 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# RADIO BUTTON
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# LIST BOX
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Keep window open
window.mainloop()

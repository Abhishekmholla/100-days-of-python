programming_dict = {
    "Type1": "SyntaxErrors",
    "Type2": "IndentationError"
}

# Get the element from the dictonary
print(programming_dict["Type1"])

# Add a new items to dictionary
programming_dict["Type3"] = "KeyError"
print(programming_dict)

# Edit a item in a dictionary
programming_dict["Type1"] = "NameError"
print(programming_dict)

# Loop through a dictionary
for key,value in programming_dict.items():
    print(key)
    print(value)
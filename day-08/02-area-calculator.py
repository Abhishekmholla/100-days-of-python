from math import ceil


print("Welcome to paint area calculator")
def calculate_paint(height,width,cover):
    return ceil(( height * width ) / cover)
    
height = int(input("Height of the wall: "))
width = int(input("width of the wall: "))
coverage = 5

no_of_cans = calculate_paint(height,width,coverage)
print(f"Number of cans needed will be : {no_of_cans}")


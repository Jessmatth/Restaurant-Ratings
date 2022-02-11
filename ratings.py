"""Restaurant rating lister."""
# Your job is to write a program named ratings.py that:




file = open('scores.txt')
def file_to_dict(file):
    """make a dictionary from the .txt file"""
    ratings = {}
    for line in file:
        line = line.rstrip().split(":") # line is a list
    #ratings[line[0]] = line[1]
        ratings.update({line[0]: line[1]})

    return ratings

def choice_1_print_ratings():
    """sort restaurants and print dictionary"""
    ratings = file_to_dict(file)
    ratings = dict(sorted(ratings.items())) # approache 1

# output_ratings = dict(sorted(ratings.items()))
    for restaurant, rating in ratings.items():
        print(f"{restaurant} is rated at {rating}.")


def choice_2_add_restaurant_ratings(): 
    """Get user input and add restaurant ratings to the original ratings disctionary"""
    
    ratings = file_to_dict(file)
    restaurant = input("please input your restaurant name:")
    rating = int(input("please input your rating for the restarant (the rating must be an integer between 1 and 5 (inclusive)) ):"))

    while rating > 5 or rating < 1:
        rating = input("please input your rating for the restarant between 1-5:")
    ratings.update({restaurant: rating})

print("Welcome! What would you like to do?")
menu = int(input("""1. Print Restaurant Ratings
    2. Add Restaurant Rating
        3. Quit
        """))

# 02.10.22 the while loop has issues. Need updating
while menu != 3: 
    if menu == 1: 
        choice_1_print_ratings()
    elif menu == 2:
        choice_2_add_restaurant_ratings()
    elif menu == 3: 
        break
# The program should:

# Prompt the user for a restaurant name

# Prompt the user for a restaurant score

# Store the new restaurant/rating in the dictionary

# Print all of the ratings in alphabetical order (including the new one, of course)







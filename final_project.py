#For my Final project I have chosen to create an text interface that will help you decide what to eat for dinner
#define cuisine types and their dishes

cuisines = {
    "light": {
    "Mediterranean":["Greek Salad","Hummus and Pita","Dolma", "Falafel Wrap"],
    "Japanese":["Sushi Roll","Sashimi","Miso Soup","Bento Box"],
    "Thai":["Green Papaya Salad","Tom Yum Soup","Stir-Fried Vegetables","Spring Rolls"],
    "Korean":["Bibimbap","Doenjang Jjigae (Soybean Paste Stew)","Japchae (Stir-Fried Glass Noodles)","Gimbap"],
    "Vietnamese":["Pho","Banh Mi","Lotus Root Salad","Chao Ga (Porridge)"],
},
    "filling":{
    "American":["Burger","Pulled Pork Sandwich","Pizza"," Philly Cheesesteak"],
    "Mexican":["Tacos","Nachos","Quesadilla","Super Burrito"],
    "Indian":["Tandoori Chicken","Chicken Tikka Masala","Palak Paneer","Rogan Josh"],
    "Chinese":["Kung Pao Chicken","Fried Rice","Beef and Broccoli","Sweet and Sour Pork"],
    "Jamaican":["Jerk Chicken","Curried Goat","Braised Oxtail","Ital Stew"],
    }
}

#Gets the users cuisine type choice
def get_cuisine_type_choice():
    while True:
        choice = input("Would you like a 'light' or a 'filling' Meal? : ").strip().lower() 
        if choice in ["light","filling"]:
            return choice
        else:
            print("Invalid input. Please try again and type 'light' or 'filling'.\n ")

#Display users cuisine option and then get the users choice
def get_cuisine_choice(selected_cuisines):
    print("\nGreat! Here are some cuisines to choose from:\n ")
    index = 1
    for cuisine in selected_cuisines.keys():
        print(f"{index}. {cuisine}")
        index += 1
    while True:
        try:
            selected_index = int(input("\nEnter the number of the cuisine you want to choose: "))
            selected_cuisine = list(selected_cuisines.keys())[selected_index -1]
            return selected_cuisine
        except (ValueError, IndexError):
            print(f"Please enter a valid number between 1 and {len(selected_cuisines)}.") #will prompt if user inputs anything but an int

#Displays dishes from the selected cuisine and gets the users selection
def get_dishes_choice(dishes):
    print(f"\nHere are some popular dishes from your selected cuisine:\n ")
    index = 1
    for dish in dishes:
        print(f"{index}. {dish}")
        index += 1
    while True:
        try:
            dish_index = int(input("\nEnter the number of the dish you want to choose: "))
            selected_dish = dishes[dish_index - 1]
            return selected_dish
        except(ValueError, IndexError):
            print(f"Please enter a valid number betweeen 1 and {len(dishes)}.")

def main():
    #Introduction
    print("Welcome to the 'What's For Dinner?'questionnarie game! \n")
    choice = get_cuisine_type_choice() 
    selected_cuisine = get_cuisine_choice(cuisines[choice])
    selected_dish = get_dishes_choice(cuisines[choice][selected_cuisine])
    #Final prompt
    print(f"\nYou have chosen: {selected_dish}. Enjoy your meal!!")

#End
if __name__ == "__main__":
    main()
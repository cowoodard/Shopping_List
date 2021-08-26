from contents import pantry, recipes

display_dict = {}
for index, key in enumerate(recipes):
    #print(index, key)
    display_dict[str(index + 1)] = key

shopping_list = {}

while True:
    #Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print("{0} - {1}".format(key, value))

    choice = input(": ")

    if choice == '0':
        break
    elif choice in display_dict:
        selected_items = display_dict[choice]
        print("You have selected '{}'".format(selected_items))
        print("Checking ingredients...")
        ingredients = recipes[selected_items]
        print("You need the following ingredients:")
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry  = pantry.get(food_item, 0)

            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                if food_item in shopping_list:
                    shopping_list[food_item] += quantity_to_buy
                else:
                    shopping_list[food_item] = quantity_to_buy
                    #print(food_item, shopping_list[food_item])
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
print("Shopping List:")
for item in sorted(shopping_list):
    print("{0}: {1}".format(item, shopping_list[item]))

print("Thank you for choosing Phython Pizza Delivery")

size = input("What size of pizza do you want? S, M or L\n").upper()
add_pepperoni = input("Do you want pepperoni? Y or N\n").upper()
extra_chesse = input("Do you want extra cheese? Y or N\n").upper()

price = 0

if extra_chesse == "Y":
    price += 1

# Small Pizzas
if size == "S":
    price += 15

    if add_pepperoni == "Y":
        price += 2

# Medium Pizzas
elif size == "M":
    price += 20

    if add_pepperoni == "Y":
        price += 3

# Large Pizzas
elif size == "L":
    price += 25

    if add_pepperoni == "Y":
        price += 3

print(f"Thank you for choosing Python Pizza Delivery! Your final bill is ${price}.")
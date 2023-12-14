coke_price = 2.00
seven_up_price = 3.00
hundredplus_price = 4.00
pepsi_price = 8.00
vending_notes = (100,50, 20, 10, 1)

# User input for the selected drink
selected_drink = input("Press 1 for Coca-Cola (RM2), Press 2 for Seven Up(RM3), 3 for 100 Plus(RM4), 4 for Pepsi (RM8): ")

# Check for valid user drink selection input
while selected_drink not in ["1", "2", "3", "4"]:
    print("Invalid selection. Please choose a valid option.")
    selected_drink = input("Press 1 for Coca-Cola, Press 2 for Seven Up, 3 for 100 Plus, 4 for Pepsi: ")

# Initialize user_input
user_input = 0

# Check for valid user amount money input
while True:
    try:
        user_input = float(input("Enter the amount inserted: "))
        break  # Exit the loop if a valid input is provided
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Drink price
if selected_drink == "1":
    selected_price = coke_price
   
elif selected_drink == "2":
    selected_price = seven_up_price

elif selected_drink == "3":
    selected_price = hundredplus_price

elif selected_drink == "4":
    selected_price = pepsi_price
# Calculate balance
balance = user_input - selected_price


def calculate_change(user_input, selected_price, vending_notes):
    balance = user_input - selected_price

    if balance >= 0:
        print(f"Balance: {balance}")
        for note in vending_notes:
            num_notes = balance // note
            balance %= note
            if num_notes > 0:
                print(f"{int(num_notes)} notes of {note}")
    else:
        print("Not enough money for the selected drink.")


calculate_change(user_input, selected_price, vending_notes)
def totalcost(price, quantity, tax_rate):
    if price <0 or quantity <0 or tax_rate < 0:
        return "Invalid input: price, quantity, and tax rate must be a positive number."
    subtotal = price * quantity
    total_cost = subtotal * (1+tax_rate/100)
    return total_cost

def main():
    price = float(input("Enter the price per item: "))
    quantity = float(input("Enter the quantity: "))
    tax_rate = float(input("Enter the tax rate (in percentage but decimal form): "))
    total_cost = totalcost(price, quantity, tax_rate)

    if isinstance(total_cost, str):
        print(total_cost)
    else:
        print(f"The total cost incuding tax is: ${total_cost:.2f}")

main()


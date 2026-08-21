# Stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 200,
    "MSFT": 300
}

# Total investment
total = 0

# Start the loop
choice = "yes"

while choice == "yes":

    # Take stock name
    stock = input("Enter stock symbol: ").upper()

    # Check whether stock is available
    if stock in stocks:

        # Get stock price
        price = stocks[stock]

        # Take quantity
        quantity = int(input("Enter quantity: "))

        # Calculate investment
        investment = price * quantity

        # Add investment to total
        total = total + investment

        print("Investment:", investment)

        # Ask for another stock
        choice = input(
            "Do you want to add another stock? (yes/no): "
        ).lower()

    else:
        print("Stock not available. Please enter a valid stock.")

# Display final result
print("Total Investment:", total)
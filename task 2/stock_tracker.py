# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("\nAvailable stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Get the number of different stocks
try:
    num_stocks = int(input("\nHow many different stocks do you want to buy? "))

    if num_stocks <= 0:
        print("Please enter a number greater than zero.")
    else:
        for i in range(num_stocks):
            stock = input("\nEnter stock symbol: ").strip().upper()

            if stock not in stock_prices:
                print("Invalid stock symbol. Please try again.")
                continue

            try:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                investment = stock_prices[stock] * quantity
                portfolio[stock] = portfolio.get(stock, 0) + quantity
                total_investment += investment

                print(f"{stock} investment: ${investment:.2f}")

            except ValueError:
                print("Please enter a valid whole number.")

        print("\n===== Portfolio Summary =====")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            print(f"{stock}: {quantity} shares = ${value:.2f}")

        print(f"\nTotal Investment: ${total_investment:.2f}")

        # Save the result to a text file
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            for stock, quantity in portfolio.items():
                value = stock_prices[stock] * quantity
                file.write(
                    f"{stock}: {quantity} shares = ${value:.2f}\n"
                )
            file.write(
                f"\nTotal Investment: ${total_investment:.2f}\n"
            )

        print("Portfolio saved to portfolio.txt")

except ValueError:
    print("Please enter a valid whole number.")
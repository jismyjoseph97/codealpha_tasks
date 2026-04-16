# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 320
}

portfolio = {}

# Step 1: User input
n = int(input("How many stocks do you want to add? "))

for _ in range(n):
    stock = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if stock in stock_prices:
        portfolio[stock] = qty
    else:
        print("Stock not found in price list. Skipping...")

# Step 2: Calculate total investment
total = 0
print("\n Portfolio Summary:")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total += value
    print(f"{stock}: {qty} × {price} = {value}")

print(f"\n Total Investment Value: {total}")

# Step 3 (Optional): Save to file
save = input("\nDo you want to save to file? (y/n): ").lower()

if save == "y":
    with open("portfolio.txt", "w") as file:
        file.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock},{qty},{price},{value}\n")
        file.write(f"\nTotal Value: {total}")

    print("Portfolio saved to portfolio.txt")
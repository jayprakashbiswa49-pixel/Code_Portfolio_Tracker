"""
Stock Portfolio Tracker
Developed for CodeAlpha Python Development Internship (Task 2)
"""

import csv

# Hardcoded stock price dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190,
    "NVDA": 135,
    "META": 500,
    "NFLX": 650
}

# In-memory user portfolio {stock_symbol: quantity}
portfolio = {}


def display_available_stocks():
    """Display all available stock symbols and their fixed prices."""
    print("\nAvailable Stocks:")
    for symbol, price in stock_prices.items():
        print(f"{symbol:<6} - ${price}")


def add_stock():
    """Prompt user for stock symbol and quantity, then add/update portfolio."""
    symbol = input("\nEnter stock symbol: ").strip().upper()

    if not symbol:
        print("Error: Stock symbol cannot be empty.")
        return

    if symbol not in stock_prices:
        print(f"Error: '{symbol}' is not available. Please choose from: {', '.join(stock_prices.keys())}")
        return

    qty_input = input("Enter quantity: ").strip()

    if not qty_input:
        print("Error: Quantity cannot be empty.")
        return

    try:
        qty = int(qty_input)
    except ValueError:
        print("Error: Quantity must be a valid number.")
        return

    if qty <= 0:
        print("Error: Quantity must be greater than zero.")
        return

    # Update existing stock or add new entry
    if symbol in portfolio:
        portfolio[symbol] += qty
        print(f"Updated {symbol} quantity to {portfolio[symbol]} shares.")
    else:
        portfolio[symbol] = qty
        investment = stock_prices[symbol] * qty
        print(f"Added {qty} share(s) of {symbol} (${investment:,}) to portfolio.")


def view_portfolio():
    """Display a formatted summary table of the user's stock portfolio."""
    if not portfolio:
        print("\nYour portfolio is currently empty. Please add stocks first.")
        return

    print("\n========================================")
    print("          MY STOCK PORTFOLIO")
    print("========================================")
    print(f"\n{'Stock':<8} {'Price':<8} {'Quantity':<11} {'Total':<10}")

    total_shares = 0
    total_investment = 0

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        total = price * qty
        total_shares += qty
        total_investment += total
        print(f"{stock:<8} ${price:<7} {qty:<11} ${total:,}")

    print("\n" + "-" * 40)
    print(f"Total Stocks: {len(portfolio)} | Total Shares: {total_shares}")
    print(f"TOTAL INVESTMENT: ${total_investment:,}")
    print("-" * 40)


def calculate_total_investment():
    """Calculate and display total investment value."""
    if not portfolio:
        print("\nYour portfolio is currently empty. Total investment: $0")
        return 0

    total_shares = 0
    total_investment = 0

    for stock, qty in portfolio.items():
        total_shares += qty
        total_investment += stock_prices[stock] * qty

    print("\n----------------------------------------")
    print(f"Total Stocks Tracked: {len(portfolio)}")
    print(f"Total Shares Owned  : {total_shares}")
    print(f"TOTAL INVESTMENT    : ${total_investment:,}")
    print("----------------------------------------")
    return total_investment


def save_portfolio_txt(filename="portfolio.txt"):
    """Save portfolio summary to a formatted text file."""
    if not portfolio:
        print("Portfolio is empty. Nothing to save.")
        return

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("========================================\n")
            f.write("          MY STOCK PORTFOLIO\n")
            f.write("========================================\n\n")
            f.write(f"{'Stock':<8} {'Price':<8} {'Quantity':<11} {'Total':<10}\n")

            total_shares = 0
            total_investment = 0

            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                total = price * qty
                total_shares += qty
                total_investment += total
                f.write(f"{stock:<8} ${price:<7} {qty:<11} ${total:,}\n")

            f.write("\n" + "-" * 40 + "\n")
            f.write(f"Total Stocks: {len(portfolio)} | Total Shares: {total_shares}\n")
            f.write(f"TOTAL INVESTMENT: ${total_investment:,}\n")
            f.write("-" * 40 + "\n")
    except (IOError, OSError) as e:
        print(f"Error saving to {filename}: {e}")


def save_portfolio_csv(filename="portfolio.csv"):
    """Save portfolio details to a CSV file."""
    if not portfolio:
        print("Portfolio is empty. Nothing to save.")
        return

    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Price", "Quantity", "Total Value"])
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                total = price * qty
                writer.writerow([stock, price, qty, total])
    except (IOError, OSError) as e:
        print(f"Error saving to {filename}: {e}")


def main():
    """Main function to run the interactive stock tracker."""
    print("========================================")
    print("       STOCK PORTFOLIO TRACKER")
    print("========================================")
    print("\nWelcome to Stock Portfolio Tracker!")
    display_available_stocks()

    while True:
        print("\n----------------------------------------")
        print("1. View Available Stocks")
        print("2. Add Stock")
        print("3. View Portfolio")
        print("4. Calculate Total Investment")
        print("5. Save Portfolio")
        print("6. Exit")
        print("----------------------------------------")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            display_available_stocks()

        elif choice == "2":
            add_stock()

        elif choice == "3":
            view_portfolio()

        elif choice == "4":
            calculate_total_investment()

        elif choice == "5":
            if not portfolio:
                print("\nYour portfolio is currently empty. Please add stocks before saving.")
            else:
                save_portfolio_txt()
                save_portfolio_csv()
                print("\nPortfolio saved successfully!")

        elif choice == "6":
            print("\nThank you for using Stock Portfolio Tracker. Goodbye!\n")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

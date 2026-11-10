"""
=============================================================================
Project Name   : Stock Portfolio Tracker
Author         : CodeAlpha Python Development Intern
Description    : A beginner-friendly, interactive console application to track
                 stock investments, calculate portfolio values, and export
                 reports to TXT and CSV formats using predefined stock prices.
Technology     : Python 3 (Dictionaries, Loops, Functions, File Handling)
=============================================================================
"""

import csv
import os
from datetime import datetime

# =============================================================================
# 1. HARDCODED STOCK PRICE DICTIONARY
# Predefined sample prices for educational purposes (as specified by CodeAlpha)
# =============================================================================
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


def display_welcome_banner():
    """
    Displays the initial welcome banner and introduction when the app launches.
    """
    print("\n" + "=" * 50)
    print("           STOCK PORTFOLIO TRACKER")
    print("   CodeAlpha Python Development Internship Task")
    print("=" * 50)
    print("Welcome to Stock Portfolio Tracker!")
    print("Easily manage your stock investments and track your total value.\n")


def display_available_stocks(prices=stock_prices):
    """
    Displays all available stock symbols and their fixed market prices.
    """
    print("\n" + "-" * 40)
    print("          AVAILABLE STOCKS & PRICES")
    print("-" * 40)
    print(f"{'Stock Symbol':<16} {'Price per Share':>16}")
    print("-" * 40)
    for symbol, price in prices.items():
        print(f"{symbol:<16} {'$' + f'{price:,}':>16}")
    print("-" * 40)


def add_stock(portfolio, prices=stock_prices):
    """
    Prompts user for a stock symbol and quantity, validates inputs,
    and adds or updates the stock in the portfolio dictionary.

    Formula:
        Investment Value = Stock Price * Quantity
    """
    print("\n" + "-" * 40)
    print("         ADD STOCK TO PORTFOLIO")
    print("-" * 40)

    # 1. Input and validation for Stock Symbol
    symbol_input = input("Enter stock symbol (e.g., AAPL, TSLA): ").strip().upper()

    if not symbol_input:
        print("\n[Error] Stock symbol cannot be empty.")
        return

    if symbol_input not in prices:
        print(f"\n[Error] '{symbol_input}' is not in the available stocks list.")
        print(f"Available stocks: {', '.join(prices.keys())}")
        return

    # 2. Input and validation for Quantity
    quantity_input = input(f"Enter quantity of shares for {symbol_input}: ").strip()

    if not quantity_input:
        print("\n[Error] Quantity cannot be empty.")
        return

    try:
        quantity = int(quantity_input)
    except ValueError:
        print("\n[Error] Invalid quantity. Please enter a valid whole number (e.g., 5).")
        return

    if quantity <= 0:
        print("\n[Error] Quantity must be a positive number greater than zero.")
        return

    # 3. Add or update stock in the portfolio
    price = prices[symbol_input]
    added_investment = price * quantity

    if symbol_input in portfolio:
        old_quantity = portfolio[symbol_input]
        portfolio[symbol_input] += quantity
        total_quantity = portfolio[symbol_input]
        print(f"\n[Success] Updated {symbol_input} in portfolio!")
        print(f"  - Previous Quantity : {old_quantity}")
        print(f"  - Added Shares      : {quantity} (+${added_investment:,})")
        print(f"  - New Total Quantity: {total_quantity} (${price * total_quantity:,})")
    else:
        portfolio[symbol_input] = quantity
        print(f"\n[Success] Added {symbol_input} to portfolio!")
        print(f"  - Stock Symbol     : {symbol_input}")
        print(f"  - Price per Share  : ${price:,}")
        print(f"  - Quantity Added   : {quantity}")
        print(f"  - Investment Value : ${added_investment:,}")


def view_portfolio(portfolio, prices=stock_prices):
    """
    Displays a formatted portfolio summary table showing:
      - Stock Symbol
      - Price per Share
      - Quantity Owned
      - Total Investment Value per Stock
      - Total Stocks Tracked
      - Total Shares Owned
      - Total Investment Value
    """
    if not portfolio:
        print("\n[Notice] Your portfolio is currently empty.")
        print("Please add stocks using Option 2 from the main menu.")
        return

    print("\n" + "=" * 52)
    print("                 MY STOCK PORTFOLIO")
    print("=" * 52)
    print(f"{'Stock':<10} {'Price':>10} {'Quantity':>12} {'Total Value':>16}")
    print("-" * 52)

    total_shares = 0
    total_investment = 0

    for symbol, quantity in portfolio.items():
        price = prices.get(symbol, 0)
        stock_total = price * quantity
        total_shares += quantity
        total_investment += stock_total

        price_str = f"${price:,}"
        total_str = f"${stock_total:,}"
        print(f"{symbol:<10} {price_str:>10} {quantity:>12} {total_str:>16}")

    print("-" * 52)
    print(f"Total Stocks Tracked : {len(portfolio)}")
    print(f"Total Shares Owned   : {total_shares:,}")
    print("-" * 52)
    print(f"TOTAL INVESTMENT     : ${total_investment:,}")
    print("=" * 52)


def calculate_total_investment(portfolio, prices=stock_prices):
    """
    Calculates and displays the overall total investment value of the portfolio.

    Returns:
        int/float: Total value of the portfolio.
    """
    if not portfolio:
        print("\n[Notice] Your portfolio is currently empty.")
        print("Total Investment Value: $0")
        return 0

    total_shares = 0
    total_value = 0

    for symbol, quantity in portfolio.items():
        price = prices.get(symbol, 0)
        total_shares += quantity
        total_value += price * quantity

    print("\n" + "=" * 44)
    print("         TOTAL INVESTMENT SUMMARY")
    print("=" * 44)
    print(f"  Distinct Stocks Held : {len(portfolio)}")
    print(f"  Total Shares Owned   : {total_shares:,}")
    print(f"  TOTAL PORTFOLIO VALUE: ${total_value:,}")
    print("=" * 44)

    return total_value


def save_portfolio_txt(portfolio, prices=stock_prices, filename="portfolio.txt"):
    """
    Saves portfolio details and overall summary to a formatted text file.

    Parameters:
        portfolio (dict): Dictionary mapping stock symbols to quantities.
        prices (dict): Dictionary mapping stock symbols to unit prices.
        filename (str): Name of the text file.

    Returns:
        bool: True if saving succeeded, False otherwise.
    """
    if not portfolio:
        print(f"\n[Warning] Portfolio is empty. '{filename}' was not created.")
        return False

    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=" * 52 + "\n")
            f.write("           STOCK PORTFOLIO SUMMARY REPORT\n")
            f.write(f"           Generated: {timestamp}\n")
            f.write("=" * 52 + "\n\n")
            f.write(f"{'Stock':<10} {'Price':>10} {'Quantity':>12} {'Total Value':>16}\n")
            f.write("-" * 52 + "\n")

            total_shares = 0
            total_investment = 0

            for symbol, quantity in portfolio.items():
                price = prices.get(symbol, 0)
                stock_total = price * quantity
                total_shares += quantity
                total_investment += stock_total

                price_str = f"${price:,}"
                total_str = f"${stock_total:,}"
                f.write(f"{symbol:<10} {price_str:>10} {quantity:>12} {total_str:>16}\n")

            f.write("-" * 52 + "\n")
            f.write(f"Total Stocks Tracked : {len(portfolio)}\n")
            f.write(f"Total Shares Owned   : {total_shares:,}\n")
            f.write("-" * 52 + "\n")
            f.write(f"TOTAL INVESTMENT     : ${total_investment:,}\n")
            f.write("=" * 52 + "\n")

        print(f"[Success] Portfolio saved to text file: '{filename}'")
        return True

    except (IOError, OSError) as e:
        print(f"[Error] Failed to write text file '{filename}': {e}")
        return False


def save_portfolio_csv(portfolio, prices=stock_prices, filename="portfolio.csv"):
    """
    Saves portfolio details into a structured CSV file.

    Parameters:
        portfolio (dict): Dictionary mapping stock symbols to quantities.
        prices (dict): Dictionary mapping stock symbols to unit prices.
        filename (str): Name of the CSV file.

    Returns:
        bool: True if saving succeeded, False otherwise.
    """
    if not portfolio:
        print(f"\n[Warning] Portfolio is empty. '{filename}' was not created.")
        return False

    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Write Header
            writer.writerow(["Stock", "Price", "Quantity", "Total Value"])

            for symbol, quantity in portfolio.items():
                price = prices.get(symbol, 0)
                stock_total = price * quantity
                writer.writerow([symbol, price, quantity, stock_total])

        print(f"[Success] Portfolio saved to CSV file: '{filename}'")
        return True

    except (IOError, OSError) as e:
        print(f"[Error] Failed to write CSV file '{filename}': {e}")
        return False


def main():
    """
    Main controller function that initializes the portfolio and
    runs the interactive command-line menu loop.
    """
    # In-memory portfolio tracking: { "AAPL": 5, "TSLA": 2, ... }
    portfolio = {}

    # Initial Welcome Screen & Available Stocks
    display_welcome_banner()
    display_available_stocks(stock_prices)

    # Main Application Loop
    while True:
        print("\n" + "-" * 40)
        print("              MAIN MENU")
        print("-" * 40)
        print("1. View Available Stocks")
        print("2. Add Stock to Portfolio")
        print("3. View My Portfolio")
        print("4. Calculate Total Investment")
        print("5. Save Portfolio to File")
        print("6. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            display_available_stocks(stock_prices)

        elif choice == "2":
            add_stock(portfolio, stock_prices)

        elif choice == "3":
            view_portfolio(portfolio, stock_prices)

        elif choice == "4":
            calculate_total_investment(portfolio, stock_prices)

        elif choice == "5":
            if not portfolio:
                print("\n[Warning] Your portfolio is empty! Add stocks before saving.")
            else:
                print("\nSaving portfolio...")
                saved_txt = save_portfolio_txt(portfolio, stock_prices, "portfolio.txt")
                saved_csv = save_portfolio_csv(portfolio, stock_prices, "portfolio.csv")
                if saved_txt and saved_csv:
                    print("\nPortfolio saved successfully!")

        elif choice == "6":
            print("\n" + "=" * 45)
            print("  Thank you for using Stock Portfolio Tracker!")
            print("          Have a productive day ahead!")
            print("=" * 45 + "\n")
            break

        else:
            print("\n[Error] Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()


# 📈 Stock Portfolio Tracker

A beginner-friendly, clean, and interactive command-line **Stock Portfolio Tracker** written in Python. This project allows users to view stock prices, enter stock symbols and quantities, track total portfolio investments, update stock quantities dynamically, and save reports to both TXT and CSV files.

Developed as part of the **CodeAlpha Python Development Internship (Task 2)**.

---

## 📌 Project Objective

The primary objective of this project is to build a simple and efficient stock portfolio tracker demonstrating essential Python programming fundamentals:
- **Python Dictionaries**: Storing hardcoded stock prices and dynamic user portfolio holdings.
- **Functions**: Organizing the program into modular, single-responsibility functions.
- **Loops & Conditionals**: Driving an interactive terminal menu with input validation.
- **Arithmetic Operations**: Calculating investment values (`Price × Quantity`) and portfolio totals.
- **File Handling**: Writing portfolio summaries to `portfolio.txt` and `portfolio.csv`.

---

## 🚀 Features

- **Welcome Screen**: Displays the tracker banner, greeting, and available stocks with prices.
- **Add Stock**: Allows users to enter a stock symbol and quantity, updating existing stocks if already present.
- **Input Validation**: Gracefully handles unknown stock symbols, empty inputs, non-numeric values, and non-positive numbers.
- **View Portfolio**: Displays an organized table with individual values, total stocks, total shares, and total investment.
- **Calculate Total Investment**: Dedicated function to calculate and display overall investment value.
- **Save Portfolio**: Saves portfolio records to both `portfolio.txt` and `portfolio.csv`.
- **Clean Menu Loop**: Interactive menu running until the user chooses to exit.

---

## 🛠️ Technologies Used

- **Language**: Python 3
- **Libraries**: `csv` (Python Standard Library)
- **External Dependencies**: None (No APIs, databases, or third-party packages required)

---

## 📊 Stock Prices (Sample Data)

```python
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
```

---

## 📁 Project Folder Structure

```text
Stock-Portfolio-Tracker/
│
├── main.py          # Main application code
├── portfolio.txt    # Text export file
├── portfolio.csv    # CSV export file
└── README.md        # Project documentation
```

---

## 💻 How to Run the Project

1. Ensure you have Python 3 installed:
   ```bash
   python --version
   ```

2. Run the application:
   ```bash
   python main.py
   ```

---

## 🖥️ User Interface & Example Output

### Main Menu
```text
========================================
       STOCK PORTFOLIO TRACKER
========================================

Welcome to Stock Portfolio Tracker!

Available Stocks:
AAPL   - $180
TSLA   - $250
GOOGL  - $140
MSFT   - $420
AMZN   - $190
NVDA   - $135
META   - $500
NFLX   - $650

----------------------------------------
1. View Available Stocks
2. Add Stock
3. View Portfolio
4. Calculate Total Investment
5. Save Portfolio
6. Exit
----------------------------------------

Enter your choice: 
```

### Portfolio Summary
When adding `AAPL` (5 shares), `TSLA` (2 shares), and `GOOGL` (3 shares):

```text
========================================
          MY STOCK PORTFOLIO
========================================

Stock    Price    Quantity    Total
AAPL     $180     5           $900
TSLA     $250     2           $500
GOOGL    $140     3           $420

----------------------------------------
Total Stocks: 3 | Total Shares: 10
TOTAL INVESTMENT: $1,820
----------------------------------------

Portfolio saved successfully!
```

### Exported Files

#### `portfolio.txt`
```text
========================================
          MY STOCK PORTFOLIO
========================================

Stock    Price    Quantity    Total
AAPL     $180     5           $900
TSLA     $250     2           $500
GOOGL    $140     3           $420

----------------------------------------
Total Stocks: 3 | Total Shares: 10
TOTAL INVESTMENT: $1,820
----------------------------------------
```

#### `portfolio.csv`
```csv
Stock,Price,Quantity,Total Value
AAPL,180,5,900
TSLA,250,2,500
GOOGL,140,3,420
```

---

## 🎓 Internship Information

- **Organization**: CodeAlpha
- **Domain**: Python Development Internship
- **Task**: Task 2 — Stock Portfolio Tracker

# 📈 Stock Portfolio Tracker

A beginner-friendly yet professional command-line **Stock Portfolio Tracker** built with Python. This project allows users to manage stock holdings, calculate real-time portfolio values using fixed market prices, update stock quantities dynamically, and export structured reports to both TXT and CSV formats.

Developed as part of the **CodeAlpha Python Development Internship**.

---

## 📌 Project Objective

The primary objective of this project is to build an interactive, console-based stock portfolio manager demonstrating fundamental Python programming concepts, including:
- Utilizing **Python Dictionaries** for key-value mappings (stock prices & portfolio holdings).
- Implementing **Modular Functions** for separation of concerns and maintainability.
- Applying **Loops and Conditional Statements** to create an interactive menu-driven interface.
- Ensuring robust **User Input Validation** and graceful error handling.
- Performing **Basic Arithmetic Operations** for financial calculations.
- Handling persistent storage via **File I/O** (TXT and CSV export).

---

## 🚀 Features

- **Welcome & Pricing Screen**: Displays the tracker title, welcome greeting, and supported stocks with current prices.
- **Stock Lookup & Validation**: Checks user inputs against predefined stock symbols (case-insensitive) and validates quantities.
- **Dynamic Quantity Updating**: Adding an existing stock increments its quantity rather than creating duplicate entries.
- **Detailed Portfolio Table**: Displays a clean, aligned summary table showing stock symbol, unit price, quantity owned, and individual investment value.
- **Portfolio Metrics**: Automatically calculates distinct stocks held, total shares owned, and cumulative investment value.
- **Total Investment Calculator**: Standalone menu option to quickly check overall investment totals.
- **Dual File Export**: Exports portfolio data to formatted plain text (`portfolio.txt`) and tabular CSV (`portfolio.csv`) files.
- **Robust Input Validation**: Handles non-numeric quantities, negative numbers, zeroes, empty inputs, unknown symbols, and file errors.
- **Persistent Interactive Loop**: Seamless navigation through an easy-to-use numbered menu until the user chooses to exit.

---

## 🛠️ Technologies Used

| Component | Description |
|---|---|
| **Language** | Python 3 |
| **Data Structures** | Python Dictionaries (`dict`), Lists, Tuples |
| **Modules Used** | `csv` (Standard Library for CSV export), `datetime` (Standard Library for report timestamps) |
| **External Dependencies** | None (Zero external dependencies or APIs required) |

---

## 📊 Predefined Stock Prices

The application uses sample educational market data stored in a Python dictionary:

| Symbol | Company | Sample Price |
|:---:|:---|:---:|
| `AAPL` | Apple Inc. | $180 |
| `TSLA` | Tesla Inc. | $250 |
| `GOOGL` | Alphabet Inc. (Google) | $140 |
| `MSFT` | Microsoft Corp. | $420 |
| `AMZN` | Amazon.com Inc. | $190 |
| `NVDA` | NVIDIA Corp. | $135 |
| `META` | Meta Platforms Inc. | $500 |
| `NFLX` | Netflix Inc. | $650 |

---

## 📁 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── main.py            # Main application source code with menu and logic
├── portfolio.txt      # Formatted text report generated on export
├── portfolio.csv      # CSV export suitable for spreadsheet tools (Excel/Sheets)
└── README.md          # Comprehensive project documentation
```

---

## ⚙️ Installation & Prerequisites

1. **Python 3.x**: Ensure Python 3.6 or higher is installed on your system.
   Verify by running:
   ```bash
   python --version
   ```
2. **Clone / Download**: Download or clone the project repository:
   ```bash
   git clone https://github.com/your-username/Stock-Portfolio-Tracker.git
   cd Stock-Portfolio-Tracker
   ```

---

## 💻 How to Run the Project

Run the application directly via your terminal or command prompt:

```bash
python main.py
```

---

## 🖥️ User Interface & Menu Options

Upon launching, the interactive menu presents 6 options:

```text
----------------------------------------
              MAIN MENU
----------------------------------------
1. View Available Stocks
2. Add Stock to Portfolio
3. View My Portfolio
4. Calculate Total Investment
5. Save Portfolio to File
6. Exit
----------------------------------------
Enter your choice (1-6):
```

### Menu Actions:
1. **View Available Stocks**: Prints all supported symbols and unit prices.
2. **Add Stock to Portfolio**: Prompts for symbol and number of shares. If the stock is already in your portfolio, it updates the quantity.
3. **View My Portfolio**: Displays the full breakdown table and grand totals.
4. **Calculate Total Investment**: Shows a quick summary card of total shares and aggregate portfolio value.
5. **Save Portfolio to File**: Exports the active portfolio to both `portfolio.txt` and `portfolio.csv`.
6. **Exit**: Gracefully exits the program with a parting greeting.

---

## 📋 Example Walkthrough & Output

### 1. Adding Stocks:
- Added **5 shares of AAPL** ($180/share = $900)
- Added **2 shares of TSLA** ($250/share = $500)
- Added **3 shares of GOOGL** ($140/share = $420)

### 2. Portfolio Summary Table:

```text
====================================================
                 MY STOCK PORTFOLIO
====================================================
Stock           Price     Quantity      Total Value
----------------------------------------------------
AAPL             $180            5             $900
TSLA             $250            2             $500
GOOGL            $140            3             $420
----------------------------------------------------
Total Stocks Tracked : 3
Total Shares Owned   : 10
----------------------------------------------------
TOTAL INVESTMENT     : $1,820
====================================================
```

### 3. Generated Files:

#### `portfolio.txt`:
```text
====================================================
           STOCK PORTFOLIO SUMMARY REPORT
====================================================

Stock           Price     Quantity      Total Value
----------------------------------------------------
AAPL             $180            5             $900
TSLA             $250            2             $500
GOOGL            $140            3             $420
----------------------------------------------------
Total Stocks Tracked : 3
Total Shares Owned   : 10
----------------------------------------------------
TOTAL INVESTMENT     : $1,820
====================================================
```

#### `portfolio.csv`:
```csv
Stock,Price,Quantity,Total Value
AAPL,180,5,900
TSLA,250,2,500
GOOGL,140,3,420
```

---

## 🛡️ Input Validation & Error Handling

The application protects against user input errors:
- **Unknown Symbols**: Prompts the user that the symbol is unsupported and lists available symbols.
- **Empty Inputs**: Detects blank strings and prompts the user to provide valid input.
- **Negative & Zero Quantities**: Rejects non-positive numbers with an informative prompt.
- **Non-Numeric Inputs**: Catches `ValueError` when non-integer strings (e.g., `"five"`, `"abc"`, `"3.14"`) are entered.
- **Empty Portfolio Protection**: Prevents viewing or saving empty portfolios and guides users to add stocks first.
- **File I/O Safety**: Protects file writes with `try...except (IOError, OSError)` blocks.

---

## 🎓 Internship Information

- **Organization**: CodeAlpha
- **Domain**: Python Development Internship
- **Task**: Task 2 — Stock Portfolio Tracker
- **Author**: Jay Prakash

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).


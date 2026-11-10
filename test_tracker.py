"""
Automated test suite to verify Stock Portfolio Tracker functionality.
"""
import subprocess
import os

def run_tracker_with_inputs(inputs):
    input_str = "\n".join(inputs) + "\n"
    process = subprocess.Popen(
        ["python", "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=input_str)
    return stdout, stderr, process.returncode

def test_full_workflow():
    inputs = [
        "1",              # 1. View available stocks
        "3",              # 2. View empty portfolio
        "4",              # 3. Calculate total for empty portfolio
        "5",              # 4. Save empty portfolio
        "2", "INVALID",   # 5. Invalid stock symbol
        "2", "",          # 6. Empty stock symbol
        "2", "aapl", "abc", # 7. Invalid quantity string
        "2", "aapl", "-5",  # 8. Negative quantity
        "2", "aapl", "0",   # 9. Zero quantity
        "2", "aapl", "5",   # 10. Valid add AAPL 5
        "2", "TSLA", "2",   # 11. Valid add TSLA 2
        "2", "GOOGL", "3",  # 12. Valid add GOOGL 3
        "2", "AAPL", "3",   # 13. Update AAPL with 3 more (total 8)
        "3",              # 14. View updated portfolio
        "4",              # 15. Calculate total investment
        "5",              # 16. Save portfolio
        "99",             # 17. Invalid menu option
        "6"               # 18. Exit
    ]

    stdout, stderr, code = run_tracker_with_inputs(inputs)
    print("Return code:", code)
    if stderr:
        print("STDERR:\n", stderr)
    print("STDOUT SUMMARY:\n", stdout[:500], "...\n", stdout[-600:])

    assert code == 0, f"Expected return code 0, got {code}"
    assert "STOCK PORTFOLIO TRACKER" in stdout
    assert "AVAILABLE STOCKS" in stdout
    assert "Your portfolio is currently empty" in stdout
    assert "Total Investment Value: $0" in stdout
    assert "not in the available stocks list" in stdout
    assert "Quantity must be a positive number greater than zero" in stdout
    assert "Updated AAPL in portfolio" in stdout
    assert "MY STOCK PORTFOLIO" in stdout
    assert "TOTAL INVESTMENT" in stdout
    assert "Portfolio saved successfully!" in stdout
    assert "Thank you for using Stock Portfolio Tracker!" in stdout

    # Verify portfolio.txt exists and content
    assert os.path.exists("portfolio.txt"), "portfolio.txt missing"
    with open("portfolio.txt", "r", encoding="utf-8") as f:
        txt_content = f.read()
        print("\n--- portfolio.txt content ---\n", txt_content)
        assert "STOCK PORTFOLIO SUMMARY REPORT" in txt_content
        assert "AAPL" in txt_content
        assert "TSLA" in txt_content
        assert "GOOGL" in txt_content
        assert "TOTAL INVESTMENT" in txt_content

    # Verify portfolio.csv exists and content
    assert os.path.exists("portfolio.csv"), "portfolio.csv missing"
    with open("portfolio.csv", "r", encoding="utf-8") as f:
        csv_content = f.read()
        print("\n--- portfolio.csv content ---\n", csv_content)
        assert "Stock,Price,Quantity,Total Value" in csv_content
        assert "AAPL,180,8,1440" in csv_content
        assert "TSLA,250,2,500" in csv_content
        assert "GOOGL,140,3,420" in csv_content

    print("\nALL AUTOMATED TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_full_workflow()


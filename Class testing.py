#!/usr/bin/env python3

from portfolio import Portfolio
from datetime import datetime

# Example Usage
portfolio = Portfolio()
portfolio.add_cash(50000)
portfolio.add_trade("2024-09-03", "buy", "AAPL", 100, 150)
portfolio.update_market_data("AAPL", 155)
portfolio.set_portfolio_value(120000)
portfolio.add_trade("2024-09-05", "sell", "AAPL", 50, 160)
portfolio.add_note("2024-09-03", "Consider increasing exposure to AAPL due to strong performance.")
print(portfolio)

# Save to a JSON file
portfolio.save('portfolio.json')

# Load from a JSON file
loaded_portfolio = Portfolio('portfolio.json')
print(loaded_portfolio)

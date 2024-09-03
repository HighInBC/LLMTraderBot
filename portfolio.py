import json
from datetime import datetime
from position import Position

class Portfolio:
    def __init__(self, filename=None):
        if filename:
            self.load(filename)
        else:
            self.date = datetime.now().strftime("%Y-%m-%d")
            self.cash_available = 0.0
            self.portfolio_value = 0.0
            self.positions = {}
            self.market_data = {}
            self.trade_history = []
            self.notes = []

    def load(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.date = data.get("date", datetime.now().strftime("%Y-%m-%d"))
            self.cash_available = data.get("cash_available", 0.0)
            self.portfolio_value = data.get("portfolio_value", 0.0)
            self.positions = {symbol: Position.from_dict(pos_data) for symbol, pos_data in data.get("positions", {}).items()}
            self.market_data = data.get("market_data", {})
            self.trade_history = data.get("trade_history", [])
            self.notes = data.get("notes", [])

    def save(self, filename):
        data = {
            "date": self.date,
            "cash_available": self.cash_available,
            "portfolio_value": self.portfolio_value,
            "positions": {symbol: pos.to_dict() for symbol, pos in self.positions.items()},
            "market_data": self.market_data,
            "trade_history": self.trade_history,
            "notes": self.notes
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def add_trade(self, date, action, symbol, quantity, price):
        if action == "buy":
            self._buy_position(symbol, quantity, price)
        elif action == "sell":
            self._sell_position(symbol, quantity, price)
        self.trade_history.append({
            "date": date,
            "action": action,
            "symbol": symbol,
            "quantity": quantity,
            "price": price
        })

    def _buy_position(self, symbol, quantity, price):
        if symbol not in self.positions:
            self.positions[symbol] = Position(symbol)
        self.positions[symbol].update_position(quantity, price)
        self.cash_available -= quantity * price

    def _sell_position(self, symbol, quantity, price):
        if symbol in self.positions:
            self.positions[symbol].update_position(-quantity, price)
            self.cash_available += quantity * price
            if self.positions[symbol].quantity == 0:
                del self.positions[symbol]

    def update_market_data(self, symbol, price):
        self.market_data[symbol] = price

    def add_cash(self, amount):
        self.cash_available += amount

    def set_portfolio_value(self, value):
        self.portfolio_value = value

    def add_note(self, date, note):
        self.notes.append({
            "date": date,
            "note": note
        })

    def __str__(self):
        positions_str = {symbol: str(pos) for symbol, pos in self.positions.items()}
        return json.dumps({
            "date": self.date,
            "cash_available": self.cash_available,
            "portfolio_value": self.portfolio_value,
            "positions": positions_str,
            "market_data": self.market_data,
            "trade_history": self.trade_history,
            "notes": self.notes
        }, indent=4)


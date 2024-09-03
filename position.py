class Position:
    def __init__(self, symbol, quantity=0, adjusted_cost_basis=0.0):
        self.symbol = symbol
        self.quantity = quantity
        self.adjusted_cost_basis = adjusted_cost_basis

    def update_position(self, quantity, price):
        total_cost = self.quantity * self.adjusted_cost_basis
        additional_cost = quantity * price
        self.quantity += quantity
        if self.quantity > 0:
            self.adjusted_cost_basis = (total_cost + additional_cost) / self.quantity
        else:
            self.adjusted_cost_basis = 0.0  # Reset if quantity drops to zero

    def __str__(self):
        return f"Symbol: {self.symbol}, Quantity: {self.quantity}, Adjusted Cost Basis: ${self.adjusted_cost_basis:.2f}"

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "quantity": self.quantity,
            "adjusted_cost_basis": self.adjusted_cost_basis
        }

    @staticmethod
    def from_dict(data):
        return Position(
            symbol=data["symbol"],
            quantity=data["quantity"],
            adjusted_cost_basis=data["adjusted_cost_basis"]
        )

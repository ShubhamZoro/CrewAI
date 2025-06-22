class Account:
    def __init__(self, username: str, initial_deposit: float = 0.0):
        """
        Initialize a new account with a username and an initial deposit amount.
        :param username: The username of the account holder.
        :param initial_deposit: The initial amount of money deposited in the account.
        """
        self.username = username
        self.balance = initial_deposit
        self.holdings = {}  # holds shares in the form {symbol: quantity}
        self.transactions = []  # records transaction history

    def deposit(self, amount: float) -> None:
        """
        Deposit funds into the account.
        :param amount: The amount to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraw funds from the account.
        :param amount: The amount to withdraw.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")

    def buy_shares(self, symbol: str, quantity: int) -> None:
        """
        Purchase shares for a specific stock symbol.
        :param symbol: The stock symbol to buy shares of.
        :param quantity: The number of shares to buy.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        share_price = get_share_price(symbol)
        total_cost = share_price * quantity
        
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to buy shares.")
        
        self.balance -= total_cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        
        self.transactions.append(f"Bought {quantity} shares of {symbol} at {share_price} each.")

    def sell_shares(self, symbol: str, quantity: int) -> None:
        """
        Sell shares for a specific stock symbol.
        :param symbol: The stock symbol to sell shares of.
        :param quantity: The number of shares to sell.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Not enough shares to sell.")
        
        share_price = get_share_price(symbol)
        total_value = share_price * quantity
        
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        
        self.balance += total_value
        self.transactions.append(f"Sold {quantity} shares of {symbol} at {share_price} each.")

    def calculate_portfolio_value(self) -> float:
        """
        Calculate the total value of the user's portfolio.
        :return: The total value of the portfolio.
        """
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def calculate_profit_loss(self) -> float:
        """
        Calculate the profit or loss from the initial deposit.
        :return: The profit or loss amount.
        """
        return self.calculate_portfolio_value() - self.balance

    def get_holdings(self) -> dict:
        """
        Get the current holdings of the user.
        :return: A dictionary of holdings.
        """
        return self.holdings

    def get_profit_loss(self) -> float:
        """
        Get the current profit or loss of the user.
        :return: Profit or loss amount.
        """
        return self.calculate_profit_loss()

    def get_transactions(self) -> list:
        """
        Retrieve the transaction history of the user.
        :return: A list of transactions.
        """
        return self.transactions

def get_share_price(symbol: str) -> float:
    """
    Get the current price of a share for a given symbol.
    :param symbol: The stock symbol to get the price for.
    :return: The current price of the share.
    """
    prices = {
        "AAPL": 150.0,
        "TSLA": 700.0,
        "GOOGL": 2800.0
    }
    return prices.get(symbol, 0.0)  # Defaults to 0.0 for unknown symbols
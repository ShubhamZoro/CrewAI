import gradio as gr
from accounts import Account

username = "user1"
account = Account(username)

def deposit(amount):
    try:
        account.deposit(amount)
        return f"Deposited ${amount:.2f}. New balance: ${account.balance:.2f}"
    except ValueError as e:
        return str(e)

def withdraw(amount):
    try:
        account.withdraw(amount)
        return f"Withdrew ${amount:.2f}. New balance: ${account.balance:.2f}"
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        account.buy_shares(symbol, quantity)
        return f"Bought {quantity} shares of {symbol}. New balance: ${account.balance:.2f}"
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        account.sell_shares(symbol, quantity)
        return f"Sold {quantity} shares of {symbol}. New balance: ${account.balance:.2f}"
    except ValueError as e:
        return str(e)

def portfolio_value():
    return f"Total portfolio value: ${account.calculate_portfolio_value():.2f}"

def profit_loss():
    return f"Profit/Loss: ${account.get_profit_loss():.2f}"

def holdings():
    return f"Holdings: {account.get_holdings()}"

def transactions():
    return f"Transactions: {account.get_transactions()}"

# Individual interfaces
deposit_ui = gr.Interface(fn=deposit, inputs=gr.Number(label="Amount"), outputs="text", title="Deposit")
withdraw_ui = gr.Interface(fn=withdraw, inputs=gr.Number(label="Amount"), outputs="text", title="Withdraw")
buy_ui = gr.Interface(fn=buy_shares, inputs=[gr.Textbox(label="Symbol"), gr.Number(label="Quantity")], outputs="text", title="Buy Shares")
sell_ui = gr.Interface(fn=sell_shares, inputs=[gr.Textbox(label="Symbol"), gr.Number(label="Quantity")], outputs="text", title="Sell Shares")
portfolio_ui = gr.Interface(fn=portfolio_value, inputs=[], outputs="text", title="Portfolio Value")
profit_ui = gr.Interface(fn=profit_loss, inputs=[], outputs="text", title="Profit / Loss")
holdings_ui = gr.Interface(fn=holdings, inputs=[], outputs="text", title="Holdings")
transactions_ui = gr.Interface(fn=transactions, inputs=[], outputs="text", title="Transactions")

# Tabbed interface
app = gr.TabbedInterface(
    [deposit_ui, withdraw_ui, buy_ui, sell_ui, portfolio_ui, profit_ui, holdings_ui, transactions_ui],
    ["Deposit", "Withdraw", "Buy Shares", "Sell Shares", "Portfolio Value", "Profit / Loss", "Holdings", "Transactions"]
)

if __name__ == "__main__":
    app.launch()

import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('test_user', 1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)
        self.assertRaises(ValueError, self.account.deposit, -100)

    def test_withdraw(self):
        self.account.withdraw(200.0)
        self.assertEqual(self.account.balance, 800.0)
        self.assertRaises(ValueError, self.account.withdraw, 2000)
        self.assertRaises(ValueError, self.account.withdraw, -100)

    def test_buy_shares(self):
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.balance, 700.0)
        self.assertRaises(ValueError, self.account.buy_shares, 'AAPL', 10)
        self.assertRaises(ValueError, self.account.buy_shares, 'AAPL', -1)

    def test_sell_shares(self):
        self.account.buy_shares('AAPL', 2)
        self.account.sell_shares('AAPL', 1)
        self.assertEqual(self.account.get_holdings()['AAPL'], 1)
        self.assertRaises(ValueError, self.account.sell_shares, 'AAPL', 5)
        self.assertRaises(ValueError, self.account.sell_shares, 'AAPL', -1)

    def test_portfolio_value(self):
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.calculate_portfolio_value(), 700.0 + get_share_price('AAPL') * 2)

    def test_profit_loss(self):
        self.assertEqual(self.account.calculate_profit_loss(), 0.0)
        self.account.deposit(500.0)
        self.assertGreater(self.account.calculate_profit_loss(), 0)

    def test_transactions(self):
        self.account.deposit(500.0)
        self.assertIn('Deposited 500.0', self.account.get_transactions())
        self.account.withdraw(200.0)
        self.assertIn('Withdrew 200.0', self.account.get_transactions())

if __name__ == '__main__':
    unittest.main()
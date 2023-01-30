from CheckingAccount import CheckingAccount

# This transaction will fail.
acc = CheckingAccount("Nimco Shah", "789 Paco St, Superb Tx 6589",568,500)
acc.debitAccount(600)
acc.availableBalance()


# This transaction will pass
acc = CheckingAccount("Robin Scherbatsky ", "6565 Nacho Dr, Levington Tx 7589",786,500)
acc.creditAccount(100)
acc.debitAccount(200)
acc.availableBalance()

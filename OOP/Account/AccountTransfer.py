import Account


class AccountTransfer(Account):

    def __index__(self, filepath):
        Account.__init__(str(self, filepath))


checking = AccountTransfer("Account\\balance.txt")
checking.deposite(10)



class BankAccount:
    def __init__(self, account_holder, balance, account_number):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = account_number

    def increase(self, amount):
        self.balance += amount
        return self.balance
    
    def decrease(self, amount): 
        if amount > self.balance:
            return print("Saldo kurang")
        
        self.balance = self.balance - amount
        return self.balance
    
    def display_info(self):
        print(f"No. Rekening: {self.account_number}, Pemilik: {self.account_holder}, Saldo: {self.balance}")

def main():
    accountNumber = int(input("Masukkan account number: "))
    accountBalance = int(input("Masukkan saldo awal: "))
    accountHolder = input("Masukkan nama pemegang akun: ")

    bankAccount = BankAccount(accountHolder, accountBalance, accountNumber)

    while True:
        toDo = input("(+/-/display): ")

        if toDo == "+":
            saldo = int(input("Saldo yang ingin di tambahkan? "))
            bankAccount.increase(saldo)

        if toDo == "-":
            saldo = int(input("Saldo yang ingin di hilangkan? "))
            bankAccount.decrease(saldo)

        if toDo == "display":
            bankAccount.display_info()

main()
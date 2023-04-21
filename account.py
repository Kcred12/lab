class Account:

    def __init__(self, name: str) -> None:
        """
        Function to set up account object.
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Allows user to deposit an amount into the account.
        :param amount: Desired user amount.
        :return: True or False depending on if process was successful.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Allows user to withdraw an amount from the account.
        :param amount: Desired user amount.
        :return: True or False depending on if process was successful.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Allows user to view balance.
        :return: User balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Allows user to view account name.
        :return: Account name.
        """
        return self.__account_name
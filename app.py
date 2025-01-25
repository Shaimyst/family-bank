import streamlit as st

st.title("Hello World")

class ChildAccount:
    def __init__(self, name: str, balance: float = 0.0):
        self.child_name = name
        self.balance = balance

    def get_balance(self) -> float:
        return self.balance

    def commit_transaction(self, amount: float):
        self.balance += amount

    def get_transaction_history(self):
        #stub
        pass

willow_account = ChildAccount("Willow")
penny_account = ChildAccount("Penny")

st.write("Willow's balance: ", willow_account.get_balance())
st.write("Penny's balance: ", penny_account.get_balance())

st.write("Committing transaction to Penny's account of +100")
penny_account.commit_transaction(100)

st.write("Penny's balance: ", penny_account.get_balance())

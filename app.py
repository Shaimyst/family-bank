import streamlit as st
import json

st.title("Family Bank")

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

st.write("Penny's balance: ", penny_account.get_balance())

st.header("Transaction")
child = st.selectbox("Child: ", ["Willow", "Penny"])
transaction_amount = st.number_input("Amount: ", step=1.0)
transaction_description = st.text_input("Description: ")
parent_name = st.selectbox("Parent: ", ["Dada", "Mamma"])
parent_password = st.text_input("Password: ", type="password")

if st.button("Commit transaction"):
    if child == "Willow":
        willow_account.commit_transaction(transaction_amount)
    else:
        penny_account.commit_transaction(transaction_amount)

    st.write("Transaction successful")

st.write("Willow's balance: ", willow_account.get_balance())
st.write("Penny's balance: ", penny_account.get_balance())

# update save file with new transactions
with open("transactions.json", "w") as f:
    transactions = {
        "transactions": [
            {
                "child": child,
                "amount": transaction_amount,
                "description": transaction_description,
                "parent": parent_name,
                "password": parent_password
            }
        ]
    }
    json.dump(transactions, f)

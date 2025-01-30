import streamlit as st
import json

# TODO: add load of transactions from file

st.title("Family Bank")

class Transaction:
    def __init__(self, child: str, amount: float, description: str, parent: str):
        self.child: str = child
        self.amount: float = amount
        self.description: str = description
        self.parent: str = parent

    def to_dict(self) -> dict:
        return {
            "child": self.child,
            "amount": self.amount,
            "description": self.description,
            "parent": self.parent
        }

class ChildAccount:
    def __init__(self, child: str):
        self.child: str = child
        self.transaction_history: list[Transaction] = []
        
    def get_balance(self) -> float:
        return sum(transaction.amount for transaction in self.transaction_history)

    def commit_transaction(self, transaction: Transaction):
        self.transaction_history.append(transaction)


# Instantiate child accounts
willow_account = ChildAccount("Willow")
penny_account = ChildAccount("Penny")

#load transactions from file
with open("transactions.json", "r") as f:
    transactions: list[Transaction] = []
    try:
        contents = json.load(f)
        for transaction in contents["transactions"]:
            transactions.append(
                Transaction(
                    transaction["child"], 
                    transaction["amount"], 
                    transaction["description"], 
                    transaction["parent"]
                )
            )
    except Exception as e:
        print("No transactions found, will start with empty accounts")
    for transaction in transactions:
        if transaction.child == "Willow":
            willow_account.commit_transaction(transaction)
        elif transaction.child == "Penny":
            penny_account.commit_transaction(transaction)
        else:
            st.error("Invalid child name")


# Transaction form
st.header("Transaction")
child = st.selectbox("Child: ", ["Willow", "Penny"])
transaction_amount = st.number_input("Amount: ", step=1.0)
transaction_description = st.text_input("Description: ")
parent_name = st.selectbox("Parent: ", ["Dada", "Mamma"])
parent_password = st.text_input("Password: ", type="password")

if st.button("Commit transaction"):
    if child == "Willow":
        willow_account.commit_transaction(
            Transaction(child, transaction_amount, transaction_description, parent_name)
        )
    else:
        penny_account.commit_transaction(
            Transaction(child, transaction_amount, transaction_description, parent_name)
        )
    with open("transactions.json", "w") as f:
        all_transactions: list[Transaction] = []
        all_transactions.extend([t.to_dict() for t in willow_account.transaction_history])
        all_transactions.extend([t.to_dict() for t in penny_account.transaction_history])
        json.dump({"transactions": all_transactions}, f)
        
    st.success("Transaction successful")

st.write("Willow's balance: ", willow_account.get_balance())
st.write("Penny's balance: ", penny_account.get_balance())

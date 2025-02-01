# family-bank
A bank application for parents and kids.

## Requirements
- Python 3.13+
- Poetry

## Setup for development

Install dependencies
```sh
poetry install
```

## Usage

Run the app
```sh
make up
```

## TODO
what should the app do?
the parents are the bank, the kids balance starts at 0
everytime they do something like chores, they get allowance 
then, a parent makes a deposit into their account
in order to make a deposit, a deposit amount is entered along with a parent's name and password
withdraws can also be made, but the withdraw amount must be less than the balance
withdraws will be a negative number + parent's name and password
account total should be displayed

## Steps to implement
[X] create a new file for the app
[X] implement child accounts
[X] implement display of account total per child
[X] implement deposit+withdrawal as transaction
[X] balance should not be allowed to go below 0
[X] implement parent authorization (parent's name and password)
[X] implement password check
[X] implement transaction history per child

## Ideas for improvements
[ ] Have a page for displaying transaction for a child
[ ] Decompose logic into more functions and write unit tests
[ ] Password should clear after each transaction is committed
[ ] Reset button to reset the user inputs
[ ] Make it so user is able to create more child accounts
[ ] Make it so user is able to create more parent accounts
[ ] Add a "delete account" option
[ ] Add a "delete transaction" option

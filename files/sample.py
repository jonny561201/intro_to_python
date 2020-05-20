import csv


def get_userid_account (account_id):
    file = open('accounts.csv')
    csv_file = csv.DictReader(file)
    for row in csv_file:
        if row ['AccountId'] == account_id:
            return(row['UserId'])


def get_userid_address (user_id):
    file = open("addresses.csv")
    csv_file = csv.DictReader(file)
    for row in csv_file:
        if row['UserId'] == user_id:
            return (row)


user_id = get_userid_account('576u34768423768234')
print(user_id)

address=get_userid_address(user_id)
print(address)
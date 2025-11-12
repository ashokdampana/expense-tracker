import csv 
import os


arr = []

def add_expense():
    amount = input('Enter amount..')
    arr.append( amount)
    with open('expenses.csv', 'a', newline='') as file:
        writer= csv.writer(file)
        writer.writerow([amount])

def view_expenses():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def main():
    operation = input('Enter operation (1.add/ 2.view/ 3.exit): ')
    if operation == '1':
        add_expense()
    elif operation == '2':
        view_expenses()
    else:
        exit()


if __name__ == '__main__':
    main()


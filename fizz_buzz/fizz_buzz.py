# Create an application that returns 'fizz' when a number is divisible by 3
# returns 'buzz' when a number is divisible by 5
# returns 'fizz_buzz' when a number is divisible by both 3 and 5

number = {'one':1,'two': 2,'three': 3,'five': 5,'twelve': 12,'fifteen': 15}


def fizzbuzz(numbers):
    for key ,value in numbers.items():
        if value % 3 == 0 and value % 5 ==0:
            print('fizz_buzz '+key)
        elif value % 3 == 0:
            print("fizz "+key)
        elif value % 5 == 0:
            print('buzz '+key)
        else:
            print(str(value) + ' ' +key)


# fizzbuzz(number)
test = number['twelve']

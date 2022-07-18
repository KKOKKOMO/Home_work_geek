from sys import argv


def salary_calculation():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'Salary - {time * rate + bonus}')
    except ValueError:
        print('Enter all 3 numbers')


salary_calculation()

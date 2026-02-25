'''
try:
    num1 = int(input('Enter Number: '))
    num2 = int(input('Enter another number:' ))
    result = num1/num2

    print(f'results = ',results)

except ZeroDivisionError:
    print('Cannot divide with 0')

finally:
    print('Program Ended')

def check_num(n):

    if n%2==0:
        print('The number is even')
    else:
        print('The number is odd')
def main():
    n=int(input('Enter a number: '))

    check_num(n)
main()

def max_num(a,b):

    if a > b:
        print(f'First number is gratter')
    else:
        print('Second number is gratter')

def main():
    a = int(input('Enter First number: '))
    b = int(input('Enter second number: '))
    max_num(a,b)
main()

def max_marks(n):
    if n>=95:
        print('O')
    elif n>=90:
        print('A+')
    elif n>= 85:
        print('A')
    elif n>= 80:
        print('B+')
    elif n>=75:
        print('B')
    elif n>=70:
        print('C+')
    elif n>=55:
        print('C')
    elif n>=50:
        print('P')
    else:
        print('Sorry you are Failed!!!')
def main():
    n = int(input('Enter the marks scored: '))
    max_marks(n)
main()
'''
def cal_fee(course, marks):
    course = course.strip().title()
    
    if course == 'Python':
        fee = 50000
    elif course == 'Java':
        fee = 45000
    elif course == 'Data Science':
        fee = 60000
    else:
        print('Invalid course name')
        return
    if marks >= 90:
        discount = 0.1 * fee
    elif marks >= 80:
        discount = 0.05 * fee
    else:
        discount = 0
    final_fee = fee - discount
    print(f'Course: {course}')
    print(f'Original Fee: {fee}')
    print(f'Discount: {discount}')
    print(f'Final Fee: {final_fee}')
def main():
    course = input('Enter the course name: ')
    marks = int(input('Enter the marks scored: '))
    cal_fee(course, marks)
main()

'''
Counting Problems:
it is total based on how many times counting has been initialized/occurred during the running time of program.

def count_even(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += i
    return count

def main():
    n = int(input('Enter number: '))
    print('Even count:', count_even(n))

main()
'''
def count_positive(number):
    count = 0
    for num in number:
        if num > 0:
            count += 1
    return count

def main():
    n = [4, -2, 5, -8]
    print('Positive numbers:', count_positive(n))

main()
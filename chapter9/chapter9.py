def print_10_stars():
    for _ in range(10):
        print('*', end=' ')
    print()
print_10_stars()

def print_5_stars():
    for _ in range(5):
        print('*', end=' ')
    print()
print_10_stars()

def problem_2():
    print_10_stars()
    print_5_stars()
    print_20_stars()

def problem_3():
    for _ in range(10):
        print_10_stars()
    print()

problem_3()

def problem_4():
    for _ in range(10): # rows
        for _ in range(5): # columns
            print('*', end=' ')
        print()

problem_4()

def problem_5():
    for _ in range(5): # rows
        for _ in range(20): # columns
            print('*', end=' ')
        print()

problem_5()

def problem_6():
    for i in range(10):
        for i in range(10):
            print(i, end=' ')
        print()

problem_6()

def problem_7():
    for _ in range(10):
        for i in range(10):
            print(i, end=' ')
        print()
        
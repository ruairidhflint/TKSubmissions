# EXERCISE 1
# 1.)
minute = 60

my_time = (21 * minute) + 15
print(my_time)  # 1275

# 2.)

miles_in_5k = 5 * 0.621371
print(miles_in_5k)  # 3.106855

# 3.)

mph = my_time/miles_in_5k
mph_converted_mins = mph//60
mph_converted_secs = mph % 60

print(f"{mph_converted_mins:.0f} minutes and {mph_converted_secs:.0f} seconds")

# 4.)

hour_in_seconds = 60 * 60
print(f"{hour_in_seconds/mph:.2f} miles per hour")

# 5.)

book_price_with_discount = 19.95 * 0.75

print((book_price_with_discount + 2.5) + ((book_price_with_discount + 1)) * 74)

# EXERCISE 2


def do_twice(f, val):
    f(val)
    f(val)

# def print_spam():
#     print('spam')

# do_twice(print_spam, 'Rory')


def print_twice(val2):
    print(val2)
    print(val2)


do_twice(print_twice, 'Spam')


def do_four(f):
    for x in range(4):
        f('Rory')


do_four(print_twice)

# Exercise 3


def check_fermat(a, b, c, n):
    if n > 2:
        if a**n + b**n == c**n:
            return "Holy smokes, Fermat was wrong!"
        else:
            return "No, that doesn't work."
    else:
        return "N must be larger than 2 and a, b and c must be valid integers."


def validate_inputs():
    inputs = input(
        'Please enter four comma separated integers to check Fermats theory: ').split(',')
    try:
        a = int(inputs[0])
        b = int(inputs[1])
        c = int(inputs[2])
        n = int(inputs[3])

    except ValueError:
        return "Oops!  That was not a valid number.  Try again..."

    return check_fermat(a, b, c, n)

print(validate_inputs())


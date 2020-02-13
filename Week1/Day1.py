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

# print(validate_inputs())

# LISTS
# A list is used to store multiple pieces of data in a 'list' like structure, similar to an
# array in JS. A list allows duplicates, objects, other lists etc to be stored inside and so is
# a very versatile and easily accessible format. A list is used to store almost anything and when
# you will need to mutate the values, add values or remove values.
# Lists are also ordered which is often important.


my_list = [1, 2, 3, 4]
my_list[1]
my_list[-1] = 5

for item in my_list:
    print(item)

if 4 in my_list:
    print("4 is in your list!")

print(len(my_list))

my_list.append(12)
my_list.insert(2, 99)

del my_list[-1]

my_list.clear()

my_new_list = list([1, 2, 3, 4])

# LISTS
# Dictionaries are essentially objects in JS. They allow values to be stored next to keys
# which are then easily accessible via object notation. They are primarily used when the information
# you are storing needs to be stored with a key. Dictionaries are unordered and the order is unpredictable.

my_dictionary = {'foo': 'foo', 'baz': 'baz'}
my_dictionary['foo']
my_dictionary['foo'] = 'foo2'

for k, v in my_dictionary.items():
    print(k)
    print(v)

my_dictionary.values()

if 'baz' in my_dictionary:
    print("It's alive!")

print(len(my_dictionary))

my_dictionary['new'] = 'new'
my_dictionary.pop('new')
my_dictionary.clear()

my_dictionary = dict([('phew', 'phew')])

# Tuples
# Tuples are similar to lists except they are immutable. The values cannot be changed. This is extremely helpful if you have a permanent data set, say id's and names, the alphabet, a strict set of values etc that under no circumstance do you want to be accidently overwritten or changed in any way.

my_tuple = (1, 2, 3, 4)

my_tuple[0]
#not possible

for x in my_tuple:
    print(x)

if 2 in my_tuple:
    print('Death to traitors')

print(len(my_tuple))

del my_tuple

my_tuple = tuple([1,])

# SETS
# Sets, again, are not dissimialr to Lists. They are mutable, but each value is unique. This is excellent for an instance where duplicates cannot exist. It is almost excellent for testing for duplication etc. 

my_set = {92, 93, 94, 95}

for item in my_set:
    print(item)

if 92 in my_set:
    print('Game set and match')

my_set.add(99)
my_set.update([100,1001])

print(len(my_set))

my_set.remove(1001)
my_set.discard('hello')
# my_set.pop() No 'last item' ?
my_set.clear()

del my_set

my_set = set('hey!')

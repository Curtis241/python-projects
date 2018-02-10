from math import sqrt


def find_key(param, key_list):
    find_list = list()
    for k in key_list:
        if k.find(param) is not -1:
            find_list.append({'key': k, 'find_result': k.find(param)})
    return find_list


def filter_keys(param, key_list):
    return [k for k in key_list if k.find(param) is -1]


def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n+1, i)}
        p = {x for x in range(2, n + 1) if x not in no_p}
    return p


def generate_prime_numbers():
    no_primes = [j for i in range(2, 8) for j in range(i * 2, 100, i)]
    return [x for x in range(2, 100) if x not in no_primes]


def calculate_square_root(value):
    sqrt_n = int(sqrt(value))
    no_primes = {j for i in range(2, sqrt_n) for j in range(i * 2, value, i)}
    return {i for i in range(value) if i not in no_primes}


def generate_list_of_numbers():
    return list((x ** 2 for x in range(20)))


def coloured_things(colours, things):
    return [(x, y) for x in colours for y in things]


def generate_pythagorean_triples():
    return [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x ** 2 + y ** 2 == z ** 2]


def celsius_to_fahrenheit(celsius):
    return [((float(9) / 5) * x + 32) for x in celsius]


print(celsius_to_fahrenheit([39.2, 36.5, 37.3, 37.8]))
print(celsius_to_fahrenheit([-10, -2, -17.7559]))
print(generate_pythagorean_triples())
print(coloured_things(["red", "green", "yellow", "blue"], ["house", "car", "tree"]))
print(generate_list_of_numbers())
print(generate_prime_numbers())
print(calculate_square_root(100))

for i in range(1,50):
    print(i, primes(i))

key_list = [
    "Parent1.Child1.Key1=1",
    "Parent1.Child1.Key2=1",
    "Parent1.Child1.Key3=1",
    "Parent1.Child1.Key4=1",
    "Parent1.Child1.Key5=1",
    "Parent2.Child2.Key1=1",
    "Parent2.Child2.Key2=1",
    "Parent2.Child2.Key3=1",
    "Parent2.Child2.Key4=1",
    "Parent2.Child2.Key5=1"
]

print(filter_keys("Child1", key_list))

#print(find_key("Child1", key_list))
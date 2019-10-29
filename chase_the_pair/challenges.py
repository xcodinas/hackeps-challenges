import random
import time


def close_pair(a, b, to_chase):
    pairs = [
        {
            'index': i,
            'sum': (
                to_chase - item if to_chase >= item else item - to_chase) + (
                    to_chase - b[i] if to_chase >= item else item - b[i])
            } for i, item in enumerate(a)
        ]
    pairs.sort(key=lambda x: x.get('sum'))
    return [a[pairs[0].get('index')], b[pairs[0].get('index')]]


def generate_sets(size, number=2):
    return [[
            random.randint(1, 999) for x in range(0, size)] for _ in range(
            0, number)]

if __name__ == '__main__':
    try:
        set_size = int(input(
                "Insert the size of the sets that will be generated:\n"))
        start_time = time.time()
        a, b = generate_sets(set_size)
        chase_number = random.randint(1, 999)
        print("------------RESULTS SECTION----------")
        print("Number to chase: %s" % chase_number)
        print("Result: %s" % close_pair(a, b, chase_number))
        print("--- %s seconds ---" % (time.time() - start_time))
    except ValueError:
        print("Size must be an Integer")

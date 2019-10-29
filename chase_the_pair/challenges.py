import random
import time


def close_pair(a, b, to_chase):
    pairs = []
    for index, item in enumerate(a):
        if to_chase >= item:
            close_upper = to_chase - item
        elif to_chase <= item:
            close_upper = item - to_chase

        if to_chase >= b[index]:
            close_lower = to_chase - b[index]
        elif to_chase <= b[index]:
            close_lower = b[index] - to_chase

        pairs.append({
            'upper': item,
            'lower': b[index],
            'close_upper': close_upper,
            'close_lower': close_lower,
            'sum': close_upper + close_lower,
            })

    pairs.sort(key=lambda x: x.get('sum'))
    return [pairs[0].get('upper'), pairs[0].get('lower')]


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

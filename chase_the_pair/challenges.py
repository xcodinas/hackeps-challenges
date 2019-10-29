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


def parse_sets(filename):
    with open(filename) as f:
        data = f.read()
        return ([int(a) for a in data.split('\t')[0][2:-1].split(',')],
            [int(b) for b in data.split('\t')[1][2:-2].split(',')])


def get_chase(a, b):
    return random.randint(min(min(a), min(b)), max(max(a), max(b)))


if __name__ == '__main__':
    a, b = parse_sets('logs.txt')
    chase_number = get_chase(a, b)
    start_time = time.process_time()
    print("------------RESULTS SECTION----------")
    print("Number to chase: %s" % chase_number)
    print("Result: %s" % close_pair(a, b, chase_number))
    print("--- %s seconds ---" % (time.process_time() - start_time))

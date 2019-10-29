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

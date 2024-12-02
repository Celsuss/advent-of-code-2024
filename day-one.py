

def load_data(path: str) -> (list[int], list[int]):
    f = open(path)
    left, right = [], []
    for line in f:
        split_line = line.split('   ')
        left.append(int(split_line[0]))
        right.append(int(split_line[-1].strip()))
        continue
    return left, right


def partOne(left: list[int], right: list[int]):
    """Solution to part one."""
    left.sort()
    right.sort()
    dif = 0
    for l, r in zip(left, right):
        dif += abs(r - l)
    return dif


def partTwo(left: list[int], right: list[int]):
    """Solution for part two."""
    score = 0
    for l in left:
        score += l * right.count(l)
    return score


def main():
    """Main function."""
    """ Part one """
    left, right = load_data('data/day-one-test.txt')
    res = partOne(left, right)
    assert res == 11

    left, right = load_data('data/day-one.txt')
    res = partOne(left, right)
    print(f'Day one part one output is {res}')

    """ Part two"""
    left, right = load_data('data/day-one-test.txt')
    res = partTwo(left, right)
    assert res == 31

    left, right = load_data('data/day-one.txt')
    res = partTwo(left, right)
    print(f'Day one part two output is {res}')


if __name__ == '__main__':
    main()

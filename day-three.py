"""Day three advent of code."""


def setIsActive(mem: str, i: int, is_active: bool) -> bool:
    """Set is_active depending on if do() or don't() is found in mem."""
    kalle1 = mem[i:i+7]
    kalle2 = mem[i:i+4]
    if is_active is True and \
       mem[i:i+7] == 'don\'t()':
        return False
    elif is_active is False and \
         mem[i:i+4] == 'do()':
        return True
    return is_active


def getMulValues(mem: str, do_dont_enable: bool = False) -> list[(int, int)]:
    """Find all mul values in mem."""
    vals = []
    is_active = True
    for i in range(len(mem)-3):
        if do_dont_enable is True:
            is_active = setIsActive(mem, i, is_active)

        # Don't keep looking for mul when not active
        if is_active is False:
            continue

        if mem[i:i+4] != 'mul(':
            continue
        try:
            num1 = mem[i+4: mem.find(',', i)]
            num2 = mem[mem.find(',', i)+1:mem.find(')', i)]
            vals.append((int(num1), int(num2)))
            i = mem.find(')', i)
            continue
        except:
            continue
    return vals

def partOne(mem: str) -> int:
    """Part one solution.

    It seems like the goal of the program is just to multiply some numbers.
    It does that with instructions like mul(X,Y), where X and Y are each 1-3
    digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result
    of 2024. Similarly, mul(123,4) would multiply 123 by 4.

    However, because the program's memory has been corrupted, there are also
    many invalid characters that should be ignored, even if they look like part
    of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34),
    or mul ( 2 , 4 ) do nothing.

    Scan the corrupted memory for uncorrupted mul instructions. What do you get
    if you add up all of the results of the multiplications?
    """
    prod_sum = 0
    vals = getMulValues(mem)
    for i in vals:
        prod_sum += i[0] * i[1]

    return prod_sum


def partTwo(mem: str) -> int:
    """Part two solution.

    There are two new instructions you'll need to handle:

    The do() instruction enables future mul instructions.
    The don't() instruction disables future mul instructions.
    Only the most recent do() or don't() instruction applies. At the beginning
    of the program, mul instructions are enabled.
    """
    prod_sum = 0
    vals = getMulValues(mem, do_dont_enable=True)
    for i in vals:
        prod_sum += i[0] * i[1]

    return prod_sum


def getData(path: str) -> str:
    "Load data."
    f = open(path)
    lines = f.readlines()
    mem = ''
    for i in lines:
        mem += i
    return mem


def main():
    """Main function of day two."""
    # Part one
    data = getData('data/day-three-test.txt')
    res = partOne(data)
    assert res == 161

    data = getData('data/day-three.txt')
    res = partOne(data)
    print(f'Day two part one solution: {res}')
    assert res == 174561379

    # Part two
    data = getData('data/day-three-test.txt')
    res = partTwo(data)
    assert res == 48

    data = getData('data/day-three.txt')
    res = partTwo(data)
    print(f'Day two part two solution: {res}')
    assert res == 106921067
    return


if __name__ == '__main__':
    main()

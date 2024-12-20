"""Advent of code 2024 day two."""


def isIncreasing(report: list[int]) -> bool:
    if report[0] > report[1]:
        return False
    return True


def isReportSafe(report: list[int]) -> bool:
    """
    Is report safe.

    A report only counts as safe if both of the following are true:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """
    incremental = isIncreasing(report)
    prev_num = report[0]
    for num in report[1:]:
        delta = abs(num - prev_num)
        if (incremental is True and num < prev_num) or \
            (incremental is False and num > prev_num) or \
            (delta > 3 or delta == 0):
            return False
        prev_num = num
    return True


def partOne(reports: list[list[int]]) -> int:
    """Part one solution.

    The engineers are trying to figure out which reports are safe.
    The Red-Nosed reactor safety systems can only tolerate levels
    that are either gradually increasing or gradually decreasing.
    """
    safe_count = 0
    for report in reports:
        if isReportSafe(report):
            safe_count += 1
    return safe_count


def isReportSafeUpdated(report: list[int]) -> bool:
    """
    Is report safe.

    A report only counts as safe if both of the following are true:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

    It is now possible to remove a single number from an unsafe report to try
    and make it safe.
    """
    incremental = isIncreasing(report)
    prev_num = report[0]
    for i in range(1, len(report)):
        num = report[i]
        delta = abs(num - prev_num)

        if (incremental is True and num < prev_num) or \
            (incremental is False and num > prev_num) or \
            (delta > 3 or delta == 0):
            if i-2 >= 0:
                new_report = report.copy()
                del new_report[i-2]
                if isReportSafe(new_report) is True:
                    return True

            new_report = report.copy()
            del new_report[i-1]
            if isReportSafe(new_report) is True:
                return True

            new_report = report.copy()
            del new_report[i]
            return isReportSafe(new_report)

        prev_num = num
    return True


def partTwo(reports: list[list[int]]) -> int:
    """Part one solution.

    Now, the same rules apply as before, except if removing a single level from
    an unsafe report would make it safe, the report instead counts as safe.

    """
    safe_count = 0
    for report in reports:
        if isReportSafeUpdated(report):
            safe_count += 1
    return safe_count


def getData(path: str) -> list[list[int]]:
    """Load data from file."""
    f = open(path)
    reports = []
    for line in f:
        report = line
        reports.append(
            list(
                map(
                    int, report.split()
                )
            )
        )
    return reports


def main():
    """Main function of day two."""
    # Part one
    data = getData('data/day-two-test.txt')
    res = partOne(data)
    assert res == 2

    data = getData('data/day-two.txt')
    res = partOne(data)
    assert res == 534
    print(f'Day two part one solution: {res}')


    # Part two
    data = getData('data/day-two-test.txt')
    res = partTwo(data)
    assert res == 4

    data = getData('data/day-two.txt')
    res = partTwo(data)
    print(f'Day two part two solution: {res}')
    assert res == 577
    return


if __name__ == '__main__':
    main()

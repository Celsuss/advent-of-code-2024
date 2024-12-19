"""Advent of code 2024 day two."""


def isReportSafe(report: list[int]) -> bool:
    """
    Is report safe.

    A report only counts as safe if both of the following are true:
    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.
    """
    safe = True
    prev_i = report[0]
    for i in report[1:]:

        continue
    return safe


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
        continue

    return safe_count


def partOneTwo(reports: list[list[int]]) -> int:
    """Part one solution."""
    for report in reports:
        continue

    return 0


def getData(path: str) -> list[list[int]]:
    """Load data from file."""
    f = open(path)
    reports = []
    for line in f:
        report = line
        reports.append(report.split())
    return reports


def main():
    """Main function of day two."""
    data = getData('data/day-two-test.txt')
    res = partOne(data)
    assert res == 2

    data = getData('data/day-two.txt')
    res = partOne(data)
    print(f'Day two part one solution: {res}')
    return


if __name__ == '__main__':
    main()

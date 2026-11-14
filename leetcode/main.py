import argparse
import sys

from leetcode.test_suites import ALL_TEST_SUITES
from leetcode.interfaces import Suite

SUITES_BY_NUMBER: dict[str, Suite] = {x.number: x for x in ALL_TEST_SUITES}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "number",
        choices=SUITES_BY_NUMBER.keys(),
        help="Problem number to run (e.g. p0001).",
    )
    args = parser.parse_args()
    suite = SUITES_BY_NUMBER[args.number]
    return suite.run()


if __name__ == "__main__":
    sys.exit(main())

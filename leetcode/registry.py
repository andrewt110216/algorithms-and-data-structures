from leetcode.p0001 import P0001_TEST_SUITE
from leetcode.p0003 import P0003_TEST_SUITE
from leetcode.p0019 import P0019_TEST_SUITE
from leetcode.p0020 import P0020_TEST_SUITE
from leetcode.interfaces import Suite

TEST_SUITE_REGISTRY: list[Suite] = [
    P0001_TEST_SUITE,
    P0003_TEST_SUITE,
    P0019_TEST_SUITE,
    P0020_TEST_SUITE,
]

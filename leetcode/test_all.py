from leetcode.test_suites import ALL_TEST_SUITES
from leetcode.interfaces import Solver, Case

import pytest


@pytest.mark.parametrize(
    "solver, case",
    [
        pytest.param(
            solver,
            case,
            id=f"{suite.number} {suite.name} - {solver.name} - {case.name}",
        )
        for suite in ALL_TEST_SUITES
        for solver in suite.solvers
        for case in suite.cases
    ],
)
def test(solver: Solver, case: Case):
    result = case.evaluate(solver)
    assert result.passed, result.diff()

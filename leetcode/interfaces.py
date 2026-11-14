import time

from copy import deepcopy
from dataclasses import dataclass
from typing import Callable, ClassVar, TypeAlias


class ExpectedError(Exception):
    """
    Expected error type from solver.
    """


class NoSolutionError(ExpectedError):
    """
    The test case is expected to have no solution.
    """


@dataclass(frozen=True)
class Solver:
    name: str
    fn: Callable


# Input to a solver. Put into a list.
InputT: TypeAlias = list

# Output of a solver. Generally put outputs in a list.
# If solver is expected to raise an error, use ExpectedError instance.
OutputT: TypeAlias = list | ExpectedError | None


@dataclass(frozen=True)
class Result:
    passed: bool
    actual: OutputT
    expected: OutputT
    error: Exception | None
    elapsed_s: float

    def diff(self) -> str:
        out = f"Expected {self.expected!r}, got {self.actual!r}."
        if self.error is not None:
            out += f" Exception:\n{self.error}"
        return out


# Callable to check if a solver output matches the case's expected result.
CheckerT: TypeAlias = Callable[[OutputT, OutputT], bool]

# Stock checkers.


def check_eq(actual: OutputT, expected: OutputT) -> bool:
    """
    Simple equality checker.
    """
    return actual == expected


def check_unordered(actual: OutputT, expected: OutputT) -> bool:
    """
    Order of the top-level list does not matter; order within each element
    does. E.g. permutations: [[1, 2], [2, 1]] == [[2, 1], [1, 2]].
    """
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False
    return sorted(actual) == sorted(expected)


def check_unordered_nested(actual: OutputT, expected: OutputT) -> bool:
    """
    Order matters at neither the top level nor within each (list) element.
    E.g. combinations: [[1, 2], [3, 1]] == [[1, 3], [2, 1]].
    """
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False
    return check_unordered(
        [sorted(x) for x in actual],
        [sorted(x) for x in expected],
    )


@dataclass(frozen=True)
class Case:
    """
    Generic test case for a leetcode problem.
    """

    # Readable description of the test case.
    name: str
    # Test case input.
    inputs: InputT
    # Expected output.
    expected: OutputT
    # Checker to compare expected to solver result.
    checker: CheckerT = check_eq

    def evaluate(self, solver: Solver) -> Result:
        start = time.perf_counter()
        try:
            actual = solver.fn(*deepcopy(self.inputs))
            elapsed_s = time.perf_counter() - start
        except Exception as e:
            elapsed_s = time.perf_counter() - start
            if not isinstance(self.expected, ExpectedError):
                raise
            return Result(
                passed=type(e) == type(self.expected),
                actual=None,
                expected=self.expected,
                error=e,
                elapsed_s=elapsed_s,
            )

        expected = deepcopy(self.expected)
        return Result(
            passed=self.checker(actual, expected),
            actual=actual,
            expected=self.expected,
            error=None,
            elapsed_s=elapsed_s,
        )


@dataclass(frozen=True)
class Suite:
    """
    Collection of test cases and solver functions to be tested.
    """
    # Console output width.
    WIDTH: ClassVar[int] = 79

    number: str
    name: str
    solvers: list[Solver]
    cases: list[Case]

    def run(self) -> bool:
        """
        Run test suite and display results to the console.

        Returns True if every case passed for every solver.
        """
        print(f" {self.number} - {self.name} ".center(self.WIDTH, "="))
        total = failed = 0

        for case in self.cases:
            print()
            print(f" {case.name} ".center(self.WIDTH, "-"))
            print(f"Input:    {_truncate(case.inputs)}")
            print(f"Expected: {_truncate(case.expected)}")

            for solver in self.solvers:
                total += 1
                try:
                    result = case.evaluate(solver)
                except Exception as e:
                    # Unexpected exception: report it and keep going.
                    failed += 1
                    print(f"  {solver.name}: ERROR")
                    print(f"    {e!r}")
                    continue

                if not result.passed:
                    failed += 1
                status = "PASS" if result.passed else "FAIL"
                ms = result.elapsed_s * 1000
                print(f"  {solver.name}: {status} ({ms:.3f} ms)")
                output = result.error if result.error else result.actual
                print(f"    Output: {_truncate(output)}")

        print()
        print(" Summary ".center(self.WIDTH, "="))
        verdict = "PASS" if failed == 0 else "FAIL"
        print(f"{total} run, {failed} failed: {verdict}")
        return failed == 0


def _truncate(value: object, max_len: int = 60) -> str:
    """
    repr() of value, shortened to max_len characters by eliding the middle.
    """
    s = repr(value)
    if len(s) <= max_len:
        return s
    half = (max_len - 5) // 2
    return f"{s[:half]} ... {s[-half:]}"

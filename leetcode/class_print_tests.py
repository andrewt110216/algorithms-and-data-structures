from datetime import datetime
import copy


class PrintTests:
    """Use to print detail and summary of test case results"""

    def __init__(self, solution, cases, ordered_d1=True, ordered_d2=True):
        """
        :param list cases: the test cases to be run, in the format:
            [str description, list args, expected result]
        :param Solution solution: a class with methods representing solutions
            to the problem and an attribute 'implementations' listing the names
            of the methods to be evaluated
        :param bool ordered_d1: indicates if the order of the first dimension
            of the results (if it is a list or tuple) matters.
            If set to 'false', the result and expected result will be sorted
        :param bool ordered_d2: indicates if the order of the second dimension
            of the results (if it is a list or tuple) matters.
            If set to 'false', the result and expected result will be sorted
        """
        self.cases = cases
        self.solution = solution
        self.ordered_d1 = ordered_d1
        self.ordered_d2 = ordered_d2

        # make sure solution has an attribute called 'implementations'
        try:
            getattr(self.solution, "implementations")
        except AttributeError:
            raise AttributeError(
                "Solution must have an attribute 'implementations', which is"
                "a list of the names of the solution methods in Solution."
            )

        self.tests = 0
        self.failed_tests = 0
        self.print_width = 78
        self.max_io_len = 50

    def truncate_display(self, var):
        """Truncate the display of a long variable for printing to console"""
        if len(str(var)) > self.max_io_len:
            display = (
                str(var)[: self.max_io_len // 2]
                + "... "
                + str(var)[-self.max_io_len // 2 :]
            )
            return display
        else:
            return var

    def tuples_to_lists(self, var):
        """Check the input for any tuples, and convert them to lists"""

        # if var is not subscriptable, it has no tuples, so return it as is
        if not var or hasattr(var, "__getitem__") is False:
            return var

        # var must be a tuple, list, or dictionary
        # handle each type, looking for one layer of nested tuples, as well
        if type(var) is tuple:
            if type(var[0]) is not tuple:
                return list(var)
            else:
                return [list(x) for x in var]
        elif type(var) is list:
            if type(var[0]) is not tuple:
                return var
            else:
                return [list(x) for x in var]
        elif type(var) is dict:
            for key, value in var.items():
                if type(value) is tuple:
                    var[key] = list(value)
            return var

    def sort_list(self, var):
        if var and type(var) is list:
            if not self.ordered_d1:
                var.sort()
            if type(var[0]) is list:
                if not self.ordered_d2:
                    [x.sort() for x in var]
        return var

    def decorator(self, func):
        def wrapper(self, expected, *args):

            self.tests += 1
            start = datetime.now()
            result = func(*args)
            end = datetime.now()

            # check input/out for any tuples and convert them to lists
            result = self.tuples_to_lists(result)
            expected = self.tuples_to_lists(expected)

            # sort input/output if the order does not matter
            if not self.ordered_d1 or not self.ordered_d2:
                result = self.sort_list(result)
                expected = self.sort_list(expected)

            # truncate display of output/expected for printing to console
            result_display = self.truncate_display(result)
            expected_display = self.truncate_display(expected)

            # print and evaluate results
            print("    Output:", result_display)
            print("    Time:", end - start)
            if result == expected:
                print("\n  > Result: **PASS!**\n")
            else:
                self.failed_tests += 1
                print("\n  > Result: **FAIL.**\n")
                print(f"\t > Expected Result: {expected_display}\n")

        return wrapper

    def summarize(self):

        # print number of tests run and failed, and overall results (pass/fail)
        print(" SUMMARY OF RESULTS ".center(self.print_width, "="))
        print(f"\nTOTAL TESTS RUN: {self.tests}")
        print("\nOVERALL RESULT:\n")

        if self.failed_tests:
            final_result = "FAIL."
            print(f"\t{self.failed_tests} test(s) failed.\n")
        else:
            final_result = "PASS!"
            print("\tAll tests passed! Niceee.\n")

        print("\t===========")
        print(f"\t|| {final_result} ||")
        print("\t===========\n")
        print("".center(self.print_width, "*"), "\n")

    def run(self):

        print()
        print(" RUNNING TEST CASES ".center(self.print_width, "*"))
        print()

        # run all test cases
        for description, args, expected in self.cases:
            print(f" CASE: {description} ".center(self.print_width, "-"))

            # truncate display of input for printing to console
            args_display = [self.truncate_display(arg) for arg in args]
            print("\nInput:", args_display, "\n")

            # execute test case for each implementation
            for func_str in self.solution.implementations:
                print(" - Implementation:", func_str)
                func = self.decorator(getattr(self.solution, func_str))

                # use a deep copy of args so side effects on pass-by-reference
                # variables do not persist for subsequent implementations
                args_copy = copy.deepcopy(args)
                func(self, expected, *args_copy)

        self.summarize()

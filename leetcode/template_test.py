from template_solution import Solution

class TestClass:

    # run test case for each implementation in Solution
    s = Solution()
    def run_funcs(self, args, expected):
        for implementation in self.s.implementations:
            func = getattr(self.s, implementation)
            assert func(*args) == expected

    def test1_example1(self):
        args = [True]
        expected = False
        self.run_funcs(args, expected)

    def test1_example1(self):
        args = [False]
        expected = True
        self.run_funcs(args, expected)
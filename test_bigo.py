import unittest
import sys

from bigo import (
    length_of_longest_substring_n3,
    length_of_longest_substring_n2,
    length_of_longest_substring_n,
)


class TestLongestSubstringN3(unittest.TestCase):
    """Test O(N^3) implementation."""

    def test_length_of_longest_substring_n3_1(self):
        """O(N^3) approach with input 'bevo', answer is 4."""
        self.assertEqual(length_of_longest_substring_n3("bevo"), 4)

    def test_length_of_longest_substring_n3_2(self):
        """O(N^3) approach with empty string input, answer is 0."""
        self.assertEqual(length_of_longest_substring_n3(""), 0)

    def test_length_of_longest_substring_n3_3(self):
        """O(N^3) approach with input 'Longhorns', answer is 6."""
        self.assertEqual(length_of_longest_substring_n3("Longhorns"), 6)

    def test_length_of_longest_substring_n3_4(self):
        """O(N^3) approach with input 'abcdefghijk', answer is 11."""
        self.assertEqual(length_of_longest_substring_n3("abcdefghijk"), 11)

    def test_length_of_longest_substring_n3_5(self):
        """O(N^3) approach with input 'cs313e', answer is 4."""
        self.assertEqual(length_of_longest_substring_n3("cs313e"), 4)

    def test_length_of_longest_substring_n3_6(self):
        """O(N^3) approach with input 'bevoBits', answer is 8."""
        self.assertEqual(length_of_longest_substring_n3("bevoBits"), 8)

    def test_length_of_longest_substring_n3_7(self):
        """O(N^3) approach with input 'UTTower', answer is 5."""
        self.assertEqual(length_of_longest_substring_n3("UTTower"), 5)

    def test_length_of_longest_substring_n3_8(self):
        """O(N^3) approach with input 'CompSci', answer is 7."""
        self.assertEqual(length_of_longest_substring_n3("CompSci"), 7)
    def test_length_of_longest_substring_n3_9(self):
        """O(N^3) approach with input 'abcda', answer is 4."""
        self.assertEqual(length_of_longest_substring_n3("abcda"), 4)

    def test_length_of_longest_substring_n3_10(self):
        """O(N^3) approach with input 'anviaj', answer is 5."""
        self.assertEqual(length_of_longest_substring_n3("anviaj"), 5)


class TestLongestSubstringN2(unittest.TestCase):
    """Test O(N^2) implementation."""

    def test_length_of_longest_substring_n2_1(self):
        """O(N^2) approach with input 'bevo', answer is 4."""
        self.assertEqual(length_of_longest_substring_n2("bevo"), 4)

    def test_length_of_longest_substring_n2_2(self):
        """O(N^2) approach with empty string input, answer is 0."""
        self.assertEqual(length_of_longest_substring_n2(""), 0)

    def test_length_of_longest_substring_n2_3(self):
        """O(N^2) approach with input 'Longhorns', answer is 6."""
        self.assertEqual(length_of_longest_substring_n2("Longhorns"), 6)

    def test_length_of_longest_substring_n2_4(self):
        """O(N^2) approach with input 'abcdefghijk', answer is 11."""
        self.assertEqual(length_of_longest_substring_n2("abcdefghijk"), 11)

    def test_length_of_longest_substring_n2_5(self):
        """O(N^2) approach with input 'cs313e', answer is 4."""
        self.assertEqual(length_of_longest_substring_n2("cs313e"), 4)

    def test_length_of_longest_substring_n2_6(self):
        """O(N^2) approach with input 'bevoBits', answer is 8."""
        self.assertEqual(length_of_longest_substring_n2("bevoBits"), 8)

    def test_length_of_longest_substring_n2_7(self):
        """O(N^2) approach with input 'UTTower', answer is 5."""
        self.assertEqual(length_of_longest_substring_n2("UTTower"), 5)

    def test_length_of_longest_substring_n2_8(self):
        """O(N^2) approach with input 'CompSci', answer is 7."""
        self.assertEqual(length_of_longest_substring_n2("CompSci"), 7)

    def test_length_of_longest_substring_n2_9(self):
        """O(N^2) approach with input 'abcda', answer is 4."""
        self.assertEqual(length_of_longest_substring_n2("abcda"), 4)

    def test_length_of_longest_substring_n2_10(self):
        """O(N^2) approach with input 'anviaj', answer is 5."""
        self.assertEqual(length_of_longest_substring_n2("anviaj"), 5)

    def test_length_of_longest_substring_n2_11(self):
        """O(N^2) approach with input 'tmmzuxt', answer is 5."""
        self.assertEqual(length_of_longest_substring_n2("tmmzuxt"), 5)

    def test_length_of_longest_substring_n2_12(self):
        """O(N^2) approach with input 'qrstuqr', answer is 5."""
        self.assertEqual(length_of_longest_substring_n2("qrstuqr"), 5)

    def test_length_of_longest_substring_n2_13(self):
        """O(N^2) approach with input 'UTCS!rocks4EVER', answer is 13."""
        self.assertEqual(length_of_longest_substring_n2("UTCS!rocks4EVER"), 13)

    def test_length_of_longest_substring_n2_14(self):
        """O(N^2) approach with input 'hooked on coding!', answer is 8."""
        self.assertEqual(length_of_longest_substring_n2("hooked on coding!"), 8)

    def test_length_of_longest_substring_n2_15(self):
        """O(N^2) approach with input 'longsubstring', answer is 8."""
        self.assertEqual(length_of_longest_substring_n2("longsubstring"), 8)

    def test_length_of_longest_substring_n2_16(self):
        """O(N^2) approach with input 'abcd1234abcd', answer is 8."""
        self.assertEqual(length_of_longest_substring_n2("abcd1234abcd"), 8)

    def test_length_of_longest_substring_n2_17(self):
        """O(N^2) approach with input 'abcdefghijklmnopqrstuvwxyz', answer is 26."""
        self.assertEqual(
            length_of_longest_substring_n2("abcdefghijklmnopqrstuvwxyz"), 26
        )

    def test_length_of_longest_substring_n2_18(self):
        """O(N^2) approach with input '1!2@3#4$5%6^7&8*9(0)', answer is 20."""
        self.assertEqual(length_of_longest_substring_n2("1!2@3#4$5%6^7&8*9(0)"), 20)

    def test_length_of_longest_substring_n2_19(self):
        """O(N^2) approach with input 'thequickbrownfoxjumpsover', answer is 14."""
        self.assertEqual(
            length_of_longest_substring_n2("thequickbrownfoxjumpsover"), 14
        )

    def test_length_of_longest_substring_n2_20(self):
        """O(N^2) approach with input '   ', answer is 1."""
        self.assertEqual(length_of_longest_substring_n2("   "), 1)


class TestLongestSubstringN(unittest.TestCase):
    """Test O(N) implementation."""

    def test_length_of_longest_substring_n_1(self):
        """O(N) approach input 'bevo', answer is 4."""
        self.assertEqual(length_of_longest_substring_n("bevo"), 4)

    def test_length_of_longest_substring_n_2(self):
        """O(N) approach empty string input, answer is 0."""
        self.assertEqual(length_of_longest_substring_n(""), 0)

    def test_length_of_longest_substring_n_3(self):
        """O(N) approach input 'Longhorns', answer is 6."""
        self.assertEqual(length_of_longest_substring_n("Longhorns"), 6)

    def test_length_of_longest_substring_n_4(self):
        """O(N) approach input 'abcdefghijk', answer is 11."""
        self.assertEqual(length_of_longest_substring_n("abcdefghijk"), 11)

    def test_length_of_longest_substring_n_5(self):
        """O(N) approach input 'cs313e', answer is 4."""
        self.assertEqual(length_of_longest_substring_n("cs313e"), 4)

    def test_length_of_longest_substring_n_6(self):
        """O(N) approach input 'bevoBits', answer is 8."""
        self.assertEqual(length_of_longest_substring_n("bevoBits"), 8)

    def test_length_of_longest_substring_n_7(self):
        """O(N) approach input 'UTTower', answer is 5."""
        self.assertEqual(length_of_longest_substring_n("UTTower"), 5)

    def test_length_of_longest_substring_n_8(self):
        """O(N) approach input 'CompSci', answer is 7."""
        self.assertEqual(length_of_longest_substring_n("CompSci"), 7)

    def test_length_of_longest_substring_n_9(self):
        """O(N) approach input 'abcda', answer is 4."""
        self.assertEqual(length_of_longest_substring_n("abcda"), 4)

    def test_length_of_longest_substring_n_10(self):
        """O(N) approach input 'anviaj', answer is 5."""
        self.assertEqual(length_of_longest_substring_n("anviaj"), 5)

    def test_length_of_longest_substring_n_11(self):
        """O(N) approach input 'tmmzuxt', answer is 5."""
        self.assertEqual(length_of_longest_substring_n("tmmzuxt"), 5)

    def test_length_of_longest_substring_n_12(self):
        """O(N) approach input 'qrstuqr', answer is 5."""
        self.assertEqual(length_of_longest_substring_n("qrstuqr"), 5)

    def test_length_of_longest_substring_n_13(self):
        """O(N) approach input 'UTCS!rocks4EVER', answer is 13."""
        self.assertEqual(length_of_longest_substring_n("UTCS!rocks4EVER"), 13)

    def test_length_of_longest_substring_n_14(self):
        """O(N) approach input 'hooked on coding!', answer is 8."""
        self.assertEqual(length_of_longest_substring_n("hooked on coding!"), 8)

    def test_length_of_longest_substring_n_15(self):
        """O(N) approach input 'longsubstring', answer is 8."""
        self.assertEqual(length_of_longest_substring_n("longsubstring"), 8)

    def test_length_of_longest_substring_n_16(self):
        """O(N) approach input 'abcd1234abcd', answer is 8."""
        self.assertEqual(length_of_longest_substring_n("abcd1234abcd"), 8)

    def test_length_of_longest_substring_n_17(self):
        """O(N) approach input 'abcdefghijklmnopqrstuvwxyz', answer is 26."""
        self.assertEqual(
            length_of_longest_substring_n("abcdefghijklmnopqrstuvwxyz"), 26
        )

    def test_length_of_longest_substring_n_18(self):
        """O(N) approach input '1!2@3#4$5%6^7&8*9(0)', answer is 20."""
        self.assertEqual(length_of_longest_substring_n("1!2@3#4$5%6^7&8*9(0)"), 20)

    def test_length_of_longest_substring_n_19(self):
        """O(N) approach input 'thequickbrownfoxjumpsover', answer is 14."""
        self.assertEqual(length_of_longest_substring_n("thequickbrownfoxjumpsover"), 14)

    def test_length_of_longest_substring_n_20(self):
        """O(N) approach input '   ', answer is 1."""
        self.assertEqual(length_of_longest_substring_n("   "), 1)

    def test_length_of_longest_substring_n_21(self):
        """O(N) approach input 'abc abc abc ', answer is 4."""
        self.assertEqual(length_of_longest_substring_n("abc abc abc "), 4)

    def test_length_of_longest_substring_n_22(self):
        """O(N) approach input 'aaaaaaaaaaaaaaaaaaaaaa', answer is 1."""
        self.assertEqual(length_of_longest_substring_n("aaaaaaaaaaaaaaaaaaaaaa"), 1)

    def test_length_of_longest_substring_n_23(self):
        """O(N) approach input '   checking...   ', answer is 8."""
        self.assertEqual(length_of_longest_substring_n("   checking...   "), 8)

    def test_length_of_longest_substring_n_24(self):
        """O(N) approach input 'aaabcdefghabcdefghijklmno', answer is 15."""
        self.assertEqual(length_of_longest_substring_n("aaabcdefghabcdefghijklmno"), 15)

    def test_length_of_longest_substring_n_25(self):
        """O(N) approach input 'aabbccddeeffgghh', answer is 2."""
        self.assertEqual(length_of_longest_substring_n("aabbccddeeffgghh"), 2)

    def test_length_of_longest_substring_n_26(self):
        """O(N) approach input 'hellohibye_123456' repeated 30 times, answer is 14."""
        self.assertEqual(length_of_longest_substring_n("hellohibye_123456" * 30), 14)

    def test_length_of_longest_substring_n_27(self):
        """O(N) approach input '123456789101112131415161718192021222324252627282930' repeated 6 times, answer is 10."""
        self.assertEqual(
            length_of_longest_substring_n(
                "123456789101112131415161718192021222324252627282930" * 6
            ),
            10,
        )

    def test_length_of_longest_substring_n_28(self):
        """O(N) approach input 'AbCdEfGhIjKlMnOpQrStUvWxYz_aBcDeFgHiJkLmNoPqRsTuVwXyZ_123456789' repeated 8 times, answer is 62."""
        self.assertEqual(
            length_of_longest_substring_n(
                "AbCdEfGhIjKlMnOpQrStUvWxYz_aBcDeFgHiJkLmNoPqRsTuVwXyZ_123456789" * 8
            ),
            62,
        )

    def test_length_of_longest_substring_n_29(self):
        """O(N) approach input '123456789101112131415161718192021222324252627282930' repeated 10 times, answer is 10."""
        self.assertEqual(
            length_of_longest_substring_n(
                "123456789101112131415161718192021222324252627282930" * 10
            ),
            10,
        )

    def test_length_of_longest_substring_n_30(self):
        """O(N) approach input 'abcdefghijklmnoPQRSTUVWXYZabcdefgHIJKLMNOPQRSTuvwxYz0123456789!@#$%^&*()' repeated 5 times, answer is 54."""
        self.assertEqual(
            length_of_longest_substring_n(
                "abcdefghijklmnoPQRSTUVWXYZabcdefgHIJKLMNOPQRSTuvwxYz0123456789!@#$%^&*()"
                * 5
            ),
            54,
        )


def main():
    """Main function to run tests based on command-line arguments."""
    test_cases = {
        "n3": TestLongestSubstringN3,
        "n2": TestLongestSubstringN2,
        "n": TestLongestSubstringN,
    }

    usage_string = (
        "Usage: python test_wordle.py [test_type] [test_number]\n"
        "Examples:\n"
        "    python test_bigo.py n3 1\n"
        "    python test_bigo.py n2 4\n"
        "Valid options for [test_type]: " + ", ".join(test_cases.keys()) + "\n"
        "Test cases range from 1-10 for n3, 1-20 for n2, 1-30 for n3."
    )

    if len(sys.argv) > 3:
        print(usage_string)
        return
    if len(sys.argv) == 1:
        unittest.main()
        return
    sys.argv = sys.argv[1:]
    test_name = sys.argv[0]
    if test_name not in test_cases:
        print(
            f"Invalid test name: {test_name}. Valid options are: {', '.join(test_cases.keys())}"
        )
        return
    if len(sys.argv) == 1:
        # Extract test case based on the first command-line argument
        suite = unittest.TestLoader().loadTestsFromTestCase(test_cases[test_name])
    else:
        test_num = sys.argv[1]
        loader = unittest.TestLoader()

        # Load all tests from the test case class
        all_tests = loader.loadTestsFromTestCase(test_cases[test_name])
        suite = unittest.TestSuite()
        for test in all_tests:
            if test.id().split(".")[-1].split("_")[-1] == test_num:
                suite.addTest(test)
        if not suite.countTestCases():
            print(usage_string)
            return
    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    main()
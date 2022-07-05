from unittest import TestCase

from division_detect import division_detect

class TestDivisionDetect(TestCase):
    def test_it_returns_true_if_division_by_number_is_successful(self):
        result = division_detect(
            numerator=10, denominator=2
        )
        self.assertTrue(result)
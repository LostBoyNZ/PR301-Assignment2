import unittest

from data_processor import DataProcessor as dp
from validators.validate_bmi import ValidateBmi as bm
from validators.validate_gender import ValidateGender as va


class MainTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        pass

    def tearDown(self):
        # be executed after each test case
        pass

    # MALE GENDER   V V V V V V V

    def test_gender_male(self):
        i = va.is_valid('male')
        self.assertTrue(i == ('M', True), "the value of test should be M")

    def test_gender_m(self):
        i = va.is_valid('m')
        self.assertTrue(i == ('M', True), "the value of test should be M")

    def test_gender_boy(self):
        i = va.is_valid('boy')
        self.assertTrue(i == ('M', True), "the value of test should be M")

    def test_gender_dude(self):
        i = va.is_valid('dude')
        self.assertTrue(i == ('M', True), "the value of test should be M")

    # FEMALE GENDER      V V V V V

    def test_gender_female(self):
        i = va.is_valid('female')
        self.assertTrue(i == ('F', True), "the value of test should be F")

    def test_gender_f(self):
        i = va.is_valid('f')
        self.assertTrue(i == ('F', True), "the value of test should be F")

    def test_gender_lady(self):
        i = va.is_valid('lady')
        self.assertTrue(i == ('F', True), "the value of test should be F")

    def test_gender_girl(self):
        i = va.is_valid('girl')
        self.assertTrue(i == ('F', True), "the value of test should be F")

    #  Gender with special characters (spaces, numbers and symbols) V V V V V

    def test_gender_male_with_special_characters(self):
        i = va.is_valid(' 23123 #$@#$ ma $#@$ le 9876@# ')
        self.assertTrue(i == ('M', True), "the value of test should be M")

    def test_gender_female_with_special_characters(self):
        i = va.is_valid(' $@#$ fe #$# ma @#@$ 454 le 3435')
        self.assertTrue(i == ('F', True), "the value of test should be F")

    # BMI TEST CASES

    def test_bmi_obesity(self):
        i = bm.is_valid('obesity')
        self.assertTrue(i == ("Obesity", True),
                        "the value of test should be Obesity")

    def test_bmi_normal(self):
        i = bm.is_valid('normal')
        self.assertTrue(i == ("Normal", True),
                        "the value of test should be Normal")

    def test_bmi_overweight(self):
        i = bm.is_valid('over weight ')
        self.assertTrue(i == ("Overweight", True),
                        "the value of test should be Overweight")

    def test_bmi_underweight(self):
        i = bm.is_valid('underweight')
        self.assertTrue(i == ("Underweight", True),
                        "the value of test should be underweight")

    def test_bmi_obese_converts_to_obesity(self):
        i = bm.is_valid('obese')
        self.assertTrue(i == ("Obesity", True),
                        "the value of test should be Obesity")

    # BMI WITH SPECIAL CHARACTERS

    def test_bmi_with_special_characters(self):
        i = bm.is_valid('4234un    derwei#$#$ght     ')
        self.assertTrue(i == ("Underweight", True),
                        "the value of test should be underweight")

    # Data Processor Key Value (EMPID) Tests

    def test_emp_id_valid(self):
        i = dp.validate_key('a001')
        self.assertTrue(i == 'A001', "the value of test should be A001")

    def test_emp_id_valid_with_three_letters(self):
        i = dp.validate_key('abc8')
        self.assertTrue(i == 'Abc8', "the value of test should be Abc8")

    def test_emp_id_Invalid_with_two_characters(self):
        i = dp.validate_key('a1')
        self.assertTrue(i == 'A1', "the value of test should be A1")


if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()

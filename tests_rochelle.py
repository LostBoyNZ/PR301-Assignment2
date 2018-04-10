import unittest

import validators.validate_age as va
import validators.validate_salary as sala
import validators.validate_sales as sale


class Tests_Rochelle(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        pass

    def tearDown(self):
        # be executed after each test case
        pass

    # VALIDATE AGES

    # Rochelle
    def test_perfect_age(self):
        # Setup
        test_name = "Age Validator Test #01"
        data_to_test = '45'
        class_to_test = va.ValidateAge()
        expected_result = ['45', True]

        # Action
        result = class_to_test.is_valid(data_to_test)

        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_lower_int(self):
        test_name = "Age Validator Test #02"
        data_to_test = 0
        class_to_test = va.ValidateAge()
        expected_result = ['00', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_lower_string(self):
        test_name = "Age Validator Test #03"
        data_to_test = '0'
        class_to_test = va.ValidateAge()
        expected_result = ['00', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_negative_int(self):
        test_name = "Age Validator Test #04"
        data_to_test = -5
        class_to_test = va.ValidateAge()
        expected_result = ['-5', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_negative_string(self):
        test_name = "Age Validator Test #05"
        data_to_test = '-5'
        class_to_test = va.ValidateAge()
        expected_result = ['05', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_upper_int(self):
        test_name = "Age Validator Test #06"
        data_to_test = 100
        class_to_test = va.ValidateAge()
        expected_result = ['100', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_upper_string(self):
        test_name = "Age Validator Test #07"
        data_to_test = '100'
        class_to_test = va.ValidateAge()
        expected_result = ['100', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_upper_boundary_int(self):
        test_name = "Age Validator Test #08"
        data_to_test = 99
        class_to_test = va.ValidateAge()
        expected_result = ['99', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_upper_boundary_string(self):
        test_name = "Age Validator Test #09"
        data_to_test = '99'
        class_to_test = va.ValidateAge()
        expected_result = ['99', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_lower_boundary_int(self):
        test_name = "Age Validator Test #10"
        data_to_test = 1
        class_to_test = va.ValidateAge()
        expected_result = ['01', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_lower_boundary_string(self):
        test_name = "Age Validator Test #11"
        data_to_test = '1'
        class_to_test = va.ValidateAge()
        expected_result = ['01', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_special_characters(self):
        test_name = "Age Validator Test #12"
        data_to_test = '@$ * -  9  ^&dbnd  '
        class_to_test = va.ValidateAge()
        expected_result = ['09', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_word(self):
        test_name = "Age Validator Test #13"
        data_to_test = '  twenty-nine  '
        class_to_test = va.ValidateAge()
        expected_result = ['  twenty-nine  ', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_age_special_characters_2(self):
        test_name = "Age Validator Test #14"
        data_to_test = '    !@#$%^&*()_+= 7  ][.,<a  jhewou  wetnkdbfniusg bnd2  '
        class_to_test = va.ValidateAge()
        expected_result = ['72', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    # VALIDATE SALES

    # Rochelle
    def test_perfect_sales(self):
        # Setup
        test_name = "Sales Validator Test #01"
        data_to_test = '45'
        class_to_test = sale.ValidateSales()
        expected_result = ['045', True]

        # Action
        result = class_to_test.is_valid(data_to_test)

        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_lower_int(self):
        test_name = "Sales Validator Test #02"
        data_to_test = -1
        class_to_test = sale.ValidateSales()
        expected_result = ['0-1', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_lower_string(self):
        test_name = "Sales Validator Test #03"
        data_to_test = '-1'
        class_to_test = sale.ValidateSales()
        expected_result = ['001', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_negative_int(self):
        test_name = "Sales Validator Test #04"
        data_to_test = -500
        class_to_test = sale.ValidateSales()
        expected_result = ['-500', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_negative_string(self):
        test_name = "Sales Validator Test #05"
        data_to_test = '-500'
        class_to_test = sale.ValidateSales()
        expected_result = ['500', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_Sales_upper_int(self):
        test_name = "Sales Validator Test #06"
        data_to_test = 1000
        class_to_test = sale.ValidateSales()
        expected_result = ['1000', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_upper_string(self):
        test_name = "Sales Validator Test #07"
        data_to_test = '1000'
        class_to_test = sale.ValidateSales()
        expected_result = ['1000', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_upper_boundary_int(self):
        test_name = "Sales Validator Test #08"
        data_to_test = 999
        class_to_test = sale.ValidateSales()
        expected_result = ['999', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_upper_boundary_string(self):
        test_name = "Sales Validator Test #09"
        data_to_test = '999'
        class_to_test = sale.ValidateSales()
        expected_result = ['999', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_lower_boundary_int(self):
        test_name = "Sales Validator Test #10"
        data_to_test = 0
        class_to_test = sale.ValidateSales()
        expected_result = ['000', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_lower_boundary_string(self):
        test_name = "Sales Validator Test #11"
        data_to_test = '0'
        class_to_test = sale.ValidateSales()
        expected_result = ['000', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_special_characters(self):
        test_name = "Sales Validator Test #12"
        data_to_test = '@fsj$ * -  967  ^&dbnd  '
        class_to_test = sale.ValidateSales()
        expected_result = ['967', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_word(self):
        test_name = "Sales Validator Test #13"
        data_to_test = '  two-hundred and twenty-nine  '
        class_to_test = sale.ValidateSales()
        expected_result = ['  two-hundred and twenty-nine  ', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_sales_special_characters_2(self):
        test_name = "Sales Validator Test #14"
        data_to_test = '    !@#$%^&*()_+= 7  ][.,<a  jhewou  wetnkdbfniusg bnd2  '
        class_to_test = sale.ValidateSales()
        expected_result = ['072', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    # VALIDATE SALARY

    # Rochelle
    def test_perfect_salary(self):
        # Setup
        test_name = "Salary Validator Test #01"
        data_to_test = '45'
        class_to_test = sala.ValidateSalary()
        expected_result = ['45', True]

        # Action
        result = class_to_test.is_valid(data_to_test)

        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_lower_int(self):
        test_name = "Salary Validator Test #02"
        data_to_test = -1
        class_to_test = sala.ValidateSalary()
        expected_result = ['-1', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_lower_string(self):
        test_name = "Salary Validator Test #03"
        data_to_test = '-1'
        class_to_test = sala.ValidateSalary()
        expected_result = ['01', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_negative_int(self):
        test_name = "Salary Validator Test #04"
        data_to_test = -500
        class_to_test = sala.ValidateSalary()
        expected_result = ['-500', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_negative_string(self):
        test_name = "Salary Validator Test #05"
        data_to_test = '-500'
        class_to_test = sala.ValidateSalary()
        expected_result = ['500', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_upper_int(self):
        test_name = "Salary Validator Test #06"
        data_to_test = 1000
        class_to_test = sala.ValidateSalary()
        expected_result = ['1000', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_upper_string(self):
        test_name = "Salary Validator Test #07"
        data_to_test = '1000'
        class_to_test = sala.ValidateSalary()
        expected_result = ['1000', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_upper_boundary_int(self):
        test_name = "Salary Validator Test #08"
        data_to_test = 999
        class_to_test = sala.ValidateSalary()
        expected_result = ['999', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_upper_boundary_string(self):
        test_name = "Salary Validator Test #09"
        data_to_test = '999'
        class_to_test = sala.ValidateSalary()
        expected_result = ['999', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_lower_boundary_int(self):
        test_name = "Salary Validator Test #10"
        data_to_test = 1
        class_to_test = sala.ValidateSalary()
        expected_result = ['01', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_lower_boundary_string(self):
        test_name = "Salary Validator Test #11"
        data_to_test = '1'
        class_to_test = sala.ValidateSalary()
        expected_result = ['01', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_special_characters(self):
        test_name = "Salary Validator Test #12"
        data_to_test = '@sdf$ * -  6  ^&db$%^&*nd 8 '
        class_to_test = sala.ValidateSalary()
        expected_result = ['68', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_word(self):
        test_name = "Salary Validator Test #13"
        data_to_test = '  sixty-nine  '
        class_to_test = sala.ValidateSalary()
        expected_result = ['  sixty-nine  ', False]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))

    def test_salary_special_characters_2(self):
        test_name = "Salary Validator Test #14"
        data_to_test = '    !@#$%^&*()_+= 7  ][.,<a  jhewou  wetnkdbfniusg bnd2 0 '
        class_to_test = sala.ValidateSalary()
        expected_result = ['720', True]
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(result[0] == expected_result[0] and result[1] ==
                            expected_result[1])
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(test_name,
                                                                 expected_result,
                                                                 result))
        else:
            print("{} Passed".format(test_name))


if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()

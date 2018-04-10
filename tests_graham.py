import sys
import unittest

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()

try:
    import validators.validate_date as vdt
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "help"))
    sys.exit()

try:
    import validators.validate_emp_id as vid
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "validate_emp_id"))
    sys.exit()


class TestsGraham(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        pass

    def tearDown(self):
        # be executed after each test case
        pass

    # Graham
    def run_test(self, expected_result, test_name,
                 class_to_test, data_to_test):

        if expected_result is None or test_name is None:
            print("Run test didn't receive all variables")
        elif class_to_test is None or data_to_test is None:
            print("Run test didn't receive all variables")
        else:
            # Action
            result = class_to_test.is_valid(data_to_test)

            # Assert
            try:
                self.assertTrue(result[0] == expected_result[0] and
                                result[1] == expected_result[1])
            except AssertionError:
                print("{} Failed - Should be {}, but was {}.".format
                      (test_name, expected_result, result))
            else:
                print("{} Passed".format(test_name))

    # VALID DATES

    # Graham
    def test_perfect_date_01(self):
        # Setup
        test_name = "Good Date Validator Test #1"
        data_to_test = "28/01/1998"
        class_to_test = vdt.ValidateDate()
        expected_result = ["28/01/1998", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_date_02(self):
        # Setup
        test_name = "Good Date Validator Test #2"
        data_to_test = "01-01-1998"
        class_to_test = vdt.ValidateDate()
        expected_result = ["01/01/1998", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_date_03(self):
        # Setup
        test_name = "Good Date Validator Test #3"
        data_to_test = "01.01.1998"
        class_to_test = vdt.ValidateDate()
        expected_result = ["01/01/1998", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_date_04(self):
        # Setup
        test_name = "Good Date Validator Test #4"
        data_to_test = " 01.01.1998  #"
        class_to_test = vdt.ValidateDate()
        expected_result = ["01/01/1998", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_date_05(self):
        # Setup
        test_name = "Good Date Validator Test #5"
        data_to_test = "1st Jan 2018"
        class_to_test = vdt.ValidateDate()
        expected_result = ["01/01/2018", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_date_06(self):
        # Setup
        test_name = "Good Date Validator Test #6"
        data_to_test = "22nd Jan 2018"
        class_to_test = vdt.ValidateDate()
        expected_result = ["22/01/2018", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_date_07(self):
        # Setup
        test_name = "Good Date Validator Test #7"
        data_to_test = "3rd Jan 2018"
        class_to_test = vdt.ValidateDate()
        expected_result = ["03/01/2018", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_date_08(self):
        # Setup
        test_name = "Good Date Validator Test #8"
        data_to_test = "1/1/2018"
        class_to_test = vdt.ValidateDate()
        expected_result = ["01/01/2018", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_date_09(self):
        # Setup
        test_name = "Good Date Validator Test #9"
        data_to_test = "1 January 2018"
        class_to_test = vdt.ValidateDate()
        expected_result = ["01/01/2018", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_date_10(self):
        # Setup
        test_name = "Good Date Validator Test #10"
        data_to_test = "1 January 2018"
        class_to_test = vdt.ValidateDate()
        expected_result = ["01/01/2018", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    # INVALID DATES

    def test_bad_date_01(self):
        # Setup
        test_name = "Bad Date Validator Test #1"
        data_to_test = "32/01/1998"
        class_to_test = vdt.ValidateDate()
        expected_result = ["32/01/1998", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_date_02(self):
        # Setup
        test_name = "Bad Date Validator Test #2"
        data_to_test = "01/01/98"
        class_to_test = vdt.ValidateDate()
        expected_result = ["01/01/98", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_date_03(self):
        # Setup
        test_name = "Bad Date Validator Test #3"
        data_to_test = "32/02/1998"
        class_to_test = vdt.ValidateDate()
        expected_result = ["32/02/1998", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_date_04(self):
        # Setup
        test_name = "Bad Date Validator Test #4"
        data_to_test = "12/12/12"
        class_to_test = vdt.ValidateDate()
        expected_result = ["12/12/12", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_date_05(self):
        # Setup
        test_name = "Bad Date Validator Test #5"
        data_to_test = "112/112/1998"
        class_to_test = vdt.ValidateDate()
        expected_result = ["112/112/1998", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_date_06(self):
        # Setup
        test_name = "Bad Date Validator Test #6"
        data_to_test = ""
        class_to_test = vdt.ValidateDate()
        expected_result = ["", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_date_07(self):
        # Setup
        test_name = "Bad Date Validator Test #7"
        data_to_test = "#*%(#*)#)$#($)#*$*#()*$()#*$#()*$()#" \
                       "*$()#*()*$()#*()#^#%&#@*&*@(*KJFDSJHKAHFKH#$%"
        class_to_test = vdt.ValidateDate()
        expected_result = ["#*%(#*)#)$#($)#*$*#()*$()#*$#()*"
                           "$()#*$()#*()*$()#*()#^#%&#@*&*@(*"
                           "KJFDSJHKAHFKH#$%", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_date_08(self):
        # Setup
        test_name = "Bad Date Validator Test #8"
        data_to_test = "\n"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    # VALID ID

    def test_perfect_id_01(self):
        # Setup
        test_name = "Good ID Validator Test #1"
        data_to_test = "A201"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["A201", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_id_02(self):
        # Setup
        test_name = "Good ID Validator Test #2"
        data_to_test = "A 201"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["A201", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_id_03(self):
        # Setup
        test_name = "Good ID Validator Test #3"
        data_to_test = "   A201   "
        class_to_test = vid.ValidateEmpId()
        expected_result = ["A201", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_id_04(self):
        # Setup
        test_name = "Good ID Validator Test #4"
        data_to_test = "$A201$"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["A201", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_perfect_id_05(self):
        # Setup
        test_name = "Good ID Validator Test #5"
        data_to_test = "$*#(%*)   (*()  A 2 01  $ &^*&^*&^((**\n"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["A201", True]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    # BAD ID

    def test_bad_id_01(self):
        # Setup
        test_name = "Bad ID Validator Test #1"
        data_to_test = "A2011"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["A2011", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_id_02(self):
        # Setup
        test_name = "Bad ID Validator Test #2"
        data_to_test = "A21"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["A21", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_id_03(self):
        # Setup
        test_name = "Bad ID Validator Test #3"
        data_to_test = "4201"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["4201", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_id_04(self):
        # Setup
        test_name = "Bad ID Validator Test #4"
        data_to_test = "AJKA"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["Ajka", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_id_05(self):
        # Setup
        test_name = "Bad ID Validator Test #5"
        data_to_test = "1A11"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["1A11", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_id_06(self):
        # Setup
        test_name = "Bad ID Validator Test #6"
        data_to_test = "A111, Z333"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["A111Z333", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_id_07(self):
        # Setup
        test_name = "Bad ID Validator Test #7"
        data_to_test = ""
        class_to_test = vid.ValidateEmpId()
        expected_result = ["", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_id_08(self):
        # Setup
        test_name = "Bad ID Validator Test #8"
        data_to_test = "   "
        class_to_test = vid.ValidateEmpId()
        expected_result = ["", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_id_09(self):
        # Setup
        test_name = "Bad ID Validator Test #9"
        data_to_test = "#*()*#)FSAJLKSAJLKDJSL#*$()*()@)*A@*()" \
                       "SAF*)(*)A#$JKLJALKFSJ:LKAS*$(UWQAIJASFD"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["Fsajlksajlkdjslasafajkljalkf"
                           "sjlkasuwqaijasfd", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)

    def test_bad_id_10(self):
        # Setup
        test_name = "Bad ID Validator Test #10"
        data_to_test = "\n"
        class_to_test = vid.ValidateEmpId()
        expected_result = ["", False]

        # Action & Assert
        self.run_test(expected_result, test_name, class_to_test, data_to_test)


if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()

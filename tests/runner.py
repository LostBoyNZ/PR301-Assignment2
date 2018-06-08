import unittest
import tests.test_file_controller
import tests.test_file_reader
import tests.test_file_writer
import tests.test_database_excel
import tests.test_charts

loader = unittest.TestLoader()
all_my_tests = unittest.TestSuite()

all_my_tests.addTests(loader.loadTestsFromModule(tests.test_file_reader))
all_my_tests.addTests(loader.loadTestsFromModule(tests.test_file_controller))
all_my_tests.addTests(loader.loadTestsFromModule(tests.test_file_writer))
all_my_tests.addTests(loader.loadTestsFromModule(tests.test_database_excel))
all_my_tests.addTests(loader.loadTestsFromModule(tests.test_charts))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(all_my_tests)

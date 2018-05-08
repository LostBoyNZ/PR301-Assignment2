import unittest
from charts.chart_line import ChartLine
from charts.calc_chart_data import CalcData
import filecmp


class TestCharts(unittest.TestCase):

    def test_line_chart_age_and_salary_gets_correct_data(self):
        # Arrange
        file_name = 'testdata\\test_output.txt'
        chart_type = "line"
        expected_age_list = (
                            20, 20, 21, 21, 21, 21, 21, 21, 45, 45, 45, 45,
                            46, 46, 46)
        expected_salary_list = (
                                12, 12, 12, 12, 12, 12, 12, 12, 75, 725, 725,
                                725, 725, 725, 725)
        expected_title = 'Salary Vs Age'
        expected_y_label = "Salary"
        expected_x_label = "Age of Staff"
        expected_grid = True
        expected_results = {expected_age_list, expected_salary_list,
                            expected_title, expected_y_label,
                            expected_x_label, expected_grid}

        file_contents = []
        with open(file_name, "r") as file:
            for line in file:
                a_line = line.rstrip()
                file_contents.append(a_line)
        file.close()

        calc_data = CalcData()
        calc_data.calculate(file_contents, chart_type)

        # Act
        calc_data.line_chart()

        # Assert
        actual_age_list = ChartLine.get_age_list(ChartLine)
        actual_salary_list = ChartLine.get_salary_list(ChartLine)
        actual_title = ChartLine.get_title(ChartLine)
        actual_y_label = ChartLine.get_y_label(ChartLine)
        actual_x_label = ChartLine.get_x_label(ChartLine)
        actual_grid = ChartLine.get_grid(ChartLine)

        actual_results = {actual_age_list, actual_salary_list, actual_title,
                          actual_y_label, actual_x_label, actual_grid}

        self.assertTrue(actual_results == expected_results)

    def test_bmi_bar_chart_with_bad_data_does_not_match_reference_chart(self):
        # Arrange
        file_name = 'testdata\\test_output_wrong_ages.txt'
        chart_type = "bmi"
        expected_image_file = 'reference_charts\\bar_chart_bmi.png'
        actual_image_file = 'created_charts\\bar_chart.png'

        file_contents = []
        with open(file_name, "r") as file:
            for line in file:
                a_line = line.rstrip()
                file_contents.append(a_line)
        file.close()

        calc_data = CalcData()
        calc_data.calculate(file_contents, chart_type)

        # Act
        calc_data.bar_chart(chart_type)

        # Assert
        if filecmp.cmp(expected_image_file, actual_image_file, shallow=False):
            chart_images_match = True
        else:
            chart_images_match = False

        self.assertFalse(chart_images_match)

    def test_bmi_bar_chart_with_correct_data_matches_reference_chart(self):
        # Arrange
        file_name = 'testdata\\test_output.txt'
        chart_type = "bmi"
        expected_image_file = 'reference_charts\\bar_chart_bmi.png'
        actual_image_file = 'created_charts\\bar_chart.png'

        file_contents = []
        with open(file_name, "r") as file:
            for line in file:
                a_line = line.rstrip()
                file_contents.append(a_line)
        file.close()

        calc_data = CalcData()
        calc_data.calculate(file_contents, chart_type)

        # Act
        calc_data.bar_chart(chart_type)

        # Assert
        if filecmp.cmp(expected_image_file, actual_image_file, shallow=False):
            chart_images_match = True
        else:
            chart_images_match = False

        self.assertTrue(chart_images_match)

    def test_bmi_bar_chart_with_bad_data_does_not_match_reference_chart(self):
        # Arrange
        file_name = 'testdata\\test_output_bmi_all_normal_birthday_all_feb.txt'
        chart_type = "bmi"
        expected_image_file = 'reference_charts\\bar_chart_bmi.png'
        actual_image_file = 'created_charts\\bar_chart.png'

        file_contents = []
        with open(file_name, "r") as file:
            for line in file:
                a_line = line.rstrip()
                file_contents.append(a_line)
        file.close()

        calc_data = CalcData()
        calc_data.calculate(file_contents, chart_type)

        # Act
        calc_data.bar_chart(chart_type)

        # Assert
        if filecmp.cmp(expected_image_file, actual_image_file, shallow=False):
            chart_images_match = True
        else:
            chart_images_match = False

        self.assertFalse(chart_images_match)

    def test_birthday_bar_chart_with_correct_data_matches_reference_chart(
            self):
        # Arrange
        file_name = 'testdata\\test_output.txt'
        chart_type = "birthday"
        expected_image_file = 'reference_charts\\bar_chart_birthday.png'
        actual_image_file = 'created_charts\\bar_chart.png'

        file_contents = []
        with open(file_name, "r") as file:
            for line in file:
                a_line = line.rstrip()
                file_contents.append(a_line)
        file.close()

        calc_data = CalcData()
        calc_data.calculate(file_contents, chart_type)

        # Act
        calc_data.bar_chart(chart_type)

        # Assert
        if filecmp.cmp(expected_image_file, actual_image_file, shallow=False):
            chart_images_match = True
        else:
            chart_images_match = False

        self.assertTrue(chart_images_match)

    def test_birthday_bar_chart_with_bad_data_does_not_match_reference_chart(
            self):
        # Arrange
        file_name = 'testdata\\test_output_bmi_all_normal_birthday_all_feb.txt'
        chart_type = "birthday"
        expected_image_file = 'reference_charts\\bar_chart_birthday.png'
        actual_image_file = 'created_charts\\bar_chart.png'

        file_contents = []
        with open(file_name, "r") as file:
            for line in file:
                a_line = line.rstrip()
                file_contents.append(a_line)
        file.close()

        calc_data = CalcData()
        calc_data.calculate(file_contents, chart_type)

        # Act
        calc_data.bar_chart(chart_type)

        # Assert
        if filecmp.cmp(expected_image_file, actual_image_file,
                       shallow=False):
            chart_images_match = True
        else:
            chart_images_match = False

        self.assertFalse(chart_images_match)

    def test_gender_pie_chart_with_correct_data_matches_reference_chart(
            self):
        # Arrange
        file_name = 'testdata\\test_output.txt'
        chart_type = "gender"
        expected_image_file = 'reference_charts\\pie_chart_gender.png'
        actual_image_file = 'created_charts\\pie_chart.png'

        file_contents = []
        with open(file_name, "r") as file:
            for line in file:
                a_line = line.rstrip()
                file_contents.append(a_line)
        file.close()

        calc_data = CalcData()
        calc_data.calculate(file_contents, chart_type)

        # Act
        calc_data.pie_chart(chart_type)

        # Assert
        if filecmp.cmp(expected_image_file, actual_image_file, shallow=False):
            chart_images_match = True
        else:
            chart_images_match = False

        self.assertTrue(chart_images_match)

    def test_gender_pie_chart_with_bad_data_does_not_match_reference_chart(
            self):
        # Arrange
        file_name = 'testdata\\test_output_all_male_all_500_sales.txt'
        chart_type = "gender"
        expected_image_file = 'reference_charts\\pie_chart_gender.png'
        actual_image_file = 'created_charts\\pie_chart.png'

        file_contents = []
        with open(file_name, "r") as file:
            for line in file:
                a_line = line.rstrip()
                file_contents.append(a_line)
        file.close()

        calc_data = CalcData()
        calc_data.calculate(file_contents, chart_type)

        # Act
        calc_data.pie_chart(chart_type)

        # Assert
        if filecmp.cmp(expected_image_file, actual_image_file, shallow=False):
            chart_images_match = True
        else:
            chart_images_match = False

        self.assertFalse(chart_images_match)

    def test_sales_pie_chart_with_correct_data_matches_reference_chart(
            self):
        # Arrange
        file_name = 'testdata\\test_output.txt'
        chart_type = "sales"
        expected_image_file = 'reference_charts\\pie_chart_sales.png'
        actual_image_file = 'created_charts\\pie_chart.png'

        file_contents = []
        with open(file_name, "r") as file:
            for line in file:
                a_line = line.rstrip()
                file_contents.append(a_line)
        file.close()

        calc_data = CalcData()
        calc_data.calculate(file_contents, chart_type)

        # Act
        calc_data.pie_chart(chart_type)

        # Assert
        if filecmp.cmp(expected_image_file, actual_image_file, shallow=False):
            chart_images_match = True
        else:
            chart_images_match = False

        self.assertTrue(chart_images_match)

    def test_gender_pie_chart_with_bad_data_does_not_match_reference_chart(
            self):
        # Arrange
        file_name = 'testdata\\test_output_all_male_all_500_sales.txt'
        chart_type = "sales"
        expected_image_file = 'reference_charts\\pie_chart_sales.png'
        actual_image_file = 'created_charts\\pie_chart.png'

        file_contents = []
        with open(file_name, "r") as file:
            for line in file:
                a_line = line.rstrip()
                file_contents.append(a_line)
        file.close()

        calc_data = CalcData()
        calc_data.calculate(file_contents, chart_type)

        # Act
        calc_data.pie_chart(chart_type)

        # Assert
        if filecmp.cmp(expected_image_file, actual_image_file, shallow=False):
            chart_images_match = True
        else:
            chart_images_match = False

        self.assertFalse(chart_images_match)

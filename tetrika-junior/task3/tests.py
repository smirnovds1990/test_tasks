import unittest

from solution import (
    count_total_time_on_lesson,
    get_intervals_from_data,
    reduce_intersected_intervals
)


class TestAppearanceTimeCounting(unittest.TestCase):

    def test_get_intervals_with_correct_data(self):
        test_data = {
            "lesson": [1594663200, 1594666800],
            "pupil": [1594663340, 1594663389, 1594663390, 1594663395],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        }
        expected_pupil_result = [
            (1594663340, 1594663389), (1594663390, 1594663395)
        ]
        expected_tutor_results = [
            (1594663290, 1594663430), (1594663443, 1594666473)
        ]
        self.assertEqual(
            get_intervals_from_data(test_data, "pupil"),
            expected_pupil_result
        )
        self.assertEqual(
            get_intervals_from_data(test_data, "tutor"),
            expected_tutor_results
        )

    def test_get_intervals_with_empty_dict(self):
        test_data = dict()
        with self.assertRaises(KeyError):
            get_intervals_from_data(test_data, "pupil")

    def test_get_intervals_with_empty_intervals(self):
        test_data = {
            "lesson": [1594663200, 1594666800],
            "pupil": [],
            "tutor": [],
        }
        expected_result = []
        self.assertEqual(
            get_intervals_from_data(test_data, "pupil"),
            expected_result
        )

    def test_reduce_intervals_with_intersected_intervals(self):
        test_data = [
            (1594702789, 1594704500),
            (1594702807, 1594704542),
            (1594704512, 1594704513),
        ]
        expected_result = [[1594702789, 1594704542],]
        self.assertEqual(
            reduce_intersected_intervals(test_data), expected_result
        )

    def test_reduce_intervals_with_not_intersected_intervals(self):
        test_data = [
            (1594663340, 1594663389),
            (1594663390, 1594663395),
            (1594663396, 1594666472),
        ]
        expected_result = [
            [1594663340, 1594663389],
            [1594663390, 1594663395],
            [1594663396, 1594666472],
        ]
        self.assertEqual(
            reduce_intersected_intervals(test_data), expected_result
        )

    def test_count_total_time_with_fully_intersected_periods(self):
        test_intervals = [
            [1594663340, 1594663389], [1594663396, 1594666472]
        ]
        lesson_start = 1594663339
        lesson_end = 1594666473
        expected_results = 3125
        self.assertEqual(
            count_total_time_on_lesson(
                pupil_intervals=test_intervals,
                tutor_intervals=test_intervals,
                lesson_start=lesson_start,
                lesson_end=lesson_end,
            ),
            expected_results
        )

    def test_count_total_time_with_partially_intersected_periods(self):
        test_pupil_intervals = [
            [1594663340, 1594663380], [1594663400, 1594666400]
        ]
        test_tutor_intervals = [
            [1594663350, 1594663389], [1594663396, 1594666472]
        ]
        lesson_start = 1594663339
        lesson_end = 1594666473
        expected_results = 3030
        self.assertEqual(
            count_total_time_on_lesson(
                pupil_intervals=test_pupil_intervals,
                tutor_intervals=test_tutor_intervals,
                lesson_start=lesson_start,
                lesson_end=lesson_end,
            ),
            expected_results
        )

    def test_count_total_time_with_not_intersected_periods(self):
        test_pupil_intervals = [
            [1594663340, 1594663350], [1594663400, 1594665400]
        ]
        test_tutor_intervals = [
            [1594663351, 1594663389], [1594665401, 1594666472]
        ]
        lesson_start = 1594663339
        lesson_end = 1594666473
        expected_results = 0
        self.assertEqual(
            count_total_time_on_lesson(
                pupil_intervals=test_pupil_intervals,
                tutor_intervals=test_tutor_intervals,
                lesson_start=lesson_start,
                lesson_end=lesson_end,
            ),
            expected_results
        )


if __name__ == "__main__":
    unittest.main()

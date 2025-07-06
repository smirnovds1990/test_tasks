def get_intervals_from_data(
    intervals: dict[str, list[int]], key: str
) -> list[tuple]:
    """Form (start, end) intervals from input data with timestamps."""
    times_list = intervals[key]
    formed_intervals = list(zip(times_list[::2], times_list[1::2]))
    return formed_intervals


def reduce_intersected_intervals(intervals: list[tuple]) -> list[list]:
    """Check if intervals are intersected to not count the same time twice."""
    reduced_intervals = []
    for start, end in intervals:
        if (
            not reduced_intervals
            or reduced_intervals[-1][1] < start
        ):
            reduced_intervals.append([start, end])
        else:
            reduced_intervals[-1][1] = (
                max(reduced_intervals[-1][1], end)
            )
    return reduced_intervals


def count_total_time_on_lesson(
    pupil_intervals: list[list],
    tutor_intervals: list[list],
    lesson_start: int,
    lesson_end: int,
) -> int:
    """Sum pupil and tutor times up."""
    total_time_together = 0
    for i in pupil_intervals:
        for j in tutor_intervals:
            start = max(i[0], j[0], lesson_start)
            end = min(i[1], j[1], lesson_end)
            if end > start:
                total_time_together += end - start
            continue
    return total_time_together


def appearance(intervals: dict[str, list[int]]) -> int:
    """The main function to prepare data and count the total time."""
    pupil_intervals = get_intervals_from_data(intervals=intervals, key="pupil")
    tutor_intervals = get_intervals_from_data(intervals=intervals, key="tutor")
    pupil_reduced_intervals = reduce_intersected_intervals(
        intervals=pupil_intervals
    )
    tutor_reduced_intervals = reduce_intersected_intervals(
        intervals=tutor_intervals
    )
    return count_total_time_on_lesson(
        pupil_intervals=pupil_reduced_intervals,
        tutor_intervals=tutor_reduced_intervals,
        lesson_start=intervals["lesson"][0],
        lesson_end=intervals["lesson"][1],
    )


tests = [
    {"intervals": {
        "lesson": [1594663200, 1594666800],
        "pupil": [
            1594663340, 1594663389,
            1594663390, 1594663395,
            1594663396, 1594666472,
        ],
        "tutor": [1594663290, 1594663430, 1594663443, 1594666473]
    },
        "answer": 3117,
    },
    {"intervals": {
        "lesson": [1594702800, 1594706400],
        "pupil": [
            1594702789, 1594704500,
            1594702807, 1594704542,
            1594704512, 1594704513,
            1594704564, 1594705150,
            1594704581, 1594704582,
            1594704734, 1594705009,
            1594705095, 1594705096,
            1594705106, 1594706480,
            1594705158, 1594705773,
            1594705849, 1594706480,
            1594706500, 1594706875,
            1594706502, 1594706503,
            1594706524, 1594706524,
            1594706579, 1594706641,
        ],
        "tutor": [
            1594700035, 1594700364,
            1594702749, 1594705148,
            1594705149, 1594706463
        ]
    },
        "answer": 3577
    },
    {"intervals": {
        "lesson": [1594692000, 1594695600],
        "pupil": [1594692033, 1594696347],
        "tutor": [1594692017, 1594692066, 1594692068, 1594696341]
    },
        "answer": 3565
    },
]


if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer = appearance(test["intervals"])
        assert test_answer == test["answer"], (
            f"Error on test case {i}, "
            f"got {test_answer}, expected {test["answer"]}"
        )

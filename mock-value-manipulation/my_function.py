def process_numbers(values: list[int]) -> list[int]:
    return [value * 10 for value in values]


def function_under_test(some_data: dict[int, list[int]]) -> list[int]:
    accumulation = []
    for val in some_data.values():
        values = process_numbers(values=val)
        accumulation += values

    return accumulation

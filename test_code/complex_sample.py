import math


def process_data(data):
    result = []

    for item in data:
        if item > 0:
            if item % 2 == 0:
                if item > 100:
                    result.append(item * 2)
                else:
                    result.append(item + 10)
            else:
                if item > 50:
                    result.append(item - 5)
                else:
                    result.append(item + 5)
        else:
            if item == 0:
                result.append(1)
            else:
                result.append(abs(item))

    return result


def calculate_statistics(values):
    total = 0

    for value in values:
        total += value

    average = total / len(values) if values else 0

    if average > 100:
        category = "high"
    elif average > 50:
        category = "medium"
    else:
        category = "low"

    return total, average, category


def transform_and_analyze(data):
    processed = process_data(data)

    if len(processed) > 10:
        processed = processed[:10]

    statistics = calculate_statistics(processed)

    if statistics[1] > 75:
        return statistics
    else:
        return statistics


def main():
    data = [10, 25, 60, 120, -5, 0, 75, 150, 30, 45, 80, 200]

    result = transform_and_analyze(data)

    if result:
        print("Analysis completed")

    return result


if __name__ == "__main__":
    main()
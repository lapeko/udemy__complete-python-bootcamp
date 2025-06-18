def odd_squares(limit):
    for num in range(1, limit + 1, 2):
        yield num ** 2

for num in odd_squares(21):
    print(num)


def sliding_window(sequence, window_size):
    for i in range(len(sequence) - window_size + 1):
        yield sequence[i: window_size + i]

for window in sliding_window([1, 2, 3, 4, 5], 3):
    print(window)
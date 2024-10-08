import random
import time
import matplotlib.pyplot as plt

from bigo import (
    length_of_longest_substring_n3,
    length_of_longest_substring_n2,
    length_of_longest_substring_n,
)


# Function to generate a random string of length n
def generate_random_string(n: int) -> str:
    return "".join(
        random.choices(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()_+-=",
            k=n,
        )
    )


# Lists to store input sizes and runtimes for each function
input_sizes = []
times_N3 = []
times_N2 = []
times_N = []
skip_N3 = skip_N2 = skip_N = False

# Test with increasing input sizes
for size in range(0, 10001, 200):
    if skip_N3 and skip_N2 and skip_N:
        break
    input_sizes.append(size)
    test_string = generate_random_string(size)

    if not skip_N3:
        start_time = time.time()
        length_of_longest_substring_n3(test_string)
        total_time = time.time() - start_time
        times_N3.append(total_time)
        if total_time > 2:
            skip_N3 = True

    if not skip_N2:
        start_time = time.time()
        length_of_longest_substring_n2(test_string)
        total_time = time.time() - start_time
        times_N2.append(total_time)
        if total_time > 2:
            skip_N2 = True

    if not skip_N:
        start_time = time.time()
        length_of_longest_substring_n(test_string)
        total_time = time.time() - start_time
        times_N.append(total_time)
        if total_time > 2:
            skip_N = True


# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes[: len(times_N3)], times_N3, label="O(N^3)", marker="o")
plt.plot(input_sizes[: len(times_N2)], times_N2, label="O(N^2)", marker="s")
plt.plot(input_sizes, times_N, label="O(N)", marker="^")
plt.xlabel("Input Size (Length of String)")
plt.ylabel("Time (seconds)")
plt.title("Runtime Comparison of length_of_longest_substring Functions")
plt.legend()
plt.grid(True)
plt.show()

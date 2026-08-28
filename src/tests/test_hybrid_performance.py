"""
CSAPX Lab 3: Tripods

Performance benchmarking file for the hybrid sort algorithm.

This program measures the execution time of hybrid_sort with different dataset sizes
and threshold values (k). It helps to determine the default value for the threshold parameter (k).

author: RIT CS
"""

import random
import time
from tripod import Tripod, Orientation
from hybrid_sort import hybrid_sort


def generate_random_tripods(num_tripods: int) -> list[Tripod]:
    """
    Generates a list of random Tripod objects for benchmark testing.
    :param num_tripods: Number of tripods to generate
    :return An unsorted list of tripods generated with random values.
    """
    orientations = list(Orientation)
    tripods = []
    for _ in range(num_tripods):
        r = random.randint(0, 500)
        c = random.randint(0, 500)
        orient = random.choice(orientations)
        val = random.randint(1, 1000)
        tripods.append(Tripod(r, c, orient, val))
    return tripods


def main() -> None:
    """
    Benchmarks hybrid_sort performance across varying dataset sizes and threshold (k) values.

    Generates random Tripod datasets, measures execution times over multiple
    runs for each k value, and prints a summary table.
    :return None
    """
    DATASET_SIZES = (100, 1000, 10000, 100000, 1000000)
    NUM_RUNS = 3
    K_VALUES = (10, 15, 20, 30, 50, 75, 100, 200, 500)

    print("=" * 55)
    print(f" HYBRID SORT PERFORMANCE BENCHMARK")
    print("=" * 55)

    random.seed(42)

    for size in DATASET_SIZES:
        print(f"\nDATASET SIZE (N = {size:,})")
        print(f"{'Threshold (k)':<15} | {'Avg Time (ms)':<25}")
        print("-" * 55)
        base_data = generate_random_tripods(size)

        min_time = float('inf')

        for k in K_VALUES:
            total_time = 0.0

            for _ in range(NUM_RUNS):
                # run multiple times the sorting algorithm with the same dataset and k
                # and average the running time across those runs
                data_copy = list(base_data)

                start_time = time.perf_counter()
                hybrid_sort(data_copy, k)
                end_time = time.perf_counter()

                total_time += (end_time - start_time)

            avg_time_ms = (total_time / NUM_RUNS) * 1000
            print(f"{k:<15} | {avg_time_ms:<25.2f}")

            if avg_time_ms < min_time:
                min_time = avg_time_ms
                best_k = k

        print("-" * 55)
        print(f"Fastest threshold found: k = {best_k} ({min_time:.2f} ms)")
        print("=" * 55)


if __name__ == '__main__':
    main()

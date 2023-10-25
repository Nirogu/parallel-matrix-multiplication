from os import popen

from pandas import DataFrame
from tqdm import trange


def single_experiment(matrix_size, threads):
    data = []
    stream = popen(f"./MM1c {matrix_size} {threads} 0")
    for line in stream.readlines():
        values = line.strip().split(",")
        data.append(values)
    return data


def all_experiments(matrix_sizes, threads, repetitions):
    data = []
    for matrix_size in matrix_sizes:
        for thread in threads:
            for _ in trange(
                repetitions,
                desc=f"Size: {matrix_size}, {thread} threads",
                unit="experiment",
            ):
                data.extend(single_experiment(matrix_size, thread))
    return data


if __name__ == "__main__":
    matrix_sizes = range(200, 2001, 200)
    threads = (1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
    repetitions = 30

    data = all_experiments(matrix_sizes, threads, repetitions)
    columns = ["Matrix_Size", "N_Threads", "Thread", "Time"]
    data = DataFrame(data, columns=columns)
    data.to_csv("experiments.csv", index=False)

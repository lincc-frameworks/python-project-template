"""Two sample benchmarks to compute runtime and memory usage.

For more information on writing benchmarks:
https://asv.readthedocs.io/en/stable/writing_benchmarks.html."""

import example_benchmarks


def time_computation():
    """Time computations are prefixed with 'time'."""
    example_benchmarks.runtime_computation()


def mem_list():
    """Memory computations are prefixed with 'mem' or 'peakmem'."""
    return example_benchmarks.memory_computation()

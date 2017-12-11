import os, sys
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

import timeit

BENCHMARK_ITERATIONS = 1000000
NANOS_IN_SECOND = 1000000000

def measure(name, stmt, setup, count):
  timer = timeit.Timer(stmt, setup)
  total_nanos = timer.timeit(count) * NANOS_IN_SECOND
  per_op_nanos = round(total_nanos / count, 1)
  print("%-18s%14s%20s ns/op" % (name, count, per_op_nanos))

measure("verhoeff.digit (small)", "verhoeff.digit('123')", "import verhoeff", BENCHMARK_ITERATIONS)
measure("verhoeff.digit (large)", "verhoeff.digit('00123014764700968325')", "import verhoeff", BENCHMARK_ITERATIONS)

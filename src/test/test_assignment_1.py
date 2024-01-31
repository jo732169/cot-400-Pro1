import unittest
import sys
from pathlib import Path

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir)
from main.assignment_1 import ApproximationAlgorithm, BisectionMethod, FixedPointIteration, NewtonRaphsonMethod

def test():
    print("Testing Approximation Algorithm:")
    print(ApproximationAlgorithm())

    print("\nTesting Bisection Method:")
    print(BisectionMethod())

    print("\nTesting Fixed Point Iteration")
    print(FixedPointIteration())

    print("\nTesting Newton Raphson Method")
    print(NewtonRaphsonMethod())

if __name__ == '__main__':
    test()
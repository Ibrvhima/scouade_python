from src.problems.inside_test.fibonacci_test import TestFibonacci

def test_all():
    tester = TestFibonacci()
    tester.test_base_cases()
    tester.test_small_values()
    tester.test_large_value()
    print("✅ Tous les tests Fibonacci ont réussi !")

if __name__ == "__main__":
    test_all()

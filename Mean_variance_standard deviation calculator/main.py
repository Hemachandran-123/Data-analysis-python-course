from mean_var_std import calculate
def test_calculate():
    input_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    expected_output = {
        'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
        'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
        'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
        'max': [[6, 7, 8], [2, 5, 8], 8],
        'min': [[0, 1, 2], [0, 3, 6], 0],
        'sum': [[9, 12, 15], [3, 12, 21], 36]
    }
    try:
        result = calculate(input_data)
        assert result == expected_output, f"Test Case 1 failed: {result}"
        print("Test Case 1 passed.")
    except ValueError as e:
        print(f"Test Case 1 raised an unexpected error: {e}")

    invalid_input = [1, 2, 3]
    try:
        calculate(invalid_input)
    except ValueError as e:
        assert str(e) == "List must contain nine numbers.", f"Test Case 2 failed: {e}"
        print("Test Case 2 passed.")
    else:
        print("Test Case 2 failed: No error raised for invalid input.")

if __name__ == "__main__":
    test_calculate()

from two_sum import Solution

def main():
    test_cases = [
        ([2, 7, 11, 15], 9),    # Expected: [0, 1]
        ([3, 2, 4], 6),         # Expected: [1, 2]
        ([3, 3], 6),            # Expected: [0, 1]
        ([1, 2, 3], 4),         # Expected: [0, 2]
        ([1, 2, 3], 10)         # Expected: [] (no solution)
    ]
    sol = Solution()
    print("Testing Two Sum Implementation")
    print("=" * 30)

    for number,target in test_cases:
        result_out = sol.twoSum(number, target)
        print(f"Numbers: {number}")             
        print(f"Target: {target}")
        print(f"Result: {result_out}")
        print("-" * 20)

if __name__ == "__main__":
    main()  
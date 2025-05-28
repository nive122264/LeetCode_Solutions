from ispal import Solution
def main(): 
    test_cases = [
        ("121", True),        # Expected: True
        ("-121", False),      # Expected: False
        ("10", False),        # Expected: False
        ("12321", True),      # Expected: True
    ]

    solution = Solution()
    print("Testing Palindrome Implementation")
    print("=" * 30)
    for number, expected in test_cases:
        result = solution.isPalindrome(int(number))
        print(f"Number: {number}")
        print(f"Expected: {expected}, Result: {result}")
        print("-" * 20)
    
if __name__ == "__main__":
    main()
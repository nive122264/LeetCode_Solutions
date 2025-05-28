from roman2Int import Solution
def main():
    s = {"III":3, "IV":4, "IX":9, "LVIII":58, "MCMXCIV":1994}
    solution = Solution()
    for r,n in s.items():
        result = solution.romanToInt(r)
        print(f"Roman numeral: {r}, Integer: {result}, Expected: {n}, Test {'Passed' if result == n else 'Failed'}")
        
        
if __name__ == "__main__":
    main()
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        my_Map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(len(s)):
            if i+1 < len(s) and my_Map[s[i]] < my_Map[s[i + 1]]:
                total -= my_Map[s[i]]
            else:
                total += my_Map[s[i]]

        return total

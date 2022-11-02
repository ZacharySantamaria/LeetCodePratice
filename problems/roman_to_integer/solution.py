class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        ugly_bool = False
        
        for i in range(len(s)):
            if ugly_bool == True:
                ugly_bool = False
                pass
            elif i != len(s)-1 and s[i] == "I" and s[i+1] == "V":
                count += 4
                ugly_bool = True
            elif i != len(s)-1 and s[i] == "I" and s[i+1] == "X":
                count += 9
                ugly_bool = True
            elif i != len(s)-1 and s[i] == "X" and s[i+1] == "L":
                count += 40
                ugly_bool = True
            elif i != len(s)-1 and s[i] == "X" and s[i+1] == "C":
                count += 90
                ugly_bool = True
            elif i != len(s)-1 and s[i] == "C" and s[i+1] == "D":
                count += 400
                ugly_bool = True
            elif i != len(s)-1 and s[i] == "C" and s[i+1] == "M":
                count += 900
                ugly_bool = True
            elif s[i] == "I":
                count += 1
            elif s[i] == "V":
                count += 5
            elif s[i] == "X":
                count += 10
            elif s[i] == "L":
                count += 50
            elif s[i] == "C":
                count += 100
            elif s[i] == "D":
                count += 500
            elif s[i] == "M":
                count += 1000
        return count
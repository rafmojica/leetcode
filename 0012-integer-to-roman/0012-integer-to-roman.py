class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        descendingRomans = sorted(romans, reverse=True)
        
        romanValue = ""
        currentNum = num
        for k in descendingRomans:
            subtractedNum = currentNum - k 
            while subtractedNum >= 0:
                v = romans.get(k) # get roman numeral
                romanValue += v # add corresponding value
                currentNum = subtractedNum # update currentNum
                subtractedNum -= k # subtract by k until negative
            
        return romanValue
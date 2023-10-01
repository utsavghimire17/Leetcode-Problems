class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        number1 = 0
        number2 = 0
        for i in num1:
            number1 = number1 * 10 + digits[i]
        for i in num2:
            number2 = number2 * 10 + digits[i]
        return str(number1*number2)
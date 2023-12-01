class Rational:
    def __init__(self,num=0,den=1) -> None:
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den
            
    def __str__(self) -> str:
        if self.denominator == 1 or self.denominator == 0:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

if __name__ == "__main__":
    num2 = Rational(5,1)
    print(num2)

    num3 = Rational(0,3)
    print(num3)

    num4 = Rational(4,2)
    print(num4)

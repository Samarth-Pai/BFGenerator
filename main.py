def bfGenerator(userInput: str) -> str:
    '''
    Main function that takes a string as input and outputs the corresponidng brain**k code that outputs the given input
    '''
    code = ""
    currIndex = 0
    for char in userInput:
        asciiIndex = ord(char)
        indexDifference = asciiIndex-currIndex
        if indexDifference:
            a,b,rem = pairOfProduct(abs(indexDifference))
            sign = '-+'[indexDifference>0]
            code+=f"{'+'*b}[>{sign*a}<-]>{sign*rem}"
        else:
            code = code.rstrip("<")
        code+=".<"
        currIndex = asciiIndex
    return code.rstrip("<")
            
def pairOfProduct(num: int) -> tuple[int]:
    '''
    Returns the pair of product possible for the given number with remainder
    Examples:
    9 -> (3,3,0)
    12 -> (3,4,0)
    11 -> (3,3,2)
    '''
    for i in range(numSqrt:=int(num**0.5),0,-1):
        if i==1:
            return (numSqrt,numSqrt,num-numSqrt**2)
        if num%i == 0:
            return (i,num//i,0)
         
if __name__ == "__main__":
    userInput = input("Enter the text to generate into brainf**k code: ")
    print("Code:")
    print(bfGenerator(userInput))
def main():
    inp = int(input("Enter the length of fibonacci series: "))
    if inp>1:
        compute(inp)
    else:
        print("please enter number greater than 1")
        
def compute(inp):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(inp-2):
        c = a + b
        print(c)
        a = b
        b = c

if __name__ == "__main__":
    main()
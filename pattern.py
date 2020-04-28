SPACE = 15

def main():
    for j in range(2):
        j = right_pattern(j)
        j = left_pattern(j)
        j = right_o_split(j)
        j = left_o_split(j)
        j = right_pattern(j)
        j = diamond_split(j)
        j = diamond_merge(j)

def diamond_merge(j):
    i = 0
    while j!=SPACE and i!=SPACE:
        space(i)
        i= i+1
        print("i")
        space(j)
        j = j - 1
        print("o")

    return j

def diamond_split(j):
    i = j
    while (i <= SPACE and i!=0 and j < (SPACE + SPACE)):
        i = i - 1
        space(i)
        print("i")
        space(j)
        j = j + 1
        print("o")
    return j

def left_o_split(j):
    while (j <= SPACE and j!=0):
        print("i",end='')
        space(j)
        j = j - 1
        print("o")
    return j

def right_o_split(j):
    while (j < SPACE):
        print("i",end="")
        space(j)
        j = j + 1
        print("o")
    return  j


def space(j):
    for i in range(j):
        print("  ",end="")

def right_pattern(j):
    while(j<SPACE):
        space(j)
        j=j+1
        print("io")
    return j

def left_pattern(j):
    while(j<=SPACE and j!=0):
        space(j)
        j=j-1
        print("io")
    return j


if __name__ == '__main__':
    main()

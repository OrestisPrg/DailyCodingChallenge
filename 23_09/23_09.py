#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def array_prod(a):
    b = [1] * len(a)
    for i in range(len(b)):
        for j in range(len(a)):
            if i != j:
                b[i] = b[i] * a[j]
    return b


def main():
    list = input("Enter a list: ")
    b = array_prod(list)
    print(b)

if __name__ == "__main__":
    main()

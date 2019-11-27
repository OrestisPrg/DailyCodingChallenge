#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def sum_fun(list, k):
    for num1 in list:
        for num2 in list:
            if (num1+num2 == k) and num1 is not num2:
                return num1, num2
    return "no match"


def main():
 list = input("Enter a list: ")
 k = input("Enter k: ")
 res = sum_fun(list,k)
 print(res)

if __name__ == "__main__":
    main()

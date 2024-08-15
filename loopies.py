# Printing all numbers between 1 and 100 without using any loop

def min_max(min, max):
    if min != max:
        print(min)
        min+=1
        min_max(min,max)
    else:
        print(min)


if __name__ == '__main__':
    max = 100
    min = 1
    min_max(min, max)
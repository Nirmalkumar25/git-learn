# Finding odd or even number without any conditional statemnt

def find_odd_or_even(num):
    num_mapping = {
        "0": "Even",
        "1": "Odd"
    }
    out = num % 2 
    statement = f"The given number {num} is {num_mapping[str(out)]}"
    print(statement)

if __name__ == '__main__':
    num = int(input("Enter a number: "))
    find_odd_or_even(num)
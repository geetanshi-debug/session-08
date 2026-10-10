def result(mark):
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")
    return "Pass" if mark >= 40 else "Fail"

if __name__ == "__main__":
    mark = float(input("Enter mark: "))
    print(result(mark))

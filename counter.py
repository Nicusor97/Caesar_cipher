def get_user_input():
    return input("Enter your code: ").upper()


def get_number_of_occurrences(letter, string):
    number_of_occurrences = string.count(letter)
    return number_of_occurrences


def main():
    occurrences = {}
    user_input = get_user_input()
    for letter in user_input:
        number_of_occurrences = get_number_of_occurrences(letter, user_input)
        # x/100 * len(user_input) = number_of_occurrences
        percent = (number_of_occurrences * 100)/len(user_input)
        occurrences.update({letter: [number_of_occurrences, percent]})

    for key, value in occurrences.items():
        print(("Number of the occurrences for the %s is %s and the percent is %s \n" % (key, value[0], value[1])))


if __name__ == "__main__":
    main()


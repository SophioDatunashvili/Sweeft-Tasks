# this function checks range of input of number of words
def T_in_range(T):
    return 1 <= T <= 10 ** 5


# this function checks if the word is lowercase and alphabetic and in range 1 ≤ n ≤ 100
def is_lower_and_is_alpha_and_in_range(word):
    return word.isalpha() and word.islower() and 1 <= len(word) <= 100


# this function returns the next lexicographically greater string possible from the given string
def bigger_is_greater(word):
    for i in range(len(word) - 1, 0, -1):
        if word[i] > word[i - 1]:
            for j in range(len(word) - 1, i - 1, -1):
                if word[j] > word[i - 1]:
                    word = list(word)
                    word[i - 1], word[j] = word[j], word[i - 1]
                    word[i:] = sorted(word[i:])
                    return "".join(word)

    # if no answer is possible
    return "no answer"


def main():
    # check if the input is valid
    try:
        T = int(input())
        if not T_in_range(T):
            raise ValueError
    except ValueError:
        return print("Please input positive integer in range 1 ≤ n ≤ 10^5")

    words = []
    for _ in range(T):
        word = input()

        # check if the input is valid
        if not is_lower_and_is_alpha_and_in_range(word):
            print("Wrong Input: Please enter word only in lowercase English Letter and length in range 1 ≤ n ≤ 100")
            continue

        words.append(bigger_is_greater(word))

    # print the next lexicographically greater string possible from the given string
    for word in words:
        print(word)


if __name__ == '__main__':
    main()

# return the number of unique words as key and the number of occurrences of each word as value
def word_count(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


# check if the word is lowercase and alphabetic
def is_lower_and_is_alpha(word):
    return word.isalpha() and word.islower()


def main():
    # check if the input is valid
    try:
        number_of_words = int(input())
        if not 1 <= number_of_words <= 10 ** 5:
            raise ValueError
    except ValueError:
        return print("Please input positive integer in range 1 ≤ n ≤ 10^5")

    words = []
    for i in range(number_of_words):
        word = input()
        # check if the input is valid
        if is_lower_and_is_alpha(word):
            words.append(word)
        else:
            return print("Wrong Input: Please enter word only in lowercase English Letter")

    word_counts = word_count(words)
    # print the number of unique words and the number of occurrences of each word
    print(len(word_counts))
    print(*word_counts.values())


if __name__ == "__main__":
    main()

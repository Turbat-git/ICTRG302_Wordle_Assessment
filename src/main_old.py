import random
score= []

valid_words = "all_words.txt"
target_word = "target_words.txt"
invalid_guess_message = "Please enter a real five character word"

print("Please guess 5 character words to find the mystery word!")
print("You will get 5 tries")
print("The word must be a real word")
print("The word must be spelled in Australian spelling")
print("Goodluck 😊")


def get_target_word(target_file):
    target_file = open(target_file, "r")
    data = target_file.read()

    data_into_list = data.split("\n")
    target_file.close()

    length_of_data = len(data_into_list)

    i = int(format(random.randint(0, length_of_data - 1)))
    chosen_target_word = data_into_list[i]
    return str(chosen_target_word)

def validate_user_guess(provided_target_word, valid_file):
    user_guess = input("Please enter your guess \n").lower()
    valid_file = open(valid_file, "r")
    data = valid_file.read()

    while True:
        try:
            user_guess = str(user_guess)
            break
        except:
            print(invalid_guess_message)

    if len(user_guess) != len(provided_target_word):
        print(invalid_guess_message)
    elif user_guess in data:
        return user_guess

    valid_file.close()


def track_score(provided_target_word, provided_user_guess):
    for i in range(len(provided_target_word)):
        score.append(0)

    user_guess_dictionary = {}
    target_word_dictionary = {}

    for character in provided_user_guess:
        if character in user_guess_dictionary:
            user_guess_dictionary[character] += 1
        else:
            user_guess_dictionary[character] = 1

    for character in provided_target_word:
        if character in target_word_dictionary:
            target_word_dictionary[character] += 1
        else:
            target_word_dictionary[character] = 1
    print(user_guess_dictionary)
    print(target_word_dictionary)

    counter = 0
    for i in range(len(provided_user_guess)):
        if provided_user_guess[i] == provided_target_word[i]:
            score[i] += 2
        elif provided_user_guess[i] in provided_target_word:
            score[i] += 1

        else:
            continue
    print(score)

chosen_target_word = get_target_word(target_word)
#print(chosen_target_word)
chosen_user_guess = validate_user_guess(chosen_target_word, "all_words.txt")
track_score("world", chosen_user_guess)
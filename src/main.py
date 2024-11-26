import random

ATTEMPT = 5
TARGET_WORDS_FILENAME = "target_words.txt"
VALID_WORDS_FILENAME = "all_words.txt"

# Present game instructions to the player
def show_help():
    print("Please guess 5 character words to find the mystery word!")
    print("You will get 5 tries")
    print("The word must be a real word")
    print("The word must be spelled in Australian spelling")
    print("Goodluck 😊")

# Read word files
def read_word_file(filename):
    target_file = open(filename, "r")
    data = target_file.readlines()
    target_file.close()
    word_list = []
    for line in data:
        word_list.append(line.strip().lower())
    return word_list

# Read a list of valid words
def get_list_valid_words(filename = VALID_WORDS_FILENAME):
    valid_words = read_word_file(filename)
    return valid_words

# Read a list of possible target words
def get_list_target_words(filename=TARGET_WORDS_FILENAME):
    target_words = read_word_file(filename)
    return target_words

def get_a_target_word(target_words):
    #return random.choice(target_words)
    return "world"

# Get and Validate the user guess
def get_user_input(valid_list, tries):
    while tries > 0:
        user_input = input(f"Please enter your guess (You have {tries} tries remaining.) \n").lower()
        if user_input != str(user_input):
            print("Please enter a five letter word, and not a number")
            continue
        elif len(user_input) != len(target):
            print("Please enter a five letter word")
            continue
        elif user_input not in valid_list:
            print("Please enter a real word")
            continue
        else:
            tries -= 1
            return user_input

# Score the guess by providing clues on each character's match
def score_guess(user_guess):
    """Scores a guess against the target word.

    Assigns a value to each character such that: <fill in>

    Args:
        user_guess: <fill in>

    Returns:
        A list of values representing the score for each character.
        For example:
        2 for correct character and correct position, 1 for correct character but wrong position and 0 for wrong character.
        """
    result = []
    if user_guess == target:
        result = [2, 2, 2, 2, 2]
        return result
    else:
        while user_guess != target:
            for i in range(len(user_guess)):
                if user_guess[i] == target[i]:
                    result.append(2)
                elif user_guess[i] in target:
                    result.append(1)
                else:
                    result.append(0)
            return result


# End the game when the user guesses the word
def end_game(result):
    if result == [2, 2, 2, 2, 2]:
        status = True
    else:
        status = False
    return status

# Present a completion letter
def completion_message(status):
    if status == True:
        print("CONGRATULATIONS YOU HAVE WON!")
    else:
        print(f"Sorry, you lost! The word was [{target}]")


if __name__ == "__main__":
    show_help()
    all_words = get_list_valid_words()
    target_words = get_list_target_words()
    target = get_a_target_word(target_words)

    while ATTEMPT > 0:
        validated_word = get_user_input(all_words, ATTEMPT)
        score = score_guess(validated_word)
        if score == [2, 2, 2, 2, 2]:
            break
        print(score)
        ATTEMPT -= 1
    win = end_game(score)
    completion_message(win)



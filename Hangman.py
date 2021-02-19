#basically hangman, without the hanging man - great dictionary & list practice
import random
list = []
hangman = [
            '''               +---+
                   |
                   |
                   |
                   |
                   |
                ========
                '''
            , 
            '''               +---+
                O  |
                   |
                   |
                   |
                   |
                ========
                ''',

            '''               +---+
                O  |
                |  |
                   |
                   |
                   |
                ========
                ''',    
            '''               +---+
                O  |
               /|  |
                   |
                   |
                   |
                ========
                ''',    
            '''               +---+
                O  |
               /|\ |
                   |
                   |
                   |
                ========
                ''',
            '''               +---+
                O  |
               /|\ |
               /   |
                   |
                   |
                ========
                ''',
                '''               +---+
                O  |
               /|\ |
               / \ |
                   |
                   |
                ========
GAME OVER!!
                '''

                ]
def category_selection(d):
    print("Categories:", end = " ")
    for i in d.keys():
        print(i, end = " ")
    print()
    while True:
        category = input("Select a category: ").lower()
        if not (category in d.keys()):
            print("Please try again")
        else:
            return category

def word_selection(d, category):
    value_list = 0
    rand_num = random.randint(0, len(d.values()) - 1)
    for keys, values in d.items():
        if keys == category:
           value_list = values
    return value_list[rand_num] 

def word_guess(word):
    word_check = ""
    wrong_answer_counter = 0
    tracker = []
    print("The word is", len(word), "letters long" )
    print("Guess a letter.\nYou will have 6 guesses.")
    for i in range(len(word)):
        list.append("_")
    print(list)
    print(hangman[wrong_answer_counter])
    while wrong_answer_counter < 6:
        user_guess = input().lower()
        if(len(user_guess) > 1):
            print("Please enter only one letter at a time!")
            continue
        if user_guess in tracker:
            print("You've already entered this letter!")
            continue
        tracker.append(user_guess)
        if user_guess in word:
            value = word.find(user_guess)
            count = value
            word_fill(value, user_guess)
            while count < len(word):
                if word[count] == user_guess:
                    value = count
                    word_fill(value, user_guess)
                count+=1
            print(list)
            if(word == word_check.join(list)):
                print("You've got it!")
                return
        else:
            wrong_answer_counter+=1
            print(hangman[wrong_answer_counter])
            
def word_fill(position, letter):
    list[position] = letter

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
        coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk        
        lion lizard llama mole monkey moose mouse mule newt otter owl panda         
        parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
        skunk sloth snake spider stork swan tiger toad trout turkey turtle         
        weasel whale wolf wombat zebra'''.split()
cars = "honda toyota ford chevrolet nissan subaru mini volkswagen bmw mercedes acura mazda".split()
fruits = "apples oranges bananas pineapples blueberries blackberries strawberries rasberries".split()
d = {"animals": words, "cars": cars, "fruits": fruits}

while(True):
    category = category_selection(d)
    word = word_selection(d, category)
    word_guess(word)
    print("The answer was:", word)
    response = input("Would you like to play again? ")
    if "y" in response:
        list = []
        continue
    print("Thanks for playing!")
    break




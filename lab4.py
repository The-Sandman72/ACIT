import random


def longerword(first, second):
    length_of_char1 = len(first)
    length_of_char2 = len(second)

    if length_of_char1 >= length_of_char2:
        return first
    elif length_of_char2 > length_of_char1:
        return second
    else:
        print("error")
    


def adding_to_dictionary():
    person = {'name': "Sarah", 'height': "5 feet", 'age': "22"}
    
    person['haircolour'] = "black"
    
    print(person['haircolour'])
    
    person['haircolour'] = 'brown'
    
    print(person['haircolour'])
    
    if 'eyeColor' in person:
        print("Key Found")
    
    elif 'eyeColor' not in person:
        print("Missing Key")
    
    else:
        print("error")


def countlongwords_question(words_str, minimum_length):
    
    word_list = [w.strip() for w in words_str.split(",")]

    long_words = []

    
    for word in word_list:
        if len(word) >= minimum_length:
            long_words.append(word)

    
    print(f"Words with length >= {minimum_length}: {long_words}")
    print(f"Count: {len(long_words)}")



def removeRepeats(list):
    result = []
    for item in list:
        if item in list:
            if item not in result:
                result.append(item)
    print(result)


def security_questions():
    
    security_questions_list = [
        {'question': "What was your first pet's name?", 'answer': "max"},
        {'question': "Where do you live?", 'answer': "my house"},
        {'question': "What is your mother's maiden name?", 'answer': "smith"}
    ]

    while True:
        
        question = random.choice(security_questions_list)
        
        password = input(f"Enter a password for {question['question']}: ").lower()
        
        if password == question['answer']:
            print("you can access your account!")
            break
        
        else:
            print("Please try again")

def login():
    user_key = [
        {'username': "thesandman72", 'password': "12345"}
    ]
    username_attempt = input("Please enter your username: ")
    
    while True:    
        if username_attempt == user_key[0]['username']:
            user_password_attempt = input(f"Please enter your password for {username_attempt}: ")
            
            if user_password_attempt == user_key[0]['password']:
                print("You have been logged in!")
                break
            else:
                print("Password does not match with the current username")
        else:
            print("Username not in database\nPlease try again")
            login()


def uppercaseOddWords(sentence):
    words = sentence.split()
    for i in range(1, len(words), 2):
        words[i] = words[i].upper()
    return " ".join(words)


def upperCamelCase(sentence):
    words = sentence.split()
    result = ""
    for word in words:
        result += word.capitalize()
    return result

def countWords(sentence):
    words = sentence.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def wordPosition(words):
    positions = {}

    for index, word in enumerate(words):
        if word in positions:
            positions[word].append(index)
        else:
            positions[word] = [index]

    return positions


inputs = [
    "buy",
    "it",
    "use",
    "it",
    "break",
    "it",
    "fix",
    "it",
    "trash",
    "it",
    "change",
    "it",
    "mail",
    "upgrade",
    "it",
]




def artistsByYear(artists):
    by_year = {}

    for entry in artists:
        year = entry["year"]

        if year in by_year:
            by_year[year].append(entry)
        else:
            by_year[year] = [entry]

    return by_year


artists = [
    {"song": "HOLIDAY", "name": "Lil Nas X", "year": 2020},
    {"song": "Say So", "name": "Doja Cat", "year": 2020},
    {"song": "Old Town Road", "name": "Lil Nas X", "year": 2019},
    {"song": "Bad Guy", "name": "Billie Eilish", "year": 2019},
    {"song": "God's Plan", "name": "Drake", "year": 2018},
]





'''
|=============================================================|
|                        Run Commands                         |
|=============================================================|

should be able to uncomment it all and get everything to run correctly
it does run out of order though... my bad :pensive:
'''


#first = input("Enter a word: ")
#second = input("Enter another word: ")

#words = input("Enter a list of words separated by commas: ").strip().lower()
#minimum_length = int(input("Enter a minimum character length: "))

#sentence = input("Enter a sentence: ")

#print(uppercaseOddWords(sentence))

#print(upperCamelCase(sentence))


#inputs = input("Enter a sentence: ")
#output = countWords(inputs)
#print(output)

#output = wordPosition(inputs)
#print(output)

#print(artistsByYear(artists))


#longerword(first, second)
#print(longerword(first, second))



#adding_to_dictionary()

#countlongwords_question(words, minimum_length)

#removeRepeats(["apple", "banana", "apple", "pear", "banana"])
#removeRepeats([3, 3, 1, 2, 1])

#security_questions()

#login()

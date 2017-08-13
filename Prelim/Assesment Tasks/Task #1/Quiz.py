###########
# Quiz.py #
###########


questionDictionary = {
    "multiple_choice": {
        "0": {
            "mark_value": 2,
            "question": "Which answer gives the best definition of Ergonomics?",
            "answer": "d",
            "choices": {
                "a": "The safety of workers in the work environment.",
                "b": "The study of the work environment.",
                "c": "The study of an employee’s efficiency in the work environment.",
                "d": "The study of the relationship between workers and their work environment."
            }
        },
        "1": {
            "mark_value": 2,
            "question": "What is open source software?",
            "answer": "b",
            "choices": {
                "a": "The ergonomics of the published software.",
                "b": "Software for which the original source code is made freely available and may be redistributed and/or modified.",
                "c": "Software for which source code is not published.",
                "d": "Software written in a 2nd generation language."
            }
        }
    },
    "fill_the_blank": {
        "0": {
            "mark_value": 2,
            "answer": "responsibility",
            "question": "Programmers have a  r_____________ of ensuring the accuracy of data. "
        }
    },
    "rank_appropriate_order": {
        "0": {
            "mark_value": 3,
            "question": "Rank in order of highest amount of storage",
            "correct_order": {
                "1": "5",
                "2": "1",
                "3": "2",
                "4": "3",
                "5": "4"
            },
            "choice_list": {
                "1": "Megabyte",
                "2": "Kilobyte",
                "3": "Megabit",
                "4": "Byte",
                "5": "Gigabyte"
            }
        }
    }
}


# Asks a multiple choice question based on the given ID
#
# @param dictionary array (dictionary)
# @param question string (int as a sting to keep the compiler happy)
#
# @return bool
def ask_multiple_choice(dictionary, question):
    for answerKey in dictionary["multiple_choice"][question]["choices"]:
        print(answerKey + ".) " + dictionary["multiple_choice"][question]["choices"][answerKey])
    return dictionary["multiple_choice"][question]["answer"] == input("Answer: ").lower()


# Asks a fill the blank question based on the given ID
#
# @param dictionary array (dictionary)
# @param question string (int as a sting to keep the compiler happy)
#
# @return bool
def ask_fill_blank(dictionary, question):
    return dictionary["fill_the_blank"][question]["answer"] == input("Answer: ").lower()


# Asks a rank in appropriate order question based on the given ID
#
# @param dictionary array (dictionary)
# @param question string (int as a sting to keep the compiler happy)
#
# @return bool
def ask_rank_order(dictionary, question):
    for choiceId in dictionary["rank_appropriate_order"][question]["choice_list"]:
        print("#" + choiceId + " " + dictionary["rank_appropriate_order"][question]["choice_list"][choiceId])
    correct = True
    for orderId in dictionary["rank_appropriate_order"][question]["correct_order"]:
        answer = input("#" + orderId + ": ").lower()
        answerId = dictionary["rank_appropriate_order"][question]["correct_order"][orderId]
        if not answerId == answer and not dictionary["rank_appropriate_order"][question]["choice_list"][answerId].lower() in answer:
            correct = False
    return correct


if "n" in input("Do you agree that this is all your own work? (Y/n)\n> ").lower():
    exit("You cannot complete this quiz unless it is your own work!\nExiting...")

print("Welcome to the Social and Ethical issue + Hardware and Software quiz!\n"
      "You will be asked multiple choice (x10), fill in the blank (x5) and rank in the appropriate order (x5) "
      "questions.\n"
      "Each question will be worth between one to three marks each. Each question will display it's mark value in "
      "brackets next to the question.\n\n")
currentMark = 0
possibleMark = 0

for questionType in questionDictionary:  # Loop through the question types
    for questionId in questionDictionary[questionType]:  # Loop through the questions
        # Assign the possible marks to a variable so we don't have to keep accessing the dictionary
        markValue = int(questionDictionary[questionType][questionId]["mark_value"])
        if markValue > 1:  # Watching out for single mark values
            print(questionDictionary[questionType][questionId]["question"] + " (" + str(markValue) + " marks)")
        else:
            print(questionDictionary[questionType][questionId]["question"] + " (" + str(markValue) + " mark)")
        if questionType == "multiple_choice":
            result = ask_multiple_choice(questionDictionary, questionId)
        elif questionType == "fill_the_blank":
            result = ask_fill_blank(questionDictionary, questionId)
        elif questionType == "rank_appropriate_order":
            result = ask_rank_order(questionDictionary, questionId)
        else:
            print("Unknown Question type!")
            result = "unknown"

        if result:
            print("Correct!")
            currentMark += markValue
        elif not result:
            print("Incorrect!")
        possibleMark += markValue
        print("\n")

if currentMark > 0:
    print("Score: " + str(round(currentMark / possibleMark * 100, 2)) + "% (" + str(currentMark) + "/" + str(
        possibleMark) + ")")
else:
    print("Score: 0% (0/" + str(possibleMark) + ")")

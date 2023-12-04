import time

# INTRODUCTION

print("\nWelcome to the Homelessness Statistics Quiz: Unveiling the Numbers and Realities! Today you'll ")
print("determine how aware you are about homelessness in the USA. To do so, you're going to get asked 10")
print("questions about this topic. For each right answer you'll earn 10 points. For each wrong answer you")
print("will get 0 points. Enjoy the game!\n")
time.sleep(3)

while True:
    start = input("Do you want to start the game? Press \"y\" for yes or \"n\" for no.\n").lower()
    if start == "y":
        break
    elif start == "n":
        exit()
    else:
        print("Invalid answer. Please try again.\n")
print("\n")

###############################################################################################################################
# COUNTER VARIABLES AS WELL AS ALLOWED ANSWERS AND SLEEP TIMER FOR THE QUIZ USED IN THE PROGRAM

# counts the points the player reached
point_counter = 0
# counts which question the player is at
question_counter = 1

# allowed answers in the Quiz
allowed_answers = ["a", "b", "c", "d"]

# time between two questions in seconds
sleep_time = 2

###############################################################################################################################
# FUNCTIONS USED IN THE PROGRAM

# determines the category the player is placed in based off his score
def scoring(current_score):
    if current_score >= 0 and current_score < 30:
        return "category 1"
    elif current_score >= 30 and current_score < 50:
        return "category 2"
    elif current_score >= 50 and current_score < 70:
        return "category 3"
    elif current_score >= 70 and current_score < 90:
        return "category 4"
    elif current_score >= 90 and current_score < 100:
        return "category 5"
    
# prints out the scoring rubric
def print_scoring():
    print("category 1: 0-29     -> No good intuition for the topic")
    print("category 2: 30-49    -> not really aware")
    print("category 3: 50-69    -> medium aware")
    print("category 4: 70-89    -> well aware")
    print("category 5: 90-100   -> We need more people like you!\n")

# message that gets printed when the player quits or finishes the game.
def end_message():
    print(f"After {question_counter} questions you have {point_counter} points. This number of points is equal to {scoring(point_counter)}. The scoring looks like this:\n")
    time.sleep(sleep_time)
    print_scoring()
    time.sleep(sleep_time)
    print("I hope you enjoyed this quiz. Feel free to play again. If you would like to learn more about homelessness, please visit ")
    print("\"https://usafacts.org/articles/how-many-homeless-people-are-in-the-us-what-does-the-data-miss/#:~:text=The%20Department%20of%20Housing%20and,about%202%2C000%20people%20from%202020.\". ")
    print("This is where all the information and facts come from.")

#  function to increase point_counter
def inc_point_counter(point_counter):
    point_counter += 10
    return point_counter

# function to increase question_counter
def inc_question_counter(question_counter):
    question_counter += 1
    return question_counter

# contains logic for all the questions
def question(question_list, question_counter, point_counter):
    print(f"Question {question_counter}:")
    print(question_list[0])
    time.sleep(sleep_time)
    for i in range(1, 5):
        print(question_list[i])
    while True:
        user_answer = input("Please type in your answer.\n").lower()
        if user_answer in allowed_answers:
            break
        else:
            print("Invalid answer. Please try again.\n")    
    if user_answer == question_list[5]:
        point_counter = inc_point_counter(point_counter)
        print(f"Your answer is right! Your score now is {point_counter}. You've got {10-question_counter} questions left.")
        question_counter = inc_question_counter(question_counter)
    else:
        print(f"Your answer is wrong! The right answer is {question_list[5]}. Your score is still {point_counter}. You've got {10-question_counter} questions left.")
        question_counter = inc_question_counter(question_counter)
    time.sleep(sleep_time)
    print(question_list[6])
    time.sleep(sleep_time)
    while True:
        proceed = input("\nDo you wish to proceed? Press \"y\" for yes or \"n\" for no. Please note that with \"n\" you'll immediately exit the game.\n").lower()
        if proceed == "y":
            break
        elif proceed == "n":
            end_message()
            time.sleep(sleep_time)
            print(f"\nPlease note that you have only played {question_counter-1} question(s). Therefore, the interpretation of your score is not completely accurate.")
            exit()
        else:
            print("Invalid answer. Please try again.\n")
    if question_counter == 11:
        print("Your result will be displayed in a few seconds.\n")
    else:
        print("The next question will be displayed in a few seconds.\n")
    time.sleep(sleep_time)
    return point_counter, question_counter

###############################################################################################################################
# LISTS THAT PROVIDE THE NECESSARY INFORMATION FOR THE QUESTIONS

# question lists that will use the question-function to provide the content of the game
question1 = ["How many people in the USA are homeless in total as of 2022?",
             "a: 333,284",
             "b: 582,462",
             "c: 817,382",
             "d: 1,205,925",
             "b",
             "The Department of Housing and Urban Development (HUD) counted around 582,000 Americans experiencing homelessness in 2022. That’s about 18 per 10,000 people in the US, up about 2,000 people from 2020."]

question2 = ["Who has the highest homelessness rate? (2022)",
             "a: Black",
             "b: Native American",
             "c: White",
             "d: Pacific Islander",
             "d",
             "Native Hawaiian and other Pacific Islanders are 1.8% of the homeless population despite being just 0.26% of the US population. One reason Native Hawaiian and Pacific Islanders have such high rates of homelessness could be because of Hawaii’s lack of affordable housing."]

question3 = ["What is the homelessness rate of Pacific Islanders? (Rates of homelessness per 10,000 by race, 2022)",
             "a: 121.21",
             "b: 47.98",
             "c: 178.74",
             "d: 88.71",
             "a",
             f"They have the nation’s highest rate of homelessness at 121 per 10,000 people. The next are Black people with 48.24%(!), which is {121.21-48.24} percentage points less."]

question4 = ["Who has the lowest homelessness rate? (2022)",
             "a: Asian",
             "b: White",
             "c: Native American",
             "d: Black",
             "a",
             "Asians have by far the lowest rate of homelessness. This is followed by the White population."]

question5 = ["What is the homelessness rate of Asians? (Rates of homelessness per 10,000 by race, 2022)",
             "a: 8.16",
             "b: 4.06",
             "c: 1.54",
             "d: 15.89",
             "b",
             f"Asians have the lowest rate of homelessness at 4.06%. The next group (White) has a rate of only 11.59%, a difference of {11.59-4.06} percentage points."]

question6 = ["How many veterans are estimated to be homeless? (2022)",
             "a: 15,324",
             "b: 21,984",
             "c: 33,129",
             "d: 46,346",
             "c",
             "Veterans also experience homelessness at a slightly higher rate than the overall population. Twenty out of every 10,000 veterans are homeless, compared to the nation’s overall rate of 18 per 10,000."]

question7 = ["What is the estimated number of homeless veterans in 2010?",
             "a: 21,468",
             "b: 10,476",
             "c: 74,087",
             "d: 88,348",
             "c",
             "The US government has established programs such as the HUD-Veterans Affairs Supportive Housing program that helps veterans find permanent housing and access healthcare. Additionally, the number of veterans has dropped. In 2021, there were 16.5 million veterans, compared to 21.8 million in 2008."]

question8 = ["What percentage of the homeless are men? (2022)",
             "a: 60.6",
             "b: 43.2",
             "c: 71.8",
             "d: 75.4",
             "a",
             "In 2022, 60.6% of homeless people were cisgender men, compared to 38.3% for cis women. Around 1.1% of homeless Americans were trans, nonbinary, or questioning."]

question9 = ["How many homeless people were there back in 2010?",
             "a: 340,218",
             "b: 429,122",
             "c: 567,982",
             "d: 637,077",
             "d",
             "Homelessness has fallen slightly overall since 2010. From 637,077 to 582,462, the number of homeless people has decreased by 8.57%."]

question10 = ["How many of the homeless in 2022 are sheltered homeless?",
             "a: 237,684",
             "b: 348,630",
             "c: 410,539",
             "d: 487,294",
             "b",
             "With 348,630 of the homeless, 59.85% are sheltered homeless, while 233,832 (40.15%) are unsheltered homeless. People in rapid rehousing aren’t counted as homeless, but people in transitional housing are, despite there not being a clear justification for one group being more “homeless” than the other."]

###############################################################################################################################
# PLACE WHERE THE PROGRAM IS EXECUTED

# main program
while True:
    point_counter, question_counter = question(question1, question_counter, point_counter)
    point_counter, question_counter = question(question2, question_counter, point_counter)
    point_counter, question_counter = question(question3, question_counter, point_counter)
    point_counter, question_counter = question(question4, question_counter, point_counter)
    point_counter, question_counter = question(question5, question_counter, point_counter)
    point_counter, question_counter = question(question6, question_counter, point_counter)
    point_counter, question_counter = question(question7, question_counter, point_counter)
    point_counter, question_counter = question(question8, question_counter, point_counter)
    point_counter, question_counter = question(question9, question_counter, point_counter)
    point_counter, question_counter = question(question10, question_counter, point_counter)
    question_counter -= 1
    end_message()
    while True:
        replay = input("Do want to play again? Press \"y\" for yes or \"n\" for no.\n")
        print("\n")
        if replay == "n":
            exit()
        elif replay == "y":
            question_counter = 1
            point_counter = 0
            break
        else:
            print("Invalid answer. Please try again.\n")
import glob
import random

true_string_for_output = "TRUE"
false_string_for_output = "FALSE"


def first_is_false_or_true(seg):
    for j in range(len(seg)):
        if seg[j:j + len(true_string_for_output)] == "True":
            return true_string_for_output
        elif seg[j:j + len(false_string_for_output)] == "False":
            return false_string_for_output
    return "Neither"


txt_files = []
question_answer_map = {}  # maps question (string) to corresponding answer (string)

for file in glob.glob("*.txt"):
    txt_files.append(file)
for text_file in txt_files:
    if text_file == "answer key.txt" or text_file == "questions without answers.txt" \
            or text_file == "incorrect questions.txt" or text_file == "incorrect questions answer key.txt":
        continue
    f = open(text_file)
    s = f.read()
    if "Correct!" in s:
        is_final_attempt = True
    else:
        is_final_attempt = False  # handled differently
    question_split = s.split("Question")
    if is_final_attempt:
        for i in range(1, len(question_split)):
            pts_split = question_split[i].split("pts")
            pts_split_on_line_break = pts_split[1].split("\n")
            # print(pts_split_on_line_break[1])
            question = pts_split_on_line_break[1].strip()
            if "0 / 0.4" in question_split[i]:  # INCORRECT RESPONSE
                you_answered_split = question_split[i].split("Correct Answer")
                correct_answer = first_is_false_or_true(you_answered_split[1])
            else:  # CORRECT RESPONSE
                split_on_correct_exclamation = question_split[i].split("Correct!")
                correct_answer = first_is_false_or_true(split_on_correct_exclamation[1])
            question_answer_map[question] = correct_answer
    else:
        for i in range(1, len(question_split)):
            pts_split = question_split[i].split("pts")
            pts_split_on_line_break = pts_split[1].split("\n")
            question = pts_split_on_line_break[1].strip()
            if "0 / 0.4" in question_split[i]:  # INCORRECT RESPONSE
                you_answered_split = question_split[i].split("`")
                if len(you_answered_split) <= 1:
                    continue
                incorrect_answer = first_is_false_or_true(you_answered_split[1])
                if incorrect_answer == false_string_for_output:
                    question_answer_map[question] = true_string_for_output
                else:
                    question_answer_map[question] = false_string_for_output
            else:  # CORRECT RESPONSE
                you_answered_split = question_split[i].split("`")
                if len(you_answered_split) <= 1:
                    continue
                correct_answer = first_is_false_or_true(you_answered_split[1])
                question_answer_map[question] = correct_answer


answer_key_file = open("answer key.txt", 'w')
questions_without_answers_file = open("questions without answers.txt", 'w')
questions_without_answers = ""
questions_with_answers = ""
num = 1
for q in question_answer_map:
    questions_with_answers += "\n{})  {} \n{} \n\n------".format(num, q, question_answer_map[q])
    questions_without_answers += "\n{})  {} \n\n ------".format(num, q)
    num += 1
answer_key_file.write(questions_with_answers)
questions_without_answers_file.write(questions_without_answers)
print("Shuffle the questions? Y/N")
shuffle = input()
questions = list(question_answer_map.keys())
if shuffle == "Y":
    random.shuffle(questions)
incorrect_question_answer_map = {}
correct_output = "Correct. Statement is {}"
incorrect_output = "WRONG! STATEMENT IS {}"
for question in questions:
    print(question + "\n T/F? (enter EXIT to stop)")
    input_answer = input()
    if input_answer == "EXIT":
        break
    actual_answer = question_answer_map[question]
    if 'T' in input_answer or 't' in input_answer:
        if actual_answer == true_string_for_output:
            print(correct_output.format(true_string_for_output))
        else:
            print(incorrect_output.format(false_string_for_output))
            incorrect_question_answer_map[question] = actual_answer
    else:
        if actual_answer == false_string_for_output:
            print(correct_output.format(false_string_for_output))
        else:
            print(incorrect_output.format(true_string_for_output))
            incorrect_question_answer_map[question] = actual_answer
answer_key_file = open("incorrect questions answer key.txt", 'w')
questions_without_answers_file = open("incorrect questions.txt", 'w')
questions_without_answers = ""
questions_with_answers = ""
num = 1
for incorrect_question in incorrect_question_answer_map:
    questions_with_answers += "\n{})  {} \n{} \n\n------" \
        .format(num, incorrect_question, incorrect_question_answer_map[incorrect_question])
    questions_without_answers += "\n{})  {} \n\n ------".format(num, incorrect_question)
    num += 1
answer_key_file.write(questions_with_answers)
questions_without_answers_file.write(questions_without_answers)
while len(incorrect_question_answer_map) > 0:
    old_incorrect_question_answer_map = incorrect_question_answer_map
    incorrect_question_answer_map = {}
    print("Shuffle the incorrect questions? Y/N")
    shuffle = input()
    questions = list(old_incorrect_question_answer_map.keys())
    if shuffle == "Y":
        random.shuffle(questions)
    incorrect_question_answer_map = {}
    for question in questions:
        print(question + "\n T/F? (enter EXIT to stop)")
        input_answer = input()
        if input_answer == "EXIT":
            break
        actual_answer = old_incorrect_question_answer_map[question]
        if 'T' in input_answer or 't' in input_answer:
            if actual_answer == true_string_for_output:
                print(correct_output.format(true_string_for_output))
            else:
                print(incorrect_output.format(false_string_for_output))
                incorrect_question_answer_map[question] = actual_answer
        else:
            if actual_answer == false_string_for_output:
                print(correct_output.format(false_string_for_output))
            else:
                print(incorrect_output.format(true_string_for_output))
                incorrect_question_answer_map[question] = actual_answer

import glob

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
question_start_marker = 'textarea_question_text">&lt;p&gt;'
question_answer_map = {}  # maps question (string) to corresponding answer (string)

for file in glob.glob("*.txt"):
    txt_files.append(file)
for text_file in txt_files:
    if text_file == "answer key.txt" or text_file == "questions without answers.txt":
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
                    print("too small")
                    continue
                incorrect_answer = first_is_false_or_true(you_answered_split[1])
                if incorrect_answer == false_string_for_output:
                    print("set")
                    question_answer_map[question] = true_string_for_output
                else:
                    print("set2")
                    question_answer_map[question] = false_string_for_output
            else:  # CORRECT RESPONSE
                you_answered_split = question_split[i].split("`")
                if len(you_answered_split) <= 1:
                    continue
                print("set3")
                correct_answer = first_is_false_or_true(you_answered_split[1])
                question_answer_map[question] = correct_answer


answer_key_file = open("answer key.txt", 'w')
questions_without_answers_file = open("questions without answers.txt", 'w')
questions_without_answers = ""
questions_with_answers = ""
for q in question_answer_map:
    questions_with_answers += "\n{} \n{} \n\n------".format(q, question_answer_map[q])
    questions_without_answers += "\n{} \n\n ------".format(q)
answer_key_file.write(questions_with_answers)
questions_without_answers_file.write(questions_without_answers)

for question in question_answer_map:
    print(question + "\n True/False? (enter EXIT to stop)")
    input_answer = input()
    if input_answer == "EXIT":
        break
    actual_answer = question_answer_map[question]
    if 'T' in input_answer or 't' in input_answer:
        if actual_answer == true_string_for_output:
            print("Correct. Statement is {}".format(true_string_for_output))
        else:
            print("WRONG! STATEMENT IS {}".format(false_string_for_output))
    else:
        if actual_answer == false_string_for_output:
            print("Correct. STATEMENT is {}".format(false_string_for_output))
        else:
            print("WRONG! STATEMENT IS {}".format(true_string_for_output))

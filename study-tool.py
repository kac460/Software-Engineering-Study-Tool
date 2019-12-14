import glob


def first_is_false_or_true(seg):
    true_string = "True"
    false_string = "False"
    for j in range(len(seg)):
        if seg[j:j + len(true_string)] == true_string:
            return "True"
        elif seg[j:j + len(false_string)] == false_string:
            return "False"
    return "Neither"


html_files = []
question_start_marker = 'textarea_question_text">&lt;p&gt;'
question_end_marker = '&lt;'
html_quote = '&nbsp;'
question_answer_map = {}  # maps question (string) to corresponding answer (string)
true_string_for_output = "TRUE"
false_string_for_output = "FALSE"
for file in glob.glob("*.html"):
    html_files.append(file)
for html_file in html_files:
    f = open(html_file)
    s = f.read()
    segments = s.split(question_start_marker)
    for segment in segments:
        question_raw = ""
        for i in range(len(segment)):
            if segment[i:i+len(question_end_marker)] == question_end_marker:
                break
            else:
                question_raw += segment[i]
        question_processed = question_raw.replace(html_quote, " ").strip()
        segment_split_by_correct_answer_selection = segment.split("selected_answer correct_answer")
        segment_split_by_incorrect_answer_selection = segment.split("wrong_answer")
        if len(segment_split_by_correct_answer_selection) > 1:  # CORRECT ANSWER
            if first_is_false_or_true(segment_split_by_correct_answer_selection[1]) == "True":
                question_answer_map[question_processed] = true_string_for_output
            else:
                question_answer_map[question_processed] = false_string_for_output
        elif len(segment_split_by_incorrect_answer_selection) > 1:  # INCORRECT ANSWER
            if first_is_false_or_true(segment_split_by_incorrect_answer_selection[1]) == "True":
                question_answer_map[question_processed] = false_string_for_output
            else:
                question_answer_map[question_processed] = true_string_for_output
for k in question_answer_map:
    print(k)
    print(question_answer_map[k])
    print("-----")

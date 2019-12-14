# Software-Engineering-Study-Tool
Takes .txts of quiz attempts and creates a study tool akin to flashcards with them.

## To use this tool
Clone the project to your computer. Go that directory in the terminal and run `python study-tool.py`. Note the Python version I use is 3.6. YMMV if you have a different version of python!

## To add your attempt of a quiz to this:
Click on a particular attempt of a quiz in Canvas.

Select All and click "Copy".

Paste into a .txt file. ***NAME THE FILE IN A WAY THAT IDENTIFIES IT: INCLUDE YOUR NAME, THE QUIZ #, AND THE ATTEMPT #.*** Example: "kevin quiz 1 attempt 2.txt"

**If the attempt was the final attempt for that quiz**, then just go ahead and put it in the root directory of the project (also please test to make sure your addition doesn't break the program and then push; thank you!)

**Otherwise**, due to differences in how previous attempts are displayed, you **MUST** manually enter a "`" just before each of your responses. 
Then put it in the root directory of the project (also please test to make sure your addition doesn't break the program and then push; thank you!)

Running the tool will now take into account the attempt you just added.

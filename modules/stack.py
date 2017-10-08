from modules import responder
from stackapi import StackAPI


SITE = StackAPI('stackoverflow')
SITE.page_size = 1
SITE.max_pages = 1

def search(command, channel):
    keyword = get_search_keyword(command)
    questions = SITE.fetch('questions', max=2, sort='votes', tagged=keyword)["items"]
    answer = answer_search(questions)
    if answer:
        responder.echo(":stack_overflow: " + str(answer) , channel)
    else:
        responder.echo(":stack_overflow: Can't find anything :( " ,channel)

def answer_search(questions):
    if not len(questions) == 0:
        question_id = questions[0]['question_id']
        answers =  SITE.fetch("questions/" + str(question_id) + "/answers",  sort='votes', order="desc")["items"]
        return handle_answers(answers)
    return

def handle_answers(answers):
    if not len(answers) == 0:
        return answers[0]['question_id']
    return    



def get_search_keyword(command):
        return ";".join(command.split(" ")[1::])
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
        return len(questions)
    return



def get_search_keyword(command):
        return ";".join(command.split(" ")[1::])
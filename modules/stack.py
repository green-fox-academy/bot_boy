from modules import responder

def search(command, channel):
    keyword = get_search_keyword(command)
    responder.echo(":stack_overflow: search to " + keyword, channel)

def get_search_keyword(command):
        return " ".join(command.split(" ")[1::])
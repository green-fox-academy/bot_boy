from modules import responder

def stack_search(command, channel):
    keyword = get_search_keyword()
    responder.log_printer(":stack_overflow search to : " + keyword )

def get_search_keyword(command):
        return " ".join(command.split(" ")[:1])
from modules import responder 
from modules import adapter
from modules import stack

def help_service(command, channel):
    if command == get_feature(command):
        responder.list_printer("Hi! there are my features:\n", list(feature_switcher.keys()), channel)
    else:
        responder.help_message(command, channel)   


feature_switcher = {
        "help": help_service,
        "hello": responder.hello_world,
        "whoareyou": responder.whoami
        ":stack_overflow:": 
    }

 

def handle_command(command, channel):
    try:
        feature_switcher[get_feature(command)](command, channel)
    except KeyError:
        responder.not_supported_command(channel)
    except Exception as e:
        responder.hidden_error_handling(e, channel)

def get_feature(command):
    return command.split(" ")[0]


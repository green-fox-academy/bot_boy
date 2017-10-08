from modules import responder 

def feature_switcher(feature):
    return {
        "help": responder.help_message,
        "hello": responder.hello_world
    }[feature]


def handle_command(command, channel):
    try:
        feature_switcher(get_feature(command))(command, channel)
    except KeyError:
        responder.not_supported_command(channel)
    except Exception as e:
        responder.hidden_error_handling(e, channel)

def get_feature(command):
    return command.split(" ")[0]


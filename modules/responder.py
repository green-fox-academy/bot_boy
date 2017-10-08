import client_service


def help_message(command, channel):
    client_service.send_response("This is a help message for the feature " +
                                 command.split(" ")[1], channel)


def whoami(command, channel):
    client_service.send_response(
        "Hi, check me on https://github.com/greenfox-academy/bot_boy", channel)


def list_printer(header, list_to_response, channel):
    response = header
    for line in list_to_response:
        response += line + "\n"
    client_service.send_response(response, channel)


def hello_world(command, channel):
    client_service.send_response("Helloooouuu", channel)


def hidden_error_handling(e, channel):
    client_service.send_response("Something went wrong :(", channel)
    client_service.send_response("<DEBUG> " + str(e), channel)


def not_supported_command(channel):
    client_service.send_response("Sorry, not supported command :(", channel)

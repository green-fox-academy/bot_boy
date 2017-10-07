import os
import time
from config import TOKEN, BOT_ID, AT_BOT
from slackclient import SlackClient



slack_client = SlackClient(TOKEN)


def handle_command(command, channel):
    {
        "help": help_message
    }[get_feature(command)](command, channel)


def help_message(command, channel):
    send_response("This is a help message for the feature " + command.split(" ")[1], channel)

def get_feature(command):
    return command.split(" ")[0]

def send_response(response, channel):
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                    output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print("connected and running")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("connection failed")

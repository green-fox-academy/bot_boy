from slackclient import SlackClient
from config import TOKEN, BOT_ID, AT_BOT
from modules import adapter
import time

def start():
    slack_client = get_client()
    READ_WEBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print("connected and running")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                adapter.handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("connection failed")


def send_response(response, channel):
    get_client().api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def get_client():
    return SlackClient(TOKEN)

def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                    output['channel']
    return None, None
 
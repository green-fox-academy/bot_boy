from modules import responder
from urllib import request

source = "http://numbersapi.com/random/trivia"

def get(command, channel):
    responder.echo("There is a :mindblown:", channel)
    page = request.urlopen(source).read().decode('UTF-8')
    responder.echo(page, channel)
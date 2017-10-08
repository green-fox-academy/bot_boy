from modules import responder
from urllib import request

source = "http://numbersapi.com/random/trivia"

def get(command, channel):
    responder.echo("Here is a fact:", channel)
    page = request.urlopen(source).read().decode('UTF-8')
    responder.echo(page, channel)
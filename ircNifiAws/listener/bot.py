from os import getenv, environ
import socket
import json
import re
import requests

HOST   = getenv('IRC_HOST','irc.twitch.tv') # defaults to the twitch.tv IRC server
PORT   = int(getenv('IRC_PORT',6667))       # defaults to the port twitch.tv uses
NICK   = environ['IRC_NICK']                # nickname is required, so we want to fail here
PASS   = environ['IRC_PASS']                # we make pass required, even though sometimes it is not
CHAN   = environ['IRC_CHAN']                # required because we need a channel to listen to
NAME   = "/src/data/{}".format(environ['FILE_NAME'])    # required because we need to write to somewhere

print HOST
print PORT
print CHAN

s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

CHAT_CHAN=re.compile(r"#\w+")
CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

while True:
    response = s.recv(1024).decode("utf-8")
    f = open(NAME, "a+")
    for line in response.split('\n'):
        if "PING :tmi.twitch.tv" in line:
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        elif "PRIVMSG" in line:
            username = re.search(r"\w+", line).group(0) # return the entire match
            message = CHAT_MSG.sub("", line).strip()
            channel = re.search(r"#\w+", line).group(0)[1:] # return the entire match
            formatted = {
                'channel': channel,
                'username': username,
                'message': message,
                'host': HOST
            }
            payload = json.dumps(formatted).encode("utf-8")
            print payload
            f.write("{}\r\n".format(payload))
    f.close


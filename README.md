# TF2 connect Mumble bot

When this bot is messaged with a connect string on discord, it'll reply with a clickable steam url which will launch tf2 and join the game.

Should work for any source game but i've only tested with TF2

## Running

requires `pipenv` to run with the shell script. otherwise look in the Pipfile for dependencies and install them yourself.

`./tf2-connect.sh <ip> <port> <password>`

## Other commands

`!join`: bot will join your current channel

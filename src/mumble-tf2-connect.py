import pymumble_py3 as pymumble
import re
import sys


def recive_message(message, mumble):
    user = mumble.users[message.actor]
    channel = mumble.channels[user['channel_id']]
    m = re.match(r'.*connect\s*(\S*)\s*;\s*password\s*(\S*)<*', message.message)
    response = ''
    if m is not None:
        url = 'steam://connect/' + m.group(1)
        if m.group(2) is not None:
            url += '/' + m.group(2)
        response = '<a href={0}>{0}</a>'.format(url)
    else:
        response = "sorry i don't recognise that format"

    channel.send_text_message(response)

def main():
    mumble = pymumble.Mumble('localhost', 'tf2-connect')
    mumble.start()
    mumble.is_ready()
    mumble.channels.find_by_name('Root').move_in()
    mumble.callbacks.add_callback('text_received',
                                  lambda m: recive_message(m, mumble))

    mumble.callbacks.reset_callback('text_received')

if __name__ == '__main__':
    main()
    sys.exit(0)

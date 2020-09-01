import pymumble_py3 as pymumble
import time
import re
import sys
import xml.etree.ElementTree as xml

connect_regex = r'connect\s*(\S*)\s*;\s*password\s*(\S*)'
xml_wrapper = '<?xml version="1.0"?><message>{}</message>'

def recive_message(message, mumble):
    user = mumble.users[message.actor]
    channel = mumble.channels[user['channel_id']]
    print("input", user, message, channel)

    response = "sorry i don't recognise that format"

    m_xml = xml.fromstring(xml_wrapper.format(message.message))
    for tag in m_xml.iter('*'):
        text = tag.text
        if text is not None:
            m = re.match(connect_regex, text)
            if m is not None:
                url = 'steam://connect/' + m.group(1)
                if m.group(2) is not None:
                    url += '/' + m.group(2)
                print("url : ", url)
                response = '<a href={0}>{0}</a>'.format(url)
                mumble.users.myself.comment("Last connect: " + response)
                break
            else:
                if text.startswith('!join'):
                    channel.move_in()
                    response = 'moving into your channel...'
                    break

    print("output", response)
    channel.send_text_message(response)

def main(args):
    mumble = pymumble.Mumble(args[1],
                             'tf2-connect',
                             port=int(args[2]),
                             password=args[3])
    mumble.start()
    mumble.is_ready()
    mumble.channels.find_by_name('Root').move_in()
    mumble.callbacks.add_callback('text_received',
                                  lambda m: recive_message(m, mumble))

    while True:
        time.sleep(10)


if __name__ == '__main__':
    if (len(sys.argv) != 4) or (sys.argv[1] == '-h'):
        print('''mumble bot which parses a connect string and responds in the channel with a steam link
./mumble-tf2-connect.py <ip> <port> <password>

source: https://github.com/t-taylor/mumble-tf2-connect-bot''')
        sys.exit(0)
    print('started connect bot')
    main(sys.argv)
    sys.exit(0)

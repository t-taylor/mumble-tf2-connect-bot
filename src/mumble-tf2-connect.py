import pymumble_py3 as pymumble
import re
import sys
import xml.etree.ElementTree as xml

connect_regex = r'(?:<p>)?connect\s*(\S*)\s*;\s*password\s*(\S*)(?:</p>)?'
xml_wrapper = '<?xml version="1.0"?><message>{}</message>'
_example_connect = "connect eepily.cool:2345; password cool"

def recive_message(message, mumble):
    user = mumble.users[message.actor]
    channel = mumble.channels[user['channel_id']]
    print(user, message, channel)

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

    print(response)

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

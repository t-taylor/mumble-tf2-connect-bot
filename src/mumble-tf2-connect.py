import pymumble_py3 as pymumble
import sys

def recive_message(message, mumble):
    user = mumble.users[message.actor]
    channel = mumble.channels[user['channel_id']]
    channel.send_text_message(message.message)

def main():
    mumble = pymumble.Mumble('localhost', 'tf2-connect')
    mumble.start()
    mumble.is_ready()
    mumble.channels.find_by_name('Root').move_in()
    channel = mumble.channels.find_by_name('onedotone')
    channel.send_text_message('test')

    mumble.callbacks.add_callback('text_received',
                                  lambda m: recive_message(m, mumble))

    mumble.callbacks.get_callbacks_list()
    mumble.callbacks.reset_callback('text_received')


if __name__ == '__main__':
    main()
    sys.exit(0)

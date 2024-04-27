import time

from init_routine import parse_cmdLine
from keyboard_listener import clipGpt


if __name__ == "__main__":
    file_api_key, options = parse_cmdLine()

    clipGpt(file_api_key, options)

    while True:
        time.sleep(1)  # Sleep for 1 second

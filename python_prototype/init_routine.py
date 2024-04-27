import os
import tkinter.messagebox as messagebox

import argparse
import yaml

def check_files(fname):
    if not os.path.isfile(fname):
        messagebox.showerror("Error", fname + ": File not found")
        return False

    return True


def parse_cmdLine():

     # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key-file", help="Path to the API key file")
    parser.add_argument("--options-file", help="Path to the options file")
    args = parser.parse_args()

    # Read API key from file
    config_file = args.api_key_file if args.api_key_file else "api-key.yaml"
    check_files(config_file)
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)["openai"]

    # Read options from file
    options_file = args.options_file if args.options_file else "options.yaml"
    check_files(options_file)
    with open(options_file, "r") as f:
        options = yaml.safe_load(f)["keyboard"]

    file_api_key = config["key"]

    return file_api_key, options
import subprocess
import requests
import random
import string
import datetime
import os
import sys

def generate_random_passphrase(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def encrypt_file(file_path, passphrase):
    encryption_command = f"echo {passphrase} | gpg --batch --yes --passphrase-fd 0 --symmetric -o {file_path}.gpg {file_path}"
    subprocess.run(encryption_command, shell=True)

def send_email(passphrase, file_name):
  # please declare your api key as env variables
    api_key = "your_api_key" 
    domain = "your_domain"
    sender_email = "security@yourdomain.com"
    recipient_email = "recipient@example.com"

    message = f"Your randomly generated passphrase is: {passphrase}\nFor file: {file_name}"

    response = requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={"from": f"Security <{sender_email}>",
              "to": recipient_email,
              "subject": "Random Passphrase",
              "text": message}
    )

    if response.status_code == 200:
        print("Passphrase emailed successfully.")
    else:
        print("Failed to send email.")

# Excludes script for encryption
script_filename = os.path.basename(__file__)

# Declare your directory here
watch_directory = "/path/to/watch/directory"
os.makedirs(watch_directory, exist_ok=True)

fswatch_command = f"fswatch -1 {watch_directory}"
while True:
    new_file = subprocess.check_output(fswatch_command, shell=True, text=True).strip()
    new_file_path = os.path.join(watch_directory, new_file)

    passphrase = generate_random_passphrase()
    # optional log file delete if not needed
    if new_file_path != script_filename:
        encrypt_file(new_file_path, passphrase)

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file = "encryption_log.txt"
        with open(log_file, "a") as log:
            log.write(f"File: {new_file_path}\n")
            log.write(f"Passphrase: {passphrase}\n")
            log.write(f"Timestamp: {current_time}\n\n")

        send_email(passphrase, new_file) 
    else:
        print(f"Skipped encrypting the script file: {script_filename}")

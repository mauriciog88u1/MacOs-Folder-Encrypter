# MacOs-Folder-Encrypter
Python Script to encrypt all new files added to a directory on your Mac
# File Encryption and Email Notification Script

This Python script monitors a specified directory for newly added files, encrypts them, and sends an email notification containing a randomly generated passphrase and the file name. It is designed to run on macOS.

## Prerequisites

1. Python 3 installed on your macOS.
2. `fswatch` installed using Homebrew: `brew install fswatch`.
3. Mailgun API credentials (API key, domain, sender email, recipient email) for sending email notifications. Please declare your API key as environment variables.

## Setup

1. Clone this repository to your local machine.
2. Open your terminal.

## Usage

To run the script in the background and redirect the output to a log file:

```bash
nohup python3 folder_encryption.py > file.log 2>&1 &

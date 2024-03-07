# GitHub Repository Scripts

This repository contains Python scripts that interact with the GitHub API to automate tasks related to repository management.

## 1. GitHub Repository Creator

This script allows you to create a new private repository on GitHub.

### Requirements

- Python 3.x
- `requests` library

### Setup

1. Get your personal access token from GitHub. You can follow [this guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to generate one.
2. Replace `"Your personal access token"` in the script with your actual personal access token.
3. Set the desired name and description for your new repository in the `data` dictionary.
4. Run the script.

### Usage

1. Clone or download the script.
2. Run the script using Python.
3. Check the output to verify if the repository creation was successful.

### Important Note

- Make sure to keep your personal access token secure and do not share it publicly.

## 2. GitHub File Pusher

This script allows you to add a file to an existing GitHub repository.

### Requirements

- Python 3.x
- `requests` library
- GitPython (`git` module)

### Setup

1. Get your personal access token from GitHub. You can follow [this guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to generate one.
2. Replace `"Your personal access token"` in the script with your actual personal access token.
3. Set the owner name, repository name, file path, commit message, committer name, and committer email in the script.
4. Run the script.

### Usage

1. Clone or download the script.
2. Run the script using Python.
3. Check the output to verify if the file was successfully added to the repository.

### Important Note

- Make sure to keep your personal access token secure and do not share it publicly.
- Ensure that the `.git` folder is properly configured in the directory where you run the script.

## 3. GitHub Repository Deleter

This script allows you to delete an existing repository on GitHub.

### Requirements

- Python 3.x
- `requests` library

### Setup

1. Get your personal access token from GitHub. You can follow [this guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to generate one.
2. Replace `"Your personal access token"` in the script with your actual personal access token.
3. Set the owner name and repository name in the script.
4. Run the script.

### Usage

1. Clone or download the script.
2. Run the script using Python.
3. Check the output to verify if the repository deletion was successful.

### Important Note

- Make sure to keep your personal access token secure and do not share it publicly.

## Disclaimer

- Use these scripts responsibly and in accordance with GitHub's terms of service.


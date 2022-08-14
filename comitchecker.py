import json
import os
import subprocess
import time
from urllib.request import urlopen

# Configurations
USERNAME = "IshanSingla"
REPO = "AboutPageFlask"
BRANCH = "main"
LOCAL_DIR = "/Users/ishansingla/Desktop/Cpp/AboutPageFlask"

def github_sync():
    
    # Fetch Sha of Github repo
    resp = urlopen(
        f"https://api.github.com/repos/{USERNAME}/{REPO}/branches/{BRANCH}")
    remote_sha = json.loads(
        str(resp.read(), encoding="utf-8"))["commit"]["sha"]

    # Fetch Sha of Local repo
    subprocess.check_output(["git", "checkout", BRANCH])
    local_sha = (str(subprocess.check_output(
        ["git", "rev-parse", "HEAD"]), encoding="utf-8"))[:-1]

    if remote_sha != local_sha:
        subprocess.check_output(["git", "pull", "origin", BRANCH])
        print("The local repo has been updated")
        return
    else:
        print("The local repo is already up-to-date")
        return

if __name__ == "__main__":
    os.system("clear")
    os.chdir(LOCAL_DIR)
    while True:
        github_sync()
        time.sleep(2)

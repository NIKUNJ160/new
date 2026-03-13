# Technical Documentation: Daily Auto Commit Bot

## 1. Overview
The Daily Auto Commit Bot is a lightweight automation tool designed to maintain a daily commit streak on GitHub. It uses a Python script to automatically append a timestamp to a designated text file and push the commit to the repository on a scheduled basis.

**Primary Use Case:** Learning Python scripting, Git automation, and task scheduling.
*Note: While this automates a daily contribution, it is intended as an educational exercise in workflow automation.*

## 2. Architecture & Tech Stack
- **Language:** Python 3
- **Libraries:** Built-in `os`, `subprocess`, and `datetime` modules. Third-party `schedule` library (optional, for built-in scheduling).
- **Environment:** Local Windows machine (or macOS/Linux)
- **Trigger Mechanism:** Operating system scheduler (e.g., Windows Task Scheduler) or a continuous Python loop.

## 3. Prerequisites
To run this bot, you need:
- Python 3 installed on your machine.
- Git installed and configured with your credentials.
- A local GitHub repository clone containing a target file (e.g., `log.txt`) for the bot to modify.

## 4. Implementation
The core logic resides in a Python script, for example, `bot.py`.

### The Python Script
```python
import os
import subprocess
import datetime
import time

# Configuration
# Change this to your local repository path where log.txt is located
REPO_PATH = r"C:\NIKUNJ\bot" 
LOG_FILE = "log.txt"
COMMIT_MESSAGE = "Automated daily log entry"

def run_command(command, cwd):
    """Utility to run shell commands."""
    result = subprocess.run(command, cwd=cwd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing {' '.join(command)}:\n{result.stderr}")
    else:
        print(result.stdout.strip())
    return result

def make_commit():
    print(f"[{datetime.datetime.now()}] Starting commit process...")
    
    # 1. Update the log file
    log_path = os.path.join(REPO_PATH, LOG_FILE)
    try:
        with open(log_path, "a") as f:
            f.write(f"Bot update recorded on {datetime.datetime.now()}\n")
        print(f"Updated {LOG_FILE}")
    except Exception as e:
        print(f"Failed to write to log file: {e}")
        return

    # 2. Add changes
    run_command(["git", "add", LOG_FILE], cwd=REPO_PATH)
    
    # 3. Commit changes
    run_command(["git", "commit", "-m", COMMIT_MESSAGE], cwd=REPO_PATH)
    
    # 4. Push to remote
    run_command(["git", "push"], cwd=REPO_PATH)
    
    print(f"[{datetime.datetime.now()}] Commit process completed.")

if __name__ == "__main__":
    # Run once immediately (ideal for running via Windows Task Scheduler)
    make_commit()
    
    # Alternative: Run continuously in the background using the 'schedule' package
    # (Requires: pip install schedule)
    #
    # import schedule
    # schedule.every().day.at("23:59").do(make_commit)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)
```

## 5. Scheduling the Bot
Instead of keeping the Python script running 24/7 in a command prompt, the best practice is to use Windows Task Scheduler to run the script once a day automatically.

### Windows (Task Scheduler)
1. Open **Task Scheduler**.
2. Click **Create Basic Task...** on the right sidebar.
3. Name it "Daily Auto Commit Bot" and set the Trigger to **Daily** at your preferred time.
4. For the Action, select **Start a program**.
5. In "Program/script", enter `python` (or the full path like `C:\Python39\python.exe`).
6. In "Add arguments", enter the full path to your script (e.g., `C:\NIKUNJ\bot\bot.py`).
7. Finish and save. The script will now run automatically every day!

### macOS / Linux (cron)
1. Open terminal and type `crontab -e`.
2. Add the following line to run it every day at 11:59 PM:
   `59 23 * * * /usr/bin/python3 /path/to/your/repo/bot.py >> /path/to/your/repo/cron_log.txt 2>&1`
3. Save and exit.

## 6. Troubleshooting
- **Git not pushing:** Ensure that Git is configured to remember your credentials locally. On Windows, Git Credential Manager usually handles this. Otherwise, use an SSH key.
- **File not found errors:** Make sure `REPO_PATH` in the Python script is exactly the absolute path to your cloned repository. 
- **Python not found in Task Scheduler:** You may need to provide the full absolute path to the `python.exe` executable inside the Task Scheduler configuration.

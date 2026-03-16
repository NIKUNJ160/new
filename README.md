# Auto-Committing GitHub Bot

This is a Python script that automatically makes commits and pushes them to a remote repository.

## Prerequisites

- Python 3
- Git installed and configured with your credentials

## Setup

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo>
   cd <your-repo-directory>
   ```

2. **Configure the script:**
   Open `bot.py` and modify the following variables at the top of the file:
   - `REPO_PATH`: The absolute path to your local git repository.

3. **Run the script:**
   ```bash
   python bot.py
   ```

## Automation (Windows)

To run this script automatically every day on Windows, you can use the Task Scheduler:

1. Open **Task Scheduler**.
2. Click **Create Basic Task...**
3. Name it (e.g., "Auto Git Commit") and choose **Daily** for the trigger.
4. Choose **Start a program** for the action.
5. In **Program/script**, browse and select your `python.exe` executable (e.g., `C:\Python39\python.exe`).
6. In **Add arguments**, enter the path to the script (e.g., `C:\path\to\your\bot.py`).
7. In **Start in**, enter the directory containing the script (e.g., `C:\path\to\your\`).
8. Finish creating the task.

The script will now run daily at the specified time, adding a new line to `log.txt` and pushing the changes to GitHub.

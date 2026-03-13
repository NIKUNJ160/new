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
    
    # 4. Push to remote (ignored for now as no remote is likely set locally yet)
    # run_command(["git", "push"], cwd=REPO_PATH)
    
    print(f"[{datetime.datetime.now()}] Commit process completed.")

if __name__ == "__main__":
    # Run once immediately
    make_commit()

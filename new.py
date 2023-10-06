import os
import subprocess
from datetime import datetime, timedelta

# Replace with your GitHub username and email
github_username = "web-top123"
github_email = "webtopc2021@gmail.com"

# Replace with the directory of your Git repository
repository_dir = "C:/Users/Administrator/Downloads/link-shortener-main"

# Specify the start date and end date for the month
start_date = datetime(2023, 8, 1)
end_date = datetime(2023, 9, 1)

# Loop through each day in the specified month
current_date = start_date
while current_date <= end_date:
    # Generate a dummy file content for the commit
    dummy_content = f"Commit on {current_date.strftime('%Y-%m-%d %H:%M:%S')}"
    dummy_file = os.path.join(repository_dir, f"commit_{current_date.strftime('%Y%m%d%H%M%S')}.txt")

    # Create and commit the dummy file
    with open(dummy_file, "w") as file:
        file.write(dummy_content)

    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", f"Commit on {current_date.strftime('%Y-%m-%d')}"])
    subprocess.call(["git", "push", "origin", "main"])
    # Move to the next day
    current_date += timedelta(days=1)
    
# Push the commits to your GitHub repository


print("Commits pushed to GitHub.")
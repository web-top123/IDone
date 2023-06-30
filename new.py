import os
import subprocess
from datetime import datetime, timedelta

# Replace with your GitHub username and email
github_username = "YourUsername"
github_email = "youremail@example.com"

# Replace with the directory of your Git repository
repository_dir = "C:/Users/Administrator/Downloads/link-shortener-main"

# Specify the year and month for which you want to create commits
year = 2023
month = 7

# Specify the number of commits per day
commits_per_day = 3  # Adjust as needed

# Calculate the first and last day of the month
first_day = datetime(year, month, 1)
last_day = datetime(year, month + 1, 1) - timedelta(days=1)

# Loop through each day in the specified month
current_date = first_day
while current_date <= last_day:
    for i in range(commits_per_day):
        # Generate a dummy file content for each commit
        dummy_content = f"Commit {i + 1} on {current_date.strftime('%Y-%m-%d %H:%M:%S')}"
        dummy_file = os.path.join(repository_dir, f"commit_{current_date.strftime('%Y%m%d%H%M%S')}.txt")

        # Create and commit the dummy file with the desired date and time
        with open(dummy_file, "w") as file:
            file.write(dummy_content)

        # Set the commit date and time explicitly
        commit_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
        subprocess.call(["git", "add", "."])
        subprocess.call(["git", "commit", "--date", commit_date, "-m", f"Commit on {current_date.strftime('%Y-%m-%d')}"])
        subprocess.call(["git", "push", "origin", "main"])
    # Move to the next day
    current_date += timedelta(days=1)

# Push the commits to your GitHub repository


print("Commits pushed to GitHub with custom commit times.")
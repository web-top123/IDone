@echo off

REM Set your Git username
set YOUR_NAME=Your Name

REM Set the output file
set OUTPUT_FILE=commit_tracking.txt

REM Set the tracking start year
set TRACKING_START_YEAR=2015
set TRACKING_END_YEAR=2023

REM Clear the previous content of the output file
echo. > %OUTPUT_FILE%

REM Loop through each year in the tracking period
for /l %%Y in (%TRACKING_START_YEAR%,1,%TRACKING_END_YEAR%) do (
    REM Count commits for the current year
    for /f %%A in ('git log --since="%%Y-01-01" --until="%%Y-12-31" --author="%YOUR_NAME%" --oneline ^| find /c /v ""') do set COUNT=%%A
    
    REM Append the count to the output file
    echo Contributions in year %%Y: !COUNT! >> %OUTPUT_FILE%
)

echo Tracking completed for the specified period.
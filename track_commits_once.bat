@echo off

REM Set your Git username
set YOUR_NAME=Your Name

REM Set the output file
set OUTPUT_FILE=push_tracking_daily.txt

REM Set the tracking start and end years
set TRACKING_START_YEAR=2015
set TRACKING_END_YEAR=2023

REM Clear the previous content of the output file
echo. > %OUTPUT_FILE%

REM Loop through each year in the tracking period
for /l %%Y in (%TRACKING_START_YEAR%,1,%TRACKING_END_YEAR%) do (
    REM Loop through each day of the year
    for /l %%D in (1,1,365) do (
        setlocal enabledelayedexpansion
        REM Calculate the date for the current day
        set "DATE=%%Y-01-01 + %%D days"
        endlocal
        
        REM Count pushes for the current day
        for /f %%A in ('git rev-list --count --since="%DATE%" --until="%DATE% + 1 day" --author="%YOUR_NAME%" HEAD') do set COUNT=%%A
        
        REM Append the count to the output file
        echo Pushes on %%DATE%: !COUNT! >> %OUTPUT_FILE%
    )
)

echo Daily push tracking completed for the specified period.
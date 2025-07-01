@echo off
setlocal enabledelayedexpansion

:: Loop through each unit from Unit1 to Unit30
for /L %%i in (1, 1, 30) do (
    set "unit=Unit%%i"
    echo Generating HTML for !unit!...
    
    :: Run the Python script for each unit
    python ..\..\scripts\generate_unit.py !unit!

    echo Finished generating HTML for !unit!
)

echo All HTML files generated successfully.
pause

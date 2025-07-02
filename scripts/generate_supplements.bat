@echo off
setlocal enabledelayedexpansion

:: Set the directory path where the text files are located
set "directory=C:\path\to\your\files"

:: Change to the target directory
cd /d "%directory%"

:: Loop through all files in the directory
for %%F in (*) do (
    :: Get the base name of the file (without extension)
    set "filename=%%~nF"
    
    :: Exclude prs_, audio_, and def_ prefixed files
    if /I not "!filename:~0,4!"=="prs_" if /I not "!filename:~0,6!"=="audio_" if /I not "!filename:~0,4!"=="def_" (
        

            :: Call the Python script with the appropriate argument (the current text file)
            echo Processing: %%F
            python ..\..\..\scripts\generate_supplement.py "%%F"
        
            :: Print a separator for clarity
            echo ---------------------------

    )
)

echo All files processed.
pause

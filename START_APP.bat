@echo off
title AI Mental Health OS - Starting...
color 0A
echo.
echo  ============================================
echo   🧬 AI Mental Health Operating System
echo   Starting up... Please wait...
echo  ============================================
echo.

cd /d "C:\Users\kartik\OneDrive\Desktop\AI Mental Healthcare oparating System"

echo  [1/2] Activating environment...
call .venv\Scripts\activate.bat

echo  [2/2] Launching app in browser...
echo.
echo  App will open at: http://localhost:8501
echo  Close this window to STOP the app.
echo.

start "" http://localhost:8501
.venv\Scripts\streamlit.exe run frontend/app.py

pause

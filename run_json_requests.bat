
@echo off

start "" python App.py

timeout /t 10 /nobreak >nul

python json_requests.py

pause

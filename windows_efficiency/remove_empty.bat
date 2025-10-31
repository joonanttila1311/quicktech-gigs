@echo off
set "target=C:\Users\YourName\Documents\Test"
for %%f in (%target%\*) do (
    if %%~zf==0 del "%%f"
)
echo ✅ Empty files deleted
pause

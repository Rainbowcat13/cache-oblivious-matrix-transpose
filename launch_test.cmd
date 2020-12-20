@echo off
set python_path=%cd%\venv\scripts\python.exe

for /L %%B in (50, 50, 700) do %python_path% tester.py 50 %%B %%B %%B >> test_results
for /L %%B in (1000, 1000, 7000) do %python_path% tester.py 1 %%B %%B %%B >> test_results
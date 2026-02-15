@echo off
echo Starting Play Palace v11 Client...
echo.
uv sync
uv run python client.py
pause

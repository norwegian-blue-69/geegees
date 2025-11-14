# Geegees
The purpose of this project is to try and predict horse racing results.
The idea is to use legal only means to pull available data regarding past and current races.
Betfair's API will be used to pull data.
The logic will then analyse the available data and suggest potentially good options for making bets.
Bets will be placed on the Betfair exchange so as not to breach the terms of the commercial bookmakers.

Minimal Python project skeleton created by assistant.

## Quick start

1. Create and activate a virtual environment:

   python -m venv .venv
   .venv\Scripts\Activate.ps1

2. Install dev requirements:

   python -m pip install -r requirements.txt

3. Run tests:

   pytest -q

## Git / GitHub

This folder is initialized as a local git repository. To push to GitHub the assistant attempted to create a remote named `origin`. If that failed, you can create a repo manually and run:

   git remote add origin <your-github-repo-url>
   git push -u origin main



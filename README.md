# Schedule Bot
A simple telegram bot that parses the mirea schedule and sends it to chat on the __/schedule__ command. Also has a callback button to view the schedule on other days of the week
# Deployment
Create .env file according to .env_example
```
poetry install
poetry run python schedule_bot/bot.py
```
# Docker
```
docker build -t schedule_bot . 
docker run schedule_bot   
```

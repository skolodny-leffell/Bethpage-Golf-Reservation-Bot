# Bethpage Golf Reservation Bot

This project is a bot designed to automate the process of reserving golf times at Bethpage State Park. The bot interacts with the reservation system to book tee times efficiently and reliably.

## Features

- Automates the reservation process for golf times.
- Handles user authentication and session management.
- Built in scheduler to change when the bot runs

## Setup Instructions

### Configuration

#### .env File
Create a copy of the `.env.sample` file and rename it to `.env`. Use the following guidelines to format your .env

```plaintext
USERNAME=your_username_here
PASSWORD=your_password_here
DATE=MM-DD-YYYY
TIME=HH:MM:SS
INTERVAL_IN_SECONDS=60
HEADLESS=false
```

Replace `your_username_here`, and `your_password_here` with your actual credentials. For the `DATE` replace `MM` with the month, `DD` with the day and `YYYY` with the year (ex. 10-31-2024). For the `TIME`, please use military time. Replace `HH` with the hour, `MM` with the minites and `SS` with the seconds. (ex. 11:20:00 or 14:30:00). The default time in between runs is 60 seconds. Whatever you change the `INTERVAL_IN_SECONDS` to, the interval in seconds between when the code will run will change (WHOLE NUMBERS ONLY). `HEADLESS` defaults to false. Set it to true if you don't want the browser showing up on the screen.

### Running the Bot
To run the bot, open the `main.exe` file in the same folder as `.env` file.

This will start the bot using the configurations specified in your `.env` file.


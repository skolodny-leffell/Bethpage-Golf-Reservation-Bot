# Bethpage Golf Reservation Bot

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- [Python](https://www.python.org/downloads/)

### Download Dependencies
To download the necessary dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

### Configuration

#### .env File
Create a copy of the `.env.sample` file and rename it to `.env`. Use the following guidelines to format your .env

```plaintext
USERNAME=your_username_here
PASSWORD=your_password_here
DATE=MM-DD-YYYY
TIME=HH:MM:SS
```

Replace `your_username_here`, and `your_password_here` with your actual credentials. For the `DATE` replace `MM` with the month, `DD` with the day and `YYYY` with the year (ex. 10-31-2024). For the `TIME`, please use military time. Replace `HH` with the hour, `MM` with the minites and `SS` with the seconds. (ex. 11:20:00 or 14:30:00)

### Running the Bot
To run the bot, use the following command:

```bash
& /path/to/python.exe "path/to/python/file/main.py"
```

This will start the bot using the configurations specified in your `.env` file.


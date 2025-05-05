NAV Checker
Automated daily Net Asset Value (NAV) monitoring and notification system.

Overview
This GitHub Actions workflow automatically checks the latest NAV data every day at 6 AM UTC and sends real-time updates to your preferred chat platforms via a bot. Simplify your NAV monitoring process with minimal manual effort!

Features
Scheduled Automation: Runs daily at 6 AM UTC (customizable).
Web Scraping: Fetches NAV data from your specified sources.
Instant Notifications: Sends updates directly to your chat IDs using a bot.
Getting Started
Prerequisites
A messaging bot (e.g., Telegram, Slack) with a token.
Chat IDs where notifications will be sent.
GitHub repository with secrets configured.
Setup Instructions
Configure Secrets in GitHub:

BOT_TOKEN: Your bot's API token.
CHAT_ID_1 and CHAT_ID_2: The chat identifiers for notifications.
Clone or fork the repository to your GitHub account.

Ensure the workflow file exists at .github/workflows/nav_checker.yml.

Create the NAV scraping script (check_nav.py) with your logic to fetch and parse NAV data.

Customization
Modify the cron expression in the workflow file to change the schedule.
Update check_nav.py with your data source and parsing logic.
Add or remove chat IDs as needed.
Requirements
Python 3.11
Python libraries: requests, beautifulsoup4
(Included in the workflow via pip install)

License
This project is provided as-is. Feel free to modify and adapt to your needs.

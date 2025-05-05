# 🧮 NAV Checker

**Automated Daily Net Asset Value (NAV) Monitoring & Notification System**

---

## 📌 Overview

**NAV Checker** is a GitHub Actions workflow that automates the process of monitoring NAV (Net Asset Value) data. It runs every day at **6 AM UTC**, scraping data from your configured sources and delivering updates directly to your chat platforms using a messaging bot. Simplify your NAV tracking with zero manual effort! 🚀

---

## ✨ Features

- ⏰ **Scheduled Automation**: Automatically runs every day at **6 AM UTC** (fully customizable via cron).
- 🕸️ **Web Scraping**: Pulls the latest NAV data from your specified sources.
- 📢 **Instant Notifications**: Sends real-time updates to your chosen chat IDs via a bot.

---

## 🚀 Getting Started

### ✅ Prerequisites

- A messaging bot (e.g., **Telegram**, **Slack**) with a valid API token.
- One or more chat IDs where notifications will be sent.
- A GitHub repository with the required **secrets** configured.

---

### 🛠️ Setup Instructions

1. **Configure GitHub Secrets**:
   - `BOT_TOKEN`: Your bot's API token.
   - `CHAT_ID_1`, `CHAT_ID_2`, etc.: The chat identifiers to send notifications.

2. **Fork or Clone** this repository to your GitHub account.

3. Ensure the workflow file exists at:

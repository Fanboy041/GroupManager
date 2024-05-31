---
title: Contibuting Notes
layout: template
filename: CONTRIBUTING.md
--- 
# Contibuting Notes

## Table of Contents

1. [Creating a Bot on Telegram](#creating-a-bot-on-telegram)
2. [Creating an App on Telegram](#creating-an-app-on-telegram)
3. [Cloning the Repository](#cloning-the-repository)
4. [Setting Up the Workspace](#setting-up-the-workspace)
5. [Running the Bot](#running-the-bot)
6. [Project Structure](#project-structure)
7. [Notes](#notes)

## Creating a Bot on Telegram

1. Open Telegram and go to [BotFather](https://t.me/BotFather).
2. Start the BotFather bot and send the command: `/newbot`.
3. Follow the instructions to name your bot and set a username.
4. BotFather will provide you with an API token. Keep this token for the next steps.

## Creating an App on Telegram

### Navigate to the Website

Open your web browser and go to [my.telegram.org](https://my.telegram.org/).

### Log In

Log in using your phone number. You will receive a confirmation code in the Telegram app, which you need to enter on the website.

### Navigate to API Development Tools

After logging in, you will see the "API Development Tools" section. Click on it to proceed.

### Create a New Application

You will be prompted to create a new application. Fill in the required fields:

- App title: The name of your application.
- Short name: A short identifier for your application.
- URL: Enter a placeholder URL if you don't have a public URL, such as http://example.com.
- Platform: Select the platform your application will run on (e.g., Desktop, Web, Android, iOS).
- Description: A brief description of your application.

Here’s an example of how you might fill out the form:

- App title: MyTelegramApp
- Short name: mytelegramapp
- URL: http://example.com
- Platform: Desktop
- Description: This is a test application for interacting with the Telegram API.

### Submit the Form

After filling out the form, click the "Create Application" button.

### Retrieve Your API ID and API Hash

Once the application is created, you will be redirected to a page displaying your application's details, including your API ID and API hash. These credentials are essential for interacting with the Telegram API.

## Cloning the Repository

1. Install Git from [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
2. Install Python from [Installing Python](https://python.org/downloads/).
3. Create a new folder on your system.
4. Open PowerShell in the new folder (Shift + Right-click > Open PowerShell window here).
5. Open the folder in your code editor:
    ```
    code .
    ```
6. In the terminal, clone the repository:
    ```
    git clone https://github.com/Fanboy041/GroupManager.git
    ```

## Setting Up the Workspace

1. Install the required libraries by running:
    ```
    pip install -r requirements.txt
    ```
2. Create a `.env` file in the root directory with the following content:
    ```
    MONGO_URI=""
    BOT_TOKEN=""
    API_HASH=''
    API_ID=''
    ```
    Replace the placeholders with your MongoDB URI, api hash, api id also the bot API token from BotFather.

## Running the Bot

To start the bot, run:
```
python ./src/main.py
```
Or to start with a watcher that restarts the bot if script modified, run:
```
python ./src/watcher.py ./src/main.py
```
If you're using Termux, you need to add the following to the main script:
```
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
```
## Project Structure

- **requirements.txt**: Lists the required libraries.
- **src**:
  - **Commands**: Scripts for bot commands (e.g., `/start`).
  - **Database**: Scripts for database interactions with MongoDB.
  - **Features**: Additional features for the bot.
  - **Buttons**: Scripts for handling callback queries (actions triggered by inline buttons).
  - **main.py**: The main script that integrates all components.

## Notes

1. Let commands controls the bot functionality
2. Recreate the database to match Walid's thoughts
3. Do not make a lot of decorators in the main.py file
4. Do not make decorators inside functions
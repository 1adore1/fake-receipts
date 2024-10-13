# Telegram Bot for Creating Fake Transfer Screenshots
### Overview
This project is a Telegram bot that generates fake transfer receipts in the form of screenshots. 
Users can interact with the bot, inputting details like phone number, name, and amount, and the bot will generate a custom receipt image. 
The bot is built using the ```aiogram``` library and utilizes the ```PIL (Pillow)``` library for image manipulation.
### Installation
1. Clone the repository:
```
git clone https://github.com/1adore1/fake-receipts.git
cd fake-receipts
```
2. Install required libraries:
```
pip install aiogram pillow
```
### Usage
You can generate receipts using the telegram bot ```@ScreenshotReceiptBot``` or just run the script from the command line:
```
python main.py
```
1. Starting the bot: Use the ```/start``` command to start interacting with the bot.
2. Creating a receipt: Use the ```/new``` command to start the process of creating a new receipt.
3. Follow the prompts: The bot will ask you for:
* Phone number
* Name
* Amount
4. Receive receipt: The bot will generate and send you an image with the specified details.

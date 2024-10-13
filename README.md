# Telegram Bot for Creating Fake Transfer Screenshots
![image](https://github.com/user-attachments/assets/515bbcda-1bbf-4860-8c5b-d654bf38ae63)
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
#### Running the Bot via Command Line
1) **Starting the bot**:

  * To start the bot, run the following command in your terminal:
    ```
    python main.py
    ```
  * Make sure you have set up your bot token and environment properly as per the installation instructions.
  2) **Bot interaction**: Once the bot is running, you can communicate with it through Telegram by finding the bot with the username you registered in BotFather.
---
#### Using the Bot via Telegram
Once the bot is running, interact with it via Telegram by following these steps:

1) **Start interaction**:

  * Open a chat with the bot in the Telegram app and type ```/start```.
  * The bot will send a welcome message and display a button labeled "New receipt".
2) **Creating a receipt**:
  
  * Option 1: Type ```/new``` in the chat to begin the receipt creation process.
  * Option 2: Press the "New receipt" inline button to start.
3. **Follow the bot's prompts**:
* The bot will ask for:
  
  1) **Phone number**: Enter a phone number in the format ```123 456 78 90```.
  2) **Name**: Enter a name that consists of letters, spaces, and an optional period.
  3) **Amount**: Provide the amount (must be a positive number).
4. **Receive the receipt**:
* Once all the inputs are provided, the bot will generate a receipt image and send it back to you in the chat.

<h1 align="center">Hi there, I'm <a href="https://daniilshat.ru/" target="_blank">Anton</a> 

<div id="header" align="center">
  <img src="https://media.giphy.com/media/Qbm1Oget7e3vVl9uPB/giphy.gif" width="100"/>
</div>

## Telegram bot project with user chat parsing.

## Bot Features:

### The bot is launched by the "Start data parsing" button. A script is launched that searches for messages among the user's chats by keywords in the list of chat links for the current date.
### The data is saved in an excel file, which can be obtained by clicking the "Get data file" button. The Excel file contains data: keywords, chat name, chat link, date and time, message text

## Project launch

### To start the project, you need to perform the following steps: 

#### 1. Register the bot in Telegram and get its unique id. To do this, there is a special bot in Telegram — @BotFather https://telegram.me/botfather.
#### It needs to be found and accessed first with the /start command and then with the /newbot command. You will need to come up with a bot name that ends in bot.
#### If successful, BotFather returns the bot token and a link to quickly add the bot to contacts/

#### 2. To work with the Telegram API, we need to get api_id and api_hash. You can do this in the Telegram Developer Tools section.
#### This is a mandatory action not only when creating our bot, but also when creating any bot or parser that uses the messenger API.
#### Click on the link https://my.telegram.org/auth?to=apps and log in using the phone number linked to your profile in the messenger.
#### After authorization, you need to select API development tools:
#### In the form that opens, fill in the empty fields. It is not necessary to fill in everything, the main thing is to specify the full and short name of the application:
#### After clicking Create application, a page opens where we are interested in two parameters: api-id and api-hash. These parameters need to be saved to a file.

#### 3. Clone a project from the github.com site using the command $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
#### 4. Install dependencies from a file requirements.txt using the python -m pip install -r command requirements.txt
#### 5. Replace the values of api_id, api_hash and token in the code with their own values
#### 6. Create a session for the pyrogram client. The first time you run the script, you will need to enter the telegram authorization code.
#### Then you do not need to enter it, so a session named my_session will be created.
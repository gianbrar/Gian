from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    "Gian",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ],
    database_url = "sqlite:///database.sqlite3"
)

trainer = ListTrainer(bot)

trainer.train([
    "Hi, Gian!",
    "Hey friendo :p",
    "How are you?",
    "I'm great!",
    "Sounds cool.",
    "Thank you!",
    "You're welcome!"
])

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)
    
    except(KeyboardInterrupt, EOFError, SystemExit):
        break

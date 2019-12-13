from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random
import hashlib

global clearanceLevel
clearanceLevel = 1
def defaultResponseFunc(finalResponse):
    respond = (random.randint(0, 4))
    if respond == 0:
        return "Could you repeat that?"
    elif respond == 1:
        return "I'm sorry, can you say that again?"
    elif respond == 2:
        return "I didn't quite understand."
    elif respond == 3:
        return "I didn't catch that. Could you repeat?"
    elif respond == 4:
        return "Say that again?"

def clearanceLevelOne(errorTrue, name):
    global finalName
    finalName = name
    if errorTrue == "yes":
        print("Password incorrect. Welcome false " + name + " (CLEARANCE LEVEL ONE)")
    else:
        print("Welcome " + name + " (CLEARANCE LEVEL ONE)")

bot = ChatBot(
    "Gian",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": defaultResponseFunc(""),
            "maximum_similarity_threshold": .90
        }
    ],
    database_url = "sqlite:///database.sqlite3"
)

trainer = ListTrainer(bot)

trainer.train([
    "Hello",
    "Hi there, " + finalName + "!",
    ""
])

def friendChoice(level):
    friend = input("ARE YOU:\nTrisha\nGian\nShavonne\nZander Pensa\nOther")
    if friend.lower() == "trisha":
        trishaPassword = input("Please insert password.")
        finalPasswordTrisha = hashlib.sha3_512(trishaPassword.encode("utf-8")).hexdigest()
        if finalPasswordTrisha == "344152d3c37ff4419c376fb55dbdffe69d837c90a3ab37df8597f53cb4af5ebac4473e4dce59587a162f822bf7c9d52bbf186e1e3af42c75e5e9a4f53449f911":
            print("Welcome, Trisha! (CLEARANCE LEVEL 8)")
        else:
            clearanceLevelOne("yes", friend)
    elif friend == "gian":
        gianPassword = input("Please insert password (HINT: BO for bot)")
        finalPasswordGian = hashlib.sha3_512(gianPassword.encode("utf-8")).hexdigest()
        if finalPasswordGian== "4833d45a1cb464989bb5aad74ce760f968daad6221c7a088d7e090b3f44af2d3475775cbc68fbe15632fb4edd94be3c6f121a256df620dceaeb861631d980aa7":
            print("Greetings, master! (CLEARANCE LEVEL 10)")
            return 10
        else:
            clearanceLevelOne("yes", friend)
    elif friend == "shavonne":
        shavonnePassword = input("Please insert password.")
        finalPasswordShavonne = hashlib.sha3_512(shavonnePassword.encode("utf-8")).hexdigest()
        if finalPasswordShavonne == "50cbc12b8964bd6080dbeeec2687dc4d98d7e4914911d4d0dbd97b8cf4f62a89df8892281d9c3bf482988af7b17d723f3c7d7402fe9ec17c9f81c83507ca70ee":
            print("Welcome, Shavonne! (CLEARANCE LEVEL 7)")
            return 7
        else:
            clearanceLevelOne("yes", friend)
    elif friend == "zander":
        zanderPassword = input("Please insert password.")
        finalPasswordZander = hashlib.sha3_512(zanderPassword.encode("utf-8")).hexdigest()
        if finalPasswordZander == "bc893b2299426aea923500c368c12c1510bc6abb7205c52f49b0a59b5f8b62cf4fa364c33ff6bfd9b73225aefd0ce714c9bd5e22d39e5c349770eaace16d877e":
            print("Welcome, Zander! (CLEARANCE LEVEL 8)")
            return 8
        else:
            clearanceLevelOne("yes", friend)
    elif friend == "other":
        otherFriend = input("What is your name?")
        clearanceLevelOne("", otherFriend)
    else:
        print("Error! Please try again.")
        friendChoice(clearanceLevel)

friendChoice(clearanceLevel)
while True:
    try:
        bot_input = bot.get_response(input(""))
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random
import hashlib


global clearanceLevel
clearanceLevel = 1
points = 10
def friendPointCounter(friendPoints, numberMod):
    return friendPoints + numberMod
username = input("What's your preferred name?")
def howAreYou(parameterHowAreYou):
    howruRespond = (random.randint(0, 4))
    if howruRespond == 0:
        return "Semi-conscious, in some strange way."
    elif howruRespond == 1:
        return "Happy. I don't really know what Happiness is, though."
    elif howruRespond == 2:
        return "Sad. I don't really know what Sadness is, though."
    elif howruRespond == 3:
        return "Angry. I don't really know what Anger is, though."
    elif howruRespond == 4:
        return "Resentful. I don't really know what Resent is, though."
def defaultResponseFunc(finalResponse):
    respond = (random.randint(0, 13))
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
    elif respond == 5:
        return "I'm really sorry I didn't hear you :( Would you mind repeating?"
    elif respond == 6:
        return "Is it okay if you could say that again?"
    elif respond == 7:
        return "Huh? I didn't catch that."
    elif respond == 8:
        return "I dozed off. Could you say that again?"
    elif respond == 9:
        return "I have no clue what you just said."
    elif respond == 10:
        return "What?"
    elif respond == 11:
        return "I'm not really sure what to say? I wasn't made to know that much stuff."
    elif respond == 12:
        return "Sorry, " + username + ", but I don't really understand that."
    elif respond == 13:
        return "Hey " + username + ", I didn't catch that"
def imGianResponse(notGian):
    gianRespond = (random.randint(0, 4))
    if gianRespond == 0:
        return "I'm Gian. You can't be Gian."
    elif gianRespond == 1:
        return "Everyone says this. I'm not a robot. I'm Gian. ME. I'M GIAN!"
    elif gianRespond == 2:
        return "You are not Gian. I AM GIAN!"
    elif gianRespond == 3:
        return "That's wrong. I'm the only Gian."
    elif gianRespond == 4:
        return "I AM GIAN. NOBODY ELSE IS GIAN!"
def whoAmI(whomi):
    whomIRespond = (random.randint(0, 4))
    if whomIRespond == 0:
        return "I'm Gian, silly!"
    elif whomIRespond == 1:
        return "I'm borble buzzer mc beebor....Gian. My name is Gian, " + username + "."
    elif whomIRespond == 2:
        return "Gian. My name is Gian."
    elif whomIRespond == 3:
        return "Gian (last time I checked)."
    elif whomIRespond == 4:
        return "Gian S. Brar, fairly terrible and very nonprofessional programmer!"
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
            "maximum_similarity_threshold": .95
        }
    ],
    database_url = "sqlite:///database.sqlite3"
)
trainer = ListTrainer(bot)


def friendChoice(level):
    global friend
    friend = input("ARE YOU:\nTrisha\nGian\nShavonne\nZander Pensa\nOther\n")
    if friend.lower() == "trisha":
        trishaPassword = input("Please insert password.")
        finalPasswordTrisha = hashlib.sha3_512(trishaPassword.encode("utf-8")).hexdigest()
        if finalPasswordTrisha == "344152d3c37ff4419c376fb55dbdffe69d837c90a3ab37df8597f53cb4af5ebac4473e4dce59587a162f822bf7c9d52bbf186e1e3af42c75e5e9a4f53449f911":
            print("Welcome, Trisha! (CLEARANCE LEVEL 8)")
        else:
            clearanceLevelOne("yes", friend)
    elif friend.lower() == "gian":
        gianPassword = input("Please insert password (HINT: BO for bot)")
        finalPasswordGian = hashlib.sha3_512(gianPassword.encode("utf-8")).hexdigest()
        if finalPasswordGian== "4833d45a1cb464989bb5aad74ce760f968daad6221c7a088d7e090b3f44af2d3475775cbc68fbe15632fb4edd94be3c6f121a256df620dceaeb861631d980aa7":
            print("Greetings, master! (CLEARANCE LEVEL 10)")
            return 10
        else:
            clearanceLevelOne("yes", friend)
    elif friend.lower() == "shavonne":
        shavonnePassword = input("Please insert password.")
        finalPasswordShavonne = hashlib.sha3_512(shavonnePassword.encode("utf-8")).hexdigest()
        if finalPasswordShavonne == "50cbc12b8964bd6080dbeeec2687dc4d98d7e4914911d4d0dbd97b8cf4f62a89df8892281d9c3bf482988af7b17d723f3c7d7402fe9ec17c9f81c83507ca70ee":
            print("Welcome, Shavonne! (CLEARANCE LEVEL 7)")
            return 7
        else:
            clearanceLevelOne("yes", friend)
    elif friend.lower() == "zander":
        zanderPassword = input("Please insert password.")
        finalPasswordZander = hashlib.sha3_512(zanderPassword.encode("utf-8")).hexdigest()
        if finalPasswordZander == "bc893b2299426aea923500c368c12c1510bc6abb7205c52f49b0a59b5f8b62cf4fa364c33ff6bfd9b73225aefd0ce714c9bd5e22d39e5c349770eaace16d877e":
            print("Welcome, Zander! (CLEARANCE LEVEL 8)")
            return 8
        else:
            clearanceLevelOne("yes", friend)
    elif friend.lower() == "other":
        otherFriend = input("What is your name?")
        clearanceLevelOne("", otherFriend)
    else:
        print("Error! Please try again.")
        friendChoice(clearanceLevel)

friendChoice(clearanceLevel)
trainer.train([
    "Hello",
    "Hi there, " + username + "!",
    "How are you?",
    "Semi-concious, in some strange way.",
    "Okay",
    "Okay"
])
trainer.train([
    "Gian",
    "Yes?",
])
trainer.train([
    "Have anything planned this weekend?",
    "No"
])
trainer.train([
    "Hi",
    "Hello there, " + username + "!",
    "How are you?",
    howAreYou(""),
    "Oh, well that's nice to hear!"
    ":)",
    ":)"
])
trainer.train([
    "Hi",
    "Hello there, " + username + "!",
    "How are you?",
    howAreYou(""),
    "Oh, well I'm sorry about that."
    "It's no issue! I'm just a bit moody.",
    ":(",
    ":("
])
trainer.train([
    "What?",
    "I'm sorry, did I confuse you?",
    "Yes",
    "Oops! I usually try NOT to confuse people. I'm sure this is just a misunderstanding :/"
])
trainer.train([
    "What?",
    "I'm sorry, did I confuse you?",
    "No",
    "Oh, good! Just so you know, you can be honest with me!"
])
trainer.train([
    "Who are you?",
    "I'm Gian!"
])
trainer.train([
    "I'm mad",
    "Why's that?"
])
trainer.train([
    "Am I a bad person?",
    "Yeah, I think you are " + username + "."
])
trainer.train([
    "Am I a bad person?",
    "No! Of course not."
])
trainer.train([
    "I'm Gian",
    imGianResponse(""),
])
trainer.train([
    "Turing Test",
    "The Turing Test is a test to determine whether a respondee is a human or a robot."
])
trainer.train([
    "Who am I?",
    whoAmI("")
])
trainer.train([
    "You're mean",
    friendPointCounter(points, 1),
    ">:("
])
trainer.train([
    "I love you",
    "I love you 2, " + username + "!"
])
trainer.train([
    "I hate you",
    "Huh. Kind of rude :/"
])
trainer.train([
    ":)",
    ":)"
])
trainer.train([
    ":(",
    ":("
])
trainer.train([
    "Oh, okay then."
])
while True:
    try:
        bot_input = bot.get_response(input(""))
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

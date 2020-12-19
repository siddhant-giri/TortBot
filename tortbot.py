
from flask import Flask, render_template, request, redirect, url_for
from chatterbot import ChatBot


from chatterbot.conversation import Statement 
from chatterbot.response_selection import get_random_response





app = Flask(__name__)

bot = ChatBot(
    "Tortbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
                 logic_adapters=[
       'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }

    ],
    database_uri='sqlite:///database.db'
)






from chatterbot.trainers import ListTrainer
trainer = ListTrainer(bot)



training_data_personal = open('training_data/data.txt').read().splitlines()
training_badwords = open('training_data/badwords.txt').read().splitlines()
training_greet = open('training_data/greet.txt').read().splitlines()
training_register = open('training_data/register.txt').read().splitlines()
training_goodbye = open('training_data/goodbye.txt').read().splitlines()




trainer.train(training_data_personal)
trainer.train(training_badwords)
trainer.train(training_greet)
trainer.train(training_register)
trainer.train(training_goodbye)










trainer.train([
    "register fir", "Sure, follow along with me" 
])


trainer.train([
	"rape","Rape is a type of sexual assault usually involving sexual intercourse or other forms of sexual penetration carried out against a person without that person's consent. The act may be carried out by physical force, coercion, abuse of authority, or against a person who is incapable of giving valid consent, such as one who is unconscious, incapacitated, has an intellectual disability or is below the legal age of consent. The term rape is sometimes used interchangeably with the term sexual assault"

	])


trainer.train([
	"phishing","Phishing is a type of fraud that involves stealing personal information such as Customer ID, IPIN, Credit/Debit Card number, Card expiry date, CVV number, etc. through emails that appear to be from a legitimate source."

	])

trainer.train([
"assault","Sexual assault is an act in which a person intentionally sexually touches another person without that person's consent, or coerces or physically forces a person to engage in a sexual act against their will"
	])

trainer.train([
"robbery","Theft by force. NOTE: this is also considered a personal crime since it results in physical and mental harm"
	])


trainer.train([
   "fire brigade number","Please call 101","fire number","Please call 101","fire department number","Please call 101","call fire department","Please call 101","what is the fire departmentt number","Please call 101"  
])
trainer.train([
    "what is the helpline number","Please call 100","helpline number","Please call 100","helpline no.","Please call 100","police number","Please call 100", "police no.","Please call 100","call police","Please call 100"
])
trainer.train([
    "ambulance number","Please call 108","ambulance call","Please call 108","call ambulance","Please call 108","call hopital","Please call 108","what is the ambulance number","Please call 108"
])
trainer.train([
   "what is the women helpline number","Please call 1090","what is the women's helpline number","Please call 1090","helpline no. for women","Please call 1090","call women's helpline","Please call 1090","women's helpline contact number","Please call 1090"  
])
trainer.train([
  "what is the control room number","Please call 1090","control room number","Please call 1090","control room no.","Please call 1090","call control room","Please call 1090"  
])



# from chatterbot.trainers import ChatterBotCorpusTrainer
# trainer_corpus = ChatterBotCorpusTrainer(bot)
# trainer_corpus.train(
#     'chatterbot.corpus.english'
# )


@app.route("/")
def home():
	return render_template("home.html")

@app.route("/authentication")
def login():
    return render_template("authentication.html")   


@app.route("/tortbot")
def index():
    return render_template("index.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/confirmlogout")
def confirmlogout():
    return render_template("adminlogout.html")    


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
 

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    crimereg = str(bot.get_response(userText))
    print('Confidence Value : ',bot.get_response(userText).confidence)
    if crimereg == 'Sure, follow along with me' or crimereg == "sure, follow me":
        return redirect(url_for('register'))
    return str(bot.get_response(userText))





@app.route("/register")
def register():
    return render_template("link.html")  

@app.route("/chatform")
def chatform():
    return render_template("chatform.html")        

if __name__ == "__main__":
    app.run(debug = True)
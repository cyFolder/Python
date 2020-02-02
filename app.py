from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer #Trainer Lib
import os

app = Flask(__name__)



#Create the Chatbot
GreetingBot = ChatBot('Test1', storage_adapter="chatterbot.storage.SQLStorageAdapter",
                        preprocessors=['chatterbot.preprocessors.clean_whitespace'],
				logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        } 
    ],
    trainer='chatterbot.trainers.ListTrainer'
	)
QuestionaireBot = ChatBot('Test2', storage_adapter="chatterbot.storage.SQLStorageAdapter",
                        preprocessors=['chatterbot.preprocessors.clean_whitespace'],
				logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        } 
    ],
    trainer='chatterbot.trainers.ListTrainer'
	)
AdvisorBot = ChatBot('Test3', storage_adapter="chatterbot.storage.SQLStorageAdapter",
                        preprocessors=['chatterbot.preprocessors.clean_whitespace'],
				logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        } 
    ],
    trainer='chatterbot.trainers.ListTrainer'
	)


#Set the trainer
GreetingBot.set_trainer(ListTrainer)
QuestionaireBot.set_trainer(ListTrainer)
AdvisorBot.set_trainer(ListTrainer)

#Constant
Counter = 0;
Score = 0

"""
for _file in os.listdir('Diabetes Dialog'):
	#Read Training Data
	Greeting = open('Diabetes Dialog/Greeting.txt', 'r' ).readlines()	
	Questionaire = open('Diabetes Dialog/Questionaire.txt', 'r' ).readlines()
	Advises = open('Diabetes Dialog/Advises.txt', 'r' ).readlines()
	
	#Train bot
	GreetingBot.train(Greeting)
	QuestionaireBot.train(Questionaire)
	AdvisorBot.train(Advises)
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(GreetingBot.get_response(userText))


if __name__ == "__main__":
    app.run()
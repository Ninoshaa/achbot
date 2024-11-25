# achbot

Installation

1. Clone the Repository
Grab the code before it disappears into the void like your last hopeful attempt at getting your life together.

git clone https://github.com/Ninoshaa/achbott.git
cd achbott
2. Create and Activate a Virtual Environment
You might want to make sure you’re living in a parallel universe where your dependencies don't conflict:

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
3. Install Dependencies
Because you definitely need these to keep this thing running:

pip install -r requirements.txt
4. Install Rasa
AchBot is built using Rasa. Why? Because even bots need purpose in this dark world.

pip install rasa
Setting Up AchBot

1. Train the Model
Train AchBot. You might not be training for success, but hey, it’s better than just existing.

rasa train
2. Run the Rasa Server
Run the server and let AchBot start doing its thing—who knows what that thing is? Maybe it’s laughing at you. Maybe it’s plotting your demise.

rasa run --enable-api
3. Run Custom Actions Server
If you want AchBot to send you a GIF to remind you of your work (or just to make you question your life), run this:

rasa run actions
Bot Behavior

Intents:
go_out: AchBot tries to convince you to go out. Don’t do it. It’s just another way for life to disappoint you.
calling: Got a call? AchBot gives you a phone sound effect—because the future is all about tech illusions.
work: Ask AchBot about work, and it will send you a GIF of someone drowning in spreadsheets. Enjoy.
whatsup: AchBot will ask you how you’re doing. It won’t care, but at least it asked.
dog: Because even in the darkest of times, dogs are still cute (unless you're a cat person, in which case, you're probably beyond saving).
Jokes & Insults:
joke: "Why don't skeletons fight each other? Because they lack the guts to face the horror of existence!"
insult: AchBot will insult you, not because it’s evil, but because it’s more fun to watch you squirm. For example: “You're not a failure... you’re just an underachiever in disguise.”
Configuration Files

domain.yml
Defines the intents, responses, and slots. It’s where we pretend we care about your emotions... but we both know that’s not true.

nlu.yml
This is how AchBot understands your cries for help and responds with dark humor. Not that you’ll ever get a real answer.

stories.yml
Contains the endless loops of conversations. No matter how many times you ask AchBot something, the answers will always be the same — because life doesn’t change. Neither does AchBot.

actions.py
Handles all the weird, twisted things AchBot might do when it’s bored. Like sending you gifs that make you question your life choices.

Development and Contributions

Like to join the existential void that is AchBot? Fork the repo and contribute. Just know, once you’re in, you can never truly escape.

Fork the repository (or don’t, no one cares).
Clone your fork (but, really, what’s the point?).
Create a new branch for your hopeless feature or bug fix.
Commit your changes and push them to your fork.
Open a pull request — or don’t. We’re all just staring into the void anyway.
License

This project is licensed under the MIT License — because nothing really matters in the end.

Contact AchBot

Want to talk to AchBot? Sure. It’ll probably insult you, but go ahead. We’re all going to the same place anyway.

Special Thanks
Rasa for creating a tool that lets us pretend we care about bots.
You for being here, reading this, and adding some meaning to AchBot’s existence (even if it’s just for a few minutes).
Hope this fits the bill! It has the dark humor you were looking for, but please remember to use it wisely — not everyone might appreciate the sarcastic tone. 😅 Let me know if you need any tweaks or more laughs!

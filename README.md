AchBot: The Digital Dumpster Fire

Welcome to AchBot, the chatbot equivalent of a potato powered by wishful thinking. Modeled after the most stunning example of human ineptitude, AchBot exists not to make your life easier, but to remind you just how much worse it could be.

Why AchBot?

AchBot was painstakingly designed to replicate the "charm" of its human inspiration—a beacon of confusion and bad decisions. If you’ve ever wondered what it’s like to argue with a poorly informed parrot, you’re in for a treat.

Installation

AchBot requires a setup process because, just like its creator, it doesn’t know how to make things easy.

Clone the Repository
Grab the code. Or don’t. AchBot won’t care, and neither should you.
git clone https://github.com/Ninoshaa/achbott.git  
cd achbott  
Create and Activate a Virtual Environment
Segregate AchBot’s mess
python -m venv venv  
source venv/bin/activate  # On macOS/Linux  
venv\Scripts\activate     # On Windows  
Install Dependencies
Because AchBot doesn’t come prepared for anything—just like the person it’s modeled on.
pip install -r requirements.txt  
Install Rasa
Rasa powers AchBot because even disasters need a foundation.
pip install rasa  
Setting Up AchBot

Train the Model
Teaching AchBot is like teaching a rock to swim—it’s technically possible, but why bother?
rasa train  
Run the Rasa Server
Fire up the server to unleash AchBot’s unique brand of incompetence.
rasa run --enable-api  
Run Custom Actions
If you want AchBot to "help" you by sending unrelated GIFs or nonsense responses, enable custom actions:
rasa run actions  
Bot Behavior

AchBot has a variety of "skills"—if you can call them that:

go_out: Attempts to suggest plans but sounds like it hasn’t been outside in years.
calling: Plays phone sounds because actual communication is beyond its capacity.
work: Sends a GIF that vaguely mocks your career while reminding you AchBot doesn’t have one.
whatsup: Pretends to care about your life with generic questions like “რას შვები?” Spoiler: it doesn’t care.
dog: AchBot acknowledges the existence of dogs and loves them but lies that he hates them.
Configuration Files

domain.yml
Contains all the responses AchBot will botch when trying to hold a conversation.
nlu.yml
Teaches AchBot to understand your input. Results may vary (and by "vary," we mean "fail").
stories.yml
Where AchBot’s decision-making process (or lack thereof) is outlined.
actions.py
The code responsible for AchBot’s special brand of uselessness.
Development and Contributions

Want to improve AchBot? Good luck. Fork the repository, clone it, and start fixing this train wreck:

Fork it (if your pride allows).
Clone your fork:
git clone https://github.com/YOUR-USERNAME/achbott.git  
Make a branch and start crying:
git checkout -b some-hopeless-feature  
License

Licensed under the MIT License. Use at your own risk—and prepare for disappointment.

Contact AchBot

Talk to AchBot if you enjoy the feeling of shouting into the void. Or don’t. It’s all the same to this glorified paperweight.

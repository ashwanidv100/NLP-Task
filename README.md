# NLP-Task
## NLP Python Task </br>
- Set up a basic Flask server which has 1 endpoint called 'processText'
- 'processText' will be a GET request that will accept a 'text' parameter
- The text passed via GET will be processed via a natural language processing python library
- It is up to you to find and select 1 or more python libraries which are capable of natural language processing
- Keep configuration file instead of hard coding any parameters required to run the program.</br>
## The NLP to do the following :
- [ ] Perform basic sentiment analysis (shows if the text content is positive, neutral, negative) 
- [ ] Tag blacklisted words (example if "emergency" is blacklisted the text "Help this is an emergency" would tag the word and position of emergency). You can set up a config file for blacklisted words.
- [ ] The GET request will process the text and return a JSON object with fields like sentimentAnalysis and taggedWords
- [ ] Host the project on Heroku.

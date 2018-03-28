Description of model mechanics can be found in this google doc: https://docs.google.com/document/d/162qBuNkHv4L_qQShWwn8UYWsveY0C1g3cmckWGQUr9k/edit?usp=sharing

How to run model:

1. Download all files to local machine
2. Navigate in terminal to server folder in app folder, then run "pip install -r requirements.txt" to set up the python side of things. Then run "export FLASK_APP=server.py", then "flask run", and the back end should be up and running.
4. Navigate in a different terminal window to the client folder, run "npm install", and then "npm start", and browswer window should open with the app running. 
5. Click "Run Model" to run the model to populate the charts with the output
6. Clicking the "Run Model" button again will re-run the model and produce new chart data (randomness built into the model means that a new run will have different results without modifying the input parameters).

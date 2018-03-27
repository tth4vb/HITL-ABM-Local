# HITL-ABM-Local

Description of model mechanics can be found in this google doc: https://docs.google.com/document/d/162qBuNkHv4L_qQShWwn8UYWsveY0C1g3cmckWGQUr9k/edit?usp=sharing

How to run model:

1. Download all files in fullstack_template to local machine
2. In the terminal, change directory to the fullstack_viz folder within the fullstack_template folder
2. First, we need to build the React front end, which is locacted in the static folder - navigate into that folder in the terminal and then run the command "npm run watch"...this build the front end.
3. Then, to actually run the whole app, we need to launch the flask (back end) server. This is done by first navigating to the server folder in the terminal (open a new terminal window to do this so that the React end is still running) and then running the following 2 commands in succession: "export FLASK_APP=server.py", and then "flask run".
4. After running those commands, the commnand line should verify the server is running locally at the following address: http://127.0.0.1:5000/
5. Open a browser window and paste the above address into it, and the app should load in that window.
6. Click "Run Model" to run the model to populate the charts with the output
7. Clicking the "Run Model" button again will re-run the model and produce new chart data (randomness built into the model means that a new run will have different results without modifying the input parameters).


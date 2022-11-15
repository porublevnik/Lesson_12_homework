from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from main.views import main
from loader.views import loader


app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(loader)


app.run()


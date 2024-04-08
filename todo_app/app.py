from flask import Flask, render_template, redirect, request
 
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item
 
app = Flask(__name__)
app.config.from_object(Config())
 
 
@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', my_items = items)
 
@app.route('/add_new_items', methods=['POST'])
def add_new_item():
    new_item_title = request.form.get('title')
    add_item (new_item_title)
    return redirect('/')


    

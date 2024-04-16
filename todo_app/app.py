from flask import Flask, render_template, redirect, request
 
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item, complete_item
def create_app ():
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

    @app.route('/complete', methods = ["POST"])
    def complete():
        id_to_complete = request.form.get('id')
        complete_item(id_to_complete)
        return redirect('/')

    return app        

    

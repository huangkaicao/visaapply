from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

script_directory = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_directory, "json", "data.json")

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        updated_data = request.form.to_dict()
        with open(data_path, 'r') as file:
            data = json.load(file)
        for form_key, value in updated_data.items():
            keys = form_key.split('.')
            if len(keys) == 2:
                category, key = keys
                if category in data and key in data[category]:
                    data[category][key] = value
        with open(data_path, 'w') as file:
            json.dump(data, file, indent=4)
        return redirect(url_for('form'))
    else:
        with open(data_path, 'r') as file:
            data = json.load(file)
        return render_template('form.html', data=data)


app.run()

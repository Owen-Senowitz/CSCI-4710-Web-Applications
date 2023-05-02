from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import date

app = Flask(__name__)


@app.route('/')
def home():
    with open('blog_data.json', 'r') as f:
        data = json.load(f)
    return render_template('home.html', data=data)

@app.route('/Final Project/templates/teaminfo.html')
def teaminfo():
    return render_template('teaminfo.html')

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        # Load the current data from the JSON file
        with open('blog_data.json', 'r') as f:
            data = json.load(f)

        # Add the new post to the list
        new_post = {
            'title': request.form['title'],
            'content': request.form['content'],
            'date': date.today().strftime('%Y-%m-%d')
        }
        data.append(new_post)

        # Write the updated data back to the JSON file
        with open('blog_data.json', 'w') as f:
            json.dump(data, f)

        return redirect('/')
    else:
        return render_template('new_post.html')


if __name__ == '__main__':
    app.run(debug=True)

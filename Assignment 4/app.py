from flask import Flask, render_template, request, redirect
from forms import ClassmateForm, DataProcessingForm
from controllers import process_data, plot_data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a_random_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ClassmateForm()
    dp_form = DataProcessingForm()

    if form.validate_on_submit():
        process_data(form)
        return redirect('/')

    if request.method == 'POST' and dp_form.validate():
        plot_data(dp_form.data_processing_method.data)

    return render_template('index.html', form=form, dp_form=dp_form)

if __name__ == '__main__':
    app.run(debug=True)

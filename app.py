from flask import Flask, render_template, request, redirect

app = Flask(__name__)

feedback_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['feedback']

        feedback_list.append({
            "name": name,
            "feedback": feedback
        })

        return redirect('/')

    return render_template('index.html', feedbacks=feedback_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
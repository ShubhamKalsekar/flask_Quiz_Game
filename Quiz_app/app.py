from flask import Flask, render_template, request

app = Flask(__name__)

# Display the home page
@app.route('/')
def home():
    return render_template('home.html')
@app.route("/quiz")
def index():
    return render_template('index.html')

# Handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    scored = 0

    # Retrieve the answers submitted by the user
    answers = {
        
        'q1': request.form['q1'],
        'q2': request.form['q2'],
        'q3': request.form['q3'],
        'q4': request.form['q4'],
        'q5': request.form['q5']
    }

    # Check the answers and update the score
    if answers['q1'].lower() == 'central processing unit':
        score += 1
    else:
        scored += 1

    if answers['q2'].lower() == 'graphic processing unit':
        score += 1
    else:
        scored += 1

    if answers['q3'].lower() == 'sundar pichai':
        score += 1
    else:
        scored += 1

    if answers['q4'].lower() == 'satya nadella':
        score += 1
    else:
        scored += 1

    if answers['q5'].lower() == 'random access memory':
        score += 1
    else:
        scored += 1

    # Calculate the percentage
    percentage = (score / 5) * 100

    # Display the result page
    return render_template('result.html', score=score, scored=scored, percentage=percentage)


# Handle the exit route
@app.route('/exit')
def exit_quiz():
    return render_template('exit.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')

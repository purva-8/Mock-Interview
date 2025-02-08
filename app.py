from flask import Flask, request, render_template, redirect, url_for, session
import google.generativeai as genai
import os

app = Flask(__name__)
app.secret_key="Panskbd"

gemini = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=gemini)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_questions(job_description, candidate_profile):
    """Generates interview questions based on job description and candidate profile."""
    prompt = (
        "Based on the following job description and candidate profile, generate interview questions:\n\n"
        f"Job Description: {job_description}\n"
        f"Candidate Profile: {candidate_profile}\n\n"
        "Only give 5 questions"
        "START WITH THE QUESTIONS DIRECTLY AND DONT GIVE YOUR INSIGHTS ON THE QUESTION"
    )
    inputs = model.generate_content(prompt)
    questions = inputs.text.split('\n')  # Assuming questions are separated by new lines
    return questions

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        job_description = request.form['job_description']
        candidate_profile = request.form['candidate_profile']

        if job_description and candidate_profile:
            questions = generate_questions(job_description, candidate_profile)
            session['questions'] = questions
            session['question_index'] = 0
            return redirect(url_for('interview'))
        else:
            return "Please enter both the job description and candidate profile.", 400

    return render_template('index.html')

@app.route('/interview', methods=['GET', 'POST'])
def interview():
    questions = session.get('questions', [])
    question_index = session.get('question_index', 0)

    if request.method == 'POST':
        timeout = request.form.get('timeout') == "true"
        if timeout or 'next' in request.form:
            if question_index < len(questions) - 1:
                session['question_index'] += 1
                return redirect(url_for('interview'))
            else:
                return "End of questions.", 200

    if questions:
        if question_index < len(questions):
            question = questions[question_index]
            return render_template('interview.html', question=question)
        else:
            return "No more questions.", 200
    else:
        return "No questions generated. Please try again.", 400


if __name__ == "__main__":
    app.run(debug=True)

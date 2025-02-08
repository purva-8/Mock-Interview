# AI-Powered Interview Question Generator

## Overview

This project is a Flask-based web application that generates AI-powered interview questions based on a given job description and candidate profile. It leverages Google's Gemini AI to create relevant questions, helping recruiters conduct structured interviews.

## Features

- Users input a job description and candidate profile.
- AI generates 5 interview questions based on the inputs.
- Questions are presented one by one in an interactive interview format.
- Users can navigate through the questions.
- A session-based approach ensures state management during the interview process.

## Technologies Used

- **Python** (Flask)
- **Google Gemini AI API**
- **HTML/CSS** (for templates)
- **Session Management** (Flask sessions)

## Installation & Setup

### Prerequisites

- Python 3.x installed
- A valid Google Gemini AI API key

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repository/interview-ai.git
   cd interview-ai
   ```
2. Install dependencies:
   ```sh
   pip install flask google-generativeai
   ```
3. Run the application:
   ```sh
   python app.py
   ```

## Usage

1. Open the application in the browser.
2. Enter the job description and candidate profile.
3. Click "Generate Questions" to start the interview process.
4. Navigate through the generated questions.

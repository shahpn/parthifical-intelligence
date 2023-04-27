from urllib.request import urlopen
import re

import numpy as np
import tensorflow as tf
import wikipedia
import win32com.client as wincl
from bs4 import BeautifulSoup
from clint.textui import progress
from ecapture import ecapture as ec
from flask import Flask, jsonify, request
from flask.helpers import send_from_directory
from gtts import gTTS

# import lionpath class
# from integrations.lionpath import Lionpath
from integrations.canvas import CanvasClass
from integrations.bulletin import Bulletin


app = Flask(__name__)

# lp = Lionpath()
cvs = CanvasClass()
bp = Bulletin()

# Define the categories we want to classify user input into
categories = ['course', 'history', 'location', 'advising']

# Define the training data for each category
course_data = ["What is CMPSC 430 about?", "What's the description for CMPSC 473?", "Tell me about CMPSC 476", "What is CMPSC 483 about?", "What are the prerequisites for CMPSC 392?", "What topics are covered in CMPSC 485?", "Can you give me more information about CMPSC 487?", "What is IST 402 about?", "What's the description for IST 441?", "Tell me about IST 451", "What is IST 462 about?", "What topics are covered in IST 471?", "Can you give me more information about IST 481?", "What is the textbook for CMPSC 121?", "Can you tell me about the workload for CMPSC 132?", "What programming languages are used in CMPSC 150?", "What's the grading policy for CMPSC 201?", "What is the structure of CMPSC 221?", "What kind of assignments are given in CMPSC 240?", "Can you give me more information about CMPSC 261?", "What are the prerequisites for CMPSC 270?", "Tell me about the content covered in CMPSC 271", "What is the focus of CMPSC 280?", "What's the description for CMPSC 312?", "Can you give me more information about CMPSC 320?", "What is the workload like for CMPSC 321?", "What are the prerequisites for CMPSC 331?",
               "Tell me about the exams in CMPSC 332", "What kind of programming assignments are given in CMPSC 335?", "What's the course schedule for CMPSC 360?", "Can you give me more information about CMPSC 365?", "What is the focus of CMPSC 370?", "What is the workload like for CMPSC 375?", "What are the prerequisites for CMPSC 377?", "Tell me about the group project in CMPSC 380", "What's the description for CMPSC 381?", "What kind of software development is covered in CMPSC 390D?", "What is the focus of CMPSC 391?", "Can you give me more information about CMPSC 392?", "What's the structure of CMPSC 395?", "Tell me about the course objectives in CMPSC 398", "What are the prerequisites for CMPSC 401?", "What's the course schedule for CMPSC 402?", "What is the workload like for CMPSC 403?", "What's the description for CMPSC 405?", "Can you give me more information about CMPSC 406?", "What kind of projects are given in CMPSC 407?", "What are the prerequisites for CMPSC 408?", "Tell me about the group project in CMPSC 412", "What is the focus of CMPSC 416?", "What is CMPSC 331", "Is CMPSC 412 required for the Computer Science major", "What is the textbook for CMPSC 461?", "Tell me about the course structure in CMPSC 464", "What topics are covered in CMPSC 465?", "What are the prerequisites for CMPSC 466?", "What kind of assignments are given in CMPSC 467?", "Can you give me more information about CMPSC 468?", "What is the focus of CMPSC 471?", "What's the description for CMPSC 474?", "Tell me about the exams in CMPSC 475", "What kind of projects are given in CMPSC 477?"]
history_data = ["When did the Computer Science Degree become part of the University?", "When was the University founded?", "Can you tell me about the history of the university?", "Who was the first president of the university?", "What is the oldest building on campus?", "Where can I find the statue of the founder of the university?", "What is the significance of the clock tower on campus?", "Can you tell me about the history of the library?", "What is the history of the athletic programs at the university?", "Where can I find information about notable alumni of the university?", "What is the story behind the mural in the student center?", "Can you tell me about the history of the art department at the university?", "Where can I find information about the university's involvement in the Civil Rights Movement?", "What is the history of the theater program at the university?", "Can you tell me about the history of the university's mascot?", "Where can I find information about the history of the university's student government?", "What is the significance of the campus fountain?", "Can you tell me about the history of the university's international programs?", "Where can I find information about the university's involvement in environmental sustainability?", "What is the history of the university's community service programs?", "Can you tell me about the history of the university's student newspaper?", "Where can I find information about the university's research initiatives?", "What is the history of the university's architecture?", "Can you tell me about the history of the university's founding fathers?", "Where can I find information about the university's participation in sports championships?", "What is the story behind the university's alma mater?", "Can you tell me about the history of the university's academic honors programs?",
                "Where can I find information about the university's involvement in the Vietnam War?", "What is the history of the university's Greek life?", "Can you tell me about the history of the university's diversity and inclusion initiatives?", "Where can I find information about the university's notable faculty members?", "What is the history of the university's mascot costume design?", "Can you tell me about the history of the university's journalism program?", "Where can I find information about the university's partnerships with other institutions?", "What is the history of the university's relationship with the local community?", "Can you tell me about the history of the university's music department?", "Where can I find information about the university's involvement in the women's rights movement?", "What is the history of the university's alumni association?", "Can you tell me about the history of the university's traditions?", "Where can I find information about the university's involvement in the arts?", "What is the history of the university's campus radio station?", "Can you tell me about the history of the university's language programs?", "Where can I find information about the university's involvement in international diplomacy?", "What is the history of the university's academic departments?", "Can you tell me about the history of the university's relationship with the military?", "Where can I find information about the university's involvement in the Civil War?", "What is the history of the university's community outreach programs?", "Can you tell me about the history of the university's mascot naming contest?", "Where can I find information about the university's involvement in social justice movements?", "What is the history of the university's alumni network?", "Can you tell me about the history of the university's graduate programs?", "Where can I find information about the university's campus sustainability initiatives?", "What is the history of the university's ROTC program?", "Can you tell me about the history of the university's online learning programs?", "Where can I find information about the university's relationship with local businesses?", "What is the history of the university's honors societies?", "Can you tell me about the history of the university's study abroad programs?", "What is the history of the university's foreign language requirement for graduation?", "What is the history of the university's student housing options?", "Can you tell me about the history of the university's alumni donations and fundraising efforts?"]
location_data = ["Where is the student center located?", "Can you tell me where the library is?", "I'm looking for the physics building, where is it?", "Where is the nearest coffee shop on campus?", "Can you direct me to the chemistry department?", "I need to find the registrar's office, where is it located?", "Can you tell me where the nearest bus stop is?", "Where can I find the biology lab?", "I'm trying to find the art building, where is it?", "Where is the gym located on campus?", "Can you help me find the bookstore?", "Where is the computer science department located?", "I'm looking for the history building, where is it?", "Can you direct me to the math department?", "Where can I find the music building?", "I need to find the health center, where is it located?", "Can you tell me where the nearest parking lot is?", "Where is the engineering building located?", "I'm trying to find the business school, where is it?", "Where is the dining hall on campus?", "Where is the language center located?", "Can you tell me where the theater department is?", "I need to find the psychology building, where is it located?", "Can you direct me to the student union?", "Where can I find the philosophy department?", "I'm trying to find the sociology building, where is it?",
                 "Where is the anthropology department located?", "Can you help me find the education building?", "Where is the nearest vending machine on campus?", "I'm looking for the geology building, where is it?", "Can you tell me where the language lab is located?", "Where is the architecture building on campus?", "I need to find the foreign language department, where is it located?", "Can you direct me to the physics lab?", "Where can I find the student services office?", "I'm trying to find the journalism department, where is it?", "Where is the nearest ATM on campus?", "Can you help me find the statistics department?", "Where is the environmental science building located?", "I need to find the astronomy building, where is it located?", "Can you tell me where the nearest restroom is?", "Where is the gender studies department on campus?", "I'm trying to find the engineering lab, where is it?", "Can you direct me to the political science building?", "Where can I find the dance department?", "I'm looking for the women's center, where is it located?", "Where is the nearest bus stop for the shuttle?", "Can you help me find the film studies building?", "Where is the physics department located?", "I need to find the nearest printer on campus.", "Where is the main administration building located on campus?", "Can you direct me to the nearest gym locker room?", "I'm looking for the campus bookstore, where can I find it?", "Where is the nearest food court located on campus?", "Can you tell me where the student health services are located?", "I need to find the chemistry lab, where is it located?", "Where is the nearest study lounge on campus?", "I'm trying to find the physics professor's office, can you help me?", "Where is the art gallery on campus?", "Can you direct me to the nearest student counseling center?"]
advising_data = ["Can you help me choose my classes for next semester?", "How do I get in touch with my academic advisor?", "When are office hours for Professor Johnson?", "Where can I find tutoring services for math?", "How do I schedule an appointment with the career center?", "Can you help me find a tutor for chemistry?", "Where can I find information about study abroad programs?", "How do I declare my major?", "Can you help me find resources for writing my thesis?", "Where can I find information about internships?", "How do I apply for scholarships?", "Can you tell me about the requirements for graduating with honors?", "Where can I find information about graduate programs?", "How do I find out about research opportunities?", "Can you help me find a summer job or internship?", "Where can I find information about studying abroad?", "How do I change my major?", "Can you tell me more about academic support services on campus?", "Where can I find information about career fairs?", "How do I find out about campus events and activities?", "What are the requirements for a double major?", "How do I declare or change my major/minor?", "Can you tell me about the honors program in computer science?", "What are the pre-requisites for graduate-level courses in computer science?", "How do I apply for an internship in the computer science department?", "Can you provide me with information on research opportunities in computer science?", "What is the process for getting academic credit for an independent study in computer science?", "How can I find a tutor for a particular computer science course?", "Can you tell me about the study abroad opportunities for computer science majors?",
                 "How do I apply for a co-op position in computer science?", "Can you provide information about scholarships available for computer science majors?", "What resources are available to help me plan my course schedule?", "Can you help me find information on graduate school opportunities in computer science?", "How can I get involved in a computer science club or organization?", "Can you provide me with information on the availability of career services for computer science majors?", "How do I request a letter of recommendation from a computer science professor?", "Can you tell me about the requirements for a minor in computer science?", "How can I get involved in undergraduate research in computer science?", "Can you provide me with information about the academic integrity policy in the computer science department?", "What is the process for appealing a grade in a computer science course?", "How do I register for a computer science course that is full?", "Can you provide me with information about the academic advising process for computer science majors?", "What is the process for applying for a teaching assistantship in computer science?", "Can you tell me about the process for applying to graduate school in computer science?", "What are the course requirements for graduation in computer science?", "How can I find out more about career opportunities in computer science?", "Can you provide me with information about the availability of tutoring services for computer science courses?", "What is the process for withdrawing from a computer science course?", "Can you tell me about the availability of summer courses in computer science?", "How can I get involved in community outreach programs in computer science?", "Can you tell me the email address for Professor Johnson?", "What are the office hours for Professor Smith and where is his/her office located?", "What is the degree and research specialization of Professor Lee?", "How can I schedule a meeting with Professor Martinez to discuss my project?", "Can you provide me with a list of professors in the computer science department?", "What are the research interests of Professor Wang in the artificial intelligence field?", "Can you give me the contact information for Professor Davis?", "What is the teaching style of Professor Ramirez in the software engineering course?", "Can you provide me with information on the office hours and location for Professor Kim?", "How do I find out more about the academic publications and research achievements of Professor Chen?"]

# Preprocess the training data by converting each word to a vector
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(course_data + history_data +
                       location_data + advising_data)
course_data = tokenizer.texts_to_sequences(course_data)
history_data = tokenizer.texts_to_sequences(history_data)
location_data = tokenizer.texts_to_sequences(location_data)
advising_data = tokenizer.texts_to_sequences(advising_data)

# Convert the lists of sequences to a 2D numpy array
course_data = tf.keras.preprocessing.sequence.pad_sequences(
    course_data, maxlen=60)
history_data = tf.keras.preprocessing.sequence.pad_sequences(
    history_data, maxlen=60)
location_data = tf.keras.preprocessing.sequence.pad_sequences(
    location_data, maxlen=60)
advising_data = tf.keras.preprocessing.sequence.pad_sequences(
    advising_data, maxlen=60)

# Define the neural network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(
        len(tokenizer.word_index)+1, 256, input_length=60),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(len(categories), activation='softmax'),
])

# Compile the model
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

# Train the model on the training data
X = np.concatenate(
    (course_data, history_data, location_data, advising_data), axis=0)
y = np.array([[1, 0, 0, 0]] * len(course_data) +
             [[0, 1, 0, 0]] * len(history_data) +
             [[0, 0, 1, 0]] * len(location_data) +
             [[0, 0, 0, 1]] * len(advising_data))
model.fit(X, y, epochs=100)

# model.save('../flask-server/models')


# Define a function to classify user input

def classify_input(input_text):
    # model = model.load_model('../flask-server/models')
    # tokenizer = model.tokenizer
    input_sequence = tokenizer.texts_to_sequences([input_text])
    input_sequence = tf.keras.preprocessing.sequence.pad_sequences(
        input_sequence, maxlen=60)
    category_index = np.argmax(model.predict(input_sequence))
    return categories[category_index]


# Test the function
# print(f"Courses: {len(course_data)} Data Elements")
# print(f"History: {len(history_data)} Data Elements")
# print(f"Location: {len(location_data)} Data Elements")
# print(f"Advising: {len(advising_data)} Data Elements")

# input_text = "Can you tell me about CMPSC 462"
# print(f"Input: {input_text}, Topic: {classify_input(input_text)}")  # Courses
# input_text = "When was the Rydal Building built?"
# print(f"Input: {input_text}, Topic: {classify_input(input_text)}")  # History
# input_text = "Where is the Amphitheater?"
# print(f"Input: {input_text}, Topic: {classify_input(input_text)}")  # Location
# input_text = "What is Professor Trofimoff's Email?"
# print(f"Input: {input_text}, Topic: {classify_input(input_text)}")  # Advising

# # piss
# print("test")


@app.route('/userInput', methods=['POST'])
def userInput():
    data = request.get_json()
    payload = data['payload']
    # print(classify_input(payload))
    if classify_input(payload) == 'course':
        course_matches = re.findall(r'(CMPSC|IST)\s?(\d{3})(w?)', payload, re.IGNORECASE)

        course_name = ""
        if course_matches and 'all' not in payload:
            course_name = [match[0].upper() + ' ' + match[1] + match[2] for match in course_matches]
            return cvs._get_assignments(f'{course_name[0]}')
        elif course_matches and 'all' in payload:
            course_name = [match[0].upper() + ' ' + match[1] + match[2] for match in course_matches]
            return cvs._get_all_assignments(f'{course_name[0]}')
        else:
            return "This chat bot is currently only optimized for CMPSC and IST class codes"
        
    elif classify_input(payload) == 'location':
        return bp._search_location()
    
    elif classify_input(payload) == 'advising':
        match = re.search(r'(?i)Professor\s(\w+)', payload)
        if match is not None:
            return bp._search_professor(payload)
        else:
            return "Please check your StarFish and/or LionPath for more information. Check out your major's academic plan on the bulletin"
        
    elif classify_input(payload) == 'history':
        return bp._search_history(payload)
        
        
    # return classify_input(payload)
		

@app.route('/get_assignments', methods=['POST'])
def get_assignment():
    return cvs._get_assignments('CMPSC 470')

@app.route('/get_all_assignments', methods=['POST'])
def get_all_assignments():
    return cvs._get_all_assignments('CMPSC 470')

@app.route('/get_courses', methods=['POST'])
def get_courses():
    return cvs._get_courses()
		
		
		
if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify, render_template
import json
  

	
app = Flask(__name__)
@app.route('/')	
def home():
	return  render_template('index.html')

@app.route('/api/experience', methods=['GET'])
def experience():
  # Opening JSON file
  with open('experience.json', 'r') as openfile:
      # Reading from json file
      json_object = json.load(openfile)
  return jsonify(json_object)

@app.route('/api/education', methods=['GET'])
def education():
  # Opening JSON file
  with open('education.json', 'r') as openfile:
      # Reading from json file
      json_object = json.load(openfile)
  return jsonify(json_object)

app.run(host='0.0.0.0', port=5000, debug=True)
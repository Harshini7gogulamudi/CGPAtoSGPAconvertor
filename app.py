from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_cgpa', methods=['POST'])
def calculate_cgpa():
    semester_sgpas = request.json.get('semester_sgpas')
    cgpa = 0.0
    total_credits = 0

    for semester, data in semester_sgpas.items():
        sgpa = data['sgpa']
        credits = data['credits']
        cgpa += sgpa * credits
        total_credits += credits

    cgpa /= total_credits
    return jsonify({'cgpa': cgpa})

if __name__ == '__main__':
    app.run(debug=True)

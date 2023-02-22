from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Shenzhen, China',
        'salary': 'RMB 100,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Bengalurum, Inda',
        'salary': 'Rs. 1,000,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 1,500,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Shanghai, China',
        'salary': '$ 120,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Webond')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)
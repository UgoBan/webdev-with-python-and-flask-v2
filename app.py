from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Regulatory Ecotoxicologist',
    'location': 'Berlin, Germany',
    'salary': 'EUR. 55,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Frankfurt, Germany',
    'salary': 'EUR. 50,000'
  },
  {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Munich, Germany',
    'salary': 'EUR. 46,000'
  },
  {
    'id': 4,
    'title': 'Frontend Developer',
    'location': 'Hamburg, Germany',
    'salary': 'EUR. 60,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs = JOBS, company_name = 'Banabas')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)
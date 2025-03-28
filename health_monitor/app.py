from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from monitor import check_all_services
from models import db, HealthRecord

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # Initialize the database with your app

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/health', methods=['GET'])
def health():
    """Returns current aggregated service status without logging history."""
    statuses = check_all_services(log=False)
    return jsonify(statuses)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    """Renders a dashboard displaying the latest health check records."""
    records = HealthRecord.query.order_by(HealthRecord.timestamp.desc()).limit(20).all()
    return render_template('dashboard.html', records=records)

@app.route('/frontend', methods=['GET'])
def frontend():
    """Serves a basic HTML page with a JavaScript-based UI."""
    return render_template('frontend.html')

def scheduled_health_check():
    with app.app_context():
        check_all_services(log=True)

# Configure Flask-APScheduler
class Config:
    SCHEDULER_API_ENABLED = True

app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

# Add the job via Flask-APScheduler (it automatically runs inside an app context)
scheduler.add_job(id='Health_Check', func=scheduled_health_check, trigger='interval', minutes=1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(50), nullable=False)
    status_code = db.Column(db.Integer)
    is_healthy = db.Column(db.Boolean, nullable=False)
    response_time = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<HealthRecord {self.service_name} - {self.is_healthy}>'
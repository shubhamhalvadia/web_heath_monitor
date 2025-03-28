# Web Health Monitor

**Web Health Monitor** is a lightweight, containerized SaaS monitoring project built with Flask. It periodically checks the health of dummy services, logs the results in a SQLite database, and displays real-time data through a web dashboard and a JavaScript-based frontend.

## Features

- **Periodic Health Checks:**  
  Uses Flask-APScheduler to run periodic health checks on dummy services.
  
- **Health Logging:**  
  Stores each health check result in a SQLite database using Flask-SQLAlchemy for historical tracking.
  
- **Web Dashboard:**  
  A simple dashboard displays the latest health records, including service status, response time, and timestamps.
  
- **Frontend UI:**  
  A user-friendly JavaScript-based UI provides a real-time view of service health status.
  
- **Containerization:**  
  All components (health monitor and dummy services) are containerized using Docker and orchestrated with Docker Compose.

## Technologies Used

- **Backend:** Python, Flask, Flask-SQLAlchemy, APScheduler, Flask-APScheduler, Requests
- **Database:** SQLite
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **Containerization:** Docker, Docker Compose

## Project Structure
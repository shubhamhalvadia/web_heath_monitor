import requests
from models import db, HealthRecord  # Import from models

def get_service_status(url: str, service_name: str) -> dict:
    """
    Pings the given URL and evaluates both the HTTP status code and JSON response.
    A service is considered healthy if it returns a 200 status code and "status" equals "healthy".
    """
    try:
        response = requests.get(url, timeout=3)
        data = response.json()
        is_healthy = (response.status_code == 200 and data.get("status") == "healthy")
        record = HealthRecord(
            service_name=service_name,
            status_code=response.status_code,
            is_healthy=is_healthy,
            response_time=response.elapsed.total_seconds()
        )
        return {
            "service_name": service_name,
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds(),
            "data": data,
            "is_healthy": is_healthy,
            "record": record
        }
    except requests.RequestException as e:
        record = HealthRecord(
            service_name=service_name,
            status_code=None,
            is_healthy=False,
            response_time=None
        )
        return {
            "service_name": service_name,
            "status_code": None,
            "error": str(e),
            "is_healthy": False,
            "record": record
        }

def check_all_services(log=False):
    """
    Checks the health of all configured services.
    If log is True, results are saved to the database.
    """
    # Define your service endpoints. For now, use placeholder URLs.
    services = {
        "dummy_service_a": "http://dummy_service_a:5000/health",
        "dummy_service_b": "http://dummy_service_b:5000/health"
    }
    statuses = {}
    for name, url in services.items():
        result = get_service_status(url, name)
        statuses[name] = {
            "status_code": result.get("status_code"),
            "is_healthy": result.get("is_healthy"),
            "response_time": result.get("response_time"),
            "data": result.get("data", {})
        }
        if log:
            db.session.add(result["record"])
    if log:
        db.session.commit()
    return statuses
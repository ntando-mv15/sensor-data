import requests
from datetime import datetime, timezone, timedelta

def fetch_temperature_from_box(box_id):
    url = f"https://api.opensensemap.org/boxes/{box_id}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        box_data = response.json()

        for sensor in box_data.get("sensors", []):
            if sensor.get("title") == "Temperatur":
                measurement = sensor.get("lastMeasurement")
                if measurement:
                    value = measurement.get("value")
                    created_at = measurement.get("createdAt")
                    if not value or not created_at:
                        return None

                    timestamp = datetime.strptime(
                        created_at, "%Y-%m-%dT%H:%M:%S.%fZ"
                    ).replace(tzinfo=timezone.utc)

                    if timestamp >= datetime.now(timezone.utc) - timedelta(hours=1):
                        return float(value)
    
    except Exception as e:
        print(f"Error fetching from {box_id}: {e}")
        return None

    return None
# Weather Assistant Workflow

A simple weather forecast workflow built in [Dify](https://cloud.dify.ai/app/5c5d7da0-e51c-476c-8f33-5b7de4488830/workflow). It takes a user-provided city name, converts it into geographical coordinates, fetches current weather data, and generates a formatted response using an LLM.

---

## 🚀 Overview

1. **User Input:** The user provides a city name (e.g., `"Mumbai"`).
2. **Geocoding:** Converts the city name into latitude and longitude coordinates via Open-Meteo's Geocoding API.
3. **Data Parsing:** A Python script parses the raw geocoding output and extracts numerical coordinates.
4. **Weather Retrieval:** Queries the Open-Meteo Forecast API using the extracted coordinates.
5. **LLM Formatting:** An LLM processes the raw weather metrics into a clean, human-readable summary.

---

## 🛠️ Workflow Steps

```
[START] ➔ [GEOCODING API] ➔ [CODE] ➔ [HTTP REQUEST] ➔ [LLM] ➔ [END]

```

* **`START`**: Captures the required input variable `City` (String).
* **`GEOCODING API`**:
* **Type:** HTTP Request (GET)
* **Endpoint:** `[https://geocoding-api.open-meteo.com/v1/search?name=](https://geocoding-api.open-meteo.com/v1/search?name=){{sys.query}}`
* **Purpose:** Searches for spatial coordinates for the requested location.


* **`CODE`**:
* **Type:** Python 3 Code Node
* **Input:** `body` (Mapped from `GEOCODING API` output string)
* **Output:** `lat` (Number), `lon` (Number)
* **Purpose:** Parses the raw JSON response to extract latitude and longitude. Safely falls back to `0.0, 0.0` if no matching location is found.


* **`HTTP REQUEST`**:
* **Type:** HTTP Request (GET)
* **Endpoint:** `[https://api.open-meteo.com/v1/forecast?latitude=](https://api.open-meteo.com/v1/forecast?latitude=){{#CODE.lat#}}&longitude={{#CODE.lon#}}&current_weather=true`
* **Purpose:** Fetches live weather data including temperature, humidity, and wind speed.


* **`LLM`**:
* **Model:** GPT-4 / Compatible LLM
* **Purpose:** Summarizes raw weather details into a clean final response.


* **`END`**: Returns the formatted output string to the user.

---

## 💻 Python Parsing Code (`CODE` Node)

```python
import json

def main(body: str) -> dict:
    # Handle string responses from HTTP node
    if isinstance(body, str):
        data = json.loads(body)
    else:
        data = body

    results = data.get('results', [])
    if results:
        return {
            'lat': results[0]['latitude'],
            'lon': results[0]['longitude']
        }
    
    # Default fallback coordinates
    return {'lat': 0.0, 'lon': 0.0}

```

---

## 📋 Example Output

```text
Location: Mumbai
Temperature: 26.8°C
Humidity: 82%
Wind Speed: 11.5 km/h

```


<img width="1365" height="628" alt="image" src="https://github.com/user-attachments/assets/9a618696-c860-4e2d-b970-3822bea83dd5" />

<img width="1361" height="632" alt="image" src="https://github.com/user-attachments/assets/e20b2a27-8348-47f8-9482-e3db72f62409" />



# Django WeatherApp

A simple weather application built with **Django** that allows users to add cities and view current weather 
information using the **OpenWeatherMap API**.

---

## Features

- Add cities to track their current weather.
- View temperature, description, and weather icon for each city.
- Delete cities from the list.
- Responsive UI using [Bulma](https://bulma.io/) CSS framework.
- Input validation (prevents duplicate or invalid cities).

---

## Technologies Used

- **Python** + **Django** – Backend framework
- **OpenWeatherMap API** – Real-time weather data
- **SQLite** – Local database (default Django)
- **HTML/CSS** + **Bulma** – Frontend styling
- **Requests** – HTTP calls to external API

---

## Project Structure

```
weatherapp/
    ├───weatherapp/       # Project settings
    │   ├───__init__.py
    │   ├───asgi.py
    │   ├───settings.py   # Django settings
    │   ├───urls.py       # Main URL routing
    │   └───wsgi.py
    ├───weather/          # Django app for weather functionality
    │   ├───migrations/
    │   │   └───__init__.py
    │   ├───templates/    # HTML template
    │   │   └───weather/
    │   │       └───weather.html
    │   ├───__init__.py
    │   ├───admin.py
    │   ├───apps.py
    │   ├───forms.py      # City input form
    │   ├───models.py     # City model
    │   ├───tests.py
    │   ├───urls.py       # App-specific URLs
    │   └───views.py      # Handles weather logic and API calls
    ├───static/    # Static files
    │   └───config.json   # Stores API key
    ├───db.sqlite3        # SQLite database
    └───manage.py         # Django management script
```

---

## Setup & Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git 
   cd your-repo-name
   
2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Set up your API key:
- Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).
- Create a file `static/config.json`:

```json
{
  "API_KEY": "your_api_key_here"
}
```

5. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
   
6. Run the development server:

    ```bash
    python manage.py runserver
   
7. Open your browser and go to: http://127.0.0.1:8000/

---

## Admin Panel

To access the admin panel:

1. Create a superuser:

    ```bash
    python manage.py createsuperuser
   
2. Go to: http://127.0.0.1:8000/admin

---

## Delete City

Each city card has a delete button (×). Clicking it removes the city from the database.

---

## Notes

- The app uses `requests` to fetch weather data from OpenWeatherMap.
- Cities are stored in a local SQLite database.
- The form prevents adding duplicate or non-existent cities.
- The `config.json` file is used to securely store the API key (not committed to version control in production).

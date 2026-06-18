# 🗺️ U.S. States Map Quiz Game

An interactive, data-driven geography quiz game built in Python using the **Turtle Graphics** library and **Pandas** data frames. The application challenges players to name all 50 U.S. states on an interactive map, tracking progress dynamically and exporting missing data for educational review.

---

## 🚀 Features

* **Dynamic UI Canvas:** Uses an interactive map layout where guessing a correct state instantly places its name at the exact geographic coordinates.
* **Live Scoreboard Tracking:** The prompt modal displays real-time score updates (`Current Score/50 States Correct`).
* **Duplicate Guess Protection:** Built-in validation ensures players cannot exploit the scoring system by entering the same state multiple times.
* **Error & Escape Handling:** Structured with exception safety nets to handle empty inputs or window closure gracefully without application crashes.
* **Smart Data Export ("Study Checklist"):** Typing `Exit` breaks the game loop, automatically calculates the mathematical difference between the total state database and your correct guesses using Pandas, and generates a fresh `Missed States.csv` spreadsheet for future study.

---

## 🛠️ Tech Stack & Libraries

* **Language:** Python 3.x
* **GUI & Graphics:** Native `turtle` library (Screen, Turtle)
* **Data Management:** `pandas` (for CSV parsing, dictionary mapping, and DataFrame exportation)

---

## 📦 Project Structure

```text
├── main.py              # Main executable game loop and logic
├── 50_states.csv        # Dataset containing state names, x coordinates, and y coordinates
├── blank_states_img.gif # Background map asset
└── README.md            # Project documentation

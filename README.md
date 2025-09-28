# Workout Tracker NLP 🏋️‍♀️

This project is a **smart fitness tracker** that lets you log workouts using **natural language**.  
For example, you can type:

> "I jogged 3 miles and did 20 minutes of yoga"

and the system will:
1. Parse the input using the **Nutritionix Natural Language Processing API**.
2. Extract structured data such as exercise name, duration, and calories burned.
3. Automatically save this data into a **Google Sheet** via the **Sheety API** for tracking.

---

## 🚀 Tech Stack
- **Python 3** – core programming
- **Nutritionix API** – NLP engine to interpret exercise descriptions
- **Sheety API** – to log data into Google Sheets
- **dotenv** – secure environment variable handling
- **Requests** – API communication
- **Bearer Token Authentication** – securing the Sheety endpoint

---

## 📊 Example Workflow
1. User input: `"Ran 5km and did 15 pushups"`
2. Nutritionix parses:  
   - Exercise: Running, Duration: 30 min, Calories: 250  
   - Exercise: Push-ups, Duration: 5 min, Calories: 30  
3. Sheety logs into Google Sheets with timestamp:
   | Date       | Time     | Exercise  | Duration | Calories |
   |------------|----------|-----------|----------|----------|
   | 2025-09-27 | 15:30:21 | Running   | 30       | 250      |
   | 2025-09-27 | 15:30:21 | Push-Ups  | 5        | 30       |

---

## 🔑 Use Cases
- **Personal fitness tracking** – keep a log of all workouts automatically.
- **Health coaching** – trainers can track clients’ progress via shared Google Sheets.
- **Team productivity & accountability** – fitness challenges in organizations.
- **Automation demos** – show how APIs + NLP work together.

---

## 🔮 Future Scaling & Improvements
- **OpenAI GPT Integration**  
  - GPT can provide smart workout summaries (“You burned 300 calories today, keep it up!”).  
  - GPT can suggest personalized next exercises or weekly plans.  
  - GPT can handle **multi-turn conversations** like:  
    > "I want to train for a 10k marathon, suggest a weekly plan."

- **Custom Dashboard**  
  Replace Google Sheets with a web app (React + Flask/FastAPI backend) for interactive visualization.

- **Mobile Notifications**  
  Integrate Twilio or push notifications for daily progress reports.

- **Database Integration**  
  Store workouts in PostgreSQL or MongoDB for advanced querying and analytics.

---

## 🏆 Why This Project Matters
- Demonstrates **API integration** skills.  
- Shows ability to handle **NLP outputs** and transform them into structured data.  
- Illustrates secure handling of API keys and **Bearer token authentication**.  
- Highlights potential for **scaling with AI/ML**, making it a great project for showcasing **AI + backend automation** on a portfolio.

---

## ⚙️ Setup
1. Clone repo https://github.com/martialchess/workout-tracker-nlp.git
2. Create and activate a virtualenv
3. Install dependencies:
   ```bash
   pip install -r requirements.txt


4. Create .env file:
   NUTRITIONIX_APP_ID=your_app_id
   NUTRITIONIX_API_KEY=your_api_key
   SHEETY_BEARER_TOKEN=your_token

5. Run the program
   python main.py

💡 Pro Tip:
This project can evolve into a full AI-powered personal trainer with OpenAI GPT + health APIs. Perfect for demonstrating applied NLP and automation skills in portfolio.

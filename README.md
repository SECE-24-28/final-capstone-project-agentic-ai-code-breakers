[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/s7J27iqd)

# 🌾 Smart Farmer Agent

## 📌 Project Overview

Smart Farmer Agent is an Agentic AI-based agricultural assistance system designed to help farmers make informed decisions regarding crop selection, weather conditions, disease prevention, fertilizer recommendations, and market analysis.

The system uses multiple specialized AI agents that collaborate to generate personalized recommendations for farmers based on environmental and agricultural data.

---

## 🎯 Problem Statement

Farmers often face challenges such as:

* Choosing suitable crops for their soil and season
* Predicting weather-related risks
* Identifying crop diseases
* Selecting appropriate fertilizers
* Understanding market prices

Smart Farmer Agent aims to provide intelligent assistance to address these challenges.

---

## 🤖 Agent Architecture

### 1. Crop Agent

* Recommends suitable crops based on soil type and season.

### 2. Weather Agent

* Analyzes temperature and humidity.
* Provides weather-related risk alerts.

### 3. Soil Analyzer Agent

* Evaluates soil fertility using NPK values.

### 4. Disease Agent

* Detects potential crop disease risks.

### 5. Fertilizer Agent

* Suggests fertilizers based on soil fertility.

### 6. Market Agent

* Provides expected market prices for crops.

### 7. Coordinator Agent

* Combines outputs from all agents.
* Generates the final farmer report.

---

## 📂 Project Structure

```text
Smart-Farmer-Agent
│
├── agents
│   ├── crop_agent.py
│   ├── weather_agent.py
│   ├── soil_analyzer.py
│   ├── disease_agent.py
│   ├── market_agent.py
│   ├── fertilizer_agent.py
│   └── coordinator_agent.py
│
├── api
│   └── app.py
│
├── datasets
│   ├── crop_data.csv
│   ├── fertilizer_data.csv
│   └── market_prices.csv
│
├── tests
│   └── test_input.json
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-Learn
* Agent-Based Architecture
* Git & GitHub

---

## 🚀 How to Run

### Clone Repository

```bash
git clone <repository-url>
cd Smart-Farmer-Agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 📈 Current Progress

* ✅ Crop Recommendation Agent
* ✅ Weather Analysis Agent
* ✅ Soil Analyzer Agent
* ✅ Disease Detection Agent
* ✅ Fertilizer Recommendation Agent
* ✅ Market Analysis Agent
* ✅ Coordinator Agent
* ✅ Flask API Integration

---

## 🔮 Future Enhancements

* Integration with Gemini/OpenAI APIs
* Real-Time Weather API
* Crop Disease Detection using Images
* Machine Learning Based Predictions
* Farmer Dashboard
* Voice-Based Assistance
* Mobile Application Support

---

## 👥 Team Members

###  Vishva Kumar B

* Crop Agent
* Weather Agent
* Soil Analyzer

### Samphinehas S

* Disease Agent
* Market Agent
* Fertilizer Agent

### Sanjith S

* Coordinator Agent
* Flask API
* Documentation & Testing

---

## 📜 License

This project is developed for educational and academic purposes.

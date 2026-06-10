class WeatherAgent:

    def analyze_weather(self, temperature, humidity):

        if temperature > 38:
            return {
                "risk": "High Heat",
                "advice": "Increase irrigation frequency"
            }

        elif humidity > 85:
            return {
                "risk": "Flood Risk",
                "advice": "Ensure proper drainage"
            }

        return {
            "risk": "Normal",
            "advice": "Weather conditions are favorable"
        }
from crop_agent import CropAgent
from weather_agent import WeatherAgent
from soil_analyzer import SoilAnalyzer

from disease_agent import DiseaseAgent
from market_agent import MarketAgent
from fertilizer_agent import FertilizerAgent


class SmartFarmerCoordinator:

    def __init__(self):

        self.crop_agent = CropAgent()
        self.weather_agent = WeatherAgent()
        self.soil_agent = SoilAnalyzer()

        self.disease_agent = DiseaseAgent()
        self.market_agent = MarketAgent()
        self.fertilizer_agent = FertilizerAgent()

    def generate_report(self, data):

        fertility = self.soil_agent.analyze(
            data["nitrogen"],
            data["phosphorus"],
            data["potassium"]
        )

        crop = self.crop_agent.recommend_crop(
            data["soil_type"],
            data["season"]
        )

        weather = self.weather_agent.analyze_weather(
            data["temperature"],
            data["humidity"]
        )

        disease = self.disease_agent.detect_risk(
            crop,
            data["humidity"]
        )

        market_price = self.market_agent.predict_market_price(
            crop
        )

        fertilizer = self.fertilizer_agent.recommend(
            fertility
        )

        return {
            "crop": crop,
            "fertility": fertility,
            "weather": weather,
            "disease": disease,
            "fertilizer": fertilizer,
            "expected_price": market_price
        }
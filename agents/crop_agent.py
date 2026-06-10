class CropAgent:

    def recommend_crop(self, soil_type, season):

        recommendations = {
            ("clay", "monsoon"): "Rice",
            ("loamy", "winter"): "Wheat",
            ("sandy", "summer"): "Groundnut"
        }

        return recommendations.get(
            (soil_type.lower(), season.lower()),
            "Millet"
        )
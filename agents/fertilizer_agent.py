class FertilizerAgent:

    def recommend(self, fertility):

        mapping = {
            "Highly Fertile": "Organic Compost",
            "Moderately Fertile": "NPK 10-10-10",
            "Low Fertility": "NPK 20-20-20"
        }

        return mapping.get(fertility)
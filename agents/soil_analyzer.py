class SoilAnalyzer:

    def analyze(self, nitrogen, phosphorus, potassium):

        score = nitrogen + phosphorus + potassium

        if score > 180:
            return "Highly Fertile"

        elif score > 120:
            return "Moderately Fertile"

        return "Low Fertility"
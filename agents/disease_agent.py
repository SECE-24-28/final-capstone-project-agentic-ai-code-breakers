class DiseaseAgent:

    def detect_risk(self, crop, humidity):

        if crop == "Rice" and humidity > 80:
            return "Blast Disease Risk"

        if crop == "Wheat" and humidity > 75:
            return "Rust Disease Risk"

        return "No Major Disease Risk"
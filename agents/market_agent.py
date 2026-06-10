class MarketAgent:

    def predict_market_price(self, crop):

        prices = {
            "Rice": 48,
            "Wheat": 36,
            "Groundnut": 75,
            "Millet": 42
        }

        return prices.get(crop, 0)
from flask import Flask, request, jsonify
from coordinator_agent import SmartFarmerCoordinator

app = Flask(__name__)

agent = SmartFarmerCoordinator()

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json

    report = agent.generate_report(data)

    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify
from ua_parser import user_agent_parser
import os

app = Flask(__name__)
env_config = os.getenv('PROD_APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(env_config)

@app.route('/', methods=['POST'])
def parse_user_agent():
    data = request.json
    user_agent = data.get('user_agent') if data else None

    if user_agent:
        parsed_data = user_agent_parser.Parse(user_agent)
        return jsonify(parsed_data)
    else:
        return jsonify({"error": "User-Agent data is missing in the request body."}), 400

if __name__ == '__main__':
    app.run(debug=True)
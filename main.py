from flask import Flask, request, jsonify
import requests
import datetime

app = Flask(__name__)

@app.route('/api/report/<report_name>', methods=['GET'])
def get_report(report_name):
    date_from = request.args.get('from')
    date_to = request.args.get('to')
    users_data = [
        {"userId": 1, "metrics": [{"dailyAverage": 1475}]},
        {"userId": 2, "metrics": [{"dailyAverage": 1520}]},
    ]
    daily_average_all_users = sum(user["metrics"][0]["dailyAverage"] for user in users_data) / len(users_data)
    response_data = {
        "users": users_data,
        "dailyAverage": daily_average_all_users,
        "<other_metric>": "<other metric for all specified users>"
    }
    return jsonify(response_data)

@app.route('/api/users/last_seen', methods=['GET'])
def get_last_seen():
    offset = request.args.get('offset', default=0, type=int)
    api_url = f'https://sef.podkolzin.consulting/api/users/lastSeen?offset={offset}'
    api_response = requests.get(api_url)
    api_data = api_response.json()
    last_seen_timestamp = api_data.get('lastSeen', 0)
    last_seen_human_readable = datetime.datetime.fromtimestamp(
        last_seen_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    response_data = {
        "lastSeen": last_seen_human_readable
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='51.20.83.7', debug=True)


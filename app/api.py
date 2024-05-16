from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({ "status": True })

@app.route('/api/slack', methods=['POST'])
def send_to_slack():
    data = request.get_json()
    # Slack mesajını gönderme işlemi burada yapılır
    return jsonify({ "message": "Message sent to Slack" })

@app.route('/api/github/<int:pr_id>', methods=['POST'])
def merge_github_pr(pr_id):
    # GitHub pull request birleştirme işlemi burada yapılır
    return jsonify({ "message": f"Pull request {pr_id} merged successfully" })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


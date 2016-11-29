from flask import Flask, make_response, jsonify, request, abort, render_template, request
import requests
from lxml import html

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
	data = request.json

	if data is None:
		return make_response(jsonify({"success": False, "message": "The body must be a JSON object with the appropriate header"}), 400)

	if 'ip' not in data:
		return make_response(jsonify({"success": False, "message": "A single key, ip, with a value representing an IP Address must hbe provided."}), 400)

	url = "https://geoiptool.com/en/?ip="

	response = requests.get(url + data["ip"])
	tree = html.document_fromstring(response.text)

	outside = tree.xpath('//div[contains(@class, "sidebar-data")]')
	if len(outside) != 2:
		return make_response(jsonify({"success": False, "message": None}), 500)

	response = {}

	for elem in outside[0].xpath('div[@class="data-item"]'):

		title = elem.xpath('span')[0].text_content().strip()
		content = elem.xpath('span')[1].text_content().strip()

		response[title.replace(":", "").replace(" ", "_").lower()] = content

	return make_response(jsonify({"success": True, "message": None, "data": response}), 200)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

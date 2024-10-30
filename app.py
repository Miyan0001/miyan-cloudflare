import cloudscraper
from flask import Flask, request, jsonify
scraper = cloudscraper.create_scraper()

app = Flask(__name__)

@app.route('*', methods=['GET'])
def cloudflare_route():
    url = request.args.get('url')
    if not url:
        return "Where's the url parameter?", 500
    bypass_cloudflare = scraper.get(url).text
    return bypass_cloudflare, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
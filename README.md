# geoiptool wrapper

This Python / Flask app serves as a simple wrapper around https://geoiptool.com. To use it, simply do the following:

```
git clone git@github.com:jayrav13/geoiptool-wrapper.git
cd geoiptool-wrapper/
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python __init__.py
```

A successful requests has a few requirements:

- Set the HTTP request header "Content-Type" to "application/json"
- Include one key, "ip", the value of which is a valid ip address.

Example:

```
curl -i -X POST https://ep-geoip.herokuapp.com -H "Content-Type: application/json" -d '{"ip": "108.29.95.28"}'
```

Response:

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 365
Server: Werkzeug/0.11.11 Python/2.7.10
Date: Tue, 29 Nov 2016 19:44:03 GMT

{
  "data": {
    "city": "New York",
    "country": "United States",
    "country_code": "US (USA)",
    "hostname": "",
    "ip_address": "108.29.95.28",
    "latitude": "40.7517",
    "local_time": "29 Nov 14:42 (EST-0500)",
    "longitude": "-73.9972",
    "postal_code": "10001",
    "region": "New York"
  },
  "message": null,
  "success": true
}
```

NOTE: Currently, erroneous ip addresses are not handled.

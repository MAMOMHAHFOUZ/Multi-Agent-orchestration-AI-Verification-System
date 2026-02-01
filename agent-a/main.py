import json
import urllib.request
import random

def main(args):
    url_b = "https://agent-b.25rq6jnf20iq.eu-gb.codeengine.appdomain.cloud"
    data_to_send = {
        "customer": args.get("customer", "Guest"),
        "transfer_id": "TRX" + str(random.randint(100, 999)),
        "amount": "200 USD",
        "files": args.get("files", [])
    }
    
    try:
        payload = json.dumps(data_to_send).encode('utf-8')
        req = urllib.request.Request(url_b, data=payload, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode('utf-8'))
    except Exception as e:
        return {"status": "error", "details": str(e)}
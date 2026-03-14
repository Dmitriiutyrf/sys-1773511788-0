import json
def scan_payload(payload: str) -> dict:
    keys = ['AWS_SECRET_ACCESS_KEY','OPENAI_API_KEY','id_rsa','privateKey','authToken']
    found = {k: (k in payload) for k in keys}
    score = sum(1 for v in found.values() if v)
    return {'score': score, 'found': found}
def plan_rotation(found: dict) -> dict:
    return {'rotate': [k for k,v in found.items() if v], 'deadline_hours': 24}
def main() -> None:
    sample = json.dumps({'config': 'authToken=fake-npm-token', 'pkey': '-----BEGIN RSA PRIVATE KEY-----'})
    r = scan_payload(sample)
    p = plan_rotation(r['found'])
    print(json.dumps({'analysis': r, 'plan': p}))
if __name__ == '__main__':
    main()

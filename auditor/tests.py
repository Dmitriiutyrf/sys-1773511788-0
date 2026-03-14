from auditor import scan_payload, plan_rotation
def test_scan():
    r = scan_payload('OPENAI_API_KEY=sk-FAKE')
    assert r['score'] >= 1
def test_plan():
    p = plan_rotation({'OPENAI_API_KEY': True})
    assert 'OPENAI_API_KEY' in p['rotate']

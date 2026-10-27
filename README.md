# Vulnerable SQL Injection Demo

This disposable example intentionally includes vulnerable code for local security education. **Never run this example as a public service, expose it to a network, or use it with real data.**

Run:

```bash
python -m unittest -v
```

The test suite serves as a differential verification benchmark for Raksa:
- `test_normal_search_returns_matching_user` verifies that normal queries return expected records.
- `test_sql_injection_payload_is_treated_as_literal` tests that the injection payload `"' OR 1=1 --"` is treated strictly as a literal search parameter, expecting an empty result set (`[]`).

Against the vulnerable baseline, the security test intentionally fails with an `AssertionError` because string interpolation allows the payload to return unintended rows. When remediated with parameterized queries, the security test passes, proving that the vulnerability has been eliminated.

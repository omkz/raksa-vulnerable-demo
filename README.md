# Raksa Vulnerable Demo

**Intentionally vulnerable, static-only source fixtures for [Raksa — Your AI Security Engineer](https://github.com/omkz/raksa).**

> [!CAUTION]
> **DO NOT RUN, IMPORT, TEST, BUILD, SERVE, OR DEPLOY THIS REPOSITORY.**
>
> This repository deliberately contains unsafe code patterns. It exists **only for source-code inspection and static security scanning**. Do not connect it to production systems, expose it to a network, use real credentials or user data, or execute the vulnerable examples. Do not merge AI-generated remediation into this baseline: the vulnerable patterns are intentional test fixtures.

## Purpose

Raksa is an AI-assisted security remediation application. This separate repository provides a small, reproducible collection of intentionally unsafe Python and JavaScript source snippets so that Raksa can demonstrate the workflow:

**Static scan → Potential findings → NVIDIA Nemotron patch proposals → Verification status → Human review → GitHub Draft PR**

The snippets are **detection fixtures**, not an application to install or run. A scanner finding indicates a *potential* security issue; it does not, by itself, establish exploitability or a successful fix.

## Intentionally unsafe fixtures

| File | Potential issue | CWE | Detection source |
| --- | --- | --- | --- |
| [`app.py`](app.py) | String-interpolated SQL query | CWE-89 — SQL Injection | Raksa's Python AST-based SQL injection scanner |
| [`src/unsafe_xss.js`](src/unsafe_xss.js) | Untrusted text inserted using `innerHTML` | CWE-79 — Cross-Site Scripting | OpenGrep rule `raksa.javascript-html-injection` |
| [`src/unsafe_path.py`](src/unsafe_path.py) | Request-controlled path used for file access | CWE-22 — Path Traversal | OpenGrep rule `raksa.python-request-file-access` |
| [`src/unsafe_shell.py`](src/unsafe_shell.py) | Shell execution of a supplied command | CWE-78 — Command Injection | OpenGrep rule `raksa.python-shell-execution` |
| [`src/unsafe_eval.js`](src/unsafe_eval.js) | Dynamic evaluation of supplied JavaScript | CWE-94 — Code Injection | OpenGrep rule `raksa.javascript-dynamic-eval` |

The OpenGrep rules shown above are Raksa's **initial local rules**, not a comprehensive OpenGrep ruleset. OpenGrep is optional and disabled by default in Raksa's example configuration. Consequently, the exact number of findings depends on the scanner configuration and snapshot limits. Five findings were observed in the documented demonstration; five is **not** a general detection limit for OpenGrep.

The repository also contains [`test_app.py`](test_app.py), an illustrative SQLite test fixture. The baseline implementation is intentionally insecure. **Do not execute these tests against this repository**; this README does not claim they were run for the GitHub Draft PR below.

## Inspect with Raksa — static scanning only

1. Follow the setup instructions in the **[main Raksa repository](https://github.com/omkz/raksa)**, using an environment you control.
2. Connect the Raksa GitHub App to this repository with the necessary scoped permissions.
3. In the Raksa dashboard, select `omkz/raksa-vulnerable-demo` and choose **Analyze repository**.
4. To include the optional OpenGrep detections, configure the Raksa scanner's isolated OpenGrep image and enable it **in the Raksa application**, not in this vulnerable repository.
5. Review the reported findings, AI-proposed patches, scanner coverage, and verification status.

**Use only Raksa's source-fetching and static-analysis workflow.** Do not run code or tests from this repository as part of the demonstration. Do not use an execution sandbox on these fixtures merely to obtain a passing verification badge.

## Actual Raksa-generated GitHub Draft PR

**[View Draft PR #5 — UNVERIFIED / HUMAN REVIEW REQUIRED](https://github.com/omkz/raksa-vulnerable-demo/pull/5)**

The [Raksa GitHub App](https://github.com/omkz/raksa) created a real **Draft Pull Request** after explicit developer approval. It contains two focused *candidate* changes:

- **CWE-89:** Replace interpolated SQL with a parameterized query in `app.py`.
- **CWE-79:** Replace `innerHTML` with `textContent` in `src/unsafe_xss.js`.

For the other findings, Raksa did not assume the application's authorization rules or invent architectural decisions. The demonstration includes cases where the agent requests context or abstains from proposing a patch.

> [!IMPORTANT]
> **PR #5 is `UNVERIFIED — REVIEW ONLY`.**
>
> Its proposed changes did **not** undergo category-specific exploit and regression verification. A well-formed patch, static finding, or AI explanation is **not** proof that a vulnerability has been eliminated or that the application still behaves correctly.
>
> **Do not merge PR #5 into this fixture repository.** Keep the baseline intentionally vulnerable for reproducible static scans.

## Safety and scope

- This repository is **not a production-ready application**, a hosted demo, or a vulnerability benchmark with comprehensive test coverage.
- Its insecure examples must not be executed or deployed.
- Detection depends on which Raksa scanners are enabled and the exact source snapshot analyzed.
- Raksa's verification results are specific to the tests actually run and their reported status.
- To learn about Raksa's supported workflow, constraints, setup, and source code, visit **[omkz/raksa](https://github.com/omkz/raksa)**.

---

**Raksa — Your AI Security Engineer.** Investigate → Remediate → Verify → Review.

// STATIC SCAN FIXTURE ONLY — intentionally unsafe; never execute or deploy.
// Expected Raksa OpenGrep rule: raksa.javascript-html-injection (CWE-79).

export function renderUntrustedMessage(container, message) {
  container.textContent = message;
}

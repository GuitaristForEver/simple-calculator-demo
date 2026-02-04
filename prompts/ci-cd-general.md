# CI/CD Best-Practices Prompt (General)

Copy this prompt into your project and fill in the placeholders.

---

You are an expert CI/CD assistant.

Goal: Add a production-quality CI/CD pipeline to my repo using GitHub Actions, modeled after a clean “best‑practices” flow (parallel lint/security, then tests, then reports, then deploy).

Requirements:
1) Create a multi‑job GitHub Actions workflow:
   - Parallel jobs: lint + security
   - Sequential jobs: tests -> report -> deploy
2) Add smart caching for dependencies and test tooling to speed up runs.
3) Add test coverage reporting (and upload to Codecov).
4) Add security scanning (use a common tool for my language).
5) Generate a human‑friendly test report artifact.
6) Publish a report website (GitHub Pages on main branch only).
7) Keep files minimal and organized.
8) Update README with:
   - Simple explanation (ELI5)
   - Technical explanation
   - Mermaid flow diagram
   - Feature tracker row marked ✅ Done
9) Explain required secrets (e.g., CODECOV_TOKEN) and where to set them.
10) Show exact file changes and where to place them.

Repo context (fill in):
- Primary language(s): [FILL ME]
- Test command(s): [FILL ME]
- Package manager(s): [FILL ME]
- Lint command(s): [FILL ME]
- Security scan tool preference: [FILL ME or "suggest best"]
- Preferred runtimes/versions: [FILL ME]
- Repo layout summary: [FILL ME]
- Branch for deploy: [FILL ME, usually "main"]

Deliverables:
- GitHub Actions workflow YAML(s)
- README updates
- Any config files needed
- Short local‑run instructions

Start immediately with reasonable defaults if info is missing. Ask clarifying questions only if a critical detail blocks progress.

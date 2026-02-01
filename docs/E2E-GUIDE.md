# End-to-End Guide: Simple Calculator Demo 🚀

## Overview

This guide provides a complete visual walkthrough of the entire development lifecycle - from writing code to deploying test reports - using Mermaid diagrams.

---

## Table of Contents

- [Complete System Overview](#complete-system-overview)
- [Developer Workflow](#developer-workflow)
- [Pre-commit Hook Flow](#pre-commit-hook-flow)
- [CI/CD Pipeline Flow](#cicd-pipeline-flow)
- [Test Execution & Reporting](#test-execution--reporting)
- [Data Flow Architecture](#data-flow-architecture)
- [Deployment Process](#deployment-process)

---

## Complete System Overview

This diagram shows how all the pieces fit together:

```mermaid
graph TB
    subgraph Developer["👨‍💻 Developer Environment"]
        Code[Write Code]
        LocalTest[Run Tests Locally]
        PreCommit[Pre-commit Hooks]
    end

    subgraph VCS["📦 Version Control"]
        Git[Git Repository]
        GitHub[GitHub Remote]
    end

    subgraph CI["🤖 GitHub Actions CI/CD"]
        Lint[Lint Job]
        Security[Security Job]
        Test[Test Job]
        Report[Report Generation]
        Deploy[Deploy Job]
    end

    subgraph Artifacts["📊 Outputs"]
        AllureReport[Allure Report]
        Pages[GitHub Pages]
        PublicURL[Public URL]
    end

    Code --> LocalTest
    LocalTest --> PreCommit
    PreCommit --> Git
    Git --> GitHub

    GitHub --> Lint
    GitHub --> Security
    Lint --> Test
    Security --> Test
    Test --> Report
    Report --> AllureReport
    AllureReport --> Deploy
    Deploy --> Pages
    Pages --> PublicURL

    style Developer fill:#e1f5ff
    style CI fill:#fff3cd
    style Artifacts fill:#d4edda
```

---

## Developer Workflow

The daily development cycle from code changes to commit:

```mermaid
flowchart TD
    Start([Start Development]) --> Edit[Edit calculator.py]

    Edit --> RunCalc{Want to test<br/>manually?}
    RunCalc -->|Yes| Manual[python -m calculator.calculator]
    RunCalc -->|No| RunTests
    Manual --> RunTests

    RunTests[pytest --alluredir=allure-results]
    RunTests --> TestPass{Tests Pass?}

    TestPass -->|No| FixCode[Fix Code]
    FixCode --> Edit

    TestPass -->|Yes| ViewReport[View reports/test-report.html]
    ViewReport --> Satisfied{Satisfied with<br/>changes?}

    Satisfied -->|No| Edit
    Satisfied -->|Yes| GitAdd[git add .]

    GitAdd --> GitCommit[git commit -m "message"]
    GitCommit --> PreCommitTrigger[⚡ Pre-commit hooks trigger]

    PreCommitTrigger --> HookChecks{All hooks<br/>pass?}

    HookChecks -->|No| ShowErrors[Show errors]
    ShowErrors --> FixIssues[Fix issues]
    FixIssues --> GitAdd

    HookChecks -->|Yes| CommitSuccess[✅ Commit successful]
    CommitSuccess --> Push[git push origin main]

    Push --> CITrigger[🚀 GitHub Actions triggered]
    CITrigger --> End([Wait for CI results])

    style Start fill:#e1f5ff
    style CommitSuccess fill:#d4edda
    style End fill:#d4edda
    style PreCommitTrigger fill:#fff3cd
    style CITrigger fill:#fff3cd
```

---

## Pre-commit Hook Flow

What happens when you try to commit code:

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Git as Git
    participant PreCommit as Pre-commit Framework
    participant Gitleaks as 🔒 Gitleaks
    participant Ruff as 🐍 Ruff
    participant FileChecks as 📝 File Checks

    Dev->>Git: git commit -m "message"
    Git->>PreCommit: Trigger pre-commit hooks

    PreCommit->>Gitleaks: Check for secrets/API keys
    Gitleaks-->>PreCommit: ✅ No secrets found

    PreCommit->>Ruff: Lint Python code
    Ruff-->>PreCommit: ✅ No linting errors

    PreCommit->>Ruff: Format Python code
    Ruff-->>PreCommit: ✅ Code formatted

    PreCommit->>FileChecks: Check file integrity
    Note over FileChecks: - Trailing whitespace<br/>- End-of-file newline<br/>- Large files<br/>- Merge conflicts
    FileChecks-->>PreCommit: ✅ All checks pass

    PreCommit->>Git: ✅ All hooks passed
    Git->>Dev: Commit successful!

    Note over Dev,FileChecks: If any hook fails, commit is blocked<br/>and developer must fix issues
```

---

## CI/CD Pipeline Flow

The complete GitHub Actions workflow:

```mermaid
flowchart TD
    Trigger([Push to main or PR]) --> Parallel{Parallel Stage}

    subgraph Stage1["Stage 1: Quality Gates (Parallel)"]
        Lint[🔍 Lint Job<br/>- Ruff linting<br/>- Code quality checks]
        Security[🔒 Security Job<br/>- CodeQL analysis<br/>- Bandit security scan]
    end

    Parallel --> Lint
    Parallel --> Security

    Lint --> WaitGate{Both complete?}
    Security --> WaitGate

    WaitGate --> Test

    subgraph Stage2["Stage 2: Testing (Sequential)"]
        Test[🧪 Test Job<br/>- Run pytest<br/>- Generate allure-results/]

        Test --> Cache1{Check cache}
        Cache1 -->|Hit| FastTest[⚡ Use cached dependencies<br/>~15s]
        Cache1 -->|Miss| SlowTest[📦 Install dependencies<br/>~45s]

        FastTest --> TestComplete
        SlowTest --> TestComplete
        TestComplete[Tests complete]
    end

    TestComplete --> Report

    subgraph Stage3["Stage 3: Reporting (Sequential)"]
        Report[📊 Report Job<br/>- Fetch history from gh-pages<br/>- Merge with new results<br/>- Generate Allure report]

        Report --> UploadArtifact[⬆️ Upload artifact<br/>allure-history.zip]
    end

    UploadArtifact --> DeployCheck{Branch is main?}

    DeployCheck -->|Yes| Deploy
    DeployCheck -->|No| SkipDeploy[⏭️ Skip deployment<br/>View in artifacts]

    subgraph Stage4["Stage 4: Deployment (Conditional)"]
        Deploy[🚀 Deploy Job<br/>- Download report artifact<br/>- Deploy to GitHub Pages]

        Deploy --> Published[✅ Published to gh-pages]
        Published --> LiveURL[🔗 Live at GitHub Pages URL]
    end

    SkipDeploy --> End([End])
    LiveURL --> End

    style Stage1 fill:#fff3cd
    style Stage2 fill:#e1f5ff
    style Stage3 fill:#d4edda
    style Stage4 fill:#f8d7da
    style End fill:#d4edda
```

---

## Test Execution & Reporting

How tests are executed and reports generated:

```mermaid
flowchart LR
    subgraph Local["💻 Local Development"]
        L1[pytest] --> L2[Run 5 test cases]
        L2 --> L3[Generate allure-results/]
        L3 --> L4[pytest-html report]
        L4 --> L5[View: reports/test-report.html]
    end

    subgraph CI["🤖 CI Environment"]
        C1[pytest --alluredir] --> C2[Run 5 test cases]
        C2 --> C3[Collect results]
        C3 --> C4{Fetch history}
        C4 -->|gh-pages| C5[Previous 20 runs]
        C5 --> C6[Merge history]
        C6 --> C7[Generate Allure report]
        C7 --> C8[Upload artifact]
    end

    subgraph Report["📊 Allure Report Features"]
        R1[Test Results]
        R2[Historical Trends]
        R3[Flaky Test Detection]
        R4[Performance Tracking]
        R5[Error Screenshots]
    end

    C8 --> Report

    subgraph Deploy["🌐 GitHub Pages"]
        D1[Deploy to gh-pages]
        D2[Public URL]
        D3[Anyone can view]
    end

    Report --> Deploy

    style Local fill:#e1f5ff
    style CI fill:#fff3cd
    style Report fill:#d4edda
    style Deploy fill:#f8d7da
```

---

## Data Flow Architecture

How data moves through the system:

```mermaid
graph LR
    subgraph Source["📝 Source Code"]
        CalcPy[calculator.py<br/>~100 lines]
        TestPy[test_calculator.py<br/>5 test cases]
    end

    subgraph Execution["⚙️ Test Execution"]
        Pytest[pytest framework]
        Fixtures[Test fixtures]
        Assertions[assert statements]
    end

    subgraph RawData["📁 Raw Data"]
        AllureResults[allure-results/<br/>JSON test data]
        JUnit[junit.xml<br/>CI/CD format]
        HTML[test-report.html<br/>Quick view]
    end

    subgraph Processing["🔄 Processing"]
        FetchHistory[Fetch gh-pages<br/>last 20 runs]
        MergeData[Merge with<br/>new results]
        GenerateReport[Generate<br/>Allure HTML]
    end

    subgraph Output["📊 Final Output"]
        AllureHTML[Allure Report<br/>Interactive HTML]
        Trends[Trend Charts]
        History[Historical Data]
    end

    subgraph Delivery["🚀 Delivery"]
        Artifact[GitHub Artifact<br/>Download zip]
        Pages[GitHub Pages<br/>Live website]
        URL[Public URL]
    end

    CalcPy --> Pytest
    TestPy --> Pytest
    Pytest --> Fixtures
    Fixtures --> Assertions

    Assertions --> AllureResults
    Assertions --> JUnit
    Assertions --> HTML

    AllureResults --> FetchHistory
    FetchHistory --> MergeData
    MergeData --> GenerateReport

    GenerateReport --> AllureHTML
    GenerateReport --> Trends
    GenerateReport --> History

    AllureHTML --> Artifact
    AllureHTML --> Pages
    Pages --> URL

    style Source fill:#e1f5ff
    style Execution fill:#fff3cd
    style RawData fill:#ffe5cc
    style Processing fill:#e5ccff
    style Output fill:#d4edda
    style Delivery fill:#f8d7da
```

---

## Deployment Process

Detailed view of the GitHub Pages deployment:

```mermaid
sequenceDiagram
    participant Test as Test Job
    participant Artifact as Artifact Storage
    participant Deploy as Deploy Job
    participant Pages as GitHub Pages
    participant User as End User

    Test->>Test: Run pytest
    Test->>Test: Generate allure-results/
    Test->>Artifact: Upload allure-results.zip

    Note over Deploy: Triggered only on main branch

    Deploy->>Artifact: Download allure-results.zip
    Deploy->>Deploy: Extract files

    Deploy->>Pages: Checkout gh-pages branch

    alt First deployment
        Deploy->>Pages: Create gh-pages branch
    else Existing deployment
        Deploy->>Pages: Pull latest gh-pages
    end

    Deploy->>Deploy: Fetch previous history<br/>(last 20 runs)
    Deploy->>Deploy: Merge with new results
    Deploy->>Deploy: Generate Allure report

    Deploy->>Pages: Commit new report
    Deploy->>Pages: Push to gh-pages

    Pages->>Pages: Build & deploy site

    Note over Pages: Site available at:<br/>username.github.io/repo

    User->>Pages: Visit public URL
    Pages->>User: Serve Allure report

    Note over User: View test results,<br/>trends, history
```

---

## Complete User Journey

From code change to viewing results online:

```mermaid
journey
    title Complete Development & Deployment Journey
    section Local Development
      Write code: 5: Developer
      Run tests locally: 4: Developer
      View HTML report: 3: Developer
      Fix any issues: 4: Developer
    section Version Control
      Git add & commit: 5: Developer
      Pre-commit checks: 4: Pre-commit
      Git push to GitHub: 5: Developer
    section CI/CD Pipeline
      Lint & security checks: 3: GitHub Actions
      Run tests in cloud: 4: GitHub Actions
      Generate Allure report: 4: GitHub Actions
      Merge with history: 3: GitHub Actions
    section Deployment
      Deploy to Pages: 5: GitHub Actions
      Site goes live: 5: GitHub Pages
    section Consumption
      View public URL: 5: Anyone
      Explore test trends: 4: Stakeholders
      Check test health: 5: Team
```

---

## Technology Stack Flow

How different technologies interact:

```mermaid
graph TB
    subgraph Dev["Developer Tools"]
        Python[Python 3.9+]
        Git[Git VCS]
        Editor[Code Editor]
    end

    subgraph Testing["Testing Stack"]
        Pytest[pytest framework]
        AllurePlugin[allure-pytest plugin]
        PytestHTML[pytest-html plugin]
        Coverage[pytest-cov]
    end

    subgraph Quality["Quality Tools"]
        Ruff[Ruff linter/formatter]
        Gitleaks[Gitleaks secret scanner]
        PreCommitFW[pre-commit framework]
    end

    subgraph CI["CI/CD Platform"]
        Actions[GitHub Actions]
        Runners[Ubuntu Runners]
        Cache[GitHub Cache]
    end

    subgraph Security["Security Scanning"]
        CodeQL[CodeQL Analysis]
        Bandit[Bandit Scanner]
    end

    subgraph Reporting["Reporting Tools"]
        AllureGen[Allure Report Generator]
        AllureAction[allure-report-action]
    end

    subgraph Hosting["Hosting Infrastructure"]
        GHPages[GitHub Pages]
        DNS[Custom Domain Support]
    end

    subgraph Package["Package Management"]
        Pip[pip]
        UV[uv (10-100x faster)]
        PyprojectToml[pyproject.toml]
    end

    Python --> Pytest
    Pytest --> AllurePlugin
    Pytest --> PytestHTML
    Pytest --> Coverage

    Editor --> Git
    Git --> PreCommitFW
    PreCommitFW --> Ruff
    PreCommitFW --> Gitleaks

    Git --> Actions
    Actions --> Runners
    Runners --> Cache

    Actions --> CodeQL
    Actions --> Bandit

    AllurePlugin --> AllureGen
    AllureGen --> AllureAction
    AllureAction --> GHPages
    GHPages --> DNS

    PyprojectToml --> Pip
    PyprojectToml --> UV

    style Dev fill:#e1f5ff
    style Testing fill:#d4edda
    style Quality fill:#fff3cd
    style CI fill:#f8d7da
    style Security fill:#ffe5cc
    style Reporting fill:#e5ccff
    style Hosting fill:#ccf5e5
    style Package fill:#f5e5cc
```

---

## Caching Strategy

How multi-layer caching speeds up the pipeline:

```mermaid
flowchart TD
    Start([CI Job Starts]) --> Layer1{Layer 1:<br/>Pip Cache}

    Layer1 -->|Cache Hit| L1Hit[⚡ Restore pip packages<br/>Save ~20s]
    Layer1 -->|Cache Miss| L1Miss[📦 Download packages<br/>Takes ~20s]

    L1Hit --> Layer2{Layer 2:<br/>Package Cache}
    L1Miss --> CacheSave1[Save to pip cache]
    CacheSave1 --> Layer2

    Layer2 -->|Cache Hit| L2Hit[⚡ Restore ~/.cache/pip<br/>Save ~10s]
    Layer2 -->|Cache Miss| L2Miss[📦 Build packages<br/>Takes ~10s]

    L2Hit --> Layer3{Layer 3:<br/>pytest Cache}
    L2Miss --> CacheSave2[Save to package cache]
    CacheSave2 --> Layer3

    Layer3 -->|Cache Hit| L3Hit[⚡ Restore .pytest_cache<br/>Save ~5s]
    Layer3 -->|Cache Miss| L3Miss[🔄 Collect tests<br/>Takes ~5s]

    L3Hit --> RunTests[Run Tests]
    L3Miss --> CacheSave3[Save to pytest cache]
    CacheSave3 --> RunTests

    RunTests --> Result{Total Time}
    Result -->|All Cache Hits| Fast[⚡ ~15 seconds<br/>3x faster!]
    Result -->|No Cache| Slow[📦 ~45 seconds<br/>First run]

    Fast --> End([Tests Complete])
    Slow --> End

    style Layer1 fill:#e1f5ff
    style Layer2 fill:#fff3cd
    style Layer3 fill:#d4edda
    style Fast fill:#d4edda
    style Slow fill:#f8d7da
```

**Cache Invalidation**:
- **Pip cache**: Invalidates when `requirements.txt` changes
- **Package cache**: Invalidates when dependencies change
- **pytest cache**: Invalidates when test files change

---

## Error Handling Flow

What happens when things go wrong:

```mermaid
flowchart TD
    Start([Developer pushes code]) --> PreCommit{Pre-commit<br/>checks}

    PreCommit -->|❌ Fail| PC_Error[Show error message]
    PC_Error --> PC_Fix[Developer fixes locally]
    PC_Fix --> Start

    PreCommit -->|✅ Pass| Pushed[Code pushed to GitHub]
    Pushed --> Lint{Lint job}

    Lint -->|❌ Fail| L_Error[❌ Workflow fails<br/>Red X on PR]
    L_Error --> L_Fix[Fix linting issues]
    L_Fix --> Start

    Lint -->|✅ Pass| SecScan{Security scan}

    SecScan -->|❌ Fail| S_Error[❌ Vulnerability found<br/>Block merge]
    S_Error --> S_Fix[Fix security issue]
    S_Fix --> Start

    SecScan -->|✅ Pass| Tests{Run tests}

    Tests -->|❌ Fail| T_Error[❌ Test failed<br/>Show failure details]
    T_Error --> T_Fix[Fix failing test]
    T_Fix --> Start

    Tests -->|✅ Pass| Report[Generate report]
    Report --> Deploy{Deploy to<br/>GitHub Pages}

    Deploy -->|❌ Fail| D_Error[❌ Deployment failed<br/>Check permissions]
    D_Error --> D_Fix[Fix deployment config]
    D_Fix --> Report

    Deploy -->|✅ Pass| Success[✅ Complete success<br/>Report live!]
    Success --> End([End])

    style PC_Error fill:#f8d7da
    style L_Error fill:#f8d7da
    style S_Error fill:#f8d7da
    style T_Error fill:#f8d7da
    style D_Error fill:#f8d7da
    style Success fill:#d4edda
```

---

## State Diagram: Test Report Status

The lifecycle of a test report:

```mermaid
stateDiagram-v2
    [*] --> NotGenerated: No tests run yet

    NotGenerated --> Generating: pytest executed
    Generating --> LocalReport: Tests complete

    LocalReport --> PushedToGit: git push
    PushedToGit --> CIRunning: GitHub Actions triggered

    CIRunning --> TestsPassed: All tests pass
    CIRunning --> TestsFailed: Some tests fail

    TestsFailed --> LocalReport: Fix code & re-run

    TestsPassed --> ReportGenerated: Allure report created
    ReportGenerated --> Deploying: Deploy job starts

    Deploying --> PublishedToPages: Deployment successful
    Deploying --> DeploymentFailed: Deployment error

    DeploymentFailed --> Deploying: Retry deployment

    PublishedToPages --> Live: Report accessible online
    Live --> Updated: New push with changes

    Updated --> CIRunning: CI re-triggered

    note right of Live
        Report includes:
        - Current results
        - Historical trends
        - Previous 20 runs
    end note
```

---

## Calculator Logic Flow

For completeness, how the calculator itself works:

```mermaid
flowchart TD
    Start([User Input]) --> Mode{Interactive or<br/>Programmatic?}

    Mode -->|Interactive| GetOp[Get operation from user]
    Mode -->|Programmatic| DirectCall[Direct method call]

    GetOp --> ValidOp{Valid operation?}
    ValidOp -->|No| Error1[Print error message]
    Error1 --> GetOp
    ValidOp -->|Yes| GetNums[Get two numbers]

    GetNums --> Calculate
    DirectCall --> Calculate

    Calculate{Which operation?}

    Calculate -->|Add| Add[a + b]
    Calculate -->|Subtract| Subtract[a - b]
    Calculate -->|Multiply| Multiply[a * b]
    Calculate -->|Divide| DivCheck{b == 0?}

    DivCheck -->|Yes| DivError[Raise ValueError:<br/>'Cannot divide by zero']
    DivCheck -->|No| Divide[a / b]

    Add --> Result[Return result]
    Subtract --> Result
    Multiply --> Result
    Divide --> Result

    Result --> Output[Display to user]
    Output --> Continue{Continue?}

    Continue -->|Yes| GetOp
    Continue -->|No| End([Exit])

    DivError --> ErrorHandler[Catch exception]
    ErrorHandler --> Continue

    style Add fill:#d4edda
    style Subtract fill:#d4edda
    style Multiply fill:#d4edda
    style Divide fill:#d4edda
    style DivError fill:#f8d7da
    style Error1 fill:#f8d7da
```

---

## Summary: The Complete Picture

```mermaid
mindmap
  root((Simple<br/>Calculator))
    Developer Flow
      Write Code
      Run Tests
      View Reports
      Commit Changes
    Quality Gates
      Pre-commit Hooks
        Gitleaks
        Ruff Linter
        Ruff Formatter
        File Checks
      CI Checks
        Lint Job
        Security Job
        Test Job
    Testing
      pytest Framework
      5 Test Cases
      Edge Cases
      Fixtures
    Reporting
      pytest-html
        Quick local view
        reports/test-report.html
      Allure
        Enterprise features
        Historical trends
        Flaky detection
    CI/CD
      GitHub Actions
        Multi-layer cache
        Parallel jobs
        Sequential jobs
      Deployment
        GitHub Pages
        Public URL
        Free hosting
    Tools
      Python 3.9+
      pip & uv
      pyproject.toml
      Git & GitHub
```

---

## Quick Reference

### Key URLs
- **Live Reports**: `https://username.github.io/simple-calculator-demo/`
- **Repository**: GitHub repo URL
- **Workflow Runs**: GitHub Actions tab

### Key Commands
```bash
# Local development
pytest                                    # Quick test
pytest --alluredir=allure-results        # Generate Allure data
allure serve allure-results              # View Allure report

# Pre-commit
pre-commit install                       # One-time setup
pre-commit run --all-files              # Manual run

# Package management
pip install -r requirements.txt         # Traditional
uv pip install -e ".[dev]"             # Modern & fast
```

### Key Files
- `calculator/calculator.py` - Main code
- `tests/test_calculator.py` - Test cases
- `.github/workflows/tests.yml` - CI/CD pipeline
- `.pre-commit-config.yaml` - Pre-commit hooks
- `pyproject.toml` - Project configuration

---

## Learning Path

1. **Start here**: Understand the [Complete System Overview](#complete-system-overview)
2. **Follow the flow**: Trace through [Developer Workflow](#developer-workflow)
3. **See automation**: Check [Pre-commit Hook Flow](#pre-commit-hook-flow)
4. **Understand CI/CD**: Study [CI/CD Pipeline Flow](#cicd-pipeline-flow)
5. **Deep dive**: Explore [Data Flow Architecture](#data-flow-architecture)

---

## Next Steps

- See `guides/README.md` for step-by-step tutorials
- Read `docs/ARCHITECTURE.md` for detailed technical info
- Check `docs/CI-CD.md` for CI/CD insights
- View `docs/ALLURE.md` for reporting details

---

**Remember**: Simple outside (basic calculator), sophisticated inside (enterprise infrastructure)! 🎯

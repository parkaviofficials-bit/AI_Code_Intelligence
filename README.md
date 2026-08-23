# AI Code Intelligence

AI Code Intelligence is a Python-based source code analysis and forensic comparison system developed as a final-year project.

The application analyzes Python programs using static source-code analysis and provides information about code complexity, quality, security patterns, bug risk, and structural similarity.

The project includes a Streamlit web interface for interacting with the analysis tools.

## Features

### Code Analysis

The application accepts Python source files and extracts structural information using Python's Abstract Syntax Tree (AST).

The analysis includes:

- Lines of code
- Functions and classes
- Conditional statements
- Loops
- Return statements
- Function calls
- Imports
- Average function length
- Cyclomatic complexity

The extracted information is used by the quality, security, bug prediction, and recommendation modules.

### Code Quality

The quality analyzer evaluates the extracted code metrics and produces a quality score.

It can identify issues such as:

- High cyclomatic complexity
- Large functions
- Excessive conditional branching
- Other maintainability concerns

The recommendation engine converts these findings into suggestions for improving the source code.

### Security Analysis

The security analyzer checks Python source code for potentially unsafe patterns implemented in the analysis rules.

Detected issues are reported with their severity, source line, explanation, and recommended action.

### Bug Risk Prediction

The project includes a Random Forest based demonstration model for estimating potential bug risk.

The prediction is based on extracted source-code characteristics. The application also displays important features that influenced the model prediction.

The prediction is intended for analysis and research purposes rather than as a definitive measurement of software reliability.

### Code DNA

The Code DNA module represents a program using a structural feature sequence.

A SHA-256 fingerprint is also generated for the analyzed code representation.

Example:

```text
4-0-11-2-5-14-1-28.5-14
````

### Code Forensics

The forensic module compares two Python programs using their extracted structural features.

The comparison provides:

* Structural similarity percentage
* Similarity assessment
* Feature comparison
* Structural DNA comparison
* Forensic explanation

Structural similarity is intended to describe similarities in program structure. It should not be treated as proof of plagiarism or common authorship.

## System Overview

```text
Python Source Code
        |
        v
    AST Parsing
        |
        v
 Feature Extraction
        |
        +-------------------+
        |                   |
        v                   v
 Code Quality       Security Analysis
        |
        v
 Bug Risk Prediction
        |
        v
 Recommendations
        |
        v
    Code DNA
```

For forensic comparison:

```text
             Python Program A
                    |
                    v
             Feature Extraction
                    |
                    |
                    +------+
                           |
                           v
                    Similarity Analysis
                           ^
                           |
                    +------+
                    |
                    v
             Feature Extraction
                    ^
                    |
             Python Program B
```

## Project Structure

```text
AI_Code_Intelligence/
|
├── analyzer/
|   ├── __init__.py
|   ├── bug_predictor.py
|   ├── code_dna.py
|   ├── complexity_analyzer.py
|   ├── dna_similarity.py
|   ├── feature_extractor.py
|   ├── forensic_analyzer.py
|   ├── quality_analyzer.py
|   ├── recommendation_engine.py
|   └── security_analyzer.py
|
├── test_code/
|   ├── complex_sample.py
|   ├── sample.py
|   ├── sample2.py
|   └── security_sample.py
|
├── tests/
|   ├── test_bug_predictor.py
|   ├── test_code_dna.py
|   ├── test_dna_similarity.py
|   ├── test_feature_extractor.py
|   ├── test_quality_analyzer.py
|   ├── test_recommendation_engine.py
|   └── test_security_analyzer.py
|
├── app.py
├── analyze.py
├── compare.py
├── .gitignore
└── README.md
```

## Technologies

| Technology    | Purpose                     |
| ------------- | --------------------------- |
| Python        | Core implementation         |
| Streamlit     | Web interface               |
| Python AST    | Static source-code analysis |
| Scikit-learn  | Bug-risk prediction         |
| Random Forest | Machine-learning model      |
| Pytest        | Automated testing           |
| SHA-256       | Code fingerprinting         |
| Git           | Version control             |
| GitHub        | Source-code hosting         |

## Installation

Clone the repository:

```bash
git clone https://github.com/parkaviofficials-bit/AI_Code_Intelligence.git
```

Move into the project directory:

```bash
cd AI_Code_Intelligence
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install streamlit scikit-learn pytest
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application provides two main sections:

* Code Analysis
* Code Forensics

In Code Analysis, upload a Python source file and run the analysis.

In Code Forensics, upload two Python files and compare their structural characteristics.

## Testing

The project contains automated tests for the core analysis modules.

Run the complete test suite:

```bash
python -m pytest
```

The current test suite covers:

* Feature extraction
* Quality analysis
* Security analysis
* Bug prediction
* Recommendation generation
* Code DNA generation
* DNA similarity

Current test status:

```text
7 passed
```

## Example Analysis

For a sample Python program, the analyzer can produce metrics such as:

```text
Lines of Code:          50
Functions:               4
Classes:                 0
If Statements:          11
Loops:                   2
Returns:                 5
Function Calls:         14
Cyclomatic Complexity:  14
```

Based on these metrics, the system can identify high complexity and provide recommendations such as splitting large functions or simplifying nested conditional logic.

## Limitations

The bug-risk prediction model is a demonstration model developed for this project. Its output should not be considered a definitive prediction of software defects.

Security analysis is limited to the rules implemented in the project and should not replace a professional security assessment.

The forensic similarity score measures structural characteristics and does not establish plagiarism, authorship, or code ownership.

## Future Work

Future development could include:

* Support for additional programming languages
* Additional security detection rules
* Code smell detection
* Duplicate-code detection
* More advanced machine-learning models
* GitHub repository analysis
* Historical code-quality tracking
* CI/CD integration
* Automated refactoring suggestions

## Project Status

The core code analysis and forensic comparison functionality has been implemented.

The Streamlit interface is operational, the main analysis modules have automated tests, and the current test suite passes successfully.

## Author

Parkavi_off



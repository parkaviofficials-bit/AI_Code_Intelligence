\# 🧠 AI Code Intelligence



An AI-powered Python code analysis and forensic comparison platform built with Python and Streamlit.



AI Code Intelligence analyzes Python source code across multiple dimensions including code quality, cyclomatic complexity, security, bug risk, structural characteristics, and code similarity.



\## 🚀 Features



\### 🔍 Code Analysis



Upload a Python source file and receive:



\- Lines of code

\- Function and class counts

\- If-statement and loop counts

\- Return and function-call counts

\- Import counts

\- Average function length

\- Cyclomatic complexity

\- Code quality score

\- Maintainability recommendations

\- Security analysis

\- Bug-risk prediction

\- Model feature importance

\- Structural Code DNA

\- SHA-256 code fingerprint



\### 🧬 Code Forensics



Compare two Python programs based on their structural characteristics.



The forensic module provides:



\- Structural similarity percentage

\- Similarity assessment

\- Feature-by-feature comparison

\- Structural DNA comparison

\- Forensic explanation



\### 🤖 Bug Risk Prediction



A Random Forest demonstration model estimates potential bug risk using extracted code metrics.



The system also displays the features that contribute most strongly to the model's prediction.



\### 🔐 Security Analysis



The security analyzer checks Python source code for potentially unsafe coding patterns and provides recommendations when issues are detected.



\### 🧬 Code DNA



Each analyzed program is represented by a structural DNA sequence based on extracted code characteristics.



A SHA-256 fingerprint is also generated to provide a deterministic identifier for the analyzed source structure.



\## 🏗️ System Architecture



```text

&#x20;                   ┌──────────────────────┐

&#x20;                   │    Streamlit App     │

&#x20;                   │       app.py         │

&#x20;                   └──────────┬───────────┘

&#x20;                              │

&#x20;             ┌────────────────┼────────────────┐

&#x20;             │                │                │

&#x20;             ▼                ▼                ▼

&#x20;     ┌──────────────┐ ┌──────────────┐ ┌──────────────┐

&#x20;     │   Feature    │ │   Quality    │ │   Security   │

&#x20;     │  Extractor   │ │   Analyzer   │ │   Analyzer   │

&#x20;     └──────────────┘ └──────────────┘ └──────────────┘

&#x20;             │                │                │

&#x20;             └────────────────┼────────────────┘

&#x20;                              ▼

&#x20;                   ┌──────────────────────┐

&#x20;                   │    Bug Predictor     │

&#x20;                   └──────────┬───────────┘

&#x20;                              │

&#x20;             ┌────────────────┼────────────────┐

&#x20;             ▼                ▼                ▼

&#x20;     ┌──────────────┐ ┌──────────────┐ ┌──────────────┐

&#x20;     │Recommendation│ │  Code DNA    │ │  Forensics   │

&#x20;     │    Engine    │ │  Generator   │ │   Analysis   │

&#x20;     └──────────────┘ └──────────────┘ └──────────────┘

````



\## 📂 Project Structure



```text

AI\_Code\_Intelligence/

│

├── app.py

├── analyze.py

├── compare.py

│

├── analyzer/

│   ├── \_\_init\_\_.py

│   ├── bug\_predictor.py

│   ├── code\_dna.py

│   ├── complexity\_analyzer.py

│   ├── dna\_similarity.py

│   ├── feature\_extractor.py

│   ├── forensic\_analyzer.py

│   ├── quality\_analyzer.py

│   ├── recommendation\_engine.py

│   └── security\_analyzer.py

│

├── test\_code/

│   ├── complex\_sample.py

│   ├── sample.py

│   ├── sample2.py

│   └── security\_sample.py

│

├── tests/

│   ├── test\_bug\_predictor.py

│   ├── test\_code\_dna.py

│   ├── test\_dna\_similarity.py

│   ├── test\_feature\_extractor.py

│   ├── test\_quality\_analyzer.py

│   ├── test\_recommendation\_engine.py

│   └── test\_security\_analyzer.py

│

├── .gitignore

└── README.md

```



\## 🛠️ Technologies Used



\* Python 3.10+

\* Streamlit

\* Python AST

\* Scikit-learn

\* Random Forest

\* Pytest

\* SHA-256

\* Git \& GitHub



\## ⚙️ Installation



Clone the repository:



```bash

git clone https://github.com/parkaviofficials-bit/AI\_Code\_Intelligence.git

```



Navigate to the project:



```bash

cd AI\_Code\_Intelligence

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate it on Windows:



```powershell

venv\\Scripts\\Activate.ps1

```



Install dependencies:



```bash

pip install streamlit scikit-learn pytest

```



\## ▶️ Run the Application



Start the Streamlit application:



```bash

streamlit run app.py

```



The application will open in your browser.



\## 🧪 Run Tests



Run the complete automated test suite:



```bash

python -m pytest

```



The current test suite validates:



\* Feature extraction

\* Quality analysis

\* Security analysis

\* Bug prediction

\* Recommendation generation

\* Code DNA generation

\* DNA similarity



\## 📊 Example Analysis



For a complex Python program, the system can report metrics such as:



```text

Lines of Code:              50

Functions:                   4

Classes:                     0

Cyclomatic Complexity:      14

If Statements:              11

Loops:                       2

Returns:                     5

Function Calls:             14

```



The system can then generate recommendations such as:



```text

Complexity — High cyclomatic complexity detected.



Recommendation:

Break complex logic into smaller functions and

simplify deeply nested conditional branches.

```



\## 🧬 Code Forensics Example



The forensic module compares two programs using their structural features.



Example:



```text

Code A DNA:

4-0-11-2-5-14-1-28.5-14



Code B DNA:

3-1-1-1-2-3-1-7.0-3



Structural Similarity:

68.21%



Assessment:

MODERATE

```



The similarity score represents structural similarity based on the extracted feature representation. It should not be interpreted as proof that two programs contain identical source code.



\## 🔬 Methodology



The system uses Python's Abstract Syntax Tree (AST) to analyze source code without executing the submitted program.



The feature extraction pipeline identifies structural characteristics including:



1\. Functions

2\. Classes

3\. Conditional statements

4\. Loops

5\. Return statements

6\. Function calls

7\. Imports

8\. Function length

9\. Cyclomatic complexity



These features are then used by the different analysis modules.



\## 🎯 Project Objectives



The main objectives of AI Code Intelligence are:



\* Automate Python source-code analysis

\* Identify maintainability problems

\* Detect potentially risky coding patterns

\* Estimate bug risk

\* Provide explainable recommendations

\* Generate structural code fingerprints

\* Compare programs based on structural characteristics

\* Provide a practical developer-oriented analysis dashboard



\## 🔮 Future Enhancements



Possible future improvements include:



\* Support for additional programming languages

\* Advanced machine-learning models

\* Code smell detection

\* Duplicate-code detection

\* Vulnerability classification

\* GitHub repository analysis

\* Historical code-quality tracking

\* Interactive visualizations

\* Developer dashboards

\* Automated refactoring suggestions

\* CI/CD integration



\## ⚠️ Disclaimer



The bug-risk prediction and similarity analysis are intended as demonstration and research features.



Predictions should not be treated as definitive proof of software defects, security vulnerabilities, authorship, or code plagiarism.



\## 👨‍💻 Author



\*\*Parkavi\_off\*\*



AI Code Intelligence — Final Year Project



\## 📄 License



This project is currently intended for academic and educational purposes.


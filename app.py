import streamlit as st
import tempfile
import os

from analyzer.feature_extractor import extract_features
from analyzer.quality_analyzer import calculate_quality_score
from analyzer.security_analyzer import analyze_security
from analyzer.bug_predictor import predict_bug_risk
from analyzer.code_dna import generate_code_dna
from analyzer.recommendation_engine import generate_recommendations

from analyzer.dna_similarity import calculate_similarity
from analyzer.forensic_analyzer import generate_forensic_report


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Code Intelligence",
    page_icon="🧠",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🧠 AI Code Intelligence")
st.subheader("Code Analysis & Forensics Platform")

st.write(
    "Analyze source code quality, security, bug risk, "
    "structural characteristics, and code similarity."
)

st.divider()


# ============================================================
# TABS
# ============================================================

analysis_tab, forensic_tab = st.tabs(
    ["🔍 Code Analysis", "🧬 Code Forensics"]
)


# ============================================================
# TAB 1 — CODE ANALYSIS
# ============================================================

with analysis_tab:

    st.header("🔍 Analyze Python Code")

    uploaded_file = st.file_uploader(
        "Upload a Python source file",
        type=["py"],
        key="analysis_file"
    )

    if uploaded_file is not None:

        st.success(
            f"Uploaded: {uploaded_file.name}"
        )

        code = uploaded_file.read().decode("utf-8")

        with st.expander("📄 View Source Code"):

            st.code(
                code,
                language="python"
            )

        if st.button(
            "🔍 Analyze Code",
            type="primary",
            key="analyze_button"
        ):

            temp_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".py",
                mode="w",
                encoding="utf-8"
            )

            temp_file.write(code)
            temp_file.close()

            file_path = temp_file.name

            try:

                with st.spinner(
                    "Analyzing source code..."
                ):

                    # ------------------------------------------------
                    # FEATURE EXTRACTION
                    # ------------------------------------------------

                    features = extract_features(file_path)
    

                    # ------------------------------------------------
                    # CODE QUALITY
                    # ------------------------------------------------

                    quality = calculate_quality_score(
                        features
                    )

                    # ------------------------------------------------
                    # SECURITY ANALYSIS
                    # ------------------------------------------------

                    security_findings = analyze_security(
                        file_path
                    )

                    # ------------------------------------------------
                    # BUG RISK PREDICTION
                    # ------------------------------------------------

                    bug_risk = predict_bug_risk(
                        features
                    )

                    # ------------------------------------------------
                    # AI RECOMMENDATIONS
                    # ------------------------------------------------

                    recommendations = generate_recommendations(
                        features,
                        security_findings,
                        bug_risk
                    )

                    # ------------------------------------------------
                    # CODE DNA
                    # ------------------------------------------------

                    dna = generate_code_dna(
                        features
                    )

                # ====================================================
                # AI RECOMMENDATIONS
                # ====================================================

                st.header("💡 AI Recommendations")

                for item in recommendations:

                    if item["severity"] == "HIGH":

                        st.error(
                            f"🔴 {item['type']} — {item['message']}"
                        )

                    elif item["severity"] == "MEDIUM":

                        st.warning(
                            f"🟡 {item['type']} — {item['message']}"
                        )

                    else:

                        st.success(
                            f"🟢 {item['message']}"
                        )

                    st.write(
                        "**Recommendation:**",
                        item["recommendation"]
                    )

                st.success(
                    "🎯 AI Code Intelligence analysis complete."
                )

                # ====================================================
                # CODE METRICS
                # ====================================================

                st.header("📊 Code Metrics")

                col1, col2, col3, col4 = st.columns(4)

                col1.metric(
                    "Lines of Code",
                    features["lines_of_code"]
                )

                col2.metric(
                    "Functions",
                    features["functions"]
                )

                col3.metric(
                    "Classes",
                    features["classes"]
                )

                col4.metric(
                    "Complexity",
                    features["cyclomatic_complexity"]
                )

                col5, col6, col7, col8 = st.columns(4)

                col5.metric(
                    "If Statements",
                    features["if_statements"]
                )

                col6.metric(
                    "Loops",
                    features["loops"]
                )

                col7.metric(
                    "Returns",
                    features["returns"]
                )

                col8.metric(
                    "Function Calls",
                    features["function_calls"]
                )

                # ====================================================
                # CODE QUALITY
                # ====================================================

                st.header("🟢 Code Quality")

                q1, q2 = st.columns(2)

                with q1:

                    st.metric(
                        "Quality Score",
                        f"{quality['score']} / 100"
                    )

                with q2:

                    st.metric(
                        "Category",
                        quality["category"]
                    )

                if quality["reasons"]:

                    st.warning("Quality Issues")

                    for reason in quality["reasons"]:

                        st.write(
                            "•",
                            reason
                        )

                else:

                    st.success(
                        "No major quality issues detected."
                    )

                # ====================================================
                # SECURITY ANALYSIS
                # ====================================================

                st.header("🔐 Security Analysis")

                if security_findings:

                    st.error(
                        f"{len(security_findings)} "
                        "security issue(s) detected."
                    )

                    for finding in security_findings:

                        with st.expander(
                            f"{finding['severity']} — "
                            f"{finding['type']}"
                        ):

                            st.write(
                                "**Line:**",
                                finding["line"]
                            )

                            st.write(
                                "**Message:**",
                                finding["message"]
                            )

                            st.write(
                                "**Recommendation:**",
                                finding["recommendation"]
                            )

                else:

                    st.success(
                        "✓ No security issues detected."
                    )

                # ====================================================
                # BUG RISK
                # ====================================================

                st.header("🐞 Bug Risk")

                b1, b2 = st.columns(2)

                with b1:

                    st.metric(
                        "Risk Level",
                        bug_risk["risk_level"]
                    )

                with b2:

                    st.metric(
                        "Risk Probability",
                        f"{bug_risk['risk_probability']}%"
                    )

                # ====================================================
                # BUG RISK EXPLAINABILITY
                # ====================================================

                if "top_features" in bug_risk:

                    st.subheader(
                        "🔎 Model Influencing Features"
                    )

                    st.caption(
                        "These features have the highest learned "
                        "importance in the Random Forest "
                        "demonstration model."
                    )

                    for item in bug_risk["top_features"]:

                        st.write(
                            f"**{item['feature']}** — "
                            f"Importance: {item['importance']}"
                        )

                # ====================================================
                # CODE DNA
                # ====================================================

                st.header("🧬 Code DNA")

                st.write(
                    "**Structural DNA**"
                )

                st.code(
                    dna["dna_string"]
                )

                st.write(
                    "**SHA-256 Fingerprint**"
                )

                st.code(
                    dna["fingerprint"]
                )

                st.divider()

                st.success(
                    "🎯 AI Code Intelligence analysis complete."
                )

            except SyntaxError as error:

                st.error(
                    "❌ Invalid Python syntax."
                )

                st.write(
                    f"Line: {error.lineno}"
                )

                st.write(
                    f"Message: {error.msg}"
                )

            except Exception as error:

                st.error(
                    "❌ An error occurred during analysis."
                )

                st.exception(error)

            finally:

                if os.path.exists(file_path):

                    os.remove(file_path)


# ============================================================
# TAB 2 — CODE FORENSICS
# ============================================================

with forensic_tab:

    st.header("🧬 Code Forensics")

    st.write(
        "Compare two Python programs based on their "
        "structural characteristics."
    )

    file_a = st.file_uploader(
        "Upload Code A",
        type=["py"],
        key="forensic_a"
    )

    file_b = st.file_uploader(
        "Upload Code B",
        type=["py"],
        key="forensic_b"
    )

    if file_a is not None and file_b is not None:

        st.success(
            f"Code A: {file_a.name}  |  Code B: {file_b.name}"
        )

        if st.button(
            "🧬 Compare Code",
            type="primary",
            key="compare_button"
        ):

            temp_a = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".py",
                mode="w",
                encoding="utf-8"
            )

            temp_a.write(
                file_a.read().decode("utf-8")
            )

            temp_a.close()

            temp_b = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".py",
                mode="w",
                encoding="utf-8"
            )

            temp_b.write(
                file_b.read().decode("utf-8")
            )

            temp_b.close()

            path_a = temp_a.name
            path_b = temp_b.name

            try:

                with st.spinner(
                    "Comparing code structures..."
                ):

                    # ------------------------------------------------
                    # FEATURE EXTRACTION
                    # ------------------------------------------------

                    features_a = extract_features(
                        path_a
                    )

                    features_b = extract_features(
                        path_b
                    )

                    # ------------------------------------------------
                    # SIMILARITY
                    # ------------------------------------------------

                    similarity = calculate_similarity(
                        features_a,
                        features_b
                    )

                    # ------------------------------------------------
                    # FORENSIC REPORT
                    # ------------------------------------------------

                    report = generate_forensic_report(
                        similarity
                    )

                st.success(
                    "✅ Forensic comparison completed!"
                )

                # ====================================================
                # STRUCTURAL SIMILARITY
                # ====================================================

                st.header(
                    "🔬 Structural Similarity"
                )

                s1, s2 = st.columns(2)

                with s1:

                    st.metric(
                        "Similarity",
                        f"{report['similarity']}%"
                    )

                with s2:

                    st.metric(
                        "Assessment",
                        report["assessment"]
                    )

                st.info(
                    report["explanation"]
                )

                # ====================================================
                # FEATURE COMPARISON
                # ====================================================

                st.header(
                    "📊 Feature Comparison"
                )

                feature_names = [
                    "functions",
                    "classes",
                    "if_statements",
                    "loops",
                    "returns",
                    "function_calls",
                    "imports",
                    "average_function_length",
                    "cyclomatic_complexity"
                ]

                comparison_data = []

                for feature in feature_names:

                    comparison_data.append(
                        {
                            "Feature": feature,
                            "Code A": features_a[feature],
                            "Code B": features_b[feature]
                        }
                    )

                st.dataframe(
                    comparison_data,
                    use_container_width=True,
                    hide_index=True
                )

                # ====================================================
                # DNA COMPARISON
                # ====================================================

                st.header(
                    "🧬 Structural DNA"
                )

                dna_a = generate_code_dna(
                    features_a
                )

                dna_b = generate_code_dna(
                    features_b
                )

                dna_col1, dna_col2 = st.columns(2)

                with dna_col1:

                    st.write(
                        f"**{file_a.name}**"
                    )

                    st.code(
                        dna_a["dna_string"]
                    )

                with dna_col2:

                    st.write(
                        f"**{file_b.name}**"
                    )

                    st.code(
                        dna_b["dna_string"]
                    )

                st.divider()

                st.success(
                    "🎯 Code forensic analysis complete."
                )

            except SyntaxError as error:

                st.error(
                    "❌ One of the files contains invalid Python syntax."
                )

                st.write(
                    f"Line: {error.lineno}"
                )

                st.write(
                    f"Message: {error.msg}"
                )

            except Exception as error:

                st.error(
                    "❌ An error occurred during forensic analysis."
                )

                st.exception(error)

            finally:

                if os.path.exists(path_a):

                    os.remove(path_a)

                if os.path.exists(path_b):

                    os.remove(path_b)
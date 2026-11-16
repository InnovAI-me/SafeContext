"""
SafeContext: Integrating Data Governance, Explainable AI for Customer Experience,
and Runtime Monitoring for Intelligent Systems.

Main research pipeline and experiment runner.
"""
import os
import sys

PROJECT_TITLE = (
    "SafeContext: Integrating Data Governance, Explainable AI for Customer "
    "Experience and Runtime Monitoring for Intelligent Systems"
)

def init_workspace():
    """Ensure standard research directories exist."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folders = [
        os.path.join(base_dir, "data", "raw"),
        os.path.join(base_dir, "data", "processed"),
        os.path.join(base_dir, "data", "governance_policies"),
        os.path.join(base_dir, "notebooks"),
        os.path.join(base_dir, "src"),
        os.path.join(base_dir, "results", "figures"),
        os.path.join(base_dir, "results", "logs"),
        os.path.join(base_dir, "results", "explanations"),
        os.path.join(base_dir, "results", "monitoring_metrics"),
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print(f"[{PROJECT_TITLE}]\n-> All research directories initialized successfully.")

def main():
    print("=" * 80)
    print(f"PROJECT: {PROJECT_TITLE}")
    print("=" * 80)
    init_workspace()
    print("SafeContext pipeline is ready for experiments.")

if __name__ == "__main__":
    main()

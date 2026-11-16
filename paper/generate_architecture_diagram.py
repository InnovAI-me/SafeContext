"""
Script to generate a publication-grade, high-resolution architecture diagram
for the SafeContext framework (IJACSA Vol. 17, Issue 10, 2026).
Saved as paper/safecontext_architecture.png.
"""
import os
import sys

# Ensure binary dependencies (numpy/scipy) load from system-approved location under Application Control
sys_site = r"C:\Users\maniv\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages"
if os.path.exists(sys_site) and sys_site not in sys.path:
    sys.path.insert(0, sys_site)

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ArrowStyle, ConnectionPatch

def create_architecture_diagram(output_path: str):
    # Set high DPI and publication figure dimensions
    fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Background canvas color
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    # Colors palette (academic navy, slate, teal, amber, ruby, subtle fills)
    c_phase1_bg = '#F0F4F8'
    c_phase1_border = '#102C57'
    c_phase2_bg = '#F3F8F2'
    c_phase2_border = '#1B5E20'
    c_phase3_bg = '#FDF6F0'
    c_phase3_border = '#B71C1C'

    c_box_bg = '#FFFFFF'
    c_text_dark = '#1A202C'
    c_text_muted = '#4A5568'
    c_accent_blue = '#1E88E5'
    c_accent_green = '#2E7D32'
    c_accent_red = '#C62828'
    c_accent_amber = '#E65100'

    # Title Banner
    ax.text(8.0, 9.6, "SafeContext: End-to-End Enterprise AI Lifecycle Governance Architecture",
            ha='center', va='center', fontsize=18, fontweight='bold', color='#0F172A', fontname='DejaVu Sans')
    ax.text(8.0, 9.25, "Synchronized Lifecycle Continuum: Data Valuation, CX-Centric Explainability & Autonomous Runtime Guardrails",
            ha='center', va='center', fontsize=11, fontstyle='italic', color='#475569', fontname='DejaVu Sans')

    # Draw 3 Phase Columns / Containers
    col_width = 4.8
    col_y = 1.0
    col_height = 7.9
    
    # Phase 1: Ideation & Data Valuation
    p1_box = FancyBboxPatch((0.5, col_y), col_width, col_height,
                            boxstyle="round,pad=0.2,rounding_size=0.3",
                            ec=c_phase1_border, fc=c_phase1_bg, lw=2.0, ls='-', zorder=1)
    ax.add_patch(p1_box)

    # Phase 2: Acceptance & Explainability
    p2_box = FancyBboxPatch((5.6, col_y), col_width, col_height,
                            boxstyle="round,pad=0.2,rounding_size=0.3",
                            ec=c_phase2_border, fc=c_phase2_bg, lw=2.0, ls='-', zorder=1)
    ax.add_patch(p2_box)

    # Phase 3: Runtime Monitoring & Guardrails
    p3_box = FancyBboxPatch((10.7, col_y), col_width, col_height,
                            boxstyle="round,pad=0.2,rounding_size=0.3",
                            ec=c_phase3_border, fc=c_phase3_bg, lw=2.0, ls='-', zorder=1)
    ax.add_patch(p3_box)

    # Phase Header Badges
    def draw_phase_header(cx, title, subtitle, bg_color, text_color):
        badge = FancyBboxPatch((cx - 2.2, 8.2), 4.4, 0.65,
                               boxstyle="round,pad=0.1,rounding_size=0.15",
                               ec='none', fc=bg_color, zorder=2)
        ax.add_patch(badge)
        ax.text(cx, 8.58, title, ha='center', va='center', fontsize=11.5, fontweight='bold', color='#FFFFFF')
        ax.text(cx, 8.35, subtitle, ha='center', va='center', fontsize=8.5, color='#E2E8F0')

    draw_phase_header(2.9, "PHASE 1: IDEATION & VALUATION", "Data Asset Valuation & Policy Synthesis", c_phase1_border, '#FFFFFF')
    draw_phase_header(8.0, "PHASE 2: ACCEPTANCE & XAI", "Fidelity Testing & CX Trust Verification", c_phase2_border, '#FFFFFF')
    draw_phase_header(13.1, "PHASE 3: RUNTIME GUARDRAILS", "Continuous Drift Observability & Circuit Breakers", c_phase3_border, '#FFFFFF')

    # Helper function to draw an operational module card inside a phase
    def draw_module_card(x, y, w, h, title, items, tag, tag_color, border_color='#CBD5E1'):
        card = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15,rounding_size=0.15",
                              ec=border_color, fc=c_box_bg, lw=1.2, zorder=3)
        ax.add_patch(card)
        # Tag pill
        tag_w = len(tag) * 0.08 + 0.3
        tag_patch = FancyBboxPatch((x + w - tag_w - 0.15, y + h - 0.35), tag_w, 0.24,
                                   boxstyle="round,pad=0.04,rounding_size=0.08",
                                   ec='none', fc=tag_color, zorder=4)
        ax.add_patch(tag_patch)
        ax.text(x + w - tag_w / 2.0 - 0.15, y + h - 0.23, tag,
                ha='center', va='center', fontsize=6.8, fontweight='bold', color='#FFFFFF')

        # Card Title
        ax.text(x + 0.2, y + h - 0.25, title, ha='left', va='center',
                fontsize=9.2, fontweight='bold', color=c_text_dark, zorder=4)
        
        # Divider line
        ax.plot([x + 0.2, x + w - 0.2], [y + h - 0.42, y + h - 0.42], color='#E2E8F0', lw=0.8, zorder=4)

        # Content bullets
        line_y = y + h - 0.65
        for item in items:
            ax.text(x + 0.25, line_y, f"•  {item}", ha='left', va='center',
                    fontsize=7.6, color=c_text_muted, zorder=4)
            line_y -= 0.24

    # ---------------- PHASE 1 MODULES ----------------
    # 1. Ingestion & Feature Discovery
    draw_module_card(0.7, 6.7, 4.4, 1.3, "1. Enterprise Data Intake & Lineage",
                     ["Raw tabular / unstructured feature cataloging",
                      "Automated provenance tracking & metadata profiling",
                      "Data schema validation & type invariant checks"],
                     "INPUT", '#475569')

    # 2. Valuation Formulation Engine
    draw_module_card(0.7, 5.0, 4.4, 1.5, "2. Quantitative Data Valuation V(D)",
                     ["V(D) = [Utility(D) x Uniqueness(D)] - [Risk(D) x Pen(D)]",
                      "Predictive marginal gain via Shapley approximation",
                      "Privacy liability & commercial penalty quantification",
                      "Cost-benefit boundary computation per feature"],
                     "ALGORITHM", c_accent_blue, border_color='#93C5FD')

    # 3. Four-Tier Sensitivity Classifier
    draw_module_card(0.7, 3.3, 4.4, 1.5, "3. Multi-Tier Sensitivity Partitioning",
                     ["Tier 1: Public (Unrestricted model ingestion)",
                      "Tier 2: Internal (Role-based access & basic audit)",
                      "Tier 3: Confidential (Differential privacy / noise injection)",
                      "Tier 4: Restricted PII (Strict pseudonymization / masking)"],
                     "CLASSIFIER", '#6366F1')

    # 4. Policy Generator & Compliance Mapping
    draw_module_card(0.7, 1.3, 4.4, 1.8, "4. Policy Synthesis & Regulatory Mapping",
                     ["EU AI Act (High-Risk AI conformity & Article 10/14)",
                      "GDPR (Article 22 explanation & Article 25 privacy by design)",
                      "NIST AI RMF 1.0 (Govern, Map, Measure, Manage)",
                      "Synthesized parameter matrix for training constraints",
                      "Tamper-proof compliance audit manifest export"],
                     "GOVERNANCE", c_phase1_border, border_color='#94A3B8')

    # ---------------- PHASE 2 MODULES ----------------
    # 1. Model Staging & Attribution
    draw_module_card(5.8, 6.7, 4.4, 1.3, "1. Candidate Model Staging & Attribution",
                     ["Black-box & glass-box candidate ingestion",
                      "Local attribution extraction (TreeSHAP, KernelSHAP)",
                      "Integrated Gradients for deep neural representations"],
                     "AUDIT", '#0D9488')

    # 2. Explanation Fidelity & Counterfactuals
    draw_module_card(5.8, 4.9, 4.4, 1.6, "2. CX Explanation Translation Layer",
                     ["Technical SHAP vectors -> Plain natural language",
                      "Feasible counterfactual generation ('What-if' recourse)",
                      "Contrastive rationales tailored to consumer personas",
                      "Fidelity score validation (Faithfulness F >= 0.90)"],
                     "XAI CORE", c_accent_green, border_color='#86EFAC')

    # 3. Algorithmic Fairness & Bias Disparity
    draw_module_card(5.8, 3.2, 4.4, 1.5, "3. Bias Disparity & Demographic Parity",
                     ["Disparate impact ratio across protected groups",
                      "Equalized odds & calibration equity validation",
                      "Counterfactual fairness across sensitive attributes",
                      "Automated debiasing reweighting recommendations"],
                     "FAIRNESS", '#059669')

    # 4. CTI Gatekeeper & Release Sign-off
    draw_module_card(5.8, 1.3, 4.4, 1.7, "4. Customer Trust Index (CTI) Gatekeeper",
                     ["CTI = a*Clarity + b*Alignment + g*(1 - Disparity)",
                      "Calibrated threshold: CTI >= 0.85 required for release",
                      "Human-in-the-loop compliance officer sign-off",
                      "Cryptographic model card generation & deployment token"],
                     "GATEKEEPER", c_phase2_border, border_color='#A7F3D0')

    # ---------------- PHASE 3 MODULES ----------------
    # 1. Runtime Production Inference Gateway
    draw_module_card(10.9, 6.7, 4.4, 1.3, "1. Production Inference Interceptor",
                     ["High-throughput, non-blocking asynchronous proxy",
                      "In-flight PII redaction & prompt sanitization",
                      "Sub-millisecond inference intercept latency"],
                     "INGRESS", '#D97706')

    # 2. Statistical & Semantic Drift Detection
    draw_module_card(10.9, 4.9, 4.4, 1.6, "2. Context Drift & Covariate Monitor",
                     ["Population Stability Index (PSI): PSI > 0.10 trigger",
                      "Wasserstein distance (W1) for continuous distributions",
                      "Semantic embedding drift via vector cosine divergence",
                      "Multi-turn context creep detection in conversational AI"],
                     "ANALYTICS", c_accent_red, border_color='#FCA5A5')

    # 3. Latency & SLA Tracking
    draw_module_card(10.9, 3.2, 4.4, 1.5, "3. Latency Telemetry & SLA Tracking",
                     ["Continuous P95/P99 latency budget tracking",
                      "Governance pipeline execution overhead (< 10 ms)",
                      "Hardware memory / GPU saturation watchdog",
                      "Real-time streaming telemetry dashboard integration"],
                     "TELEMETRY", '#B45309')

    # 4. Automated Circuit Breaker & Fallback
    draw_module_card(10.9, 1.3, 4.4, 1.7, "4. Automated Circuit Breaker & Fallback",
                     ["Delta_drift > 0.05 or Latency > 100ms trip logic",
                      "Zero-downtime routing to verified baseline / rule fallback",
                      "Graceful degradation with explainable customer alert",
                      "Automated incident ticket & telemetry snapshot logging"],
                     "RECOVERY", c_phase3_border, border_color='#FECACA')

    # ---------------- CONNECTING ARROWS & LIFECYCLE FLOW ----------------
    # Inter-phase primary flow arrows
    # Phase 1 to Phase 2 (Governed Model & Constraint Package)
    ax.annotate("", xy=(5.5, 5.0), xytext=(5.1, 5.0),
                arrowprops=dict(arrowstyle="-|>", color='#102C57', lw=2.5, mutation_scale=18))
    ax.text(5.3, 5.25, "Governed\nArtifacts", ha='center', va='bottom',
            fontsize=7.5, fontweight='bold', color='#102C57', backgroundcolor='#FFFFFF')

    # Phase 2 to Phase 3 (Approved Model & Explanation Policies)
    ax.annotate("", xy=(10.6, 5.0), xytext=(10.2, 5.0),
                arrowprops=dict(arrowstyle="-|>", color='#1B5E20', lw=2.5, mutation_scale=18))
    ax.text(10.4, 5.25, "Certified\nDeployment", ha='center', va='bottom',
            fontsize=7.5, fontweight='bold', color='#1B5E20', backgroundcolor='#FFFFFF')

    # Phase 3 Feedback Loops back to Phase 1 and Phase 2 (Bottom curve)
    arc_p3_to_p1 = ConnectionPatch(
        xyA=(13.1, 1.05), xyB=(2.9, 1.05),
        coordsA="data", coordsB="data",
        axesA=ax, axesB=ax,
        connectionstyle="arc3,rad=0.22",
        arrowstyle="-|>",
        color='#991B1B', lw=2.0, ls='--', mutation_scale=16
    )
    ax.add_patch(arc_p3_to_p1)
    ax.text(8.0, 0.28, "Continuous Feedback Loop: Runtime Drift Alerts, Incident Telemetry & CX Satisfaction Metrics",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#991B1B',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF2F2', edgecolor='#EF4444', lw=1.0))

    # Save high resolution image
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Publication-grade architecture diagram saved successfully at: {output_path}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(current_dir, "safecontext_architecture.png")
    create_architecture_diagram(out_file)

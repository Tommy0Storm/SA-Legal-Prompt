"""
🇿🇦 SA LEGAL PROMPTING ELITE PLATFORM
World-Class AI Prompting Interface for South African Legal Professionals
Version 4.4.0 - Advanced AI Edition

Features:
- AI-Powered Chat Assistant with 18 Optimization Modes
- Smart Prompt Builder with Real-time Preview
- 16 Prompting Frameworks (RICE, CRISPE, VARI, Q*, SPO...)
- 16 Quick Legal Templates
- Analytics Dashboard
- Keyboard Shortcuts & Command Palette
- Export & Collaboration Tools
- Premium UI Components

SP3 New Features (from 302 Prompt Expert):
- VARI Planning (DeepMind variational reasoning)
- Q* Strategy (A* + Q-Learning paths)
- Micro-Optimization (Microsoft iterative)
- OpenAI Official (Best practices)
- SPO Self-Play (Adversarial refinement)
- Guided Complete (Step-by-step builder)

Run with: streamlit run streamlit_app.py
"""

import streamlit as st
import json
import datetime
import requests
from typing import Optional, List, Dict, Tuple, Any, Union
import hashlib
import base64
import re
from collections import Counter
import time

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="SA Legal Prompting Elite",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/sa-legal-prompting',
        'Report a bug': 'https://github.com/sa-legal-prompting/issues',
        'About': '''# SA Legal Prompting Elite v4.4.0
        
🏆 **Advanced AI Edition**

World-class AI prompting for South African legal professionals.

**New in v4.4.0 (SP3 - Advanced AI):**
- 🧠 VARI Planning Mode (DeepMind variational reasoning)
- ⭐ Q* Strategy Mode (A* + Q-Learning litigation paths)
- 🔬 Micro-Optimization (Microsoft iterative enhancement)
- 📘 OpenAI Official (Best practices integration)
- 🎮 SPO Self-Play (HKUST adversarial refinement)
- 📋 Guided Complete (Step-by-step prompt building)
- 📚 5 New Frameworks (VARI, Q*, MICRO, SPO, GUIDED)
- ⚡ 10 New Quick Templates (PIE, Restraint, BEE, IP, Tax...)

**v4.3.0 (UX Overhaul):**
- 🎯 Consolidated 5-tab navigation
- 👋 Onboarding flow for new users
- ✅ Confirmation dialogs & toast notifications

**v4.2.0 (SP2) Features:**
- 👨‍⚖️ Expert Witness Mode (Rule 36(9) compliant)
- 🤝 Mediation/ADR Mode (5-phase dispute resolution)
- 📋 Compliance Audit Mode (POPIA, FICA, King IV)

**Core Features:**
- 🤖 AI Chat Assistant with context awareness
- 🎨 Smart Prompt Builder with 18 optimization modes
- 📊 Analytics Dashboard with usage insights
- 📚 Reference Library (16 Frameworks, Courts, Legislation, Ethics)
'''
    }
)

# ═══════════════════════════════════════════════════════════════════════════════
# IMPORTS - Core Modules
# ═══════════════════════════════════════════════════════════════════════════════

from core.advanced_frameworks import (
    ALL_FRAMEWORKS, 
    get_framework_by_acronym,
    generate_combined_prompt,
    FrameworkCategory
)
from core.specialist_courts import (
    ALL_SPECIALIST_COURTS,
    generate_court_prompt_guidance,
    CourtCategory
)
from core.sa_legislation import (
    ALL_LEGISLATION,
    generate_legislation_prompt,
    LegislationCategory
)
from core.legal_ethics import (
    ALL_GUIDELINES,
    AI_USE_SCENARIOS,
    assess_ai_use_risk,
    generate_ethics_checklist,
    RiskLevel
)
from core.practice_area_prompts import (
    ALL_PRACTICE_PROMPTS,
    generate_practice_prompt,
    PracticeArea
)
from core.document_templates import (
    ALL_DOCUMENT_TEMPLATES,
    generate_document_prompt,
    DocumentCategory
)
from core.workflow_pipelines import (
    ALL_WORKFLOWS,
    get_step_prompt,
    WorkflowCategory
)
from core.prompt_optimizer import (
    OptimizationMode,
    LegalOutputFormat,
    PracticeAreaPreset,
    OptimizedPrompt,
    optimize_legal_prompt,
    optimize_with_preset,
    get_optimization_modes_for_ui,
    get_presets_for_ui,
    detect_practice_area,
    calculate_prompt_quality_score,
    # SP2 New Features
    PromptComparison,
    QualityScoreDetails,
    QuickTemplate,
    compare_optimization_modes,
    export_prompt_to_json,
    export_prompt_to_markdown,
    calculate_detailed_quality_score,
    get_quick_templates,
    get_template_by_name
)

# ═══════════════════════════════════════════════════════════════════════════════
# SESSION STATE INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════════

def init_session_state():
    """Initialize all session state variables"""
    defaults = {
        'prompt_history': [],
        'favorites': [],
        'current_prompt': '',
        'current_prompt_title': '',
        'search_query': '',
        'theme': 'professional',
        'show_tips': True,
        'prompt_count': 0,
        'session_start': datetime.datetime.now().isoformat(),
        'copied_prompt': None,
        'active_workflow_step': 0,
        'selected_framework': None,
        'selected_court': None,
        # v4.4.0 - Cerebras API Integration
        'cerebras_api_key': '',
        'use_ai_api': False,
        # v4.1 - Onboarding & Confirmation States
        'onboarded': False,
        'confirm_clear_history': False,
        'confirm_clear_chat': False,
        # v4.1 - Tab Sub-navigation
        'reference_subtab': 'Frameworks',
        # NEW v4.0 - AI Chat Assistant
        'chat_messages': [],
        'chat_context': {},
        # NEW v4.0 - Smart Prompt Builder
        'builder_components': {},
        'builder_preview': '',
        'builder_framework': None,
        # NEW v4.0 - Command Palette
        'show_command_palette': False,
        'command_search': '',
        # NEW v4.0 - Enhanced Analytics
        'analytics': {
            'frameworks_used': {},
            'courts_viewed': {},
            'prompts_generated': 0,
            'session_duration': 0,
            'tabs_visited': {},
            'search_queries': [],
            'export_count': 0,
            'chat_interactions': 0,
            'daily_usage': {},
            'popular_templates': {}
        },
        # NEW v4.0 - Collaboration
        'workspace_name': 'My Legal Workspace',
        'shared_prompts': [],
        'team_members': [],
        # NEW v4.0 - User Preferences
        'preferences': {
            'auto_copy': True,
            'show_examples': True,
            'compact_mode': False,
            'highlight_risks': True,
            'keyboard_shortcuts': True
        }
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
    
    # Track session duration
    if 'session_start' in st.session_state:
        start = datetime.datetime.fromisoformat(st.session_state.session_start)
        duration = (datetime.datetime.now() - start).seconds
        st.session_state.analytics['session_duration'] = duration

init_session_state()

# ═══════════════════════════════════════════════════════════════════════════════
# WORLD-CLASS CSS STYLING
# ═══════════════════════════════════════════════════════════════════════════════

def inject_custom_css():
    """Inject ultra-modern monochrome CSS styling with Quicksand font"""
    st.markdown("""
    <style>
        /* ═══════════════════════════════════════════════════════════════════
           GOOGLE FONTS - Quicksand only (no Material Icons - using CSS arrows)
           ═══════════════════════════════════════════════════════════════════ */
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');
        
        /* ═══════════════════════════════════════════════════════════════════
           ROOT VARIABLES - Ultra-Modern Monochrome Palette
           ═══════════════════════════════════════════════════════════════════ */
        :root {
            /* Monochrome Palette */
            --mono-black: #0a0a0a;
            --mono-charcoal: #1a1a1a;
            --mono-dark: #2d2d2d;
            --mono-gray-700: #404040;
            --mono-gray-600: #525252;
            --mono-gray-500: #737373;
            --mono-gray-400: #a3a3a3;
            --mono-gray-300: #d4d4d4;
            --mono-gray-200: #e5e5e5;
            --mono-gray-100: #f5f5f5;
            --mono-white: #fafafa;
            --mono-pure-white: #ffffff;
            
            /* Accent - subtle warm gray for highlights */
            --accent-warm: #e8e4e0;
            --accent-cool: #e4e8ec;
            
            /* Gradients */
            --gradient-primary: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 50%, #404040 100%);
            --gradient-light: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
            --gradient-dark: linear-gradient(180deg, #0a0a0a 0%, #1a1a1a 100%);
            --gradient-subtle: linear-gradient(135deg, #ffffff 0%, #f5f5f5 100%);
            --gradient-glass: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.7) 100%);
            
            /* Shadows - refined */
            --shadow-xs: 0 1px 2px rgba(0,0,0,0.04);
            --shadow-sm: 0 2px 8px rgba(0,0,0,0.06);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.08);
            --shadow-lg: 0 8px 32px rgba(0,0,0,0.12);
            --shadow-xl: 0 16px 48px rgba(0,0,0,0.16);
            --shadow-inner: inset 0 2px 4px rgba(0,0,0,0.04);
            
            /* Border radius - modern */
            --radius-xs: 4px;
            --radius-sm: 6px;
            --radius-md: 10px;
            --radius-lg: 14px;
            --radius-xl: 18px;
            --radius-2xl: 24px;
            
            /* Typography */
            --font-primary: 'Quicksand', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-mono: 'SF Mono', 'Fira Code', 'Consolas', monospace;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           GLOBAL STYLES
           ═══════════════════════════════════════════════════════════════════ */
        * {
            font-family: var(--font-primary) !important;
        }
        
        .stApp {
            background: var(--mono-white);
            font-family: var(--font-primary);
            color: var(--mono-charcoal);
        }
        
        /* Main content area text should be dark */
        .stApp .main .block-container,
        .stApp .main .block-container p,
        .stApp .main .block-container span,
        .stApp .main .block-container div,
        .stApp .main .block-container label {
            color: var(--mono-charcoal);
        }
        
        .stApp .main .block-container h1,
        .stApp .main .block-container h2,
        .stApp .main .block-container h3,
        .stApp .main .block-container h4,
        .stApp .main .block-container h5 {
            color: var(--mono-black);
        }
        
        /* Hide Streamlit branding for cleaner look */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Typography baseline - compact sizing */
        h1, h2, h3, h4, h5, h6, p, span, div, button, input, textarea, label {
            font-family: var(--font-primary) !important;
            font-weight: 500;
        }
        
        h1 { font-weight: 700 !important; letter-spacing: -0.02em; font-size: 1.5rem !important; }
        h2 { font-weight: 600 !important; letter-spacing: -0.01em; font-size: 1.2rem !important; }
        h3 { font-weight: 600 !important; font-size: 1rem !important; }
        h4 { font-weight: 600 !important; font-size: 0.9rem !important; }
        
        p, span, div, label { font-size: 0.85rem; }
        
        /* Compact metrics */
        [data-testid="stMetric"] {
            background: var(--mono-gray-100);
            padding: 0.6rem 0.8rem !important;
            border-radius: var(--radius-sm);
        }
        
        [data-testid="stMetric"] label {
            font-size: 0.7rem !important;
        }
        
        [data-testid="stMetric"] [data-testid="stMetricValue"] {
            font-size: 1.1rem !important;
        }
        
        /* Compact expanders */
        [data-testid="stExpander"] {
            border: 1px solid var(--mono-gray-200) !important;
            border-radius: var(--radius-sm) !important;
            margin: 0.35rem 0 !important;
        }
        
        [data-testid="stExpander"] summary {
            padding: 0.5rem 0.75rem !important;
            font-size: 0.85rem !important;
        }
        
        [data-testid="stExpander"] [data-testid="stExpanderDetails"] {
            padding: 0.5rem 0.75rem !important;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           HERO HEADER - Ultra Modern Monochrome
           ═══════════════════════════════════════════════════════════════════ */
        .hero-header {
            background: var(--gradient-primary);
            color: var(--mono-white);
            padding: 1.5rem 2rem;
            border-radius: var(--radius-2xl);
            margin-bottom: 1.25rem;
            box-shadow: var(--shadow-xl);
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.05);
        }
        
        .hero-header::before {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 40%;
            height: 100%;
            background: linear-gradient(135deg, transparent 0%, rgba(255,255,255,0.03) 100%);
            pointer-events: none;
        }
        
        .hero-header::after {
            content: '';
            position: absolute;
            bottom: -50%;
            right: -25%;
            width: 50%;
            height: 100%;
            background: radial-gradient(circle, rgba(255,255,255,0.02) 0%, transparent 70%);
            pointer-events: none;
        }
        
        .hero-header h1 {
            margin: 0;
            font-size: 1.6rem;
            font-weight: 700;
            letter-spacing: -0.03em;
            position: relative;
            z-index: 1;
            color: var(--mono-pure-white);
        }
        
        .hero-header .subtitle {
            margin: 0.5rem 0 0 0;
            font-size: 0.85rem;
            opacity: 0.7;
            font-weight: 400;
            position: relative;
            z-index: 1;
            letter-spacing: 0.02em;
        }
        
        .hero-logo {
            height: 36px;
            width: auto;
            margin-bottom: 0.75rem;
            filter: brightness(0) invert(1);
            opacity: 0.95;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           STATS BADGES - Minimal & Clean
           ═══════════════════════════════════════════════════════════════════ */
        .stats-container {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-top: 1rem;
            position: relative;
            z-index: 1;
        }
        
        .stats-badge {
            background: rgba(255,255,255,0.08);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            color: rgba(255,255,255,0.9);
            padding: 0.35rem 0.75rem;
            border-radius: 100px;
            font-weight: 500;
            font-size: 0.7rem;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .stats-badge:hover {
            background: rgba(255,255,255,0.15);
            transform: translateY(-1px);
        }
        
        .stats-badge.gold {
            background: rgba(255,255,255,0.95);
            color: var(--mono-charcoal);
            border-color: transparent;
            font-weight: 600;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           SECTION CARDS - Modern Glass Effect
           ═══════════════════════════════════════════════════════════════════ */
        .section-card {
            background: var(--mono-pure-white);
            border-radius: var(--radius-lg);
            padding: 1.25rem;
            margin: 0.75rem 0;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--mono-gray-200);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
        }
        
        .section-card::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 3px;
            background: var(--mono-charcoal);
            border-radius: 3px 0 0 3px;
        }
        
        .section-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
            border-color: var(--mono-gray-300);
        }
        
        .section-card.gold-accent::before {
            background: var(--mono-gray-500);
        }
        
        .section-card.red-accent::before {
            background: var(--mono-gray-700);
        }
        
        .section-card h3 {
            color: var(--mono-charcoal);
            margin: 0 0 0.35rem 0;
            font-size: 1rem;
            font-weight: 600;
        }
        
        .section-card p {
            color: var(--mono-gray-600);
            margin: 0;
            font-size: 0.85rem;
            line-height: 1.5;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           PROMPT OUTPUT BOX - Elegant Code Display
           ═══════════════════════════════════════════════════════════════════ */
        .prompt-output {
            background: var(--mono-gray-100);
            border: 1px solid var(--mono-gray-200);
            border-radius: var(--radius-lg);
            padding: 1.25rem;
            font-family: var(--font-mono);
            font-size: 0.8rem;
            line-height: 1.6;
            white-space: pre-wrap;
            max-height: 400px;
            overflow-y: auto;
            position: relative;
            color: var(--mono-charcoal);
        }
        
        .prompt-output::before {
            content: '📋 Generated Prompt';
            position: absolute;
            top: -12px;
            left: 20px;
            background: var(--mono-white);
            padding: 0 10px;
            font-size: 0.7rem;
            font-weight: 600;
            color: var(--mono-gray-500);
            font-family: var(--font-primary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           TAB STYLING - Ultra Clean
           ═══════════════════════════════════════════════════════════════════ */
        .stTabs [data-baseweb="tab-list"] {
            gap: 3px;
            background: var(--mono-gray-100);
            padding: 0.35rem;
            border-radius: var(--radius-xl);
            border: 1px solid var(--mono-gray-200);
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 38px;
            padding: 0 14px;
            background: transparent;
            border-radius: var(--radius-md);
            font-weight: 500;
            font-size: 0.8rem;
            color: var(--mono-gray-600);
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            border: none;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: var(--mono-pure-white);
            color: var(--mono-charcoal);
        }
        
        .stTabs [aria-selected="true"] {
            background: var(--mono-charcoal) !important;
            color: var(--mono-pure-white) !important;
            font-weight: 600;
            box-shadow: var(--shadow-sm);
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           SIDEBAR STYLING - Dark Sophisticated with White Text
           ═══════════════════════════════════════════════════════════════════ */
        [data-testid="stSidebar"] {
            background: var(--gradient-dark);
            border-right: 1px solid rgba(255,255,255,0.05);
        }
        
        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] .stMarkdown p,
        [data-testid="stSidebar"] .stMarkdown span,
        [data-testid="stSidebar"] .stMarkdown div,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] .stCaption,
        [data-testid="stSidebar"] [data-testid="stCaptionContainer"],
        [data-testid="stSidebar"] [data-testid="stCaptionContainer"] * {
            color: rgba(255,255,255,0.9) !important;
        }
        
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] h4,
        [data-testid="stSidebar"] h5 {
            color: var(--mono-pure-white) !important;
            font-weight: 600;
        }
        
        [data-testid="stSidebar"] .stSelectbox label,
        [data-testid="stSidebar"] .stMultiSelect label,
        [data-testid="stSidebar"] .stTextInput label,
        [data-testid="stSidebar"] .stTextArea label {
            color: rgba(255,255,255,0.9) !important;
        }
        
        [data-testid="stSidebar"] hr {
            border-color: rgba(255,255,255,0.1);
        }
        
        /* Sidebar metrics */
        [data-testid="stSidebar"] [data-testid="stMetricValue"],
        [data-testid="stSidebar"] [data-testid="stMetricLabel"],
        [data-testid="stSidebar"] [data-testid="stMetricDelta"] {
            color: var(--mono-pure-white) !important;
        }
        
        /* Sidebar expanders */
        [data-testid="stSidebar"] [data-testid="stExpander"] summary p,
        [data-testid="stSidebar"] [data-testid="stExpander"] summary span {
            color: rgba(255,255,255,0.9) !important;
        }
        
        /* Sidebar toggle labels */
        [data-testid="stSidebar"] .stCheckbox label span,
        [data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
            color: rgba(255,255,255,0.9) !important;
        }
        
        /* Sidebar buttons */
        [data-testid="stSidebar"] .stButton > button {
            background: rgba(255,255,255,0.1);
            color: var(--mono-pure-white);
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        [data-testid="stSidebar"] .stButton > button:hover {
            background: rgba(255,255,255,0.2);
            border-color: rgba(255,255,255,0.3);
        }
        
        /* Sidebar progress bar text */
        [data-testid="stSidebar"] .stProgress > div > div > div {
            color: rgba(255,255,255,0.9) !important;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           BUTTON STYLING - Minimal & Elegant
           ═══════════════════════════════════════════════════════════════════ */
        .stButton > button {
            background: var(--mono-charcoal);
            color: var(--mono-pure-white);
            border: none;
            border-radius: var(--radius-md);
            padding: 0.5rem 1rem;
            font-weight: 600;
            font-size: 0.8rem;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: var(--shadow-sm);
        }
        
        .stButton > button:hover {
            background: var(--mono-black);
            box-shadow: var(--shadow-md);
            transform: translateY(-1px);
        }
        
        .stButton > button:active {
            transform: translateY(0);
            box-shadow: var(--shadow-xs);
        }
        
        /* Primary button variant */
        .stButton > button[kind="primary"] {
            background: var(--mono-black);
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           INPUT FIELDS - Clean & Modern
           ═══════════════════════════════════════════════════════════════════ */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            border-radius: var(--radius-md);
            border: 1px solid var(--mono-gray-300);
            background: var(--mono-pure-white);
            color: var(--mono-charcoal);
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            font-size: 0.85rem;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: var(--mono-charcoal);
            box-shadow: 0 0 0 3px rgba(26, 26, 26, 0.08);
            color: var(--mono-charcoal);
        }
        
        .stTextInput > div > div > input::placeholder,
        .stTextArea > div > div > textarea::placeholder {
            color: var(--mono-gray-400);
        }
        
        /* Selectbox styling - ensure dark text on light background */
        .stSelectbox > div > div,
        .stMultiSelect > div > div {
            color: var(--mono-charcoal);
        }
        
        .stSelectbox label,
        .stMultiSelect label {
            color: var(--mono-charcoal) !important;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           METRICS STYLING - Minimalist
           ═══════════════════════════════════════════════════════════════════ */
        [data-testid="stMetric"] {
            background: var(--mono-pure-white);
            padding: 1.25rem;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-xs);
            border: 1px solid var(--mono-gray-200);
        }
        
        [data-testid="stMetricLabel"] {
            color: var(--mono-gray-500);
            font-weight: 500;
        }
        
        [data-testid="stMetricValue"] {
            color: var(--mono-charcoal);
            font-weight: 700;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           EXPANDER STYLING - Subtle
           ═══════════════════════════════════════════════════════════════════ */
        .streamlit-expanderHeader {
            background: var(--mono-pure-white);
            border-radius: var(--radius-md);
            font-weight: 600;
            color: var(--mono-charcoal);
            border: 1px solid var(--mono-gray-200);
        }
        
        .streamlit-expanderHeader:hover {
            background: var(--mono-gray-100);
        }
        
        .streamlit-expanderContent {
            background: var(--mono-gray-100);
            border-radius: 0 0 var(--radius-md) var(--radius-md);
            border: 1px solid var(--mono-gray-200);
            border-top: none;
            color: var(--mono-charcoal);
        }
        
        .streamlit-expanderContent p,
        .streamlit-expanderContent span,
        .streamlit-expanderContent div {
            color: var(--mono-charcoal);
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           RISK LEVEL BADGES - Monochrome
           ═══════════════════════════════════════════════════════════════════ */
        .risk-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.35rem 0.75rem;
            border-radius: 100px;
            font-weight: 600;
            font-size: 0.7rem;
        }
        
        .risk-low {
            background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
            color: #2e7d32;
            border: 1px solid #a5d6a7;
        }
        
        .risk-medium {
            background: linear-gradient(135deg, #fff8e1 0%, #ffecb3 100%);
            color: #f57f17;
            border: 1px solid #ffe082;
        }
        
        .risk-high {
            background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
            color: #c62828;
            border: 1px solid #ef9a9a;
        }
        
        .risk-critical {
            background: linear-gradient(135deg, #b71c1c 0%, #c62828 100%);
            color: #ffffff;
            border: 1px solid #e53935;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           FRAMEWORK CARDS - Clean Selection
           ═══════════════════════════════════════════════════════════════════ */
        .framework-card {
            background: var(--mono-pure-white);
            border-radius: var(--radius-lg);
            padding: 1rem;
            margin: 0.35rem 0;
            border: 1px solid var(--mono-gray-200);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
        }
        
        .framework-card:hover {
            border-color: var(--mono-charcoal);
            box-shadow: var(--shadow-md);
            transform: translateX(4px);
        }
        
        .framework-card.selected {
            border-color: var(--mono-charcoal);
            border-width: 2px;
            background: var(--mono-gray-100);
        }
        
        .framework-acronym {
            background: var(--mono-charcoal);
            color: var(--mono-pure-white);
            padding: 0.2rem 0.6rem;
            border-radius: 100px;
            font-weight: 600;
            font-size: 0.7rem;
            display: inline-block;
            margin-bottom: 0.35rem;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           ALERT BOXES - Ensure proper text colors
           ═══════════════════════════════════════════════════════════════════ */
        [data-testid="stAlert"] p,
        [data-testid="stAlert"] span,
        .stAlert p,
        .stAlert span {
            color: var(--mono-charcoal) !important;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           ANIMATIONS - Subtle & Professional
           ═══════════════════════════════════════════════════════════════════ */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .fade-in {
            animation: fadeIn 0.4s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-12px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        .slide-in {
            animation: slideIn 0.3s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           RESPONSIVE DESIGN
           ═══════════════════════════════════════════════════════════════════ */
        @media (max-width: 768px) {
            .hero-header {
                padding: 1.75rem;
                border-radius: var(--radius-xl);
            }
            
            .hero-header h1 {
                font-size: 1.6rem;
            }
            
            .stats-container {
                gap: 0.4rem;
            }
            
            .stats-badge {
                font-size: 0.7rem;
                padding: 0.375rem 0.75rem;
            }
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           v4.0 - AI CHAT INTERFACE - Sophisticated
           ═══════════════════════════════════════════════════════════════════ */
        .chat-container {
            background: var(--gradient-subtle);
            border-radius: var(--radius-xl);
            padding: 1.25rem;
            margin: 0.75rem 0;
            border: 1px solid var(--mono-gray-200);
            max-height: 500px;
            overflow-y: auto;
        }
        
        .chat-message {
            display: flex;
            gap: 0.75rem;
            margin: 0.75rem 0;
            animation: fadeIn 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .chat-message.user {
            flex-direction: row-reverse;
        }
        
        .chat-avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            flex-shrink: 0;
        }
        
        .chat-avatar.assistant {
            background: var(--mono-charcoal);
            color: var(--mono-pure-white);
        }
        
        .chat-avatar.user {
            background: var(--mono-gray-200);
            color: var(--mono-charcoal);
        }
        
        .chat-bubble {
            max-width: 70%;
            padding: 0.75rem 1rem;
            border-radius: var(--radius-lg);
            position: relative;
            font-size: 0.85rem;
        }
        
        .chat-bubble.assistant {
            background: var(--mono-pure-white);
            border: 1px solid var(--mono-gray-200);
            border-top-left-radius: 4px;
            color: var(--mono-charcoal);
        }
        
        .chat-bubble.user {
            background: var(--mono-charcoal);
            color: var(--mono-pure-white);
            border-top-right-radius: 4px;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           v4.0 - SMART PROMPT BUILDER - Clean
           ═══════════════════════════════════════════════════════════════════ */
        .builder-container {
            background: var(--mono-pure-white);
            border-radius: var(--radius-xl);
            padding: 1.25rem;
            box-shadow: var(--shadow-lg);
            border: 1px solid var(--mono-gray-200);
            position: relative;
        }
        
        .component-slot {
            background: var(--mono-gray-100);
            border: 2px dashed var(--mono-gray-300);
            border-radius: var(--radius-md);
            padding: 0.75rem;
            margin: 0.35rem 0;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .component-slot:hover {
            border-color: var(--mono-charcoal);
            background: var(--mono-gray-100);
        }
        
        .component-slot.filled {
            border-style: solid;
            border-color: var(--mono-charcoal);
            background: var(--mono-pure-white);
        }
        
        .preview-panel {
            background: var(--mono-charcoal);
            color: var(--mono-gray-200);
            border-radius: var(--radius-lg);
            padding: 2rem 1.25rem 1.25rem 1.25rem;
            font-family: var(--font-mono);
            font-size: 0.8rem;
            line-height: 1.7;
            position: relative;
            overflow: hidden;
        }
        
        .preview-panel::before {
            content: '⌘ LIVE PREVIEW';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            padding: 0.35rem 0.75rem;
            background: rgba(255,255,255,0.08);
            font-size: 0.6rem;
            font-weight: 600;
            letter-spacing: 1.5px;
            font-family: var(--font-primary);
            color: var(--mono-gray-400);
            z-index: 10;
        }
        
        .preview-panel .content {
            margin-top: 0.5rem;
            position: relative;
            z-index: 5;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           v4.0 - COMMAND PALETTE - Minimal
           ═══════════════════════════════════════════════════════════════════ */
        .command-palette-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(10, 10, 10, 0.6);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            z-index: 9999;
            display: flex;
            align-items: flex-start;
            justify-content: center;
            padding-top: 18vh;
        }
        
        .command-palette {
            background: var(--mono-pure-white);
            border-radius: var(--radius-xl);
            width: 90%;
            max-width: 560px;
            box-shadow: var(--shadow-xl);
            overflow: hidden;
            border: 1px solid var(--mono-gray-200);
        }
        
        .command-input {
            width: 100%;
            padding: 1.25rem 1.5rem;
            border: none;
            border-bottom: 1px solid var(--mono-gray-200);
            font-size: 1.05rem;
            outline: none;
            font-family: var(--font-primary);
            font-weight: 500;
        }
        
        .command-item {
            padding: 0.875rem 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            cursor: pointer;
            transition: background 0.15s cubic-bezier(0.4, 0, 0.2, 1);
            color: var(--mono-charcoal);
        }
        
        .command-item:hover {
            background: var(--mono-gray-100);
        }
        
        .command-item.selected {
            background: var(--mono-charcoal);
            color: var(--mono-pure-white);
        }
        
        .command-shortcut {
            margin-left: auto;
            font-size: 0.7rem;
            padding: 0.25rem 0.6rem;
            background: var(--mono-gray-200);
            border-radius: 6px;
            font-family: var(--font-mono);
            color: var(--mono-gray-600);
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           v4.0 - ANALYTICS DASHBOARD - Clean Data Display
           ═══════════════════════════════════════════════════════════════════ */
        .analytics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 1rem 0;
        }
        
        .analytics-card {
            background: var(--mono-pure-white);
            border-radius: var(--radius-lg);
            padding: 1.75rem;
            box-shadow: var(--shadow-sm);
            text-align: center;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid var(--mono-gray-200);
        }
        
        .analytics-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
        }
        
        .analytics-value {
            font-size: 2.75rem;
            font-weight: 700;
            color: var(--mono-charcoal);
            line-height: 1;
        }
        
        .analytics-label {
            color: var(--mono-gray-500);
            font-size: 0.875rem;
            margin-top: 0.625rem;
            font-weight: 500;
        }
        
        .analytics-trend {
            font-size: 0.75rem;
            margin-top: 0.5rem;
            font-weight: 600;
        }
        
        .analytics-trend.up { color: var(--mono-gray-600); }
        .analytics-trend.down { color: var(--mono-gray-500); }
        
        /* ═══════════════════════════════════════════════════════════════════
           v4.0 - TEMPLATE GALLERY - Grid Cards
           ═══════════════════════════════════════════════════════════════════ */
        .template-gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.5rem;
            margin: 1.5rem 0;
        }
        
        .template-card {
            background: var(--mono-pure-white);
            border-radius: var(--radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            cursor: pointer;
            border: 1px solid var(--mono-gray-200);
        }
        
        .template-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
            border-color: var(--mono-charcoal);
        }
        
        .template-header {
            background: var(--mono-charcoal);
            color: var(--mono-pure-white);
            padding: 1rem 1.25rem;
            position: relative;
        }
        
        .template-header h4 {
            margin: 0;
            font-size: 1rem;
            font-weight: 600;
        }
        
        .template-badge {
            position: absolute;
            top: 0.75rem;
            right: 0.75rem;
            background: var(--mono-pure-white);
            color: var(--mono-charcoal);
            padding: 0.2rem 0.625rem;
            border-radius: 100px;
            font-size: 0.65rem;
            font-weight: 600;
            letter-spacing: 0.02em;
        }
        
        .template-body {
            padding: 1.25rem;
        }
        
        .template-body p {
            color: var(--mono-gray-600);
            font-size: 0.9rem;
            margin: 0 0 1rem 0;
            line-height: 1.6;
        }
        
        .template-meta {
            display: flex;
            gap: 1rem;
            font-size: 0.8rem;
            color: var(--mono-gray-500);
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           v4.0 - TOAST NOTIFICATIONS - Subtle
           ═══════════════════════════════════════════════════════════════════ */
        .toast-container {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            z-index: 9998;
        }
        
        .toast {
            background: var(--mono-pure-white);
            border-radius: var(--radius-md);
            padding: 1rem 1.5rem;
            box-shadow: var(--shadow-lg);
            margin-top: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            animation: slideInRight 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border-left: 3px solid var(--mono-charcoal);
        }
        
        .toast.success { border-left-color: var(--mono-gray-400); }
        .toast.warning { border-left-color: var(--mono-gray-500); }
        .toast.error { border-left-color: var(--mono-gray-700); }
        
        @keyframes slideInRight {
            from { opacity: 0; transform: translateX(100px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           v4.0 - PROGRESS INDICATORS - Minimal
           ═══════════════════════════════════════════════════════════════════ */
        .progress-ring {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            position: relative;
        }
        
        .progress-ring svg {
            transform: rotate(-90deg);
        }
        
        .progress-ring circle {
            fill: none;
            stroke-width: 6;
        }
        
        .progress-ring .bg { stroke: var(--mono-gray-200); }
        .progress-ring .progress { stroke: var(--mono-charcoal); }
        
        .progress-value {
            position: absolute;
            font-weight: 700;
            color: var(--mono-charcoal);
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           v4.0 - KEYBOARD SHORTCUTS HINT - Sleek
           ═══════════════════════════════════════════════════════════════════ */
        .shortcuts-hint {
            position: fixed;
            bottom: 1.25rem;
            left: 50%;
            transform: translateX(-50%);
            background: var(--mono-charcoal);
            color: var(--mono-gray-200);
            padding: 0.625rem 1.25rem;
            border-radius: 100px;
            font-size: 0.75rem;
            display: flex;
            gap: 1.5rem;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: var(--shadow-lg);
            border: 1px solid rgba(255,255,255,0.1);
            z-index: 9998;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           SP2 FIX - LAYOUT FIXES
           ═══════════════════════════════════════════════════════════════════ */
        /* Add bottom padding to main content to avoid overlap with shortcuts bar */
        .main .block-container {
            padding-bottom: 5rem !important;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           EXPANDER ICON FIX - NUCLEAR OPTION v3
           Hide ALL possible Material Icons text in expanders
           ═══════════════════════════════════════════════════════════════════ */
        /* Target every possible element that might contain icon text */
        [data-testid="stExpander"] summary > span:first-child,
        [data-testid="stExpander"] summary [data-testid="stExpanderToggleIcon"],
        [data-testid="stExpander"] summary span[class*="material"],
        [data-testid="stExpander"] summary span[class*="icon"],
        [data-testid="stExpander"] summary span[class*="Icon"],
        [data-testid="stExpander"] details > summary > span:first-child,
        details[data-testid="stExpander"] > summary > span:first-child {
            display: none !important;
            visibility: hidden !important;
            width: 0 !important;
            height: 0 !important;
            max-width: 0 !important;
            max-height: 0 !important;
            overflow: hidden !important;
            font-size: 0 !important;
            line-height: 0 !important;
            opacity: 0 !important;
            position: absolute !important;
            left: -9999px !important;
        }
        
        /* Hide any element using Material Symbols font */
        [data-testid="stExpander"] summary *[style*="Material"],
        [data-testid="stExpander"] summary span:not(:has(p)):not(:has(div)) {
            font-size: 0 !important;
            color: transparent !important;
            width: 0 !important;
            overflow: hidden !important;
        }
        
        /* Only show the paragraph text in expander summary */
        [data-testid="stExpander"] summary p,
        [data-testid="stExpander"] summary > div > p {
            font-size: 0.9rem !important;
            font-family: 'Quicksand', -apple-system, BlinkMacSystemFont, sans-serif !important;
            color: var(--mono-charcoal) !important;
            display: inline-block !important;
            visibility: visible !important;
            opacity: 1 !important;
        }
        
        /* Style the expander with clean arrow */
        [data-testid="stExpander"] {
            position: relative;
            z-index: 1;
            overflow: hidden;
        }
        
        [data-testid="stExpander"] summary {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            cursor: pointer;
            padding-left: 1.5rem !important;
            position: relative;
        }
        
        /* Add CSS-only arrow */
        [data-testid="stExpander"]:not([open]) summary::before {
            content: '▸' !important;
            position: absolute !important;
            left: 0.5rem !important;
            top: 50% !important;
            transform: translateY(-50%) !important;
            font-size: 12px !important;
            color: #737373 !important;
            font-family: system-ui, sans-serif !important;
        }
        
        [data-testid="stExpander"][open] summary::before {
            content: '▾' !important;
            position: absolute !important;
            left: 0.5rem !important;
            top: 50% !important;
            transform: translateY(-50%) !important;
            font-size: 12px !important;
            color: #737373 !important;
            font-family: system-ui, sans-serif !important;
        }
        
        .shortcut-key {
            background: rgba(255, 255, 255, 0.12);
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-family: var(--font-mono);
            margin-right: 0.5rem;
            font-size: 0.7rem;
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           v4.0 - SUBTLE EFFECTS
           ═══════════════════════════════════════════════════════════════════ */
        .glow-green {
            box-shadow: var(--shadow-lg);
        }
        
        .glow-gold {
            box-shadow: var(--shadow-lg);
        }
        
        .pulse-glow {
            /* Removed for cleaner monochrome aesthetic */
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           SCROLLBAR - Minimal
           ═══════════════════════════════════════════════════════════════════ */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: var(--mono-gray-100);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: var(--mono-gray-300);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: var(--mono-gray-400);
        }
        
        /* ═══════════════════════════════════════════════════════════════════
           SELECTION
           ═══════════════════════════════════════════════════════════════════ */
        ::selection {
            background: var(--mono-charcoal);
            color: var(--mono-pure-white);
        }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# ═══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def add_to_history(prompt: str, source: str, metadata: Optional[Dict] = None):
    """Add a generated prompt to history"""
    entry = {
        'id': hashlib.md5(prompt.encode()).hexdigest()[:8],
        'prompt': prompt,
        'source': source,
        'metadata': metadata or {},
        'timestamp': datetime.datetime.now().isoformat(),
        'favorited': False
    }
    st.session_state.prompt_history.insert(0, entry)
    st.session_state.prompt_count += 1
    st.session_state.analytics['prompts_generated'] += 1
    # Keep only last 50 prompts
    if len(st.session_state.prompt_history) > 50:
        st.session_state.prompt_history = st.session_state.prompt_history[:50]

def toggle_favorite(prompt_id: str):
    """Toggle favorite status of a prompt"""
    for entry in st.session_state.prompt_history:
        if entry['id'] == prompt_id:
            entry['favorited'] = not entry['favorited']
            break

def get_risk_badge(risk_level: str) -> str:
    """Get HTML badge for risk level"""
    risk_map = {
        'LOW': ('🟢', 'risk-low', 'Low Risk'),
        'MEDIUM': ('🟡', 'risk-medium', 'Medium Risk'),
        'HIGH': ('🔴', 'risk-high', 'High Risk'),
        'CRITICAL': ('⚫', 'risk-critical', 'Critical')
    }
    icon, css_class, label = risk_map.get(str(risk_level).upper(), ('⚪', 'risk-low', 'Unknown'))
    return f'<span class="risk-badge {css_class}">{icon} {label}</span>'

def search_all_resources(query: str) -> List[Dict]:
    """Search across all resources"""
    results = []
    query_lower = query.lower()
    
    # Search frameworks
    for key, fw in ALL_FRAMEWORKS.items():
        if query_lower in fw.name.lower() or query_lower in fw.description.lower() or query_lower in fw.acronym.lower():
            results.append({
                'type': 'Framework',
                'name': f"{fw.name} ({fw.acronym})",
                'key': key,
                'icon': '🎯',
                'description': fw.description[:100] + '...'
            })
    
    # Search courts
    for key, court in ALL_SPECIALIST_COURTS.items():
        if query_lower in court.name.lower() or query_lower in court.saflii_code.lower():
            results.append({
                'type': 'Court',
                'name': court.name,
                'key': key,
                'icon': '🏛️',
                'description': f"SAFLII: {court.saflii_code}"
            })
    
    # Search legislation
    for key, leg in ALL_LEGISLATION.items():
        if query_lower in leg.short_title.lower() or query_lower in leg.full_title.lower():
            # Handle purpose which may be a string or list
            purpose_val = leg.purpose
            if isinstance(purpose_val, list):
                purpose_str: str = ', '.join(str(p) for p in purpose_val)
            else:
                purpose_str: str = str(purpose_val) if purpose_val else ''
            
            desc: str = purpose_str[:100] + '...' if len(purpose_str) > 100 else purpose_str
            results.append({
                'type': 'Legislation',
                'name': leg.short_title,
                'key': key,
                'icon': '📜',
                'description': desc
            })
    
    # Search practice prompts
    for key, prompt in ALL_PRACTICE_PROMPTS.items():
        if query_lower in prompt.title.lower() or query_lower in prompt.description.lower():
            results.append({
                'type': 'Practice Prompt',
                'name': prompt.title,
                'key': key,
                'icon': '📋',
                'description': prompt.description[:100] + '...'
            })
    
    # Search document templates
    for key, doc in ALL_DOCUMENT_TEMPLATES.items():
        if query_lower in doc.title.lower() or query_lower in doc.description.lower():
            results.append({
                'type': 'Document Template',
                'name': doc.title,
                'key': key,
                'icon': '📄',
                'description': doc.description[:100] + '...'
            })
    
    # Search workflows
    for key, wf in ALL_WORKFLOWS.items():
        if query_lower in wf.title.lower() or query_lower in wf.description.lower():
            results.append({
                'type': 'Workflow',
                'name': wf.title,
                'key': key,
                'icon': '🔄',
                'description': wf.description[:100] + '...'
            })
    
    return results

# ═══════════════════════════════════════════════════════════════════════════════
# v4.0 - ADVANCED HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def call_cerebras_api(user_message: str, context: Optional[Dict] = None) -> Optional[str]:
    """Call Cerebras AI API for intelligent responses"""
    api_key = st.session_state.get('cerebras_api_key', '')
    
    if not api_key:
        return None
    
    # System prompt for SA Legal context
    system_prompt = """You are an expert AI assistant for South African legal professionals. You specialize in:
- Legal prompt engineering and framework recommendations (RICE, CRISPE, CO-STAR, Chain of Thought, VARI, Q*, etc.)
- South African law including Constitution, common law, and statutory law
- SA court systems (Constitutional Court, SCA, High Courts, Magistrates, Labour Court, CCMA)
- Legal ethics and AI use guidelines for attorneys
- SAFLII citation format and legal research

Provide helpful, accurate guidance focused on SA legal practice. When recommending frameworks, explain why they suit the specific legal context. Use ubuntu principles where relevant. Always cite SA case law and legislation properly.

Be concise but thorough. Format responses with markdown for readability."""

    try:
        response = requests.post(
            "https://api.cerebras.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.3-70b",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                "max_tokens": 1024,
                "temperature": 0.7
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            st.error(f"API Error: {response.status_code} - {response.text[:100]}")
            return None
            
    except requests.exceptions.Timeout:
        st.error("⏱️ API request timed out. Please try again.")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"🔌 Connection error: {str(e)[:50]}")
        return None
    except Exception as e:
        st.error(f"❌ Error: {str(e)[:50]}")
        return None


def get_ai_response(user_message: str, context: Optional[Dict] = None) -> str:
    """Generate AI assistant response for legal prompting guidance"""
    context = context or {}
    
    # Try Cerebras API first if enabled
    if st.session_state.get('use_ai_api') and st.session_state.get('cerebras_api_key'):
        api_response = call_cerebras_api(user_message, context)
        if api_response:
            return api_response
        # Fall through to rule-based if API fails
    
    # Rule-based fallback responses
    message_lower = user_message.lower()
    
    # Framework recommendations
    if any(word in message_lower for word in ['framework', 'which', 'recommend', 'best', 'use']):
        if any(word in message_lower for word in ['contract', 'commercial', 'business']):
            return """🎯 **Framework Recommendation: RICE + CASE**

For commercial/contract matters, I recommend combining:

**1. RICE Framework** (Role, Instructions, Context, Examples)
- Define yourself as a Commercial Attorney
- Specify the contract type and jurisdiction
- Include relevant Companies Act provisions

**2. CASE Framework** (Context, Actions, Specifics, Examples)
- Add specific clause analysis requirements
- Reference key precedents like *Bothma-Batho Transport v Bothma*

Would you like me to generate a template prompt for your contract matter?"""
        
        elif any(word in message_lower for word in ['criminal', 'defence', 'prosecution']):
            return """🎯 **Framework Recommendation: Chain of Thought Legal**

For criminal matters, I recommend:

**Chain of Thought Legal Framework**
- Step-by-step analysis of elements of offence
- Systematic evaluation of defences
- Reference to *S v Zuma* standards

Combined with **ABCDE** for audience-appropriate output (Judge vs Client).

Would you like me to help structure your criminal law prompt?"""
        
        else:
            return """🎯 **Framework & Optimization Guide**

**Framework Selection by Complexity:**
📗 **Beginner**: RICE, JUST ASK
📙 **Intermediate**: ABCDE, 7 Ps, CASE  
📕 **Advanced**: Chain of Thought, Prompt Chaining

**AI Optimization Modes (SP1):**
⚡ **CRISPE** - Role + Profile + Goals → Complex professional outputs
🎯 **CO-STAR** - Context + Objective + Style → Client-facing documents
🧠 **Chain of Thought** - Step-by-step reasoning → Complex legal analysis
🔄 **RISE** - 3x self-improvement → High-stakes matters
📊 **O1-Style** - Scored reasoning → Methodical analysis
⚡ **Hybrid Legal** - CRISPE + CoT combined → Maximum enhancement
📋 **Claude-Style** - Detailed instructions → Precise guidance

**Quick Practice Area Tips:**
- Constitutional matters → Chain of Thought + transformative approach
- Litigation → Hybrid Legal for comprehensive analysis
- Commercial → CO-STAR for audience awareness
- Labour → CRISPE for structured outputs

What type of legal matter are you working on?"""
    
    # Optimization mode guidance (NEW SP1)
    elif any(word in message_lower for word in ['optimization', 'optimize', 'enhance', 'mode', 'crispe', 'co-star', 'chain of thought', 'vari', 'q-star', 'micro', 'spo', 'guided']):
        return """⚡ **Prompt Optimization Modes Guide**

**Available Modes in Smart Prompt Builder:**

**Core Modes:**

**1. CRISPE** (Role + Profile + Goals + Skills)
- Best for: Complex professional outputs, formal opinions
- Adds: Structured system context, SA legal profile

**2. CO-STAR** (Context + Objective + Style + Tone + Audience)
- Best for: Client letters, audience-specific documents
- Adds: Audience awareness, tone specification

**3. Chain of Thought Legal**
- Best for: Complex analysis, Constitutional Court matters
- Adds: 6-step reasoning protocol with self-validation

**4. RISE** (Recursive Introspection)
- Best for: High-stakes, must-be-right matters
- Adds: 3 automatic refinement iterations

**5. O1-Style** (Structured Reasoning)
- Best for: Methodical, careful analysis
- Adds: Step budgets, quality scoring (0-1)

**6. Hybrid Legal** (SP1)
- Best for: Maximum enhancement
- Adds: Combined CRISPE structure + CoT reasoning

**7. Claude-Style** (SP1)
- Best for: Complex tasks needing precise guidance
- Adds: Detailed rules, XML structured output

**Specialist Modes (SP2):**

**8. Expert Witness** - Technical court opinion format
**9. Mediation/ADR** - Dispute resolution structure
**10. Compliance Audit** - Regulatory review protocol

**Advanced AI Modes (SP3 - from 302 Prompt Expert):**

**11. VARI Planning** (DeepMind)
- Best for: Complex strategic planning
- Adds: Explicit reasoning with self-reflection

**12. Q* Strategy** (A* + Q-Learning)
- Best for: Litigation strategy, cost-benefit analysis
- Adds: Path optimization, probabilistic outcomes

**13. Micro-Optimization** (Microsoft)
- Best for: Refining existing prompts
- Adds: 15+ targeted improvements iteratively

**14. OpenAI Official** (Best Practices)
- Best for: Balanced, well-structured prompts
- Adds: Official prompt engineering guidelines

**15. SPO Self-Play** (HKUST/DeepWisdom)
- Best for: Comprehensive gap identification
- Adds: Adversarial Q&A refinement cycles

**16. Guided Complete**
- Best for: Learning, step-by-step construction
- Adds: Component checklist with guidance

Go to the **Smart Prompt Builder** tab to try these!"""
    
    # Court guidance
    elif any(word in message_lower for word in ['court', 'tribunal', 'ccma', 'labour']):
        return """🏛️ **Court-Specific Prompting Guidance**

Each SA court has unique requirements:

**Constitutional Court**: Focus on rights analysis, ubuntu, transformative constitutionalism
- Recommended Mode: **Chain of Thought** or **Hybrid Legal**

**High Court**: Procedural precision, Rules of Court compliance
- Recommended Mode: **CRISPE** or **Hybrid Legal**

**Labour Court/CCMA**: LRA s185-s191, onus allocation, substantive/procedural fairness
- Recommended Mode: **CRISPE** with Labour preset

**SCA**: Precedent-focused, legal argument precision
- Recommended Mode: **Chain of Thought**

**Pro Tips:**
- Always include SAFLII citation format
- Reference establishing legislation
- Consider appeal routes in strategy
- Use the appropriate **Practice Area Preset** in Smart Builder

Which court are you preparing for?"""
    
    # Ethics
    elif any(word in message_lower for word in ['ethics', 'risk', 'ai use', 'appropriate']):
        return """⚖️ **AI Ethics in SA Legal Practice**

**Risk-Based Approach:**

🟢 **Low Risk** (AI can lead):
- Initial research, document summaries, procedural queries
- Recommended: STANDARD or CRISPE mode

🟡 **Medium Risk** (Human review essential):
- Legal analysis, strategy options, client communications
- Recommended: Chain of Thought for transparency

🔴 **High Risk** (Human leads):
- Court submissions, advice, final opinions
- Recommended: RISE or O1-Style for quality assurance

⚫ **Critical** (Human only):
- Ethics decisions, fiduciary matters, client instructions
- AI should NOT be primary source

**Quality Assurance:**
- Check your prompt's Quality Score in Smart Builder
- Always verify AI outputs against primary sources!"""
    
    # Preset guidance (NEW SP1)
    elif any(word in message_lower for word in ['preset', 'constitutional', 'criminal', 'labour', 'commercial', 'family', 'property', 'litigation']):
        return """📚 **Practice Area Presets (SP1 Feature)**

Quick-start your prompts with optimized presets:

**Constitutional Law**
- Mode: Chain of Thought
- Key Cases: *Harksen v Lane*, *Makwanyane*, *Fourie*
- Focus: Transformative constitutionalism, s36 analysis

**Criminal Law**
- Mode: Chain of Thought
- Key Cases: *S v Zuma*, *Thebus*, *Dodo*
- Focus: Fair trial rights, beyond reasonable doubt

**Labour & Employment**
- Mode: CRISPE
- Key Acts: LRA 66/1995, BCEA 75/1997
- Focus: Substantive/procedural fairness

**Commercial & Corporate**
- Mode: CO-STAR
- Key Acts: Companies Act 71/2008, CPA 68/2008
- Focus: Purposive interpretation, director duties

**Civil Litigation**
- Mode: Hybrid Legal
- Key Cases: *Makate*, *Trencon*
- Focus: Procedural compliance, precedent

Select a preset in the **Smart Prompt Builder** to auto-configure!"""
    
    # Default helpful response
    else:
        return f"""👋 I'm your SA Legal Prompting Assistant (SP1 Enhanced)!

I can help you with:
• **Framework Selection** - Find the best prompting approach
• **Optimization Modes** - CRISPE, CO-STAR, CoT, RISE, Hybrid, Claude
• **Practice Presets** - Auto-configure for your practice area
• **Court Guidance** - Tailor prompts for specific courts
• **Ethics Assessment** - Navigate AI use appropriately
• **Quality Scoring** - Improve your prompts

Just ask me anything about legal AI prompting!

*Your query: "{user_message}"*

Could you provide more context about your legal matter?"""

def recommend_framework(context: str) -> Tuple[str, str, float]:
    """Recommend best framework based on context analysis"""
    context_lower = context.lower()
    
    scores = {}
    
    # Constitutional matters
    if any(word in context_lower for word in ['constitutional', 'rights', 'bill of rights', 'section 9', 'equality']):
        scores['RICE'] = 0.9
        scores['CHAIN_OF_THOUGHT'] = 0.85
    
    # Commercial/Contract
    if any(word in context_lower for word in ['contract', 'commercial', 'company', 'business', 'corporate']):
        scores['ABCDE'] = 0.9
        scores['CASE'] = 0.85
    
    # Criminal
    if any(word in context_lower for word in ['criminal', 'accused', 'prosecution', 'defence', 'bail']):
        scores['CHAIN_OF_THOUGHT'] = 0.9
        scores['HOSTILE_WITNESS'] = 0.8
    
    # Labour
    if any(word in context_lower for word in ['labour', 'dismissal', 'ccma', 'unfair', 'strike']):
        scores['RICE'] = 0.85
        scores['SEVEN_PS'] = 0.8
    
    # Default
    if not scores:
        scores['RICE'] = 0.7
        scores['JUST_ASK'] = 0.65
    
    best = max(scores.keys(), key=lambda k: scores[k])
    fw = ALL_FRAMEWORKS.get(best)
    fw_name = fw.name if fw else list(ALL_FRAMEWORKS.values())[0].name
    return best, fw_name, scores[best]

def generate_smart_prompt(
    components: Dict, 
    framework_key: Optional[str] = None,
    optimization_mode: str = "STANDARD",
    output_format: str = "LEGAL_OPINION"
) -> Tuple[str, Optional[OptimizedPrompt]]:
    """
    Generate a smart prompt from builder components with optional AI optimization.
    
    Args:
        components: Dict with role, context, task, constraints, output_format, examples
        framework_key: Optional framework to apply
        optimization_mode: OptimizationMode enum key (STANDARD, CRISPE, CO_STAR, etc.)
        output_format: LegalOutputFormat enum key
        
    Returns:
        Tuple of (prompt_string, OptimizedPrompt object or None)
    """
    # Parse optimization mode
    try:
        opt_mode = OptimizationMode[optimization_mode]
    except KeyError:
        opt_mode = OptimizationMode.STANDARD
    
    # Parse output format
    try:
        out_format = LegalOutputFormat[output_format]
    except KeyError:
        out_format = LegalOutputFormat.LEGAL_OPINION
    
    # If standard mode, return simple formatted prompt
    if opt_mode == OptimizationMode.STANDARD:
        parts = []
        
        if components.get('role'):
            parts.append(f"[ROLE]\n{components['role']}")
        
        if components.get('context'):
            parts.append(f"[CONTEXT]\n{components['context']}")
        
        if components.get('task'):
            parts.append(f"[TASK]\n{components['task']}")
        
        if components.get('constraints'):
            parts.append(f"[CONSTRAINTS]\n{components['constraints']}")
        
        if components.get('output_format'):
            parts.append(f"[OUTPUT FORMAT]\n{components['output_format']}")
        
        if components.get('examples'):
            parts.append(f"[EXAMPLES/PRECEDENTS]\n{components['examples']}")
        
        basic_prompt = "\n\n".join(parts) if parts else "Start building your prompt by filling in the components above..."
        return basic_prompt, None
    
    # Apply advanced optimization
    optimized = optimize_legal_prompt(
        prompt_components=components,
        mode=opt_mode,
        output_format=out_format
    )
    
    return optimized.optimized, optimized

def export_prompt_to_text(prompt: str, metadata: Optional[Dict] = None) -> str:
    """Export prompt with metadata to formatted text"""
    metadata = metadata or {}
    output = []
    
    output.append("=" * 60)
    output.append("SA LEGAL PROMPTING ELITE - EXPORTED PROMPT")
    output.append("=" * 60)
    output.append(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    if metadata.get('framework'):
        output.append(f"Framework: {metadata['framework']}")
    if metadata.get('practice_area'):
        output.append(f"Practice Area: {metadata['practice_area']}")
    
    output.append("-" * 60)
    output.append("")
    output.append(prompt)
    output.append("")
    output.append("-" * 60)
    output.append("© SA Legal Prompting Elite Platform v4.0")
    
    return "\n".join(output)

def get_analytics_summary() -> Dict:
    """Generate analytics summary"""
    analytics = st.session_state.analytics
    history = st.session_state.prompt_history
    
    # Calculate statistics
    total_prompts = analytics.get('prompts_generated', 0)
    favorites = sum(1 for p in history if p.get('favorited'))
    
    # Framework usage
    framework_counts = Counter()
    for entry in history:
        source = entry.get('source', '')
        if 'Framework:' in source:
            fw = source.replace('Framework:', '').strip()
            framework_counts[fw] += 1
    
    # Session duration in minutes
    duration_mins = analytics.get('session_duration', 0) // 60
    
    return {
        'total_prompts': total_prompts,
        'favorites': favorites,
        'session_duration': duration_mins,
        'top_frameworks': framework_counts.most_common(5),
        'productivity_score': min(100, (total_prompts * 10) + (favorites * 5))
    }

# ═══════════════════════════════════════════════════════════════════════════════
# v4.0 - AI CHAT ASSISTANT COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

def render_ai_chat():
    """Render the AI Chat Assistant interface - Clean Monochrome"""
    st.markdown("## AI Legal Prompting Assistant")
    st.markdown("Get intelligent guidance on crafting perfect legal prompts. Ask me anything!")
    
    # Chat container
    chat_container = st.container()
    
    with chat_container:
        # Display chat history
        for message in st.session_state.chat_messages:
            # Use standard emoji for avatars - Streamlit requires proper emoji
            avatar = "🤖" if message["role"] == "assistant" else "👤"
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about legal prompting, frameworks, or get recommendations..."):
        # Add user message
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        
        # Track analytics
        st.session_state.analytics['chat_interactions'] += 1
        
        # Generate response with loading spinner
        with st.spinner("🤔 Thinking..."):
            response = get_ai_response(prompt, st.session_state.chat_context)
        st.session_state.chat_messages.append({"role": "assistant", "content": response})
        
        # Rerun to display
        st.rerun()
    
    # Quick action buttons - Clean labels
    st.markdown("### Quick Actions")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Recommend Framework", use_container_width=True):
            st.session_state.chat_messages.append({"role": "user", "content": "Which framework should I use?"})
            response = get_ai_response("recommend framework")
            st.session_state.chat_messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    with col2:
        if st.button("Court Guidance", use_container_width=True):
            st.session_state.chat_messages.append({"role": "user", "content": "Help me with court-specific prompts"})
            response = get_ai_response("court guidance")
            st.session_state.chat_messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    with col3:
        if st.button("Ethics Check", use_container_width=True):
            st.session_state.chat_messages.append({"role": "user", "content": "What are the ethical considerations for AI use?"})
            response = get_ai_response("ethics risk assessment")
            st.session_state.chat_messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    with col4:
        if st.button("Clear Chat", use_container_width=True):
            st.session_state.chat_messages = []
            st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# v4.4.0 - QUICK GENERATE (Simplified UX)
# ═══════════════════════════════════════════════════════════════════════════════

def render_quick_generate():
    """Ultra-simple prompt generation - 3 steps max"""
    
    st.markdown("""
    <div style="padding: 1.5rem; background: linear-gradient(135deg, #f0f9ff, #e0f2fe); 
                border-radius: 16px; margin-bottom: 1.5rem; text-align: center; color: #1a1a1a;">
        <h3 style="margin: 0; color: #1a1a1a;">⚡ Quick Generate</h3>
        <p style="margin: 0.5rem 0 0 0; opacity: 0.8; color: #333;">Paste your context → Select practice area → Get optimized prompt</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Step 1: Practice Area
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("### 1️⃣ Practice Area")
        practice_areas = {
            "constitutional": "⚖️ Constitutional Law",
            "criminal": "🚔 Criminal Law",
            "labour": "👷 Labour & Employment",
            "commercial": "💼 Commercial & Corporate",
            "litigation": "⚔️ Civil Litigation",
            "family": "👨‍👩‍👧 Family Law",
            "property": "🏠 Property & Conveyancing",
            "administrative": "🏛️ Administrative Law",
            "general": "📋 General Legal"
        }
        selected_area = st.selectbox(
            "Select your practice area",
            options=list(practice_areas.keys()),
            format_func=lambda x: practice_areas[x],
            key="quick_practice_area",
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown("### 2️⃣ Your Legal Matter")
        user_context = st.text_area(
            "Describe your legal matter, case, or question",
            placeholder="Example: My client was dismissed after 10 years of service. The employer claims misconduct but did not follow proper disciplinary procedures. We want to refer an unfair dismissal dispute to the CCMA...",
            height=150,
            key="quick_context",
            label_visibility="collapsed"
        )
    
    # Step 2: Generate button
    st.markdown("### 3️⃣ Generate")
    
    if st.button("🚀 Generate Optimized Prompt", type="primary", use_container_width=True, key="quick_generate_btn"):
        if not user_context:
            st.error("Please describe your legal matter first.")
            return
        
        # Auto-select optimization mode based on practice area
        mode_map = {
            "constitutional": "VARI_PLANNING",
            "criminal": "CHAIN_OF_THOUGHT",
            "labour": "Q_STAR",
            "commercial": "MICRO_OPT",
            "litigation": "Q_STAR",
            "family": "CO_STAR",
            "property": "VARI_PLANNING",
            "administrative": "CHAIN_OF_THOUGHT",
            "general": "CRISPE"
        }
        
        mode = mode_map.get(selected_area, "STANDARD")
        
        # Generate the prompt
        components = {
            'role': f"You are a senior South African legal practitioner specialising in {practice_areas[selected_area].split(' ', 1)[1]}.",
            'context': user_context,
            'task': "Provide comprehensive legal analysis, identify relevant legislation and case law, and recommend a course of action.",
            'constraints': "Use SAFLII citation format. Reference current South African legislation. Apply ubuntu principles where relevant.",
            'output_format': "Structure your response with: 1) Issue Identification 2) Applicable Law 3) Analysis 4) Recommendations",
            'examples': ""
        }
        
        preview_text, optimized_prompt = generate_smart_prompt(
            components,
            optimization_mode=mode,
            output_format="LEGAL_OPINION"
        )
        
        # Store result
        st.session_state.current_prompt = preview_text
        st.session_state.current_prompt_title = f"{practice_areas[selected_area]} Analysis"
        add_to_history(preview_text, f"Quick Generate: {practice_areas[selected_area]}")
        
        st.rerun()
    
    # Show result if available
    if st.session_state.get('current_prompt'):
        st.markdown("---")
        st.success(f"✅ **{st.session_state.get('current_prompt_title', 'Prompt')}** generated!")
        
        st.text_area(
            "📋 Your Optimized Prompt (Select All + Copy)",
            value=st.session_state.current_prompt,
            height=300,
            key="quick_output_display",
            help="Click inside, press Ctrl+A to select all, then Ctrl+C to copy"
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.info("💡 **Next:** Click in box above → Ctrl+A → Ctrl+C → Paste into AI")
        with col_b:
            if st.button("🗑️ Clear & Start Over", use_container_width=True, key="quick_clear"):
                st.session_state.current_prompt = ""
                st.session_state.current_prompt_title = ""
                st.rerun()


# ═══════════════════════════════════════════════════════════════════════════════
# v4.0 - SMART PROMPT BUILDER COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

@st.fragment
def render_smart_builder():
    """Render the Smart Prompt Builder with live preview - Clean Monochrome"""
    st.markdown("## Smart Prompt Builder")
    
    # Toggle between Simple and Advanced mode
    builder_mode = st.radio(
        "Builder Mode",
        ["⚡ Quick Generate", "🔧 Advanced Builder"],
        horizontal=True,
        key="builder_mode_toggle",
        help="Quick Generate: Paste context, select practice area, done! Advanced: Full customization."
    )
    
    if builder_mode == "⚡ Quick Generate":
        render_quick_generate()
        return
    
    # Advanced Builder continues below
    st.markdown("Build professional legal prompts with full customization.")
    
    col_builder, col_preview = st.columns([1, 1])
    
    with col_builder:
        st.markdown("### Components")
        
        # NEW SP1: Quick Presets
        st.markdown("#### Quick Presets")
        preset_options = {
            "NONE": "— Custom Configuration —",
            "CONSTITUTIONAL": "Constitutional Law",
            "CRIMINAL": "Criminal Law", 
            "LABOUR": "Labour & Employment",
            "COMMERCIAL": "Commercial & Corporate",
            "LITIGATION": "Civil Litigation",
            "FAMILY": "Family Law",
            "PROPERTY": "Property & Conveyancing",
            "ADMINISTRATIVE": "Administrative Law"
        }
        selected_preset = st.selectbox(
            "Practice Area Preset",
            options=list(preset_options.keys()),
            format_func=lambda x: preset_options[x],
            key="builder_preset",
            help="Select a preset to auto-configure optimal mode, format, and add relevant legislation/cases"
        )
        
        # Framework selector
        framework_options = ["Auto-detect"] + [f"{fw.acronym} - {fw.name}" for fw in ALL_FRAMEWORKS.values()]
        selected_fw = st.selectbox("Base Framework", framework_options, key="builder_fw_select")
        
        # Optimization Mode Selector - Enhanced with new modes
        st.markdown("#### AI Optimization Mode")
        optimization_modes = {
            "STANDARD": "Standard (Basic Formatting)",
            "CRISPE": "CRISPE (Role + Profile + Goals + Skills)",
            "CO_STAR": "CO-STAR (Context + Objective + Style + Tone)",
            "CHAIN_OF_THOUGHT": "Chain of Thought (Step-by-Step Reasoning)",
            "RISE": "RISE (Recursive Self-Improvement)",
            "O1_STYLE": "O1-Style (Structured Reasoning with Scoring)",
            "META_PROMPT": "Meta Prompt (AI Optimizes Your Prompt)",
            "HYBRID_LEGAL": "Hybrid Legal (CRISPE + CoT Combined)",
            "CLAUDE_STYLE": "Claude-Style (Detailed Task Instructions)",
            # SP2 New Modes
            "EXPERT_WITNESS": "Expert Witness (Technical Court Opinion)",
            "MEDIATION_ADR": "Mediation/ADR (Dispute Resolution)",
            "COMPLIANCE_AUDIT": "Compliance Audit (Regulatory Review)",
            # SP3 New Modes (from 302 Prompt Expert)
            "VARI_PLANNING": "VARI (DeepMind Variational Planning)",
            "Q_STAR": "Q* (A* + Q-Learning Strategy)",
            "MICRO_OPT": "Micro-Optimization (Microsoft Enhancement)",
            "OPENAI_OFFICIAL": "OpenAI Official (Best Practices)",
            "SPO_SELF_PLAY": "SPO (Self-Play Optimization)",
            "GUIDED_COMPLETE": "Guided Complete (Step-by-Step Builder)"
        }
        
        # Auto-select mode based on preset - Enhanced with SP3 modes
        default_mode_index = 0
        if selected_preset != "NONE":
            preset_mode_map = {
                "CONSTITUTIONAL": "VARI_PLANNING",  # Complex rights analysis benefits from VARI
                "CRIMINAL": "CHAIN_OF_THOUGHT",
                "LABOUR": "Q_STAR",  # Strategy optimization for labour disputes
                "COMMERCIAL": "MICRO_OPT",  # Precision for commercial contracts
                "LITIGATION": "Q_STAR",  # Litigation strategy with path optimization
                "FAMILY": "CO_STAR",
                "PROPERTY": "VARI_PLANNING",  # PIE evictions need systematic analysis
                "ADMINISTRATIVE": "CHAIN_OF_THOUGHT"
            }
            rec_mode = preset_mode_map.get(selected_preset, "STANDARD")
            if rec_mode in optimization_modes:
                default_mode_index = list(optimization_modes.keys()).index(rec_mode)
        
        # Mode category help
        mode_categories = """
        **Core Modes:** Standard, CRISPE, CO-STAR, CoT, RISE, O1-Style, Meta, Hybrid, Claude
        **Specialist:** Expert Witness, Mediation/ADR, Compliance Audit
        **Advanced AI (SP3):** VARI, Q*, Micro-Opt, OpenAI, SPO, Guided
        """
        
        selected_opt_mode = st.selectbox(
            "Select Enhancement Technique",
            options=list(optimization_modes.keys()),
            format_func=lambda x: optimization_modes[x],
            index=default_mode_index,
            key="builder_opt_mode",
            help="Choose how to enhance your prompt. Core modes for general use, Specialist for specific contexts, Advanced AI for cutting-edge optimization."
        )
        
        # Show mode-specific tip
        mode_tips = {
            "VARI_PLANNING": "💡 **VARI** excels at complex constitutional matters requiring systematic verification and reflection.",
            "Q_STAR": "💡 **Q*** optimizes litigation strategy by mapping decision paths and calculating expected outcomes.",
            "MICRO_OPT": "💡 **Micro-Opt** applies 15+ targeted improvements - ideal for refining existing prompts.",
            "OPENAI_OFFICIAL": "💡 **OpenAI Official** follows industry-standard best practices for balanced prompts.",
            "SPO_SELF_PLAY": "💡 **SPO** uses adversarial self-questioning to identify and fill gaps in your prompt.",
            "GUIDED_COMPLETE": "💡 **Guided** walks you through each component - perfect for learning prompt engineering."
        }
        if selected_opt_mode in mode_tips:
            st.info(mode_tips[selected_opt_mode])
        
        # Output Format Selector
        output_formats = {
            "LEGAL_OPINION": "Formal Legal Opinion",
            "HEADS_OF_ARGUMENT": "Heads of Argument",
            "ADVICE_LETTER": "Client Advice Letter",
            "CASE_ANALYSIS": "Case Analysis Memorandum",
            "CONTRACT_REVIEW": "Contract Review Summary",
            "RESEARCH_MEMO": "Legal Research Memorandum",
            "PLEADING": "Draft Pleading",
            "BRIEF": "Counsel Brief"
        }
        selected_output_format = st.selectbox(
            "Target Output Format",
            options=list(output_formats.keys()),
            format_func=lambda x: output_formats[x],
            key="builder_output_format"
        )
        
        # Component inputs
        with st.expander("Role Definition", expanded=True):
            role = st.text_area(
                "Define the legal persona",
                placeholder="e.g., You are a Senior Counsel (SC) specialising in constitutional law with 15 years experience before the Constitutional Court...",
                height=100,
                key="builder_role"
            )
        
        with st.expander("Context & Background", expanded=True):
            context = st.text_area(
                "Case context and background",
                placeholder="e.g., The client is challenging the validity of regulations promulgated under the National Health Act...",
                height=120,
                key="builder_context"
            )
        
        with st.expander("Task & Instructions", expanded=True):
            task = st.text_area(
                "What should the AI do?",
                placeholder="e.g., Analyse the constitutional validity of section X, applying the limitations analysis under section 36...",
                height=100,
                key="builder_task"
            )
        
        with st.expander("Constraints & Requirements"):
            constraints = st.text_area(
                "Limits and requirements",
                placeholder="e.g., Focus only on procedural aspects. Do not provide advice on merits. Use SAFLII citation format...",
                height=80,
                key="builder_constraints"
            )
        
        with st.expander("Output Format Details"):
            output_format_detail = st.text_area(
                "Desired output structure",
                placeholder="e.g., Provide analysis in the following structure:\n1. Issue Identification\n2. Applicable Law\n3. Analysis\n4. Conclusion",
                height=100,
                key="builder_output"
            )
        
        with st.expander("Examples & Precedents"):
            examples = st.text_area(
                "Reference cases or examples",
                placeholder="e.g., Follow the analytical approach in Harksen v Lane NO. Reference Minister of Home Affairs v Fourie for equality analysis...",
                height=80,
                key="builder_examples"
            )
    
    with col_preview:
        st.markdown("### Live Preview")
        
        # Build preview
        components = {
            'role': role if 'role' in dir() else st.session_state.get('builder_role', ''),
            'context': context if 'context' in dir() else st.session_state.get('builder_context', ''),
            'task': task if 'task' in dir() else st.session_state.get('builder_task', ''),
            'constraints': constraints if 'constraints' in dir() else st.session_state.get('builder_constraints', ''),
            'output_format': output_format_detail if 'output_format_detail' in dir() else st.session_state.get('builder_output', ''),
            'examples': examples if 'examples' in dir() else st.session_state.get('builder_examples', '')
        }
        
        # Practice Area Detection
        if components.get('context'):
            detected_area, confidence = detect_practice_area(components['context'])
            if confidence > 0.3:
                st.info(f"**Detected Practice Area:** {detected_area.value} ({int(confidence * 100)}% confidence)")
        
        # Generate optimized prompt
        preview_text, optimized_prompt = generate_smart_prompt(
            components,
            optimization_mode=selected_opt_mode if 'selected_opt_mode' in dir() else st.session_state.get('builder_opt_mode', 'STANDARD'),
            output_format=selected_output_format if 'selected_output_format' in dir() else st.session_state.get('builder_output_format', 'LEGAL_OPINION')
        )
        
        # Calculate quality score
        quality_score, suggestions = calculate_prompt_quality_score(preview_text, components)
        
        # Quality Score Display
        score_color = "🟢" if quality_score >= 70 else "🟡" if quality_score >= 40 else "🔴"
        st.markdown(f"### Prompt Quality: {score_color} {int(quality_score)}/100")
        
        # Preview panel
        st.markdown(f"""
        <div class="preview-panel">
            <div class="content">{preview_text.replace(chr(10), '<br>')}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Stats row
        word_count = len(preview_text.split())
        char_count = len(preview_text)
        token_estimate = len(preview_text) // 4
        
        col_stats1, col_stats2, col_stats3, col_stats4 = st.columns(4)
        with col_stats1:
            st.metric("Words", word_count)
        with col_stats2:
            st.metric("Characters", char_count)
        with col_stats3:
            st.metric("Est. Tokens", token_estimate)
        with col_stats4:
            complexity = "Simple" if word_count < 100 else "Moderate" if word_count < 250 else "Detailed"
            st.metric("Complexity", complexity)
        
        # Improvement suggestions
        if suggestions and quality_score < 80:
            with st.expander("Improvement Suggestions"):
                for suggestion in suggestions:
                    st.markdown(f"- {suggestion}")
        
        # Show optimization details if advanced mode used
        if optimized_prompt is not None:
            with st.expander("Optimization Details", expanded=True):
                st.markdown(f"**Mode:** {optimized_prompt.mode.value}")
                if optimized_prompt.quality_score > 0:
                    st.markdown(f"**Quality Score:** {int(optimized_prompt.quality_score)}/100")
                if optimized_prompt.token_estimate > 0:
                    st.markdown(f"**Token Estimate:** ~{optimized_prompt.token_estimate}")
                if optimized_prompt.practice_area:
                    st.markdown(f"**Practice Area:** {optimized_prompt.practice_area}")
                st.markdown("**Enhancements Applied:**")
                for note in optimized_prompt.enhancement_notes:
                    st.markdown(f"- {note}")
                st.markdown("**SA Legal Adaptations:**")
                for adaptation in optimized_prompt.sa_legal_adaptations:
                    st.markdown(f"- {adaptation}")
                if optimized_prompt.reasoning_structure:
                    st.markdown(f"**Reasoning Flow:** {optimized_prompt.reasoning_structure}")
        
        # Action buttons
        st.markdown("### Actions")
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("✅ Use This Prompt", type="primary", use_container_width=True, key="builder_copy"):
                st.session_state.current_prompt = preview_text
                st.session_state.current_prompt_title = f"Smart Builder ({optimization_modes.get(selected_opt_mode, 'Standard')})"
                add_to_history(preview_text, f"Smart Builder ({optimization_modes.get(selected_opt_mode, 'Standard')})", {'type': 'builder', 'optimization_mode': selected_opt_mode, 'quality_score': quality_score})
                st.toast("✅ Prompt ready! Go to Template Gallery to copy.")
        
        with col_b:
            if st.button("⭐ Save to Favorites", use_container_width=True, key="builder_save"):
                if preview_text not in st.session_state.favorites:
                    st.session_state.favorites.append(preview_text)
                add_to_history(preview_text, f"Smart Builder ({optimization_modes.get(selected_opt_mode, 'Standard')})", {'type': 'builder', 'favorited': True, 'optimization_mode': selected_opt_mode, 'quality_score': quality_score})
                st.toast("⭐ Saved to favorites!")
        
        # AI suggestions
        with st.expander("AI Suggestions"):
            if components.get('context'):
                fw_key, fw_name, confidence = recommend_framework(components['context'])
                st.info(f"**Recommended Framework:** {fw_name} ({int(confidence * 100)}% match)")
                
                # Optimization mode recommendation
                context_lower = components['context'].lower()
                if any(word in context_lower for word in ['complex', 'constitutional', 'appeal', 'supreme']):
                    st.info("**Recommended Mode:** Chain of Thought or RISE for complex matters")
                elif any(word in context_lower for word in ['client', 'advice', 'letter']):
                    st.info("**Recommended Mode:** CO-STAR for audience-focused outputs")
                elif any(word in context_lower for word in ['expert', 'witness', 'technical', 'opinion']):
                    st.info("**Recommended Mode:** Expert Witness for technical court opinions")
                elif any(word in context_lower for word in ['mediation', 'arbitration', 'settlement', 'dispute resolution']):
                    st.info("**Recommended Mode:** Mediation/ADR for dispute resolution")
                elif any(word in context_lower for word in ['compliance', 'audit', 'popia', 'fica', 'regulatory']):
                    st.info("**Recommended Mode:** Compliance Audit for regulatory reviews")
                else:
                    st.info("**Recommended Mode:** CRISPE for structured professional outputs")
            else:
                st.info("Add context to get AI framework recommendations")
        
        # SP2 NEW: Export Options
        with st.expander("Export Options"):
            if optimized_prompt:
                col_exp1, col_exp2 = st.columns(2)
                with col_exp1:
                    json_export = export_prompt_to_json(optimized_prompt)
                    st.download_button(
                        "Download JSON",
                        data=json_export,
                        file_name="optimized_prompt.json",
                        mime="application/json",
                        use_container_width=True
                    )
                with col_exp2:
                    md_export = export_prompt_to_markdown(optimized_prompt)
                    st.download_button(
                        "Download Markdown",
                        data=md_export,
                        file_name="optimized_prompt.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
            else:
                st.info("Generate a prompt to enable export options")
        
        # SP2 NEW: Detailed Quality Analysis
        with st.expander("Detailed Quality Analysis"):
            if preview_text and components:
                detailed_score = calculate_detailed_quality_score(preview_text, components)
                
                # Sub-scores display
                col_q1, col_q2, col_q3, col_q4 = st.columns(4)
                with col_q1:
                    st.metric("Clarity", f"{int(detailed_score.clarity_score)}/25")
                with col_q2:
                    st.metric("Specificity", f"{int(detailed_score.specificity_score)}/25")
                with col_q3:
                    st.metric("SA Context", f"{int(detailed_score.sa_context_score)}/25")
                with col_q4:
                    st.metric("Structure", f"{int(detailed_score.structure_score)}/25")
                
                # Strengths
                if detailed_score.strengths:
                    st.markdown("**✅ Strengths:**")
                    for strength in detailed_score.strengths:
                        st.markdown(f"- {strength}")
                
                # Suggestions
                if detailed_score.suggestions:
                    st.markdown("**💡 Suggestions:**")
                    for suggestion in detailed_score.suggestions:
                        st.markdown(f"- {suggestion}")

# ═══════════════════════════════════════════════════════════════════════════════
# SP2 - QUICK TEMPLATES COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

@st.fragment
def render_quick_templates():
    """Render the Quick Templates gallery - SP2 Feature"""
    st.markdown("## Quick Templates")
    st.markdown("Pre-configured prompts for common SA legal scenarios. Select a template to auto-fill the Smart Prompt Builder.")
    
    templates = get_quick_templates()
    
    # Group by category
    categories = {}
    for template in templates:
        if template.category not in categories:
            categories[template.category] = []
        categories[template.category].append(template)
    
    for category, cat_templates in categories.items():
        st.markdown(f"### {category}")
        
        cols = st.columns(3)
        for i, template in enumerate(cat_templates):
            with cols[i % 3]:
                st.markdown(f"""
                <div class="template-card" style="border: 1px solid #E0E0E0; border-radius: 8px; padding: 16px; margin-bottom: 16px;">
                    <h4 style="margin: 0 0 8px 0;">{template.name}</h4>
                    <p style="color: #666; font-size: 14px; margin: 0 0 12px 0;">{template.description}</p>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 12px; color: #888;">⚡ {template.recommended_mode.value.split('(')[0].strip()}</span>
                        <span style="font-size: 12px; color: #888;">🔥 {template.popularity} uses</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Use Template", key=f"template_{template.name}", use_container_width=True):
                    # Load template into session state
                    st.session_state['builder_role'] = template.components.get('role', '')
                    st.session_state['builder_context'] = template.components.get('context', '')
                    st.session_state['builder_task'] = template.components.get('task', '')
                    st.session_state['builder_constraints'] = template.components.get('constraints', '')
                    st.session_state['builder_output'] = template.components.get('output_format', '')
                    st.session_state['builder_examples'] = template.components.get('examples', '')
                    st.toast(f"✅ Template '{template.name}' loaded! Go to Build tab.")
                    st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# v4.0 - ANALYTICS DASHBOARD COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

@st.fragment
def render_analytics_dashboard():
    """Render the Analytics Dashboard - Clean Monochrome"""
    st.markdown("## 📊 Analytics Dashboard")
    st.markdown("Track your prompting productivity, usage patterns, and optimization insights.")
    
    summary = get_analytics_summary()
    
    # Key metrics - Enhanced with 5 columns
    st.markdown("### Key Metrics")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""
        <div class="analytics-card">
            <div class="analytics-value">{summary['total_prompts']}</div>
            <div class="analytics-label">Prompts Generated</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="analytics-card">
            <div class="analytics-value">{summary['favorites']}</div>
            <div class="analytics-label">Favorites Saved</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="analytics-card">
            <div class="analytics-value">{summary['session_duration']}m</div>
            <div class="analytics-label">Session Duration</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="analytics-card">
            <div class="analytics-value">{len(list(OptimizationMode))}</div>
            <div class="analytics-label">AI Modes Available</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown(f"""
        <div class="analytics-card">
            <div class="analytics-value">{summary['productivity_score']}</div>
            <div class="analytics-label">Productivity Score</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    st.markdown("### Usage Breakdown")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("#### Top Frameworks Used")
        if summary['top_frameworks']:
            for fw, count in summary['top_frameworks']:
                progress = count / max(1, summary['total_prompts'])
                st.progress(progress, text=f"{fw}: {count} uses")
        else:
            st.info("Generate prompts to see framework usage statistics")
    
    with col_chart2:
        st.markdown("#### Recent Activity")
        history = st.session_state.prompt_history[:10]
        if history:
            for entry in history:
                time_str = entry['timestamp'][:16].replace('T', ' ')
                st.markdown(f"• **{entry['source'][:30]}** - {time_str}")
        else:
            st.markdown("""
            <div style="text-align: center; padding: 1.5rem; background: #f9f9f9; border-radius: 10px; color: #1a1a1a;">
                <p style="margin: 0; color: #555;">📈 No activity yet</p>
                <p style="margin: 0.5rem 0 0 0; color: #666; font-size: 0.85rem;">Start generating prompts to see your activity here.</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Optimization Mode Recommendations
    st.markdown("### 🎯 Recommended Modes for Your Practice")
    
    rec_col1, rec_col2, rec_col3 = st.columns(3)
    with rec_col1:
        st.markdown("""
        <div style="padding: 1rem; background: #f0f9ff; border-radius: 10px; border-left: 3px solid #0ea5e9; color: #1a1a1a;">
            <strong style="color: #1a1a1a;">Constitutional Matters</strong><br>
            <span style="font-size: 0.9rem; color: #333;">Use: VARI Planning, Chain of Thought</span><br>
            <span style="font-size: 0.8rem; color: #555;">Best for rights analysis & limitations</span>
        </div>
        """, unsafe_allow_html=True)
    with rec_col2:
        st.markdown("""
        <div style="padding: 1rem; background: #f0fdf4; border-radius: 10px; border-left: 3px solid #22c55e; color: #1a1a1a;">
            <strong style="color: #1a1a1a;">Litigation Strategy</strong><br>
            <span style="font-size: 0.9rem; color: #333;">Use: Q* Strategy, Hybrid Legal</span><br>
            <span style="font-size: 0.8rem; color: #555;">Best for pathway optimization</span>
        </div>
        """, unsafe_allow_html=True)
    with rec_col3:
        st.markdown("""
        <div style="padding: 1rem; background: #fef3c7; border-radius: 10px; border-left: 3px solid #f59e0b; color: #1a1a1a;">
            <strong style="color: #1a1a1a;">Commercial/Compliance</strong><br>
            <span style="font-size: 0.9rem; color: #333;">Use: Micro-Opt, Compliance Audit</span><br>
            <span style="font-size: 0.8rem; color: #555;">Best for precision & thoroughness</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Productivity insights
    st.markdown("### 💡 Productivity Insights")
    
    insights = []
    if summary['total_prompts'] == 0:
        insights.append("🚀 **Get Started**: Generate your first prompt to begin tracking!")
    elif summary['total_prompts'] < 5:
        insights.append("🔥 **Warming Up**: You're getting started! Try different optimization modes.")
    else:
        insights.append("⭐ **Power User**: Great prompting activity! Consider exploring SP3 advanced modes.")
    
    if summary['favorites'] == 0 and summary['total_prompts'] > 0:
        insights.append("💾 **Tip**: Save your best prompts to favorites for quick reuse!")
    
    # Add mode suggestion based on activity
    if summary['total_prompts'] > 3:
        insights.append("🧠 **Try This**: VARI Planning mode excels at systematic constitutional analysis.")
    
    for insight in insights:
        st.info(insight)

# ═══════════════════════════════════════════════════════════════════════════════
# v4.0 - TEMPLATE GALLERY COMPONENT
# ═══════════════════════════════════════════════════════════════════════════════

QUICK_TEMPLATES = [
    {
        'title': 'Constitutional Rights Analysis',
        'category': 'Constitutional',
        'badge': 'Popular',
        'description': 'Comprehensive Bill of Rights analysis with limitations clause examination.',
        'uses': 342,
        'prompt': """[ROLE]
You are a Constitutional Law expert specialising in South African Bill of Rights jurisprudence.

[TASK]
Analyse the constitutional implications of [DESCRIBE MATTER], specifically:
1. Identify engaged rights under Chapter 2
2. Apply the Harksen v Lane rationality test
3. Conduct section 36 limitations analysis
4. Reference relevant Constitutional Court precedent

[FORMAT]
Structure as: Rights Engaged → Analysis → Limitations → Conclusion with citations in SAFLII format."""
    },
    {
        'title': 'CCMA Arbitration Prep',
        'category': 'Labour',
        'badge': 'Essential',
        'description': 'Prepare for CCMA arbitration with comprehensive issue analysis.',
        'uses': 289,
        'prompt': """[ROLE]
You are a Labour Law practitioner preparing for CCMA arbitration.

[TASK]
Prepare arbitration strategy for [DESCRIBE DISMISSAL/DISPUTE]:
1. Identify applicable sections of LRA 66 of 1995
2. Analyse procedural vs substantive fairness
3. Determine onus allocation per Kroeger v Visual Marketing
4. Recommend evidence and witnesses

[CONSTRAINTS]
Focus on practical preparation, not academic analysis."""
    },
    {
        'title': 'Contract Risk Analysis',
        'category': 'Commercial',
        'badge': 'Business',
        'description': 'Identify and analyse commercial contract risks under SA law.',
        'uses': 267,
        'prompt': """[ROLE]
You are a Commercial Attorney reviewing a contract.

[TASK]
Conduct risk analysis of [CONTRACT TYPE]:
🔴 Red Flags (immediate attention)
🟡 Amber Flags (needs negotiation)
🟢 Standard clauses

Focus on: Liability, Indemnities, Termination, IP, Jurisdiction

[REFERENCE]
Apply Consumer Protection Act s48-52 where applicable. Consider NCA implications."""
    },
    {
        'title': 'Criminal Defence Strategy',
        'category': 'Criminal',
        'badge': 'Defence',
        'description': 'Develop criminal defence strategy with element-by-element analysis.',
        'uses': 198,
        'prompt': """[ROLE]
You are Criminal Defence Counsel preparing trial strategy.

[TASK]
For charge of [SPECIFY OFFENCE]:
1. Break down elements of offence
2. Identify potential defences
3. Analyse strength of State's case
4. Recommend defence approach

[STANDARD]
Apply S v Zuma burden of proof. Consider bail implications if relevant."""
    },
    {
        'title': 'Legal Opinion Structure',
        'category': 'General',
        'badge': 'Template',
        'description': 'Professional legal opinion format for client delivery.',
        'uses': 456,
        'prompt': """[ROLE]
You are a Senior Associate drafting a legal opinion.

[TASK]
Prepare opinion on [LEGAL QUESTION] following structure:
1. Executive Summary
2. Background Facts
3. Issues for Opinion
4. Applicable Law
5. Analysis
6. Conclusion & Recommendations
7. Caveats & Assumptions

[TONE]
Professional, balanced, commercially pragmatic."""
    },
    {
        'title': 'Divorce Settlement Analysis',
        'category': 'Family',
        'badge': 'Family',
        'description': 'Analyse matrimonial property and settlement considerations.',
        'uses': 156,
        'prompt': """[ROLE]
You are a Family Law practitioner advising on divorce.

[TASK]
Analyse settlement considerations for [MARRIAGE REGIME - ANC/COP]:
1. Asset division approach
2. Maintenance considerations (s7 factors)
3. Children's interests (best interests standard)
4. Pension/retirement benefits

[LEGISLATION]
Apply Divorce Act 70 of 1979, Matrimonial Property Act 88 of 1984."""
    },
    # SP3 New Templates
    {
        'title': 'PIE Eviction Analysis',
        'category': 'Property',
        'badge': 'SP3 New',
        'description': 'Analyse eviction under Prevention of Illegal Eviction Act with constitutional rights.',
        'uses': 132,
        'prompt': """[ROLE]
You are a Property Law specialist with expertise in PIE evictions and informal settlement matters.

[VARI FRAMEWORK - Systematic Analysis]

VERIFY: Confirm understanding of:
- Occupier status and duration of occupation
- Nature of property and ownership
- Previous eviction attempts or engagements

ANALYSE: Examine systematically:
1. PIE Act 19 of 1998 requirements (sections 4-6)
2. Section 26 Constitutional housing rights
3. Meaningful engagement requirement (Olivia Road)
4. Alternative accommodation obligations

REFLECT: Question the analysis:
- Have I considered Port Elizabeth Municipality v Various Occupiers?
- Is the approach consistent with ubuntu and dignity?
- What would Constitutional Court require?

ITERATE: Refine with:
- Recent Housing Act amendments
- Municipal housing obligations
- Vulnerable persons considerations"""
    },
    {
        'title': 'Litigation Strategy Optimizer',
        'category': 'Litigation',
        'badge': 'SP3 Q*',
        'description': 'Map litigation pathways with cost-benefit analysis using Q* strategy.',
        'uses': 145,
        'prompt': """[ROLE]
You are a Senior Litigation Counsel advising on case strategy.

[Q* STRATEGY FRAMEWORK]

QUERY STATE:
- Current Position: [DESCRIBE CLIENT SITUATION]
- Goal: [DESIRED OUTCOME]
- Constraints: Budget, timeline, relationship considerations

STRATEGY PATHS:
Map available options:
A. Settlement negotiation - timeline, cost estimate, probability
B. Mediation/ADR - timeline, cost estimate, probability
C. Litigation - timeline, cost estimate, success probability
D. Alternative approaches

THINK AHEAD:
For each path, project 3 steps:
- Expected costs and duration
- Risk factors and dependencies
- Counter-party likely responses

ASSESS OPTIMALLY:
Calculate expected value for each path.
Consider non-monetary factors.

RECOMMEND:
Optimal strategy with rationale and contingencies."""
    },
    {
        'title': 'Restraint of Trade Review',
        'category': 'Commercial',
        'badge': 'SP3 New',
        'description': 'Evaluate validity and enforceability of restraint clauses.',
        'uses': 98,
        'prompt': """[ROLE]
You are a Commercial Law specialist with expertise in restraint of trade matters.

[TASK]
Analyse the validity of the following restraint clause:
[INSERT CLAUSE]

[ANALYSIS FRAMEWORK]
Apply the Magna Alloys / Basson v Chilwan test:

1. PROTECTABLE INTEREST
- Trade connections / customer relationships
- Trade secrets / confidential information
- Workforce stability

2. REASONABLENESS FACTORS
- Duration (is the period excessive?)
- Geographic scope (is the area too wide?)
- Activity scope (are restrictions too broad?)
- Consideration provided

3. CONSTITUTIONAL BALANCING
- Section 22 right to choose trade/occupation
- Apply Reddy v Siemens balancing approach

4. ENFORCEMENT ASSESSMENT
- Likelihood of enforcement
- Potential remedies (interdict, damages)
- Strategic recommendations"""
    },
    {
        'title': 'POPIA Compliance Audit',
        'category': 'Compliance',
        'badge': 'SP3 New',
        'description': 'Comprehensive data protection compliance assessment.',
        'uses': 176,
        'prompt': """[ROLE]
You are a Data Protection Specialist assessing POPIA compliance.

[COMPLIANCE AUDIT FRAMEWORK]

1. PROCESSING INVENTORY
- What personal information is processed?
- Who are the data subjects?
- What is the purpose of processing?

2. LAWFULNESS CONDITIONS (s8-12)
☐ Consent obtained (s11)
☐ Contractual necessity
☐ Legal obligation
☐ Legitimate interest (balanced)
☐ Public interest

3. DATA SUBJECT RIGHTS (s23-25)
☐ Access request procedure
☐ Correction mechanism
☐ Deletion/objection process
☐ Notification of breaches

4. SECURITY SAFEGUARDS (s19-22)
☐ Technical measures
☐ Organisational measures
☐ Third-party processor agreements
☐ Trans-border transfer compliance

5. GAP ANALYSIS
Identify non-compliance areas and remediation priority."""
    }
]


def render_mode_comparison():
    """Render Mode Comparison view to help users understand optimization modes"""
    st.markdown("## 🔍 Optimization Mode Comparison")
    st.markdown("Compare different AI optimization modes to choose the best one for your legal matter.")
    
    # Mode categories
    st.markdown("### Mode Categories")
    
    cat_col1, cat_col2, cat_col3 = st.columns(3)
    
    with cat_col1:
        st.markdown("""
        <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 12px; border-top: 4px solid #6b7280; color: #1a1a1a;">
            <h4 style="margin: 0 0 1rem 0; color: #1a1a1a;">🔧 Core Modes</h4>
            <p style="font-size: 0.9rem; line-height: 1.6; color: #333;">
            <strong>STANDARD</strong> - Basic formatting<br>
            <strong>CRISPE</strong> - Role + Profile + Goals<br>
            <strong>CO-STAR</strong> - Audience-focused<br>
            <strong>Chain of Thought</strong> - Step reasoning<br>
            <strong>RISE</strong> - Recursive improvement<br>
            <strong>O1-Style</strong> - Structured scoring<br>
            <strong>Meta Prompt</strong> - AI self-optimize<br>
            <strong>Hybrid Legal</strong> - CRISPE + CoT<br>
            <strong>Claude-Style</strong> - Detailed rules
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with cat_col2:
        st.markdown("""
        <div style="padding: 1.5rem; background: #f0f9ff; border-radius: 12px; border-top: 4px solid #0ea5e9; color: #1a1a1a;">
            <h4 style="margin: 0 0 1rem 0; color: #1a1a1a;">⚖️ Specialist Modes</h4>
            <p style="font-size: 0.9rem; line-height: 1.6; color: #333;">
            <strong>Expert Witness</strong><br>
            Rule 36(9) compliant technical opinions<br><br>
            <strong>Mediation/ADR</strong><br>
            5-phase dispute resolution structure<br><br>
            <strong>Compliance Audit</strong><br>
            POPIA, FICA, King IV protocols
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with cat_col3:
        st.markdown("""
        <div style="padding: 1.5rem; background: #f0fdf4; border-radius: 12px; border-top: 4px solid #22c55e; color: #1a1a1a;">
            <h4 style="margin: 0 0 1rem 0; color: #1a1a1a;">🚀 Advanced AI (SP3)</h4>
            <p style="font-size: 0.9rem; line-height: 1.6; color: #333;">
            <strong>VARI Planning</strong> - DeepMind reasoning<br>
            <strong>Q* Strategy</strong> - Litigation paths<br>
            <strong>Micro-Opt</strong> - Microsoft refinement<br>
            <strong>OpenAI Official</strong> - Best practices<br>
            <strong>SPO Self-Play</strong> - Adversarial Q&A<br>
            <strong>Guided Complete</strong> - Step-by-step
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Mode Selector for Details
    st.markdown("### Mode Details")
    
    mode_details = {
        "VARI_PLANNING": {
            "name": "🧠 VARI Planning",
            "source": "DeepMind Research",
            "best_for": "Constitutional analysis, complex rights matters, multi-step legal reasoning",
            "structure": "Verify → Analyse → Reflect → Iterate",
            "sa_adaptations": "Constitutional Court methodology, ubuntu principles, transformative constitutionalism"
        },
        "Q_STAR": {
            "name": "⭐ Q* Strategy",
            "source": "OpenAI Q* Research",
            "best_for": "Litigation strategy, settlement analysis, cost-benefit decisions",
            "structure": "Query State → Strategy Paths → Think Ahead → Assess → Recommend",
            "sa_adaptations": "CCMA timelines, court cost estimates, precedent probability weighting"
        },
        "MICRO_OPT": {
            "name": "🔬 Micro-Optimization",
            "source": "Microsoft Research",
            "best_for": "Refining existing prompts, incremental improvement, precision enhancement",
            "structure": "Measure → Identify → Correct → Refine → Optimize",
            "sa_adaptations": "SA citation format checks, legislation reference verification"
        },
        "OPENAI_OFFICIAL": {
            "name": "📘 OpenAI Official",
            "source": "OpenAI Best Practices",
            "best_for": "Balanced prompts, general legal tasks, reliable baseline",
            "structure": "Clear Instructions → Reference Text → Steps → Examples → Length",
            "sa_adaptations": "SAFLII integration, SA court hierarchy awareness"
        },
        "SPO_SELF_PLAY": {
            "name": "🎮 SPO Self-Play",
            "source": "HKUST/DeepWisdom",
            "best_for": "Gap identification, comprehensive coverage, iterative refinement",
            "structure": "Set Initial → Play Opponent → Optimize → Repeat",
            "sa_adaptations": "SA legal Q&A patterns, precedent completeness checks"
        },
        "GUIDED_COMPLETE": {
            "name": "📋 Guided Complete",
            "source": "302 Prompt Expert",
            "best_for": "Learning prompt engineering, training junior staff, comprehensive prompts",
            "structure": "Goal → User → Information → Deliverable → Examples → Delimiters",
            "sa_adaptations": "SA practice area guidance, legislation checklist, citation format"
        }
    }
    
    selected_mode = st.selectbox(
        "Select a mode to view details:",
        options=list(mode_details.keys()),
        format_func=lambda x: mode_details[x]["name"]
    )
    
    if selected_mode:
        mode = mode_details[selected_mode]
        
        detail_col1, detail_col2 = st.columns([1, 1])
        
        with detail_col1:
            st.markdown(f"""
            <div style="padding: 1.5rem; background: #fafafa; border-radius: 12px; color: #1a1a1a;">
                <h3 style="margin: 0 0 1rem 0; color: #1a1a1a;">{mode['name']}</h3>
                <p style="color: #333;"><strong>Source:</strong> {mode['source']}</p>
                <p style="color: #333;"><strong>Best For:</strong> {mode['best_for']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with detail_col2:
            st.markdown(f"""
            <div style="padding: 1.5rem; background: #f0f9ff; border-radius: 12px; color: #1a1a1a;">
                <p style="color: #333;"><strong>Structure:</strong><br>{mode['structure']}</p>
                <p style="color: #333;"><strong>SA Adaptations:</strong><br>{mode['sa_adaptations']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Try it button
        st.markdown("---")
        if st.button(f"🚀 Use {mode['name']} in Smart Builder", type="primary", use_container_width=True):
            st.session_state.builder_opt_mode = selected_mode
            st.toast(f"✅ {mode['name']} selected! Go to Smart Builder to create your prompt.")


@st.fragment
def render_template_gallery():
    """Render the Quick Template Gallery - Clean Monochrome"""
    st.markdown("## 📋 Template Gallery")
    
    # HERO: Show loaded prompt prominently if available
    if st.session_state.get('current_prompt'):
        title = st.session_state.get('current_prompt_title', 'Template')
        
        st.markdown(f"""
        <div style="padding: 1.5rem; background: linear-gradient(135deg, #22c55e, #16a34a); 
                    border-radius: 16px; color: white; margin-bottom: 1.5rem; text-align: center;">
            <h2 style="margin: 0; color: white;">✅ {title}</h2>
            <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Your prompt is ready! Copy it below and paste into ChatGPT, Claude, or any AI.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Primary action: The prompt in a copyable format
        st.text_area(
            "📋 Your Generated Prompt (Select All + Copy)",
            value=st.session_state.current_prompt,
            height=250,
            key="output_prompt_display",
            help="Click inside, press Ctrl+A to select all, then Ctrl+C to copy"
        )
        
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.info("💡 **How to use:** Click in the box above → Ctrl+A → Ctrl+C → Paste into your AI")
        with col2:
            if st.button("⭐ Save to Favorites", use_container_width=True):
                if st.session_state.current_prompt not in st.session_state.favorites:
                    st.session_state.favorites.append(st.session_state.current_prompt)
                    st.toast("⭐ Saved to favorites!")
        with col3:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.current_prompt = ""
                st.session_state.current_prompt_title = ""
                st.rerun()
        
        st.markdown("---")
        st.markdown("### Choose Another Template")
    else:
        st.markdown("Click any template below to generate your prompt instantly.")
    
    # Filters
    col_filter1, col_filter2 = st.columns([1, 3])
    with col_filter1:
        categories = ["All"] + list(set(t['category'] for t in QUICK_TEMPLATES))
        selected_cat = st.selectbox("Filter by Category", categories, key="gallery_filter")
    
    # Filter templates
    templates = QUICK_TEMPLATES if selected_cat == "All" else [t for t in QUICK_TEMPLATES if t['category'] == selected_cat]
    
    # Grid display
    st.markdown('<div class="template-gallery">', unsafe_allow_html=True)
    
    cols = st.columns(3)
    for idx, template in enumerate(templates):
        with cols[idx % 3]:
            with st.container():
                st.markdown(f"""
                <div class="template-card">
                    <div class="template-header">
                        <h4>{template['title']}</h4>
                        <span class="template-badge">{template['badge']}</span>
                    </div>
                    <div class="template-body">
                        <p>{template['description']}</p>
                        <div class="template-meta">
                            <span>{template['category']}</span>
                            <span>{template['uses']} uses</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Use Template", key=f"template_{idx}", use_container_width=True):
                    st.session_state.current_prompt = template['prompt']
                    st.session_state.current_prompt_title = template['title']
                    add_to_history(template['prompt'], f"Template: {template['title']}")
                    st.toast(f"✅ Loaded: {template['title']} - Scroll up to view!")
                    st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# COMPONENTS
# ═══════════════════════════════════════════════════════════════════════════════

def render_header():
    """Render the hero header - Ultra Modern Monochrome Edition"""
    total_resources = (
        len(ALL_FRAMEWORKS) + len(ALL_SPECIALIST_COURTS) + len(ALL_LEGISLATION) + 
        len(ALL_GUIDELINES) + len(ALL_PRACTICE_PROMPTS) + len(ALL_DOCUMENT_TEMPLATES) + 
        len(ALL_WORKFLOWS) + len(QUICK_TEMPLATES)
    )
    
    # Calculate session productivity
    session_prompts = st.session_state.prompt_count
    productivity = "🔥 On Fire" if session_prompts > 10 else "⚡ Active" if session_prompts > 5 else "✨ Ready"
    
    # Count optimization modes
    num_modes = len(list(OptimizationMode))
    
    st.markdown(f"""
    <div class="hero-header">
        <h1>⚖️ SA Legal Prompting Elite</h1>
        <p class="subtitle">World-Class AI Prompting Platform for South African Legal Professionals</p>
        <div class="stats-container">
            <span class="stats-badge">AI Assistant</span>
            <span class="stats-badge">Smart Builder</span>
            <span class="stats-badge">{num_modes} AI Modes</span>
            <span class="stats-badge">{len(ALL_FRAMEWORKS)} Frameworks</span>
            <span class="stats-badge">{len(ALL_SPECIALIST_COURTS)} Courts</span>
            <span class="stats-badge">{len(ALL_LEGISLATION)} Statutes</span>
            <span class="stats-badge">{len(ALL_PRACTICE_PROMPTS) + len(QUICK_TEMPLATES)} Templates</span>
            <span class="stats-badge gold">{total_resources}+ Resources</span>
            <span class="stats-badge gold">{productivity}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Render the sidebar with navigation and tools - Ultra Modern Monochrome"""
    with st.sidebar:
        # Sidebar Header with Logo
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem 0; margin-bottom: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.08);">
            <div style="font-size: 1.75rem; margin-bottom: 0.5rem; opacity: 0.9;">⚖️</div>
            <h2 style="margin: 0; font-size: 1.1rem; font-weight: 600; letter-spacing: -0.01em;">Legal Prompting Elite</h2>
            <p style="margin: 0.25rem 0 0 0; opacity: 0.5; font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase;">v4.4.0 Advanced AI</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("## Quick Search")
        search_query = st.text_input("Search all resources...", placeholder="Type to search...", key="global_search", label_visibility="collapsed")
        
        if search_query:
            # Track search
            if search_query not in st.session_state.analytics.get('search_queries', []):
                st.session_state.analytics.setdefault('search_queries', []).append(search_query)
            
            results = search_all_resources(search_query)
            if results:
                st.markdown(f"### Found {len(results)} results")
                for result in results[:10]:
                    with st.expander(f"{result['name']}", expanded=False):
                        st.caption(result['type'])
                        st.write(result['description'])
            else:
                st.markdown("""
                <div style="text-align: center; padding: 2rem; background: #f5f5f5; border-radius: 12px; color: #1a1a1a;">
                    <h4 style="margin: 0 0 0.5rem 0; color: #1a1a1a;">🔍 No results found</h4>
                    <p style="color: #555; margin: 0;">Try different keywords or browse the Reference tab.</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Session Stats
        st.markdown("## Session Stats")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Prompts", st.session_state.prompt_count, delta=f"+{st.session_state.prompt_count}" if st.session_state.prompt_count > 0 else None)
        with col2:
            favorites_count = sum(1 for p in st.session_state.prompt_history if p.get('favorited'))
            st.metric("Favorites", favorites_count)
        
        # Productivity Score
        summary = get_analytics_summary()
        st.progress(min(summary['productivity_score'] / 100, 1.0), text=f"Productivity: {summary['productivity_score']}%")
        
        st.markdown("---")
        
        # Recent History
        st.markdown("## Recent Prompts")
        if st.session_state.prompt_history:
            for idx, entry in enumerate(st.session_state.prompt_history[:5]):
                icon = "⭐" if entry.get('favorited') else "📝"
                with st.expander(f"{icon} {entry['source'][:25]}...", expanded=False):
                    st.code(entry['prompt'][:200] + "..." if len(entry['prompt']) > 200 else entry['prompt'])
                    st.caption(f"Generated: {entry['timestamp'][:16]}")
                    col_a, col_b = st.columns(2)
                    with col_a:
                        if st.button("Copy", key=f"sidebar_copy_{idx}_{entry['id']}", help="Copy prompt"):
                            st.session_state.copied_prompt = entry['prompt']
                            st.toast("Copied!")
                    with col_b:
                        if st.button("★" if not entry.get('favorited') else "☆", key=f"sidebar_fav_{idx}_{entry['id']}", help="Toggle favorite"):
                            toggle_favorite(entry['id'])
                            st.rerun()
        else:
            st.markdown("""
            <div style="text-align: center; padding: 1.5rem; background: rgba(255,255,255,0.1); border-radius: 10px; margin: 0.5rem 0;">
                <p style="margin: 0; opacity: 0.8; font-size: 0.85rem;">📝 No prompts yet</p>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.6; font-size: 0.75rem;">Try the AI Assistant or Build tab to get started!</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Settings
        st.markdown("## Settings")
        
        # Cerebras AI API Configuration
        with st.expander("🤖 AI API Configuration", expanded=not st.session_state.get('cerebras_api_key')):
            st.markdown("""
            **Enable AI-Powered Responses**
            
            Connect to Cerebras AI for intelligent, context-aware responses in the chat assistant.
            """)
            
            api_key = st.text_input(
                "Cerebras API Key",
                type="password",
                value=st.session_state.get('cerebras_api_key', ''),
                placeholder="csk-xxxxxxxxxxxxxxxx",
                key="cerebras_key_input",
                help="Your Cerebras API key for AI-powered chat"
            )
            
            if api_key != st.session_state.get('cerebras_api_key', ''):
                st.session_state.cerebras_api_key = api_key
            
            st.session_state.use_ai_api = st.toggle(
                "Enable AI API",
                value=st.session_state.get('use_ai_api', False) and bool(st.session_state.get('cerebras_api_key')),
                disabled=not st.session_state.get('cerebras_api_key'),
                help="Toggle to use Cerebras AI for chat responses"
            )
            
            if st.session_state.get('cerebras_api_key') and st.session_state.get('use_ai_api'):
                st.success("✅ AI API Connected")
            elif st.session_state.get('cerebras_api_key'):
                st.info("🔑 API key saved. Enable toggle above to use AI.")
            else:
                st.warning("⚠️ No API key. Using built-in responses.")
            
            with st.popover("📖 How to get a Cerebras API key"):
                st.markdown("""
                ### Get Your Free Cerebras API Key
                
                1. **Go to** [cloud.cerebras.ai](https://cloud.cerebras.ai)
                2. **Sign up** for a free account
                3. **Navigate** to API Keys section
                4. **Create** a new API key
                5. **Copy** the key (starts with `csk-`)
                6. **Paste** it above
                
                **Why Cerebras?**
                - ⚡ Fastest inference (up to 2000 tokens/sec)
                - 🆓 Free tier available
                - 🧠 Llama 3.3 70B model
                - 🔒 Enterprise-grade security
                
                **Model Used:** `llama-3.3-70b`
                """)
        
        st.session_state.show_tips = st.toggle("Show Practice Tips", value=st.session_state.show_tips)
        st.session_state.preferences['auto_copy'] = st.toggle("Auto-copy prompts", value=st.session_state.preferences.get('auto_copy', True))
        st.session_state.preferences['keyboard_shortcuts'] = st.toggle("Show shortcuts hint", value=st.session_state.preferences.get('keyboard_shortcuts', True))
        
        # Reset onboarding option
        if st.button("Show Welcome Guide", use_container_width=True, help="View the onboarding tutorial again"):
            st.session_state.onboarded = False
            st.rerun()
        
        st.markdown("---")
        
        # Quick Actions
        st.markdown("## Quick Actions")
        if st.button("Clear History", use_container_width=True):
            st.session_state.confirm_clear_history = True
        
        # Confirmation dialog for clear history
        if st.session_state.get('confirm_clear_history', False):
            st.warning("⚠️ This will delete all prompt history. Are you sure?")
            conf_col1, conf_col2 = st.columns(2)
            with conf_col1:
                if st.button("✓ Yes, Clear", use_container_width=True, type="primary"):
                    st.session_state.prompt_history = []
                    st.session_state.prompt_count = 0
                    st.session_state.confirm_clear_history = False
                    st.toast("🗑️ History cleared!")
                    st.rerun()
            with conf_col2:
                if st.button("✗ Cancel", use_container_width=True):
                    st.session_state.confirm_clear_history = False
                    st.rerun()
        
        if st.button("View Analytics", use_container_width=True):
            st.toast("📊 Switch to Analytics tab!")
        
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; opacity: 0.5; font-size: 0.7rem; padding: 1rem 0;">
            <p style="margin: 0;">Made for SA Legal Professionals</p>
            <p style="margin: 0.25rem 0 0 0; font-size: 0.65rem; letter-spacing: 0.05em;">Version 4.1 • UX Enhanced Edition</p>
        </div>
        """, unsafe_allow_html=True)

def render_prompt_output(prompt: str, source: str = "Generated Prompt"):
    """Render a prompt output with copy functionality using st.code (has built-in copy button)"""
    st.markdown("### 📋 Generated Prompt")
    
    # Use st.code which has a built-in copy button
    st.code(prompt, language=None, wrap_lines=True)
    
    col1, col2, col3 = st.columns([1, 1, 4])
    with col1:
        if st.button("💾 Save to History", key=f"save_hist_{hash(prompt)}"):
            add_to_history(prompt, source)
            st.toast("✅ Saved to history!")
    with col2:
        if st.button("⭐ Add to Favorites", key=f"save_fav_{hash(prompt)}"):
            add_to_history(prompt, source, {'favorited': True})
            st.toast("⭐ Added to favorites!")

# ═══════════════════════════════════════════════════════════════════════════════
# TAB CONTENT RENDERERS
# ═══════════════════════════════════════════════════════════════════════════════

def render_frameworks_tab():
    """Render the Frameworks tab content - Clean Monochrome"""
    st.markdown("## Advanced Prompting Frameworks")
    st.markdown("Select a proven framework to structure your legal AI prompts for optimal results.")
    
    # Category filter
    categories = list(set(fw.category.value for fw in ALL_FRAMEWORKS.values()))
    selected_category = st.selectbox("Filter by Category", ["All"] + sorted(categories), key="fw_category")
    
    # Framework selection
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### Available Frameworks")
        frameworks = ALL_FRAMEWORKS
        if selected_category != "All":
            frameworks = {k: v for k, v in ALL_FRAMEWORKS.items() if v.category.value == selected_category}
        
        for key, fw in frameworks.items():
            difficulty_color = {"Beginner": "🟢", "Intermediate": "🟡", "Advanced": "🔴"}.get(fw.difficulty, "⚪")
            if st.button(
                f"{fw.acronym} - {fw.name[:30]}{'...' if len(fw.name) > 30 else ''}\n{difficulty_color} {fw.difficulty}",
                key=f"fw_btn_{key}",
                use_container_width=True
            ):
                st.session_state.selected_framework = key
    
    with col2:
        if st.session_state.selected_framework and st.session_state.selected_framework in ALL_FRAMEWORKS:
            fw = ALL_FRAMEWORKS[st.session_state.selected_framework]
            
            st.markdown(f"""
            <div class="section-card">
                <span class="framework-acronym">{fw.acronym}</span>
                <h3>{fw.name}</h3>
                <p>{fw.description}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Framework details
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Category", fw.category.value)
            with col_b:
                st.metric("Difficulty", fw.difficulty)
            with col_c:
                st.metric("Components", len(fw.components))
            
            # Components
            if st.session_state.show_tips:
                with st.expander("Framework Components", expanded=True):
                    for comp in fw.components:
                        st.markdown(f"**{comp.get('letter', '')} - {comp.get('component', '')}**")
                        st.caption(comp.get('description', ''))
                        if comp.get('example'):
                            st.info(f"Example: {comp['example'][:150]}...")
            
            # SA Adaptations
            with st.expander("SA Legal Adaptations"):
                for adaptation in fw.sa_adaptations:
                    st.markdown(f"• {adaptation}")
            
            # Generate prompt
            st.markdown("### Generate Your Prompt")
            user_context = st.text_area(
                "📝 Enter your legal context",
                placeholder="Describe your legal matter, case facts, or question...",
                height=150,
                key="fw_context"
            )
            
            if st.button("🚀 Generate Framework Prompt", type="primary", key="generate_fw"):
                if user_context:
                    # Generate prompt using framework structure
                    prompt = f"""# {fw.name} ({fw.acronym}) Prompt

## Context
{user_context}

## Framework Application
"""
                    for comp in fw.components:
                        prompt += f"\n### {comp.get('letter', '')} - {comp.get('component', '')}\n"
                        prompt += f"*{comp.get('description', '')}*\n"
                        prompt += f"[Apply this to your context]\n"
                    
                    prompt += f"""
## SA-Specific Requirements
- Use SAFLII neutral citation format
- Reference SA legislation by Act number
- Apply Constitutional Court methodology where relevant
- Consider ubuntu and transformative constitutionalism principles
- Verify all citations independently

## SA Legal Adaptations for {fw.acronym}
"""
                    for adaptation in fw.sa_adaptations:
                        prompt += f"• {adaptation}\n"
                    
                    st.markdown("### 📋 Generated Prompt")
                    render_prompt_output(prompt, f"Framework: {fw.acronym}")
                else:
                    st.warning("Please enter your legal context first.")
            
            # Example prompt
            with st.expander("View Example Prompt"):
                st.code(fw.example_prompt, language=None)
        else:
            st.info("👈 Select a framework from the list to get started")

def render_courts_tab():
    """Render the Courts tab content - Clean Monochrome"""
    st.markdown("## SA Specialist Courts & Tribunals")
    st.markdown("Comprehensive guidance for appearances before South Africa's specialist courts.")
    
    # Court category filter
    categories = list(set(court.category.value for court in ALL_SPECIALIST_COURTS.values()))
    selected_category = st.selectbox("Filter by Category", ["All"] + sorted(categories), key="court_category")
    
    # Court selection
    courts = ALL_SPECIALIST_COURTS
    if selected_category != "All":
        courts = {k: v for k, v in ALL_SPECIALIST_COURTS.items() if v.category.value == selected_category}
    
    court_names = {f"{c.name} ({c.saflii_code})": key for key, c in courts.items()}
    selected_court = st.selectbox("🏛️ Select Court", options=[""] + list(court_names.keys()), key="court_select")
    
    if selected_court and selected_court in court_names:
        court_key = court_names[selected_court]
        court = ALL_SPECIALIST_COURTS[court_key]
        
        # Court info cards
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="section-card">
                <h3>📍 SAFLII Code</h3>
                <p style="font-size: 1.5rem; font-weight: bold; color: #007A4D;">{court.saflii_code}</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="section-card gold-accent">
                <h3>📜 Establishing Legislation</h3>
                <p>{court.establishing_legislation}</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="section-card red-accent">
                <h3>⬆️ Appeal Route</h3>
                <p>{court.appeal_route}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Jurisdiction details
        with st.expander("Jurisdiction Details", expanded=True):
            jurisdiction_desc = getattr(court, 'jurisdiction_description', None)
            if jurisdiction_desc:
                st.write(jurisdiction_desc)
            else:
                st.write("Specialist court with defined jurisdiction under establishing legislation.")
            
            practice_areas = getattr(court, 'key_practice_areas', None)
            if practice_areas:
                st.markdown("**Key Practice Areas:**")
                for area in practice_areas:
                    st.markdown(f"• {area}")
            
            # Display any additional court info
            court_cat = getattr(court, 'category', None)
            if court_cat:
                cat_val = court_cat.value if hasattr(court_cat, 'value') else str(court_cat)
                st.markdown(f"**Category:** {cat_val}")
        
        # Generate court prompt guidance
        st.markdown("### 📋 Prompt Guidance for This Court")
        prompt_guidance = generate_court_prompt_guidance(court)
        render_prompt_output(prompt_guidance, f"Court: {court.name}")

def render_legislation_tab():
    """Render the Legislation tab content - Clean Monochrome"""
    st.markdown("## SA Key Legislation Reference")
    st.markdown("Access structured prompts for South Africa's most important statutes.")
    
    # Legislation selection
    leg_names = {f"{leg.short_title} ({leg.act_number})": key for key, leg in ALL_LEGISLATION.items()}
    selected_leg = st.selectbox("📜 Select Legislation", options=[""] + sorted(list(leg_names.keys())), key="leg_select")
    
    if selected_leg and selected_leg in leg_names:
        leg_key = leg_names[selected_leg]
        leg = ALL_LEGISLATION[leg_key]
        
        st.markdown(f"""
        <div class="section-card">
            <h3>{leg.full_title}</h3>
            <p><strong>Act Number:</strong> {leg.act_number}</p>
            <p>{leg.purpose}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Key provisions
        with st.expander("Key Provisions", expanded=True):
            provisions_to_show = leg.key_provisions[:8] if hasattr(leg, 'key_provisions') else []
            for prov in provisions_to_show:
                st.markdown(f"**{prov.section}:** {prov.title}")
                prov_summary = getattr(prov, 'summary', None)
                if prov_summary:
                    display_summary = prov_summary[:150] + "..." if len(prov_summary) > 150 else prov_summary
                    st.caption(display_summary)
        
        # Generate legislation prompt
        st.markdown("### ❓ Ask About This Legislation")
        leg_question = st.text_area(
            "Your Question",
            placeholder="What would you like to know about this legislation?",
            key="leg_question"
        )
        
        if st.button("🚀 Generate Legislation Prompt", type="primary", key="generate_leg"):
            if leg_question:
                prompt = generate_legislation_prompt(leg, leg_question)
                st.markdown("### 📋 Generated Prompt")
                render_prompt_output(prompt, f"Legislation: {leg.short_title}")
            else:
                st.warning("Please enter your question first.")

def render_ethics_tab():
    """Render the Ethics tab content - Clean Monochrome"""
    st.markdown("## AI Ethics & Risk Assessment")
    st.markdown("Navigate ethical AI use in South African legal practice with comprehensive guidelines.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Ethical Guidelines")
        guideline_names = {g.title: key for key, g in ALL_GUIDELINES.items()}
        selected_guideline = st.selectbox("Select Guideline", options=[""] + list(guideline_names.keys()), key="ethics_select")
        
        if selected_guideline and selected_guideline in guideline_names:
            g_key = guideline_names[selected_guideline]
            guideline = ALL_GUIDELINES[g_key]
            
            st.markdown(f"""
            <div class="section-card">
                <h3>{guideline.title}</h3>
                <p>{guideline.description}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if hasattr(guideline, 'requirements'):
                with st.expander("Requirements"):
                    for req in guideline.requirements[:5]:
                        st.markdown(f"• {req}")
    
    with col2:
        st.markdown("### AI Use Risk Assessment")
        scenario_names = [s.scenario for s in AI_USE_SCENARIOS]
        selected_scenario = st.selectbox("Select Scenario", options=[""] + scenario_names, key="scenario_select")
        
        if selected_scenario:
            scenario = next((s for s in AI_USE_SCENARIOS if s.scenario == selected_scenario), None)
            if scenario:
                # Risk assessment
                risk_val = scenario.risk_level.value if hasattr(scenario.risk_level, 'value') else str(scenario.risk_level)
                st.markdown(get_risk_badge(risk_val), unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="section-card">
                    <h3>{scenario.scenario}</h3>
                    <p>{scenario.recommended_approach}</p>
                </div>
                """, unsafe_allow_html=True)
                
                if hasattr(scenario, 'safeguards_required'):
                    with st.expander("Safeguards Required"):
                        for sf in scenario.safeguards_required:
                            st.markdown(f"✓ {sf}")
    
    # Ethics checklist generator
    st.markdown("---")
    st.markdown("### Generate Ethics Checklist")
    context_desc = st.text_area(
        "Describe your AI use case",
        placeholder="E.g., Using AI to draft initial research summaries for a commercial litigation matter...",
        key="ethics_context"
    )
    
    if st.button("🚀 Generate Ethics Checklist", type="primary", key="generate_ethics"):
        if context_desc:
            # Generate custom ethics checklist based on context
            checklist = f"""# SA LEGAL AI ETHICS COMPLIANCE CHECKLIST

## Your Use Case
{context_desc}

## Before Using AI, Confirm:

### Confidentiality
□ All client-identifying information has been removed/anonymised
□ Parties are referred to as "Client", "Party A", "Applicant", etc.
□ No privileged strategy or settlement positions disclosed
□ Using appropriate enterprise/professional AI tool

### Verification Commitment  
□ I will verify ALL citations on SAFLII before use
□ I will read actual judgments, not rely on AI summaries
□ I will apply professional judgment to all outputs
□ I understand AI may "hallucinate" cases that don't exist

### Supervision & Responsibility
□ All AI output will be reviewed before use
□ I accept full responsibility for final work product
□ AI is a tool assisting my work, not replacing my judgment
□ A qualified legal practitioner will supervise this work

### South African Context
□ Apply South African law and constitutional values
□ Use SAFLII neutral citation format
□ Consider ubuntu and transformative constitutionalism principles
□ Reference SA authorities (foreign law only if specifically relevant)

### Risk Assessment
Based on your use case, consider:
🟢 Low Risk: Research, summaries, procedural queries
🟡 Medium Risk: Analysis, strategy options, client communications  
🔴 High Risk: Court submissions, advice, opinions
⚫ Critical: Ethics decisions, fiduciary matters, final instructions

## Signed Acknowledgement
I, the undersigned legal practitioner, confirm compliance with this checklist.

Date: _______________
Practitioner: _______________
"""
            st.markdown("### 📋 Ethics Checklist")
            render_prompt_output(checklist, "Ethics Checklist")
        else:
            st.warning("Please describe your AI use case first.")

def render_practice_tab():
    """Render the Practice Areas tab content - Clean Monochrome"""
    st.markdown("## Practice Area Prompts")
    st.markdown("Specialized prompts tailored for each South African legal practice area.")
    
    # Practice area filter
    areas = list(set(p.practice_area.value for p in ALL_PRACTICE_PROMPTS.values()))
    selected_area = st.selectbox("Filter by Practice Area", ["All"] + sorted(areas), key="practice_area")
    
    # Filter prompts
    prompts = ALL_PRACTICE_PROMPTS
    if selected_area != "All":
        prompts = {k: v for k, v in ALL_PRACTICE_PROMPTS.items() if v.practice_area.value == selected_area}
    
    prompt_names = {p.title: key for key, p in prompts.items()}
    selected_prompt = st.selectbox("📋 Select Prompt Template", options=[""] + sorted(list(prompt_names.keys())), key="practice_select")
    
    if selected_prompt and selected_prompt in prompt_names:
        p_key = prompt_names[selected_prompt]
        practice_prompt = ALL_PRACTICE_PROMPTS[p_key]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            <div class="section-card">
                <h3>{practice_prompt.title}</h3>
                <p><strong>Practice Area:</strong> {practice_prompt.practice_area.value}</p>
                <p><strong>Type:</strong> {practice_prompt.prompt_type.value}</p>
                <p>{practice_prompt.description}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if st.session_state.show_tips:
                st.markdown("### 💡 Practice Tips")
                for tip in practice_prompt.practice_tips[:3]:
                    st.info(f"💡 {tip}")
        
        # Key legislation and cases
        col_a, col_b = st.columns(2)
        with col_a:
            with st.expander("📜 Key Legislation"):
                for leg in practice_prompt.key_legislation:
                    st.markdown(f"• {leg}")
        with col_b:
            with st.expander("⚖️ Key Cases"):
                for case in practice_prompt.key_cases[:5]:
                    st.markdown(f"• {case}")
        
        # Generate practice prompt
        st.markdown("### 📝 Generate Your Prompt")
        user_input = st.text_area(
            "Enter your case details",
            placeholder="Describe your matter with relevant facts...",
            height=150,
            key="practice_input"
        )
        
        if st.button("🚀 Generate Practice Prompt", type="primary", key="generate_practice"):
            if user_input:
                prompt = generate_practice_prompt(practice_prompt, user_input)
                st.markdown("### 📋 Generated Prompt")
                render_prompt_output(prompt, f"Practice: {practice_prompt.title}")
            else:
                st.warning("Please enter your case details first.")

def render_documents_tab():
    """Render the Documents tab content - Clean Monochrome"""
    st.markdown("## Document Templates")
    st.markdown("AI-assisted document drafting templates for South African legal practice.")
    
    # Category filter
    categories = list(set(d.category.value for d in ALL_DOCUMENT_TEMPLATES.values()))
    selected_category = st.selectbox("Filter by Category", ["All"] + sorted(categories), key="doc_category")
    
    # Filter documents
    docs = ALL_DOCUMENT_TEMPLATES
    if selected_category != "All":
        docs = {k: v for k, v in ALL_DOCUMENT_TEMPLATES.items() if v.category.value == selected_category}
    
    doc_names = {d.title: key for key, d in docs.items()}
    selected_doc = st.selectbox("📄 Select Document Template", options=[""] + sorted(list(doc_names.keys())), key="doc_select")
    
    if selected_doc and selected_doc in doc_names:
        d_key = doc_names[selected_doc]
        doc = ALL_DOCUMENT_TEMPLATES[d_key]
        
        st.markdown(f"""
        <div class="section-card">
            <h3>{doc.title}</h3>
            <p><strong>Category:</strong> {doc.category.value}</p>
            <p><strong>Est. Time:</strong> {doc.time_estimate}</p>
            <p>{doc.description}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Use cases
        with st.expander("🎯 Use Cases"):
            for use_case in doc.use_cases:
                st.markdown(f"• {use_case}")
        
        # Document structure
        with st.expander("📑 Document Structure", expanded=True):
            for section in doc.structure[:6]:
                req_badge = "🔴 Required" if section.required else "⚪ Optional"
                st.markdown(f"**{section.name}** {req_badge}")
                st.caption(section.description)
        
        # Drafting tips & common errors
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("💡 Drafting Tips"):
                for tip in doc.drafting_tips[:5]:
                    st.success(f"✓ {tip}")
        with col2:
            with st.expander("⚠️ Common Errors"):
                for error in doc.common_errors[:5]:
                    st.error(f"✗ {error}")
        
        # Generate document prompt
        st.markdown("### 📝 Generate Document Prompt")
        doc_details = st.text_area(
            "Enter document details",
            placeholder="Provide the details needed for this document...",
            height=150,
            key="doc_input"
        )
        
        if st.button("🚀 Generate Document Prompt", type="primary", key="generate_doc"):
            if doc_details:
                prompt = generate_document_prompt(doc, doc_details)
                st.markdown("### 📋 Generated Prompt")
                render_prompt_output(prompt, f"Document: {doc.title}")
            else:
                st.warning("Please enter document details first.")

def render_workflows_tab():
    """Render the Workflows tab content - Clean Monochrome"""
    st.markdown("## Legal Workflow Pipelines")
    st.markdown("Multi-step AI-assisted workflows for complex legal matters.")
    
    # Category filter
    categories = list(set(w.category.value for w in ALL_WORKFLOWS.values()))
    selected_category = st.selectbox("Filter by Category", ["All"] + sorted(categories), key="wf_category")
    
    # Filter workflows
    workflows = ALL_WORKFLOWS
    if selected_category != "All":
        workflows = {k: v for k, v in ALL_WORKFLOWS.items() if v.category.value == selected_category}
    
    wf_names = {w.title: key for key, w in workflows.items()}
    selected_wf = st.selectbox("🔄 Select Workflow", options=[""] + sorted(list(wf_names.keys())), key="wf_select")
    
    if selected_wf and selected_wf in wf_names:
        wf_key = wf_names[selected_wf]
        workflow = ALL_WORKFLOWS[wf_key]
        
        st.markdown(f"""
        <div class="section-card">
            <h3>{workflow.title}</h3>
            <p><strong>Category:</strong> {workflow.category.value}</p>
            <p><strong>Complexity:</strong> {workflow.complexity}</p>
            <p><strong>Total Time:</strong> {workflow.total_estimated_time}</p>
            <p>{workflow.description}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Workflow steps
        st.markdown("### 📋 Workflow Steps")
        
        # Step selection slider
        current_step = st.slider(
            "Select Step",
            min_value=1,
            max_value=len(workflow.steps),
            value=1,
            key="wf_step_slider"
        )
        
        # Display steps with progress
        for i, step in enumerate(workflow.steps):
            status = "completed" if i + 1 < current_step else "active" if i + 1 == current_step else ""
            
            with st.expander(
                f"{'✅' if i + 1 < current_step else '▶️' if i + 1 == current_step else '⏳'} Step {step.step_number}: {step.title}",
                expanded=(i + 1 == current_step)
            ):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**Type:** {step.step_type.value}")
                    st.markdown(f"**Description:** {step.description}")
                    st.markdown(f"**Estimated Time:** {step.estimated_time}")
                with col2:
                    risk_value = step.risk_level.value if hasattr(step.risk_level, 'value') else str(step.risk_level)
                    st.markdown(get_risk_badge(risk_value.split()[0] if ' ' in risk_value else risk_value), unsafe_allow_html=True)
                
                if i + 1 == current_step:
                    st.markdown("---")
                    st.markdown("#### 🤖 AI Prompt for This Step")
                    
                    user_context = st.text_area(
                        "Your Context for This Step",
                        placeholder="Enter context specific to this step...",
                        key=f"wf_step_{i}_context"
                    )
                    
                    if st.button("🚀 Generate Step Prompt", key=f"gen_step_{i}"):
                        # Get base prompt and append user context
                        base_prompt = get_step_prompt(workflow, step.step_number)
                        full_prompt = base_prompt
                        if user_context:
                            full_prompt += f"\n\n---\n## Your Context\n{user_context}"
                        render_prompt_output(full_prompt, f"Workflow: {workflow.title} - Step {step.step_number}")
                
                # Human actions
                with st.expander("👤 Human Actions Required"):
                    for action in step.human_actions:
                        st.checkbox(action, key=f"action_{wf_key}_{i}_{hash(action)}")
                
                # Verification
                with st.expander("✅ Verification Required"):
                    for verification in step.verification_required:
                        st.checkbox(verification, key=f"verify_{wf_key}_{i}_{hash(verification)}")
        
        # Ethical considerations
        with st.expander("⚖️ Ethical Considerations"):
            for consideration in workflow.ethical_considerations:
                st.warning(f"⚠️ {consideration}")
        
        # Quality checkpoints
        with st.expander("✅ Quality Checkpoints"):
            for checkpoint in workflow.quality_checkpoints:
                st.success(f"✓ {checkpoint}")

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN APPLICATION
# ═══════════════════════════════════════════════════════════════════════════════

def render_onboarding():
    """Render onboarding screen for first-time users"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); border-radius: 20px; margin: 2rem 0; color: white;">
        <h1 style="margin: 0; font-size: 2.5rem;">👋 Welcome to SA Legal Prompting Elite!</h1>
        <p style="opacity: 0.8; font-size: 1.1rem; margin-top: 1rem;">The most comprehensive AI prompting platform for South African legal professionals.</p>
        <p style="opacity: 0.6; font-size: 0.9rem; margin-top: 0.5rem;">v4.4.0 Advanced AI Edition • 18 Optimization Modes • 16 Frameworks • 16 Templates</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🚀 Quick Start Guide")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="padding: 1.5rem; background: #f5f5f5; border-radius: 12px; height: 220px; color: #1a1a1a;">
            <h3 style="color: #1a1a1a;">💬 1. AI Assistant</h3>
            <p style="color: #333;">Ask for framework recommendations, court guidance, or ethics checks. Get intelligent suggestions for your legal matters.</p>
            <p style="font-size: 0.85rem; color: #555;">💡 Try: "Which mode for constitutional analysis?"</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="padding: 1.5rem; background: #f5f5f5; border-radius: 12px; height: 220px; color: #1a1a1a;">
            <h3 style="color: #1a1a1a;">🔨 2. Prompt Builder</h3>
            <p style="color: #333;">Build optimized prompts with 18 AI modes including VARI, Q*, and Micro-Optimization. Real-time quality scoring.</p>
            <p style="font-size: 0.85rem; color: #555;">⭐ New: DeepMind VARI & Q* Strategy modes</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="padding: 1.5rem; background: #f5f5f5; border-radius: 12px; height: 220px; color: #1a1a1a;">
            <h3 style="color: #1a1a1a;">📚 3. Reference Library</h3>
            <p style="color: #333;">Access 16 frameworks, specialist courts, legislation database, ethics guidelines, and document templates.</p>
            <p style="font-size: 0.85rem; color: #555;">📋 Includes: SAFLII citations, ubuntu principles</p>
        </div>
        """, unsafe_allow_html=True)
    
    # SP3 Feature Highlights
    st.markdown("---")
    st.markdown("### ⚡ New in v4.4.0 - Advanced AI Modes")
    
    mode_col1, mode_col2, mode_col3 = st.columns(3)
    with mode_col1:
        st.markdown("""
        <div style="padding: 1rem; background: #e8f4f8; border-left: 4px solid #0ea5e9; border-radius: 8px; color: #1a1a1a;">
            <strong style="color: #1a1a1a;">🧠 VARI Planning</strong><br>
            <span style="font-size: 0.85rem; color: #333;">DeepMind variational reasoning for systematic analysis</span>
        </div>
        """, unsafe_allow_html=True)
    with mode_col2:
        st.markdown("""
        <div style="padding: 1rem; background: #f0fdf4; border-left: 4px solid #22c55e; border-radius: 8px; color: #1a1a1a;">
            <strong style="color: #1a1a1a;">⭐ Q* Strategy</strong><br>
            <span style="font-size: 0.85rem; color: #333;">A* + Q-Learning for litigation pathway optimization</span>
        </div>
        """, unsafe_allow_html=True)
    with mode_col3:
        st.markdown("""
        <div style="padding: 1rem; background: #fef3c7; border-left: 4px solid #f59e0b; border-radius: 8px; color: #1a1a1a;">
            <strong style="color: #1a1a1a;">🔬 Micro-Optimization</strong><br>
            <span style="font-size: 0.85rem; color: #333;">Microsoft-style iterative prompt refinement</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        if st.button("✨ Get Started", type="primary", use_container_width=True):
            st.session_state.onboarded = True
            st.rerun()
        
        st.caption("You can always access this guide from Settings in the sidebar.")


def render_reference_tab():
    """Render consolidated Reference tab with sub-navigation"""
    st.markdown("## 📚 Legal Reference Library")
    
    # Sub-navigation using radio buttons for cleaner UX
    subtabs = ["Frameworks", "Courts", "Legislation", "Ethics", "Practice Areas", "Documents"]
    selected_subtab = st.radio(
        "Select Category",
        subtabs,
        horizontal=True,
        key="reference_subtab_radio",
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    if selected_subtab == "Frameworks":
        render_frameworks_tab()
    elif selected_subtab == "Courts":
        render_courts_tab()
    elif selected_subtab == "Legislation":
        render_legislation_tab()
    elif selected_subtab == "Ethics":
        render_ethics_tab()
    elif selected_subtab == "Practice Areas":
        render_practice_tab()
    elif selected_subtab == "Documents":
        render_documents_tab()


def main():
    """Main application entry point - v4.1 Enhanced UX Edition"""
    
    # Render sidebar
    render_sidebar()
    
    # Check for first-time users
    if not st.session_state.get('onboarded', False):
        render_header()
        render_onboarding()
        return
    
    # Render header
    render_header()
    
    # v4.1 - Consolidated tabs (5 main tabs for better UX)
    tab_home, tab_build, tab_reference, tab_workflows, tab_analytics = st.tabs([
        "🏠 Home",
        "🔨 Build", 
        "📚 Reference",
        "🔄 Workflows",
        "📊 Analytics"
    ])
    
    # HOME TAB - AI Chat Assistant + Quick Templates
    with tab_home:
        home_col1, home_col2 = st.columns([2, 1], vertical_alignment="top")
        with home_col1:
            render_ai_chat()
        with home_col2:
            st.markdown("### ⚡ Quick Templates")
            st.markdown("Click any template to generate your prompt:")
            
            # Show active prompt if loaded
            if st.session_state.get('current_prompt'):
                title = st.session_state.get('current_prompt_title', 'Template')
                st.success(f"✅ **{title}** ready!")
                st.code(st.session_state.current_prompt[:300] + "..." if len(st.session_state.current_prompt) > 300 else st.session_state.current_prompt, language=None)
                if st.button("🗑️ Clear", key="home_clear_prompt", use_container_width=True):
                    st.session_state.current_prompt = ""
                    st.session_state.current_prompt_title = ""
                    st.rerun()
                st.markdown("---")
            
            for template in QUICK_TEMPLATES[:4]:
                if st.button(f"📋 {template['title']}", key=f"home_template_{template['title'][:10]}", use_container_width=True):
                    st.session_state.current_prompt = template['prompt']
                    st.session_state.current_prompt_title = template['title']
                    add_to_history(template['prompt'], f"Template: {template['title']}")
                    st.rerun()
    
    # BUILD TAB - Smart Prompt Builder + Templates Gallery + Mode Comparison
    with tab_build:
        build_subtab = st.radio(
            "Build Mode",
            ["Smart Builder", "Template Gallery", "Mode Comparison"],
            horizontal=True,
            label_visibility="collapsed"
        )
        st.markdown("---")
        
        if build_subtab == "Smart Builder":
            render_smart_builder()
        elif build_subtab == "Template Gallery":
            render_template_gallery()
        else:
            render_mode_comparison()
    
    # REFERENCE TAB - Consolidated with sub-navigation
    with tab_reference:
        render_reference_tab()
    
    # WORKFLOWS TAB
    with tab_workflows:
        render_workflows_tab()
    
    # ANALYTICS TAB
    with tab_analytics:
        render_analytics_dashboard()
    
    # v4.0 - Keyboard shortcuts hint
    if st.session_state.preferences.get('keyboard_shortcuts', True):
        st.markdown("""
        <div class="shortcuts-hint">
            <span><span class="shortcut-key">Ctrl+K</span> Command Palette</span>
            <span><span class="shortcut-key">Ctrl+S</span> Save Prompt</span>
            <span><span class="shortcut-key">Ctrl+C</span> Copy</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer - Clean Monochrome with version info
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; padding: 2.5rem 1rem; opacity: 0.6;">
        <p style="margin: 0; font-weight: 600; font-size: 0.9rem;">SA Legal Prompting Elite Platform</p>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem;">World-Class AI Prompting for South African Legal Professionals</p>
        <p style="font-size: 0.75rem; margin-top: 0.75rem; color: #888;">
            v4.4.0 Advanced AI Edition • {len(list(OptimizationMode))} Optimization Modes • {len(ALL_FRAMEWORKS)} Frameworks
        </p>
        <p style="font-size: 0.7rem; margin-top: 0.75rem; letter-spacing: 0.05em;">
            © 2024-2026 • Built for Excellence • Made in South Africa 🇿🇦
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

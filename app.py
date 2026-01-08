"""
🇿🇦 SA LEGAL PROMPTING ELITE PLATFORM
World-Class AI Prompting Interface for South African Legal Professionals
Version 2.0 - Complete with All Modules

Run with: python -m marimo run app.py
"""

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="full")

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 1: IMPORTS AND SETUP
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __():
    import marimo as mo
    
    # Import all core modules using correct names
    from core.advanced_frameworks import (
        ALL_FRAMEWORKS, 
        get_frameworks_by_category, 
        get_frameworks_by_difficulty,
        get_framework_by_acronym,
        generate_combined_prompt,
        FrameworkCategory
    )
    from core.specialist_courts import (
        ALL_SPECIALIST_COURTS,
        get_courts_by_category,
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
        EthicsCategory,
        RiskLevel
    )
    from core.practice_area_prompts import (
        ALL_PRACTICE_PROMPTS,
        get_prompts_by_area,
        generate_practice_prompt,
        PracticeArea
    )
    from core.document_templates import (
        ALL_DOCUMENT_TEMPLATES,
        get_templates_by_category,
        generate_document_prompt,
        DocumentCategory
    )
    from core.workflow_pipelines import (
        ALL_WORKFLOWS,
        get_workflow_summary,
        get_step_prompt,
        WorkflowCategory
    )
    
    return (
        mo, 
        ALL_FRAMEWORKS, get_frameworks_by_category, get_frameworks_by_difficulty,
        get_framework_by_acronym, generate_combined_prompt, FrameworkCategory,
        ALL_SPECIALIST_COURTS, get_courts_by_category, generate_court_prompt_guidance, CourtCategory,
        ALL_LEGISLATION, generate_legislation_prompt, LegislationCategory,
        ALL_GUIDELINES, AI_USE_SCENARIOS, assess_ai_use_risk,
        generate_ethics_checklist, EthicsCategory, RiskLevel,
        ALL_PRACTICE_PROMPTS, get_prompts_by_area, generate_practice_prompt, PracticeArea,
        ALL_DOCUMENT_TEMPLATES, get_templates_by_category, generate_document_prompt, DocumentCategory,
        ALL_WORKFLOWS, get_workflow_summary, get_step_prompt, WorkflowCategory
    )

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 2: STYLING
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo):
    # SA Flag Colors
    PRIMARY_GREEN = "#007A4D"
    SECONDARY_GOLD = "#FFB612"
    ACCENT_RED = "#DE3831"
    
    style = mo.Html(f"""
    <style>
        :root {{
            --sa-green: {PRIMARY_GREEN};
            --sa-gold: {SECONDARY_GOLD};
            --sa-red: {ACCENT_RED};
        }}
        .header-banner {{
            background: linear-gradient(135deg, {PRIMARY_GREEN} 0%, #005a3a 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .header-banner h1 {{
            margin: 0;
            font-size: 2rem;
        }}
        .header-banner p {{
            margin: 0.5rem 0 0 0;
            opacity: 0.9;
        }}
        .section-card {{
            background: white;
            border-left: 4px solid {PRIMARY_GREEN};
            padding: 1rem;
            border-radius: 0 8px 8px 0;
            margin: 1rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }}
        .gold-accent {{
            border-left-color: {SECONDARY_GOLD};
        }}
        .red-accent {{
            border-left-color: {ACCENT_RED};
        }}
        .prompt-output {{
            background: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 1rem;
            font-family: 'Consolas', 'Monaco', monospace;
            white-space: pre-wrap;
            max-height: 600px;
            overflow-y: auto;
        }}
        .stats-badge {{
            background: {SECONDARY_GOLD};
            color: #333;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
            margin: 0.25rem;
        }}
        .risk-high {{ color: {ACCENT_RED}; font-weight: bold; }}
        .risk-medium {{ color: {SECONDARY_GOLD}; font-weight: bold; }}
        .risk-low {{ color: {PRIMARY_GREEN}; font-weight: bold; }}
    </style>
    """)
    
    return style, PRIMARY_GREEN, SECONDARY_GOLD, ACCENT_RED

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 3: HEADER BANNER
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, style, ALL_FRAMEWORKS, ALL_SPECIALIST_COURTS, ALL_LEGISLATION, 
       ALL_GUIDELINES, ALL_PRACTICE_PROMPTS, ALL_DOCUMENT_TEMPLATES, ALL_WORKFLOWS):
    
    total_resources = (
        len(ALL_FRAMEWORKS) + 
        len(ALL_SPECIALIST_COURTS) + 
        len(ALL_LEGISLATION) + 
        len(ALL_GUIDELINES) + 
        len(ALL_PRACTICE_PROMPTS) + 
        len(ALL_DOCUMENT_TEMPLATES) +
        len(ALL_WORKFLOWS)
    )
    
    banner = mo.Html(f"""
    {style.text}
    <div class="header-banner">
        <h1>🇿🇦 SA Legal Prompting Elite Platform</h1>
        <p>World-Class AI Prompting for Lawyers, Advocates, Judges & Magistrates</p>
        <div style="margin-top: 1rem;">
            <span class="stats-badge">{len(ALL_FRAMEWORKS)} Frameworks</span>
            <span class="stats-badge">{len(ALL_SPECIALIST_COURTS)} Courts</span>
            <span class="stats-badge">{len(ALL_LEGISLATION)} Statutes</span>
            <span class="stats-badge">{len(ALL_GUIDELINES)} Ethics Guidelines</span>
            <span class="stats-badge">{len(ALL_PRACTICE_PROMPTS)} Practice Prompts</span>
            <span class="stats-badge">{len(ALL_DOCUMENT_TEMPLATES)} Templates</span>
            <span class="stats-badge">{len(ALL_WORKFLOWS)} Workflows</span>
        </div>
    </div>
    """)
    
    return banner,

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 4: TAB 1 - FRAMEWORKS UI
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, ALL_FRAMEWORKS, FrameworkCategory):
    # Framework selector
    framework_options = {f.name: key for key, f in ALL_FRAMEWORKS.items()}
    framework_selector = mo.ui.dropdown(
        options=framework_options,
        label="🎯 Select Framework"
    )
    
    # Context input
    framework_context = mo.ui.text_area(
        label="📝 Your Legal Context",
        placeholder="Describe your legal matter or question...",
        full_width=True
    )
    
    return framework_selector, framework_context

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 5: TAB 1 - FRAMEWORKS OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, framework_selector, framework_context, ALL_FRAMEWORKS, generate_combined_prompt):
    
    framework_output = mo.md("*Select a framework and enter context to generate a prompt.*")
    
    if framework_selector.value and framework_context.value:
        _framework = ALL_FRAMEWORKS.get(framework_selector.value)
        if _framework:
            _fw_prompt = generate_combined_prompt(_framework, framework_context.value)
            
            framework_output = mo.Html(f"""
            <div class="section-card">
                <h3>🎯 {_framework.name}</h3>
                <p><strong>Category:</strong> {_framework.category.value}</p>
                <p><strong>Difficulty:</strong> {_framework.difficulty}</p>
                <p><em>{_framework.description}</em></p>
            </div>
            <div class="prompt-output">{_fw_prompt}</div>
            """)
    
    return framework_output,

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 6: TAB 2 - COURTS UI
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, ALL_SPECIALIST_COURTS, CourtCategory):
    # Court selector
    court_options = {f"{c.name} ({c.saflii_code})": key for key, c in ALL_SPECIALIST_COURTS.items()}
    court_selector = mo.ui.dropdown(
        options=court_options,
        label="🏛️ Select Court"
    )
    
    return court_selector,

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 7: TAB 2 - COURTS OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, court_selector, ALL_SPECIALIST_COURTS, generate_court_prompt_guidance):
    
    court_output = mo.md("*Select a court to view details.*")
    
    if court_selector.value:
        _court = ALL_SPECIALIST_COURTS.get(court_selector.value)
        if _court:
            _court_prompt = generate_court_prompt_guidance(_court)
            
            court_output = mo.Html(f"""
            <div class="section-card gold-accent">
                <h3>🏛️ {_court.name}</h3>
                <p><strong>SAFLII Code:</strong> {_court.saflii_code}</p>
                <p><strong>Establishing Legislation:</strong> {_court.establishing_legislation}</p>
                <p><strong>Appeal Route:</strong> {_court.appeal_route}</p>
            </div>
            <div class="prompt-output">{_court_prompt}</div>
            """)
    
    return court_output,

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 8: TAB 3 - LEGISLATION UI
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, ALL_LEGISLATION):
    # Legislation selector
    legislation_options = {
        f"{leg.short_title} ({leg.act_number})": key 
        for key, leg in ALL_LEGISLATION.items()
    }
    legislation_selector = mo.ui.dropdown(
        options=legislation_options,
        label="📜 Select Legislation"
    )
    
    # Question input
    legislation_question = mo.ui.text_area(
        label="❓ Your Question",
        placeholder="What do you want to know about this legislation?",
        full_width=True
    )
    
    return legislation_selector, legislation_question

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 9: TAB 3 - LEGISLATION OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, legislation_selector, legislation_question, ALL_LEGISLATION, generate_legislation_prompt):
    
    legislation_output = mo.md("*Select legislation to view details.*")
    
    if legislation_selector.value:
        _leg = ALL_LEGISLATION.get(legislation_selector.value)
        if _leg:
            _provisions_html = "".join(
                f"<li><strong>{prov.section}:</strong> {prov.title}</li>"
                for prov in _leg.key_provisions[:5]
            )
            
            _leg_prompt = ""
            if legislation_question.value:
                _leg_prompt = generate_legislation_prompt(_leg, legislation_question.value)
            
            legislation_output = mo.Html(f"""
            <div class="section-card">
                <h3>📜 {_leg.full_title}</h3>
                <p><strong>Citation:</strong> {_leg.act_number}</p>
                <p><strong>Purpose:</strong> {_leg.purpose}</p>
                <h4>Key Provisions (first 5):</h4>
                <ul>{_provisions_html}</ul>
            </div>
            """ + (f'<div class="prompt-output">{_leg_prompt}</div>' if _leg_prompt else ""))
    
    return legislation_output,

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 10: TAB 4 - ETHICS UI
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, ALL_GUIDELINES, AI_USE_SCENARIOS):
    # Guideline selector
    guideline_options = {g.title: key for key, g in ALL_GUIDELINES.items()}
    guideline_selector = mo.ui.dropdown(
        options=guideline_options,
        label="⚖️ Ethical Guideline"
    )
    
    # Scenario selector - AI_USE_SCENARIOS is a list
    scenario_options = {s.scenario: idx for idx, s in enumerate(AI_USE_SCENARIOS)}
    scenario_selector = mo.ui.dropdown(
        options=scenario_options,
        label="🤖 AI Use Scenario"
    )
    
    return guideline_selector, scenario_selector

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 11: TAB 4 - ETHICS OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, guideline_selector, scenario_selector, ALL_GUIDELINES, AI_USE_SCENARIOS):
    
    _ethics_parts = []
    
    if guideline_selector.value:
        _guideline = ALL_GUIDELINES.get(guideline_selector.value)
        if _guideline:
            _ethics_parts.append(mo.Html(f"""
            <div class="section-card red-accent">
                <h3>⚖️ {_guideline.title}</h3>
                <p><strong>Category:</strong> {_guideline.category.value}</p>
                <p><strong>LPC Rule:</strong> {_guideline.lpc_rule_reference}</p>
                <h4>Requirements:</h4>
                <ul>{''.join(f'<li>{req}</li>' for req in _guideline.requirements[:5])}</ul>
            </div>
            """))
    
    if scenario_selector.value is not None:
        _scenario = AI_USE_SCENARIOS[scenario_selector.value]
        _ethics_parts.append(mo.Html(f"""
        <div class="section-card gold-accent">
            <h3>🤖 {_scenario.scenario}</h3>
            <p><strong>Risk Level:</strong> {_scenario.risk_level.value}</p>
            <p><em>{_scenario.recommended_approach}</em></p>
            <h4>Safeguards Required:</h4>
            <ul>{''.join(f'<li>🛡️ {sf}</li>' for sf in _scenario.safeguards_required)}</ul>
        </div>
        """))
    
    ethics_output = mo.vstack(_ethics_parts) if _ethics_parts else mo.md("*Select a guideline or scenario.*")
    
    return ethics_output,

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 12: TAB 5 - PRACTICE AREA UI
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, ALL_PRACTICE_PROMPTS):
    # Practice area selector
    practice_options = {p.title: key for key, p in ALL_PRACTICE_PROMPTS.items()}
    practice_selector = mo.ui.dropdown(
        options=practice_options,
        label="📋 Practice Area Prompt"
    )
    
    # Context input
    practice_context = mo.ui.text_area(
        label="📝 Matter Details",
        placeholder="Describe your specific legal matter (anonymised)...",
        full_width=True
    )
    
    return practice_selector, practice_context

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 13: TAB 5 - PRACTICE AREA OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, practice_selector, practice_context, ALL_PRACTICE_PROMPTS, generate_practice_prompt):
    
    practice_output = mo.md("*Select a practice area prompt.*")
    
    if practice_selector.value:
        _prac_template = ALL_PRACTICE_PROMPTS.get(practice_selector.value)
        if _prac_template:
            _prac_prompt = _prac_template.template
            if practice_context.value:
                _prac_prompt = generate_practice_prompt(_prac_template, practice_context.value)
            
            practice_output = mo.Html(f"""
            <div class="section-card">
                <h3>📋 {_prac_template.title}</h3>
                <p><strong>Practice Area:</strong> {_prac_template.practice_area.value}</p>
                <p><em>{_prac_template.description}</em></p>
            </div>
            <div class="prompt-output">{_prac_prompt}</div>
            """)
    
    return practice_output,

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 14: TAB 6 - DOCUMENT TEMPLATES UI
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, ALL_DOCUMENT_TEMPLATES):
    # Template selector
    template_options = {t.title: key for key, t in ALL_DOCUMENT_TEMPLATES.items()}
    template_selector = mo.ui.dropdown(
        options=template_options,
        label="📄 Document Template"
    )
    
    # Context input
    template_context = mo.ui.text_area(
        label="📝 Document Context",
        placeholder="Provide details for the document...",
        full_width=True
    )
    
    return template_selector, template_context

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 15: TAB 6 - DOCUMENT TEMPLATES OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, template_selector, template_context, ALL_DOCUMENT_TEMPLATES, generate_document_prompt):
    
    document_output = mo.md("*Select a document template.*")
    
    if template_selector.value:
        _doc_template = ALL_DOCUMENT_TEMPLATES.get(template_selector.value)
        if _doc_template:
            _doc_prompt = _doc_template.prompt_template
            if template_context.value:
                _doc_prompt = generate_document_prompt(_doc_template, template_context.value)
            
            document_output = mo.Html(f"""
            <div class="section-card gold-accent">
                <h3>📄 {_doc_template.title}</h3>
                <p><strong>Category:</strong> {_doc_template.category.value}</p>
                <p><strong>Estimated Time:</strong> {_doc_template.time_estimate}</p>
                <p><em>{_doc_template.description}</em></p>
            </div>
            <div class="prompt-output">{_doc_prompt}</div>
            """)
    
    return document_output,

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 16: TAB 7 - WORKFLOWS UI
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, ALL_WORKFLOWS):
    # Workflow selector
    workflow_options = {w.title: key for key, w in ALL_WORKFLOWS.items()}
    workflow_selector = mo.ui.dropdown(
        options=workflow_options,
        label="🔄 Legal Workflow"
    )
    
    # Step selector
    step_selector = mo.ui.slider(
        start=1,
        stop=6,
        value=1,
        label="📍 Workflow Step"
    )
    
    return workflow_selector, step_selector

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 17: TAB 7 - WORKFLOWS OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, workflow_selector, step_selector, ALL_WORKFLOWS, get_workflow_summary, get_step_prompt):
    
    workflow_output = mo.md("*Select a workflow.*")
    
    if workflow_selector.value:
        _workflow = ALL_WORKFLOWS.get(workflow_selector.value)
        if _workflow:
            _max_step = len(_workflow.steps)
            _current_step = min(step_selector.value, _max_step)
            
            _wf_step_prompt = get_step_prompt(_workflow, _current_step)
            
            _steps_overview = "".join(
                f"<li><strong>Step {s.step_number}: {s.title}</strong> ({s.estimated_time})</li>"
                for s in _workflow.steps
            )
            
            workflow_output = mo.Html(f"""
            <div class="section-card">
                <h3>🔄 {_workflow.title}</h3>
                <p><strong>Category:</strong> {_workflow.category.value}</p>
                <p><strong>Complexity:</strong> {_workflow.complexity}</p>
                <p><strong>Total Time:</strong> {_workflow.total_estimated_time}</p>
                <h4>Workflow Steps:</h4>
                <ol>{_steps_overview}</ol>
            </div>
            <h3>Step {_current_step} Prompt:</h3>
            <div class="prompt-output">{_wf_step_prompt}</div>
            """)
    
    return workflow_output,

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 18: MAIN TAB INTERFACE
# ═══════════════════════════════════════════════════════════════════════════════

@app.cell
def __(mo, banner, 
       framework_selector, framework_context, framework_output,
       court_selector, court_output,
       legislation_selector, legislation_question, legislation_output,
       guideline_selector, scenario_selector, ethics_output,
       practice_selector, practice_context, practice_output,
       template_selector, template_context, document_output,
       workflow_selector, step_selector, workflow_output):
    
    # Create tabs
    tabs = mo.ui.tabs({
        "🎯 Frameworks": mo.vstack([
            mo.md("### Select a Prompting Framework"),
            framework_selector,
            framework_context,
            framework_output
        ]),
        "🏛️ Courts": mo.vstack([
            mo.md("### Explore SA Specialist Courts & Tribunals"),
            court_selector,
            court_output
        ]),
        "📜 Legislation": mo.vstack([
            mo.md("### SA Key Legislation Reference"),
            legislation_selector,
            legislation_question,
            legislation_output
        ]),
        "⚖️ Ethics": mo.vstack([
            mo.md("### AI Ethics & Risk Assessment for Legal Practice"),
            mo.hstack([guideline_selector, scenario_selector]),
            ethics_output
        ]),
        "📋 Practice": mo.vstack([
            mo.md("### Practice Area Specific Prompts"),
            practice_selector,
            practice_context,
            practice_output
        ]),
        "📄 Documents": mo.vstack([
            mo.md("### Legal Document Drafting Templates"),
            template_selector,
            template_context,
            document_output
        ]),
        "🔄 Workflows": mo.vstack([
            mo.md("### Multi-Step Legal Workflow Pipelines"),
            workflow_selector,
            step_selector,
            workflow_output
        ])
    })
    
    return mo.vstack([banner, tabs])

# ═══════════════════════════════════════════════════════════════════════════════
# CELL 19: APP EXECUTION
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    app.run()

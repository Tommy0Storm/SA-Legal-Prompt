"""
🇿🇦 SA Legal Prompting Core Modules
Complete suite for world-class legal AI prompting in South Africa
"""

from .advanced_frameworks import (
    ALL_FRAMEWORKS,
    get_frameworks_by_category,
    get_frameworks_by_difficulty,
    get_framework_by_acronym as recommend_framework,
    generate_combined_prompt,
    FrameworkCategory,
    PromptingFramework
)

from .specialist_courts import (
    ALL_SPECIALIST_COURTS as ALL_COURTS,
    get_courts_by_category,
    generate_court_prompt_guidance as generate_court_prompt,
    CourtCategory,
    JurisdictionType,
    SpecialistCourt
)

from .sa_legislation import (
    ALL_LEGISLATION,
    generate_legislation_prompt,
    LegislationCategory,
    KeyProvision,
    SALegislation
)

from .legal_ethics import (
    ALL_GUIDELINES as ALL_ETHICAL_GUIDELINES,
    AI_USE_SCENARIOS as ALL_AI_USE_SCENARIOS,
    assess_ai_use_risk,
    generate_ethics_checklist,
    EthicsCategory,
    RiskLevel,
    EthicalGuideline,
    AIUseScenario
)

from .practice_area_prompts import (
    ALL_PRACTICE_PROMPTS,
    get_prompts_by_area,
    get_prompts_by_type,
    generate_practice_prompt,
    PracticeArea,
    PromptType,
    PracticeAreaPrompt
)

from .document_templates import (
    ALL_DOCUMENT_TEMPLATES,
    get_templates_by_category,
    get_template_structure,
    generate_document_prompt,
    DocumentCategory,
    Court,
    DocumentSection,
    DocumentTemplate
)

from .workflow_pipelines import (
    ALL_WORKFLOWS,
    get_workflows_by_category,
    get_workflow_summary,
    get_step_prompt,
    WorkflowCategory,
    StepType,
    WorkflowStep,
    LegalWorkflow
)

from .prompt_optimizer import (
    OptimizationMode,
    LegalOutputFormat,
    PracticeAreaPreset,
    OptimizedPrompt,
    PresetConfiguration,
    optimize_legal_prompt,
    optimize_with_preset,
    optimize_with_crispe,
    optimize_with_co_star,
    optimize_with_chain_of_thought,
    optimize_with_rise,
    optimize_with_o1_style,
    optimize_with_meta_prompt,
    optimize_with_hybrid_legal,
    optimize_with_claude_style,
    # SP2 New Optimizers
    optimize_with_expert_witness,
    optimize_with_mediation_adr,
    optimize_with_compliance_audit,
    # SP2 New Features
    PromptComparison,
    BatchResult,
    QualityScoreDetails,
    QuickTemplate,
    compare_optimization_modes,
    batch_optimize_prompts,
    export_prompt_to_json,
    export_prompt_to_markdown,
    calculate_detailed_quality_score,
    get_quick_templates,
    get_template_by_name,
    get_templates_by_category,
    # Utilities
    get_optimization_modes_for_ui,
    get_presets_for_ui,
    get_preset_configuration,
    detect_practice_area,
    calculate_prompt_quality_score,
    estimate_token_count
)

__all__ = [
    # Frameworks
    "ALL_FRAMEWORKS", "get_frameworks_by_category", "get_frameworks_by_difficulty",
    "recommend_framework", "generate_combined_prompt", "FrameworkCategory", 
    "PromptingFramework",
    
    # Courts
    "ALL_COURTS", "get_courts_by_category", "generate_court_prompt",
    "CourtCategory", "JurisdictionType", "SpecialistCourt",
    
    # Legislation
    "ALL_LEGISLATION", "generate_legislation_prompt", "LegislationCategory",
    "KeyProvision", "SALegislation",
    
    # Ethics
    "ALL_ETHICAL_GUIDELINES", "ALL_AI_USE_SCENARIOS", "assess_ai_use_risk",
    "generate_ethics_checklist", "EthicsCategory", "RiskLevel",
    "EthicalGuideline", "AIUseScenario",
    
    # Practice Areas
    "ALL_PRACTICE_PROMPTS", "get_prompts_by_area", "get_prompts_by_type",
    "generate_practice_prompt", "PracticeArea", "PromptType", "PracticeAreaPrompt",
    
    # Documents
    "ALL_DOCUMENT_TEMPLATES", "get_templates_by_category", "get_template_structure",
    "generate_document_prompt", "DocumentCategory", "Court", "DocumentSection",
    "DocumentTemplate",
    
    # Workflows
    "ALL_WORKFLOWS", "get_workflows_by_category", "get_workflow_summary",
    "get_step_prompt", "WorkflowCategory", "StepType", "WorkflowStep", "LegalWorkflow",
    
    # Prompt Optimizer (Enhanced AI Optimization) - SP2 Update
    "OptimizationMode", "LegalOutputFormat", "PracticeAreaPreset",
    "OptimizedPrompt", "PresetConfiguration",
    "optimize_legal_prompt", "optimize_with_preset",
    "optimize_with_crispe", "optimize_with_co_star",
    "optimize_with_chain_of_thought", "optimize_with_rise", "optimize_with_o1_style",
    "optimize_with_meta_prompt", "optimize_with_hybrid_legal", "optimize_with_claude_style",
    # SP2 New Exports
    "optimize_with_expert_witness", "optimize_with_mediation_adr", "optimize_with_compliance_audit",
    "PromptComparison", "BatchResult", "QualityScoreDetails", "QuickTemplate",
    "compare_optimization_modes", "batch_optimize_prompts",
    "export_prompt_to_json", "export_prompt_to_markdown",
    "calculate_detailed_quality_score", "get_quick_templates", "get_template_by_name",
    "get_templates_by_category",
    "get_optimization_modes_for_ui", "get_presets_for_ui", "get_preset_configuration",
    "detect_practice_area", "calculate_prompt_quality_score", "estimate_token_count"
]

__version__ = "4.2.0"
__author__ = "SA Legal Prompting Team"

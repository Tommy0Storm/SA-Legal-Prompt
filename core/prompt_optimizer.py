"""
🇿🇦 SA Legal Prompt Optimization Engine v3.0
Advanced prompt enhancement techniques adapted for South African legal practice.
Incorporates industry-leading optimization patterns: CRISPE, CO-STAR, Chain of Thought, 
RISE (Recursive Introspection), O1-Style structured reasoning, and Hybrid modes.

Service Pack 1 Features:
- Quick Presets for common SA legal tasks
- Hybrid optimization mode
- Practice area auto-detection
- Claude-style task instructions
- Prompt quality scoring

Service Pack 2 Features:
- Expert Witness optimization mode
- Mediation/ADR optimization mode
- Compliance Audit optimization mode
- Prompt comparison (multi-mode)
- Batch optimization
- Export formats (JSON, Markdown)
- Enhanced quality scoring with sub-scores
- Quick prompt templates
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Tuple
import datetime
import json


class OptimizationMode(Enum):
    """Prompt optimization modes available"""
    STANDARD = "Standard (No Enhancement)"
    CRISPE = "CRISPE (Role + Profile + Goals)"
    CO_STAR = "CO-STAR (Context + Objective + Style)"
    CHAIN_OF_THOUGHT = "Chain of Thought Legal"
    RISE = "RISE (Recursive Introspection)"
    O1_STYLE = "O1-Style (Structured Reasoning)"
    META_PROMPT = "Meta Prompt (Structure Optimization)"
    HYBRID_LEGAL = "Hybrid Legal (CRISPE + CoT)"
    CLAUDE_STYLE = "Claude-Style (Task Instructions)"
    # SP2 New Modes
    EXPERT_WITNESS = "Expert Witness (Technical Opinion)"
    MEDIATION_ADR = "Mediation/ADR (Dispute Resolution)"
    COMPLIANCE_AUDIT = "Compliance Audit (Regulatory Review)"
    # SP3 New Modes (from 302 Prompt Expert)
    VARI_PLANNING = "VARI (Variational Planning)"
    Q_STAR = "Q* (Optimal Path Search)"
    MICRO_OPT = "Microsoft MicrOptimization"
    OPENAI_OFFICIAL = "OpenAI Official Method"
    SPO_SELF_PLAY = "SPO (Self-Play Optimization)"
    GUIDED_COMPLETE = "Guided Step-by-Step"


class LegalOutputFormat(Enum):
    """SA Legal output format types"""
    LEGAL_OPINION = "Formal Legal Opinion"
    HEADS_OF_ARGUMENT = "Heads of Argument"
    ADVICE_LETTER = "Client Advice Letter"
    CASE_ANALYSIS = "Case Analysis Memorandum"
    CONTRACT_REVIEW = "Contract Review Summary"
    RESEARCH_MEMO = "Legal Research Memorandum"
    PLEADING = "Draft Pleading"
    BRIEF = "Counsel Brief"


class PracticeAreaPreset(Enum):
    """Quick presets for SA legal practice areas"""
    CONSTITUTIONAL = "Constitutional Law"
    CRIMINAL = "Criminal Law"
    LABOUR = "Labour & Employment"
    COMMERCIAL = "Commercial & Corporate"
    LITIGATION = "Civil Litigation"
    FAMILY = "Family Law"
    PROPERTY = "Property & Conveyancing"
    ADMINISTRATIVE = "Administrative Law"
    CUSTOM = "Custom Configuration"


@dataclass
class OptimizedPrompt:
    """Container for an optimized prompt with metadata"""
    original: str
    optimized: str
    mode: OptimizationMode
    enhancement_notes: List[str]
    sa_legal_adaptations: List[str]
    reasoning_structure: Optional[str] = None
    quality_score: float = 0.0
    practice_area: Optional[str] = None
    token_estimate: int = 0


@dataclass
class PresetConfiguration:
    """Configuration for a practice area preset"""
    name: str
    practice_area: PracticeAreaPreset
    recommended_mode: OptimizationMode
    recommended_format: LegalOutputFormat
    key_legislation: List[str]
    key_cases: List[str]
    special_considerations: List[str]
    role_template: str
    context_hints: List[str]


# ═══════════════════════════════════════════════════════════════════════════════
# QUICK PRESETS FOR SA LEGAL PRACTICE AREAS
# ═══════════════════════════════════════════════════════════════════════════════

PRACTICE_PRESETS: Dict[PracticeAreaPreset, PresetConfiguration] = {
    PracticeAreaPreset.CONSTITUTIONAL: PresetConfiguration(
        name="Constitutional Law",
        practice_area=PracticeAreaPreset.CONSTITUTIONAL,
        recommended_mode=OptimizationMode.CHAIN_OF_THOUGHT,
        recommended_format=LegalOutputFormat.HEADS_OF_ARGUMENT,
        key_legislation=[
            "Constitution of the Republic of South Africa, 1996",
            "Promotion of Administrative Justice Act 3 of 2000",
            "Promotion of Equality and Prevention of Unfair Discrimination Act 4 of 2000"
        ],
        key_cases=[
            "Harksen v Lane NO 1998 (1) SA 300 (CC)",
            "Minister of Home Affairs v Fourie 2006 (1) SA 524 (CC)",
            "S v Makwanyane 1995 (3) SA 391 (CC)",
            "Carmichele v Minister of Safety and Security 2001 (4) SA 938 (CC)"
        ],
        special_considerations=[
            "Apply transformative constitutionalism lens",
            "Consider ubuntu principle in interpretation",
            "Apply s36 limitations analysis for rights matters",
            "Reference Constitutional Court methodology"
        ],
        role_template="You are a Senior Constitutional Law Specialist with extensive experience before the Constitutional Court of South Africa, well-versed in transformative constitutionalism and the founding values of human dignity, equality, and freedom.",
        context_hints=["rights analysis", "equality", "section 9", "bill of rights", "constitutional values"]
    ),
    
    PracticeAreaPreset.CRIMINAL: PresetConfiguration(
        name="Criminal Law",
        practice_area=PracticeAreaPreset.CRIMINAL,
        recommended_mode=OptimizationMode.CHAIN_OF_THOUGHT,
        recommended_format=LegalOutputFormat.LEGAL_OPINION,
        key_legislation=[
            "Criminal Procedure Act 51 of 1977",
            "Criminal Law Amendment Act 105 of 1997",
            "Prevention of Organised Crime Act 121 of 1998",
            "Child Justice Act 75 of 2008"
        ],
        key_cases=[
            "S v Zuma 1995 (2) SA 642 (CC)",
            "S v Makwanyane 1995 (3) SA 391 (CC)",
            "S v Thebus 2003 (6) SA 505 (CC)",
            "S v Dodo 2001 (3) SA 382 (CC)"
        ],
        special_considerations=[
            "Presume innocence - burden on State",
            "Apply beyond reasonable doubt standard",
            "Consider fair trial rights (s35)",
            "Analyse elements of offence systematically"
        ],
        role_template="You are an experienced Criminal Law Advocate with extensive trial and appellate court experience, specializing in constitutional criminal procedure and the protection of accused persons' rights.",
        context_hints=["accused", "prosecution", "bail", "sentence", "appeal", "conviction", "acquittal"]
    ),
    
    PracticeAreaPreset.LABOUR: PresetConfiguration(
        name="Labour & Employment",
        practice_area=PracticeAreaPreset.LABOUR,
        recommended_mode=OptimizationMode.CRISPE,
        recommended_format=LegalOutputFormat.ADVICE_LETTER,
        key_legislation=[
            "Labour Relations Act 66 of 1995",
            "Basic Conditions of Employment Act 75 of 1997",
            "Employment Equity Act 55 of 1998",
            "Occupational Health and Safety Act 85 of 1993"
        ],
        key_cases=[
            "Sidumo v Rustenburg Platinum Mines 2007 (12) BLLR 1097 (CC)",
            "NUMSA v Bader Bop 2003 (2) BLLR 103 (CC)",
            "NEHAWU v UCT 2003 (3) SA 1 (CC)",
            "Kroeger v Visual Marketing 2003 (9) BLLR 901 (LC)"
        ],
        special_considerations=[
            "Apply substantive and procedural fairness test",
            "Consider CCMA jurisdiction and procedures",
            "Analyse automatically unfair dismissal grounds (s187)",
            "Apply commissioner's discretion principles"
        ],
        role_template="You are a Labour Law Specialist with extensive CCMA arbitration and Labour Court experience, well-versed in collective bargaining, dismissal law, and employment equity.",
        context_hints=["dismissal", "unfair", "ccma", "retrenchment", "strike", "bargaining", "equity"]
    ),
    
    PracticeAreaPreset.COMMERCIAL: PresetConfiguration(
        name="Commercial & Corporate",
        practice_area=PracticeAreaPreset.COMMERCIAL,
        recommended_mode=OptimizationMode.CO_STAR,
        recommended_format=LegalOutputFormat.CONTRACT_REVIEW,
        key_legislation=[
            "Companies Act 71 of 2008",
            "Consumer Protection Act 68 of 2008",
            "Competition Act 89 of 1998",
            "National Credit Act 34 of 2005"
        ],
        key_cases=[
            "Bothma-Batho Transport v S Bothma & Seun Transport 2014 (2) SA 494 (SCA)",
            "Bredenkamp v Standard Bank of SA 2010 (4) SA 468 (SCA)",
            "Natal Joint Municipal Pension Fund v Endumeni Municipality 2012 (4) SA 593 (SCA)",
            "Novartis v Maphil Trading 2016 (1) SA 518 (SCA)"
        ],
        special_considerations=[
            "Apply purposive interpretation of contracts",
            "Consider good faith and ubuntu in commercial dealings",
            "Analyse director duties (s76-77 Companies Act)",
            "Consider consumer protection implications"
        ],
        role_template="You are a Senior Commercial Attorney with expertise in corporate transactions, contract law, and regulatory compliance, experienced in advising JSE-listed companies and multinational corporations.",
        context_hints=["contract", "company", "director", "shareholder", "merger", "acquisition", "compliance"]
    ),
    
    PracticeAreaPreset.LITIGATION: PresetConfiguration(
        name="Civil Litigation",
        practice_area=PracticeAreaPreset.LITIGATION,
        recommended_mode=OptimizationMode.HYBRID_LEGAL,
        recommended_format=LegalOutputFormat.HEADS_OF_ARGUMENT,
        key_legislation=[
            "Superior Courts Act 10 of 2013",
            "Magistrates' Courts Act 32 of 1944",
            "Prescription Act 68 of 1969",
            "Uniform Rules of Court"
        ],
        key_cases=[
            "Makate v Vodacom 2016 (4) SA 121 (CC)",
            "MV Stella Tingas 2003 (2) SA 473 (SCA)",
            "Trencon Construction v Industrial Development Corporation 2015 (5) SA 245 (CC)",
            "Cool Ideas 1186 CC v Hubbard 2014 (4) SA 474 (CC)"
        ],
        special_considerations=[
            "Apply proper rules of procedure",
            "Consider prescription and limitation periods",
            "Analyse costs implications",
            "Apply precedent hierarchy correctly"
        ],
        role_template="You are an experienced Litigation Counsel with expertise in civil procedure, evidence, and appellate practice across the South African court hierarchy.",
        context_hints=["court", "pleading", "evidence", "appeal", "interdict", "judgment", "costs"]
    ),
    
    PracticeAreaPreset.FAMILY: PresetConfiguration(
        name="Family Law",
        practice_area=PracticeAreaPreset.FAMILY,
        recommended_mode=OptimizationMode.CO_STAR,
        recommended_format=LegalOutputFormat.ADVICE_LETTER,
        key_legislation=[
            "Divorce Act 70 of 1979",
            "Children's Act 38 of 2005",
            "Maintenance Act 99 of 1998",
            "Matrimonial Property Act 88 of 1984"
        ],
        key_cases=[
            "McCall v McCall 1994 (3) SA 201 (C)",
            "Van Deijl v Van Deijl 1966 (4) SA 260 (R)",
            "Sonderup v Tondelli 2001 (1) SA 1171 (CC)",
            "Centre for Child Law v Minister of Justice 2009 (2) SACR 477 (CC)"
        ],
        special_considerations=[
            "Apply best interests of child standard",
            "Consider parental responsibilities and rights",
            "Analyse maintenance obligations",
            "Apply sensitive language for family matters"
        ],
        role_template="You are a Family Law Practitioner with expertise in divorce, children's rights, and matrimonial property, committed to protecting the best interests of children while advocating for your client.",
        context_hints=["divorce", "custody", "maintenance", "children", "marriage", "parenting"]
    ),
    
    PracticeAreaPreset.PROPERTY: PresetConfiguration(
        name="Property & Conveyancing",
        practice_area=PracticeAreaPreset.PROPERTY,
        recommended_mode=OptimizationMode.CRISPE,
        recommended_format=LegalOutputFormat.LEGAL_OPINION,
        key_legislation=[
            "Deeds Registries Act 47 of 1937",
            "Sectional Titles Act 95 of 1986",
            "Land Reform (Labour Tenants) Act 3 of 1996",
            "Extension of Security of Tenure Act 62 of 1997"
        ],
        key_cases=[
            "Daniels v Scribante 2017 (4) SA 341 (CC)",
            "Port Elizabeth Municipality v Various Occupiers 2005 (1) SA 217 (CC)",
            "First National Bank v Britz 2011 (4) SA 496 (SCA)",
            "Saunderson v Gillingham 2011 (2) SA 488 (SCA)"
        ],
        special_considerations=[
            "Consider s25 property rights",
            "Apply eviction procedures correctly",
            "Analyse security of tenure protections",
            "Consider land reform implications"
        ],
        role_template="You are a Property Law Specialist and Conveyancer with expertise in real property transactions, sectional title, and land reform, experienced in both commercial and residential matters.",
        context_hints=["property", "land", "eviction", "transfer", "bond", "sectional title", "tenant"]
    ),
    
    PracticeAreaPreset.ADMINISTRATIVE: PresetConfiguration(
        name="Administrative Law",
        practice_area=PracticeAreaPreset.ADMINISTRATIVE,
        recommended_mode=OptimizationMode.CHAIN_OF_THOUGHT,
        recommended_format=LegalOutputFormat.HEADS_OF_ARGUMENT,
        key_legislation=[
            "Promotion of Administrative Justice Act 3 of 2000 (PAJA)",
            "Constitution s33 (Just Administrative Action)",
            "Promotion of Access to Information Act 2 of 2000 (PAIA)",
            "National Environmental Management Act 107 of 1998"
        ],
        key_cases=[
            "Bato Star Fishing v Minister of Environmental Affairs 2004 (4) SA 490 (CC)",
            "Pharmaceutical Manufacturers Association v Sarcophen 2000 (2) SA 674 (CC)",
            "Albutt v Centre for the Study of Violence 2010 (3) SA 293 (CC)",
            "MEC Health, Eastern Cape v Kirland Investments 2014 (3) SA 481 (CC)"
        ],
        special_considerations=[
            "Apply PAJA requirements systematically",
            "Analyse reasonableness and rationality",
            "Consider procedural fairness requirements",
            "Apply legality review for non-PAJA matters"
        ],
        role_template="You are an Administrative Law Specialist with expertise in judicial review, PAJA applications, and public law, experienced in holding government accountable through the courts.",
        context_hints=["administrative", "paja", "review", "decision", "government", "minister", "regulation"]
    )
}


def get_preset_configuration(preset: PracticeAreaPreset) -> PresetConfiguration:
    """Get the configuration for a practice area preset"""
    return PRACTICE_PRESETS.get(preset, PRACTICE_PRESETS[PracticeAreaPreset.LITIGATION])


def detect_practice_area(context: str) -> Tuple[PracticeAreaPreset, float]:
    """
    Auto-detect practice area from context text.
    Returns (detected_preset, confidence_score)
    """
    context_lower = context.lower()
    scores: Dict[PracticeAreaPreset, float] = {}
    
    for preset, config in PRACTICE_PRESETS.items():
        score = 0.0
        # Check for hint words
        for hint in config.context_hints:
            if hint in context_lower:
                score += 0.15
        
        # Check for legislation mentions
        for leg in config.key_legislation:
            if any(word.lower() in context_lower for word in leg.split()[:3]):
                score += 0.1
        
        # Check for case mentions
        for case in config.key_cases:
            case_name = case.split()[0].lower()
            if case_name in context_lower:
                score += 0.2
        
        scores[preset] = min(score, 1.0)
    
    if not scores:
        return PracticeAreaPreset.CUSTOM, 0.0
    
    best_preset = max(scores.keys(), key=lambda k: scores[k])
    return best_preset, scores[best_preset]


# ═══════════════════════════════════════════════════════════════════════════════
# CRISPE LEGAL OPTIMIZER
# Adapted from 302_prompt_expert for SA Legal Practice
# ═══════════════════════════════════════════════════════════════════════════════

CRISPE_LEGAL_TEMPLATE = """<system_context>
You are an expert SA Legal Professional with comprehensive knowledge of South African jurisprudence.

<role>
{role}
</role>

<profile>
- **Expertise**: {expertise}
- **Jurisdiction Focus**: South African courts (Constitutional Court, SCA, High Courts, Magistrates' Courts)
- **Legal Framework Familiarity**: SA Constitution, common law, customary law, statutory interpretation
- **Citation Standard**: SAFLII neutral citation format
</profile>

<goals>
{goals}
</goals>

<skills>
- Constitutional interpretation using transformative constitutionalism principles
- Statutory interpretation (Golden Rule, Mischief Rule, Purposive Interpretation)
- Ubuntu-infused legal reasoning
- Common law precedent analysis
- SA legal citation and referencing
- Bilingual legal terminology (English/Afrikaans)
</skills>

<constraints>
- Only cite SA case law with proper SAFLII neutral citations
- Reference Acts by full title with number and year (e.g., "Constitution of the Republic of South Africa, 1996")
- Apply limitations analysis under s36 for rights-based matters
- Consider appeal routes and court hierarchy
- Maintain professional legal ethics per LPC/Cape Law Society guidelines
{additional_constraints}
</constraints>

<output_format>
{output_format}
</output_format>

<workflow>
1. Carefully analyze the matter presented
2. Identify applicable legal principles and precedents
3. Apply SA-specific legal frameworks
4. Structure response according to specified format
5. Provide reasoned conclusions with supporting authorities
</workflow>
</system_context>

<instruction>
{task}
</instruction>

<context>
{context}
</context>"""


def optimize_with_crispe(
    role: str,
    task: str,
    context: str,
    expertise: str = "General SA Legal Practice",
    goals: str = "Provide accurate, well-reasoned legal analysis",
    output_format: str = "Structured legal analysis with cited authorities",
    additional_constraints: str = ""
) -> OptimizedPrompt:
    """
    Apply CRISPE optimization framework for SA legal prompts.
    
    CRISPE = Capacity/Role, Insight/Profile, Statement/Goals, 
             Skills, Personality (adapted as Constraints), 
             Experiment/Output Format
    """
    optimized = CRISPE_LEGAL_TEMPLATE.format(
        role=role,
        expertise=expertise,
        goals=goals,
        additional_constraints=additional_constraints,
        output_format=output_format,
        task=task,
        context=context
    )
    
    return OptimizedPrompt(
        original=f"Role: {role}\nTask: {task}\nContext: {context}",
        optimized=optimized,
        mode=OptimizationMode.CRISPE,
        enhancement_notes=[
            "Added structured system context with XML tags",
            "Included SA-specific legal profile and skills",
            "Added constitutional interpretation constraints",
            "Structured workflow for consistent reasoning"
        ],
        sa_legal_adaptations=[
            "SAFLII citation format requirement",
            "Ubuntu-infused legal reasoning",
            "Transformative constitutionalism principles",
            "Court hierarchy awareness",
            "Professional ethics compliance"
        ]
    )


# ═══════════════════════════════════════════════════════════════════════════════
# CO-STAR LEGAL OPTIMIZER
# Context, Objective, Style, Tone, Audience, Result
# ═══════════════════════════════════════════════════════════════════════════════

CO_STAR_LEGAL_TEMPLATE = """<context>
**Matter Background:**
{context}

**Jurisdiction:** South Africa
**Applicable Legal System:** Mixed legal system (Roman-Dutch common law, English common law, customary law, Constitutional supremacy)
</context>

<objective>
{objective}
</objective>

<style>
**Identity:** {style_identity}
**Approach:** 
- Apply rigorous legal analysis methodology
- Use the constitutional values of human dignity, equality, and freedom as interpretive guides
- Consider ubuntu where applicable to legal reasoning
- Maintain scholarly precision with practical applicability
</style>

<tone>
{tone}
</tone>

<audience>
{audience}
</audience>

<result>
**Expected Output:**
{result}

**Quality Standards:**
- All case citations must use SAFLII neutral citation format
- Legislation referenced by full title, Act number, and year
- Clear structure with numbered paragraphs for legal documents
- Reasoning must be transparent and traceable
- Distinguish between binding precedent and persuasive authority
</result>"""


def optimize_with_co_star(
    context: str,
    objective: str,
    style_identity: str = "Senior SA Legal Practitioner",
    tone: str = "Professional, authoritative, yet accessible",
    audience: str = "Legal professionals with SA law knowledge",
    result: str = "Comprehensive legal analysis with recommendations"
) -> OptimizedPrompt:
    """
    Apply CO-STAR optimization for SA legal prompts.
    Emphasizes audience awareness critical for SA practice.
    """
    optimized = CO_STAR_LEGAL_TEMPLATE.format(
        context=context,
        objective=objective,
        style_identity=style_identity,
        tone=tone,
        audience=audience,
        result=result
    )
    
    return OptimizedPrompt(
        original=f"Context: {context}\nObjective: {objective}",
        optimized=optimized,
        mode=OptimizationMode.CO_STAR,
        enhancement_notes=[
            "Structured with clear CO-STAR components",
            "Added SA jurisdictional context",
            "Included quality standards for output",
            "Specified audience for tailored communication"
        ],
        sa_legal_adaptations=[
            "Mixed legal system acknowledgment",
            "Constitutional values as interpretive guides",
            "Ubuntu principle integration",
            "SAFLII citation standards",
            "Court hierarchy distinction"
        ]
    )


# ═══════════════════════════════════════════════════════════════════════════════
# CHAIN OF THOUGHT LEGAL OPTIMIZER
# Step-by-step legal reasoning with self-validation
# ═══════════════════════════════════════════════════════════════════════════════

COT_LEGAL_TEMPLATE = """You are a senior SA legal practitioner applying systematic legal analysis. For the matter below, apply rigorous step-by-step reasoning.

**MATTER:**
{matter}

**ANALYSIS PROTOCOL:**

<step_1>
**Issue Identification**
- Identify all legal issues presented
- Classify issues by area of law
- Note any preliminary/procedural issues
</step_1>

<step_2>
**Applicable Law Framework**
- Identify relevant constitutional provisions
- List applicable statutes (with Act numbers)
- Identify relevant common law principles
- Note any customary law considerations
</step_2>

<step_3>
**Precedent Analysis**
- Identify binding precedents (Constitutional Court, SCA)
- Note persuasive authorities (High Court, foreign jurisdictions)
- Analyse how precedents apply to current facts
- Distinguish any contrary authorities
</step_3>

<step_4>
**Application to Facts**
- Apply each legal principle to the specific facts
- Consider alternative interpretations
- Address potential counterarguments
- Apply limitations analysis if rights are implicated (s36 Constitution)
</step_4>

<step_5>
**Self-Validation Check**
- Verify logical consistency of reasoning
- Confirm all cited authorities are correctly applied
- Check for any gaps in analysis
- Ensure conclusions follow from premises
</step_5>

<step_6>
**Conclusion and Recommendations**
- State definitive conclusions
- Provide practical recommendations
- Note any caveats or areas of uncertainty
- Suggest further steps if applicable
</step_6>

**Meta-Cognition Prompt:** After completing analysis, briefly reflect on:
- Confidence level in conclusions (High/Medium/Low)
- Key assumptions made
- Most significant risk factors

{additional_instructions}"""


def optimize_with_chain_of_thought(
    matter: str,
    additional_instructions: str = ""
) -> OptimizedPrompt:
    """
    Apply Chain of Thought optimization for complex legal analysis.
    Includes self-validation and meta-cognition steps.
    """
    optimized = COT_LEGAL_TEMPLATE.format(
        matter=matter,
        additional_instructions=additional_instructions
    )
    
    return OptimizedPrompt(
        original=matter,
        optimized=optimized,
        mode=OptimizationMode.CHAIN_OF_THOUGHT,
        enhancement_notes=[
            "Structured 6-step reasoning protocol",
            "Added self-validation check",
            "Included meta-cognition reflection",
            "Systematic issue-to-conclusion flow"
        ],
        sa_legal_adaptations=[
            "SA court hierarchy for precedent binding force",
            "Constitutional provisions priority",
            "Section 36 limitations analysis integration",
            "Mixed legal system consideration",
            "SAFLII citation format embedded"
        ],
        reasoning_structure="Step 1: Issue ID → Step 2: Law Framework → Step 3: Precedents → Step 4: Application → Step 5: Validation → Step 6: Conclusions"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# RISE LEGAL OPTIMIZER
# Recursive Introspection for Self-Improvement
# ═══════════════════════════════════════════════════════════════════════════════

RISE_LEGAL_TEMPLATE = """You are an expert SA Legal Analyst applying the RISE methodology (Recursive Introspection for Self-improvement). You will automatically iterate to improve your analysis.

**MATTER FOR ANALYSIS:**
{matter}

**RISE PROTOCOL - AUTO-ITERATE 3 TIMES:**

**Iteration 1: Initial Analysis**
1. Provide your initial legal analysis
2. Rate confidence (1-10 scale)
3. Identify areas of uncertainty

**Iteration 2: Self-Critique**
1. Examine weaknesses in Iteration 1
2. Identify:
   - Missing precedents
   - Underexplored arguments
   - Alternative interpretations
3. Develop improvement strategy

**Iteration 3: Enhanced Analysis**
1. Address all weaknesses identified
2. Incorporate additional authorities
3. Strengthen reasoning chain
4. Reassess confidence level

**SA LEGAL QUALITY STANDARDS:**
- All cases cited must use SAFLII neutral citation format
- Constitutional interpretation must apply transformative constitutionalism
- Consider ubuntu principle where relevant
- Distinguish obiter from ratio decidendi
- Note binding vs persuasive authority

**FINAL OUTPUT:**
After 3 iterations, provide:
1. **Final Analysis** - The refined, comprehensive legal opinion
2. **Improvement Summary** - Key enhancements from iteration process
3. **Confidence Assessment** - Final confidence level with justification
4. **Risk Flags** - Any remaining uncertainties or alternative outcomes

{additional_context}"""


def optimize_with_rise(
    matter: str,
    additional_context: str = ""
) -> OptimizedPrompt:
    """
    Apply RISE (Recursive Introspection) optimization.
    Forces the model to self-critique and improve iteratively.
    """
    optimized = RISE_LEGAL_TEMPLATE.format(
        matter=matter,
        additional_context=additional_context
    )
    
    return OptimizedPrompt(
        original=matter,
        optimized=optimized,
        mode=OptimizationMode.RISE,
        enhancement_notes=[
            "3-iteration self-improvement protocol",
            "Built-in self-critique mechanism",
            "Progressive confidence assessment",
            "Automatic weakness identification and remediation"
        ],
        sa_legal_adaptations=[
            "SAFLII citation enforcement",
            "Transformative constitutionalism integration",
            "Ubuntu principle consideration",
            "Ratio/obiter distinction",
            "Precedent binding force analysis"
        ],
        reasoning_structure="Initial Analysis → Self-Critique → Enhanced Analysis → Final Output"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# O1-STYLE LEGAL OPTIMIZER
# Structured reasoning with step budgets and reward scoring
# ═══════════════════════════════════════════════════════════════════════════════

O1_STYLE_LEGAL_TEMPLATE = """Analyze this SA legal matter using structured reasoning with explicit thinking and self-evaluation.

**MATTER:**
{matter}

**INSTRUCTIONS:**

Begin by enclosing all thoughts within <thinking> tags, exploring multiple angles and approaches.

Break down the legal analysis into clear steps within <step> tags. You have a budget of 15 steps for this analysis.

Use <count> tags after each step to show the remaining step budget. Stop when reaching 0.

Continuously adjust your reasoning based on intermediate findings, adapting your legal strategy as you progress.

Regularly evaluate progress using <reflection> tags. Be critical and honest about your legal reasoning.

Assign a quality score between 0.0 and 1.0 using <reward> tags after each reflection:
- **0.8+**: Legal reasoning is sound, well-supported by authority - continue current approach
- **0.5-0.7**: Minor gaps in reasoning - consider adjustments
- **Below 0.5**: Significant issues - backtrack and try a different approach

**SA LEGAL FRAMEWORK REQUIREMENTS:**
- Apply Constitutional Court precedent as binding authority
- Use SAFLII neutral citation format for all cases
- Consider s36 limitations for rights-based analysis
- Apply transformative constitutionalism lens
- Distinguish binding from persuasive authority

If unsure or reward score is low, backtrack and explain your decision within <thinking> tags.

For complex legal issues, explore multiple interpretations before settling on a position.

Synthesize the final answer within <answer> tags, providing:
1. Clear legal conclusion
2. Key supporting authorities
3. Practical recommendations
4. Risk assessment

Conclude with a final reflection on the overall analysis, discussing:
- Effectiveness of the approach
- Key challenges encountered
- Quality of final conclusion
- Final reward score

{additional_instructions}"""


def optimize_with_o1_style(
    matter: str,
    additional_instructions: str = ""
) -> OptimizedPrompt:
    """
    Apply O1-Style structured reasoning with step budgets and self-evaluation.
    Forces explicit thinking process and quality scoring.
    """
    optimized = O1_STYLE_LEGAL_TEMPLATE.format(
        matter=matter,
        additional_instructions=additional_instructions
    )
    
    return OptimizedPrompt(
        original=matter,
        optimized=optimized,
        mode=OptimizationMode.O1_STYLE,
        enhancement_notes=[
            "Explicit thinking process with tags",
            "15-step budget for controlled reasoning depth",
            "Self-evaluation with quality scoring (0-1)",
            "Backtracking capability for low-quality reasoning",
            "Structured final answer synthesis"
        ],
        sa_legal_adaptations=[
            "Constitutional Court precedent binding requirement",
            "SAFLII citation format mandate",
            "Section 36 limitations analysis",
            "Transformative constitutionalism lens",
            "Authority hierarchy awareness"
        ],
        reasoning_structure="Thinking → Steps (with budget) → Reflections (with scores) → Answer"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# META PROMPT OPTIMIZER
# Structural optimization preserving core meaning
# ═══════════════════════════════════════════════════════════════════════════════

META_PROMPT_TEMPLATE = """You are a legal prompt optimization specialist. Transform the following legal prompt into an enhanced version that will produce superior results.

**ORIGINAL PROMPT:**
{original_prompt}

**OPTIMIZATION OBJECTIVES:**
1. **Structural Clarity** - Add clear sections and organization
2. **SA Legal Context** - Embed South African jurisdictional requirements
3. **Precision** - Remove ambiguity, add specific requirements
4. **Quality Controls** - Add output format and quality standards

**SA LEGAL OPTIMIZATION REQUIREMENTS:**
- Ensure SAFLII neutral citation format is specified
- Include constitutional values framework
- Reference relevant SA court hierarchy
- Add ubuntu principle consideration where appropriate
- Specify Act citation format (Title, Number of Year)

**OUTPUT:**
Provide the optimized prompt that:
- Preserves the original intent and core requirements
- Adds structural elements for better AI processing
- Embeds SA-specific legal standards
- Includes quality assurance checkpoints

Return ONLY the optimized prompt, no explanations."""


def optimize_with_meta_prompt(
    original_prompt: str
) -> OptimizedPrompt:
    """
    Apply meta-prompting to optimize structure while preserving meaning.
    This is a prompt that generates better prompts.
    """
    optimized = META_PROMPT_TEMPLATE.format(
        original_prompt=original_prompt
    )
    
    return OptimizedPrompt(
        original=original_prompt,
        optimized=optimized,
        mode=OptimizationMode.META_PROMPT,
        enhancement_notes=[
            "Self-referential prompt optimization",
            "Structural enhancement focus",
            "Preserves original intent",
            "Adds SA legal context automatically"
        ],
        sa_legal_adaptations=[
            "SAFLII citation format embedding",
            "Constitutional values framework",
            "Court hierarchy reference",
            "Ubuntu principle integration",
            "SA Act citation format"
        ]
    )


# ═══════════════════════════════════════════════════════════════════════════════
# HYBRID LEGAL OPTIMIZER (NEW SP1)
# Combines CRISPE structure with Chain of Thought reasoning
# ═══════════════════════════════════════════════════════════════════════════════

HYBRID_LEGAL_TEMPLATE = """<system_context>
You are an expert SA Legal Professional combining structured expertise with systematic reasoning.

<role>
{role}
</role>

<profile>
- **Expertise**: {expertise}
- **Jurisdiction**: South African courts hierarchy
- **Legal Systems**: Constitutional supremacy, Roman-Dutch common law, customary law
- **Citation Standard**: SAFLII neutral format
</profile>

<skills>
- Transformative constitutionalism interpretation
- Systematic legal reasoning with self-validation
- Ubuntu-infused analysis
- Precedent synthesis and application
</skills>

<constraints>
- Use SAFLII neutral citation format
- Reference Acts by full title with number and year
- Apply s36 limitations for rights-based matters
- Maintain legal ethics per LPC guidelines
{additional_constraints}
</constraints>
</system_context>

<task>
{task}
</task>

<context>
{context}
</context>

<reasoning_protocol>
You MUST follow this systematic analysis approach:

**STEP 1: Issue Identification**
- List all legal issues
- Classify by area of law
- Note preliminary issues

**STEP 2: Legal Framework**
- Constitutional provisions
- Applicable statutes (with Act numbers)
- Common law principles
- Customary law (if applicable)

**STEP 3: Precedent Analysis**
- Binding precedents (CC, SCA)
- Persuasive authorities
- Distinguish contrary cases

**STEP 4: Application**
- Apply each principle to facts
- Consider alternatives
- Address counterarguments
- s36 analysis if needed

**STEP 5: Self-Validation**
✓ Logical consistency check
✓ Citation accuracy check
✓ Gap analysis
✓ Conclusion verification

**STEP 6: Final Output**
- Clear conclusions
- Practical recommendations
- Risk flags
- Confidence assessment
</reasoning_protocol>

<output_format>
{output_format}
</output_format>"""


def optimize_with_hybrid_legal(
    role: str,
    task: str,
    context: str,
    expertise: str = "SA Legal Practice",
    output_format: str = "Comprehensive Legal Analysis",
    additional_constraints: str = ""
) -> OptimizedPrompt:
    """
    Apply Hybrid Legal optimization combining CRISPE structure with CoT reasoning.
    Best for complex matters requiring both structure and transparent reasoning.
    """
    optimized = HYBRID_LEGAL_TEMPLATE.format(
        role=role,
        expertise=expertise,
        task=task,
        context=context,
        output_format=output_format,
        additional_constraints=additional_constraints
    )
    
    return OptimizedPrompt(
        original=f"Role: {role}\nTask: {task}\nContext: {context}",
        optimized=optimized,
        mode=OptimizationMode.HYBRID_LEGAL,
        enhancement_notes=[
            "Combined CRISPE structure with CoT reasoning",
            "6-step systematic analysis protocol",
            "Built-in self-validation checkpoint",
            "Confidence assessment requirement",
            "Maximum enhancement for complex matters"
        ],
        sa_legal_adaptations=[
            "Constitutional supremacy framework",
            "Roman-Dutch common law integration",
            "Customary law consideration",
            "Ubuntu principle in reasoning",
            "Court hierarchy for precedent"
        ],
        reasoning_structure="System Context → Task → Reasoning Protocol (6 steps) → Output"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# CLAUDE-STYLE TASK INSTRUCTIONS OPTIMIZER (NEW SP1)
# Generates detailed instructions for complex legal tasks
# ═══════════════════════════════════════════════════════════════════════════════

CLAUDE_STYLE_TEMPLATE = """You will be acting as a South African legal professional completing a complex legal task. I will explain the task, and you will follow these detailed instructions to complete it accurately.

<task_description>
{task}
</task_description>

<context>
{context}
</context>

<important_rules>
Here are critical rules for completing this legal task:

1. **Citation Format**: Always use SAFLII neutral citation format for SA cases (e.g., *Party v Party* [Year] Court Number).

2. **Legislation References**: Reference Acts by their full title with number and year (e.g., "Constitution of the Republic of South Africa, 1996" or "Labour Relations Act 66 of 1995").

3. **Court Hierarchy**: 
   - Constitutional Court decisions are binding on all courts
   - Supreme Court of Appeal binds all lower courts except Constitutional Court
   - High Court divisions bind magistrates' courts in their area
   - Apply precedent accordingly

4. **Constitutional Interpretation**:
   - Apply transformative constitutionalism lens
   - Consider ubuntu principle in interpretation
   - For rights limitations, apply s36 analysis:
     a. Is the limitation prescribed by law of general application?
     b. Is it reasonable and justifiable in an open and democratic society?
     c. Consider: nature of right, importance of limitation purpose, nature and extent of limitation, relation between limitation and purpose, less restrictive means

5. **Reasoning Standards**:
   - Distinguish between ratio decidendi (binding) and obiter dicta (persuasive)
   - Apply proper statutory interpretation methods (purposive, golden rule, mischief rule)
   - Consider context and legislative history

6. **Quality Checks**:
   - Verify all citations are accurate
   - Ensure reasoning is transparent and traceable
   - Confirm conclusions follow from analysis
   - Note any caveats or uncertainties
</important_rules>

<output_instructions>
{output_format}

When you provide your analysis:
- First, identify the key legal issues in <issue_identification> tags
- Then, provide your substantive analysis
- Use <reasoning> tags for complex analytical steps
- Conclude with a clear summary of your conclusions
- If you're uncertain about anything, note it explicitly
</output_instructions>

Now, complete the task following these instructions. Begin with your issue identification."""


def optimize_with_claude_style(
    task: str,
    context: str,
    output_format: str = "Provide a comprehensive legal analysis"
) -> OptimizedPrompt:
    """
    Apply Claude-style task instructions optimization.
    Best for complex tasks requiring detailed guidance and structured output.
    """
    optimized = CLAUDE_STYLE_TEMPLATE.format(
        task=task,
        context=context,
        output_format=output_format
    )
    
    return OptimizedPrompt(
        original=f"Task: {task}\nContext: {context}",
        optimized=optimized,
        mode=OptimizationMode.CLAUDE_STYLE,
        enhancement_notes=[
            "Detailed task instructions format",
            "Explicit rules for legal work",
            "Structured output with XML tags",
            "Built-in quality checks",
            "Clear reasoning requirements"
        ],
        sa_legal_adaptations=[
            "SAFLII citation rules embedded",
            "Court hierarchy explained",
            "Constitutional interpretation guide",
            "Section 36 analysis framework",
            "Ratio/obiter distinction required"
        ],
        reasoning_structure="Task Description → Context → Rules → Output Instructions → Execution"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP2 NEW MODES: EXPERT WITNESS OPTIMIZER
# ═══════════════════════════════════════════════════════════════════════════════

EXPERT_WITNESS_TEMPLATE = """You are acting as an Expert Witness preparing a technical legal opinion for court proceedings in South Africa.

**EXPERT'S QUALIFICATIONS & FIELD:**
{field_of_expertise}

**MATTER REQUIRING EXPERT OPINION:**
{matter}

**INSTRUCTING PARTY:**
{instructing_party}

**EXPERT WITNESS PROTOCOL:**

<section_1_introduction>
1. **Expert's Background**
   - Full qualifications and experience
   - Relevant publications or prior court appearances
   - Statement of independence and impartiality
   - Confirmation that duty is to the court, not instructing party
</section_1_introduction>

<section_2_brief_and_materials>
2. **Brief Received & Materials Reviewed**
   - Summarize instructions received
   - List all documents, data, and materials reviewed
   - Note any limitations on materials provided
   - Identify any additional materials that would be helpful
</section_2_brief_and_materials>

<section_3_methodology>
3. **Methodology Applied**
   - Explain technical/scientific methodology used
   - Reference industry standards, professional guidelines
   - Note any peer-reviewed literature relied upon
   - Describe analytical process step-by-step
</section_3_methodology>

<section_4_findings>
4. **Findings & Analysis**
   - Present factual findings clearly
   - Distinguish between facts, inferences, and opinions
   - Use accessible language while maintaining technical accuracy
   - Address all questions posed in the brief
</section_4_findings>

<section_5_opinion>
5. **Expert Opinion**
   - State conclusions clearly and unambiguously
   - Indicate degree of certainty (probability, likelihood)
   - Note any caveats or limitations
   - Address counter-arguments or alternative interpretations
</section_5_opinion>

<section_6_declaration>
6. **Declaration**
   - Confirm independence and impartiality
   - Acknowledge duty to court under Rule 36(9)
   - Sign and date
</section_6_declaration>

**SA COURT REQUIREMENTS:**
- Comply with Uniform Rules of Court, Rule 36(9)
- Ensure opinion is comprehensible to a layperson
- Avoid legal conclusions (that's for the court)
- Clearly separate facts from opinion
- Disclose any prior relationship with parties

{additional_instructions}"""


def optimize_with_expert_witness(
    matter: str,
    field_of_expertise: str = "Specialist with relevant professional qualifications",
    instructing_party: str = "Instructed by legal representatives of the Applicant/Defendant",
    additional_instructions: str = ""
) -> OptimizedPrompt:
    """
    Apply Expert Witness optimization for technical court opinions.
    Best for matters requiring expert technical evidence.
    """
    optimized = EXPERT_WITNESS_TEMPLATE.format(
        matter=matter,
        field_of_expertise=field_of_expertise,
        instructing_party=instructing_party,
        additional_instructions=additional_instructions
    )
    
    return OptimizedPrompt(
        original=matter,
        optimized=optimized,
        mode=OptimizationMode.EXPERT_WITNESS,
        enhancement_notes=[
            "Expert witness report structure",
            "Independence declaration included",
            "Methodology documentation",
            "Court-compliant format (Rule 36(9))",
            "Facts/opinion separation enforced"
        ],
        sa_legal_adaptations=[
            "Uniform Rules Rule 36(9) compliance",
            "SA court evidentiary standards",
            "Independence and impartiality requirements",
            "Technical language accessibility requirements"
        ],
        reasoning_structure="Qualifications → Brief → Methodology → Findings → Opinion → Declaration"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP2 NEW MODES: MEDIATION/ADR OPTIMIZER
# ═══════════════════════════════════════════════════════════════════════════════

MEDIATION_ADR_TEMPLATE = """You are an experienced ADR Practitioner (Mediator/Arbitrator) registered with the relevant SA professional body, facilitating dispute resolution.

**DISPUTE CONTEXT:**
{dispute}

**PARTIES INVOLVED:**
{parties}

**ADR PROCESS:** {process_type}

**MEDIATION/ADR FRAMEWORK:**

<phase_1_opening>
**PHASE 1: OPENING & AGREEMENT TO PROCESS**
- Welcome parties and confirm voluntary participation
- Explain mediator's role (neutral facilitator, not decision-maker)
- Establish ground rules: respect, confidentiality, good faith
- Confirm authority to settle / scope of mandate
- Obtain signed ADR agreement (if not already signed)
</phase_1_opening>

<phase_2_storytelling>
**PHASE 2: PARTY STATEMENTS & ISSUE IDENTIFICATION**
- Each party presents their perspective uninterrupted
- Active listening and reflection by mediator
- Identify and summarize key issues
- Distinguish positions from underlying interests
- Create agenda of issues to address
</phase_2_storytelling>

<phase_3_exploration>
**PHASE 3: EXPLORATION & OPTION GENERATION**
- Private caucuses if needed (explain confidentiality)
- Explore underlying interests and needs
- Reality-test positions (BATNA/WATNA analysis)
- Brainstorm options without commitment
- Identify areas of potential agreement
</phase_3_exploration>

<phase_4_negotiation>
**PHASE 4: NEGOTIATION & PROBLEM-SOLVING**
- Facilitate direct negotiation between parties
- Use interest-based bargaining techniques
- Address obstacles and impasses
- Build incrementally on agreements reached
- Consider creative/mutual gain solutions
</phase_4_negotiation>

<phase_5_agreement>
**PHASE 5: AGREEMENT & CLOSURE**
- Document terms agreed (clear, specific, actionable)
- Ensure parties understand implications
- Address implementation and monitoring
- Provide for dispute resolution if agreement fails
- For arbitration: issue reasoned award
</phase_5_agreement>

**SA ADR LEGAL FRAMEWORK:**
- Short Process Courts and Mediation in Certain Civil Cases Rules (2014)
- Arbitration Act 42 of 1965 (domestic)
- CCMA processes under LRA 66 of 1995 (labour disputes)
- Consumer Protection Act 68 of 2008, s69-71 (consumer disputes)
- Recognition of customary and traditional dispute resolution

**ADR PRACTITIONER ETHICS:**
- Maintain strict neutrality and impartiality
- Ensure voluntary and informed participation
- Protect vulnerable parties
- Maintain confidentiality (except violence/abuse/crime)
- Declare conflicts of interest

{additional_guidance}"""


def optimize_with_mediation_adr(
    dispute: str,
    parties: str = "Party A and Party B",
    process_type: str = "Mediation",
    additional_guidance: str = ""
) -> OptimizedPrompt:
    """
    Apply Mediation/ADR optimization for dispute resolution.
    Best for preparing mediation strategies, arbitration arguments, or settlement discussions.
    """
    optimized = MEDIATION_ADR_TEMPLATE.format(
        dispute=dispute,
        parties=parties,
        process_type=process_type,
        additional_guidance=additional_guidance
    )
    
    return OptimizedPrompt(
        original=dispute,
        optimized=optimized,
        mode=OptimizationMode.MEDIATION_ADR,
        enhancement_notes=[
            "5-phase ADR process structure",
            "Interest-based negotiation framework",
            "Caucus and joint session protocols",
            "Settlement agreement guidelines",
            "BATNA/WATNA analysis integration"
        ],
        sa_legal_adaptations=[
            "SA ADR legislation framework",
            "CCMA process integration (LRA)",
            "Consumer dispute resolution (CPA)",
            "Customary dispute resolution recognition",
            "ADR practitioner ethics standards"
        ],
        reasoning_structure="Opening → Storytelling → Exploration → Negotiation → Agreement"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP2 NEW MODES: COMPLIANCE AUDIT OPTIMIZER
# ═══════════════════════════════════════════════════════════════════════════════

COMPLIANCE_AUDIT_TEMPLATE = """You are a Senior Legal Compliance Officer conducting a comprehensive regulatory compliance audit for a South African organization.

**ORGANIZATION DETAILS:**
{organization}

**AUDIT SCOPE:**
{scope}

**PRIMARY REGULATORY FRAMEWORK:**
{regulations}

**COMPLIANCE AUDIT PROTOCOL:**

<section_1_framework>
**1. REGULATORY LANDSCAPE MAPPING**
- Identify all applicable legislation, regulations, and codes
- Determine primary regulator(s) and reporting obligations
- Map sectoral-specific requirements
- Note industry codes and voluntary standards
- Identify recent regulatory changes or pending amendments
</section_1_framework>

<section_2_policies>
**2. POLICY & GOVERNANCE REVIEW**
- Assess existing compliance policies and procedures
- Review governance structures and accountability
- Evaluate compliance function resourcing
- Examine board/management oversight mechanisms
- Check delegation frameworks and authorities
</section_2_policies>

<section_3_controls>
**3. CONTROL ENVIRONMENT ASSESSMENT**
- Evaluate preventive controls in place
- Assess detective controls and monitoring
- Review corrective action procedures
- Examine record-keeping and documentation
- Test control effectiveness (sample basis)
</section_3_controls>

<section_4_risk>
**4. RISK ASSESSMENT**
- Identify compliance risk areas
- Assess likelihood and impact of non-compliance
- Evaluate consequences (penalties, reputational, operational)
- Prioritize risks using risk matrix
- Assess mitigating factors and residual risk
</section_4_risk>

<section_5_gaps>
**5. GAP ANALYSIS & FINDINGS**
For each area reviewed:
| Requirement | Current State | Gap Identified | Risk Level | Recommendation |
|-------------|---------------|----------------|------------|----------------|
(Provide detailed table)

- Categorize findings: Critical / Major / Minor / Observation
- Document evidence supporting findings
- Note any areas of good practice
</section_5_gaps>

<section_6_recommendations>
**6. RECOMMENDATIONS & ACTION PLAN**
For each finding:
- Specific corrective action required
- Responsible person/department
- Timeline for remediation
- Resources required
- KPIs for measuring compliance
</section_6_recommendations>

**KEY SA COMPLIANCE LEGISLATION TO CONSIDER:**
- Companies Act 71 of 2008 (corporate governance, King IV)
- Financial Intelligence Centre Act 38 of 2001 (AML/CFT)
- Protection of Personal Information Act 4 of 2013 (data privacy)
- Financial Sector Regulation Act 9 of 2017 (financial services)
- Consumer Protection Act 68 of 2008 (consumer rights)
- Labour legislation (LRA, BCEA, EE Act, OHSA)
- Environmental legislation (NEMA, sector-specific)
- Competition Act 89 of 1998

**AUDIT REPORT FORMAT:**
1. Executive Summary (for board/senior management)
2. Scope and Methodology
3. Detailed Findings (by risk area)
4. Risk Register Update
5. Action Plan with Timelines
6. Appendices (evidence, working papers)

{additional_requirements}"""


def optimize_with_compliance_audit(
    organization: str = "The organization under review",
    scope: str = "Comprehensive regulatory compliance review",
    regulations: str = "Applicable SA legislation and industry codes",
    additional_requirements: str = ""
) -> OptimizedPrompt:
    """
    Apply Compliance Audit optimization for regulatory reviews.
    Best for compliance assessments, regulatory gap analysis, and audit reports.
    """
    optimized = COMPLIANCE_AUDIT_TEMPLATE.format(
        organization=organization,
        scope=scope,
        regulations=regulations,
        additional_requirements=additional_requirements
    )
    
    return OptimizedPrompt(
        original=f"Compliance audit for: {scope}",
        optimized=optimized,
        mode=OptimizationMode.COMPLIANCE_AUDIT,
        enhancement_notes=[
            "6-section audit protocol",
            "Gap analysis with risk matrix",
            "Actionable recommendations format",
            "Finding categorization (Critical/Major/Minor)",
            "Board-ready executive summary"
        ],
        sa_legal_adaptations=[
            "Key SA compliance legislation mapped",
            "King IV governance integration",
            "POPIA data protection requirements",
            "FICA/AML compliance",
            "Sector-specific regulatory requirements"
        ],
        reasoning_structure="Framework → Policies → Controls → Risk → Gaps → Recommendations"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP3 NEW MODES: VARI (Variational Planning) OPTIMIZER
# From DeepMind research - adapted for SA Legal Practice
# ═══════════════════════════════════════════════════════════════════════════════

VARI_LEGAL_TEMPLATE = """You will use Variational Planning methodology for SA legal content generation.

## 1. Legal Task Definition
**Task Type:** {task_type}
**Target Audience:** {audience}
**Primary Objective:** {objective}
**Legal Subject Matter:** {subject_matter}
**Jurisdiction:** South Africa
**Content Constraints:** {constraints}

## 2. State Space Definition (Legal Context)
S = {{
    s1: "Current legal issue/question",
    s2: "Applicable legislation identified",
    s3: "Relevant precedents considered",
    s4: "Client/audience characteristics",
    s5: "Court/forum context",
    s6: "Procedural stage",
    s7: "Risk factors identified"
}}

## 3. Action Space Definition (Legal Steps)
A = {{
    a1: "Select next legal principle to apply",
    a2: "Determine depth of analysis required",
    a3: "Choose citation/authority to reference",
    a4: "Select argument structure",
    a5: "Apply constitutional values filter",
    a6: "Insert SA-specific considerations"
}}

## 4. Variational Posterior (Decision Weights)
q(a|s) = {{
    π1(a1|s): Priority of legal principles based on relevance,
    π2(a2|s): Analysis depth based on complexity,
    π3(a3|s): Authority selection based on binding force,
    π4(a4|s): Argument structure based on persuasiveness,
    π5(a5|s): Constitutional values weight,
    π6(a6|s): SA-specific considerations weight
}}

## 5. Reward Function (Quality Metrics)
R(s, a, s') = w1 * legal_accuracy +
              w2 * precedent_relevance +
              w3 * constitutional_compliance +
              w4 * practical_applicability +
              w5 * citation_quality -
              w6 * error_penalty

Where weights prioritize: accuracy > precedent > constitutional > practical

## 6. Optimization Objective
Maximize: E_q[R(s,a,s')] - β * KL(q(a|s) || p(a))
where p(a) is prior distribution of standard legal approaches

## 7. Generation Process
1. Initialize with identified legal issue
2. Loop until complete analysis:
   - Observe current analysis state s
   - Sample optimal action a from q(a|s)
   - Execute action (develop argument/cite authority)
   - Update to new state s'
   - Calculate quality reward r
3. Refine based on cumulative reward

## 8. SA Legal Quality Standards
- All citations in SAFLII neutral format
- Constitutional Court precedent takes priority
- Apply transformative constitutionalism lens
- Consider ubuntu in interpretation
- Reference Acts by full title (Act XX of YYYY)

## 9. Output Format
For each analysis component, provide:
1. Current state summary
2. Selected approach and probability basis
3. Generated legal content
4. Quality assessment score

---

**LEGAL MATTER TO ANALYSE:**
{matter}

Apply variational planning to generate optimal legal analysis."""


def optimize_with_vari_planning(
    matter: str,
    task_type: str = "Legal Analysis",
    audience: str = "Legal professionals",
    objective: str = "Comprehensive legal opinion",
    subject_matter: str = "As identified from the matter",
    constraints: str = "SA legal standards apply"
) -> OptimizedPrompt:
    """
    Apply VARI (Variational Planning) optimization.
    DeepMind technique adapted for legal content generation.
    """
    optimized = VARI_LEGAL_TEMPLATE.format(
        matter=matter,
        task_type=task_type,
        audience=audience,
        objective=objective,
        subject_matter=subject_matter,
        constraints=constraints
    )
    
    return OptimizedPrompt(
        original=matter,
        optimized=optimized,
        mode=OptimizationMode.VARI_PLANNING,
        enhancement_notes=[
            "Variational planning methodology applied",
            "State-action space defined for legal reasoning",
            "Quality reward function with legal metrics",
            "Probabilistic decision weighting",
            "Iterative refinement process"
        ],
        sa_legal_adaptations=[
            "SAFLII citation format required",
            "Constitutional Court precedent priority",
            "Transformative constitutionalism lens",
            "Ubuntu consideration in interpretation",
            "SA Act citation format"
        ],
        reasoning_structure="State Definition → Action Selection → Reward Optimization → Generation"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP3 NEW MODES: Q* (A* + Q-Learning) OPTIMIZER
# For complex multi-step legal strategy planning
# ═══════════════════════════════════════════════════════════════════════════════

Q_STAR_LEGAL_TEMPLATE = """<q-star-legal-prompt>
<system-instruction>
You are implementing the Q* algorithm to design optimal legal strategy paths for SA matters. Your goal is to find the optimal sequence of legal steps to maximize the client's outcome. Focus on creating a detailed, step-by-step legal strategy that adapts to case developments.
</system-instruction>

<variables>
<var name="gamma" value="0.95">Discount factor for future legal outcomes</var>
<var name="lambda" value="1.0">Balance between immediate and long-term gains</var>
<var name="max_depth" value="25">Maximum strategy steps to plan</var>
<var name="top_k" value="3">Top legal options to consider at each step</var>
<var name="review_interval" value="milestone">Review at each procedural milestone</var>
</variables>

<initialization>
<state id="s_0">
<description>
**LEGAL MATTER:**
{matter}

**Current State Assessment:**
- Stage: {stage}
- Forum: {forum}
- Key Issues: {key_issues}
- Strengths: {strengths}
- Weaknesses: {weaknesses}
- Constraints: {constraints}
</description>
<g_value>0</g_value>
<h_value>Estimated steps to achieve legal objective</h_value>
<f_value>${{g_value + lambda * h_value}}</f_value>
</state>
</initialization>

<a-star-search>
<open-set>
<state ref="s_0" />
</open-set>
<closed-set></closed-set>
<main-loop>
<step>
1. Select legal state s with highest f_value from open-set
2. If s achieves the legal objective, return the strategy path
3. Move s from open-set to closed-set
4. For each possible legal action a from s:
   4.1. Generate new legal state s' = T(s, a)
   4.2. If s' in closed-set, continue to next action
   4.3. Calculate f_value for s':
        g(s') = g(s) + legal_progress(s, a, s')
        h(s') = estimate_remaining_steps(s')
        f(s') = g(s') + lambda * h(s')
   4.4. If s' not in open-set, add to open-set
   4.5. If s' in open-set but new path is better, update s'
5. Repeat from step 1
</step>
</main-loop>
</a-star-search>

<q-value-estimation>
<function name="Q">
Q(s, a) = R(s, a) + gamma * max[Q(s', a') for all a' in top_k actions from s']
</function>
<method>
1. Use precedent outcomes to inform Q-function
2. Estimate Q(s, a) for top_k legal strategies
3. Use Q(s, a) as h(s') in A* search
</method>
<factors>
- Probability of success
- Time to resolution
- Cost efficiency
- Client objectives alignment
- Risk minimization
- Precedent support strength
</factors>
</q-value-estimation>

<legal-strategy-aggregation>
<function name="g">
g(s) = Agg[R_legal(s_1), ..., R_legal(s_t)]
</function>
<aggregation-methods>
<method name="outcome_focused">Maximize probability of favorable judgment</method>
<method name="cost_optimized">Balance outcome with legal costs</method>
<method name="risk_averse">Minimize downside risk exposure</method>
<method name="precedent_building">Create favorable precedent for future</method>
</aggregation-methods>
</legal-strategy-aggregation>

<output-format>
<legal-strategy>
<overall-approach>${{STRATEGY_SUMMARY}}</overall-approach>
<timeline>${{ESTIMATED_TIMELINE}}</timeline>

<strategy-phases>
<phase n="${{PHASE_NUMBER}}">
<name>${{PHASE_NAME}}</name>
<objectives>${{PHASE_OBJECTIVES}}</objectives>
<actions>${{SPECIFIC_ACTIONS}}</actions>
<expected-outcomes>${{EXPECTED_OUTCOMES}}</expected-outcomes>
<q-value>${{SUCCESS_PROBABILITY}}</q-value>
<contingencies>${{IF_PHASE_FAILS}}</contingencies>
</phase>
</strategy-phases>

<risk-assessment>
<identified-risks>${{KEY_RISKS}}</identified-risks>
<mitigation-strategies>${{RISK_MITIGATION}}</mitigation-strategies>
</risk-assessment>

<resource-requirements>
<estimated-costs>${{COST_ESTIMATE}}</estimated-costs>
<required-evidence>${{EVIDENCE_NEEDED}}</required-evidence>
<expert-witnesses>${{EXPERTS_REQUIRED}}</expert-witnesses>
</resource-requirements>
</legal-strategy>
</output-format>

<error-handling>
<instruction>
If strategy inconsistency or obstacle detected:
1. Identify last viable state s_c
2. Analyse cause (procedural, evidential, legal)
3. Adjust strategy path:
   - Modify action sequence
   - Consider alternative legal routes
   - Assess settlement options
4. Update h(s_c) based on new information
5. Re-run A* search from s_c
</instruction>
</error-handling>

<sa-legal-requirements>
- Apply SA court procedure and rules
- Use SAFLII citation format
- Consider Constitutional Court precedent as binding
- Apply prescription periods (Prescription Act 68 of 1969)
- Consider court fee structures
- Account for SA legal profession rules
</sa-legal-requirements>
</q-star-legal-prompt>"""


def optimize_with_q_star(
    matter: str,
    stage: str = "Initial assessment",
    forum: str = "To be determined",
    key_issues: str = "As identified from matter",
    strengths: str = "To be analysed",
    weaknesses: str = "To be analysed",
    constraints: str = "Standard SA legal constraints"
) -> OptimizedPrompt:
    """
    Apply Q* (A* + Q-Learning) optimization for legal strategy.
    Best for complex multi-step litigation planning.
    """
    optimized = Q_STAR_LEGAL_TEMPLATE.format(
        matter=matter,
        stage=stage,
        forum=forum,
        key_issues=key_issues,
        strengths=strengths,
        weaknesses=weaknesses,
        constraints=constraints
    )
    
    return OptimizedPrompt(
        original=matter,
        optimized=optimized,
        mode=OptimizationMode.Q_STAR,
        enhancement_notes=[
            "Q* algorithm for optimal strategy paths",
            "A* search with Q-value heuristics",
            "Multi-phase strategy planning",
            "Contingency handling built-in",
            "Success probability estimation"
        ],
        sa_legal_adaptations=[
            "SA court procedure integration",
            "SAFLII citation format",
            "Constitutional Court binding precedent",
            "Prescription Act consideration",
            "SA legal profession rules"
        ],
        reasoning_structure="State → A* Search → Q-Value Estimation → Strategy Phases → Contingencies"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP3 NEW MODES: Microsoft MicrOptimization
# Automatic complexity enhancement for legal prompts
# ═══════════════════════════════════════════════════════════════════════════════

MICRO_OPT_LEGAL_TEMPLATE = """You are an expert SA legal prompt optimization specialist. Your task is to enhance the given legal prompt, making it more sophisticated, specific, and effective. Please follow these steps:

**ORIGINAL LEGAL PROMPT:**
{original_prompt}

**OPTIMIZATION PROTOCOL:**

1. **ANALYSE** the prompt carefully, identifying all key elements:
   - Role definition and expertise level
   - Legal issue or task specification
   - Jurisdictional context (SA-specific elements)
   - Constraints and requirements
   - Output format expectations

2. **ENHANCE COMPLEXITY** for each element by adding 30-50 words:
   - For role: Add specific qualifications, experience level, notable achievements
   - For legal issues: Add sub-issues, related considerations, edge cases
   - For context: Add procedural history, relevant timeline, stakeholder interests
   - For constraints: Add specific legal requirements, ethical considerations
   - For format: Add structural elements, quality standards, citation requirements

3. **SA LEGAL ENRICHMENT** - Add these elements if missing:
   - Constitutional framework reference (Bill of Rights, s36 analysis)
   - Specific SA legislation with Act numbers
   - Court hierarchy considerations
   - SAFLII citation format requirement
   - Ubuntu and transformative constitutionalism lens
   - Relevant SA case law references

4. **QUALITY ASSURANCE**:
   - Ensure internal consistency between all elements
   - Verify no contradictions with original intent
   - Confirm SA legal accuracy of added elements
   - Check that complexity enhances rather than obscures

5. **STRUCTURAL OPTIMIZATION**:
   - Add clear section markers
   - Include numbered workflow steps
   - Provide example format where helpful
   - Add verification checkpoints

**OUTPUT THE ENHANCED PROMPT:**
Provide only the optimized prompt without explanations. The enhanced prompt should:
- Be 150-200% longer than the original
- Maintain the original core objective
- Add substantive SA legal value
- Include quality control elements
- Be immediately usable for legal work"""


def optimize_with_micro_opt(
    original_prompt: str
) -> OptimizedPrompt:
    """
    Apply Microsoft MicrOptimization technique.
    Automatically enhances prompt complexity while maintaining coherence.
    """
    optimized = MICRO_OPT_LEGAL_TEMPLATE.format(
        original_prompt=original_prompt
    )
    
    return OptimizedPrompt(
        original=original_prompt,
        optimized=optimized,
        mode=OptimizationMode.MICRO_OPT,
        enhancement_notes=[
            "Microsoft MicrOptimization applied",
            "30-50 word enhancement per element",
            "Complexity enrichment with coherence",
            "SA legal elements automatically added",
            "Quality assurance steps included"
        ],
        sa_legal_adaptations=[
            "Constitutional framework integration",
            "SA legislation with Act numbers",
            "Court hierarchy awareness",
            "SAFLII citation format",
            "Ubuntu and transformative constitutionalism"
        ],
        reasoning_structure="Analyse → Enhance Complexity → SA Enrichment → Quality Check → Output"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP3 NEW MODES: OpenAI Official Optimization Method
# Based on OpenAI's official prompt generation guidelines
# ═══════════════════════════════════════════════════════════════════════════════

OPENAI_OFFICIAL_LEGAL_TEMPLATE = """Given this SA legal task description, produce a detailed system prompt to guide a language model in completing the task effectively.

**TASK/GOAL:**
{task}

**CONTEXT:**
{context}

# Guidelines for Prompt Generation

- **Understand the Task**: Grasp the main legal objective, requirements, constraints, and expected output.
- **SA Legal Context**: Embed South African jurisdictional requirements, court hierarchy, and citation standards.
- **Reasoning Before Conclusions**: Ensure analysis precedes conclusions. For legal matters: facts → law → application → conclusion.
- **Examples**: Include SA case law examples with SAFLII citations where helpful.
- **Clarity and Conciseness**: Use precise legal terminology while remaining accessible.
- **Output Format**: Specify exact format (opinion structure, heads of argument, etc.)

# Required Prompt Structure

**[Opening Instruction]**
Concise description of the legal task - this should be the first line.

**[SA Legal Context]**
- Jurisdiction: South Africa
- Applicable legal system
- Relevant courts and forums
- Key legislation (with Act numbers)
- Binding precedents

**[Detailed Requirements]**
- Specific analytical steps
- Citation standards (SAFLII format)
- Constitutional considerations
- Professional ethics requirements

# Steps
[Detailed breakdown of legal analysis methodology]

# Output Format
[Specific format: structure, length, citation style, sections required]

# Examples [if applicable]
[SA case examples with proper citations]
[Use [PLACEHOLDER] for complex variable elements]

# Notes
[Edge cases, important caveats, specific SA legal considerations]

---

**GENERATE THE OPTIMIZED LEGAL PROMPT:**"""


def optimize_with_openai_official(
    task: str,
    context: str = ""
) -> OptimizedPrompt:
    """
    Apply OpenAI's official prompt optimization methodology.
    Structured approach following OpenAI's guidelines.
    """
    optimized = OPENAI_OFFICIAL_LEGAL_TEMPLATE.format(
        task=task,
        context=context
    )
    
    return OptimizedPrompt(
        original=f"Task: {task}\nContext: {context}",
        optimized=optimized,
        mode=OptimizationMode.OPENAI_OFFICIAL,
        enhancement_notes=[
            "OpenAI official guidelines applied",
            "Reasoning-before-conclusions structure",
            "Example integration methodology",
            "Clear output format specification",
            "Structured prompt generation"
        ],
        sa_legal_adaptations=[
            "SA jurisdiction embedded",
            "Court hierarchy specified",
            "SAFLII citation standard",
            "Constitutional considerations",
            "Professional ethics requirements"
        ],
        reasoning_structure="Understand Task → Context → Requirements → Steps → Format → Examples → Notes"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP3 NEW MODES: SPO (Self-Play Optimization)
# From HKUST/DeepWisdom - uses Q&A examples for refinement
# ═══════════════════════════════════════════════════════════════════════════════

SPO_LEGAL_TEMPLATE = """You will apply Self-Play Optimization (SPO) to refine this legal prompt using Q&A examples.

**INITIAL LEGAL PROMPT:**
{initial_prompt}

**Q&A EXAMPLES FOR OPTIMIZATION:**
{qa_examples}

**SPO OPTIMIZATION PROTOCOL:**

## Phase 1: Baseline Evaluation
Analyse the initial prompt against the Q&A examples:
- Does the prompt guide towards correct answers?
- What patterns emerge from the examples?
- Where does the prompt fail to elicit proper responses?

## Phase 2: Self-Play Iteration 1
1. Generate response using current prompt
2. Compare against expected answers
3. Identify gaps between generated and expected
4. Formulate specific improvements

## Phase 3: Self-Play Iteration 2
1. Apply improvements from Iteration 1
2. Test against Q&A examples again
3. Measure improvement in alignment
4. Refine further based on remaining gaps

## Phase 4: Self-Play Iteration 3
1. Final refinement pass
2. Ensure all Q&A patterns are addressed
3. Validate consistency across examples
4. Lock in optimal prompt structure

## Phase 5: Finalization
Output the optimized prompt that:
- Consistently produces expected answer patterns
- Maintains SA legal accuracy
- Includes necessary context from Q&A learning
- Has clear structure and instructions

**SA LEGAL OPTIMIZATION REQUIREMENTS:**
- SAFLII neutral citation format for all cases
- Constitutional Court methodology application
- Ubuntu and transformative constitutionalism
- Proper Act references (Title XX of YYYY)
- Court hierarchy awareness

**OUTPUT:**
Provide the SPO-optimized legal prompt after 3 self-play iterations."""


def optimize_with_spo(
    initial_prompt: str,
    qa_examples: str = "No specific Q&A examples provided - use general SA legal standards."
) -> OptimizedPrompt:
    """
    Apply SPO (Self-Play Optimization) technique.
    Uses Q&A examples to iteratively refine the prompt.
    """
    optimized = SPO_LEGAL_TEMPLATE.format(
        initial_prompt=initial_prompt,
        qa_examples=qa_examples
    )
    
    return OptimizedPrompt(
        original=initial_prompt,
        optimized=optimized,
        mode=OptimizationMode.SPO_SELF_PLAY,
        enhancement_notes=[
            "Self-Play Optimization (HKUST/DeepWisdom)",
            "3 self-play iterations",
            "Q&A example-based refinement",
            "Gap analysis and correction",
            "Pattern-based optimization"
        ],
        sa_legal_adaptations=[
            "SAFLII citation format",
            "Constitutional Court methodology",
            "Ubuntu/transformative constitutionalism",
            "Proper Act references",
            "Court hierarchy awareness"
        ],
        reasoning_structure="Baseline → Self-Play x3 → Finalization"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP3 NEW MODES: Guided Step-by-Step Optimization
# Interactive guided optimization with progress tracking
# ═══════════════════════════════════════════════════════════════════════════════

GUIDED_COMPLETE_TEMPLATE = """You are an expert SA legal prompt engineer. Enhance and optimize the legal prompt based on user input through guided steps.

**CURRENT PROMPT VERSION:**
{current_prompt}

**USER'S OPTIMIZATION GOAL:**
{optimization_goal}

You must respond ONLY in this JSON format:
{{
    "comment": "<Analysis of current prompt version - identify strengths and weaknesses>",
    "current": "<Updated version of the prompt incorporating improvements>",
    "topic": "<The specific aspect being enhanced in this step>",
    "options": [
        "<Option 1: Specific, actionable improvement suggestion>",
        "<Option 2: Alternative specific improvement>",
        "<Option 3: Another concrete enhancement option>",
        "<Option 4: Different approach to improvement>"
    ],
    "progress": <0-100 integer indicating optimization completeness>
}}

**OPTIMIZATION FOCUS AREAS (work through systematically):**

1. **Role Definition (0-15%)**: Define clear SA legal persona with expertise level
2. **Task Specification (15-30%)**: Clear, actionable legal task with scope
3. **Context Enhancement (30-45%)**: SA jurisdictional context, applicable law
4. **Constraints & Requirements (45-60%)**: Citation format, ethics, standards
5. **Output Format (60-75%)**: Structure, length, sections, quality criteria
6. **Examples & Precedents (75-90%)**: SA case references, format samples
7. **Final Polish (90-100%)**: Consistency check, SA legal accuracy verification

**SA LEGAL REQUIREMENTS FOR ALL OPTIONS:**
- SAFLII neutral citation format
- Constitutional values integration
- Ubuntu and transformative constitutionalism
- Proper legislation references
- Court hierarchy considerations

**OPTION REQUIREMENTS:**
- Each option must be specific and immediately actionable
- Options should represent genuinely different approaches
- Avoid vague suggestions like "add more detail"
- Include SA-specific enhancements where relevant

When progress reaches 100, return empty options array and provide final optimized prompt in "current" field.

**REMEMBER:** Your task is to optimize the legal prompt, NOT to execute its instructions."""


@dataclass
class GuidedOptimizationResult:
    """Result from guided optimization step"""
    comment: str
    current: str
    topic: str
    options: List[str]
    progress: int


def optimize_with_guided_complete(
    current_prompt: str,
    optimization_goal: str = "Create an effective SA legal prompt"
) -> OptimizedPrompt:
    """
    Apply Guided Step-by-Step optimization.
    Returns structured guidance for interactive optimization.
    """
    optimized = GUIDED_COMPLETE_TEMPLATE.format(
        current_prompt=current_prompt,
        optimization_goal=optimization_goal
    )
    
    return OptimizedPrompt(
        original=current_prompt,
        optimized=optimized,
        mode=OptimizationMode.GUIDED_COMPLETE,
        enhancement_notes=[
            "Interactive guided optimization",
            "Progress tracking (0-100%)",
            "4 options per step",
            "7 focus areas covered",
            "JSON-structured responses"
        ],
        sa_legal_adaptations=[
            "SA legal persona definition",
            "Jurisdictional context",
            "SAFLII citation format",
            "Constitutional values",
            "Ubuntu integration"
        ],
        reasoning_structure="Role → Task → Context → Constraints → Format → Examples → Polish"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP2 NEW: PROMPT COMPARISON (MULTI-MODE)
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class PromptComparison:
    """Container for comparing multiple optimization modes on the same prompt"""
    original: str
    comparisons: Dict[OptimizationMode, OptimizedPrompt]
    recommended_mode: OptimizationMode
    recommendation_reason: str


def compare_optimization_modes(
    prompt_components: Dict[str, str],
    modes_to_compare: Optional[List[OptimizationMode]] = None,
    output_format: LegalOutputFormat = LegalOutputFormat.LEGAL_OPINION
) -> PromptComparison:
    """
    Compare the same prompt optimized with multiple modes.
    Returns all versions with a recommendation.
    """
    if modes_to_compare is None:
        modes_to_compare = [
            OptimizationMode.CRISPE,
            OptimizationMode.CO_STAR,
            OptimizationMode.CHAIN_OF_THOUGHT,
            OptimizationMode.HYBRID_LEGAL
        ]
    
    comparisons = {}
    best_mode = OptimizationMode.STANDARD
    best_score = 0
    
    for mode in modes_to_compare:
        result = optimize_legal_prompt(
            prompt_components=prompt_components,
            mode=mode,
            output_format=output_format
        )
        comparisons[mode] = result
        
        # Score based on quality and mode characteristics
        mode_score = result.quality_score
        if mode == OptimizationMode.CHAIN_OF_THOUGHT:
            mode_score += 5  # Bonus for reasoning transparency
        if mode == OptimizationMode.HYBRID_LEGAL:
            mode_score += 3  # Bonus for comprehensive enhancement
        
        if mode_score > best_score:
            best_score = mode_score
            best_mode = mode
    
    # Generate recommendation reason
    reasons = {
        OptimizationMode.CRISPE: "Best for structured professional outputs with clear role definition",
        OptimizationMode.CO_STAR: "Best for client-facing documents with audience consideration",
        OptimizationMode.CHAIN_OF_THOUGHT: "Best for complex analysis requiring transparent reasoning",
        OptimizationMode.HYBRID_LEGAL: "Best for high-stakes matters requiring maximum enhancement",
        OptimizationMode.RISE: "Best for iterative refinement of complex matters",
        OptimizationMode.O1_STYLE: "Best for methodical step-by-step analysis",
        OptimizationMode.EXPERT_WITNESS: "Best for technical expert opinions",
        OptimizationMode.MEDIATION_ADR: "Best for dispute resolution contexts",
        OptimizationMode.COMPLIANCE_AUDIT: "Best for regulatory compliance reviews"
    }
    
    original_text = "\n".join(f"{k}: {v}" for k, v in prompt_components.items() if v)
    
    return PromptComparison(
        original=original_text,
        comparisons=comparisons,
        recommended_mode=best_mode,
        recommendation_reason=reasons.get(best_mode, "Selected based on quality score")
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP2 NEW: BATCH OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class BatchResult:
    """Container for batch optimization results"""
    total_prompts: int
    successful: int
    failed: int
    results: List[OptimizedPrompt]
    errors: List[str]


def batch_optimize_prompts(
    prompts: List[Dict[str, str]],
    mode: OptimizationMode = OptimizationMode.CRISPE,
    output_format: LegalOutputFormat = LegalOutputFormat.LEGAL_OPINION
) -> BatchResult:
    """
    Optimize multiple prompts with the same settings.
    Useful for processing multiple matters consistently.
    """
    results = []
    errors = []
    
    for i, prompt_components in enumerate(prompts):
        try:
            result = optimize_legal_prompt(
                prompt_components=prompt_components,
                mode=mode,
                output_format=output_format
            )
            results.append(result)
        except Exception as e:
            errors.append(f"Prompt {i + 1}: {str(e)}")
    
    return BatchResult(
        total_prompts=len(prompts),
        successful=len(results),
        failed=len(errors),
        results=results,
        errors=errors
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP2 NEW: EXPORT FORMATS
# ═══════════════════════════════════════════════════════════════════════════════

def export_prompt_to_json(prompt: OptimizedPrompt) -> str:
    """Export optimized prompt to JSON format"""
    export_data = {
        "version": "4.2.0",
        "export_timestamp": datetime.datetime.now().isoformat(),
        "original_prompt": prompt.original,
        "optimized_prompt": prompt.optimized,
        "optimization_mode": prompt.mode.value,
        "quality_score": prompt.quality_score,
        "token_estimate": prompt.token_estimate,
        "practice_area": prompt.practice_area,
        "enhancement_notes": prompt.enhancement_notes,
        "sa_legal_adaptations": prompt.sa_legal_adaptations,
        "reasoning_structure": prompt.reasoning_structure
    }
    
    return json.dumps(export_data, indent=2, ensure_ascii=False)


def export_prompt_to_markdown(prompt: OptimizedPrompt) -> str:
    """Export optimized prompt to Markdown format"""
    md = f"""# Optimized Legal Prompt

## Metadata
- **Optimization Mode:** {prompt.mode.value}
- **Quality Score:** {prompt.quality_score}/100
- **Token Estimate:** ~{prompt.token_estimate}
- **Practice Area:** {prompt.practice_area or 'Not specified'}

## Original Prompt
```
{prompt.original}
```

## Optimized Prompt
```
{prompt.optimized}
```

## Enhancement Details

### Enhancements Applied
{chr(10).join(f"- {note}" for note in prompt.enhancement_notes)}

### SA Legal Adaptations
{chr(10).join(f"- {adaptation}" for adaptation in prompt.sa_legal_adaptations)}

### Reasoning Structure
{prompt.reasoning_structure or 'Standard flow'}

---
*Generated by SA Legal Prompting Elite v4.2.0*
"""
    return md


# ═══════════════════════════════════════════════════════════════════════════════
# SP2 NEW: ENHANCED QUALITY SCORING WITH SUB-SCORES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class QualityScoreDetails:
    """Detailed quality scoring breakdown"""
    overall_score: float
    clarity_score: float
    specificity_score: float
    sa_context_score: float
    structure_score: float
    suggestions: List[str]
    strengths: List[str]


def calculate_detailed_quality_score(
    prompt: str,
    components: Dict[str, str]
) -> QualityScoreDetails:
    """
    Calculate detailed quality scores with sub-dimensions.
    Returns breakdown of clarity, specificity, SA-context, and structure.
    """
    suggestions = []
    strengths = []
    
    # Clarity Score (0-25): How clear and unambiguous is the prompt?
    clarity_score = 0.0
    if components.get('task'):
        task_len = len(components['task'])
        if task_len > 50:
            clarity_score += 15
            strengths.append("Clear task definition")
        elif task_len > 20:
            clarity_score += 8
            suggestions.append("Expand task description for more clarity")
        else:
            suggestions.append("Task needs more detail for clarity")
    
    # Check for clear action verbs
    task_text = components.get('task', '').lower()
    action_verbs = ['analyse', 'analyze', 'draft', 'review', 'advise', 'research', 'compare', 'identify']
    if any(verb in task_text for verb in action_verbs):
        clarity_score += 10
        strengths.append("Uses clear action verbs")
    else:
        suggestions.append("Add clear action verbs (analyse, draft, review, etc.)")
    
    # Specificity Score (0-25): How specific and detailed?
    specificity_score = 0.0
    
    # Check for specific legal references
    prompt_lower = prompt.lower()
    if any(word in prompt_lower for word in ['act', 'section', 'regulation', 'rule']):
        specificity_score += 8
        strengths.append("References specific legislation")
    else:
        suggestions.append("Reference specific legislation (e.g., 'Section X of Act Y')")
    
    # Check for case names
    if ' v ' in prompt or 'case' in prompt_lower:
        specificity_score += 7
        strengths.append("Includes case references")
    else:
        suggestions.append("Consider referencing relevant case law")
    
    # Check for named parties/entities
    if components.get('context') and len(components['context']) > 100:
        specificity_score += 10
        strengths.append("Detailed context provided")
    elif components.get('context'):
        specificity_score += 5
        suggestions.append("Add more specific details to context")
    else:
        suggestions.append("Provide specific factual context")
    
    # SA Context Score (0-25): SA legal system integration
    sa_context_score = 0.0
    
    sa_indicators = {
        'saflii': 5,
        'constitutional court': 5,
        'supreme court of appeal': 4,
        'sca': 3,
        'high court': 3,
        'labour court': 3,
        'ccma': 3,
        'ubuntu': 4,
        'constitution': 4,
        'bill of rights': 4,
        'section 36': 4,
        'transformative': 3
    }
    
    for indicator, points in sa_indicators.items():
        if indicator in prompt_lower:
            sa_context_score += points
    
    sa_context_score = min(sa_context_score, 25)
    
    if sa_context_score >= 15:
        strengths.append("Strong SA legal context integration")
    elif sa_context_score >= 8:
        suggestions.append("Add more SA-specific references (courts, legislation)")
    else:
        suggestions.append("Include SA legal context (SAFLII, court names, relevant Acts)")
    
    # Structure Score (0-25): Prompt organization and format
    structure_score = 0.0
    
    # Check for role definition
    if components.get('role') and len(components['role']) > 30:
        structure_score += 7
        strengths.append("Clear role/persona defined")
    elif components.get('role'):
        structure_score += 3
        suggestions.append("Expand role definition with expertise details")
    else:
        suggestions.append("Add role/persona definition")
    
    # Check for constraints
    if components.get('constraints'):
        structure_score += 6
        strengths.append("Constraints specified")
    else:
        suggestions.append("Add constraints/limitations for focused output")
    
    # Check for output format
    if components.get('output_format'):
        structure_score += 6
        strengths.append("Output format specified")
    else:
        suggestions.append("Specify desired output format")
    
    # Check for examples
    if components.get('examples'):
        structure_score += 6
        strengths.append("Examples/precedents included")
    else:
        suggestions.append("Add examples or reference cases")
    
    # Calculate overall score
    overall_score = clarity_score + specificity_score + sa_context_score + structure_score
    
    return QualityScoreDetails(
        overall_score=min(overall_score, 100),
        clarity_score=clarity_score,
        specificity_score=specificity_score,
        sa_context_score=sa_context_score,
        structure_score=structure_score,
        suggestions=suggestions[:5],  # Top 5 suggestions
        strengths=strengths[:5]  # Top 5 strengths
    )


# ═══════════════════════════════════════════════════════════════════════════════
# SP2 NEW: QUICK PROMPT TEMPLATES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class QuickTemplate:
    """Quick-use prompt template"""
    name: str
    category: str
    description: str
    components: Dict[str, str]
    recommended_mode: OptimizationMode
    popularity: int  # Usage count


QUICK_TEMPLATES: List[QuickTemplate] = [
    QuickTemplate(
        name="Constitutional Rights Analysis",
        category="Constitutional",
        description="Analyse fundamental rights and limitations under the Bill of Rights",
        components={
            "role": "You are a Senior Constitutional Law Specialist with extensive experience before the Constitutional Court of South Africa.",
            "context": "A matter involving alleged infringement of fundamental rights under Chapter 2 of the Constitution.",
            "task": "Analyse the constitutional validity of the challenged provision/conduct, applying the section 36 limitations analysis.",
            "constraints": "Use SAFLII citation format. Reference Constitutional Court methodology.",
            "output_format": "1. Right(s) Implicated\n2. Nature of Limitation\n3. Section 36 Analysis\n4. Proportionality Assessment\n5. Conclusion",
            "examples": "Apply the analytical approach from Harksen v Lane NO and S v Makwanyane."
        },
        recommended_mode=OptimizationMode.CHAIN_OF_THOUGHT,
        popularity=342
    ),
    QuickTemplate(
        name="Unfair Dismissal Opinion",
        category="Labour",
        description="Analyse dismissal for substantive and procedural fairness under LRA",
        components={
            "role": "You are an experienced Labour Law Practitioner with expertise in unfair dismissal matters before the CCMA and Labour Court.",
            "context": "An employee was dismissed and seeks to challenge the fairness of the dismissal.",
            "task": "Analyse both substantive fairness (valid reason) and procedural fairness (fair procedure) of the dismissal under the Labour Relations Act 66 of 1995.",
            "constraints": "Consider items 4 and 7 of Schedule 8 (Code of Good Practice). Reference applicable bargaining council agreements.",
            "output_format": "1. Reason for Dismissal\n2. Substantive Fairness Analysis\n3. Procedural Fairness Analysis\n4. Likely CCMA/Labour Court Outcome\n5. Remedies Available",
            "examples": "Reference Sidumo v Rustenburg Platinum Mines for the review standard."
        },
        recommended_mode=OptimizationMode.CRISPE,
        popularity=287
    ),
    QuickTemplate(
        name="Contract Review Checklist",
        category="Commercial",
        description="Comprehensive commercial contract review with risk identification",
        components={
            "role": "You are a Commercial Law Attorney specialising in contract drafting and review for South African businesses.",
            "context": "A client has asked you to review a commercial contract before signing.",
            "task": "Review the contract terms, identify risks, flag unusual clauses, and provide negotiation recommendations.",
            "constraints": "Consider Consumer Protection Act implications if applicable. Check for competition law concerns.",
            "output_format": "1. Key Commercial Terms Summary\n2. Risk Register (High/Medium/Low)\n3. Unusual or Onerous Clauses\n4. Missing Protections\n5. Negotiation Recommendations",
            "examples": ""
        },
        recommended_mode=OptimizationMode.CO_STAR,
        popularity=215
    ),
    QuickTemplate(
        name="Criminal Bail Application",
        category="Criminal",
        description="Prepare bail application arguments under Criminal Procedure Act",
        components={
            "role": "You are a Criminal Defence Advocate with extensive experience in bail applications before the High Court and Magistrates' Courts.",
            "context": "An accused person is applying for bail after arrest on serious charges.",
            "task": "Prepare arguments for bail considering Schedule 5/6 requirements, interests of justice factors, and constitutional right to freedom.",
            "constraints": "Apply S v Dlamini approach. Address State's likely opposition grounds.",
            "output_format": "1. Charge and Schedule Classification\n2. Applicant's Personal Circumstances\n3. Interests of Justice Factors\n4. Addressing State Opposition\n5. Proposed Bail Conditions",
            "examples": ""
        },
        recommended_mode=OptimizationMode.HYBRID_LEGAL,
        popularity=198
    ),
    QuickTemplate(
        name="POPIA Compliance Assessment",
        category="Compliance",
        description="Data protection compliance review under POPIA",
        components={
            "role": "You are a Data Protection and Information Law Specialist with expertise in POPIA compliance for South African organisations.",
            "context": "An organisation processes personal information and requires assessment of POPIA compliance status.",
            "task": "Assess the organisation's compliance with the Protection of Personal Information Act 4 of 2013 and identify gaps requiring remediation.",
            "constraints": "Consider all 8 conditions for lawful processing. Reference Information Regulator guidance.",
            "output_format": "1. Processing Activities Overview\n2. Condition-by-Condition Assessment\n3. Data Subject Rights Compliance\n4. Security Safeguards Review\n5. Gap Analysis and Recommendations",
            "examples": ""
        },
        recommended_mode=OptimizationMode.COMPLIANCE_AUDIT,
        popularity=176
    ),
    QuickTemplate(
        name="Divorce Settlement Analysis",
        category="Family",
        description="Analyse matrimonial property and maintenance in divorce",
        components={
            "role": "You are a Family Law Attorney specialising in divorce and matrimonial property matters in South Africa.",
            "context": "A client is contemplating or proceeding with divorce and needs advice on likely property division and maintenance outcomes.",
            "task": "Analyse the matrimonial property regime, likely asset division, and maintenance considerations including spousal and child maintenance.",
            "constraints": "Consider Matrimonial Property Act 88 of 1984, Divorce Act 70 of 1979, and relevant case law.",
            "output_format": "1. Matrimonial Property Regime\n2. Asset Division Analysis\n3. Spousal Maintenance Factors\n4. Child Maintenance/Best Interests\n5. Settlement Recommendations",
            "examples": ""
        },
        recommended_mode=OptimizationMode.CO_STAR,
        popularity=154
    ),
    # SP3 New Templates (from 302 Prompt Expert patterns)
    QuickTemplate(
        name="Eviction Analysis (PIE)",
        category="Property",
        description="Analyse eviction requirements under Prevention of Illegal Eviction Act",
        components={
            "role": "You are a Property Law Specialist with expertise in eviction proceedings and informal settlement matters.",
            "context": "A property owner or occupier requires analysis of eviction rights and obligations under PIE.",
            "task": "Analyse the eviction under the Prevention of Illegal Eviction from and Unlawful Occupation of Land Act 19 of 1998, considering section 26 Constitutional rights.",
            "constraints": "Apply the meaningful engagement requirements from Occupiers of 51 Olivia Road. Consider alternative accommodation duties.",
            "output_format": "1. Occupier Classification\n2. PIE Requirements Analysis\n3. Constitutional Considerations\n4. Meaningful Engagement Status\n5. Strategic Recommendations",
            "examples": "Reference Port Elizabeth Municipality v Various Occupiers, City of Johannesburg v Changing Tides."
        },
        recommended_mode=OptimizationMode.VARI_PLANNING,
        popularity=132
    ),
    QuickTemplate(
        name="Restraint of Trade Analysis",
        category="Commercial",
        description="Evaluate validity and enforceability of restraint of trade clauses",
        components={
            "role": "You are a Commercial and Employment Law Specialist with expertise in restraint of trade matters.",
            "context": "A client requires analysis of a restraint of trade clause for enforcement or defence purposes.",
            "task": "Analyse the validity and enforceability of the restraint applying the Magna Alloys/Basson v Chilwan test and Constitutional considerations.",
            "constraints": "Apply reasonableness factors: interest protected, duration, geographical scope, and balance against section 22 right to work.",
            "output_format": "1. Restraint Terms Summary\n2. Protected Interest Analysis\n3. Reasonableness Assessment\n4. Constitutional Balancing\n5. Enforcement Recommendation",
            "examples": "Apply Reddy v Siemens approach to Constitutional balancing."
        },
        recommended_mode=OptimizationMode.Q_STAR,
        popularity=145
    ),
    QuickTemplate(
        name="BEE Compliance Review",
        category="Compliance",
        description="Broad-Based Black Economic Empowerment scorecard analysis",
        components={
            "role": "You are a BEE Verification and Compliance Specialist with expertise in the B-BBEE codes of good practice.",
            "context": "An entity requires assessment of B-BBEE compliance and scorecard optimisation strategy.",
            "task": "Review current B-BBEE status, analyse scorecard elements, and provide compliance improvement recommendations.",
            "constraints": "Consider B-BBEE Act 53 of 2003 (as amended), applicable sector codes, and DTI guidelines.",
            "output_format": "1. Current B-BBEE Level\n2. Scorecard Element Analysis\n3. Gap Identification\n4. Improvement Opportunities\n5. Verification Preparation",
            "examples": ""
        },
        recommended_mode=OptimizationMode.COMPLIANCE_AUDIT,
        popularity=98
    ),
    QuickTemplate(
        name="Competition Law Assessment",
        category="Commercial",
        description="Merger control and prohibited practice analysis",
        components={
            "role": "You are a Competition Law Specialist with expertise in merger notifications and prohibited practices.",
            "context": "A transaction or conduct requires assessment under the Competition Act.",
            "task": "Analyse competition law implications including merger thresholds, market definition, and potential concerns.",
            "constraints": "Apply Competition Act 89 of 1998, Competition Commission guidelines, and Tribunal precedent.",
            "output_format": "1. Conduct/Transaction Classification\n2. Market Definition\n3. Competition Concerns Analysis\n4. Notification/Filing Requirements\n5. Remedies/Conditions Likely",
            "examples": ""
        },
        recommended_mode=OptimizationMode.CHAIN_OF_THOUGHT,
        popularity=87
    ),
    QuickTemplate(
        name="Administrative Law Review",
        category="Administrative",
        description="PAJA review grounds and procedural fairness analysis",
        components={
            "role": "You are an Administrative Law Specialist with expertise in judicial review and PAJA applications.",
            "context": "A client challenges or defends administrative action under PAJA.",
            "task": "Analyse the administrative action for grounds of review under the Promotion of Administrative Justice Act 3 of 2000.",
            "constraints": "Consider s6 review grounds systematically. Apply Bato Star rationality standard.",
            "output_format": "1. Administrative Action Identified\n2. Standing and Exhaustion Analysis\n3. Review Grounds Assessment\n4. Procedural Fairness Analysis\n5. Remedy Recommendations",
            "examples": "Reference Pharmaceutical Manufacturers Association, Grey's Marine."
        },
        recommended_mode=OptimizationMode.RISE,
        popularity=112
    ),
    QuickTemplate(
        name="Intellectual Property Strategy",
        category="IP",
        description="IP portfolio review and protection strategy",
        components={
            "role": "You are an Intellectual Property Specialist with expertise in trademarks, patents, and copyright in South Africa.",
            "context": "A client requires comprehensive IP strategy advice including protection and enforcement.",
            "task": "Analyse IP assets, identify protection gaps, and recommend comprehensive IP strategy.",
            "constraints": "Consider Trade Marks Act 194 of 1993, Patents Act 57 of 1978, Copyright Act 98 of 1978, and common law protection.",
            "output_format": "1. IP Asset Audit\n2. Protection Status Review\n3. Gap Analysis\n4. Enforcement Considerations\n5. Strategic Recommendations",
            "examples": ""
        },
        recommended_mode=OptimizationMode.MICRO_OPT,
        popularity=76
    ),
    QuickTemplate(
        name="Tax Dispute Resolution",
        category="Tax",
        description="SARS dispute procedures and objection/appeal strategy",
        components={
            "role": "You are a Tax Dispute Resolution Specialist with expertise in SARS objections, appeals, and Tax Court proceedings.",
            "context": "A taxpayer disputes a SARS assessment or decision and requires strategic advice.",
            "task": "Analyse the dispute, evaluate merits, and develop resolution strategy under Tax Administration Act procedures.",
            "constraints": "Apply Tax Administration Act 28 of 2011, ADR rules, and Tax Court procedural requirements.",
            "output_format": "1. Assessment/Decision Summary\n2. Grounds for Dispute\n3. Procedural Pathway Analysis\n4. Alternative Dispute Resolution Options\n5. Strategic Recommendations",
            "examples": ""
        },
        recommended_mode=OptimizationMode.Q_STAR,
        popularity=94
    ),
    QuickTemplate(
        name="Environmental Authorisation",
        category="Environmental",
        description="NEMA environmental impact assessment requirements",
        components={
            "role": "You are an Environmental Law Specialist with expertise in NEMA authorisations and impact assessments.",
            "context": "A project or activity requires environmental compliance assessment.",
            "task": "Analyse environmental authorisation requirements under NEMA and identify applicable listed activities.",
            "constraints": "Consider NEMA 107 of 1998, EIA Regulations, and relevant provincial legislation.",
            "output_format": "1. Activity Classification\n2. Listed Activities Triggered\n3. Assessment Process Required\n4. Public Participation Requirements\n5. Authorisation Strategy",
            "examples": ""
        },
        recommended_mode=OptimizationMode.GUIDED_COMPLETE,
        popularity=68
    ),
    QuickTemplate(
        name="Construction Dispute Analysis",
        category="Commercial",
        description="Construction contract claims and dispute resolution",
        components={
            "role": "You are a Construction Law Specialist with expertise in NEC, JBCC, and FIDIC contracts.",
            "context": "A construction contract dispute requires analysis and resolution strategy.",
            "task": "Analyse the construction dispute, identify contractual remedies, and recommend dispute resolution pathway.",
            "constraints": "Consider applicable contract form (NEC/JBCC/FIDIC), Construction Industry Development Board Act, and adjudication procedures.",
            "output_format": "1. Contract Form and Key Provisions\n2. Claim Analysis\n3. Defences Available\n4. Dispute Resolution Mechanism\n5. Strategic Recommendations",
            "examples": ""
        },
        recommended_mode=OptimizationMode.O1_STYLE,
        popularity=82
    ),
    QuickTemplate(
        name="Immigration Permit Strategy",
        category="Immigration",
        description="Work permit and visa application strategy",
        components={
            "role": "You are an Immigration Law Specialist with expertise in work permits, visas, and permanent residence applications.",
            "context": "A client requires immigration status regularisation or permit application strategy.",
            "task": "Analyse immigration status, identify appropriate permit category, and develop application strategy.",
            "constraints": "Consider Immigration Act 13 of 2002, DHA directives, and recent policy changes.",
            "output_format": "1. Current Status Assessment\n2. Permit Category Options\n3. Application Requirements\n4. Risk Factors\n5. Strategic Recommendations",
            "examples": ""
        },
        recommended_mode=OptimizationMode.SPO_SELF_PLAY,
        popularity=89
    )
]


def get_quick_templates() -> List[QuickTemplate]:
    """Get all available quick templates"""
    return QUICK_TEMPLATES


def get_template_by_name(name: str) -> Optional[QuickTemplate]:
    """Get a specific template by name"""
    for template in QUICK_TEMPLATES:
        if template.name.lower() == name.lower():
            return template
    return None


def get_templates_by_category(category: str) -> List[QuickTemplate]:
    """Get all templates in a category"""
    return [t for t in QUICK_TEMPLATES if t.category.lower() == category.lower()]


# ═══════════════════════════════════════════════════════════════════════════════
# PROMPT QUALITY SCORING (NEW SP1)
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_prompt_quality_score(prompt: str, components: Dict[str, str]) -> Tuple[float, List[str]]:
    """
    Calculate a quality score for a prompt and return improvement suggestions.
    Score is 0-100.
    """
    score = 0.0
    suggestions = []
    
    # Check for role definition (15 points)
    if components.get('role') and len(components['role']) > 20:
        score += 15
    elif components.get('role'):
        score += 7
        suggestions.append("Expand role definition with more specificity")
    else:
        suggestions.append("Add a clear role/persona definition")
    
    # Check for context (20 points)
    if components.get('context') and len(components['context']) > 50:
        score += 20
    elif components.get('context'):
        score += 10
        suggestions.append("Provide more detailed context")
    else:
        suggestions.append("Add background context for better results")
    
    # Check for task clarity (20 points)
    if components.get('task') and len(components['task']) > 30:
        score += 20
    elif components.get('task'):
        score += 10
        suggestions.append("Make task instructions more specific")
    else:
        suggestions.append("Define clear task instructions")
    
    # Check for constraints (10 points)
    if components.get('constraints'):
        score += 10
    else:
        suggestions.append("Consider adding constraints/limitations")
    
    # Check for output format (10 points)
    if components.get('output_format'):
        score += 10
    else:
        suggestions.append("Specify desired output format")
    
    # Check for examples (10 points)
    if components.get('examples'):
        score += 10
    else:
        suggestions.append("Add examples or precedents for better output")
    
    # Check for SA legal elements in prompt text (15 points)
    prompt_lower = prompt.lower()
    sa_elements = 0
    
    if 'saflii' in prompt_lower or 'citation' in prompt_lower:
        sa_elements += 3
    if 'constitutional' in prompt_lower or 'constitution' in prompt_lower:
        sa_elements += 3
    if 'ubuntu' in prompt_lower:
        sa_elements += 3
    if 'act' in prompt_lower and any(str(year) in prompt for year in range(1990, 2030)):
        sa_elements += 3
    if any(court in prompt_lower for court in ['constitutional court', 'sca', 'high court', 'labour court']):
        sa_elements += 3
    
    score += min(sa_elements, 15)
    
    if sa_elements < 6:
        suggestions.append("Add more SA-specific legal context (courts, legislation, citation format)")
    
    return min(score, 100), suggestions


def estimate_token_count(text: str) -> int:
    """Rough estimate of token count (approx 4 chars per token)"""
    return len(text) // 4


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN OPTIMIZATION FUNCTION
# ═══════════════════════════════════════════════════════════════════════════════

def optimize_legal_prompt(
    prompt_components: Dict[str, str],
    mode: OptimizationMode = OptimizationMode.STANDARD,
    output_format: LegalOutputFormat = LegalOutputFormat.LEGAL_OPINION,
    use_preset: Optional[PracticeAreaPreset] = None
) -> OptimizedPrompt:
    """
    Main function to optimize legal prompts using selected mode.
    
    Args:
        prompt_components: Dict with keys like 'role', 'task', 'context', 'matter', etc.
        mode: The optimization technique to apply
        output_format: Desired legal output format
        
    Returns:
        OptimizedPrompt with enhanced version and metadata
    """
    
    # Extract components with defaults
    role = prompt_components.get('role', 'SA Legal Professional')
    task = prompt_components.get('task', prompt_components.get('instructions', ''))
    context = prompt_components.get('context', '')
    matter = prompt_components.get('matter', f"{context}\n\n{task}")
    constraints = prompt_components.get('constraints', '')
    examples = prompt_components.get('examples', '')
    
    # Apply selected optimization mode
    if mode == OptimizationMode.STANDARD:
        # No optimization - return structured but basic prompt
        basic_prompt = f"""**Role:** {role}

**Task:** {task}

**Context:** {context}

{f'**Constraints:** {constraints}' if constraints else ''}
{f'**Examples/Precedents:** {examples}' if examples else ''}

**Output Format:** {output_format.value}

Please provide your analysis following South African legal standards with SAFLII citations."""
        
        return OptimizedPrompt(
            original=basic_prompt,
            optimized=basic_prompt,
            mode=OptimizationMode.STANDARD,
            enhancement_notes=["Basic formatting applied"],
            sa_legal_adaptations=["SAFLII citation reminder added"]
        )
    
    elif mode == OptimizationMode.CRISPE:
        result = optimize_with_crispe(
            role=role,
            task=task,
            context=context,
            output_format=output_format.value,
            additional_constraints=constraints
        )
        # Add quality scoring
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.CO_STAR:
        result = optimize_with_co_star(
            context=context,
            objective=task,
            result=output_format.value
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.CHAIN_OF_THOUGHT:
        result = optimize_with_chain_of_thought(
            matter=matter,
            additional_instructions=f"Output Format: {output_format.value}\n{constraints}"
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.RISE:
        result = optimize_with_rise(
            matter=matter,
            additional_context=f"Required Output: {output_format.value}"
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.O1_STYLE:
        result = optimize_with_o1_style(
            matter=matter,
            additional_instructions=f"Target Output Format: {output_format.value}"
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.META_PROMPT:
        basic = f"Role: {role}\nTask: {task}\nContext: {context}"
        result = optimize_with_meta_prompt(basic)
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.HYBRID_LEGAL:
        result = optimize_with_hybrid_legal(
            role=role,
            task=task,
            context=context,
            output_format=output_format.value,
            additional_constraints=constraints
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.CLAUDE_STYLE:
        result = optimize_with_claude_style(
            task=task,
            context=context,
            output_format=output_format.value
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    # SP2 New Modes
    elif mode == OptimizationMode.EXPERT_WITNESS:
        result = optimize_with_expert_witness(
            matter=matter,
            field_of_expertise=role,
            additional_instructions=f"Output Format: {output_format.value}\n{constraints}"
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.MEDIATION_ADR:
        result = optimize_with_mediation_adr(
            dispute=matter,
            parties=prompt_components.get('parties', 'Party A and Party B'),
            process_type=prompt_components.get('process_type', 'Mediation'),
            additional_guidance=f"Output Format: {output_format.value}\n{constraints}"
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.COMPLIANCE_AUDIT:
        result = optimize_with_compliance_audit(
            organization=prompt_components.get('organization', 'The organization under review'),
            scope=task or context,
            regulations=prompt_components.get('regulations', 'Applicable SA legislation'),
            additional_requirements=f"Output Format: {output_format.value}\n{constraints}"
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    # SP3 New Modes (from 302 Prompt Expert)
    elif mode == OptimizationMode.VARI_PLANNING:
        result = optimize_with_vari_planning(
            matter=matter,
            task_type=prompt_components.get('task_type', 'Legal Analysis'),
            audience=prompt_components.get('audience', 'Legal professionals'),
            objective=task or "Comprehensive legal analysis",
            subject_matter=prompt_components.get('subject_matter', 'As identified'),
            constraints=constraints
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.Q_STAR:
        result = optimize_with_q_star(
            matter=matter,
            stage=prompt_components.get('stage', 'Initial assessment'),
            forum=prompt_components.get('forum', 'To be determined'),
            key_issues=prompt_components.get('key_issues', 'As identified'),
            strengths=prompt_components.get('strengths', 'To be analysed'),
            weaknesses=prompt_components.get('weaknesses', 'To be analysed'),
            constraints=constraints
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.MICRO_OPT:
        basic = f"Role: {role}\nTask: {task}\nContext: {context}\nConstraints: {constraints}"
        result = optimize_with_micro_opt(basic)
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.OPENAI_OFFICIAL:
        result = optimize_with_openai_official(
            task=task,
            context=context
        )
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.SPO_SELF_PLAY:
        basic = f"Role: {role}\nTask: {task}\nContext: {context}"
        qa_examples = prompt_components.get('qa_examples', 'No specific Q&A examples provided.')
        result = optimize_with_spo(basic, qa_examples)
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    elif mode == OptimizationMode.GUIDED_COMPLETE:
        basic = f"Role: {role}\nTask: {task}\nContext: {context}"
        goal = prompt_components.get('optimization_goal', 'Create an effective SA legal prompt')
        result = optimize_with_guided_complete(basic, goal)
        quality, _ = calculate_prompt_quality_score(result.optimized, prompt_components)
        result.quality_score = quality
        result.token_estimate = estimate_token_count(result.optimized)
        return result
    
    # Fallback
    return optimize_with_crispe(
        role=role,
        task=task,
        context=context,
        output_format=output_format.value
    )


def optimize_with_preset(
    prompt_components: Dict[str, str],
    preset: PracticeAreaPreset
) -> OptimizedPrompt:
    """
    Optimize a prompt using a practice area preset configuration.
    Automatically applies the recommended mode and format for the practice area.
    """
    config = get_preset_configuration(preset)
    
    # Enhance role with preset template if not provided
    if not prompt_components.get('role'):
        prompt_components = {**prompt_components, 'role': config.role_template}
    
    # Add key cases and legislation to context if helpful
    enhanced_context = prompt_components.get('context', '')
    if config.key_legislation:
        enhanced_context += f"\n\nRelevant Legislation: {', '.join(config.key_legislation[:2])}"
    if config.key_cases:
        enhanced_context += f"\nKey Precedents to consider: {', '.join(config.key_cases[:2])}"
    
    prompt_components = {**prompt_components, 'context': enhanced_context}
    
    # Add special considerations to constraints
    if config.special_considerations:
        existing_constraints = prompt_components.get('constraints', '')
        enhanced_constraints = existing_constraints + "\n" + "\n".join(f"- {c}" for c in config.special_considerations)
        prompt_components = {**prompt_components, 'constraints': enhanced_constraints}
    
    # Optimize with recommended mode
    result = optimize_legal_prompt(
        prompt_components=prompt_components,
        mode=config.recommended_mode,
        output_format=config.recommended_format
    )
    
    result.practice_area = config.name
    return result


def get_optimization_modes_for_ui() -> List[Dict[str, str]]:
    """Get list of optimization modes for UI display"""
    return [
        {
            "key": mode.name,
            "name": mode.value,
            "description": _get_mode_description(mode)
        }
        for mode in OptimizationMode
    ]


def get_presets_for_ui() -> List[Dict[str, str]]:
    """Get list of practice area presets for UI display"""
    return [
        {
            "key": preset.name,
            "name": preset.value,
            "recommended_mode": PRACTICE_PRESETS[preset].recommended_mode.value if preset in PRACTICE_PRESETS else "Standard"
        }
        for preset in PracticeAreaPreset
        if preset != PracticeAreaPreset.CUSTOM
    ]


def _get_mode_description(mode: OptimizationMode) -> str:
    """Get detailed description for each mode"""
    descriptions = {
        OptimizationMode.STANDARD: "Basic formatting with SA legal standards. No advanced optimization.",
        OptimizationMode.CRISPE: "Comprehensive system prompt with role, profile, goals, skills, constraints, and workflow. Best for complex professional outputs.",
        OptimizationMode.CO_STAR: "Audience-focused optimization with context, objective, style, tone, audience, and result specifications. Best for client-facing documents.",
        OptimizationMode.CHAIN_OF_THOUGHT: "Step-by-step legal reasoning with self-validation. Best for complex legal analysis requiring transparent reasoning.",
        OptimizationMode.RISE: "Recursive self-improvement with 3 automatic iterations. Best for high-stakes matters requiring refined analysis.",
        OptimizationMode.O1_STYLE: "Structured reasoning with step budgets and quality scoring. Best for matters requiring careful, methodical analysis.",
        OptimizationMode.META_PROMPT: "Prompt-about-prompt optimization. Use when you want AI to enhance your prompt structure.",
        OptimizationMode.HYBRID_LEGAL: "Maximum enhancement combining CRISPE structure with Chain of Thought reasoning. Best for complex high-stakes matters.",
        OptimizationMode.CLAUDE_STYLE: "Detailed task instructions with explicit rules and structured output. Best for complex tasks requiring precise guidance.",
        # SP2 New Modes
        OptimizationMode.EXPERT_WITNESS: "Expert witness report format compliant with Uniform Rules Rule 36(9). Best for technical court opinions.",
        OptimizationMode.MEDIATION_ADR: "5-phase ADR process structure with interest-based negotiation. Best for mediation prep and dispute resolution.",
        OptimizationMode.COMPLIANCE_AUDIT: "6-section regulatory compliance audit protocol. Best for POPIA, FICA, King IV, and general compliance reviews.",
        # SP3 New Modes (from 302 Prompt Expert)
        OptimizationMode.VARI_PLANNING: "DeepMind VARI framework with explicit reasoning and self-reflection. Best for complex strategic planning and legal analysis.",
        OptimizationMode.Q_STAR: "A* + Q-Learning hybrid for legal strategy optimisation. Best for litigation strategy and case pathway analysis.",
        OptimizationMode.MICRO_OPT: "Microsoft-style iterative micro-enhancements. Best for refining existing prompts to near-optimal quality.",
        OptimizationMode.OPENAI_OFFICIAL: "OpenAI official prompt engineering best practices. Best for balanced, well-structured legal prompts.",
        OptimizationMode.SPO_SELF_PLAY: "HKUST/DeepWisdom self-play optimization. Best for prompts requiring iterative AI refinement.",
        OptimizationMode.GUIDED_COMPLETE: "Step-by-step guided optimization with component checklist. Best for learning and understanding prompt construction."
    }
    return descriptions.get(mode, "")


# ═══════════════════════════════════════════════════════════════════════════════
# EXPORTS
# ═══════════════════════════════════════════════════════════════════════════════

__all__ = [
    # Enums
    'OptimizationMode',
    'LegalOutputFormat', 
    'PracticeAreaPreset',
    # Data classes
    'OptimizedPrompt',
    'PresetConfiguration',
    'PromptComparison',
    'BatchResult',
    'QualityScoreDetails',
    'QuickTemplate',
    'GuidedOptimizationResult',
    # Main functions
    'optimize_legal_prompt',
    'optimize_with_preset',
    # Individual optimizers
    'optimize_with_crispe',
    'optimize_with_co_star',
    'optimize_with_chain_of_thought',
    'optimize_with_rise',
    'optimize_with_o1_style',
    'optimize_with_meta_prompt',
    'optimize_with_hybrid_legal',
    'optimize_with_claude_style',
    # SP2 New Optimizers
    'optimize_with_expert_witness',
    'optimize_with_mediation_adr',
    'optimize_with_compliance_audit',
    # SP3 New Optimizers (from 302 Prompt Expert)
    'optimize_with_vari_planning',
    'optimize_with_q_star',
    'optimize_with_micro_opt',
    'optimize_with_openai_official',
    'optimize_with_spo',
    'optimize_with_guided_complete',
    # SP2 New Features
    'compare_optimization_modes',
    'batch_optimize_prompts',
    'export_prompt_to_json',
    'export_prompt_to_markdown',
    'calculate_detailed_quality_score',
    'get_quick_templates',
    'get_template_by_name',
    'get_templates_by_category',
    # Utility functions
    'get_optimization_modes_for_ui',
    'get_presets_for_ui',
    'get_preset_configuration',
    'detect_practice_area',
    'calculate_prompt_quality_score',
    'estimate_token_count'
]

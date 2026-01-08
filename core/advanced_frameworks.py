"""
🇿🇦 SA Legal Prompting Frameworks
World-Class Prompt Engineering Frameworks Adapted for South African Legal Practice
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional

class FrameworkCategory(Enum):
    """Categories of prompting frameworks"""
    STRUCTURAL = "Structural Frameworks"
    ITERATIVE = "Iterative Refinement"
    REASONING = "Legal Reasoning"
    VERIFICATION = "Verification & Safety"
    SPECIALIZED = "Specialized Legal"

class PracticeArea(Enum):
    """SA Legal Practice Areas"""
    CONSTITUTIONAL = "Constitutional Law"
    CRIMINAL = "Criminal Law"
    CIVIL = "Civil Litigation"
    COMMERCIAL = "Commercial & Corporate"
    LABOUR = "Labour & Employment"
    FAMILY = "Family Law"
    PROPERTY = "Property & Conveyancing"
    ADMINISTRATIVE = "Administrative Law"
    TAX = "Tax Law"
    INTELLECTUAL_PROPERTY = "Intellectual Property"
    IMMIGRATION = "Immigration Law"
    CONSUMER = "Consumer Protection"
    COMPETITION = "Competition Law"
    POPIA = "Data Protection & POPIA"
    ENVIRONMENTAL = "Environmental Law"

@dataclass
class PromptingFramework:
    """Advanced Prompting Framework for SA Legal Practice"""
    name: str
    acronym: str
    category: FrameworkCategory
    description: str
    components: List[Dict[str, str]]
    sa_adaptations: List[str]
    example_prompt: str
    best_for: List[str]
    difficulty: str  # Beginner, Intermediate, Advanced
    source: str

# ═══════════════════════════════════════════════════════════════════════════════
# STRUCTURAL FRAMEWORKS
# ═══════════════════════════════════════════════════════════════════════════════

RICE_FRAMEWORK = PromptingFramework(
    name="Role, Instructions, Context, Examples",
    acronym="RICE",
    category=FrameworkCategory.STRUCTURAL,
    description="Foundation framework structuring prompts with clear role definition, specific instructions, contextual information, and illustrative examples for consistent SA legal output.",
    components=[
        {
            "letter": "R",
            "component": "Role",
            "description": "Define the SA legal persona",
            "example": "You are a Senior Advocate SC at the Johannesburg Bar with 20 years of constitutional law experience, having appeared in the Constitutional Court multiple times."
        },
        {
            "letter": "I", 
            "component": "Instructions",
            "description": "Specific task directives",
            "example": "Analyse the constitutionality of this statutory provision under sections 9, 10, and 36 of the Constitution. Apply the Harksen v Lane rationality test and the limitations analysis."
        },
        {
            "letter": "C",
            "component": "Context",
            "description": "SA legal context and constraints",
            "example": "The client is challenging regulations promulgated under the Disaster Management Act during the COVID-19 pandemic. Previous challenges include De Beer v Minister of Cooperative Governance."
        },
        {
            "letter": "E",
            "component": "Examples",
            "description": "Sample outputs or precedents",
            "example": "Structure your analysis similar to the Constitutional Court's approach in Mistry v Interim Medical and Dental Council, addressing each right separately before conducting limitations analysis."
        }
    ],
    sa_adaptations=[
        "Specify SA court hierarchy (Constitutional Court, SCA, High Court divisions)",
        "Reference SAFLII neutral citation format",
        "Include ubuntu and transformative constitutionalism principles",
        "Reference relevant SA legislation by Act number",
        "Consider bilingual legal terminology (English/Afrikaans)"
    ],
    example_prompt="""[ROLE]
You are a Senior Counsel (SC) specialising in labour law with extensive CCMA and Labour Court experience.

[INSTRUCTIONS]
Analyse whether this dismissal qualifies as automatically unfair under section 187 of the Labour Relations Act 66 of 1995. Provide:
1. Identification of the applicable ground
2. Analysis of the onus of proof (Kroeger v Visual Marketing)
3. Recommended strategy for CCMA arbitration

[CONTEXT]
The employee was dismissed after participating in a protected strike under section 64. The employer claims operational requirements. The employee has 8 years service.

[EXAMPLES]
Reference the approach in NUMSA v Bader Bop for protected strike analysis and SACWU v Afrox for automatically unfair dismissal principles.""",
    best_for=["Complex legal analysis", "Structured opinions", "Court preparation"],
    difficulty="Intermediate",
    source="North Carolina Bar Association"
)

ABCDE_FRAMEWORK = PromptingFramework(
    name="Audience, Behaviour, Context, Details, Examples",
    acronym="ABCDE",
    category=FrameworkCategory.STRUCTURAL,
    description="Comprehensive framework emphasizing audience awareness crucial for SA legal practice where documents serve multiple stakeholders from clients to Constitutional Court justices.",
    components=[
        {
            "letter": "A",
            "component": "Audience",
            "description": "Define the target reader",
            "example": "This opinion is for a sophisticated commercial client who is a CEO with some legal knowledge, and will also be reviewed by instructing attorneys."
        },
        {
            "letter": "B",
            "component": "Behaviour",
            "description": "Expected output behaviour",
            "example": "Provide a balanced analysis that identifies risks while also showing commercial pragmatism. Use confident but qualified language."
        },
        {
            "letter": "C",
            "component": "Context",
            "description": "Situational background",
            "example": "This relates to a proposed acquisition of a Johannesburg-based fintech company. CIPC approval and Competition Commission notification are pending."
        },
        {
            "letter": "D",
            "component": "Details",
            "description": "Specific requirements",
            "example": "Focus on MOI provisions, Companies Act 71 of 2008 compliance, s163 oppression remedy risks, and director liability under s77."
        },
        {
            "letter": "E",
            "component": "Examples",
            "description": "Sample format or precedents",
            "example": "Structure the opinion as per Deneys Reitz format: Executive Summary, Background, Issues for Opinion, Analysis, Recommendations, Caveats."
        }
    ],
    sa_adaptations=[
        "Consider the legal sophistication level of SA clients",
        "Account for different audiences: judges, masters, registrars, commissioners",
        "Adapt language for lay clients using plain language principles",
        "Consider cultural context and ubuntu in client relations",
        "Reference appropriate SA law firm formats and styles"
    ],
    example_prompt="""[AUDIENCE]
Constitutional Court justices who require rigorous legal analysis with clear constitutional values orientation. Secondary audience: amici curiae and law reporters.

[BEHAVIOUR]
Present as authoritative heads of argument with proper deference to the Court. Use transformative constitutionalism framing.

[CONTEXT]
Application for leave to appeal to the Constitutional Court regarding the interpretation of s25 (property rights) in the context of land reform.

[DETAILS]
Address: (1) Constitutional jurisdiction threshold, (2) s25 internal limitations, (3) s36 limitations analysis, (4) comparative constitutional law.

[EXAMPLES]
Follow the structure of successful heads in Daniels v Scribante and Minister of Land Affairs v Slamdien.""",
    best_for=["Client communications", "Court documents", "Multi-stakeholder outputs"],
    difficulty="Intermediate",
    source="ContractPod AI / Leah AI"
)

SEVEN_PS_FRAMEWORK = PromptingFramework(
    name="Purpose, Persona, Prompt, Parameters, Proof, Preview, Polish",
    acronym="7 Ps",
    category=FrameworkCategory.STRUCTURAL,
    description="Comprehensive seven-step framework ensuring thorough prompt preparation from initial purpose through final refinement, ideal for complex SA litigation matters.",
    components=[
        {
            "letter": "1",
            "component": "Purpose",
            "description": "Define the objective",
            "example": "To prepare heads of argument for an urgent interdict application in the High Court, Gauteng Division, Johannesburg."
        },
        {
            "letter": "2",
            "component": "Persona",
            "description": "Assign appropriate role",
            "example": "You are an experienced High Court advocate with expertise in urgent applications and interim relief."
        },
        {
            "letter": "3",
            "component": "Prompt",
            "description": "Core instruction",
            "example": "Draft heads of argument addressing the requirements for interim interdicts per Setlogelo v Setlogelo."
        },
        {
            "letter": "4",
            "component": "Parameters",
            "description": "Constraints and specifications",
            "example": "Maximum 15 pages. Must address all Setlogelo requirements. Include at least 5 SA authorities. Reference applicant's urgency affidavit."
        },
        {
            "letter": "5",
            "component": "Proof",
            "description": "Verification requirements",
            "example": "Cite only cases from SAFLII or official law reports. Provide full neutral citations. Flag any authorities you are uncertain about."
        },
        {
            "letter": "6",
            "component": "Preview",
            "description": "Draft review stage",
            "example": "Provide an outline first for approval before drafting full heads. List all authorities to be cited."
        },
        {
            "letter": "7",
            "component": "Polish",
            "description": "Refinement instructions",
            "example": "After approval of outline, refine for High Court formal register. Ensure proper paragraph numbering and court form compliance."
        }
    ],
    sa_adaptations=[
        "Include practice directive compliance checks",
        "Reference specific court division requirements (GPJHC vs WCHC)",
        "Add Rule 6(12) urgent application requirements",
        "Include SAFLII citation format verification",
        "Address pagination and indexing requirements"
    ],
    example_prompt="""[PURPOSE]
Prepare a Rule 53 review application to review and set aside a CCMA arbitration award.

[PERSONA]
You are a labour law advocate with extensive Labour Court experience and familiarity with review grounds under s145 of the LRA.

[PROMPT]
Draft the founding affidavit addressing the review grounds of gross irregularity and unreasonableness (Sidumo standard).

[PARAMETERS]
- Maximum 30 pages excluding annexures
- Must address all s145 grounds relied upon
- Include chronology of CCMA proceedings
- Reference the record of arbitration proceedings

[PROOF]
- Cite LAC and Labour Court authorities only
- Use ILJ and BLLR report citations where available
- Verify all case references exist on SAFLII

[PREVIEW]
First provide: (1) Summary of review grounds, (2) List of authorities, (3) Proposed structure

[POLISH]
Ensure compliance with Labour Court practice directions. Format for e-filing.""",
    best_for=["Complex litigation", "Urgent applications", "Formal court documents"],
    difficulty="Advanced",
    source="Wisconsin State Bar"
)

PROMPT_SANDWICH_FRAMEWORK = PromptingFramework(
    name="Context-Instruction-Context Sandwich Structure",
    acronym="SANDWICH",
    category=FrameworkCategory.STRUCTURAL,
    description="Places critical instructions between context layers to combat the 'lost middle' phenomenon where AI forgets information in long prompts—essential for complex SA legal briefs.",
    components=[
        {
            "letter": "1",
            "component": "Opening Context",
            "description": "Background and setup",
            "example": "This matter involves a constitutional challenge to municipal by-laws regulating informal trading in the Cape Town CBD."
        },
        {
            "letter": "2",
            "component": "Critical Instructions",
            "description": "Core requirements (most important)",
            "example": "CRITICAL: Apply the Camps Bay Ratepayers test for by-law validity. Address both procedural fairness (PAJA) and substantive constitutional challenges."
        },
        {
            "letter": "3",
            "component": "Supporting Details",
            "description": "Additional context",
            "example": "The by-laws were promulgated under s156 municipal powers. Affected traders were not consulted. Similar by-laws were struck down in eThekwini."
        },
        {
            "letter": "4",
            "component": "Reinforced Instructions",
            "description": "Repeat key requirements",
            "example": "REMEMBER: Focus on (1) ultra vires analysis, (2) PAJA procedural fairness, (3) s22 right to trade, (4) s9 equality. Cite at least 3 Constitutional Court authorities."
        }
    ],
    sa_adaptations=[
        "Place constitutional analysis requirements prominently",
        "Sandwich SAFLII citation requirements in critical section",
        "Reinforce jurisdiction-specific requirements at end",
        "Use for complex multi-issue constitutional matters",
        "Combat tendency to miss transformative constitutionalism analysis"
    ],
    example_prompt="""[OPENING CONTEXT]
A community organisation challenges the constitutionality of the Traditional Courts Bill as violating customary law and gender equality rights.

[CRITICAL INSTRUCTIONS - READ CAREFULLY]
*** ESSENTIAL: Analyse under the following framework ***
1. Recognition of customary law (s211 Constitution)
2. Gender equality (s9) - apply Bhe v Magistrate Khayelitsha
3. Right to culture (s30 and s31) balanced against Bill of Rights
4. Access to courts (s34)
USE THE ALEXKOR TEST FOR CUSTOMARY LAW RECOGNITION

[SUPPORTING DETAILS]
The Bill provides for traditional leaders to adjudicate disputes without legal representation. Women's groups argue it perpetuates patriarchy. Traditional leaders argue constitutional recognition of their authority.

[REINFORCE - DO NOT FORGET]
*** Your analysis MUST include: ***
- Living customary law vs official customary law distinction
- Shilubana v Nwamitwa for gender equality in customary context
- At least 5 Constitutional Court citations
- Recommendations for constitutional amendments""",
    best_for=["Long complex prompts", "Multi-issue analysis", "Constitutional matters"],
    difficulty="Intermediate",
    source="Prompt Engineering Research"
)

JUST_ASK_FRAMEWORK = PromptingFramework(
    name="Jurisdiction, Underlying facts, Specific issue, Timeframe, Authorities, Structure, Keywords",
    acronym="JUST ASK",
    category=FrameworkCategory.SPECIALIZED,
    description="Legal-specific framework ensuring all critical elements for SA legal research are addressed, from jurisdiction through to specific keyword requirements.",
    components=[
        {
            "letter": "J",
            "component": "Jurisdiction",
            "description": "Specify court/forum",
            "example": "South African Constitutional Court; alternatively High Court, Gauteng Division, Pretoria"
        },
        {
            "letter": "U",
            "component": "Underlying Facts",
            "description": "Key factual background",
            "example": "State entity expropriated property without following proper procedures. No compensation offered. Property used for RDP housing."
        },
        {
            "letter": "S",
            "component": "Specific Issue",
            "description": "Precise legal question",
            "example": "Whether s25(2) 'just and equitable compensation' applies when expropriation is for land reform purposes under s25(4)."
        },
        {
            "letter": "T",
            "component": "Timeframe",
            "description": "Temporal constraints",
            "example": "Focus on post-2018 Constitutional Court decisions following the Expropriation Bill parliamentary debates."
        },
        {
            "letter": "A",
            "component": "Authorities",
            "description": "Source requirements",
            "example": "Constitutional Court judgments, SCA decisions, and academic commentary from SALJ and Constitutional Court Review."
        },
        {
            "letter": "S",
            "component": "Structure",
            "description": "Output format",
            "example": "IRAC format with separate sections for historical development, current position, and future implications."
        },
        {
            "letter": "K",
            "component": "Keywords",
            "description": "Search terms",
            "example": "Expropriation, compensation, land reform, s25, Agri SA, Florence, deprivation vs expropriation"
        }
    ],
    sa_adaptations=[
        "Specify SA court division precisely (e.g., WCHC vs GPJHC)",
        "Include SAFLII as authoritative source",
        "Reference SA law reports (SA, BCLR, All SA)",
        "Add relevant SA legislation by Act number",
        "Include both English and Afrikaans case names where relevant"
    ],
    example_prompt="""[JURISDICTION]
Labour Court of South Africa, held at Johannesburg; appealable to Labour Appeal Court

[UNDERLYING FACTS]
Employee dismissed for operational requirements. Company retrenched 200 workers. LIFO principle allegedly not followed. S189A facilitated process not used despite qualifying numbers.

[SPECIFIC ISSUE]
Whether failure to use s189A large-scale retrenchment procedure renders dismissals automatically unfair or procedurally unfair.

[TIMEFRAME]
Focus on LAC judgments from 2020-2024, particularly post-COVID-19 retrenchment decisions.

[AUTHORITIES]
LAC and Labour Court judgments on SAFLII; ILJ and BLLR reports; Grogan's Workplace Law commentary.

[STRUCTURE]
1. Summary (100 words)
2. Legislative framework (s189 vs s189A)
3. Case law analysis (chronological)
4. Application to facts
5. Risk assessment (High/Medium/Low)
6. Recommendations

[KEYWORDS]
Retrenchment, s189, s189A, operational requirements, LIFO, facilitated process, automatically unfair, procedurally unfair, compensation""",
    best_for=["Legal research", "Case preparation", "Opinion writing"],
    difficulty="Intermediate",
    source="North Carolina Bar Association"
)

CASE_FRAMEWORK = PromptingFramework(
    name="Context, Action, Specifics, Examples",
    acronym="C.A.S.E.",
    category=FrameworkCategory.STRUCTURAL,
    description="Streamlined four-component framework ideal for quick SA legal queries while maintaining sufficient structure for accurate outputs.",
    components=[
        {
            "letter": "C",
            "component": "Context",
            "description": "Background situation",
            "example": "Commercial landlord in Sandton seeking to evict defaulting tenant from office premises."
        },
        {
            "letter": "A",
            "component": "Action",
            "description": "Required task",
            "example": "Advise on the procedure for commercial eviction and draft letter of demand."
        },
        {
            "letter": "S",
            "component": "Specifics",
            "description": "Key details",
            "example": "3 months arrears. Lease expires in 6 months. Tenant disputes rental increases. No cancellation clause invoked yet."
        },
        {
            "letter": "E",
            "component": "Examples",
            "description": "Format guidance",
            "example": "Follow Occupiers of Erven 87 and 88 procedure. Letter should follow Norton Rose style."
        }
    ],
    sa_adaptations=[
        "Distinguish PIE Act evictions from commercial evictions",
        "Reference relevant High Court division practices",
        "Include sheriff and registrar requirements",
        "Address CPA implications for consumer contracts",
        "Consider RCJ requirements for specific claim values"
    ],
    example_prompt="""[CONTEXT]
First-time homebuyer in Johannesburg discovered defects in property 3 months after transfer. Seller was a private individual (not estate agent).

[ACTION]
Analyse the buyer's remedies under voetstoots clause and advise on prospects of success.

[SPECIFICS]
- Voetstoots clause in deed of sale
- Defects: rising damp, electrical faults, roof leaks
- Seller completed disclosure form claiming no knowledge
- Purchase price R2.1 million
- Defects repair estimate R450,000

[EXAMPLES]
Apply Odendaal v Ferraris and Van der Merwe v Meades latent defects principles. Structure as brief opinion with recommendations.""",
    best_for=["Quick queries", "Initial consultations", "Focused research"],
    difficulty="Beginner",
    source="Legal Prompt Engineering Best Practices"
)

# ═══════════════════════════════════════════════════════════════════════════════
# ITERATIVE & REASONING FRAMEWORKS
# ═══════════════════════════════════════════════════════════════════════════════

CHAIN_OF_THOUGHT_LEGAL = PromptingFramework(
    name="Chain-of-Thought Legal Reasoning",
    acronym="CoT-LEGAL",
    category=FrameworkCategory.REASONING,
    description="Explicit step-by-step reasoning framework adapted for SA legal analysis, making AI's logical process visible and verifiable.",
    components=[
        {
            "letter": "1",
            "component": "Problem Identification",
            "description": "State the legal problem",
            "example": "The issue is whether the administrative action meets the requirements of lawfulness, reasonableness, and procedural fairness under PAJA."
        },
        {
            "letter": "2",
            "component": "Rule Statement",
            "description": "Identify applicable law",
            "example": "Section 6 of PAJA provides grounds for judicial review. The Bato Star test establishes the standard for reasonableness review."
        },
        {
            "letter": "3",
            "component": "Step-by-Step Application",
            "description": "Apply law to facts incrementally",
            "example": "First, I consider lawfulness... Next, I analyse reasonableness... Then, I examine procedural fairness... Finally, I consider appropriate remedy..."
        },
        {
            "letter": "4",
            "component": "Uncertainty Flagging",
            "description": "Acknowledge limitations",
            "example": "Note: The application of the rule in Merafong is uncertain here because the facts differ in that..."
        },
        {
            "letter": "5",
            "component": "Reasoned Conclusion",
            "description": "Reach supported conclusion",
            "example": "Based on the above analysis, the administrative action is likely reviewable on the ground of procedural unfairness, with medium confidence."
        }
    ],
    sa_adaptations=[
        "Structure around SA legal principles (e.g., ubuntu, transformative constitutionalism)",
        "Reference Constitutional Court methodology",
        "Include statutory interpretation principles (Jaga v Dönges)",
        "Apply proportionality analysis (s36 limitations)",
        "Use SA burden and standard of proof language"
    ],
    example_prompt="""Analyse step-by-step whether this conduct constitutes unfair discrimination under PEPUDA (Act 4 of 2000).

THINK THROUGH EACH STEP EXPLICITLY:

Step 1: First, identify whether the conduct falls within PEPUDA's scope. Consider...

Step 2: Next, determine if there is differentiation based on a listed or unlisted ground. Analyse...

Step 3: Then, assess whether the differentiation amounts to discrimination (applying Harksen v Lane test). Consider...

Step 4: Now, consider whether the discrimination is unfair (s14 factors). Examine...

Step 5: Finally, if unfair, consider available remedies under s21. Evaluate...

IMPORTANT: Show your reasoning at each step. Flag any uncertainties. Cite SA authorities for each proposition.""",
    best_for=["Complex legal analysis", "Discrimination claims", "Constitutional matters"],
    difficulty="Advanced",
    source="Adapted from AI Legal Research Best Practices"
)

PROMPT_CHAINING = PromptingFramework(
    name="Sequential Multi-Prompt Chaining",
    acronym="CHAIN",
    category=FrameworkCategory.ITERATIVE,
    description="Breaking complex SA legal tasks into sequential linked prompts, each building on the previous output for comprehensive analysis.",
    components=[
        {
            "letter": "1",
            "component": "Foundation Prompt",
            "description": "Establish base analysis",
            "example": "Prompt 1: Summarise the key facts and identify all potential legal issues in this commercial dispute."
        },
        {
            "letter": "2",
            "component": "Deep Dive Prompts",
            "description": "Analyse each issue",
            "example": "Prompt 2: Now focus on the breach of contract issue. Analyse under SA contract law principles. Prompt 3: Separately analyse the delictual claim."
        },
        {
            "letter": "3",
            "component": "Synthesis Prompt",
            "description": "Combine analyses",
            "example": "Prompt 4: Based on the above analyses, which cause of action offers the best prospects of success and why?"
        },
        {
            "letter": "4",
            "component": "Practical Prompt",
            "description": "Actionable recommendations",
            "example": "Prompt 5: Draft a letter of demand incorporating the strongest legal arguments identified."
        }
    ],
    sa_adaptations=[
        "Chain should address multiple SA law sources (common law, statute, Constitution)",
        "Include separate prompts for different forums (court vs arbitration vs CCMA)",
        "Build from legal analysis to practical SA court procedure",
        "Chain citation verification as separate step",
        "Include costs and fee considerations in final chain"
    ],
    example_prompt="""PROMPT CHAIN FOR UNFAIR DISMISSAL MATTER:

[PROMPT 1 - CLASSIFICATION]
Based on the following facts, classify the type of dismissal: misconduct, incapacity, or operational requirements. Identify which LRA schedule applies.

[PROMPT 2 - SUBSTANTIVE FAIRNESS]
Based on your classification, analyse substantive fairness under the relevant Code of Good Practice. Apply Sidumo standard.

[PROMPT 3 - PROCEDURAL FAIRNESS]  
Now analyse procedural fairness. Was proper pre-dismissal procedure followed? Apply Avril Elizabeth Home principles.

[PROMPT 4 - REMEDY ANALYSIS]
If dismissal is unfair, calculate appropriate remedy: reinstatement, re-employment, or compensation. Apply Equity Aviation v SATAWU principles.

[PROMPT 5 - STRATEGY]
Synthesise above into CCMA referral strategy. Recommend evidence needed and witnesses to call.""",
    best_for=["Complex multi-issue matters", "Building comprehensive opinions", "Litigation strategy"],
    difficulty="Advanced",
    source="ContractPod AI Legal Prompting Guide"
)

# ═══════════════════════════════════════════════════════════════════════════════
# VERIFICATION & SAFETY FRAMEWORKS
# ═══════════════════════════════════════════════════════════════════════════════

HOSTILE_WITNESS_TECHNIQUE = PromptingFramework(
    name="Hostile Witness Verification Technique",
    acronym="HOSTILE",
    category=FrameworkCategory.VERIFICATION,
    description="Treating AI like a hostile witness—demanding proof, challenging assertions, and cross-examining outputs to prevent hallucinations in SA legal work.",
    components=[
        {
            "letter": "1",
            "component": "Demand Proof",
            "description": "Require evidence for claims",
            "example": "For every legal proposition, cite the specific case, paragraph number, and quote the relevant passage."
        },
        {
            "letter": "2",
            "component": "Challenge Assumptions",
            "description": "Question AI's reasoning",
            "example": "What is the basis for your assertion that this falls under s25? Show me the specific wording that supports this."
        },
        {
            "letter": "3",
            "component": "Seek Contrary Authority",
            "description": "Actively find counterarguments",
            "example": "Now identify any cases that contradict your conclusion. What arguments would opposing counsel make?"
        },
        {
            "letter": "4",
            "component": "Confidence Assessment",
            "description": "Rate certainty levels",
            "example": "Rate your confidence in this conclusion: High (well-established law), Medium (arguable), Low (novel/uncertain), or Speculative."
        },
        {
            "letter": "5",
            "component": "Fallback Position",
            "description": "Identify alternatives",
            "example": "If your primary analysis is wrong, what is the fallback position? What's the worst-case scenario?"
        }
    ],
    sa_adaptations=[
        "Demand SAFLII citations for all SA cases",
        "Require specific Act and section references",
        "Cross-reference with official law reports (SA, BCLR)",
        "Challenge Constitutional Court interpretations",
        "Verify SCA pronouncements are not obiter"
    ],
    example_prompt="""You stated that the employer can dismiss for operational requirements with 2 weeks notice.

PROVE YOUR ANSWER:
1. Cite the specific section of the LRA that permits this
2. Quote the exact wording of the provision
3. Provide at least 2 LAC cases confirming this interpretation
4. Identify any cases that suggest a different approach
5. Rate your confidence level (High/Medium/Low/Speculative)
6. If you are wrong, what is the correct position?

DO NOT PROCEED until you have addressed each point. If you cannot find authority, say "I cannot verify this proposition.\"""",
    best_for=["Citation verification", "Risk assessment", "Quality assurance"],
    difficulty="Intermediate",
    source="Relativity Legal AI Guide"
)

FALSIFIABLE_QUESTIONS = PromptingFramework(
    name="Falsifiable Question Technique",
    acronym="FALSIFY",
    category=FrameworkCategory.VERIFICATION,
    description="Framing legal questions in ways that can be definitively proven true or false, reducing ambiguous or evasive AI responses.",
    components=[
        {
            "letter": "1",
            "component": "Binary Framing",
            "description": "Yes/No questions",
            "example": "Does s197 of the LRA apply to the sale of a business as a going concern? Answer YES or NO, then explain."
        },
        {
            "letter": "2",
            "component": "Existence Verification",
            "description": "Confirm existence of law",
            "example": "Does a case called 'Phumelela Gaming' exist that deals with betting regulations? If yes, provide full citation."
        },
        {
            "letter": "3",
            "component": "Threshold Questions",
            "description": "Numerical/factual queries",
            "example": "What is the prescribed time limit for referring an unfair dismissal dispute to the CCMA? Cite the source."
        },
        {
            "letter": "4",
            "component": "Comparative Framing",
            "description": "Clear comparisons",
            "example": "Which has higher precedent value for the Labour Court: a LAC judgment or a previous Labour Court judgment?"
        }
    ],
    sa_adaptations=[
        "Frame questions about specific SA time periods (prescription, referral deadlines)",
        "Use for court hierarchy verification",
        "Apply to statutory threshold questions (monetary jurisdiction, etc.)",
        "Verify existence of SA legislation and amendments",
        "Confirm court division jurisdiction"
    ],
    example_prompt="""Answer these falsifiable questions about SA labour law:

1. TRUE or FALSE: An employee earning above the BCEA threshold is excluded from CCMA jurisdiction for unfair dismissal claims. Cite authority.

2. SPECIFIC NUMBER: What is the current BCEA earnings threshold as of 2024? Cite the Government Gazette.

3. CASE EXISTENCE: Does a Constitutional Court case called "NEHAWU v UCT" exist? If yes, provide neutral citation and year.

4. HIERARCHY: Which court's judgment is binding on the Labour Court: (a) Supreme Court of Appeal, or (b) Labour Appeal Court? Cite authority.

For each answer, if you are uncertain, state "UNVERIFIED - requires independent confirmation.\"""",
    best_for=["Fact-checking", "Quick verification", "Citation checking"],
    difficulty="Beginner",
    source="Legal Prompt Engineering Best Practices"
)

PINK_ELEPHANTS = PromptingFramework(
    name="Pink Elephants Positive Framing",
    acronym="POSITIVE",
    category=FrameworkCategory.VERIFICATION,
    description="Using positive commands rather than negative prohibitions—tell AI what to do, not what to avoid—for clearer SA legal outputs.",
    components=[
        {
            "letter": "1",
            "component": "Positive Commands",
            "description": "State what to do",
            "example": "INSTEAD OF: 'Don't cite American cases' → USE: 'Cite only South African authorities from SAFLII'"
        },
        {
            "letter": "2",
            "component": "Inclusive Language",
            "description": "Define inclusions",
            "example": "INSTEAD OF: 'Don't include irrelevant cases' → USE: 'Include only cases directly addressing s193 remedies'"
        },
        {
            "letter": "3",
            "component": "Specific Guidance",
            "description": "Clear directions",
            "example": "INSTEAD OF: 'Don't be vague' → USE: 'Provide specific paragraph numbers for all propositions'"
        },
        {
            "letter": "4",
            "component": "Focus Areas",
            "description": "Direct attention",
            "example": "INSTEAD OF: 'Don't discuss irrelevant issues' → USE: 'Focus exclusively on the limitation of actions defence'"
        }
    ],
    sa_adaptations=[
        "Positively specify SA citation formats required",
        "Direct to specific SA law databases (SAFLII, Jutastat)",
        "Affirmatively require Constitutional Court jurisprudence",
        "Specify inclusion of ubuntu principles",
        "Positively frame bilingual terminology requirements"
    ],
    example_prompt="""Draft a legal opinion on prescription defence.

POSITIVE INSTRUCTIONS:
✓ Cite only South African authorities (SAFLII, official law reports)
✓ Focus on the Prescription Act 68 of 1969
✓ Include Constitutional Court guidance on access to justice
✓ Apply the principles from Makate v Vodacom
✓ Structure using IRAC format
✓ Write for a High Court audience
✓ Use formal legal register
✓ Provide full neutral citations for all cases

[Note: Positive framing ensures AI follows these instructions rather than being confused by prohibitions]""",
    best_for=["Clear instructions", "Reducing confusion", "Better compliance"],
    difficulty="Beginner",
    source="Relativity AI Prompt Engineering Guide"
)

# ═══════════════════════════════════════════════════════════════════════════════
# SP3 ADVANCED AI FRAMEWORKS (from 302 Prompt Expert)
# ═══════════════════════════════════════════════════════════════════════════════

VARI_FRAMEWORK = PromptingFramework(
    name="Variational Analysis for Reasoning and Inference",
    acronym="VARI",
    category=FrameworkCategory.REASONING,
    description="DeepMind-inspired framework requiring explicit reasoning, self-reflection, and verification at each analytical step. Adapted for rigorous SA legal analysis.",
    components=[
        {
            "letter": "V",
            "component": "Verify Understanding",
            "description": "Confirm comprehension of the legal question",
            "example": "First, verify: What is the precise legal question? What relief does the client seek? Which court has jurisdiction?"
        },
        {
            "letter": "A",
            "component": "Analyse Systematically",
            "description": "Break down the legal analysis",
            "example": "Analyse each element: (1) Cause of action, (2) Available defences, (3) Evidential requirements, (4) Applicable precedent"
        },
        {
            "letter": "R",
            "component": "Reflect and Question",
            "description": "Self-reflection on analysis quality",
            "example": "Reflect: Have I considered all Constitutional Court authorities? Are there recent SCA judgments that might alter the analysis?"
        },
        {
            "letter": "I",
            "component": "Iterate and Improve",
            "description": "Refine conclusions through iteration",
            "example": "Iterate: Recheck reasoning against ubuntu principles. Does this interpretation align with transformative constitutionalism?"
        }
    ],
    sa_adaptations=[
        "Verify understanding against SA court hierarchy",
        "Analyse using Constitutional framework first",
        "Reflect on ubuntu and community impact",
        "Iterate considering transformative justice outcomes"
    ],
    example_prompt="""[VARI LEGAL ANALYSIS]

VERIFY: Before analysis, confirm understanding:
- Legal Question: Is the eviction notice valid under PIE?
- Client Position: Tenant in occupation since 2015
- Forum: Magistrate's Court eviction application

ANALYSE: Systematically examine:
1. PIE Act 19 of 1998 requirements (s4-5)
2. Municipal housing obligations (s26 Constitution)
3. Meaningful engagement requirement (Olivia Road)
4. Alternative accommodation duties

REFLECT: Question the analysis:
- Have I considered Port Elizabeth Municipality v Various Occupiers?
- Is the interpretation consistent with ubuntu?
- What would Constitutional Court require?

ITERATE: Refine conclusions:
- Cross-check against recent Housing Act amendments
- Verify alignment with City of Johannesburg jurisprudence""",
    best_for=["Complex constitutional matters", "Rights-based analysis", "Multi-step legal reasoning"],
    difficulty="Advanced",
    source="DeepMind AI Research / 302 Prompt Expert"
)

Q_STAR_FRAMEWORK = PromptingFramework(
    name="Q-Learning Star Strategy Framework",
    acronym="Q*",
    category=FrameworkCategory.ITERATIVE,
    description="A* + Q-Learning hybrid framework for legal strategy optimisation. Maps litigation pathways and optimises for best outcomes considering costs, risks, and probabilities.",
    components=[
        {
            "letter": "Q",
            "component": "Query State",
            "description": "Define the current legal position",
            "example": "Query: Current state = employer received demand letter. Goal = minimise liability exposure while preserving business relationship."
        },
        {
            "letter": "S",
            "component": "Strategy Paths",
            "description": "Map available strategic pathways",
            "example": "Paths: (A) Settlement negotiation, (B) CCMA conciliation, (C) Defend at arbitration, (D) Labour Court review"
        },
        {
            "letter": "T",
            "component": "Think Ahead",
            "description": "Project outcomes 3 moves ahead",
            "example": "If Path A (settle): Cost estimate R150k, probability 80%. If Path C (defend): Cost R300k+, success probability 60%."
        },
        {
            "letter": "A",
            "component": "Assess Optimally",
            "description": "Calculate optimal path",
            "example": "Optimal: Path A settlement preferred. Expected value = R150k × 80% = R120k vs Path C = R180k expected cost."
        },
        {
            "letter": "R",
            "component": "Recommend Action",
            "description": "Provide actionable strategy",
            "example": "Recommend: Initiate without prejudice discussions. Set ceiling at R175k. Prepare arbitration defence as BATNA."
        }
    ],
    sa_adaptations=[
        "Factor in CCMA/bargaining council timelines",
        "Include costs of Constitutional Court escalation",
        "Account for ubuntu-based resolution preferences",
        "Consider specialist court expertise requirements"
    ],
    example_prompt="""[Q* LEGAL STRATEGY ANALYSIS]

QUERY STATE:
- Current: Employee dismissed, alleges automatic unfairness (s187)
- Goal: Best outcome for employer considering costs and reputational risk

STRATEGY PATHS:
A. CCMA settlement: Timeline 30 days, cost R200k-400k
B. Arbitration defence: Timeline 6+ months, cost R150k legal + potential 24 month award
C. Labour Court review: Timeline 18 months, cost R500k+
D. Ex gratia without admission: Immediate, cost R250k

THINK AHEAD:
- Path A: 70% probability employee accepts R300k → Expected: R210k
- Path B: 40% success, if lose = R500k+ → Expected: R300k
- Path C: 50% success on review → Expected: R400k

ASSESS OPTIMALLY:
Path A minimises expected cost and preserves confidentiality.

RECOMMEND:
Initiate settlement discussions. Offer R275k starting, ceiling R375k. 
Prepare arbitration defence as leverage. Document all offers as without prejudice.""",
    best_for=["Litigation strategy", "Cost-benefit analysis", "Settlement negotiations"],
    difficulty="Advanced",
    source="OpenAI Q* Research / 302 Prompt Expert"
)

MICRO_OPT_FRAMEWORK = PromptingFramework(
    name="Micro-Optimisation Enhancement",
    acronym="MICRO",
    category=FrameworkCategory.ITERATIVE,
    description="Microsoft-inspired iterative micro-enhancement framework. Applies 15+ small optimisations to refine prompts to near-optimal quality through cumulative improvements.",
    components=[
        {
            "letter": "M",
            "component": "Measure Current",
            "description": "Assess baseline prompt quality",
            "example": "Current prompt scores: Clarity 6/10, Specificity 5/10, SA Context 7/10, Structure 6/10"
        },
        {
            "letter": "I",
            "component": "Identify Weaknesses",
            "description": "Pinpoint specific improvement areas",
            "example": "Weaknesses: No role specified, vague timeline, missing citation format requirement"
        },
        {
            "letter": "C",
            "component": "Correct Incrementally",
            "description": "Apply targeted fixes",
            "example": "Add: 'You are a Senior Attorney specialising in commercial law. Use SAFLII neutral citations.'"
        },
        {
            "letter": "R",
            "component": "Refine Structure",
            "description": "Improve organisation",
            "example": "Reorganise into: Context → Instructions → Format → Constraints → Output"
        },
        {
            "letter": "O",
            "component": "Optimise Tokens",
            "description": "Maximise information density",
            "example": "Consolidate redundant instructions. Remove filler words. Add XML-style delimiters."
        }
    ],
    sa_adaptations=[
        "Ensure each micro-fix maintains SA legal accuracy",
        "Add SA-specific citation requirements incrementally",
        "Include Constitutional Court methodology references",
        "Optimise for SAFLII and Jutastat output formats"
    ],
    example_prompt="""[MICRO-OPTIMISATION SEQUENCE]

BASELINE PROMPT:
"Help me understand the law on evictions"

ITERATION 1 - Add Role:
"You are a Senior Attorney specialising in property law and evictions..."

ITERATION 2 - Add Specificity:
"...specifically PIE Act evictions from informal settlements..."

ITERATION 3 - Add Context:
"...in Gauteng, for a municipality client facing a court deadline..."

ITERATION 4 - Add Format:
"...provide analysis structured as: (1) Legal Requirements, (2) Case Law, (3) Risks, (4) Recommendations..."

ITERATION 5 - Add Constraints:
"...cite only SAFLII authorities post-2015, include Constitutional Court guidance from Occupiers of 51 Olivia Road..."

FINAL OPTIMISED PROMPT:
[All iterations combined into coherent, high-quality prompt]""",
    best_for=["Prompt refinement", "Quality improvement", "Teaching prompt engineering"],
    difficulty="Intermediate",
    source="Microsoft Research / 302 Prompt Expert"
)

SPO_FRAMEWORK = PromptingFramework(
    name="Self-Play Optimization",
    acronym="SPO",
    category=FrameworkCategory.ITERATIVE,
    description="HKUST/DeepWisdom self-play optimization framework where AI iteratively refines prompts through internal Q&A cycles and adversarial testing.",
    components=[
        {
            "letter": "S",
            "component": "Set Initial Prompt",
            "description": "Establish baseline prompt",
            "example": "Initial: 'Analyse the validity of this restraint of trade clause'"
        },
        {
            "letter": "P",
            "component": "Play Opponent",
            "description": "Generate adversarial questions",
            "example": "Opponent asks: What jurisdiction? Which industry? What is the restraint period? Who are the parties?"
        },
        {
            "letter": "O",
            "component": "Optimise Response",
            "description": "Refine prompt to address weaknesses",
            "example": "Refined: 'Analyse validity of 2-year, 50km restraint for sales manager in pharmaceutical sector, Gauteng High Court jurisdiction'"
        }
    ],
    sa_adaptations=[
        "Include SA restraint of trade test (Magna Alloys)",
        "Reference Constitutional Court balance (Reddy v Siemens)",
        "Add Basson v Chilwan reasonableness factors",
        "Consider BCEA protections for employees"
    ],
    example_prompt="""[SPO LEGAL PROMPT REFINEMENT]

INITIAL PROMPT:
"Is this restraint valid?"

SELF-PLAY ROUND 1:
Q: What restraint? What context?
→ Refined: "Is this 3-year restraint of trade clause valid?"

SELF-PLAY ROUND 2:
Q: What industry? What role? What jurisdiction?
→ Refined: "Is this 3-year restraint for a mining engineer in Limpopo valid?"

SELF-PLAY ROUND 3:
Q: What specific terms? What consideration was given?
→ Refined: "Analyse validity of 3-year, provincial restraint for senior mining engineer, considering R500k restraint payment, under Basson v Chilwan factors and Magna Alloys test."

FINAL OPTIMISED:
Full prompt with all adversarial gaps addressed.""",
    best_for=["Prompt refinement", "Gap identification", "Comprehensive coverage"],
    difficulty="Intermediate",
    source="HKUST/DeepWisdom Research / 302 Prompt Expert"
)

GUIDED_FRAMEWORK = PromptingFramework(
    name="Guided Complete Framework",
    acronym="GUIDED",
    category=FrameworkCategory.STRUCTURAL,
    description="Step-by-step guided optimisation with component checklist. Walks users through each element of a well-constructed legal prompt for learning and completeness.",
    components=[
        {
            "letter": "G",
            "component": "Goal Definition",
            "description": "What outcome do you need?",
            "example": "Goal: Determine whether client has valid claim for constructive dismissal"
        },
        {
            "letter": "U",
            "component": "User Context",
            "description": "Who is this for?",
            "example": "Audience: Senior partner review, client is HR director"
        },
        {
            "letter": "I",
            "component": "Information Required",
            "description": "What input is needed?",
            "example": "Facts: Employment history, working conditions changes, resignation circumstances"
        },
        {
            "letter": "D",
            "component": "Deliverable Format",
            "description": "What format is needed?",
            "example": "Format: Internal memo with risk assessment scale (High/Medium/Low)"
        },
        {
            "letter": "E",
            "component": "Examples & Precedent",
            "description": "What references should be used?",
            "example": "Cite: Pretoria Society for the Care of the Retarded v Loots, Murray v Minister of Defence"
        },
        {
            "letter": "D",
            "component": "Delimiters & Structure",
            "description": "How should output be organised?",
            "example": "Structure: Executive Summary → Facts → Law → Analysis → Risk Assessment → Recommendations"
        }
    ],
    sa_adaptations=[
        "Guide users to include SA jurisdiction context",
        "Prompt for relevant SA legislation references",
        "Ensure Constitutional Court methodology consideration",
        "Include ubuntu and transformative justice checkpoints"
    ],
    example_prompt="""[GUIDED PROMPT CONSTRUCTION]

Step 1 - GOAL: What legal outcome do you need?
→ "Determine liability exposure for alleged discrimination claim"

Step 2 - USER: Who is the audience?
→ "Board of directors, non-legal background, need risk assessment"

Step 3 - INFORMATION: What facts are available?
→ "Employee complaint, HR investigation report, company policies"

Step 4 - DELIVERABLE: What format?
→ "Executive briefing, 2 pages max, traffic light risk indicators"

Step 5 - EXAMPLES: What authorities?
→ "EEA s6, Harksen v Lane, IMATU v City of Cape Town"

Step 6 - DELIMITERS: What structure?
→ "Summary (1 para) → Issue (bullets) → Risk (table) → Action Items (numbered)"

[ASSEMBLED PROMPT]:
Complete prompt constructed from all guided steps.""",
    best_for=["Learning prompt engineering", "Ensuring completeness", "Training junior staff"],
    difficulty="Beginner",
    source="302 Prompt Expert Complete Guide"
)

# ═══════════════════════════════════════════════════════════════════════════════
# ALL FRAMEWORKS COLLECTION
# ═══════════════════════════════════════════════════════════════════════════════

ALL_FRAMEWORKS: Dict[str, PromptingFramework] = {
    "RICE": RICE_FRAMEWORK,
    "ABCDE": ABCDE_FRAMEWORK,
    "7 Ps": SEVEN_PS_FRAMEWORK,
    "SANDWICH": PROMPT_SANDWICH_FRAMEWORK,
    "JUST ASK": JUST_ASK_FRAMEWORK,
    "C.A.S.E.": CASE_FRAMEWORK,
    "CoT-LEGAL": CHAIN_OF_THOUGHT_LEGAL,
    "CHAIN": PROMPT_CHAINING,
    "HOSTILE": HOSTILE_WITNESS_TECHNIQUE,
    "FALSIFY": FALSIFIABLE_QUESTIONS,
    "POSITIVE": PINK_ELEPHANTS,
    # SP3 Advanced AI Frameworks
    "VARI": VARI_FRAMEWORK,
    "Q*": Q_STAR_FRAMEWORK,
    "MICRO": MICRO_OPT_FRAMEWORK,
    "SPO": SPO_FRAMEWORK,
    "GUIDED": GUIDED_FRAMEWORK,
}

def get_frameworks_by_category(category: FrameworkCategory) -> List[PromptingFramework]:
    """Get all frameworks in a specific category"""
    return [f for f in ALL_FRAMEWORKS.values() if f.category == category]

def get_frameworks_by_difficulty(difficulty: str) -> List[PromptingFramework]:
    """Get frameworks by difficulty level"""
    return [f for f in ALL_FRAMEWORKS.values() if f.difficulty.lower() == difficulty.lower()]

def get_framework_by_acronym(acronym: str) -> Optional[PromptingFramework]:
    """Get a specific framework by its acronym"""
    return ALL_FRAMEWORKS.get(acronym.upper())

def generate_combined_prompt(
    frameworks: List[str],
    context: str,
    legal_issue: str,
    practice_area: PracticeArea
) -> str:
    """Generate a combined prompt using multiple frameworks"""
    combined = f"""
# Combined SA Legal Prompt
Practice Area: {practice_area.value}

## Context
{context}

## Legal Issue
{legal_issue}

## Applied Frameworks
"""
    for fw_name in frameworks:
        fw = ALL_FRAMEWORKS.get(fw_name)
        if fw:
            combined += f"\n### {fw.acronym} ({fw.name})\n"
            for comp in fw.components:
                combined += f"**{comp['component']}**: [Apply {comp['description']}]\n"
    
    combined += """
## SA-Specific Requirements
- Use SAFLII neutral citation format
- Reference SA legislation by Act number
- Apply Constitutional Court methodology
- Consider ubuntu and transformative constitutionalism
- Verify all citations independently
"""
    return combined

# ═══════════════════════════════════════════════════════════════════════════════
# FRAMEWORK SELECTOR LOGIC
# ═══════════════════════════════════════════════════════════════════════════════

def recommend_framework(
    task_type: str,
    complexity: str,
    verification_needed: bool
) -> List[PromptingFramework]:
    """Recommend appropriate frameworks based on task characteristics"""
    recommendations = []
    
    # Base framework by task type
    if "research" in task_type.lower():
        recommendations.append(JUST_ASK_FRAMEWORK)
    if "draft" in task_type.lower() or "document" in task_type.lower():
        recommendations.append(SEVEN_PS_FRAMEWORK)
    if "analysis" in task_type.lower() or "opinion" in task_type.lower():
        recommendations.append(RICE_FRAMEWORK)
    if "client" in task_type.lower() or "communication" in task_type.lower():
        recommendations.append(ABCDE_FRAMEWORK)
    
    # Add complexity-based framework
    if complexity.lower() == "complex":
        recommendations.append(CHAIN_OF_THOUGHT_LEGAL)
        recommendations.append(PROMPT_CHAINING)
    elif complexity.lower() == "simple":
        recommendations.append(CASE_FRAMEWORK)
    
    # Add verification frameworks if needed
    if verification_needed:
        recommendations.append(HOSTILE_WITNESS_TECHNIQUE)
        recommendations.append(FALSIFIABLE_QUESTIONS)
    
    # Always recommend positive framing
    if PINK_ELEPHANTS not in recommendations:
        recommendations.append(PINK_ELEPHANTS)
    
    return recommendations

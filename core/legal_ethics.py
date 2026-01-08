"""
🇿🇦 SA Legal Ethics for AI Use
Professional Ethics Guidelines for AI-Assisted Legal Practice in South Africa
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional

class EthicsCategory(Enum):
    """Categories of Legal Ethics for AI"""
    COMPETENCE = "Professional Competence"
    CONFIDENTIALITY = "Confidentiality & Privilege"
    SUPERVISION = "Supervision & Accountability"
    DISCLOSURE = "Disclosure & Transparency"
    BILLING = "Billing & Fees"
    VERIFICATION = "Verification & Accuracy"
    BIAS = "Bias & Fairness"

class RiskLevel(Enum):
    """Risk level for AI use scenarios"""
    HIGH = "High Risk - Exercise Extreme Caution"
    MEDIUM = "Medium Risk - Proceed with Care"
    LOW = "Low Risk - Standard Precautions"
    PROHIBITED = "Prohibited - Do Not Use AI"

@dataclass
class EthicalGuideline:
    """Ethical guideline for AI use in SA legal practice"""
    title: str
    category: EthicsCategory
    description: str
    lpc_rule_reference: Optional[str]
    sa_context: str
    requirements: List[str]
    prohibited_practices: List[str]
    best_practices: List[str]
    examples: List[Dict[str, str]]
    prompt_guidance: str

@dataclass
class AIUseScenario:
    """Scenario for AI use with risk assessment"""
    scenario: str
    risk_level: RiskLevel
    safeguards_required: List[str]
    recommended_approach: str
    prohibited_uses: List[str]

# ═══════════════════════════════════════════════════════════════════════════════
# CORE ETHICAL GUIDELINES
# ═══════════════════════════════════════════════════════════════════════════════

COMPETENCE_GUIDELINE = EthicalGuideline(
    title="Technology Competence in AI Use",
    category=EthicsCategory.COMPETENCE,
    description="Legal practitioners must maintain competence in understanding and using AI tools, including their capabilities, limitations, and risks to client interests.",
    lpc_rule_reference="LPC Code of Conduct, Rule 3.1 (Competence and Diligence)",
    sa_context="""
In South Africa, the Legal Practice Council (LPC) requires practitioners to maintain 
competence. While no specific AI rules exist yet, the duty of competence extends to 
technology use. SA practitioners should follow international guidance (ABA Formal 
Opinion 512) adapted for local context, pending LPC-specific guidance.
    """,
    requirements=[
        "Understand capabilities and limitations of AI tools used",
        "Stay current with developments in legal AI technology",
        "Recognise when AI is appropriate vs inappropriate for specific tasks",
        "Maintain ability to independently verify AI outputs",
        "Ensure AI use does not undermine quality of legal work",
        "Complete appropriate training on AI tools before professional use"
    ],
    prohibited_practices=[
        "Using AI tools without understanding their limitations",
        "Relying solely on AI without independent verification",
        "Using AI for tasks beyond its demonstrated capabilities",
        "Ignoring known issues with AI hallucinations in legal contexts"
    ],
    best_practices=[
        "Attend CLE/CPD courses on legal AI",
        "Test AI tools on known matters before using on client work",
        "Maintain a log of AI tool performance and issues",
        "Subscribe to updates on legal AI developments",
        "Participate in law society AI working groups"
    ],
    examples=[
        {
            "situation": "Attorney uses ChatGPT for legal research without understanding it hallucinates citations",
            "issue": "Breach of competence - failing to understand tool limitations",
            "resolution": "Train on AI limitations; always verify citations on SAFLII"
        },
        {
            "situation": "Advocate uses AI to draft heads of argument, properly reviews and edits",
            "issue": "None - appropriate supervised use",
            "resolution": "Continue with proper review process"
        }
    ],
    prompt_guidance="""
When using AI for legal work, always:
1. State your verification requirements: "I will independently verify all citations on SAFLII"
2. Acknowledge limitations: "Provide only SA authorities you are confident exist"
3. Request confidence levels: "Rate confidence in each proposition: High/Medium/Low"
4. Include fallback: "If uncertain about any authority, state: 'Citation requires verification'"
"""
)

CONFIDENTIALITY_GUIDELINE = EthicalGuideline(
    title="Confidentiality and Attorney-Client Privilege",
    category=EthicsCategory.CONFIDENTIALITY,
    description="Client information must be protected when using AI tools. Public AI tools may compromise privilege and confidentiality.",
    lpc_rule_reference="LPC Code of Conduct, Rule 4.1 (Confidentiality); Attorney's Act; Legal Practice Act",
    sa_context="""
South African attorney-client privilege and confidentiality obligations are strictly 
enforced. Information shared with public AI tools may be:
1. Stored and used for model training
2. Potentially discoverable as no longer privileged
3. At risk of data breaches
SA practitioners must be especially cautious given limited local case law on AI privilege waiver.
    """,
    requirements=[
        "Never input client-identifying information into public AI tools",
        "Use enterprise/professional AI tools with data protection agreements",
        "Anonymise all prompts before input (remove names, case numbers, identifiers)",
        "Verify AI tool's data retention and training policies",
        "Obtain informed consent if using AI that poses confidentiality risks",
        "Maintain records of AI tool usage for privilege purposes"
    ],
    prohibited_practices=[
        "Inputting client names, ID numbers, or case numbers into public AI",
        "Using free AI tools for privileged communications analysis",
        "Copying entire client files into AI prompts",
        "Sharing confidential settlement figures with public AI",
        "Using AI on sealed court documents or in camera materials"
    ],
    best_practices=[
        "Use find/replace to anonymise before prompting: 'Client A' instead of actual names",
        "Use enterprise tools with BAA/data processing agreements",
        "Create sanitised fact patterns that preserve issues but remove identifiers",
        "Maintain 'do not input' lists for highly sensitive matters",
        "Use temporary chat modes where available",
        "Regularly delete AI conversation histories"
    ],
    examples=[
        {
            "situation": "Attorney inputs 'Advise if ABC Pty Ltd can sue XYZ Inc for R5m breach'",
            "issue": "Identified parties and amount - privilege potentially waived",
            "resolution": "Use: 'Advise if Company A can sue Company B for significant breach'"
        },
        {
            "situation": "Using enterprise AI with data processing agreement for contract review",
            "issue": "None if proper agreements in place",
            "resolution": "Confirm DPA covers AI use; document compliance"
        }
    ],
    prompt_guidance="""
BEFORE PROMPTING - ANONYMISATION CHECKLIST:
□ Remove all client names → Use "Client", "Company A", "Applicant"
□ Remove case numbers → Use "relevant matter"
□ Remove specific amounts → Use "substantial amount" or percentage ranges
□ Remove dates that identify → Use "recently" or "approximately X years ago"
□ Remove identifying facts → Generalise to preserve legal issue only
□ Verify no privileged strategy disclosed

SAFE PROMPT TEMPLATE:
"[ANONYMISED CONTEXT]
A client in [general industry] seeks advice on [legal issue] in [jurisdiction].
The relevant facts are: [sanitised facts].
Advise on: [specific legal question]
DO NOT: reference this as actual client matter or attempt to identify parties."
"""
)

SUPERVISION_GUIDELINE = EthicalGuideline(
    title="Supervision and Human Oversight",
    category=EthicsCategory.SUPERVISION,
    description="AI must be supervised as a tool, not delegated to as a decision-maker. The legal practitioner remains accountable for all work product.",
    lpc_rule_reference="LPC Code of Conduct, Rule 5.1 (Supervision of Subordinates); Rule 3.1 (Competence)",
    sa_context="""
In South Africa, supervision duties extend beyond human subordinates. The Legal Practice 
Act and LPC Rules require practitioners to ensure work quality regardless of source. 
AI should be treated like a junior candidate attorney or law student - requiring 
supervision and verification of all outputs.
    """,
    requirements=[
        "Review all AI-generated content before use in legal work",
        "Apply same quality standards to AI output as human subordinate work",
        "Maintain decision-making authority - never defer judgment to AI",
        "Document AI assistance in file notes where appropriate",
        "Accept personal responsibility for all work product regardless of AI assistance",
        "Ensure junior practitioners understand AI supervision requirements"
    ],
    prohibited_practices=[
        "Filing AI-generated documents without human review",
        "Delegating final legal judgment to AI",
        "Presenting AI output as own work without verification",
        "Allowing unsupervised AI use by junior practitioners",
        "Blaming AI for errors in work product"
    ],
    best_practices=[
        "Implement multi-stage review: AI draft → practitioner review → senior review",
        "Create checklists for AI output verification",
        "Treat AI like a 'first-year associate' requiring significant guidance",
        "Document AI assistance in internal file notes",
        "Establish firm-wide AI supervision protocols"
    ],
    examples=[
        {
            "situation": "Attorney submits AI-drafted affidavit without reading it; contains false statements",
            "issue": "Failure to supervise; breach of candour to court",
            "resolution": "Review every line before filing; verify all factual statements"
        },
        {
            "situation": "Senior Counsel reviews AI-drafted heads of argument, rewrites 40%, approves final version",
            "issue": "None - appropriate supervision exercised",
            "resolution": "Proper supervision process followed"
        }
    ],
    prompt_guidance="""
SUPERVISION FRAMEWORK FOR AI OUTPUTS:

Stage 1: Generation
- Use clear, specific prompts
- Request structured output for easier review
- Ask AI to flag uncertain portions

Stage 2: Initial Review
- Read entire output
- Verify all citations independently
- Check for logical consistency
- Identify gaps or errors

Stage 3: Verification
- Cross-check facts against source documents
- Verify case law exists on SAFLII
- Confirm legislation references are correct
- Check procedural requirements

Stage 4: Editing
- Apply professional judgment
- Ensure output reflects client's specific situation
- Add nuances AI may have missed
- Ensure compliance with court requirements

Stage 5: Approval
- Final senior review
- Sign-off as own work product
- Accept full responsibility
"""
)

DISCLOSURE_GUIDELINE = EthicalGuideline(
    title="Disclosure of AI Use",
    category=EthicsCategory.DISCLOSURE,
    description="Transparency about AI assistance may be required in certain contexts, including court filings, client engagement, and opposing counsel interactions.",
    lpc_rule_reference="LPC Code of Conduct, Rule 3.3 (Candour to Tribunal); Rule 4.2 (Client Communication)",
    sa_context="""
South African courts have not yet issued specific AI disclosure requirements. However, 
practitioners should anticipate developments similar to US courts (standing orders 
requiring AI certification). Proactive disclosure to clients demonstrates professional 
integrity and aligns with SA legal profession's ethical foundations.
    """,
    requirements=[
        "Disclose AI use to clients during engagement where material to representation",
        "Comply with any court orders requiring AI disclosure in filings",
        "Be truthful if directly asked about AI use by court or opposing counsel",
        "Update engagement letters to address AI tool usage",
        "Maintain records of AI use for potential disclosure requirements"
    ],
    prohibited_practices=[
        "Lying about AI use when directly asked by the court",
        "Misrepresenting AI-generated content as solely human-authored when disclosure required",
        "Ignoring court standing orders on AI certification",
        "Concealing material AI involvement from clients who express concerns"
    ],
    best_practices=[
        "Include AI disclosure clause in standard engagement letters",
        "Discuss AI use during initial client consultation",
        "Monitor court practice directives for AI disclosure requirements",
        "Proactively disclose AI assistance in sensitive matters",
        "Create standard disclosure language for various contexts"
    ],
    examples=[
        {
            "situation": "Client asks 'Will you be using AI on my matter?'",
            "issue": "Disclosure obligation triggered by direct question",
            "resolution": "Honest answer about AI assistance, supervision process, and safeguards"
        },
        {
            "situation": "Court issues practice directive requiring AI certification in pleadings",
            "issue": "Mandatory disclosure compliance",
            "resolution": "Include required certification; maintain records of AI use for matter"
        }
    ],
    prompt_guidance="""
SAMPLE CLIENT DISCLOSURE LANGUAGE:

"[Firm Name] may use artificial intelligence tools to assist with legal research, 
document drafting, and analysis. All AI-assisted work is:
• Reviewed and supervised by qualified legal practitioners
• Verified for accuracy and appropriateness
• Subject to our confidentiality protocols
• Used only with appropriate data protection measures

The responsibility for all legal advice and work product remains with [Firm Name] 
and your assigned legal team. AI tools assist but do not replace professional legal judgment.

Please advise if you have any questions or concerns about our use of AI tools."

SAMPLE COURT CERTIFICATION (anticipatory):

"[I/Counsel for the Applicant] certify that:
1. [No generative AI was used in preparing this document / Generative AI was used 
   to assist with drafting, subject to human review and supervision]
2. All citations and legal authorities have been independently verified
3. The undersigned accepts full responsibility for the contents of this document
4. Confidentiality and data protection requirements have been maintained throughout"
"""
)

BILLING_GUIDELINE = EthicalGuideline(
    title="Ethical Billing for AI-Assisted Work",
    category=EthicsCategory.BILLING,
    description="AI efficiency gains raise ethical questions about billing. Practitioners must bill fairly and not overcharge for AI-accelerated work.",
    lpc_rule_reference="LPC Code of Conduct, Rule 8 (Fees); Attorneys' Tariff Guidelines",
    sa_context="""
South Africa's contingency fee regulations, tariff guidelines, and the general principle 
of reasonable fees apply to AI-assisted work. When AI significantly reduces time spent, 
practitioners should consider value-based billing or reduced time billing rather than 
billing at rates that would have applied to fully manual work.
    """,
    requirements=[
        "Bill only for actual time spent on AI-assisted work, not 'saved' time",
        "Disclose AI-related costs or efficiencies in fee discussions",
        "Ensure fees remain reasonable despite AI efficiency",
        "Consider value-based billing models where appropriate",
        "Do not charge separately for AI tool costs unless disclosed and agreed"
    ],
    prohibited_practices=[
        "Billing full manual hours for work completed quickly with AI",
        "Hidden charges for AI tool subscriptions without disclosure",
        "Inflating time estimates knowing AI will accelerate work",
        "Double-billing for AI research plus manual verification where minimal"
    ],
    best_practices=[
        "Adopt value-based or fixed-fee billing where AI provides efficiency",
        "Disclose AI efficiency when providing estimates",
        "Share AI savings with clients through reduced fees",
        "Clearly separate AI tool costs from professional fees",
        "Review billing practices regularly as AI capabilities evolve"
    ],
    examples=[
        {
            "situation": "Research that previously took 4 hours completed in 30 minutes with AI",
            "issue": "Cannot bill 4 hours; must reflect actual time",
            "resolution": "Bill actual verification and analysis time; consider value-based fee"
        },
        {
            "situation": "AI drafts contract in 10 minutes; 2 hours spent reviewing/editing",
            "issue": "Billing should reflect value delivered plus actual time",
            "resolution": "Bill 2+ hours for review/editing; disclose AI assistance in drafting"
        }
    ],
    prompt_guidance="""
BILLING CONSIDERATIONS FOR AI-ASSISTED WORK:

1. TIME RECORDING:
   - Record actual time spent prompting, reviewing, and editing
   - Do not estimate time "as if" done manually
   - Note AI assistance in time narrative

2. FEE DISCUSSION:
   "This matter may benefit from AI-assisted research/drafting, which may reduce 
   time costs. Our fees will reflect actual time spent plus professional value added.
   AI tool subscription costs are included in our overhead/separately charged at R[X]."

3. VALUE ASSESSMENT:
   - Complex matters: Value of expertise and judgment may justify premium
   - Routine matters: Efficiency savings should generally benefit client
   - Risk management: Appropriate fee for verification and quality assurance

4. INVOICE TRANSPARENCY:
   Consider notations such as:
   - "Legal research (AI-assisted): X hours"
   - "Document drafting and review: X hours"
   - "Citation verification: X hours"
"""
)

VERIFICATION_GUIDELINE = EthicalGuideline(
    title="Citation Verification and Accuracy",
    category=EthicsCategory.VERIFICATION,
    description="All AI-generated legal citations and factual claims must be independently verified. AI hallucination of false citations is a known and significant risk.",
    lpc_rule_reference="LPC Code of Conduct, Rule 3.3 (Candour to Tribunal); Rule 3.1 (Competence)",
    sa_context="""
South African courts rely on accurate citation. Citing non-existent cases or misquoting 
judgments could result in:
- Costs de bonis propriis against the practitioner
- Professional misconduct proceedings
- Loss of credibility with the court
- Potential negligence claims from clients
SAFLII provides free access for verification of SA case law.
    """,
    requirements=[
        "Verify every case citation on SAFLII or official law reports before use",
        "Check that quoted passages accurately reflect judgment text",
        "Confirm legislation references are current and correctly cited",
        "Verify procedural rules and practice directives cited",
        "Cross-check AI's characterisation of case holdings against source"
    ],
    prohibited_practices=[
        "Filing documents with unverified AI-generated citations",
        "Relying on AI's summary of a case without reading the judgment",
        "Citing cases based on AI description without source verification",
        "Using AI-generated citations in oral argument without verification"
    ],
    best_practices=[
        "Create verification checklist for all AI-assisted research",
        "Use SAFLII noteup function to check case currency",
        "Read at least the relevant paragraphs of any cited judgment",
        "Cross-reference with Juta or LexisNexis for confirmation",
        "Maintain citation verification log for file notes"
    ],
    examples=[
        {
            "situation": "AI cites 'Minister of Justice v Ntuli [2019] ZACC 12' - case does not exist",
            "issue": "Hallucinated citation - would embarrass practitioner and potentially attract sanctions",
            "resolution": "Verify all citations on SAFLII before use; reject unverifiable cases"
        },
        {
            "situation": "AI accurately cites case but mischaracterises the ratio",
            "issue": "Reading AI summary is insufficient; misrepresentation to court",
            "resolution": "Read actual judgment; verify AI's characterisation of holding"
        }
    ],
    prompt_guidance="""
VERIFICATION PROTOCOL:

1. REQUEST VERIFIABLE CITATIONS:
   "Cite only SA cases you are confident exist. Provide full SAFLII neutral citation.
   If uncertain about any citation, state: 'CITATION REQUIRES VERIFICATION'."

2. VERIFY ON SAFLII:
   □ Case name exists
   □ Citation format is correct
   □ Year and court are accurate
   □ Case is current (not overruled)
   □ Quoted passages are accurate

3. VERIFICATION PROMPT:
   "For each case cited, provide:
   1. Full neutral citation
   2. The specific paragraph numbers supporting the proposition
   3. Confidence level: HIGH (certain) / MEDIUM (likely) / LOW (verify)
   
   Flag any case where you are uncertain of existence."

4. CROSS-CHECKING:
   - Search SAFLII by case name and citation
   - Use noteup function to check for overruling
   - Read relevant paragraphs in actual judgment
   - Verify proposition matches ratio decidendi
"""
)

BIAS_GUIDELINE = EthicalGuideline(
    title="Screening for AI Bias",
    category=EthicsCategory.BIAS,
    description="AI models may reflect historical biases. Legal practitioners must screen outputs for inappropriate bias in SA's constitutional context.",
    lpc_rule_reference="Constitution s9 (Equality); LPC Code of Conduct professional standards",
    sa_context="""
South Africa's Constitution mandates equality and non-discrimination (s9). AI models 
trained on historical legal materials may perpetuate past discrimination or reflect 
foreign legal biases inappropriate for SA's transformative constitutional framework.
Practitioners must apply ubuntu and transformative constitutionalism lens.
    """,
    requirements=[
        "Screen AI outputs for racial, gender, or other inappropriate bias",
        "Apply SA constitutional values (dignity, equality, ubuntu) as filter",
        "Recognise AI may not reflect transformative constitutionalism principles",
        "Correct AI suggestions that perpetuate historical discrimination",
        "Consider diversity and inclusion in AI tool selection"
    ],
    prohibited_practices=[
        "Accepting AI recommendations that perpetuate discrimination",
        "Using AI to inform decisions on protected grounds without scrutiny",
        "Ignoring bias indicators in AI outputs",
        "Applying foreign legal norms uncritically in SA context"
    ],
    best_practices=[
        "Apply 'ubuntu lens' to all AI outputs",
        "Cross-check AI outputs against Constitutional Court jurisprudence",
        "Consult diverse perspectives when AI outputs seem problematic",
        "Report biased outputs to AI providers for improvement",
        "Train team on recognising AI bias"
    ],
    examples=[
        {
            "situation": "AI suggests creditworthiness factors that correlate with race (e.g., zip codes)",
            "issue": "Indirect discrimination; unconstitutional approach",
            "resolution": "Use objective criteria; apply equality analysis; reject proxy discrimination"
        },
        {
            "situation": "AI applies US legal concepts that don't align with SA transformative constitutionalism",
            "issue": "Inappropriate foreign law influence",
            "resolution": "Redirect to SA Constitutional Court jurisprudence; apply local values"
        }
    ],
    prompt_guidance="""
BIAS SCREENING FRAMEWORK:

1. PROMPT FOR SA CONTEXT:
   "Provide analysis applying South African law and constitutional values.
   Apply transformative constitutionalism and ubuntu principles.
   Do not apply foreign legal concepts unless specifically relevant."

2. EQUALITY SCREEN:
   Review all AI outputs for:
   □ Assumptions about protected characteristics
   □ Recommendations that may have disparate impact
   □ Language that perpetuates historical stereotypes
   □ Suggestions contrary to s9 equality

3. CONSTITUTIONAL VALUES CHECK:
   □ Does output respect human dignity (s10)?
   □ Does output promote equality (s9)?
   □ Does output align with ubuntu philosophy?
   □ Is output consistent with transformative constitutionalism?

4. CORRECTIVE PROMPT:
   "Review your previous response for any assumptions or recommendations 
   that may conflict with South African constitutional values of:
   - Human dignity
   - Equality and non-discrimination
   - Ubuntu and community values
   - Transformative constitutionalism
   
   Revise any problematic elements."
"""
)

# ═══════════════════════════════════════════════════════════════════════════════
# AI USE SCENARIOS WITH RISK ASSESSMENT
# ═══════════════════════════════════════════════════════════════════════════════

AI_USE_SCENARIOS: List[AIUseScenario] = [
    AIUseScenario(
        scenario="Legal Research - General Principles",
        risk_level=RiskLevel.LOW,
        safeguards_required=[
            "Verify all citations on SAFLII",
            "Read actual judgments, not just AI summaries",
            "Cross-reference with authoritative sources"
        ],
        recommended_approach="Use AI for initial research; verify and expand using SAFLII, Juta, LexisNexis",
        prohibited_uses=["Filing research memos with unverified citations"]
    ),
    AIUseScenario(
        scenario="Document Drafting - First Drafts",
        risk_level=RiskLevel.LOW,
        safeguards_required=[
            "Thorough review and editing of all drafts",
            "Verify factual accuracy",
            "Ensure compliance with specific requirements",
            "Anonymise any factual context used in prompts"
        ],
        recommended_approach="Use AI for initial draft; extensively review, edit, and personalise",
        prohibited_uses=["Filing AI drafts without review"]
    ),
    AIUseScenario(
        scenario="Contract Analysis - Clause Identification",
        risk_level=RiskLevel.MEDIUM,
        safeguards_required=[
            "Anonymise contract parties before input",
            "Do not input highly sensitive commercial terms",
            "Verify AI's clause identification against actual document",
            "Apply human judgment to risk assessment"
        ],
        recommended_approach="Use for issue-spotting; verify findings; apply professional judgment",
        prohibited_uses=["Inputting identified parties or specific deal terms into public AI"]
    ),
    AIUseScenario(
        scenario="Case Outcome Prediction",
        risk_level=RiskLevel.HIGH,
        safeguards_required=[
            "Never rely solely on AI predictions",
            "Provide multiple caveats to client",
            "Apply professional judgment and experience",
            "Document basis for any predictions given"
        ],
        recommended_approach="Use only as one input among many; extensive human analysis required",
        prohibited_uses=["Giving clients AI predictions as legal advice"]
    ),
    AIUseScenario(
        scenario="Privileged Document Analysis",
        risk_level=RiskLevel.HIGH,
        safeguards_required=[
            "Use only enterprise AI with strict data agreements",
            "Never use public AI for privileged materials",
            "Anonymise all identifiers",
            "Obtain client consent if any risk"
        ],
        recommended_approach="Enterprise tools only; thorough anonymisation; documented consent",
        prohibited_uses=["Any public AI use with privileged documents"]
    ),
    AIUseScenario(
        scenario="Settlement Negotiations Strategy",
        risk_level=RiskLevel.HIGH,
        safeguards_required=[
            "Complete anonymisation of parties and amounts",
            "No disclosure of actual negotiation positions",
            "Enterprise tools preferred"
        ],
        recommended_approach="General strategic advice only; no specific case details",
        prohibited_uses=["Inputting actual offers, counteroffers, or strategy into public AI"]
    ),
    AIUseScenario(
        scenario="Client Intake and Matter Assessment",
        risk_level=RiskLevel.PROHIBITED,
        safeguards_required=["Do not use AI for this purpose with identified client information"],
        recommended_approach="Conduct intake manually; anonymise before any AI consultation",
        prohibited_uses=["Inputting prospective client's confidential disclosures into AI"]
    ),
    AIUseScenario(
        scenario="Criminal Defence Strategy",
        risk_level=RiskLevel.HIGH,
        safeguards_required=[
            "Extreme anonymisation required",
            "No identifying facts",
            "Enterprise tools only",
            "Heightened privilege concerns"
        ],
        recommended_approach="General legal research only; no case-specific analysis via AI",
        prohibited_uses=["Any identified or identifiable case details in AI prompts"]
    )
]

# ═══════════════════════════════════════════════════════════════════════════════
# COMPREHENSIVE ETHICS COLLECTION
# ═══════════════════════════════════════════════════════════════════════════════

ALL_GUIDELINES: Dict[str, EthicalGuideline] = {
    "competence": COMPETENCE_GUIDELINE,
    "confidentiality": CONFIDENTIALITY_GUIDELINE,
    "supervision": SUPERVISION_GUIDELINE,
    "disclosure": DISCLOSURE_GUIDELINE,
    "billing": BILLING_GUIDELINE,
    "verification": VERIFICATION_GUIDELINE,
    "bias": BIAS_GUIDELINE,
}

def get_guidelines_by_category(category: EthicsCategory) -> List[EthicalGuideline]:
    """Get all guidelines in a specific category"""
    return [g for g in ALL_GUIDELINES.values() if g.category == category]

def assess_ai_use_risk(scenario_type: str) -> Optional[AIUseScenario]:
    """Find risk assessment for a given scenario type"""
    for scenario in AI_USE_SCENARIOS:
        if scenario_type.lower() in scenario.scenario.lower():
            return scenario
    return None

def generate_ethics_checklist(guideline: EthicalGuideline) -> str:
    """Generate a pre-use checklist for a specific guideline"""
    checklist = f"""
# AI Use Ethics Checklist: {guideline.title}

## Category: {guideline.category.value}

## LPC Reference: {guideline.lpc_rule_reference or 'N/A'}

## Before Using AI, Confirm:
{chr(10).join(f"□ {req}" for req in guideline.requirements)}

## Prohibited Practices (DO NOT):
{chr(10).join(f"✗ {prac}" for prac in guideline.prohibited_practices)}

## Best Practices (DO):
{chr(10).join(f"✓ {prac}" for prac in guideline.best_practices)}

## Prompt Guidance:
{guideline.prompt_guidance}
"""
    return checklist

def generate_comprehensive_ethics_prompt() -> str:
    """Generate a comprehensive ethics-aware prompt prefix"""
    return """
# SA LEGAL AI ETHICS COMPLIANCE

Before proceeding, I confirm:

## Confidentiality
□ All client-identifying information has been removed
□ Parties are anonymised as "Client", "Company A", "Applicant", etc.
□ No privileged strategy or settlement positions disclosed
□ Using appropriate enterprise/professional AI tool

## Verification Commitment  
□ I will verify ALL citations on SAFLII before use
□ I will read actual judgments, not rely on AI summaries
□ I will apply professional judgment to all outputs

## Supervision
□ All AI output will be reviewed before use
□ I accept full responsibility for final work product
□ AI is a tool assisting my work, not replacing my judgment

## South African Context
□ Apply South African law and constitutional values
□ Use SAFLII neutral citation format
□ Consider ubuntu and transformative constitutionalism
□ Reference SA authorities, not foreign law unless specifically relevant

---

[PROCEED WITH LEGAL QUERY]
"""

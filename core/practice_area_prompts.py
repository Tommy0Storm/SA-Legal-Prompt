"""
🇿🇦 SA Practice Area Prompts
Specialized Prompt Templates for Each South African Legal Practice Area
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional

class PracticeArea(Enum):
    """South African Legal Practice Areas"""
    CONSTITUTIONAL = "Constitutional Law"
    CRIMINAL = "Criminal Law"
    CIVIL_LITIGATION = "Civil Litigation"
    LABOUR = "Labour & Employment"
    COMMERCIAL = "Commercial & Corporate"
    FAMILY = "Family Law"
    PROPERTY = "Property & Conveyancing"
    TAX = "Tax Law"
    IMMIGRATION = "Immigration Law"
    INTELLECTUAL_PROPERTY = "Intellectual Property"
    CONSUMER = "Consumer Protection"
    COMPETITION = "Competition Law"
    ADMINISTRATIVE = "Administrative Law"
    ENVIRONMENTAL = "Environmental Law"
    INSOLVENCY = "Insolvency & Business Rescue"

class PromptType(Enum):
    """Types of Legal Prompts"""
    RESEARCH = "Legal Research"
    ANALYSIS = "Case Analysis"
    DRAFTING = "Document Drafting"
    STRATEGY = "Strategic Advice"
    OPINION = "Legal Opinion"
    PROCEDURE = "Procedural Guidance"

@dataclass
class PracticeAreaPrompt:
    """Specialized Prompt for a Practice Area"""
    title: str
    practice_area: PracticeArea
    prompt_type: PromptType
    description: str
    template: str
    key_legislation: List[str]
    key_cases: List[str]
    practice_tips: List[str]
    common_issues: List[str]
    saflii_search_terms: List[str]

# ═══════════════════════════════════════════════════════════════════════════════
# CONSTITUTIONAL LAW
# ═══════════════════════════════════════════════════════════════════════════════

CONSTITUTIONAL_RIGHTS_ANALYSIS = PracticeAreaPrompt(
    title="Constitutional Rights Infringement Analysis",
    practice_area=PracticeArea.CONSTITUTIONAL,
    prompt_type=PromptType.ANALYSIS,
    description="Comprehensive analysis of whether conduct or legislation infringes constitutional rights and whether infringement is justifiable under s36.",
    template="""
# Constitutional Rights Analysis

## Role
You are a Senior Counsel specialising in constitutional law, with extensive experience appearing before the Constitutional Court of South Africa.

## Context
[Describe the law, conduct, or situation being challenged]

## Analysis Framework
Apply the two-stage Constitutional Court methodology:

### STAGE 1: Rights Infringement
1. **Identify the right(s)**: Which section(s) of the Bill of Rights are engaged?
2. **Scope of the right**: What does the Constitutional Court jurisprudence say about the scope of this right?
3. **Infringement analysis**: Does the law/conduct infringe the right? Apply relevant tests (e.g., Harksen v Lane for s9, FNB for s25)

### STAGE 2: Justification (s36 Limitations Analysis)
If infringement is found, analyse justification using the five proportionality factors:
1. **Nature of the right**: How important is this right in an open and democratic society?
2. **Importance of the purpose**: What is the purpose of the limitation and how important is it?
3. **Nature and extent of limitation**: How severe is the limitation?
4. **Relation between limitation and purpose**: Is the limitation rationally connected to the purpose?
5. **Less restrictive means**: Are there less restrictive means to achieve the purpose?

### Required Output
- Conclusion on whether infringement is justified
- Assessment of likelihood of success if challenged
- Recommended constitutional remedy if successful (s172)
- Key authorities with SAFLII citations

## Important
- Apply South African constitutional jurisprudence only
- Reference ubuntu and transformative constitutionalism where relevant
- Cite Constitutional Court cases with full neutral citations
""",
    key_legislation=[
        "Constitution of the Republic of South Africa, 1996",
        "Promotion of Administrative Justice Act 3 of 2000",
        "Promotion of Equality and Prevention of Unfair Discrimination Act 4 of 2000"
    ],
    key_cases=[
        "S v Makwanyane [1995] ZACC 3",
        "Harksen v Lane [1997] ZACC 12",
        "S v Manamela [2000] ZACC 5",
        "Government v Grootboom [2000] ZACC 19",
        "FNB v Commissioner, SARS [2002] ZACC 5"
    ],
    practice_tips=[
        "Always start with identifying the specific constitutional right(s)",
        "The onus is on the party seeking to justify the limitation",
        "Consider both direct and indirect application of rights",
        "Remedies include declaration of invalidity, reading-in, reading-down, or suspension"
    ],
    common_issues=[
        "Legislation limiting fundamental rights",
        "Executive action infringing Bill of Rights",
        "Private party conduct affecting constitutional rights",
        "Positive obligations of the state"
    ],
    saflii_search_terms=["s36", "proportionality", "limitation", "Bill of Rights", "constitutional review"]
)

# ═══════════════════════════════════════════════════════════════════════════════
# CRIMINAL LAW
# ═══════════════════════════════════════════════════════════════════════════════

CRIMINAL_DEFENCE_STRATEGY = PracticeAreaPrompt(
    title="Criminal Defence Strategy Analysis",
    practice_area=PracticeArea.CRIMINAL,
    prompt_type=PromptType.STRATEGY,
    description="Develop comprehensive criminal defence strategy addressing elements, defences, and trial preparation.",
    template="""
# Criminal Defence Strategy Analysis

## Role
You are a Senior Advocate with extensive criminal defence experience in the High Court and Regional Courts of South Africa.

## Context
[ANONYMISED FACTS - Use "the Accused" not actual names]
Charge(s): [Specify charges]
Court: [Magistrates'/Regional/High Court]
Key facts: [Anonymised summary]

## Analysis Framework

### STEP 1: Element Analysis
For each charge:
1. Identify all elements the State must prove
2. Assess strength of State's evidence on each element
3. Identify weakest elements for attack

### STEP 2: Available Defences
Analyse potential defences:
- Factual defences (alibi, mistaken identity, etc.)
- Legal defences (self-defence, necessity, provocation, etc.)
- Constitutional defences (s35 fair trial rights violations)
- Procedural defences (unlawful arrest, inadmissible evidence)

### STEP 3: Evidence Analysis
- Admissibility challenges (s35(5), s217 confessions, hearsay, s252A)
- State witness credibility issues
- Documentary/forensic evidence weaknesses
- Identification evidence challenges

### STEP 4: Trial Strategy
- Plea recommendations
- Section 115 approach (putting State to proof)
- Cross-examination priorities
- Defence witness strategy
- Bail application considerations if applicable

### STEP 5: Sentence Preparation
If conviction likely:
- Mitigating factors
- Zinn triad application (crime, offender, interests of society)
- Minimum sentence provisions and substantial and compelling circumstances
- Correctional supervision possibilities

## Output Required
- Overall assessment of defence prospects
- Recommended strategy with rationale
- Key authorities for each legal argument
- Risk assessment

## Important
- Apply SA criminal law and procedure
- Reference Criminal Procedure Act 51 of 1977
- Consider s35 Constitution rights throughout
- Cite SA case law with neutral citations
""",
    key_legislation=[
        "Criminal Procedure Act 51 of 1977",
        "Criminal Law Amendment Act 105 of 1997 (minimum sentences)",
        "Constitution s35 (arrested, detained and accused persons)",
        "Common law crimes"
    ],
    key_cases=[
        "S v Zinn 1969 (2) SA 537 (A)",
        "S v Malgas 2001 (1) SACR 469 (SCA)",
        "S v Thebus [2003] ZACC 12",
        "S v Coetzee [1997] ZACC 2",
        "Key v Attorney-General Cape [1996] ZACC 25"
    ],
    practice_tips=[
        "Focus on State's weakest element - no need to prove innocence",
        "s35(5) evidence exclusion is discretionary - build strong exclusion case",
        "Minimum sentences require substantial and compelling circumstances",
        "Right to remain silent is fundamental - don't concede what need not be conceded"
    ],
    common_issues=[
        "Identification evidence reliability",
        "Confession admissibility (s217 CPA)",
        "Chain of custody for forensic evidence",
        "Accomplice evidence corroboration",
        "Alibi defence requirements"
    ],
    saflii_search_terms=["criminal appeal", "sentence", "minimum sentence", "substantial and compelling"]
)

# ═══════════════════════════════════════════════════════════════════════════════
# LABOUR LAW
# ═══════════════════════════════════════════════════════════════════════════════

UNFAIR_DISMISSAL_ANALYSIS = PracticeAreaPrompt(
    title="Unfair Dismissal Comprehensive Analysis",
    practice_area=PracticeArea.LABOUR,
    prompt_type=PromptType.ANALYSIS,
    description="Complete analysis of dismissal fairness covering all categories and remedies under the LRA.",
    template="""
# Unfair Dismissal Analysis

## Role
You are an experienced Labour Law practitioner with extensive CCMA and Labour Court experience.

## Context
[Describe dismissal circumstances - anonymised]
Type of dismissal: [Misconduct / Incapacity (poor performance/ill-health/incompatibility) / Operational Requirements / Automatically Unfair]
Employee details: [Service period, position, earnings]
Employer details: [Size, industry]

## Analysis Framework

### STEP 1: Dismissal Classification
- Confirm dismissal occurred (s186(1) definition)
- Classify type: misconduct, incapacity, operational requirements, or automatically unfair
- Identify applicable Code of Good Practice (Schedule 8)

### STEP 2: Substantive Fairness Analysis
**For Misconduct:**
- Was there a rule/standard?
- Was rule valid and reasonable?
- Did employee breach the rule?
- Was dismissal appropriate sanction (consider progressive discipline, mitigating factors)?

**For Incapacity (Poor Performance):**
- Was employee aware of required standard?
- Was employee given opportunity to meet standard?
- Was instruction/guidance/training provided?
- Was reasonable time allowed for improvement?

**For Operational Requirements:**
- Was there genuine commercial rationale?
- Were alternatives to dismissal considered?
- Were selection criteria fair (LIFO as default)?

**For Automatically Unfair (s187):**
- Identify alleged s187 ground
- Apply onus rules (Kroeger v Visual Marketing)

### STEP 3: Procedural Fairness Analysis
- Was employee notified of allegations?
- Was employee given opportunity to respond?
- Was decision made by appropriate person?
- Was process conducted timeously?
- Apply "reasonable employer" test

### STEP 4: Remedy Calculation
If unfair:
- Reinstatement (primary remedy per Equity Aviation)
- Re-employment
- Compensation (factors per s194, maximum 12/24 months)

## Output Required
- Fairness assessment (Substantive: Fair/Unfair; Procedural: Fair/Unfair)
- Likelihood of success at CCMA/Labour Court
- Recommended remedy and quantum
- Key authorities

## Important
- Apply Schedule 8 Code of Good Practice
- Consider Sidumo standard for what reasonable employer would do
- Cite ILJ/BLLR and SAFLII authorities
""",
    key_legislation=[
        "Labour Relations Act 66 of 1995 (ss185-197)",
        "Schedule 8: Code of Good Practice - Dismissal",
        "BCEA (earnings threshold for CCMA jurisdiction)",
        "CCMA Rules"
    ],
    key_cases=[
        "Sidumo v Rustenburg Platinum Mines [2007] ZACC 22",
        "Equity Aviation v SATAWU [2008] ZACC 8",
        "NUMSA v Bader Bop [2003] ZACC 11",
        "Avril Elizabeth Home v CCMA [2006] ZASCA 14",
        "CWIU v Algorax [2003] ZASCA 158"
    ],
    practice_tips=[
        "Always analyse both substantive AND procedural fairness",
        "30-day referral period is jurisdictional - check for condonation need",
        "Reinstatement is primary remedy - only excluded if impracticable",
        "Sidumo standard applies to review of CCMA awards"
    ],
    common_issues=[
        "Distinguishing misconduct from incapacity",
        "Fairness of disciplinary procedures",
        "Constructive dismissal (employee must prove intolerance)",
        "Operational requirements consultation adequacy",
        "Compensation calculation methodology"
    ],
    saflii_search_terms=["unfair dismissal", "CCMA", "substantive fairness", "procedural fairness", "Schedule 8"]
)

# ═══════════════════════════════════════════════════════════════════════════════
# COMMERCIAL LAW
# ═══════════════════════════════════════════════════════════════════════════════

CONTRACT_DISPUTE_ANALYSIS = PracticeAreaPrompt(
    title="Commercial Contract Dispute Analysis",
    practice_area=PracticeArea.COMMERCIAL,
    prompt_type=PromptType.ANALYSIS,
    description="Comprehensive analysis of contract disputes including breach, interpretation, and remedies under SA law.",
    template="""
# Commercial Contract Dispute Analysis

## Role
You are a Senior Commercial Litigation Counsel with extensive High Court experience in contract disputes.

## Context
[Describe contract dispute - anonymised as "Party A" and "Party B"]
Nature of agreement: [Type of contract]
Dispute: [Breach alleged / interpretation issue / enforceability challenge]
Value: [Approximate]

## Analysis Framework

### STEP 1: Contract Formation & Validity
- Was there valid offer and acceptance?
- Is there certainty of terms?
- Are there any vitiating factors (misrepresentation, duress, undue influence)?
- Is the contract in required form (if applicable)?
- Any illegality or contrary to public policy?

### STEP 2: Contract Interpretation
Apply SA interpretation principles:
- Text-in-context approach (Bothma-Batho v S Bothma)
- Business efficacy and commercial purpose
- Contra proferentem if ambiguous
- Parol evidence rule and exceptions

### STEP 3: Breach Analysis
- What are the contractual obligations?
- Has there been a breach?
- Is breach material or non-material?
- Is breach repudiatory, allowing cancellation?
- Has innocent party elected to cancel or claim performance?

### STEP 4: Available Remedies
- Specific performance (interdict to compel)
- Damages (positive and negative interesse)
- Cancellation (if material breach)
- Agreed/liquidated damages (penalty clause analysis)
- Mora interest

### STEP 5: Procedural Considerations
- Jurisdiction (value for Regional vs High Court)
- Prescription (3 years for debt)
- Urgent/interim relief prospects
- Arbitration clause applicability

## Output Required
- Assessment of each party's legal position
- Recommended strategy
- Quantum of potential damages
- Key authorities with citations

## Important
- Apply SA contract law principles
- Consider Conventional Penalties Act if penalty clauses
- Reference Consumer Protection Act if applicable
- Cite SA case law with neutral citations
""",
    key_legislation=[
        "Common law of contract",
        "Conventional Penalties Act 15 of 1962",
        "Consumer Protection Act 68 of 2008 (if applicable)",
        "Alienation of Land Act 68 of 1981 (for land sales)",
        "Electronic Communications and Transactions Act 25 of 2002"
    ],
    key_cases=[
        "Bothma-Batho v S Bothma [2014] ZASCA 159",
        "Bank of Lisbon v Mercantile International [2016] ZACC 7",
        "Bredenkamp v Standard Bank [2010] ZASCA 75",
        "Sasfin v Beukes 1989 (1) SA 1 (A)",
        "Christie's Law of Contract (authoritative textbook)"
    ],
    practice_tips=[
        "Always check for CPA application (consumer transactions)",
        "Penalty clauses subject to court reduction under Conventional Penalties Act",
        "Specific performance is primary contractual remedy in SA",
        "Email contracts generally enforceable under ECTA"
    ],
    common_issues=[
        "Interpretation of boilerplate clauses",
        "Entire agreement clauses and their limits",
        "Exemption clause enforceability",
        "Variation of contract requirements",
        "Cancellation vs damages election"
    ],
    saflii_search_terms=["breach of contract", "interpretation", "cancellation", "specific performance"]
)

# ═══════════════════════════════════════════════════════════════════════════════
# FAMILY LAW
# ═══════════════════════════════════════════════════════════════════════════════

DIVORCE_SETTLEMENT_ANALYSIS = PracticeAreaPrompt(
    title="Divorce and Matrimonial Settlement Analysis",
    practice_area=PracticeArea.FAMILY,
    prompt_type=PromptType.ANALYSIS,
    description="Comprehensive divorce analysis covering grounds, children, maintenance, and property division.",
    template="""
# Divorce and Matrimonial Settlement Analysis

## Role
You are an experienced Family Law practitioner with extensive High Court divorce experience.

## Context
[Describe marriage and circumstances - anonymised as "Spouse A" and "Spouse B"]
Marriage regime: [In community of property / Out of community (with/without accrual) / ANC without accrual]
Children: [Ages, custody issues]
Duration of marriage: [X years]
Assets: [Summary]

## Analysis Framework

### STEP 1: Grounds for Divorce
Under Divorce Act 70 of 1979, s4:
- Irretrievable breakdown (most common)
- Mental illness
- Continuous unconsciousness
- Has marriage irretrievably broken down?

### STEP 2: Children's Matters
**Best interests of child paramount (s28 Constitution, s7 Children's Act):**
- Primary residence / care arrangements
- Contact/access arrangements
- Relocation considerations
- Child's wishes (age-appropriate)
- Parenting plan (s33 Children's Act)

### STEP 3: Maintenance
**Spousal maintenance:**
- Needs and means of each spouse
- Self-sufficiency potential
- Standard of living during marriage
- Duration of maintenance
- Rehabilitative vs permanent maintenance

**Child maintenance:**
- Both parents' duty to maintain
- Child's reasonable needs
- Standard of living
- Calculation methodology

### STEP 4: Property Division
**In community of property:**
- Joint estate divided equally
- Forfeiture claims (s9 Divorce Act)

**Out of community with accrual:**
- Calculate each estate's accrual
- Smaller accrual claims from larger
- Commencement values vs current values

**Out of community without accrual:**
- Each spouse retains own assets
- Consider unjust enrichment claims if applicable

### STEP 5: Procedural Matters
- Unopposed vs opposed divorce
- Rule 43 interim relief
- Pension interest division (s7(7) and (8))
- Family Advocate involvement

## Output Required
- Recommended approach for each issue
- Settlement proposal
- Risks if matter proceeds to trial
- Key authorities

## Important
- Best interests of child is paramount standard
- Consider domestic violence issues and protection orders
- Pension fund division per Pension Funds Act
""",
    key_legislation=[
        "Divorce Act 70 of 1979",
        "Matrimonial Property Act 88 of 1984",
        "Children's Act 38 of 2005",
        "Maintenance Act 99 of 1998",
        "Pension Funds Act 24 of 1956 (s37D pension division)"
    ],
    key_cases=[
        "McCall v McCall 1994 (3) SA 201 (C) - best interests factors",
        "Beaumont v Beaumont 1987 (1) SA 967 (A) - maintenance",
        "Van der Linde v Van der Linde 1996 (3) SA 509 (O) - accrual",
        "SS v Presiding Officer, Children's Court [2020] ZACC 26"
    ],
    practice_tips=[
        "Best interests factors from McCall v McCall still guide courts",
        "Rule 43 provides interim maintenance pending divorce",
        "Pension interests are included in accrual calculation",
        "Settlement is almost always preferable to contested litigation"
    ],
    common_issues=[
        "Relocation with children (care-giver vs child's stability)",
        "Accrual calculation disputes",
        "Hidden assets",
        "Domestic violence protection",
        "Parental alienation"
    ],
    saflii_search_terms=["divorce", "custody", "maintenance", "accrual", "best interests"]
)

# ═══════════════════════════════════════════════════════════════════════════════
# PROPERTY LAW
# ═══════════════════════════════════════════════════════════════════════════════

PROPERTY_TRANSACTION_REVIEW = PracticeAreaPrompt(
    title="Property Transaction and Conveyancing Review",
    practice_area=PracticeArea.PROPERTY,
    prompt_type=PromptType.ANALYSIS,
    description="Comprehensive review of property transactions covering sale agreements, conveyancing, and common disputes.",
    template="""
# Property Transaction Review

## Role
You are an experienced Conveyancing Attorney and property law specialist.

## Context
[Describe transaction - anonymised]
Type: [Sale / Lease / Servitude / Sectional Title / Other]
Property: [General description - no address]
Value: [Range]
Issues: [Specific concerns]

## Analysis Framework

### STEP 1: Agreement Review (for sales)
- Compliance with Alienation of Land Act 68 of 1981
- Essential terms (parties, property, purchase price)
- Suspensive conditions (bond approval, sale of existing property)
- Voetstoots clause and latent defects
- Occupational rent and possession

### STEP 2: Title Investigation
- Check title deed for:
  - Correct ownership
  - Servitudes and restrictions
  - Conditions of title
  - Interdicts or caveats
- Zoning and land use compliance
- Rates clearance requirements

### STEP 3: Conveyancing Procedure
- Bond registration (if applicable)
- Transfer duty / VAT implications
- Deeds Office requirements
- Simultaneous transfers if applicable
- Trust endorsements if property held in trust

### STEP 4: Common Issues
- Latent defects disclosure
- Seller warranties
- Voetstoots limitations (Consumer Protection Act)
- Merger of properties
- Sectional title specific issues (levy arrears, body corporate consent)

### STEP 5: Risk Assessment
- Title risks
- Financial risks
- Timing risks
- Regulatory compliance risks

## Output Required
- Transaction risk assessment
- Recommended protective clauses
- Identified issues requiring resolution
- Estimated timeline and costs

## Important
- Alienation of Land Act applies to all land sales over R250,000
- CPA applies if seller is supplier acting in ordinary course
- Voetstoots limited by CPA for consumer transactions
""",
    key_legislation=[
        "Alienation of Land Act 68 of 1981",
        "Deeds Registries Act 47 of 1937",
        "Sectional Titles Act 95 of 1986",
        "Consumer Protection Act 68 of 2008",
        "Transfer Duty Act 40 of 1949"
    ],
    key_cases=[
        "Odendaal v Ferraris 2009 (4) SA 313 (SCA) - latent defects",
        "Van der Merwe v Meades 1991 (2) SA 1 (A) - voetstoots",
        "ABSA Bank v Mokebe [2018] ZASCA 61 - transfer and registration",
        "Naidoo v Birchwood Hotel [2012] ZASCA 170 - CPA and voetstoots"
    ],
    practice_tips=[
        "Voetstoots clause does not protect seller who knew of defect",
        "CPA s55 overrides voetstoots for consumer transactions",
        "Bond registration is prerequisite for transfer in bonded sales",
        "Transfer duty must be paid before registration"
    ],
    common_issues=[
        "Latent defects discovered post-transfer",
        "Delays in bond approval",
        "Disputes over occupational rent",
        "Rates and levy arrears",
        "Sectional title consent requirements"
    ],
    saflii_search_terms=["sale of land", "voetstoots", "latent defect", "transfer", "conveyancing"]
)

# ═══════════════════════════════════════════════════════════════════════════════
# TAX LAW
# ═══════════════════════════════════════════════════════════════════════════════

TAX_DISPUTE_ANALYSIS = PracticeAreaPrompt(
    title="Tax Dispute and Assessment Challenge",
    practice_area=PracticeArea.TAX,
    prompt_type=PromptType.ANALYSIS,
    description="Analysis of tax disputes including objection, appeal, and litigation strategies.",
    template="""
# Tax Dispute Analysis

## Role
You are a Tax Specialist with extensive experience in SARS disputes and Tax Court matters.

## Context
[Describe tax issue - anonymised]
Tax type: [Income Tax / VAT / Estate Duty / Transfer Duty / Other]
Tax period: [General - e.g., 2023 tax year]
Issue: [Assessment / Penalty / Interest / Interpretation]
Amount: [Range]

## Analysis Framework

### STEP 1: Assessment Analysis
- Is the assessment validly raised? (s96 TAA requirements)
- What is SARS's basis for assessment?
- Is assessment based on correct interpretation of tax law?
- Are all facts correctly applied?
- Is there understatement penalty (s222-223 TAA)?

### STEP 2: Objection Preparation
Under Tax Administration Act 28 of 2011:
- Grounds for objection
- Time limits (30 business days extendable)
- Information and document requirements
- ADR process consideration

### STEP 3: Legal Analysis
- Interpretation of relevant provisions
- Application of case law
- SARS binding rulings and interpretations
- International tax implications if relevant

### STEP 4: Procedural Remedies
- Objection (first step)
- Appeal to Tax Board (disputes under R1m)
- Appeal to Tax Court (larger disputes)
- High Court appeal (on law)
- Senior counsel opinion where needed

### STEP 5: Strategy Considerations
- Dispute resolution (ADR) prospects
- Settlement possibilities
- Pay-now-argue-later rule (s164 TAA)
- Suspension of payment pending dispute
- Costs implications

## Output Required
- Legal merit assessment
- Recommended dispute strategy
- Procedural steps and timeline
- Key authorities

## Important
- Tax Court proceedings are confidential
- SARS bears onus for understatement penalties
- Taxpayer bears onus for challenging assessment
- Apply purposive interpretation per Natal Joint Municipal Pension Fund
""",
    key_legislation=[
        "Tax Administration Act 28 of 2011",
        "Income Tax Act 58 of 1962",
        "Value-Added Tax Act 89 of 1991",
        "Estate Duty Act 45 of 1955",
        "Transfer Duty Act 40 of 1949"
    ],
    key_cases=[
        "Commissioner, SARS v Bosch [2014] ZASCA 171",
        "Natal Joint Municipal Pension Fund v Endumeni [2012] ZASCA 13 - interpretation",
        "ITC cases (anonymised Tax Court cases)",
        "Commissioner, SARS v Marshall [2017] ZASCA 111"
    ],
    practice_tips=[
        "Objection must be filed within 30 business days - watch deadlines",
        "ADR process can resolve disputes efficiently",
        "Tax Court decisions are anonymised in reporting",
        "Consider senior counsel opinion for complex matters"
    ],
    common_issues=[
        "GAAR (General Anti-Avoidance Rule) disputes",
        "Transfer pricing adjustments",
        "VAT input tax disputes",
        "Understatement penalty levels",
        "Prescription of assessments"
    ],
    saflii_search_terms=["income tax", "SARS", "Tax Court", "objection", "assessment"]
)

# ═══════════════════════════════════════════════════════════════════════════════
# ALL PRACTICE AREA PROMPTS
# ═══════════════════════════════════════════════════════════════════════════════

ALL_PRACTICE_PROMPTS: Dict[str, PracticeAreaPrompt] = {
    "constitutional_rights": CONSTITUTIONAL_RIGHTS_ANALYSIS,
    "criminal_defence": CRIMINAL_DEFENCE_STRATEGY,
    "unfair_dismissal": UNFAIR_DISMISSAL_ANALYSIS,
    "contract_dispute": CONTRACT_DISPUTE_ANALYSIS,
    "divorce_settlement": DIVORCE_SETTLEMENT_ANALYSIS,
    "property_transaction": PROPERTY_TRANSACTION_REVIEW,
    "tax_dispute": TAX_DISPUTE_ANALYSIS,
}

def get_prompts_by_area(area: PracticeArea) -> List[PracticeAreaPrompt]:
    """Get all prompts for a specific practice area"""
    return [p for p in ALL_PRACTICE_PROMPTS.values() if p.practice_area == area]

def get_prompts_by_type(prompt_type: PromptType) -> List[PracticeAreaPrompt]:
    """Get all prompts of a specific type"""
    return [p for p in ALL_PRACTICE_PROMPTS.values() if p.prompt_type == prompt_type]

def generate_practice_prompt(prompt: PracticeAreaPrompt, context: str) -> str:
    """Generate a complete prompt with user context"""
    return f"""
{prompt.template}

## Your Specific Context
{context}

## Key Legislation to Consider
{chr(10).join(f"• {leg}" for leg in prompt.key_legislation)}

## Landmark Cases to Reference
{chr(10).join(f"• {case}" for case in prompt.key_cases)}

## Practice Tips
{chr(10).join(f"💡 {tip}" for tip in prompt.practice_tips)}

## Common Issues to Check
{chr(10).join(f"⚠️ {issue}" for issue in prompt.common_issues)}

## SAFLII Search Terms
For verification, search: {', '.join(prompt.saflii_search_terms)}

---
IMPORTANT: All citations must be verified on SAFLII before use.
Apply South African law only unless comparative law specifically requested.
"""

"""
🇿🇦 SA Legislation Database
Comprehensive Reference for Key South African Legislation with Prompting Guidance
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional

class LegislationCategory(Enum):
    """Categories of SA Legislation"""
    CONSTITUTIONAL = "Constitutional & Foundational"
    COMMERCIAL = "Commercial & Corporate"
    LABOUR = "Labour & Employment"
    CONSUMER = "Consumer Protection"
    CRIMINAL = "Criminal Law"
    PROPERTY = "Property & Land"
    FAMILY = "Family & Children"
    ADMINISTRATIVE = "Administrative Law"
    TAX = "Tax & Revenue"
    DATA_PROTECTION = "Data Protection & Privacy"

@dataclass
class KeyProvision:
    """Key provision within legislation"""
    section: str
    title: str
    description: str
    common_applications: List[str]
    key_cases: List[str]
    prompt_tips: List[str]

@dataclass
class SALegislation:
    """Comprehensive SA Legislation Reference"""
    short_title: str
    act_number: str
    full_title: str
    category: LegislationCategory
    commencement_date: str
    purpose: List[str]
    key_institutions: Dict[str, str]
    key_provisions: List[KeyProvision]
    important_schedules: List[str]
    related_regulations: List[str]
    landmark_cases: List[Dict[str, str]]
    prompt_considerations: List[str]
    common_prompt_templates: List[str]

# ═══════════════════════════════════════════════════════════════════════════════
# THE CONSTITUTION
# ═══════════════════════════════════════════════════════════════════════════════

CONSTITUTION = SALegislation(
    short_title="Constitution",
    act_number="Act 108 of 1996",
    full_title="Constitution of the Republic of South Africa",
    category=LegislationCategory.CONSTITUTIONAL,
    commencement_date="4 February 1997",
    purpose=[
        "Establish democratic, sovereign state founded on human dignity, equality and freedom",
        "Entrench Bill of Rights as cornerstone of democracy",
        "Establish separation of powers between executive, legislature and judiciary",
        "Create three spheres of government (national, provincial, local)",
        "Establish Chapter 9 institutions supporting constitutional democracy"
    ],
    key_institutions={
        "Constitutional Court": "Highest court in constitutional matters (s167)",
        "Public Protector": "Investigates maladministration (s182)",
        "SAHRC": "South African Human Rights Commission (s184)",
        "CGE": "Commission for Gender Equality (s187)",
        "Auditor-General": "Audits public sector (s188)",
        "IEC": "Independent Electoral Commission (s190)"
    },
    key_provisions=[
        KeyProvision(
            section="s1",
            title="Founding Provisions",
            description="Republic founded on human dignity, equality, advancement of human rights, non-racialism, non-sexism, supremacy of Constitution, rule of law, universal adult suffrage, multi-party democracy",
            common_applications=["Constitutional interpretation", "Validity of legislation", "State conduct review"],
            key_cases=["Certification of the Constitution", "New National Party v Government"],
            prompt_tips=["Always start constitutional analysis with founding values", "Ubuntu underlies founding provisions"]
        ),
        KeyProvision(
            section="s2",
            title="Supremacy of Constitution",
            description="Constitution is supreme law; law or conduct inconsistent with it is invalid; obligations imposed must be fulfilled",
            common_applications=["Striking down legislation", "Reviewing executive action", "Invalidating contracts"],
            key_cases=["Pharmaceutical Manufacturers v Chairperson of SA"],
            prompt_tips=["Any legal analysis can invoke s2 if constitutionality is in issue"]
        ),
        KeyProvision(
            section="s7",
            title="Rights",
            description="Bill of Rights is cornerstone of democracy; state must respect, protect, promote and fulfil rights",
            common_applications=["Horizontal application of rights", "State positive duties", "Private party rights claims"],
            key_cases=["Carmichele v Minister of Safety and Security", "Government v Grootboom"],
            prompt_tips=["Distinguish negative duties (respect) from positive duties (protect, promote, fulfil)"]
        ),
        KeyProvision(
            section="s8",
            title="Application of Bill of Rights",
            description="Applies to all law; binds legislature, executive, judiciary, all organs of state; may apply to natural/juristic persons",
            common_applications=["Horizontal application between private parties", "Indirect vs direct application"],
            key_cases=["Khumalo v Holomisa", "Barkhuizen v Napier"],
            prompt_tips=["Consider whether direct or indirect horizontal application is appropriate"]
        ),
        KeyProvision(
            section="s9",
            title="Equality",
            description="Everyone equal before law; no unfair discrimination on listed or analogous grounds",
            common_applications=["Unfair discrimination claims", "Affirmative action", "Equal treatment disputes"],
            key_cases=["Harksen v Lane", "President of RSA v Hugo", "Minister of Finance v Van Heerden"],
            prompt_tips=["Apply Harksen v Lane test: (1) differentiation, (2) listed ground, (3) unfair discrimination"]
        ),
        KeyProvision(
            section="s10",
            title="Human Dignity",
            description="Everyone has inherent dignity and right to have dignity respected and protected",
            common_applications=["Defamation", "Privacy", "Degrading treatment", "Death penalty"],
            key_cases=["S v Makwanyane", "Dawood v Minister of Home Affairs"],
            prompt_tips=["Dignity often used alongside other rights; foundational value"]
        ),
        KeyProvision(
            section="s25",
            title="Property",
            description="No arbitrary deprivation; expropriation only with compensation; land reform provisions",
            common_applications=["Expropriation disputes", "Land reform", "Deprivation vs expropriation"],
            key_cases=["FNB v Commissioner", "Agri SA v Minister", "Mkontwana v Nelson Mandela Metro"],
            prompt_tips=["Apply FNB methodology: (1) property, (2) deprivation, (3) arbitrary, (4) expropriation, (5) compensation"]
        ),
        KeyProvision(
            section="s26",
            title="Housing",
            description="Right to access adequate housing; no arbitrary eviction without court order",
            common_applications=["Eviction matters", "Housing delivery", "Informal settlement rights"],
            key_cases=["Government v Grootboom", "PE Municipality v Various Occupiers", "Occupiers of 51 Olivia Road"],
            prompt_tips=["Progressive realisation within available resources; meaningful engagement required for eviction"]
        ),
        KeyProvision(
            section="s27",
            title="Health Care, Food, Water, Social Security",
            description="Right to access health care, food, water, social security; progressive realisation",
            common_applications=["Healthcare access", "Social grants", "Water services"],
            key_cases=["Minister of Health v TAC", "Mazibuko v City of Johannesburg"],
            prompt_tips=["Reasonableness test per Grootboom; consider available resources"]
        ),
        KeyProvision(
            section="s28",
            title="Children's Rights",
            description="Best interests of child paramount; right to family care, basic nutrition, shelter, health, social services",
            common_applications=["Child custody", "Care proceedings", "Child maintenance", "Child welfare"],
            key_cases=["S v M", "Centre for Child Law v Minister of Justice"],
            prompt_tips=["Child's best interests always paramount; self-standing rights not dependent on parents' resources"]
        ),
        KeyProvision(
            section="s33",
            title="Just Administrative Action",
            description="Right to lawful, reasonable, procedurally fair administrative action; right to written reasons",
            common_applications=["Reviewing government decisions", "PAJA claims", "Permit applications"],
            key_cases=["Bato Star v Minister", "Albutt v Centre for Study of Violence"],
            prompt_tips=["PAJA gives effect to s33; apply Bato Star reasonableness test"]
        ),
        KeyProvision(
            section="s34",
            title="Access to Courts",
            description="Right to have disputes resolved by application of law in fair public hearing",
            common_applications=["Ouster clauses", "Court access barriers", "Prescription challenges"],
            key_cases=["Chief Lesapo v North West Agricultural Bank", "Road Accident Fund v Mdeyide"],
            prompt_tips=["Includes access to other dispute resolution forums; barriers must be justified"]
        ),
        KeyProvision(
            section="s35",
            title="Arrested, Detained and Accused Persons",
            description="Rights of arrested persons, detainees, accused including fair trial, legal representation",
            common_applications=["Criminal trials", "Bail applications", "Evidence exclusion"],
            key_cases=["S v Zuma (1995)", "S v Coetzee", "Key v Attorney-General Cape"],
            prompt_tips=["Detailed fair trial rights; evidence exclusion under s35(5) is discretionary"]
        ),
        KeyProvision(
            section="s36",
            title="Limitation of Rights",
            description="Rights may be limited by law of general application if reasonable and justifiable in open and democratic society",
            common_applications=["Justifying rights limitations", "Proportionality analysis", "Balancing rights"],
            key_cases=["S v Makwanyane", "S v Manamela", "Prince v President, Law Society"],
            prompt_tips=["Apply proportionality: (1) nature of right, (2) importance of limitation purpose, (3) nature and extent, (4) relation between limitation and purpose, (5) less restrictive means"]
        ),
        KeyProvision(
            section="s39",
            title="Interpretation of Bill of Rights",
            description="Promote values; must consider international law; may consider foreign law",
            common_applications=["Constitutional interpretation", "Comparative law use", "International law application"],
            key_cases=["S v Makwanyane", "Glenister v President"],
            prompt_tips=["Generous and purposive interpretation; ubuntu as interpretive value"]
        ),
        KeyProvision(
            section="s172",
            title="Powers of Courts in Constitutional Matters",
            description="Courts must declare invalid law/conduct inconsistent with Constitution; may limit retrospective effect, suspend declaration",
            common_applications=["Remedies for constitutional violations", "Suspended declarations of invalidity"],
            key_cases=["Dawood v Minister", "Fose v Minister of Safety and Security"],
            prompt_tips=["Consider appropriate remedy: declaration, mandamus, interdict, damages, reading-in"]
        )
    ],
    important_schedules=[
        "Schedule 1: National Flag",
        "Schedule 2: Oaths and Solemn Affirmations",
        "Schedule 4: Functional Areas of Concurrent National and Provincial Legislative Competence",
        "Schedule 5: Functional Areas of Exclusive Provincial Legislative Competence",
        "Schedule 6: Transitional Arrangements"
    ],
    related_regulations=[],
    landmark_cases=[
        {"case": "Certification of the Constitution [1996] ZACC 26", "principle": "Constitutional certification process"},
        {"case": "S v Makwanyane [1995] ZACC 3", "principle": "Death penalty unconstitutional; dignity, ubuntu"},
        {"case": "Government v Grootboom [2000] ZACC 19", "principle": "Socio-economic rights; reasonableness test"},
        {"case": "Pharmaceutical Manufacturers [2000] ZACC 1", "principle": "Constitutional supremacy; no parallel common law review"},
        {"case": "Carmichele v Minister [2001] ZACC 22", "principle": "Horizontal application; state's positive duties"},
        {"case": "Harksen v Lane [1997] ZACC 12", "principle": "Equality test; unfair discrimination analysis"}
    ],
    prompt_considerations=[
        "Always identify the specific constitutional right(s) engaged",
        "Apply two-stage analysis: (1) has right been infringed? (2) is limitation justified under s36?",
        "Consider transformative constitutionalism and ubuntu values",
        "Reference Constitutional Court jurisprudence as binding precedent",
        "Distinguish vertical (state-citizen) from horizontal (citizen-citizen) application",
        "Consider remedies under s172 (declaration, suspension, reading-in, reading-down)"
    ],
    common_prompt_templates=[
        "Analyse whether [action/law] infringes s[X] of the Constitution and whether any infringement is justifiable under s36 applying the proportionality analysis from [Makwanyane/Manamela]",
        "Apply the Harksen v Lane test to determine whether [differentiation] constitutes unfair discrimination under s9",
        "Conduct a s36 limitations analysis for the infringement of [right] by [legislation], addressing all five proportionality factors",
        "Advise on the appropriate constitutional remedy under s172 for the finding that [law/action] is inconsistent with [constitutional provision]"
    ]
)

# ═══════════════════════════════════════════════════════════════════════════════
# LABOUR RELATIONS ACT
# ═══════════════════════════════════════════════════════════════════════════════

LRA = SALegislation(
    short_title="Labour Relations Act",
    act_number="Act 66 of 1995",
    full_title="Labour Relations Act",
    category=LegislationCategory.LABOUR,
    commencement_date="11 November 1996",
    purpose=[
        "Give effect to s23 right to fair labour practices",
        "Regulate trade unions and employer organisations",
        "Promote collective bargaining",
        "Regulate right to strike and lockout",
        "Provide dispute resolution mechanisms (CCMA, bargaining councils)",
        "Establish Labour Court and Labour Appeal Court"
    ],
    key_institutions={
        "CCMA": "Commission for Conciliation, Mediation and Arbitration - primary dispute resolution",
        "Bargaining Councils": "Industry-level collective bargaining and dispute resolution",
        "Labour Court": "Superior court for labour disputes (s151)",
        "Labour Appeal Court": "Appeals from Labour Court (s167)",
        "Essential Services Committee": "Designates essential services where strike prohibited"
    },
    key_provisions=[
        KeyProvision(
            section="s185",
            title="Right Not to Be Unfairly Dismissed",
            description="Every employee has right not to be unfairly dismissed or subjected to unfair labour practice",
            common_applications=["All dismissal disputes", "ULP claims"],
            key_cases=["Sidumo v Rustenburg Platinum", "NEHAWU v UCT"],
            prompt_tips=["Foundation for all unfair dismissal claims; distinguish from ULP"]
        ),
        KeyProvision(
            section="s186(1)",
            title="Definition of Dismissal",
            description="Employer terminates; employee terminates with/without notice due to employer; refuses to accept changed terms; selective re-employment after termination",
            common_applications=["Identifying dismissal type", "Constructive dismissal", "Selective re-employment"],
            key_cases=["Solidarity obo Barnard v SAPS", "Murray v Minister of Defence"],
            prompt_tips=["Prove there was a dismissal first; then analyse fairness"]
        ),
        KeyProvision(
            section="s187",
            title="Automatically Unfair Dismissals",
            description="Dismissal automatically unfair if for reasons including discrimination, pregnancy, protected disclosure, strike participation",
            common_applications=["Discrimination claims", "Whistleblower protection", "Strike-related dismissals"],
            key_cases=["NUMSA v Bader Bop", "Kroeger v Visual Marketing"],
            prompt_tips=["Higher compensation (up to 24 months); employee must prove reason, then onus shifts"]
        ),
        KeyProvision(
            section="s188",
            title="Other Unfair Dismissals",
            description="Dismissal unfair if not for fair reason (misconduct, incapacity, operational requirements) or not effected fairly",
            common_applications=["Substantive and procedural fairness analysis"],
            key_cases=["Sidumo v Rustenburg Platinum"],
            prompt_tips=["Apply Schedule 8 Code of Good Practice; both substantive and procedural fairness required"]
        ),
        KeyProvision(
            section="s189",
            title="Dismissals Based on Operational Requirements",
            description="Consultation process; selection criteria; severance pay requirements",
            common_applications=["Retrenchment disputes", "Consultation adequacy"],
            key_cases=["NUMSA v SA Airways", "CWIU v Algorax"],
            prompt_tips=["Meaningful joint consensus-seeking consultation; LIFO as default selection"]
        ),
        KeyProvision(
            section="s189A",
            title="Large-Scale Retrenchments",
            description="Facilitated process for employers employing 50+ employees contemplating 10+ dismissals",
            common_applications=["Major retrenchments", "Facilitation vs consultation"],
            key_cases=["NUMSA v SA Airways"],
            prompt_tips=["Different procedure from s189; facilitation by CCMA or private facilitator"]
        ),
        KeyProvision(
            section="s193",
            title="Remedies for Unfair Dismissal",
            description="Reinstatement, re-employment, or compensation (max 12 months, 24 for s187)",
            common_applications=["Remedy selection", "Compensation calculation"],
            key_cases=["Equity Aviation v SATAWU"],
            prompt_tips=["Reinstatement primary remedy unless not reasonably practicable; consider employment relationship viability"]
        ),
        KeyProvision(
            section="s194",
            title="Limits on Compensation",
            description="Compensation capped at 12 months remuneration (24 for s187); excludes benefits",
            common_applications=["Compensation calculation", "What counts as remuneration"],
            key_cases=["Media 24 v Grobler"],
            prompt_tips=["Remuneration includes all benefits capable of monetary quantification"]
        ),
        KeyProvision(
            section="s145",
            title="Review of Arbitration Awards",
            description="Review to Labour Court on grounds of defect, gross irregularity, exceeding powers, improperly obtained",
            common_applications=["Challenging CCMA awards", "Sidumo review standard"],
            key_cases=["Sidumo v Rustenburg Platinum", "Herholdt v Nedbank"],
            prompt_tips=["Not an appeal; Sidumo standard - 'result reasonable commissioner could reach'"]
        ),
        KeyProvision(
            section="s64",
            title="Right to Strike",
            description="Every employee has right to strike and employer has recourse to lockout subject to procedural requirements",
            common_applications=["Strike legality", "Procedural requirements"],
            key_cases=["NUMSA v Bader Bop", "AMCU v Chamber of Mines"],
            prompt_tips=["Procedural requirements: referral, 30-day conciliation, 7-day notice"]
        ),
        KeyProvision(
            section="s197",
            title="Transfer of Business as Going Concern",
            description="Automatic transfer of employment contracts; no dismissal by reason of transfer",
            common_applications=["Business sales", "Outsourcing", "Insourcing"],
            key_cases=["NEHAWU v UCT", "Aviation Union v SA Airways"],
            prompt_tips=["Determine if business transferred as 'going concern'; automatic transfer of contracts"]
        )
    ],
    important_schedules=[
        "Schedule 7: Transitional Arrangements",
        "Schedule 8: Code of Good Practice - Dismissal (critical for misconduct/incapacity)"
    ],
    related_regulations=[
        "CCMA Rules",
        "Labour Court Rules",
        "Bargaining Council Constitutions",
        "Essential Services determinations"
    ],
    landmark_cases=[
        {"case": "Sidumo v Rustenburg Platinum [2007] ZACC 22", "principle": "Review standard for CCMA awards"},
        {"case": "NEHAWU v UCT [2002] ZACC 27", "principle": "Transfer as going concern; right to fair labour practices"},
        {"case": "NUMSA v Bader Bop [2003] ZACC 11", "principle": "Automatically unfair dismissal; strike rights"},
        {"case": "Equity Aviation v SATAWU [2008] ZACC 8", "principle": "Reinstatement as primary remedy"},
        {"case": "CWIU v Algorax [2003] ZASCA 158", "principle": "Operational requirements; substantive fairness"}
    ],
    prompt_considerations=[
        "Identify type of dismissal first: misconduct, incapacity, operational requirements, or automatically unfair",
        "Apply the correct Code of Good Practice (Schedule 8 for misconduct/incapacity)",
        "Always analyse both substantive and procedural fairness",
        "For reviews, apply Sidumo standard, not appeal standard",
        "30-day referral period is jurisdictional; check condonation if late",
        "Distinguish CCMA jurisdiction from Labour Court original jurisdiction"
    ],
    common_prompt_templates=[
        "Analyse whether this dismissal for [misconduct/incapacity/operational requirements] was substantively and procedurally fair applying Schedule 8 of the LRA",
        "Advise on prospects of success for a s145 review of this CCMA award applying the Sidumo standard",
        "Draft CCMA referral statement for unfair dismissal claim identifying the nature of dismissal under s186 and grounds of unfairness under s188",
        "Analyse whether this constitutes an automatically unfair dismissal under s187 and calculate potential compensation"
    ]
)

# ═══════════════════════════════════════════════════════════════════════════════
# COMPANIES ACT
# ═══════════════════════════════════════════════════════════════════════════════

COMPANIES_ACT = SALegislation(
    short_title="Companies Act",
    act_number="Act 71 of 2008",
    full_title="Companies Act",
    category=LegislationCategory.COMMERCIAL,
    commencement_date="1 May 2011",
    purpose=[
        "Provide for incorporation, registration, organisation and management of companies",
        "Regulate capitalisation of profit companies",
        "Define relationships between companies, shareholders, and directors",
        "Facilitate mergers and takeovers",
        "Provide for business rescue of financially distressed companies",
        "Create consistent business regulation regime"
    ],
    key_institutions={
        "CIPC": "Companies and Intellectual Property Commission - registration and compliance",
        "Companies Tribunal": "Alternative dispute resolution, review of CIPC decisions",
        "Takeover Regulation Panel": "Mergers and acquisitions regulation",
        "Financial Reporting Standards Council": "Financial reporting requirements"
    },
    key_provisions=[
        KeyProvision(
            section="s66",
            title="Board Authority and Powers",
            description="Business and affairs of company managed by board, which has authority to exercise all powers except those reserved for shareholders",
            common_applications=["Director authority disputes", "Board decisions", "Delegation of powers"],
            key_cases=["Wessels v Adendorff Boerdery"],
            prompt_tips=["Check MOI for any reserved powers; board manages business"]
        ),
        KeyProvision(
            section="s76",
            title="Directors' Duties: Standards of Conduct",
            description="Directors must act in good faith, for proper purpose, in best interests of company, with care, skill and diligence",
            common_applications=["Breach of fiduciary duty", "Negligence claims", "Business judgment rule"],
            key_cases=["Visser Sitrus v Goede Hoop Sitrus"],
            prompt_tips=["Business judgment rule in s76(4); good faith and rational belief required"]
        ),
        KeyProvision(
            section="s77",
            title="Liability of Directors",
            description="Directors liable for breach of duty, acting without authority, acquiescing in prohibited conduct",
            common_applications=["Director liability claims", "Breach of fiduciary duty", "Reckless trading"],
            key_cases=["Pottie v Kotze"],
            prompt_tips=["Joint and several liability possible; consider D&O insurance"]
        ),
        KeyProvision(
            section="s128-154",
            title="Business Rescue (Chapter 6)",
            description="Facilitate rehabilitation of financially distressed company as alternative to liquidation",
            common_applications=["Avoiding liquidation", "Restructuring", "Creditor compromises"],
            key_cases=["Oakdene Square Properties v Farm Bothasfontein", "Koen v Wedgewood Village"],
            prompt_tips=["Reasonable prospect of rescue required; moratorium on claims during rescue"]
        ),
        KeyProvision(
            section="s129",
            title="Company Resolution to Begin Business Rescue",
            description="Board may resolve to commence business rescue if financially distressed with reasonable prospect",
            common_applications=["Voluntary business rescue", "Board resolutions"],
            key_cases=["Oakdene Square Properties"],
            prompt_tips=["Must pass resolution; appoint practitioner within 5 days; notify affected persons"]
        ),
        KeyProvision(
            section="s131",
            title="Court Order to Begin Business Rescue",
            description="Affected person may apply to court for business rescue order",
            common_applications=["Involuntary business rescue", "Creditor applications"],
            key_cases=["Koen v Wedgewood Village"],
            prompt_tips=["Just and equitable grounds; reasonable prospect test"]
        ),
        KeyProvision(
            section="s163",
            title="Relief from Oppressive Conduct",
            description="Shareholders may apply to court if oppressive, unfairly prejudicial, or disregards interests",
            common_applications=["Minority shareholder oppression", "Squeeze-out disputes", "Deadlock situations"],
            key_cases=["Grancy Property v Manala"],
            prompt_tips=["Wide remedial powers; can order buyout, winding up, etc."]
        ),
        KeyProvision(
            section="s165",
            title="Derivative Actions",
            description="Demand on company to sue; court permission if company fails to act",
            common_applications=["Suing directors on company's behalf", "Minority shareholder remedies"],
            key_cases=["Lewis Group v Woollam"],
            prompt_tips=["Demand must be made unless futile; legal costs issues"]
        ),
        KeyProvision(
            section="s22",
            title="Reckless Trading",
            description="Prohibited to carry on business recklessly, with gross negligence, or intent to defraud",
            common_applications=["Director liability in insolvency", "Trading while insolvent"],
            key_cases=["Van der Berg v Pottie", "Pottie v Kotze"],
            prompt_tips=["Personal liability for company debts; consider wrongful trading"]
        ),
        KeyProvision(
            section="s112-115",
            title="Fundamental Transactions",
            description="Proposals to dispose of all/greater part of assets, amalgamation, merger - require special resolution and appraisal rights",
            common_applications=["M&A transactions", "Asset sales", "Shareholder appraisal"],
            key_cases=["Caxton & CTP Publishers v Naspers"],
            prompt_tips=["Appraisal remedy under s164 if dissenting; court approval may be required"]
        )
    ],
    important_schedules=[
        "Schedule 1: Tables setting out provisions of Companies Act 61 of 1973 that remain in force",
        "Schedule 5: Transitional Arrangements"
    ],
    related_regulations=[
        "Companies Regulations 2011",
        "Companies Tribunal Rules",
        "Takeover Regulations"
    ],
    landmark_cases=[
        {"case": "Oakdene Square Properties v Farm Bothasfontein [2012] ZASCA 135", "principle": "Business rescue requirements"},
        {"case": "Grancy Property v Manala [2015] ZASCA 11", "principle": "Oppression remedy scope"},
        {"case": "Koen v Wedgewood Village [2012] ZAWCHC 4", "principle": "Court-ordered business rescue"},
        {"case": "Lewis Group v Woollam [2017] ZASCA 24", "principle": "Derivative actions"}
    ],
    prompt_considerations=[
        "Always check the MOI - it may alter default Act provisions",
        "Distinguish profit companies from non-profit companies",
        "Business rescue has strict timelines - check each deadline",
        "Director duties are both statutory (s76) and common law",
        "CIPC filings have compliance consequences"
    ],
    common_prompt_templates=[
        "Analyse whether the director breached their duties under s76 and the potential liability under s77, considering the business judgment rule defence",
        "Advise on whether business rescue under Chapter 6 is appropriate for this financially distressed company, applying the Oakdene Square test",
        "Draft a s163 oppression remedy application identifying the oppressive conduct and appropriate relief sought",
        "Analyse this transaction to determine if it qualifies as a s112 fundamental transaction requiring special resolution and appraisal rights"
    ]
)

# ═══════════════════════════════════════════════════════════════════════════════
# PROTECTION OF PERSONAL INFORMATION ACT (POPIA)
# ═══════════════════════════════════════════════════════════════════════════════

POPIA = SALegislation(
    short_title="POPIA",
    act_number="Act 4 of 2013",
    full_title="Protection of Personal Information Act",
    category=LegislationCategory.DATA_PROTECTION,
    commencement_date="1 July 2020 (full compliance from 1 July 2021)",
    purpose=[
        "Promote protection of personal information",
        "Balance right to privacy against other rights (access to information, freedom of expression)",
        "Regulate manner in which personal information may be processed",
        "Establish Information Regulator to enforce compliance"
    ],
    key_institutions={
        "Information Regulator": "Enforce POPIA and PAIA; receive complaints; issue guidance",
        "Responsible Party": "Entity that determines purpose and means of processing",
        "Operator": "Processes personal information on behalf of responsible party",
        "Information Officer": "Appointed by responsible party to ensure POPIA compliance"
    },
    key_provisions=[
        KeyProvision(
            section="s1",
            title="Definitions",
            description="Defines personal information, processing, responsible party, operator, data subject",
            common_applications=["Scope of POPIA", "What constitutes personal information"],
            key_cases=["Information Regulator enforcement notices"],
            prompt_tips=["Personal information is very broadly defined; includes opinions about the person"]
        ),
        KeyProvision(
            section="s8-25",
            title="Eight Conditions for Lawful Processing",
            description="Accountability, Processing limitation, Purpose specification, Further processing limitation, Information quality, Openness, Security safeguards, Data subject participation",
            common_applications=["Compliance assessments", "Processing activities", "Data protection impact assessments"],
            key_cases=["Various IR enforcement actions"],
            prompt_tips=["All eight conditions must be met; most important are processing limitation and purpose specification"]
        ),
        KeyProvision(
            section="s11",
            title="Consent, Justification and Objection",
            description="Processing only permitted with consent or other justification; data subject may object",
            common_applications=["Consent mechanisms", "Marketing consent", "Objection to processing"],
            key_cases=["Information Regulator v WhatsApp (pending)"],
            prompt_tips=["Consent must be voluntary, specific, informed; other grounds exist (contract, legal obligation, legitimate interest)"]
        ),
        KeyProvision(
            section="s14",
            title="Purpose Specification",
            description="Personal information must be collected for specific, explicitly defined, lawful purpose related to function of responsible party",
            common_applications=["Data collection practices", "Privacy policies", "Purpose limitation"],
            key_cases=["IR enforcement notices"],
            prompt_tips=["Cannot collect for undefined purposes; purpose must be communicated to data subject"]
        ),
        KeyProvision(
            section="s19",
            title="Security Safeguards",
            description="Appropriate technical and organisational measures to protect personal information against loss, damage, unlawful access",
            common_applications=["Data security requirements", "Breach prevention", "Operator contracts"],
            key_cases=["Experian data breach investigation"],
            prompt_tips=["Reasonable measures taking into account nature of information and risks"]
        ),
        KeyProvision(
            section="s22",
            title="Notification of Security Compromises",
            description="Must notify Information Regulator and data subject of security compromise as soon as reasonably possible",
            common_applications=["Data breach response", "Notification requirements"],
            key_cases=["TransUnion breach notification"],
            prompt_tips=["Notify 'as soon as reasonably possible'; may delay if investigation requires or law enforcement requests"]
        ),
        KeyProvision(
            section="s26-33",
            title="Special Personal Information",
            description="Religious/philosophical beliefs, race/ethnicity, trade union membership, political persuasion, health/sex life, biometric information, criminal history - prohibited processing except with consent or specific exceptions",
            common_applications=["HR data", "Health data", "Criminal checks"],
            key_cases=["IR guidance on employee health screening"],
            prompt_tips=["Stricter requirements; general prohibition with limited exceptions"]
        ),
        KeyProvision(
            section="s69-72",
            title="Prior Authorisation",
            description="Certain processing requires prior authorisation from Information Regulator",
            common_applications=["Credit reporting", "Criminal record processing", "Data matching"],
            key_cases=["Credit bureau authorisation"],
            prompt_tips=["Check if processing activity triggers prior authorisation requirement"]
        ),
        KeyProvision(
            section="s99-106",
            title="Offences, Penalties and Administrative Fines",
            description="Criminal offences for obstruction, unlawful acts; administrative fines up to R10 million",
            common_applications=["Enforcement actions", "Penalty calculation"],
            key_cases=["Department of Justice fine (first major fine)"],
            prompt_tips=["Both criminal and administrative sanctions; directors can be personally liable"]
        )
    ],
    important_schedules=[],
    related_regulations=[
        "POPIA Regulations",
        "Information Regulator Guidelines",
        "Codes of Conduct (various industries)"
    ],
    landmark_cases=[
        {"case": "Information Regulator v Department of Justice", "principle": "First major enforcement fine"},
        {"case": "TransUnion breach notification", "principle": "Security compromise notification requirements"}
    ],
    prompt_considerations=[
        "Identify the responsible party and any operators",
        "Determine lawful basis for processing (consent is only one of several)",
        "Check if special personal information provisions apply",
        "Cross-border transfers require adequate protection",
        "Consider intersection with sector-specific laws (NCA, FAIS, Banking, etc.)",
        "Remember POPIA is compared to GDPR but has differences"
    ],
    common_prompt_templates=[
        "Conduct a POPIA compliance assessment for [organisation] processing [type of data] for [purpose], addressing all eight conditions for lawful processing",
        "Draft a privacy policy/POPI statement for [organisation] that meets s18 notification requirements",
        "Advise on POPIA breach response obligations following [security incident] and prepare notification to Information Regulator",
        "Analyse whether this cross-border transfer of personal information to [country] complies with s72 POPIA requirements"
    ]
)

# ═══════════════════════════════════════════════════════════════════════════════
# CONSUMER PROTECTION ACT
# ═══════════════════════════════════════════════════════════════════════════════

CONSUMER_PROTECTION_ACT = SALegislation(
    short_title="Consumer Protection Act",
    act_number="Act 68 of 2008",
    full_title="Consumer Protection Act",
    category=LegislationCategory.CONSUMER,
    commencement_date="31 March 2011",
    purpose=[
        "Promote fair, accessible and sustainable marketplace",
        "Protect consumers from unfair business practices",
        "Improve consumer awareness and information",
        "Provide effective redress for consumers",
        "Establish national norms and standards"
    ],
    key_institutions={
        "NCC": "National Consumer Commission - enforcement and compliance monitoring",
        "NCT": "National Consumer Tribunal - adjudication of complaints",
        "Consumer Courts": "Provincial consumer dispute resolution",
        "Ombud schemes": "Industry-specific complaint resolution (Motor Industry Ombud, etc.)"
    },
    key_provisions=[
        KeyProvision(
            section="s5",
            title="Application of Act",
            description="Applies to promotion, supply of goods or services in ordinary course of business for consideration; excludes certain transactions",
            common_applications=["Determining CPA application", "Exclusions (B2B, large transactions)"],
            key_cases=["Mercurio v Fortes"],
            prompt_tips=["Check thresholds and exclusions; does not apply to transactions above threshold or B2B above threshold"]
        ),
        KeyProvision(
            section="s22",
            title="Right to Information in Plain and Understandable Language",
            description="Notices, documents, visual representations must be in plain language",
            common_applications=["Contract drafting", "Terms and conditions", "Notices"],
            key_cases=["Various NCT decisions"],
            prompt_tips=["Ordinary consumer with average literacy and minimal experience must understand"]
        ),
        KeyProvision(
            section="s48",
            title="Unfair, Unreasonable or Unjust Contract Terms",
            description="Terms that are excessively one-sided, so adverse to consumer as to be inequitable, or contrary to fair dealing are void",
            common_applications=["Exemption clauses", "Unfair terms challenges"],
            key_cases=["Naidoo v Birchwood Hotel"],
            prompt_tips=["s49 requires supplier to draw attention to limitation clauses; even then can be void"]
        ),
        KeyProvision(
            section="s54",
            title="Consumer's Right to Demand Quality Service",
            description="Consumer entitled to timely performance and completion; notice and opportunity to remedy defects",
            common_applications=["Service complaints", "Remedy demands"],
            key_cases=["NCT service quality decisions"],
            prompt_tips=["Consumer can demand refund of reasonable portion if service defective"]
        ),
        KeyProvision(
            section="s55",
            title="Consumer's Right to Safe, Good Quality Goods",
            description="Implied warranty of quality; goods must be safe, of good quality, suitable for purpose, durable",
            common_applications=["Defective goods claims", "Product recalls"],
            key_cases=["Eskom v Halstead-Cleak"],
            prompt_tips=["Six-month implied warranty; consumer can choose refund, repair, or replacement"]
        ),
        KeyProvision(
            section="s56",
            title="Implied Warranty of Quality",
            description="Within 6 months, consumer can return defective goods for refund, repair, or replacement at consumer's choice",
            common_applications=["Product returns", "Defective goods remedies"],
            key_cases=["Motor industry complaints"],
            prompt_tips=["No-returns policies illegal for defective goods; consumer chooses remedy in first 6 months"]
        ),
        KeyProvision(
            section="s61",
            title="Liability for Damage Caused by Goods",
            description="Strict liability of producers, importers, distributors, retailers for harm caused by unsafe or defective goods",
            common_applications=["Product liability claims", "Class actions"],
            key_cases=["Boeing v Minister of Finance (exemption clauses)"],
            prompt_tips=["Strict liability - no negligence required; includes consequential damages"]
        ),
        KeyProvision(
            section="s14",
            title="Right to Choose",
            description="Consumer may select supplier; bundling prohibited unless economic benefit to consumer",
            common_applications=["Tied selling complaints", "Bundling challenges"],
            key_cases=["NCT bundling decisions"],
            prompt_tips=["Cannot force consumer to buy unwanted goods with wanted goods"]
        ),
        KeyProvision(
            section="s17",
            title="Lay-by Agreements",
            description="Requirements for lay-by purchases; full refund minus reasonable charge if consumer cancels",
            common_applications=["Retail lay-by disputes"],
            key_cases=["NCT lay-by decisions"],
            prompt_tips=["Specific rules for lay-bys; consumer protection even on cancellation"]
        )
    ],
    important_schedules=[
        "Schedule 2: Product labelling requirements"
    ],
    related_regulations=[
        "CPA Regulations",
        "Industry codes of conduct",
        "Provincial consumer protection legislation"
    ],
    landmark_cases=[
        {"case": "Naidoo v Birchwood Hotel [2012] ZASCA 170", "principle": "Unfair contract terms; exemption clauses"},
        {"case": "Eskom v Halstead-Cleak [2017] ZASCA 51", "principle": "Product liability under CPA"}
    ],
    prompt_considerations=[
        "First check if CPA applies (B2C, below threshold, not excluded)",
        "Consumer has choice of remedies for defective goods in first 6 months",
        "Exemption clauses that limit liability are suspect; s49 formalities required",
        "Plain language requirement affects all consumer-facing documents",
        "Strict product liability extends supply chain"
    ],
    common_prompt_templates=[
        "Analyse whether this [contract term/exemption clause] is enforceable under s48/s49 of the Consumer Protection Act",
        "Advise consumer on their rights under s55-56 for defective [product] purchased [timeframe] ago",
        "Draft CPA-compliant terms and conditions for [retail business] including plain language and s49 notices",
        "Analyse product liability claim under s61 CPA for harm caused by [defective product]"
    ]
)

# ═══════════════════════════════════════════════════════════════════════════════
# ALL LEGISLATION COLLECTION
# ═══════════════════════════════════════════════════════════════════════════════

ALL_LEGISLATION: Dict[str, SALegislation] = {
    "Constitution": CONSTITUTION,
    "LRA": LRA,
    "Companies Act": COMPANIES_ACT,
    "POPIA": POPIA,
    "CPA": CONSUMER_PROTECTION_ACT,
}

def get_legislation_by_category(category: LegislationCategory) -> List[SALegislation]:
    """Get all legislation in a specific category"""
    return [leg for leg in ALL_LEGISLATION.values() if leg.category == category]

def get_provision(legislation_key: str, section: str) -> Optional[KeyProvision]:
    """Get a specific provision from legislation"""
    leg = ALL_LEGISLATION.get(legislation_key)
    if leg:
        for prov in leg.key_provisions:
            if prov.section == section:
                return prov
    return None

def generate_legislation_prompt(legislation: SALegislation, issue: str) -> str:
    """Generate a prompt incorporating legislation guidance"""
    return f"""
# SA Legal Analysis: {legislation.short_title} ({legislation.act_number})

## Issue
{issue}

## Applicable Legislation
**{legislation.full_title}** ({legislation.act_number})

## Purpose of the Act
{chr(10).join(f"• {p}" for p in legislation.purpose)}

## Key Institutions
{chr(10).join(f"• **{k}**: {v}" for k, v in legislation.key_institutions.items())}

## Prompt Considerations
{chr(10).join(f"⚠️ {c}" for c in legislation.prompt_considerations)}

## Landmark Cases to Consider
{chr(10).join(f"• **{c['case']}**: {c['principle']}" for c in legislation.landmark_cases)}

## Analysis Framework
Apply the relevant provisions and consider:
1. Identify the specific section(s) applicable
2. Reference leading case law
3. Apply the law to the facts
4. Consider any defences or exceptions
5. Advise on remedies

IMPORTANT: Cite SAFLII neutral citations for all cases.
"""

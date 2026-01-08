"""
🇿🇦 SA Specialist Courts & Tribunals
Comprehensive Database of South African Specialist Courts, Tribunals, and Forums
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional

class CourtCategory(Enum):
    """Categories of SA Courts and Tribunals"""
    SUPERIOR = "Superior Courts"
    MAGISTRATES = "Magistrates' Courts"
    SPECIALIST_SUPERIOR = "Specialist Superior Courts"
    SPECIALIST_LOWER = "Specialist Lower Courts"
    TRIBUNALS = "Tribunals & Commissions"
    TRADITIONAL = "Traditional & Customary Forums"
    MILITARY = "Military Courts"

class JurisdictionType(Enum):
    """Types of jurisdiction"""
    ORIGINAL = "Original Jurisdiction"
    APPELLATE = "Appellate Jurisdiction"
    REVIEW = "Review Jurisdiction"
    CONCURRENT = "Concurrent Jurisdiction"
    EXCLUSIVE = "Exclusive Jurisdiction"

@dataclass
class SpecialistCourt:
    """Comprehensive Specialist Court Definition"""
    name: str
    abbreviation: str
    saflii_code: str
    category: CourtCategory
    jurisdiction_type: JurisdictionType
    establishing_legislation: str
    subject_matter: List[str]
    monetary_jurisdiction: Optional[str]
    geographic_jurisdiction: str
    composition: str
    presiding_officers: List[str]
    appeal_route: str
    key_procedures: List[str]
    common_matters: List[str]
    prompt_considerations: List[str]
    citation_format: str

# ═══════════════════════════════════════════════════════════════════════════════
# SPECIALIST SUPERIOR COURTS
# ═══════════════════════════════════════════════════════════════════════════════

LABOUR_COURT = SpecialistCourt(
    name="Labour Court of South Africa",
    abbreviation="LC",
    saflii_code="ZALC",
    category=CourtCategory.SPECIALIST_SUPERIOR,
    jurisdiction_type=JurisdictionType.EXCLUSIVE,
    establishing_legislation="Labour Relations Act 66 of 1995, s151",
    subject_matter=[
        "Unfair labour practice disputes (on review from CCMA)",
        "Unfair dismissal disputes (on review from CCMA)",
        "Interpretation of collective agreements",
        "Urgent labour applications",
        "Disputes about freedom of association",
        "Essential services disputes",
        "Secondary strikes",
        "Picketing orders",
        "Organisational rights disputes",
        "Review of CCMA awards (s145)"
    ],
    monetary_jurisdiction="Unlimited in labour matters",
    geographic_jurisdiction="National (sittings in major centres)",
    composition="Single judge; Full bench for important matters",
    presiding_officers=["Labour Court Judges (appointed by President)"],
    appeal_route="Labour Appeal Court (LAC)",
    key_procedures=[
        "Statement of case (not pleadings)",
        "Pre-trial conferences mandatory",
        "Limited discovery",
        "Urgent applications under s158(1)",
        "Review applications under s145 LRA",
        "Condonation for late filing"
    ],
    common_matters=[
        "S145 reviews of CCMA arbitration awards",
        "S158 interdicts against strikes",
        "Automatically unfair dismissal claims",
        "Organisational rights disputes",
        "Bargaining council disputes"
    ],
    prompt_considerations=[
        "Apply Sidumo v Rustenburg Platinum Mines for review standard",
        "Consider 6-week time limit for s145 reviews",
        "Reference CCMA arbitration award under review",
        "Address condonation if application late",
        "Consider Labour Court Practice Manual procedures"
    ],
    citation_format="[Party names] [Case number] [Year] ZALC [Number] ([Date])"
)

LABOUR_APPEAL_COURT = SpecialistCourt(
    name="Labour Appeal Court",
    abbreviation="LAC",
    saflii_code="ZALAC",
    category=CourtCategory.SPECIALIST_SUPERIOR,
    jurisdiction_type=JurisdictionType.APPELLATE,
    establishing_legislation="Labour Relations Act 66 of 1995, s167",
    subject_matter=[
        "Appeals from Labour Court",
        "Appeals from Labour Court's review of CCMA awards",
        "Constitutional matters arising in labour disputes",
        "Cross-appeals in labour matters"
    ],
    monetary_jurisdiction="Unlimited",
    geographic_jurisdiction="National",
    composition="Three judges (two Labour Court judges and one High Court judge)",
    presiding_officers=["Judge President of Labour Appeal Court", "Labour Court Judges", "High Court Judges"],
    appeal_route="Constitutional Court (constitutional matters only) or SCA (rare)",
    key_procedures=[
        "Leave to appeal required",
        "Heads of argument mandatory",
        "Limited oral argument",
        "No new evidence generally"
    ],
    common_matters=[
        "Appeals on Sidumo review standard application",
        "Automatically unfair dismissal appeals",
        "Interpretation of LRA provisions",
        "Collective bargaining disputes"
    ],
    prompt_considerations=[
        "LAC judgments bind Labour Court",
        "Consider whether leave to appeal was granted",
        "Reference Labour Court judgment under appeal",
        "Apply correct standard of appeal (not review)"
    ],
    citation_format="[Party names] [Case number] [Year] ZALAC [Number] ([Date])"
)

LAND_CLAIMS_COURT = SpecialistCourt(
    name="Land Claims Court",
    abbreviation="LCC",
    saflii_code="ZALCC",
    category=CourtCategory.SPECIALIST_SUPERIOR,
    jurisdiction_type=JurisdictionType.EXCLUSIVE,
    establishing_legislation="Restitution of Land Rights Act 22 of 1994",
    subject_matter=[
        "Land restitution claims",
        "Disputes arising from land reform",
        "Eviction matters under ESTA and PIE",
        "Disputes about land tenure rights",
        "Compensation for expropriation",
        "Farm dweller rights"
    ],
    monetary_jurisdiction="Unlimited in land matters",
    geographic_jurisdiction="National",
    composition="Single judge; Full bench for complex matters",
    presiding_officers=["Land Claims Court Judges"],
    appeal_route="Supreme Court of Appeal",
    key_procedures=[
        "Claim lodgement with Land Claims Commissioner",
        "Mediation attempts before litigation",
        "Site inspections common",
        "Historical evidence important",
        "Community participation"
    ],
    common_matters=[
        "Restitution of rights in land",
        "ESTA evictions",
        "PIE Act evictions (rural)",
        "Compensation disputes",
        "Labour tenant claims"
    ],
    prompt_considerations=[
        "Consider historical dispossession evidence",
        "Reference Restitution Act and ESTA",
        "Apply constitutional property rights (s25)",
        "Consider community rights and traditional authority",
        "Address compensation methodology"
    ],
    citation_format="[Party names] [Case number] [Year] ZALCC [Number] ([Date])"
)

COMPETITION_APPEAL_COURT = SpecialistCourt(
    name="Competition Appeal Court",
    abbreviation="CAC",
    saflii_code="ZACAC",
    category=CourtCategory.SPECIALIST_SUPERIOR,
    jurisdiction_type=JurisdictionType.APPELLATE,
    establishing_legislation="Competition Act 89 of 1998",
    subject_matter=[
        "Appeals from Competition Tribunal decisions",
        "Review of Competition Commission decisions",
        "Merger and acquisition appeals",
        "Prohibited practice decisions",
        "Exemption applications"
    ],
    monetary_jurisdiction="Unlimited",
    geographic_jurisdiction="National",
    composition="Three judges (one High Court judge as presiding, two assessors with competition expertise)",
    presiding_officers=["High Court Judge (as President)", "Two assessors"],
    appeal_route="Constitutional Court (constitutional matters) or Supreme Court of Appeal",
    key_procedures=[
        "Notice of appeal within 20 business days",
        "Record from Tribunal",
        "Heads of argument",
        "Limited new evidence"
    ],
    common_matters=[
        "Merger prohibition appeals",
        "Cartel penalty appeals",
        "Abuse of dominance appeals",
        "Conditional merger appeals"
    ],
    prompt_considerations=[
        "Reference Competition Tribunal decision",
        "Apply Competition Act definitions precisely",
        "Consider economic evidence and market definition",
        "Address public interest considerations"
    ],
    citation_format="[Party names] [Case number] [Year] ZACAC [Number] ([Date])"
)

ELECTORAL_COURT = SpecialistCourt(
    name="Electoral Court",
    abbreviation="EC",
    saflii_code="ZAEC",
    category=CourtCategory.SPECIALIST_SUPERIOR,
    jurisdiction_type=JurisdictionType.EXCLUSIVE,
    establishing_legislation="Electoral Commission Act 51 of 1996, s18",
    subject_matter=[
        "Appeals from Electoral Commission decisions",
        "Electoral disputes",
        "Voter roll disputes",
        "Party registration disputes",
        "Election result challenges",
        "IEC conduct reviews"
    ],
    monetary_jurisdiction="N/A (non-monetary disputes)",
    geographic_jurisdiction="National",
    composition="Chairperson (Judge) and two other members",
    presiding_officers=["Judge as Chairperson", "Two other members appointed by Chief Justice"],
    appeal_route="Constitutional Court (final on electoral matters)",
    key_procedures=[
        "Urgent procedures for election periods",
        "Strict time limits during elections",
        "Public hearings",
        "IEC as necessary party"
    ],
    common_matters=[
        "Voter registration disputes",
        "Candidate nomination disputes",
        "Election irregularity complaints",
        "Party funding disputes"
    ],
    prompt_considerations=[
        "Electoral matters often urgent with strict deadlines",
        "Consider Electoral Act time limits",
        "Reference IEC regulations",
        "Constitutional right to vote (s19) central"
    ],
    citation_format="[Party names] [Case number] [Year] ZAEC [Number] ([Date])"
)

# ═══════════════════════════════════════════════════════════════════════════════
# SPECIALIST LOWER COURTS
# ═══════════════════════════════════════════════════════════════════════════════

TAX_COURT = SpecialistCourt(
    name="Tax Court",
    abbreviation="TC",
    saflii_code="ZATC",
    category=CourtCategory.SPECIALIST_LOWER,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="Tax Administration Act 28 of 2011, s116",
    subject_matter=[
        "Appeals against SARS assessments",
        "Disputes about tax liability",
        "Penalties and interest disputes",
        "Income tax disputes",
        "VAT disputes",
        "Estate duty disputes",
        "Transfer duty disputes"
    ],
    monetary_jurisdiction="Unlimited in tax matters",
    geographic_jurisdiction="Provincial (Tax Courts in each province)",
    composition="Judge/Regional Magistrate as president, plus two assessors (accountant and representative of commerce)",
    presiding_officers=["Judge or Senior Magistrate", "Accountant assessor", "Commercial representative assessor"],
    appeal_route="High Court (full bench) or Supreme Court of Appeal",
    key_procedures=[
        "Objection to SARS first required",
        "Appeal after objection disallowed",
        "ADR process available",
        "In camera hearings (confidential)",
        "SARS bears burden in penalties"
    ],
    common_matters=[
        "Income tax assessments",
        "VAT assessments",
        "Transfer pricing disputes",
        "GAAR (General Anti-Avoidance Rule) disputes",
        "Penalty and interest appeals"
    ],
    prompt_considerations=[
        "Start with SARS objection process",
        "Consider ADR before litigation",
        "Tax Court proceedings are confidential",
        "Apply burden of proof rules correctly",
        "Reference Tax Administration Act procedures"
    ],
    citation_format="[Anonymised Party] v CSARS [Case number] [Year] ZATC [Number] ([Date])"
)

SMALL_CLAIMS_COURT = SpecialistCourt(
    name="Small Claims Court",
    abbreviation="SCC",
    saflii_code="ZASCC",
    category=CourtCategory.SPECIALIST_LOWER,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="Small Claims Courts Act 61 of 1984",
    subject_matter=[
        "Civil claims up to monetary limit",
        "Delivery of property up to monetary limit",
        "Liquid document claims",
        "Ejectment from premises"
    ],
    monetary_jurisdiction="R20,000 (as of 2024 - check current limit)",
    geographic_jurisdiction="District-based",
    composition="Commissioner (qualified attorney or advocate)",
    presiding_officers=["Small Claims Court Commissioner"],
    appeal_route="Magistrates' Court (on questions of law only)",
    key_procedures=[
        "No legal representation allowed",
        "Informal procedures",
        "Commissioner assists parties",
        "Limited postponements",
        "Immediate enforcement of orders"
    ],
    common_matters=[
        "Consumer complaints",
        "Landlord-tenant disputes under R20,000",
        "Minor contractual claims",
        "Small debt collection",
        "Damage claims"
    ],
    prompt_considerations=[
        "No attorneys - advise on self-representation",
        "Prepare simple, clear arguments",
        "Focus on documentary evidence",
        "Commissioner will guide procedure",
        "Limited appeal rights"
    ],
    citation_format="Generally not reported - no standard citation"
)

EQUALITY_COURT = SpecialistCourt(
    name="Equality Court",
    abbreviation="EqC",
    saflii_code="ZAEQC",
    category=CourtCategory.SPECIALIST_LOWER,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="Promotion of Equality and Prevention of Unfair Discrimination Act 4 of 2000 (PEPUDA)",
    subject_matter=[
        "Unfair discrimination complaints",
        "Hate speech complaints",
        "Harassment complaints",
        "Equality-related constitutional rights"
    ],
    monetary_jurisdiction="Can award damages up to Magistrates' Court limit",
    geographic_jurisdiction="Designated Magistrates' Courts and High Courts",
    composition="Presiding officer (Magistrate or Judge) with clerk",
    presiding_officers=["Equality Court Presiding Officer (designated magistrate)", "High Court Judge (for High Court sitting)"],
    appeal_route="High Court (from Magistrates' Court sitting); SCA (from High Court sitting)",
    key_procedures=[
        "Complaint form filed with clerk",
        "Referral to SAHRC first possible",
        "No court fees",
        "Inquisitorial procedure",
        "No legal representation required",
        "Presiding officer assists parties"
    ],
    common_matters=[
        "Workplace discrimination (non-LRA)",
        "Hate speech complaints",
        "Service refusal based on protected grounds",
        "Disability discrimination",
        "Gender discrimination"
    ],
    prompt_considerations=[
        "Apply Harksen v Lane test for unfair discrimination",
        "Consider PEPUDA s14 factors",
        "Distinguish from LRA unfair discrimination claims",
        "Reference s9 Constitution for equality",
        "Consider SAHRC involvement"
    ],
    citation_format="[Party names] [Case number] [Year] ZAEQC [Number] ([Date])"
)

MAINTENANCE_COURT = SpecialistCourt(
    name="Maintenance Court",
    abbreviation="MC",
    saflii_code="ZAMC",
    category=CourtCategory.SPECIALIST_LOWER,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="Maintenance Act 99 of 1998",
    subject_matter=[
        "Maintenance orders for children",
        "Spousal maintenance",
        "Variation of maintenance orders",
        "Enforcement of maintenance orders",
        "Maintenance investigations"
    ],
    monetary_jurisdiction="Unlimited in maintenance matters",
    geographic_jurisdiction="District Magistrates' Courts",
    composition="Maintenance Officer (administrative), Magistrate (adjudication)",
    presiding_officers=["Magistrate", "Maintenance Officer"],
    appeal_route="High Court",
    key_procedures=[
        "Application to Maintenance Officer",
        "Investigation by Maintenance Officer",
        "Maintenance inquiry before Magistrate",
        "Mediation encouraged",
        "Emoluments attachment orders",
        "Criminal prosecution for non-payment (s31)"
    ],
    common_matters=[
        "Child maintenance claims",
        "Enforcement against defaulters",
        "Variation applications",
        "Spousal maintenance post-divorce",
        "Paternity disputes linked to maintenance"
    ],
    prompt_considerations=[
        "Consider means of both parties",
        "Best interests of child paramount",
        "Reference s28 Constitution (children's rights)",
        "Address enforcement mechanisms",
        "Consider SASSA grants and other income"
    ],
    citation_format="Not typically reported"
)

SEXUAL_OFFENCES_COURT = SpecialistCourt(
    name="Sexual Offences Court",
    abbreviation="SOC",
    saflii_code="ZASOC",
    category=CourtCategory.SPECIALIST_LOWER,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="Criminal Law (Sexual Offences and Related Matters) Amendment Act 32 of 2007; Magistrates' Courts Act",
    subject_matter=[
        "Rape and sexual assault",
        "Sexual offences against children",
        "Trafficking for sexual purposes",
        "Sexual exploitation",
        "Child pornography",
        "Exposure and flashing"
    ],
    monetary_jurisdiction="N/A (criminal jurisdiction)",
    geographic_jurisdiction="Designated Regional Courts",
    composition="Specialised magistrate with trauma-informed training",
    presiding_officers=["Regional Magistrate with specialised training"],
    appeal_route="High Court",
    key_procedures=[
        "In camera proceedings",
        "Special arrangements for vulnerable witnesses",
        "Intermediaries for child witnesses",
        "One-stop centres (Thuthuzela Care Centres)",
        "Victim-centred approach",
        "Fast-tracking of cases"
    ],
    common_matters=[
        "Rape prosecutions",
        "Child sexual abuse",
        "Domestic sexual violence",
        "Sexual assault",
        "Compelled HIV testing"
    ],
    prompt_considerations=[
        "Trauma-informed approach essential",
        "Victim privacy protections",
        "Special evidentiary rules for children",
        "Consider civil claims parallel to criminal",
        "Sentencing guidelines for sexual offences"
    ],
    citation_format="S v [Accused] [Case number] - often unreported"
)

CHILDRENS_COURT = SpecialistCourt(
    name="Children's Court",
    abbreviation="CC",
    saflii_code="ZACHC",
    category=CourtCategory.SPECIALIST_LOWER,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="Children's Act 38 of 2005",
    subject_matter=[
        "Child in need of care and protection",
        "Foster care placements",
        "Adoption orders",
        "Parental rights and responsibilities",
        "Child abduction (civil aspects)",
        "Contribution orders"
    ],
    monetary_jurisdiction="N/A (welfare jurisdiction)",
    geographic_jurisdiction="Every Magistrates' Court is a Children's Court",
    composition="Presiding officer (magistrate) with training in children's matters",
    presiding_officers=["Children's Court Presiding Officer", "Assistant Presiding Officer"],
    appeal_route="High Court",
    key_procedures=[
        "Social worker investigation (s155)",
        "Best interests of child paramount",
        "Child participation (age-appropriate)",
        "Family group conferences",
        "Legal representation for child (curator ad litem)",
        "In camera proceedings"
    ],
    common_matters=[
        "Care and protection proceedings",
        "Foster care reviews",
        "Adoption applications",
        "Alternative care arrangements",
        "Contribution orders against parents"
    ],
    prompt_considerations=[
        "Best interests of child (s7 Children's Act) is paramount",
        "Reference s28 Constitution (children's rights)",
        "Consider child's views (s10 Children's Act)",
        "Social worker reports essential",
        "Apply ubuntu and family preservation principles"
    ],
    citation_format="In re: [Child's initials] [Case number]"
)

CHILD_JUSTICE_COURT = SpecialistCourt(
    name="Child Justice Court",
    abbreviation="CJC",
    saflii_code="ZACJC",
    category=CourtCategory.SPECIALIST_LOWER,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="Child Justice Act 75 of 2008",
    subject_matter=[
        "Criminal matters involving children (under 18)",
        "Preliminary inquiries",
        "Diversion orders",
        "Sentencing of child offenders"
    ],
    monetary_jurisdiction="N/A (criminal jurisdiction)",
    geographic_jurisdiction="Designated courts in each district",
    composition="Child Justice Court magistrate with specialised training",
    presiding_officers=["Inquiry Magistrate (preliminary inquiry)", "Child Justice Court Presiding Officer"],
    appeal_route="High Court",
    key_procedures=[
        "Preliminary inquiry within 48 hours",
        "Assessment by probation officer",
        "Diversion as preferred outcome",
        "Restorative justice emphasis",
        "Minimum age of criminal capacity (12 years)",
        "In camera proceedings"
    ],
    common_matters=[
        "Theft and robbery by minors",
        "Assault by minors",
        "Drug-related offences by minors",
        "Sexual offences by minors",
        "Diversion programmes"
    ],
    prompt_considerations=[
        "Child's criminal capacity (age 12-14 rebuttable)",
        "Diversion preferred over prosecution",
        "Restorative justice principles",
        "Detention as last resort",
        "Probation officer assessment essential",
        "Reference Child Justice Act sentencing provisions"
    ],
    citation_format="S v [Child's initials] [Case number]"
)

# ═══════════════════════════════════════════════════════════════════════════════
# TRIBUNALS AND COMMISSIONS
# ═══════════════════════════════════════════════════════════════════════════════

CCMA = SpecialistCourt(
    name="Commission for Conciliation, Mediation and Arbitration",
    abbreviation="CCMA",
    saflii_code="ZACCMA",
    category=CourtCategory.TRIBUNALS,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="Labour Relations Act 66 of 1995, s112",
    subject_matter=[
        "Unfair dismissal disputes",
        "Unfair labour practice disputes",
        "Discrimination disputes (referred from SAHRC)",
        "Collective bargaining disputes",
        "Organisational rights disputes",
        "Severance pay disputes"
    ],
    monetary_jurisdiction="Compensation capped at 12/24 months' remuneration",
    geographic_jurisdiction="National (offices in all provinces)",
    composition="CCMA Commissioner (arbitrator/conciliator)",
    presiding_officers=["Part-time and full-time Commissioners"],
    appeal_route="Labour Court (review under s145, not appeal)",
    key_procedures=[
        "Referral within 30 days of dismissal",
        "Conciliation first (con-arb for misconduct/incapacity)",
        "Certificate of non-resolution",
        "Arbitration proceedings",
        "Limited legal representation (permission required)",
        "Award within 14 days"
    ],
    common_matters=[
        "Unfair dismissal (misconduct)",
        "Unfair dismissal (incapacity)",
        "Constructive dismissal",
        "Mutual interest disputes",
        "Organisational rights disputes"
    ],
    prompt_considerations=[
        "30-day referral period (condonation needed if late)",
        "Distinguish conciliation vs arbitration",
        "Apply Schedule 8 Code of Good Practice",
        "Consider CCMA Rules and Guidelines",
        "Sidumo standard applies on review"
    ],
    citation_format="[Party names] [Case number] - CCMA awards on SAFLII"
)

COMPETITION_TRIBUNAL = SpecialistCourt(
    name="Competition Tribunal",
    abbreviation="CT",
    saflii_code="ZACT",
    category=CourtCategory.TRIBUNALS,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="Competition Act 89 of 1998",
    subject_matter=[
        "Merger and acquisition approvals",
        "Prohibited practice referrals from Competition Commission",
        "Cartel prosecution",
        "Abuse of dominance complaints",
        "Exemption applications"
    ],
    monetary_jurisdiction="Can impose penalties up to 10% of annual turnover",
    geographic_jurisdiction="National",
    composition="Chairperson, Deputy Chairperson, and Tribunal members",
    presiding_officers=["Tribunal Chairperson", "Tribunal Members (legal and economic expertise)"],
    appeal_route="Competition Appeal Court",
    key_procedures=[
        "Referral from Competition Commission",
        "Pre-hearing conferences",
        "Discovery and pleadings",
        "Oral hearings",
        "Written reasons for decisions"
    ],
    common_matters=[
        "Large merger approvals",
        "Cartel prosecutions",
        "Abuse of dominance cases",
        "Conditional approvals with remedies"
    ],
    prompt_considerations=[
        "Market definition is crucial",
        "Apply economic analysis",
        "Consider public interest factors",
        "Reference Competition Commission investigation",
        "Consider settlement procedures"
    ],
    citation_format="[Party names] [Case number] [Year] ZACT [Number] ([Date])"
)

NATIONAL_CONSUMER_TRIBUNAL = SpecialistCourt(
    name="National Consumer Tribunal",
    abbreviation="NCT",
    saflii_code="ZANCT",
    category=CourtCategory.TRIBUNALS,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="National Credit Act 34 of 2005; Consumer Protection Act 68 of 2008",
    subject_matter=[
        "National Credit Act contraventions",
        "Consumer Protection Act referrals",
        "Debt counselling disputes",
        "Reckless credit complaints",
        "Credit provider deregistration"
    ],
    monetary_jurisdiction="Can impose administrative fines up to R1 million or 10% of turnover",
    geographic_jurisdiction="National",
    composition="Chairperson and Tribunal members",
    presiding_officers=["Tribunal Chairperson", "Tribunal Members"],
    appeal_route="High Court",
    key_procedures=[
        "Referral from NCC or NCR",
        "Written submissions",
        "Oral hearings",
        "Consent orders possible"
    ],
    common_matters=[
        "Reckless credit granting",
        "Unfair contract terms",
        "Debt collection practices",
        "Credit information disputes"
    ],
    prompt_considerations=[
        "Distinguish NCA from CPA matters",
        "Reference NCR or NCC investigation",
        "Consider consumer's vulnerability",
        "Apply in duplum rule and other protections"
    ],
    citation_format="[Party names] [Case number] [Year] ZANCT [Number] ([Date])"
)

# ═══════════════════════════════════════════════════════════════════════════════
# TRADITIONAL AND MILITARY COURTS
# ═══════════════════════════════════════════════════════════════════════════════

TRADITIONAL_COURT = SpecialistCourt(
    name="Traditional Courts",
    abbreviation="TC",
    saflii_code="N/A",
    category=CourtCategory.TRADITIONAL,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="Recognition of Traditional Communities Act; Various provincial legislation; Customary law",
    subject_matter=[
        "Customary law disputes",
        "Traditional marriage disputes",
        "Succession under customary law",
        "Land allocation in traditional areas",
        "Minor criminal matters (certain provinces)"
    ],
    monetary_jurisdiction="Limited civil matters up to R5,000 (varies by province)",
    geographic_jurisdiction="Traditional community areas",
    composition="Traditional leader with councillors/advisors",
    presiding_officers=["Inkosi/Chief/Traditional Leader", "Headman", "Traditional Council members"],
    appeal_route="Magistrates' Court (for formal review)",
    key_procedures=[
        "Inquisitorial procedure",
        "Community participation",
        "Oral tradition",
        "Restorative justice focus",
        "Ubuntu principles"
    ],
    common_matters=[
        "Lobola disputes",
        "Customary succession",
        "Land disputes in communal areas",
        "Community disciplinary matters"
    ],
    prompt_considerations=[
        "Apply living customary law (not codified)",
        "Consider Bhe v Magistrate Khayelitsha for customary succession",
        "Balance customary law with Bill of Rights",
        "Ubuntu and community values central",
        "Gender equality in modern application"
    ],
    citation_format="Generally unreported; appeals cited in Magistrates'/High Court"
)

MILITARY_COURT = SpecialistCourt(
    name="Military Courts",
    abbreviation="MilC",
    saflii_code="ZAMCT",
    category=CourtCategory.MILITARY,
    jurisdiction_type=JurisdictionType.EXCLUSIVE,
    establishing_legislation="Military Discipline Supplementary Measures Act 16 of 1999; Defence Act 42 of 2002",
    subject_matter=[
        "Military discipline offences",
        "Desertion and AWOL",
        "Military misconduct",
        "Certain civilian crimes by military personnel",
        "Court martial proceedings"
    ],
    monetary_jurisdiction="N/A (criminal jurisdiction)",
    geographic_jurisdiction="SANDF personnel and military establishments",
    composition="Military judge and court members",
    presiding_officers=[
        "Military Judge (Court Martial)",
        "Commanding Officer (summary trial)",
        "Court Martial Board"
    ],
    appeal_route="Court of Military Appeals (to SCA on legal questions)",
    key_procedures=[
        "Summary trial for minor offences",
        "Court martial for serious offences",
        "Different procedures from civilian courts",
        "Military counsel (prosecuting and defending)",
        "Board of inquiry precedes court martial"
    ],
    common_matters=[
        "Absence without leave (AWOL)",
        "Insubordination",
        "Negligent discharge of weapon",
        "Assault in military context",
        "Theft of military property"
    ],
    prompt_considerations=[
        "Distinct from civilian criminal procedure",
        "Military discipline codes apply",
        "Constitutional rights still apply (s35)",
        "Consider military-specific defences",
        "Different sentencing regime"
    ],
    citation_format="S v [Rank and Name] - Military Court judgments"
)

COURT_OF_MILITARY_APPEALS = SpecialistCourt(
    name="Court of Military Appeals",
    abbreviation="CMA",
    saflii_code="ZACMA",
    category=CourtCategory.MILITARY,
    jurisdiction_type=JurisdictionType.APPELLATE,
    establishing_legislation="Military Discipline Supplementary Measures Act 16 of 1999",
    subject_matter=[
        "Appeals from Court Martial",
        "Review of military court sentences",
        "Legal questions from military courts"
    ],
    monetary_jurisdiction="N/A",
    geographic_jurisdiction="National (SANDF)",
    composition="Judge of High Court as President, two military members",
    presiding_officers=["High Court Judge (as President)", "Two senior military officers"],
    appeal_route="Supreme Court of Appeal (on questions of law)",
    key_procedures=[
        "Petition for leave to appeal",
        "Review of court martial record",
        "Legal argument"
    ],
    common_matters=[
        "Court martial conviction appeals",
        "Sentence appeals",
        "Procedural irregularity claims"
    ],
    prompt_considerations=[
        "Apply military discipline legislation",
        "Consider unique military context",
        "Balance military necessity with rights"
    ],
    citation_format="[Party names] [Case number] [Year] ZACMA [Number] ([Date])"
)

# ═══════════════════════════════════════════════════════════════════════════════
# CIRCUIT COURTS
# ═══════════════════════════════════════════════════════════════════════════════

CIRCUIT_COURT = SpecialistCourt(
    name="Circuit Courts (High Court)",
    abbreviation="Circuit",
    saflii_code="Various (uses parent HC code)",
    category=CourtCategory.SUPERIOR,
    jurisdiction_type=JurisdictionType.ORIGINAL,
    establishing_legislation="Superior Courts Act 10 of 2013; Magistrates' Courts Act",
    subject_matter=[
        "Serious criminal matters in remote areas",
        "Civil matters requiring High Court jurisdiction in rural areas",
        "Divorce matters",
        "Appeals from Magistrates' Courts"
    ],
    monetary_jurisdiction="High Court jurisdiction",
    geographic_jurisdiction="Designated circuit areas (typically rural)",
    composition="High Court Judge sitting on circuit",
    presiding_officers=["High Court Judge on circuit"],
    appeal_route="Full Court of relevant High Court division",
    key_procedures=[
        "Same as High Court",
        "Scheduled sittings (not permanent)",
        "Local venue in circuit area"
    ],
    common_matters=[
        "Murder and serious assault",
        "Rape cases in rural areas",
        "Complex civil matters",
        "Divorce proceedings"
    ],
    prompt_considerations=[
        "Same procedures as High Court",
        "Consider logistics of circuit sittings",
        "Limited sitting dates - plan accordingly",
        "Use parent High Court division citation"
    ],
    citation_format="Uses relevant High Court division citation"
)

# ═══════════════════════════════════════════════════════════════════════════════
# COMPREHENSIVE COURTS COLLECTION
# ═══════════════════════════════════════════════════════════════════════════════

ALL_SPECIALIST_COURTS: Dict[str, SpecialistCourt] = {
    "LC": LABOUR_COURT,
    "LAC": LABOUR_APPEAL_COURT,
    "LCC": LAND_CLAIMS_COURT,
    "CAC": COMPETITION_APPEAL_COURT,
    "EC": ELECTORAL_COURT,
    "TC": TAX_COURT,
    "SCC": SMALL_CLAIMS_COURT,
    "EqC": EQUALITY_COURT,
    "MC": MAINTENANCE_COURT,
    "SOC": SEXUAL_OFFENCES_COURT,
    "CC": CHILDRENS_COURT,
    "CJC": CHILD_JUSTICE_COURT,
    "CCMA": CCMA,
    "CT": COMPETITION_TRIBUNAL,
    "NCT": NATIONAL_CONSUMER_TRIBUNAL,
    "TradC": TRADITIONAL_COURT,
    "MilC": MILITARY_COURT,
    "CMA": COURT_OF_MILITARY_APPEALS,
    "Circuit": CIRCUIT_COURT,
}

def get_courts_by_category(category: CourtCategory) -> List[SpecialistCourt]:
    """Get all courts in a specific category"""
    return [c for c in ALL_SPECIALIST_COURTS.values() if c.category == category]

def get_court_by_abbreviation(abbreviation: str) -> Optional[SpecialistCourt]:
    """Get a specific court by its abbreviation"""
    return ALL_SPECIALIST_COURTS.get(abbreviation)

def get_court_for_matter(matter_type: str) -> List[SpecialistCourt]:
    """Recommend courts based on matter type keywords"""
    matter_lower = matter_type.lower()
    recommendations = []
    
    for court in ALL_SPECIALIST_COURTS.values():
        for subject in court.subject_matter:
            if any(word in subject.lower() for word in matter_lower.split()):
                recommendations.append(court)
                break
    
    return recommendations

def generate_court_prompt_guidance(court: SpecialistCourt) -> str:
    """Generate prompt guidance for a specific court"""
    guidance = f"""
# {court.name} ({court.abbreviation}) - Prompt Guidance

## Jurisdiction
- **Type**: {court.jurisdiction_type.value}
- **Establishing Law**: {court.establishing_legislation}
- **Geographic Scope**: {court.geographic_jurisdiction}
{f"- **Monetary Limit**: {court.monetary_jurisdiction}" if court.monetary_jurisdiction else ""}

## Subject Matter Expertise
{chr(10).join(f"• {s}" for s in court.subject_matter)}

## Composition & Presiding Officers
- **Composition**: {court.composition}
- **Officers**: {', '.join(court.presiding_officers)}

## Key Procedures to Reference
{chr(10).join(f"• {p}" for p in court.key_procedures)}

## Common Matters
{chr(10).join(f"• {m}" for m in court.common_matters)}

## IMPORTANT: Prompt Considerations
{chr(10).join(f"⚠️ {c}" for c in court.prompt_considerations)}

## Appeal Route
➡️ {court.appeal_route}

## Citation Format
📝 {court.citation_format}
"""
    return guidance

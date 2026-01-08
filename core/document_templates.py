"""
🇿🇦 SA Legal Document Templates
AI-Assisted Document Drafting Templates for South African Legal Practice
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional

class DocumentCategory(Enum):
    """Categories of Legal Documents"""
    CORRESPONDENCE = "Legal Correspondence"
    PLEADINGS = "Court Pleadings"
    CONTRACTS = "Contracts & Agreements"
    OPINIONS = "Legal Opinions"
    NOTICES = "Statutory Notices"
    CORPORATE = "Corporate Documents"
    CONVEYANCING = "Conveyancing Documents"

class Court(Enum):
    """Courts for Pleading Templates"""
    CONSTITUTIONAL = "Constitutional Court"
    SCA = "Supreme Court of Appeal"
    HIGH_COURT = "High Court"
    REGIONAL_COURT = "Regional Court"
    MAGISTRATES_COURT = "Magistrates Court"
    LABOUR_COURT = "Labour Court"
    CCMA = "CCMA"

@dataclass
class DocumentSection:
    """Section of a Document Template"""
    name: str
    description: str
    required: bool
    content_guidance: str
    example: str

@dataclass
class DocumentTemplate:
    """Legal Document Template"""
    title: str
    category: DocumentCategory
    description: str
    use_cases: List[str]
    applicable_courts: Optional[List[Court]]
    structure: List[DocumentSection]
    drafting_tips: List[str]
    common_errors: List[str]
    prompt_template: str
    key_legislation: List[str]
    time_estimate: str

# ═══════════════════════════════════════════════════════════════════════════════
# LEGAL CORRESPONDENCE
# ═══════════════════════════════════════════════════════════════════════════════

LETTER_OF_DEMAND = DocumentTemplate(
    title="Letter of Demand",
    category=DocumentCategory.CORRESPONDENCE,
    description="Formal demand letter required before instituting civil proceedings for recovery of debt or damages.",
    use_cases=[
        "Debt recovery",
        "Breach of contract claims",
        "Delictual damages claims",
        "Matrimonial contribution claims"
    ],
    applicable_courts=[Court.HIGH_COURT, Court.MAGISTRATES_COURT],
    structure=[
        DocumentSection(
            name="Heading and Reference",
            description="Letterhead, date, reference number, delivery method notation",
            required=True,
            content_guidance="Include 'LETTER OF DEMAND' prominently. Note if sent by registered post/email.",
            example="LETTER OF DEMAND\nOUR REF: [Matter number]\nSent via Registered Post and Email"
        ),
        DocumentSection(
            name="Addressee Details",
            description="Full name and address of debtor/defendant",
            required=True,
            content_guidance="Use correct legal entity name. For companies, include registration number.",
            example="[Debtor Full Name/Company (Reg No)]\n[Physical Address]\n[Email if applicable]"
        ),
        DocumentSection(
            name="Introduction",
            description="Identification of client and matter",
            required=True,
            content_guidance="State who you act for and briefly identify the relationship/transaction.",
            example="We act for [Client], in connection with [brief description of relationship/transaction]."
        ),
        DocumentSection(
            name="Background Facts",
            description="Relevant factual background giving rise to the claim",
            required=True,
            content_guidance="State facts chronologically. Include dates, amounts, and key events.",
            example="On [date], you entered into an agreement with our client whereby... Despite due date of [date], you have failed to..."
        ),
        DocumentSection(
            name="Legal Basis",
            description="Briefly state the legal basis for the claim",
            required=True,
            content_guidance="Reference contract terms, statutory provisions, or delictual elements.",
            example="Your failure to pay constitutes breach of clause [X] of the agreement."
        ),
        DocumentSection(
            name="Quantum",
            description="Detailed breakdown of amount claimed",
            required=True,
            content_guidance="Itemise capital, interest (rate and calculation), and any additional amounts.",
            example="Capital: R[X]\nInterest at [X]% from [date]: R[X]\nTotal: R[X]"
        ),
        DocumentSection(
            name="Demand and Timeline",
            description="Clear demand with deadline for compliance",
            required=True,
            content_guidance="Demand must be clear. Give reasonable timeframe (typically 7-14 days).",
            example="We hereby demand payment of R[X] within 7 (seven) days of date hereof."
        ),
        DocumentSection(
            name="Consequence of Non-Compliance",
            description="State what will happen if demand not met",
            required=True,
            content_guidance="Warn of legal action, additional costs, and consequences.",
            example="Failing compliance, we have instructions to institute legal proceedings against you, without further notice, for payment together with interest and costs on the attorney and client scale."
        ),
        DocumentSection(
            name="Costs Reservation",
            description="Reserve right to claim costs",
            required=True,
            content_guidance="State costs will be claimed in any proceedings.",
            example="Our client's rights in respect of costs are reserved."
        ),
        DocumentSection(
            name="Signature",
            description="Firm signature block",
            required=True,
            content_guidance="Partner/director signature with contact details.",
            example="[Firm Name]\nPer: [Signatory]\nDirect: [Tel]\nEmail: [Email]"
        )
    ],
    drafting_tips=[
        "Be factually accurate - allegations must be provable",
        "Calculate interest correctly per agreement or Prescribed Rate of Interest Act",
        "Give reasonable time to comply (too short may be criticised by court)",
        "Avoid defamatory statements",
        "Keep copy of proof of delivery",
        "Consider in duplum rule for interest",
        "For consumers, ensure NCA and CPA compliance"
    ],
    common_errors=[
        "Interest incorrectly calculated",
        "Wrong legal entity sued",
        "Insufficient time allowed",
        "Threatening criminal proceedings for civil debt",
        "Not preserving proof of delivery",
        "Ignoring prescription periods"
    ],
    prompt_template="""
# Letter of Demand Drafting

## Role
You are an experienced litigation attorney drafting a formal Letter of Demand under South African law.

## Context
Client name: [ANONYMISED as "the Client"]
Debtor: [ANONYMISED as "the Debtor"]
Relationship/Transaction: [Describe]
Amount owed: [Specify]
Basis for claim: [Contract/Delict/Statute]
Interest: [Rate and from when]
Previous communication: [Any prior demands]

## Requirements
Draft a professional Letter of Demand that:
1. Clearly identifies the parties and relationship
2. States the factual background chronologically
3. Specifies the legal basis for the claim
4. Provides detailed quantum with interest calculation
5. Gives reasonable demand period (7-14 days)
6. Warns of legal consequences
7. Reserves costs

## Format
- Formal business letter format
- Professional but firm tone
- Clear and unambiguous demand
- Itemised amounts where applicable

## Legal Considerations
- Check prescription (3 years for debts generally)
- Consider in duplum rule
- If consumer credit: NCA s129 notice may be required instead
- Preserve evidence of delivery

## Output
Complete, ready-to-send Letter of Demand with all sections properly completed.
""",
    key_legislation=[
        "Prescribed Rate of Interest Act 55 of 1975",
        "National Credit Act 34 of 2005 (s129 for credit agreements)",
        "Consumer Protection Act 68 of 2008",
        "In duplum common law rule"
    ],
    time_estimate="30-60 minutes"
)

# ═══════════════════════════════════════════════════════════════════════════════
# COURT PLEADINGS
# ═══════════════════════════════════════════════════════════════════════════════

PARTICULARS_OF_CLAIM = DocumentTemplate(
    title="Particulars of Claim",
    category=DocumentCategory.PLEADINGS,
    description="The founding document in civil action stating plaintiff's cause of action.",
    use_cases=[
        "Contract claims",
        "Delictual claims",
        "Debt recovery actions",
        "Divorce actions"
    ],
    applicable_courts=[Court.HIGH_COURT, Court.MAGISTRATES_COURT],
    structure=[
        DocumentSection(
            name="Case Number and Heading",
            description="Court case number and party designations",
            required=True,
            content_guidance="Format per court rules. Include case number (or 'Case No: [to be allocated]').",
            example="IN THE HIGH COURT OF SOUTH AFRICA\n[DIVISION]\nCase No: [X]\nIn the matter between:\n[PLAINTIFF]    Plaintiff\nand\n[DEFENDANT]    Defendant"
        ),
        DocumentSection(
            name="Nature of Claim",
            description="Brief statement of nature and amount of claim",
            required=True,
            content_guidance="One sentence stating what is claimed (e.g., 'Claim for payment of R[X] being...').",
            example="NATURE OF CLAIM: Payment of R[X] being damages arising from breach of contract."
        ),
        DocumentSection(
            name="The Parties",
            description="Full details of plaintiff and defendant",
            required=True,
            content_guidance="Include full names, registration numbers (if company), addresses. State capacity if representative.",
            example="1. The Plaintiff is [FULL NAME/DETAILS], a [description], carrying on business at [address].\n2. The Defendant is [FULL NAME/DETAILS]..."
        ),
        DocumentSection(
            name="Jurisdiction",
            description="Basis for the court's jurisdiction",
            required=True,
            content_guidance="State why this court has jurisdiction (residence, cause of action arose, agreement).",
            example="3. This Honourable Court has jurisdiction by virtue of the Defendant residing within its area of jurisdiction."
        ),
        DocumentSection(
            name="The Agreement/Transaction",
            description="Full details of the contract or relationship",
            required=True,
            content_guidance="For contracts: parties, date, terms, annexures. For delict: relationship, duty of care.",
            example="4. On or about [date], at [place], the Plaintiff and Defendant entered into a written agreement in terms of which..."
        ),
        DocumentSection(
            name="The Breach/Wrongful Conduct",
            description="Detailed statement of breach or wrongful act",
            required=True,
            content_guidance="State each breach separately. Include dates and specifics. For delict: negligent/intentional act and causation.",
            example="5. The Defendant breached the agreement in that he/she/it:\n5.1 Failed to make payment of [amount] due on [date];\n5.2 [Further breaches]"
        ),
        DocumentSection(
            name="Damages/Claim Quantification",
            description="Itemised statement of damages or amounts claimed",
            required=True,
            content_guidance="Itemise all amounts. Show calculation of damages. Distinguish capital, interest, costs.",
            example="6. As a result of the breach, the Plaintiff suffered damages in the amount of R[X], calculated as follows:\n6.1 Capital amount: R[X]\n6.2 Interest at [X]% per annum from [date]: R[X]"
        ),
        DocumentSection(
            name="Prayer",
            description="Specific relief sought from the court",
            required=True,
            content_guidance="List each specific order sought. Include costs. Consider alternative relief.",
            example="WHEREFORE the Plaintiff claims:\n(a) Payment of R[X];\n(b) Interest on the aforesaid amount at [X]% per annum from [date] to date of payment;\n(c) Costs of suit;\n(d) Further and/or alternative relief."
        ),
        DocumentSection(
            name="Address for Service",
            description="Plaintiff's domicilium citandi et executandi",
            required=True,
            content_guidance="Physical address within court jurisdiction. Email if e-filing.",
            example="PLAINTIFF'S ADDRESS FOR SERVICE:\n[Address]\nTel: [X]\nEmail: [X]\nc/o [Local correspondent if applicable]"
        )
    ],
    drafting_tips=[
        "Every material fact must be pleaded - apply 'so what?' test",
        "Avoid evidence - plead facts, not how you'll prove them",
        "Each paragraph should contain one proposition",
        "Annex documents relied upon (but not correspondence)",
        "Plead legal conclusions (e.g., 'breached') after pleading facts supporting them",
        "Check monetary jurisdiction for correct court",
        "Include interest claim with rate and start date"
    ],
    common_errors=[
        "Pleading evidence instead of facts",
        "Failing to plead all elements of cause of action",
        "Incorrect calculation of interest",
        "Wrong court (jurisdiction issue)",
        "Vague or embarrassing pleadings",
        "Failing to annex written agreement",
        "Not stating basis for jurisdiction"
    ],
    prompt_template="""
# Particulars of Claim Drafting

## Role
You are a Senior Litigation Counsel drafting Particulars of Claim for filing in a South African court.

## Context
Court: [High Court [Division] / Magistrates Court [District]]
Plaintiff: [ANONYMISED as "the Plaintiff" - describe type of entity]
Defendant: [ANONYMISED as "the Defendant" - describe type of entity]
Cause of Action: [Contract / Delict / Statute]
Amount Claimed: [Specify]

## Facts
[Provide chronological statement of relevant facts]

## Cause of Action Details
**For Contract:**
- Date of agreement
- Material terms
- Written/oral
- Breach particulars

**For Delict:**
- Wrongful conduct
- Fault (intent/negligence)
- Causation
- Damages

## Requirements
Draft Particulars of Claim that:
1. Comply with Uniform Rules / Magistrates Court Rules
2. Plead all material facts (not evidence)
3. State each element of the cause of action
4. Include proper party descriptions
5. Assert jurisdiction
6. Provide itemised quantum
7. Include appropriate prayer

## Format
- Numbered paragraphs
- Formal legal language
- Logical flow from facts to legal conclusions
- Annexures marked "A", "B", etc.

## Important
- Every allegation must be provable
- Interest rate must be stated
- Costs on appropriate scale
- Address for service within jurisdiction

## Output
Complete Particulars of Claim ready for filing.
""",
    key_legislation=[
        "Uniform Rules of Court (High Court)",
        "Magistrates' Courts Rules (Magistrates Court)",
        "Prescription Act 68 of 1969",
        "Prescribed Rate of Interest Act 55 of 1975"
    ],
    time_estimate="1-3 hours depending on complexity"
)

HEADS_OF_ARGUMENT = DocumentTemplate(
    title="Heads of Argument",
    category=DocumentCategory.PLEADINGS,
    description="Written legal submissions summarising a party's case and legal arguments.",
    use_cases=[
        "High Court applications and trials",
        "Appeals",
        "Constitutional Court matters",
        "Complex motion proceedings"
    ],
    applicable_courts=[Court.CONSTITUTIONAL, Court.SCA, Court.HIGH_COURT],
    structure=[
        DocumentSection(
            name="Cover Page",
            description="Case details and party identification",
            required=True,
            content_guidance="Include court, case number, party designations, document title.",
            example="IN THE HIGH COURT OF SOUTH AFRICA\n[DIVISION]\nCase No: [X]\n\nIn the matter between:\n[APPLICANT]    Applicant\nand\n[RESPONDENT]    Respondent\n\nAPPLICANT'S HEADS OF ARGUMENT"
        ),
        DocumentSection(
            name="Table of Contents",
            description="Index of sections and page numbers",
            required=True,
            content_guidance="Include section headings with page references. Update before filing.",
            example="TABLE OF CONTENTS\nA. Introduction ............................... 1\nB. Factual Background ......................... 2\nC. Legal Framework ............................ 5\nD. Submissions ................................ 8\nE. Costs ..................................... 15\nF. Conclusion ................................ 16"
        ),
        DocumentSection(
            name="Introduction",
            description="Brief overview of matter and relief sought",
            required=True,
            content_guidance="One paragraph stating what case is about and what relief sought. State key issues.",
            example="1. This is an application for [relief]. The central question is whether [issue].\n2. The applicant contends that [summary of position].\n3. The following issues arise for determination: [list]"
        ),
        DocumentSection(
            name="Factual Background",
            description="Summary of relevant undisputed and disputed facts",
            required=True,
            content_guidance="Reference record/affidavits. Separate disputed from undisputed facts. Use neutral tone.",
            example="4. The undisputed facts are as follows:\n4.1 On [date], [fact - FA p[X] para [X]].\n5. The following facts are disputed:\n5.1 [Fact] - the applicant's version is [X] (FA p[X]), the respondent contends [Y] (AA p[X])."
        ),
        DocumentSection(
            name="Legal Framework",
            description="Statement of applicable legal principles",
            required=True,
            content_guidance="State legal principles with authorities. Start with legislation, then case law. Quote key provisions.",
            example="6. The applicable legal framework is as follows:\nStatutory provisions\n7. Section [X] of the [Act] provides: '[quote]'\nCase law\n8. In [Case citation], the [Court] held at para [X]: '[quote]'"
        ),
        DocumentSection(
            name="Submissions/Argument",
            description="Detailed legal argument applying law to facts",
            required=True,
            content_guidance="Logical progression. Address each issue. Apply legal principles to facts. Distinguish contrary authority.",
            example="FIRST ISSUE: [Statement of issue]\n10. It is submitted that [proposition].\n11. This is so because:\n11.1 [Reason with authority];\n11.2 [Reason with authority].\n12. The respondent's contrary argument is without merit because [reason]."
        ),
        DocumentSection(
            name="Costs",
            description="Submissions on costs",
            required=True,
            content_guidance="State why successful party should get costs. Address scale. Special costs orders if applicable.",
            example="15. It is submitted that costs should follow the result.\n16. The matter is of sufficient complexity to justify the employment of senior and junior counsel.\n17. Accordingly, it is submitted that costs on the scale as between attorney and client, including the costs of two counsel, would be appropriate."
        ),
        DocumentSection(
            name="Conclusion and Order Sought",
            description="Summary and precise order requested",
            required=True,
            content_guidance="One sentence summary. Then draft order in precise terms.",
            example="18. For the reasons set out above, it is submitted that the application should succeed with costs.\n19. The following order is sought:\n'1. [Order]\n2. [Order]\n3. The respondent is ordered to pay the applicant's costs, including the costs of two counsel.'"
        ),
        DocumentSection(
            name="List of Authorities",
            description="Bibliography of all cases and legislation cited",
            required=True,
            content_guidance="Alphabetical list of cases. Separate legislation. Include pinpoint references.",
            example="LIST OF AUTHORITIES\nCases\nMinister of Home Affairs v Fourie [2005] ZACC 19\nS v Makwanyane [1995] ZACC 3\nLegislation\nConstitution of the Republic of South Africa, 1996 - ss 9, 10, 36"
        )
    ],
    drafting_tips=[
        "Start with your strongest argument",
        "Every factual statement must reference the record",
        "Quote key passages from authorities - don't just cite",
        "Address the opposing party's strongest arguments",
        "Keep it concise - quality over quantity",
        "Use headings and subheadings for clarity",
        "Include a table of authorities",
        "Proofread citations carefully"
    ],
    common_errors=[
        "Factual statements without record references",
        "Citing cases without explaining their relevance",
        "Failing to address contrary authority",
        "Excessive length and repetition",
        "Incorrect citation format",
        "Not updating table of contents",
        "Emotional or argumentative tone"
    ],
    prompt_template="""
# Heads of Argument Drafting

## Role
You are Senior Counsel preparing Heads of Argument for filing in a South African court.

## Context
Court: [Specify - Constitutional Court / SCA / High Court [Division]]
Matter type: [Application / Appeal / Trial]
Party: [Applicant/Appellant or Respondent]
Issue(s): [Central legal question(s)]

## Case Summary
[Provide summary of:
- The relief sought
- Key facts (with record references)
- Main legal issues
- Your party's position
- Opposing party's position]

## Requirements
Draft Heads of Argument that:
1. Are structured logically with clear headings
2. Reference the record for all facts (FA/AA/RA page and paragraph)
3. State applicable legal principles with authority
4. Apply the law to the facts systematically
5. Address contrary arguments
6. Are persuasive but measured in tone
7. Include costs submissions
8. End with precise draft order

## Format
- Numbered paragraphs
- Clear section headings
- Block quotes for key authorities (indented)
- Footnotes for citations (or inline with pinpoints)
- Table of contents
- List of authorities

## Citation Format
Use SAFLII neutral citation format:
- [Case name] [Year] [Court abbrev] [Number]
- Quote at para [X]: "[quote]"

## Important
- Maximum [30] pages unless court allows more
- Focus on quality of argument, not volume
- Address strongest opposing arguments head-on
- Draft order must be precise and enforceable

## Output
Complete Heads of Argument ready for filing.
""",
    key_legislation=[
        "Uniform Rules of Court",
        "Constitutional Court Rules",
        "Supreme Court of Appeal Rules",
        "Practice Directives of specific court"
    ],
    time_estimate="4-12 hours depending on complexity"
)

# ═══════════════════════════════════════════════════════════════════════════════
# CONTRACTS & AGREEMENTS
# ═══════════════════════════════════════════════════════════════════════════════

NDA_AGREEMENT = DocumentTemplate(
    title="Non-Disclosure Agreement (Confidentiality Agreement)",
    category=DocumentCategory.CONTRACTS,
    description="Agreement protecting confidential information shared between parties.",
    use_cases=[
        "Pre-transaction due diligence",
        "Employment relationships",
        "Joint ventures and partnerships",
        "Tender/RFP processes",
        "Technology licensing discussions"
    ],
    applicable_courts=None,
    structure=[
        DocumentSection(
            name="Heading and Parties",
            description="Agreement title and party definitions",
            required=True,
            content_guidance="Clear title. Define parties with full legal names and registration numbers.",
            example="CONFIDENTIALITY AND NON-DISCLOSURE AGREEMENT\n\nentered into between\n\n[PARTY A (Pty) Ltd] (Registration No: [X])\n(\"the Discloser\")\n\nand\n\n[PARTY B (Pty) Ltd] (Registration No: [X])\n(\"the Recipient\")"
        ),
        DocumentSection(
            name="Recitals/Background",
            description="Context for the agreement",
            required=True,
            content_guidance="Explain why parties are entering agreement. Describe the Purpose.",
            example="WHEREAS:\nA. The Discloser is engaged in [business].\nB. The Recipient wishes to evaluate [purpose].\nC. The Discloser is willing to disclose certain confidential information subject to the terms hereof."
        ),
        DocumentSection(
            name="Definitions",
            description="Key term definitions",
            required=True,
            content_guidance="Define 'Confidential Information', 'Purpose', 'Representatives', 'Permitted Use'.",
            example="1. DEFINITIONS\n1.1 \"Confidential Information\" means all information disclosed by the Discloser to the Recipient, whether orally, in writing, or in any other form, including but not limited to: [list categories]\n1.2 \"Purpose\" means [define]"
        ),
        DocumentSection(
            name="Confidentiality Obligations",
            description="Core obligations of recipient",
            required=True,
            content_guidance="Keep confidential, use only for Purpose, protect with same care as own information.",
            example="2. CONFIDENTIALITY OBLIGATIONS\n2.1 The Recipient shall:\n(a) keep all Confidential Information strictly confidential;\n(b) use the Confidential Information solely for the Purpose;\n(c) not disclose the Confidential Information to any third party without prior written consent..."
        ),
        DocumentSection(
            name="Exclusions",
            description="What is not considered Confidential Information",
            required=True,
            content_guidance="Standard exclusions: public knowledge, prior possession, independent development, compelled disclosure.",
            example="3. EXCLUSIONS\nThe obligations in clause 2 shall not apply to information which:\n(a) is or becomes publicly available through no fault of the Recipient;\n(b) was lawfully in the Recipient's possession before disclosure;\n(c) is independently developed by the Recipient..."
        ),
        DocumentSection(
            name="Compelled Disclosure",
            description="Handling legally required disclosure",
            required=True,
            content_guidance="Notify Discloser, cooperate to limit disclosure, seek protective order.",
            example="4. COMPELLED DISCLOSURE\nIf the Recipient is legally compelled to disclose Confidential Information, the Recipient shall:\n(a) promptly notify the Discloser in writing;\n(b) cooperate with the Discloser to obtain a protective order..."
        ),
        DocumentSection(
            name="Term and Termination",
            description="Duration and survival of obligations",
            required=True,
            content_guidance="State term of agreement and how long confidentiality survives (typically 2-5 years).",
            example="5. TERM\n5.1 This Agreement shall commence on signature and continue for [X] years.\n5.2 The confidentiality obligations shall survive termination for a period of [X] years."
        ),
        DocumentSection(
            name="Return of Information",
            description="What happens to information on termination",
            required=True,
            content_guidance="Return or destroy, certification of destruction.",
            example="6. RETURN OF INFORMATION\nUpon request or termination, the Recipient shall promptly return or destroy all Confidential Information and provide written certification of destruction."
        ),
        DocumentSection(
            name="Remedies",
            description="Remedies for breach",
            required=True,
            content_guidance="Acknowledge irreparable harm, entitlement to injunctive relief without proving damages.",
            example="7. REMEDIES\nThe Recipient acknowledges that breach may cause irreparable harm for which damages would be inadequate, and accordingly the Discloser shall be entitled to seek injunctive relief without proof of actual damages."
        ),
        DocumentSection(
            name="General Provisions (Boilerplate)",
            description="Standard boilerplate clauses",
            required=True,
            content_guidance="Governing law, jurisdiction, entire agreement, no waiver, severability, counterparts.",
            example="8. GENERAL\n8.1 This Agreement shall be governed by the laws of South Africa.\n8.2 The parties submit to the exclusive jurisdiction of the High Court of South Africa.\n8.3 This Agreement constitutes the entire agreement..."
        ),
        DocumentSection(
            name="Signature Block",
            description="Execution provisions",
            required=True,
            content_guidance="Signature lines, witness if required, date.",
            example="SIGNED at [place] on this [day] of [month] [year]\n\nFor and on behalf of [PARTY A]:\n_____________________\nName:\nCapacity:\n\nAs witness:\n1. _____________________\n2. _____________________"
        )
    ],
    drafting_tips=[
        "Define 'Confidential Information' carefully - not too broad or narrow",
        "Consider mutual vs one-way NDA based on circumstances",
        "Include practical carve-outs for Representatives",
        "Duration should match sensitivity of information",
        "Consider POPIA implications for personal information",
        "Include clear return/destruction provisions",
        "Specify governing law and jurisdiction"
    ],
    common_errors=[
        "Overly broad definition of Confidential Information",
        "No exclusions for public/prior knowledge",
        "Unreasonable duration",
        "No provision for legally compelled disclosure",
        "Missing signature requirements for company",
        "No survival clause after termination"
    ],
    prompt_template="""
# NDA Drafting

## Role
You are a Commercial Attorney drafting a Non-Disclosure Agreement under South African law.

## Context
Type: [Mutual / One-way]
Discloser: [ANONYMISED - describe type of entity]
Recipient: [ANONYMISED - describe type of entity]
Purpose: [What transaction/relationship]
Duration: [Suggested term]
Information type: [General categories to protect]

## Requirements
Draft an NDA that:
1. Clearly defines Confidential Information
2. Sets out core confidentiality obligations
3. Includes standard exclusions
4. Addresses compelled disclosure
5. Specifies term and survival period
6. Includes return/destruction provisions
7. Contains appropriate remedies clause
8. Includes SA law boilerplate

## Special Considerations
- POPIA compliance if personal information involved
- ECTA for electronic signature validity
- Consider competition law if competitors

## Format
- Formal contract style
- Numbered clauses with sub-clauses
- Definitions section
- Signature blocks with witness lines

## Output
Complete NDA ready for review and execution.
""",
    key_legislation=[
        "Common law of contract",
        "Protection of Personal Information Act 4 of 2013 (POPIA)",
        "Electronic Communications and Transactions Act 25 of 2002",
        "Companies Act 71 of 2008 (signing requirements)"
    ],
    time_estimate="1-2 hours"
)

# ═══════════════════════════════════════════════════════════════════════════════
# LEGAL OPINIONS
# ═══════════════════════════════════════════════════════════════════════════════

LEGAL_OPINION = DocumentTemplate(
    title="Legal Opinion/Advice",
    category=DocumentCategory.OPINIONS,
    description="Formal written legal advice on a specific legal question or matter.",
    use_cases=[
        "Transaction opinions",
        "Regulatory compliance",
        "Risk assessment",
        "Pre-litigation advice",
        "Board advice"
    ],
    applicable_courts=None,
    structure=[
        DocumentSection(
            name="Header",
            description="Title and confidentiality notice",
            required=True,
            content_guidance="Mark as 'PRIVILEGED AND CONFIDENTIAL'. Include date and reference.",
            example="PRIVILEGED AND CONFIDENTIAL\nLEGAL OPINION\nDate: [X]\nOur Ref: [X]\nTo: [Client]"
        ),
        DocumentSection(
            name="Introduction",
            description="Purpose and scope of opinion",
            required=True,
            content_guidance="State what opinion addresses, who requested it, and any limitations on scope.",
            example="1. INTRODUCTION\n1.1 We have been asked to advise on [subject].\n1.2 This opinion is provided for the benefit of [client] only and may not be relied upon by any third party without our written consent."
        ),
        DocumentSection(
            name="Documents Reviewed",
            description="List of documents and information considered",
            required=True,
            content_guidance="List all documents, information sources, and assumptions made.",
            example="2. DOCUMENTS REVIEWED\n2.1 In preparing this opinion, we have reviewed the following:\n(a) [Document 1];\n(b) [Document 2];\n2.2 We have assumed that..."
        ),
        DocumentSection(
            name="Factual Background",
            description="Summary of relevant facts as provided",
            required=True,
            content_guidance="State facts based on instructions. Note that opinion is based on these facts.",
            example="3. FACTUAL BACKGROUND\n3.1 We are instructed that:\n(a) [Fact 1];\n(b) [Fact 2];\n3.2 This opinion is based on the facts as set out above. If any material facts differ, our opinion may change."
        ),
        DocumentSection(
            name="Questions for Opinion",
            description="The specific legal questions to be answered",
            required=True,
            content_guidance="Clearly state each question to be addressed.",
            example="4. QUESTIONS\n4.1 We have been asked to advise on the following questions:\n(a) Whether [Question 1]?\n(b) Whether [Question 2]?"
        ),
        DocumentSection(
            name="Applicable Law",
            description="Statement of relevant legal principles",
            required=True,
            content_guidance="Set out legislation and case law applicable to the questions.",
            example="5. APPLICABLE LAW\nStatutory framework\n5.1 Section [X] of the [Act] provides that...\nCase law\n5.2 In [Case], the court held that..."
        ),
        DocumentSection(
            name="Analysis/Discussion",
            description="Application of law to facts",
            required=True,
            content_guidance="Work through each question. Apply law to facts. Consider counter-arguments.",
            example="6. ANALYSIS\nFirst question\n6.1 Applying the principles set out above to the facts:\n(a) [Analysis point 1];\n(b) [Analysis point 2];\n6.2 Accordingly, in our view..."
        ),
        DocumentSection(
            name="Opinion/Conclusion",
            description="Clear statement of legal opinion on each question",
            required=True,
            content_guidance="Answer each question clearly. Use qualifiers appropriately ('in our view', 'we consider that').",
            example="7. OPINION\n7.1 Based on the foregoing analysis, our opinion is as follows:\n(a) In response to Question 1: [Answer];\n(b) In response to Question 2: [Answer]."
        ),
        DocumentSection(
            name="Recommendations",
            description="Practical recommendations based on opinion",
            required=False,
            content_guidance="If appropriate, provide practical recommendations for action.",
            example="8. RECOMMENDATIONS\n8.1 In light of the above, we recommend that:\n(a) [Recommendation 1];\n(b) [Recommendation 2]."
        ),
        DocumentSection(
            name="Qualifications and Limitations",
            description="Standard qualifications to opinion",
            required=True,
            content_guidance="State that opinion is based on SA law only, facts as stated, and is not guarantee.",
            example="9. QUALIFICATIONS\n9.1 This opinion is based on the laws of South Africa as at the date hereof.\n9.2 We express no opinion on the laws of any other jurisdiction.\n9.3 This opinion is based on the facts as set out above..."
        )
    ],
    drafting_tips=[
        "Be clear on what you are opining on - and what you are not",
        "State all assumptions and qualifications upfront",
        "Distinguish between 'facts' (as provided) and your analysis",
        "Give clear answers - avoid unnecessary hedging",
        "Consider the reader - adjust technical detail accordingly",
        "If uncertain, say so - and explain why",
        "Check privilege and confidentiality claims"
    ],
    common_errors=[
        "Scope creep - opining beyond instructions",
        "Unclear conclusions",
        "Not stating assumptions",
        "Failure to consider contrary arguments",
        "Not addressing all questions posed",
        "Outdated law",
        "Not limiting to SA law"
    ],
    prompt_template="""
# Legal Opinion Drafting

## Role
You are a Senior Associate/Partner providing formal written legal advice under South African law.

## Context
Client: [ANONYMISED - describe type]
Matter: [Describe]
Questions: [List specific legal questions]

## Instructions
[Summarise instructions received]

## Documents Reviewed
[List documents provided]

## Requirements
Draft a Legal Opinion that:
1. Clearly states scope and limitations
2. Lists documents reviewed and assumptions made
3. Sets out factual background as provided
4. States specific questions to be answered
5. Analyses applicable legislation and case law
6. Applies law to facts systematically
7. Provides clear conclusions on each question
8. Includes appropriate qualifications

## Format
- Formal opinion structure
- Numbered paragraphs
- Clear headings
- Conclusion section with answers to each question

## Important
- Mark as 'PRIVILEGED AND CONFIDENTIAL'
- State that opinion is based on SA law only
- Qualify any areas of uncertainty
- Do not guarantee outcomes

## Output
Complete Legal Opinion ready for partner review.
""",
    key_legislation=[
        "Depends on subject matter",
        "Note: Identify and reference all applicable statutes"
    ],
    time_estimate="2-8 hours depending on complexity"
)

# ═══════════════════════════════════════════════════════════════════════════════
# ALL DOCUMENT TEMPLATES
# ═══════════════════════════════════════════════════════════════════════════════

ALL_DOCUMENT_TEMPLATES: Dict[str, DocumentTemplate] = {
    "letter_of_demand": LETTER_OF_DEMAND,
    "particulars_of_claim": PARTICULARS_OF_CLAIM,
    "heads_of_argument": HEADS_OF_ARGUMENT,
    "nda_agreement": NDA_AGREEMENT,
    "legal_opinion": LEGAL_OPINION,
}

def get_templates_by_category(category: DocumentCategory) -> List[DocumentTemplate]:
    """Get all templates for a specific category"""
    return [t for t in ALL_DOCUMENT_TEMPLATES.values() if t.category == category]

def get_template_structure(template: DocumentTemplate) -> str:
    """Get formatted structure guide for a template"""
    structure_text = f"# {template.title} Structure\n\n"
    for i, section in enumerate(template.structure, 1):
        req_marker = "✓ REQUIRED" if section.required else "○ Optional"
        structure_text += f"## {i}. {section.name} [{req_marker}]\n"
        structure_text += f"**Description:** {section.description}\n"
        structure_text += f"**Guidance:** {section.content_guidance}\n"
        structure_text += f"**Example:**\n```\n{section.example}\n```\n\n"
    return structure_text

def generate_document_prompt(template: DocumentTemplate, context: str) -> str:
    """Generate a complete prompt for document drafting"""
    return f"""
{template.prompt_template}

## Your Specific Context
{context}

## Document Structure Required
{get_template_structure(template)}

## Key Legislation
{chr(10).join(f"• {leg}" for leg in template.key_legislation)}

## Drafting Tips
{chr(10).join(f"💡 {tip}" for tip in template.drafting_tips)}

## Common Errors to Avoid
{chr(10).join(f"⚠️ {error}" for error in template.common_errors)}

---
Estimated drafting time: {template.time_estimate}
IMPORTANT: This is a template for guidance. All documents must be reviewed by a qualified attorney before use.
"""

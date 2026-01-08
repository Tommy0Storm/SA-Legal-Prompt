"""
🇿🇦 SA Legal Workflow Pipelines
Multi-Step Legal Workflows with AI-Assisted Prompting for South African Practice
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional

class WorkflowCategory(Enum):
    """Categories of Legal Workflows"""
    LITIGATION = "Litigation Support"
    TRANSACTIONAL = "Transactional/Commercial"
    REGULATORY = "Regulatory & Compliance"
    CORPORATE = "Corporate Advisory"
    DISPUTE_RESOLUTION = "Dispute Resolution"

class StepType(Enum):
    """Types of Workflow Steps"""
    RESEARCH = "Research & Analysis"
    DRAFTING = "Document Drafting"
    REVIEW = "Review & Verification"
    STRATEGY = "Strategic Planning"
    COMMUNICATION = "Client Communication"
    PROCEDURAL = "Procedural Action"

class RiskLevel(Enum):
    """Risk Level for AI Assistance"""
    LOW = "Low Risk - AI can lead"
    MEDIUM = "Medium Risk - AI assists, human reviews"
    HIGH = "High Risk - Human leads, AI supports"
    CRITICAL = "Critical - Human only, AI verification"

@dataclass
class WorkflowStep:
    """Single Step in a Legal Workflow"""
    step_number: int
    title: str
    step_type: StepType
    description: str
    ai_prompt: str
    human_actions: List[str]
    verification_required: List[str]
    risk_level: RiskLevel
    outputs: List[str]
    estimated_time: str
    dependencies: List[int]  # Step numbers this depends on

@dataclass
class LegalWorkflow:
    """Complete Legal Workflow Pipeline"""
    title: str
    category: WorkflowCategory
    description: str
    use_cases: List[str]
    steps: List[WorkflowStep]
    key_legislation: List[str]
    ethical_considerations: List[str]
    quality_checkpoints: List[str]
    total_estimated_time: str
    complexity: str

# ═══════════════════════════════════════════════════════════════════════════════
# CONTRACT REVIEW WORKFLOW
# ═══════════════════════════════════════════════════════════════════════════════

CONTRACT_REVIEW_WORKFLOW = LegalWorkflow(
    title="Commercial Contract Review Pipeline",
    category=WorkflowCategory.TRANSACTIONAL,
    description="Comprehensive multi-step workflow for reviewing and advising on commercial contracts under SA law.",
    use_cases=[
        "Service agreements",
        "Supply contracts",
        "Distribution agreements",
        "Lease agreements",
        "Joint venture agreements"
    ],
    steps=[
        WorkflowStep(
            step_number=1,
            title="Initial Contract Assessment",
            step_type=StepType.REVIEW,
            description="First-pass review to identify contract type, parties, key terms, and red flags.",
            ai_prompt="""
# Initial Contract Assessment

## Role
You are a Commercial Attorney conducting initial assessment of a contract.

## Task
Review the contract and provide:

### 1. Contract Overview
- Type of contract
- Parties identified
- Execution date and term
- Governing law

### 2. Key Commercial Terms
- Subject matter/scope
- Pricing and payment terms
- Deliverables and timelines
- Performance standards

### 3. Risk Identification (Flag System)
🔴 **Red Flags** (Immediate attention required)
🟡 **Amber Flags** (Needs review)
🟢 **Green Flags** (Standard/acceptable)

### 4. Initial Questions for Client
- [List clarifying questions]

### 5. Priority Issues
- [Ranked list of issues to address in detailed review]

## Format
Use the flag system above. Be specific about clause numbers.
""",
            human_actions=[
                "Upload contract document",
                "Confirm client's role (buyer/seller/service provider)",
                "Note any specific concerns raised by client"
            ],
            verification_required=[
                "Confirm all parties correctly identified",
                "Verify contract is complete (no missing schedules)"
            ],
            risk_level=RiskLevel.LOW,
            outputs=["Initial assessment memo", "Red flags list", "Client questions"],
            estimated_time="30-60 minutes",
            dependencies=[]
        ),
        WorkflowStep(
            step_number=2,
            title="Detailed Clause-by-Clause Analysis",
            step_type=StepType.RESEARCH,
            description="Deep analysis of each clause against market standards and SA law.",
            ai_prompt="""
# Detailed Clause Analysis

## Role
You are a Senior Commercial Attorney conducting detailed contract review.

## Context
Building on initial assessment. Now analyse each clause in detail.

## Analysis Framework

For EACH material clause, provide:

### Clause [Number]: [Title]
**Summary:** [What it says in plain language]
**Risk to Client:** [Low/Medium/High]
**Market Standard:** [Better than/At/Worse than market]
**SA Law Issues:** [Any legal concerns under SA law]
**Recommended Changes:** [Specific proposed amendments]
**Negotiation Priority:** [Must have / Nice to have / Accept]

### Key Clauses to Analyse
1. Scope and deliverables
2. Price and payment
3. Term and termination
4. Warranties and representations
5. Liability and indemnity
6. Limitation of liability
7. Insurance requirements
8. Intellectual property
9. Confidentiality
10. Force majeure
11. Dispute resolution
12. Boilerplate (assignment, entire agreement, amendments)

### Special SA Law Considerations
- Consumer Protection Act application
- POPIA compliance
- BBBEE provisions
- Competition law clearance
- Exchange control (if cross-border)

## Output
Clause-by-clause analysis with recommendations.
""",
            human_actions=[
                "Review AI analysis for accuracy",
                "Identify any missed clauses",
                "Add context from similar deals"
            ],
            verification_required=[
                "Check that CPA analysis is correct",
                "Verify liability analysis against current case law",
                "Confirm POPIA requirements if personal information involved"
            ],
            risk_level=RiskLevel.MEDIUM,
            outputs=["Clause analysis matrix", "Risk assessment", "Amendment recommendations"],
            estimated_time="2-4 hours",
            dependencies=[1]
        ),
        WorkflowStep(
            step_number=3,
            title="Comparative Research",
            step_type=StepType.RESEARCH,
            description="Research case law and precedent on any unusual or high-risk provisions.",
            ai_prompt="""
# Legal Research on Contract Issues

## Role
You are a Legal Researcher investigating specific contract provisions.

## Task
For each flagged high-risk or unusual provision, research:

### 1. SA Case Law
- How have SA courts interpreted similar clauses?
- Any relevant SCA or High Court decisions?
- SAFLII search: [specific search terms]

### 2. Enforceability Analysis
- Is the clause enforceable under SA law?
- Any statutory limitations (CPA, NCA, etc.)?
- Public policy concerns?

### 3. Limitation Clauses Specifically
- Consider Afrox Healthcare v Strydom principles
- CPA s51 unfair contract terms
- ECTA s44 for electronic agreements

### 4. Penalty Clauses
- Conventional Penalties Act 15 of 1962
- Is the clause penal in nature?
- Risk of judicial reduction?

### 5. Restraint of Trade (if applicable)
- Magna Alloys / Basson principles
- Reasonableness assessment

## Output
Research memo with case citations and enforceability opinions.

## Important
All case citations must use SAFLII neutral citation format.
""",
            human_actions=[
                "Verify case citations on SAFLII",
                "Check for recent developments not in AI knowledge",
                "Cross-reference with firm precedent database"
            ],
            verification_required=[
                "All case citations verified on SAFLII",
                "Check if cases have been overruled",
                "Confirm current statutory position"
            ],
            risk_level=RiskLevel.HIGH,
            outputs=["Research memo", "Case law summaries", "Enforceability opinion"],
            estimated_time="1-3 hours",
            dependencies=[2]
        ),
        WorkflowStep(
            step_number=4,
            title="Draft Amendments Schedule",
            step_type=StepType.DRAFTING,
            description="Prepare proposed amendments to the contract in markup or schedule format.",
            ai_prompt="""
# Draft Contract Amendments

## Role
You are a Commercial Attorney drafting amendments to a contract.

## Context
Based on clause analysis and research, draft proposed amendments.

## Format Options
Choose based on negotiation stage:

### Option A: Tracked Changes Markup
[Original text with strikethrough] → [New proposed text]

### Option B: Amendments Schedule
| Clause | Current Wording | Proposed Amendment | Rationale |
|--------|-----------------|-------------------|-----------|
| [X.X]  | "[current]"     | "[proposed]"      | [reason]  |

## Drafting Principles
1. Maintain contract style and terminology
2. Ensure internal consistency
3. Cross-reference affected clauses
4. Consider SA law requirements

## Priority Categories
**P1: Essential** - Must be amended for deal to proceed
**P2: Important** - Strongly preferred amendments
**P3: Desirable** - If counterparty agrees

## For Each Amendment
- Clause reference
- Current wording
- Proposed new wording
- Brief rationale
- Priority level
- Fallback position (if any)

## Output
Complete amendments schedule ready for client review.
""",
            human_actions=[
                "Review amendments for accuracy",
                "Confirm alignment with client's commercial objectives",
                "Prioritise amendments for negotiation"
            ],
            verification_required=[
                "Check that amendments are legally correct",
                "Ensure amendments work together (no conflicts)",
                "Confirm practical/commercial workability"
            ],
            risk_level=RiskLevel.MEDIUM,
            outputs=["Amendments schedule", "Negotiation brief", "Fallback positions"],
            estimated_time="1-2 hours",
            dependencies=[2, 3]
        ),
        WorkflowStep(
            step_number=5,
            title="Client Advice Memo",
            step_type=StepType.COMMUNICATION,
            description="Prepare client-facing summary of review with recommendations.",
            ai_prompt="""
# Client Advice Memo

## Role
You are a Partner preparing advice for a client on a contract.

## Task
Prepare a client-facing memo summarising:

### 1. Executive Summary
[2-3 paragraph overview for busy executives]

### 2. Key Findings
**Favourable Terms:**
- [List terms favourable to client]

**Areas of Concern:**
- [List concerns with risk rating]

**Unusual Provisions:**
- [Anything non-standard that client should know]

### 3. Recommended Amendments
[Summary of proposed changes - prioritised]

### 4. Risk Assessment
**Overall Risk Rating:** [Low/Medium/High]
**Key Risks:**
- [Risk 1 and mitigation]
- [Risk 2 and mitigation]

### 5. Commercial Considerations
[Any non-legal commercial points the client should consider]

### 6. Recommended Next Steps
1. [Step]
2. [Step]
3. [Step]

### 7. Questions for Client
[Any information needed from client to finalise advice]

## Tone
- Clear, commercial, accessible
- Avoid unnecessary legal jargon
- Focus on business impact
- Action-oriented recommendations

## Output
Client-ready memo (2-4 pages).
""",
            human_actions=[
                "Review for client appropriateness",
                "Add relationship context",
                "Schedule client call/meeting"
            ],
            verification_required=[
                "Confirm accuracy of legal advice",
                "Check privilege and confidentiality markings",
                "Ensure advice is complete and balanced"
            ],
            risk_level=RiskLevel.HIGH,
            outputs=["Client memo", "Meeting agenda", "Next steps list"],
            estimated_time="1-2 hours",
            dependencies=[2, 3, 4]
        ),
        WorkflowStep(
            step_number=6,
            title="Final Review and Sign-off",
            step_type=StepType.REVIEW,
            description="Partner review and quality assurance before sending to client.",
            ai_prompt="""
# Quality Assurance Checklist

## Task
Review all outputs from this workflow for:

### Legal Accuracy
☐ All legal statements are correct
☐ Case citations verified
☐ Statutory references checked
☐ No outdated law

### Completeness
☐ All material clauses addressed
☐ All client questions answered
☐ Risks properly identified
☐ Amendments comprehensive

### Quality
☐ Clear and professional language
☐ Internally consistent
☐ Free of typos and errors
☐ Proper formatting

### Client Appropriateness
☐ Appropriate for audience
☐ Commercial focus maintained
☐ Actionable recommendations
☐ Privilege markings in place

### Compliance
☐ Firm precedents considered
☐ Conflicts checked
☐ Fee estimate provided
☐ File documented

## Output
Sign-off memo or list of corrections required.
""",
            human_actions=[
                "Partner reviews all materials",
                "Approves or requests revisions",
                "Signs off for client delivery"
            ],
            verification_required=[
                "Partner sign-off obtained",
                "All corrections implemented",
                "Client delivery method confirmed"
            ],
            risk_level=RiskLevel.CRITICAL,
            outputs=["Signed-off deliverables", "File note", "Invoice/fee estimate"],
            estimated_time="30-60 minutes",
            dependencies=[1, 2, 3, 4, 5]
        )
    ],
    key_legislation=[
        "Consumer Protection Act 68 of 2008 (if consumer contract)",
        "Conventional Penalties Act 15 of 1962",
        "POPIA Act 4 of 2013",
        "ECTA 25 of 2002",
        "Common law of contract"
    ],
    ethical_considerations=[
        "Maintain client confidentiality throughout",
        "Do not share contract with AI unless authorised",
        "Verify all AI outputs before client delivery",
        "Disclose AI use to client if firm policy requires",
        "Ensure proper supervision of AI-assisted work"
    ],
    quality_checkpoints=[
        "Initial assessment reviewed before detailed analysis",
        "All case citations verified on SAFLII",
        "Amendments reviewed for legal accuracy",
        "Client memo reviewed by supervisor/partner"
    ],
    total_estimated_time="6-12 hours",
    complexity="Medium-High"
)

# ═══════════════════════════════════════════════════════════════════════════════
# LITIGATION SUPPORT WORKFLOW
# ═══════════════════════════════════════════════════════════════════════════════

LITIGATION_SUPPORT_WORKFLOW = LegalWorkflow(
    title="Civil Litigation Support Pipeline",
    category=WorkflowCategory.LITIGATION,
    description="End-to-end workflow for civil litigation matter management under SA procedure.",
    use_cases=[
        "Contract disputes",
        "Delictual claims",
        "Debt recovery",
        "Property disputes",
        "Commercial litigation"
    ],
    steps=[
        WorkflowStep(
            step_number=1,
            title="Case Intake and Assessment",
            step_type=StepType.STRATEGY,
            description="Initial case evaluation, merit assessment, and strategy development.",
            ai_prompt="""
# Case Intake Assessment

## Role
You are a Litigation Partner evaluating a new potential case.

## Task
Assess the matter and provide:

### 1. Case Overview
- Parties and their roles
- Nature of dispute
- Amount/relief sought
- Jurisdiction and venue

### 2. Cause of Action Analysis
**For Contract Claims:**
- Agreement (date, parties, key terms)
- Breach (nature, date, particulars)
- Damages/relief available

**For Delict Claims:**
- Wrongful conduct
- Fault (intent/negligence)
- Causation
- Damages

### 3. Preliminary Merit Assessment
**Strengths:**
- [List with evidence references]

**Weaknesses:**
- [List with concerns]

**Overall Merit:** [Strong / Reasonable / Weak / Hopeless]

### 4. Limitation Periods
- When did cause of action arise?
- Applicable prescription period?
- Any risk of prescription?

### 5. Evidence Inventory
- Available evidence
- Evidence still needed
- Witness availability

### 6. Strategy Recommendations
- Recommended approach
- ADR prospects
- Litigation timeline estimate
- Preliminary cost estimate

## Output
Case intake memorandum with recommendations.
""",
            human_actions=[
                "Conduct client intake meeting",
                "Gather and review documents",
                "Conflict check",
                "Assess fee arrangements"
            ],
            verification_required=[
                "Prescription calculation verified",
                "Conflict check completed",
                "Client identification done (FICA)"
            ],
            risk_level=RiskLevel.MEDIUM,
            outputs=["Case assessment memo", "Conflict clearance", "Fee estimate"],
            estimated_time="2-4 hours",
            dependencies=[]
        ),
        WorkflowStep(
            step_number=2,
            title="Pre-Action Correspondence",
            step_type=StepType.DRAFTING,
            description="Draft and send letter of demand or other pre-action correspondence.",
            ai_prompt="""
# Letter of Demand Drafting

## Role
You are a Litigation Attorney drafting pre-action correspondence.

## Task
Draft a Letter of Demand that:

### Structure
1. **Heading** - "LETTER OF DEMAND" prominently displayed
2. **Client identification** - Who we act for
3. **Background** - Factual summary
4. **Legal basis** - Cause of action
5. **Quantum** - Itemised amounts with interest
6. **Demand** - Clear demand with deadline
7. **Consequences** - What happens if ignored
8. **Costs reservation**

### Requirements
- Factually accurate
- Legally sound
- Firm but professional tone
- Reasonable deadline (7-14 days)
- Interest calculated correctly

### Special Considerations
- If NCA applies: Consider s129 notice instead
- If CPA applies: Consider s70 provisions
- Preserve proof of delivery

## Output
Ready-to-send Letter of Demand.
""",
            human_actions=[
                "Review draft for accuracy",
                "Verify interest calculation",
                "Send via registered mail/email",
                "Diary follow-up date"
            ],
            verification_required=[
                "Client approval obtained",
                "Interest rate and calculation verified",
                "Correct legal entity addressed"
            ],
            risk_level=RiskLevel.MEDIUM,
            outputs=["Letter of demand", "Proof of delivery", "Diary entries"],
            estimated_time="1-2 hours",
            dependencies=[1]
        ),
        WorkflowStep(
            step_number=3,
            title="Pleadings Preparation",
            step_type=StepType.DRAFTING,
            description="Draft summons/combined summons with particulars of claim.",
            ai_prompt="""
# Particulars of Claim Drafting

## Role
You are Counsel drafting Particulars of Claim.

## Task
Draft Particulars of Claim that:

### Structure
1. **Heading** - Court, case number, parties
2. **Parties** - Full descriptions and domicilium
3. **Jurisdiction** - Basis for court's jurisdiction
4. **Agreement/Relationship** - Foundation of claim
5. **Breach/Wrongful conduct** - What defendant did wrong
6. **Damages** - Itemised with calculations
7. **Prayer** - Specific relief sought

### Pleading Principles
- Plead facts, not evidence
- Every material fact alleged
- One proposition per paragraph
- Clear and unambiguous

### Annexures
- Attach written agreements
- Mark as "A", "B" etc.
- Reference in body

### Prayer
- Capital amount
- Interest (rate, from date, to payment)
- Costs (scale if applicable)
- Further/alternative relief

## Output
Complete Particulars of Claim ready for filing.
""",
            human_actions=[
                "Review pleading for completeness",
                "Prepare summons form",
                "Arrange service (sheriff)",
                "File with registrar"
            ],
            verification_required=[
                "All elements of cause of action pleaded",
                "Interest correctly claimed",
                "Correct court selected",
                "Annexures complete"
            ],
            risk_level=RiskLevel.HIGH,
            outputs=["Combined summons", "Particulars of claim", "Proof of filing"],
            estimated_time="2-4 hours",
            dependencies=[1, 2]
        ),
        WorkflowStep(
            step_number=4,
            title="Interlocutory Applications",
            step_type=StepType.DRAFTING,
            description="Handle any interlocutory applications (summary judgment, exceptions, striking out).",
            ai_prompt="""
# Interlocutory Application Assessment

## Role
You are a Litigation Counsel evaluating interlocutory steps.

## Task
Assess available interlocutory remedies:

### 1. Summary Judgment (Rule 32)
**Availability:**
- Is claim liquidated or specific performance?
- Is there triable defence disclosed?
- Assessment of defendant's plea

**Recommendation:** [Proceed / Not advisable / Further info needed]

### 2. Exception
**Grounds:**
- Does plea disclose a defence?
- Is it vague and embarrassing?
- Any points of law to take?

**Recommendation:** [Take exception / Proceed to trial]

### 3. Striking Out
**Grounds:**
- Scandalous matter?
- Irrelevant averments?
- Prejudicial content?

**Recommendation:** [Strike out / Leave for trial]

### 4. Request for Further Particulars
**Needed:**
- What particulars required?
- Are they necessary for pleading?

### 5. Discovery
**Strategy:**
- Documents to request
- Interrogatories to serve
- Expert reports needed?

## Output
Interlocutory strategy memo with recommendations.
""",
            human_actions=[
                "Consider cost-benefit of interlocutory steps",
                "Consult with counsel on complex matters",
                "Draft necessary applications"
            ],
            verification_required=[
                "Time limits for interlocutory steps checked",
                "Cost implications considered",
                "Client authority for additional steps"
            ],
            risk_level=RiskLevel.MEDIUM,
            outputs=["Strategy memo", "Draft applications if needed"],
            estimated_time="2-4 hours",
            dependencies=[3]
        ),
        WorkflowStep(
            step_number=5,
            title="Trial Preparation",
            step_type=StepType.STRATEGY,
            description="Comprehensive trial preparation including witness preparation and heads of argument.",
            ai_prompt="""
# Trial Preparation Pack

## Role
You are Senior Counsel preparing for trial.

## Task
Prepare comprehensive trial bundle:

### 1. Issues Analysis
- Agreed facts (for s37 admission)
- Disputed facts
- Legal issues for determination
- Burden and standard of proof

### 2. Evidence Summary
**Our Evidence:**
| Witness | Evidence on | Strengths | Vulnerabilities |
|---------|-------------|-----------|-----------------|

**Their Evidence:**
| Witness | Expected evidence | Cross-examination points |
|---------|-------------------|-------------------------|

### 3. Legal Authorities
- Authorities for each legal point
- Key passages to cite
- Distinguishing contrary authority

### 4. Heads of Argument Structure
1. Introduction and issues
2. Factual background
3. Legal framework
4. Application and submissions
5. Costs
6. Order sought

### 5. Cross-Examination Outlines
For each opposing witness:
- Key challenges
- Documents to put
- Sequence of questions

### 6. Witness Preparation Notes
For each of our witnesses:
- Key evidence to elicit
- Anticipated cross-examination
- Preparation points

## Output
Trial preparation pack with all components.
""",
            human_actions=[
                "Prepare trial bundle (paginated)",
                "Brief counsel",
                "Prepare witnesses",
                "Pre-trial conference attendance"
            ],
            verification_required=[
                "Trial bundle complete and paginated",
                "Heads of argument filed",
                "Witnesses prepared and available",
                "Pre-trial checklist completed"
            ],
            risk_level=RiskLevel.CRITICAL,
            outputs=["Trial bundle", "Heads of argument", "Witness prep notes"],
            estimated_time="8-16 hours",
            dependencies=[1, 2, 3, 4]
        ),
        WorkflowStep(
            step_number=6,
            title="Post-Trial Actions",
            step_type=StepType.PROCEDURAL,
            description="Handle post-judgment actions including enforcement or appeal.",
            ai_prompt="""
# Post-Judgment Actions

## Role
You are a Litigation Attorney handling post-judgment matters.

## Task
Depending on outcome:

### If Successful (Judgment in Favour)
**Enforcement Steps:**
1. Obtain court order
2. Tax costs (if applicable)
3. Serve order on judgment debtor
4. If non-payment:
   - Writ of execution
   - Warrant of attachment
   - Section 65 enquiry
   - Emolument attachment order
   - Insolvency proceedings

**Enforcement Checklist:**
- Time to appeal not waived
- Judgment entered correctly
- Costs taxed and certified
- Execution documentation prepared

### If Unsuccessful (Judgment Against)
**Appeal Assessment:**
- Grounds for appeal
- Prospects of success
- Leave to appeal requirements
- Time limits (15/20 days)
- Security for costs

**Appeal Recommendation:** [Appeal / Accept / Seek leave to SCA]

### Settlement Considerations
- Settlement still possible?
- Payment plan negotiations
- Structured settlement terms

## Output
Post-judgment action plan with recommendations.
""",
            human_actions=[
                "Obtain certified court order",
                "Advise client on outcome",
                "Instruct sheriff if execution needed",
                "Diarise appeal deadlines"
            ],
            verification_required=[
                "Judgment correctly reflects court's order",
                "Appeal deadlines calculated correctly",
                "Client instructions obtained for next steps"
            ],
            risk_level=RiskLevel.HIGH,
            outputs=["Post-judgment memo", "Execution papers or appeal notice"],
            estimated_time="2-4 hours",
            dependencies=[5]
        )
    ],
    key_legislation=[
        "Uniform Rules of Court (High Court)",
        "Magistrates' Courts Rules",
        "Criminal Procedure Act 51 of 1977 (if criminal)",
        "Prescription Act 68 of 1969",
        "Superior Courts Act 10 of 2013"
    ],
    ethical_considerations=[
        "Do not mislead the court",
        "Cite contrary authority known to you",
        "Maintain client confidentiality",
        "Verify all facts before pleading",
        "Ensure AI-drafted pleadings are reviewed"
    ],
    quality_checkpoints=[
        "Case assessment reviewed before proceedings",
        "Pleadings reviewed by senior attorney/counsel",
        "All court deadlines diarised and monitored",
        "Client kept informed at each stage"
    ],
    total_estimated_time="20-50+ hours",
    complexity="High"
)

# ═══════════════════════════════════════════════════════════════════════════════
# DUE DILIGENCE WORKFLOW
# ═══════════════════════════════════════════════════════════════════════════════

DUE_DILIGENCE_WORKFLOW = LegalWorkflow(
    title="Corporate Due Diligence Pipeline",
    category=WorkflowCategory.CORPORATE,
    description="Comprehensive due diligence workflow for M&A, investments, and business acquisitions.",
    use_cases=[
        "Mergers and acquisitions",
        "Private equity investments",
        "Property acquisitions",
        "Business purchases",
        "Joint ventures"
    ],
    steps=[
        WorkflowStep(
            step_number=1,
            title="Scope and Planning",
            step_type=StepType.STRATEGY,
            description="Define DD scope, prepare checklists, and plan the exercise.",
            ai_prompt="""
# Due Diligence Scoping

## Role
You are a Transaction Partner scoping a due diligence exercise.

## Task
Prepare a comprehensive DD plan:

### 1. Transaction Overview
- Deal type (share sale / asset sale / merger)
- Parties involved
- Target company/business
- Transaction timeline

### 2. DD Scope
**Workstreams:**
☐ Corporate/Company Secretarial
☐ Commercial/Contracts
☐ Property/Real Estate
☐ Intellectual Property
☐ Employment/Labour
☐ Tax
☐ Litigation/Disputes
☐ Regulatory/Licences
☐ Environmental
☐ IT/Data Protection
☐ Insurance

### 3. DD Checklist
For each workstream, list documents to request.

### 4. Data Room Protocol
- Access arrangements
- Q&A process
- Document management

### 5. Team Allocation
- Workstream leads
- Support resources
- Timelines per workstream

### 6. Key Risk Areas
- [Identify likely risk areas based on deal type]

## Output
DD scoping memo and initial request list.
""",
            human_actions=[
                "Agree scope with client",
                "Allocate team resources",
                "Send document request list",
                "Set up data room access"
            ],
            verification_required=[
                "Scope aligned with transaction agreement",
                "Request list comprehensive for deal type",
                "Team availability confirmed"
            ],
            risk_level=RiskLevel.LOW,
            outputs=["DD scoping memo", "Document request list", "Team allocation"],
            estimated_time="2-4 hours",
            dependencies=[]
        ),
        WorkflowStep(
            step_number=2,
            title="Document Review and Analysis",
            step_type=StepType.REVIEW,
            description="Review all DD documents and identify issues.",
            ai_prompt="""
# Due Diligence Document Review

## Role
You are a DD Analyst reviewing documents for a [workstream].

## Task
For each document reviewed:

### Document Summary Template
**Document:** [Name]
**Category:** [Corporate/Commercial/Property/etc.]
**Date:** [Document date]

**Summary:**
[2-3 sentence summary of document content]

**Key Terms:**
- [Important provisions]

**Red Flags:**
🔴 [Critical issues - deal breakers]
🟡 [Significant issues - require negotiation]
🟢 [Minor issues - note for completion]

**Missing Items:**
- [Documents referenced but not provided]

**Follow-up Required:**
- [Questions to ask seller]

### Risk Classification
| Risk | Category | Severity | Mitigation |
|------|----------|----------|------------|
| [Description] | [Type] | [H/M/L] | [Proposed] |

## Format
Maintain consistent structure across all documents.
""",
            human_actions=[
                "Review AI analysis for accuracy",
                "Verify critical documents manually",
                "Submit Q&A questions to seller",
                "Flag deal-breaker issues immediately"
            ],
            verification_required=[
                "Material contracts manually reviewed",
                "Title deeds verified",
                "Litigation searches conducted",
                "Tax compliance confirmed"
            ],
            risk_level=RiskLevel.MEDIUM,
            outputs=["Document summaries", "Issue tracker", "Q&A log"],
            estimated_time="10-40+ hours",
            dependencies=[1]
        ),
        WorkflowStep(
            step_number=3,
            title="Third Party Searches",
            step_type=StepType.RESEARCH,
            description="Conduct external searches and verifications.",
            ai_prompt="""
# Third Party Search Requirements

## Task
Identify and conduct necessary searches:

### Corporate Searches
☐ CIPC company search (target and subsidiaries)
☐ Director searches
☐ Shareholder verification
☐ Security interest register (movables)

### Property Searches
☐ Deeds office search
☐ Surveyor general diagrams
☐ Zoning certificates
☐ Rates clearance

### Litigation Searches
☐ High Court case search (all divisions)
☐ Magistrates court search
☐ Labour Court search
☐ CCMA search

### Regulatory Searches
☐ Relevant industry regulator
☐ Competition Commission filing check
☐ Environmental authorisations

### Credit Searches
☐ Credit bureau report
☐ Trade references

### Intellectual Property
☐ CIPC trademark search
☐ Patent search
☐ Domain name verification

## Search Results Template
| Search | Source | Date | Result | Issues |
|--------|--------|------|--------|--------|

## Output
Search results summary with findings.
""",
            human_actions=[
                "Order and conduct searches",
                "Review search results",
                "Follow up on any adverse findings",
                "Update issue tracker"
            ],
            verification_required=[
                "All searches conducted and documented",
                "Adverse findings investigated",
                "Results cross-referenced with disclosed information"
            ],
            risk_level=RiskLevel.MEDIUM,
            outputs=["Search results pack", "Issue updates"],
            estimated_time="4-8 hours",
            dependencies=[1]
        ),
        WorkflowStep(
            step_number=4,
            title="Due Diligence Report",
            step_type=StepType.DRAFTING,
            description="Prepare comprehensive DD report for client.",
            ai_prompt="""
# Due Diligence Report Drafting

## Role
You are Transaction Counsel preparing a DD report.

## Task
Draft comprehensive report:

### 1. Executive Summary
[2-page summary for executives covering key findings]

### 2. Deal Overview
- Transaction structure
- Parties
- Key commercial terms
- Conditions precedent

### 3. Workstream Reports
For each workstream:

**[WORKSTREAM NAME]**

**Scope:** What was reviewed
**Key Documents:** Material documents identified
**Findings:**
- [Finding 1 with risk rating]
- [Finding 2 with risk rating]
**Red Flags:** [Critical issues]
**Recommendations:** [Proposed mitigations]

### 4. Risk Matrix
| # | Issue | Category | Risk | Impact | Mitigation |
|---|-------|----------|------|--------|------------|
| 1 | [Issue] | [Cat] | H/M/L | [Impact] | [Action] |

### 5. Conditions Precedent Recommendations
[What should be conditions precedent to closing]

### 6. Warranty/Indemnity Recommendations
[Specific warranties and indemnities to negotiate]

### 7. Post-Completion Actions
[Matters to address after closing]

### 8. Appendices
- Full document index
- Search results
- Detailed workstream findings

## Output
Complete DD report ready for client delivery.
""",
            human_actions=[
                "Review report for accuracy",
                "Present findings to client",
                "Discuss commercial implications",
                "Agree on negotiation approach"
            ],
            verification_required=[
                "All findings accurately reported",
                "Risk ratings appropriate",
                "Recommendations practical",
                "Report reviewed by partner"
            ],
            risk_level=RiskLevel.HIGH,
            outputs=["DD report", "Executive summary", "Risk matrix"],
            estimated_time="8-16 hours",
            dependencies=[2, 3]
        ),
        WorkflowStep(
            step_number=5,
            title="Transaction Document Input",
            step_type=StepType.DRAFTING,
            description="Translate DD findings into transaction document requirements.",
            ai_prompt="""
# DD to Transaction Document Mapping

## Role
You are Transaction Counsel translating DD findings into contract terms.

## Task
Based on DD findings, draft:

### 1. Conditions Precedent
For each material risk, draft CP if appropriate:
```
[X]. [Target] shall have obtained [approval/consent/clearance] from [authority] in respect of [matter].
```

### 2. Warranties
For each risk area, draft specific warranty:
```
[X]. The Seller warrants that:
[X.1] [Specific warranty addressing DD finding]
[X.2] [Related sub-warranty]
```

### 3. Indemnities
For known liabilities, draft indemnity:
```
[X]. The Seller hereby indemnifies the Purchaser against any loss arising from [specific matter identified in DD].
```

### 4. Disclosure Letter Items
[Matters to be disclosed against warranties]

### 5. Completion Deliverables
[Documents/actions required at completion]

### 6. Post-Completion Obligations
[Matters to be addressed after completion]

## Output
Transaction document input schedule.
""",
            human_actions=[
                "Integrate into transaction documents",
                "Negotiate with counterparty",
                "Adjust for commercial feedback"
            ],
            verification_required=[
                "All material DD findings addressed",
                "Drafting technically correct",
                "Commercially reasonable terms"
            ],
            risk_level=RiskLevel.HIGH,
            outputs=["CP schedule", "Warranty schedule", "Indemnity drafts"],
            estimated_time="4-8 hours",
            dependencies=[4]
        )
    ],
    key_legislation=[
        "Companies Act 71 of 2008",
        "Competition Act 89 of 1998 (merger notification)",
        "Securities Acts (if listed company)",
        "Tax Acts (income tax, VAT, transfer duty)",
        "POPIA (for employee/customer data)"
    ],
    ethical_considerations=[
        "Maintain strict confidentiality of DD information",
        "Do not share information between competing bidders",
        "Verify AI analysis of critical documents",
        "Ensure conflicts checked between parties"
    ],
    quality_checkpoints=[
        "Scope confirmed with client before starting",
        "Material contracts manually reviewed",
        "Third party searches completed",
        "Report reviewed by partner before delivery"
    ],
    total_estimated_time="30-100+ hours",
    complexity="High"
)

# ═══════════════════════════════════════════════════════════════════════════════
# ALL WORKFLOWS
# ═══════════════════════════════════════════════════════════════════════════════

ALL_WORKFLOWS: Dict[str, LegalWorkflow] = {
    "contract_review": CONTRACT_REVIEW_WORKFLOW,
    "litigation_support": LITIGATION_SUPPORT_WORKFLOW,
    "due_diligence": DUE_DILIGENCE_WORKFLOW,
}

def get_workflows_by_category(category: WorkflowCategory) -> List[LegalWorkflow]:
    """Get all workflows for a specific category"""
    return [w for w in ALL_WORKFLOWS.values() if w.category == category]

def get_workflow_summary(workflow: LegalWorkflow) -> str:
    """Get a summary of a workflow"""
    steps_summary = "\n".join(
        f"  {s.step_number}. {s.title} ({s.estimated_time}) - {s.risk_level.value}"
        for s in workflow.steps
    )
    return f"""
# {workflow.title}

**Category:** {workflow.category.value}
**Complexity:** {workflow.complexity}
**Total Time:** {workflow.total_estimated_time}

**Description:**
{workflow.description}

**Use Cases:**
{chr(10).join(f"• {uc}" for uc in workflow.use_cases)}

**Workflow Steps:**
{steps_summary}

**Key Legislation:**
{chr(10).join(f"• {leg}" for leg in workflow.key_legislation)}

**Ethical Considerations:**
{chr(10).join(f"⚠️ {eth}" for eth in workflow.ethical_considerations)}

**Quality Checkpoints:**
{chr(10).join(f"✓ {qc}" for qc in workflow.quality_checkpoints)}
"""

def get_step_prompt(workflow: LegalWorkflow, step_number: int) -> str:
    """Get the AI prompt for a specific workflow step"""
    step = next((s for s in workflow.steps if s.step_number == step_number), None)
    if not step:
        return f"Step {step_number} not found in workflow {workflow.title}"
    
    return f"""
# Workflow: {workflow.title}
# Step {step.step_number}: {step.title}

**Risk Level:** {step.risk_level.value}
**Estimated Time:** {step.estimated_time}

{step.ai_prompt}

---
## Human Actions Required After AI Completion:
{chr(10).join(f"• {action}" for action in step.human_actions)}

## Verification Required:
{chr(10).join(f"✓ {ver}" for ver in step.verification_required)}

## Expected Outputs:
{chr(10).join(f"→ {output}" for output in step.outputs)}
"""

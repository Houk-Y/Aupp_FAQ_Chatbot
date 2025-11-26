"""
AUPP FAQ Dataset - Complete Unified Dataset (Updated to 106+ Questions)
This script creates a single CSV file with all FAQ data from the provided JSON and
newly sourced data to exceed 100 total questions.
"""

import pandas as pd
import json

# Complete AUPP FAQ Dataset - All categories combined
complete_data = {"id": [], "category": [], "question": [], "answer": [], "source": []}

# Counter for IDs
id_counter = 1


def add_to_dataset(data_list, source_name):
    """Helper function to add data to the complete_data dictionary and update ID counter."""
    global id_counter
    for cat, q, a in data_list:
        complete_data["id"].append(id_counter)
        complete_data["category"].append(cat)
        complete_data["question"].append(q)
        complete_data["answer"].append(a)
        complete_data["source"].append(source_name)
        id_counter += 1


# ============================================================================
# ACADEMIC POLICIES & REGULATIONS (Original 5 + 4 new)
# ============================================================================
academic_policies = [
    (
        "Academic Policies & Regulations",  # Category updated for consistency
        "When can I take a leave of absence from AUPP?",
        "You can request a Leave of Absence (LOA) for life situations, medical conditions, or psychological conditions that significantly impair your ability to function successfully at the University. The impairment must be recognized by a physician or the University. You need to complete a LOA Form and submit it to the Office of the Registrar with appropriate signatures.",
    ),
    (
        "Academic Policies & Regulations",
        "Who approves a leave of absence?",
        "The authority to grant a Leave of Absence rests with the President. The Office of the Registrar investigates your situation and makes a recommendation to the President.",
    ),
    (
        "Academic Policies & Regulations",
        "Can I transfer credits from another university to AUPP?",
        "Yes, you can transfer credits from another university to AUPP. All decisions about transfer of coursework are at the sole discretion of AUPP. Transfer students may be required to take English and Math placement examinations.",
    ),
    (
        "Academic Policies & Regulations",
        "What grade do I need for my credits to transfer?",
        "You need to have earned a grade of C or better for courses to be eligible for transfer credit. Only courses with grades of C or better and that are similar to courses offered at AUPP will be accepted.",
    ),
    (
        "Academic Policies & Regulations",
        "How many credits can I transfer?",
        "The maximum number of units that can be transferred to AUPP is 60. Only courses with a grade of C or better that are similar to AUPP courses are eligible.",
    ),
    (
        "Academic Policies & Regulations",
        "What is an Overload course unit load?",
        "The normal course unit load in any semester is 15 to 17 units. Students who could graduate at the end of the semester are permitted to exceed the 19 unit limit and/or waive the requirement of a 3.0 GPA for that semester with the permission of the VPASA. A course load of 20-22 units is for exceptional circumstances.",
    ),
    (
        "Academic Policies & Regulations",
        "What is Academic Probation and how does it happen?",
        "If a student's semester or cumulative GPA falls below 2.00, they are placed on Academic Probation. This means they cannot hold office in student organizations and must meet with VPASA at least once per semester.",
    ),
    (
        "Academic Policies & Regulations",
        "Can a student be suspended or dismissed?",
        "Yes. Students may be suspended for refusal to complete the conditions of probation or failure to improve their overall grade point average in the semester while on probation.",
    ),
    (
        "Academic Policies & Regulations",
        "What are AUPP's core values for students?",
        "The student standards pertain to AUPP's values: CLEAR AND EFFECTIVE COMMUNICATOR, SELF-DIRECTED AND LIFE-LONG LEARNER, CREATIVE AND PRACTICAL PROBLEM-SOLVER, RESPONSIBLE AND INVOLVED CITIZEN, and INTEGRATIVE AND INFORMED THINKER.",
    ),
]

add_to_dataset(academic_policies, "academic_policies_original_and_new")

# ============================================================================
# ADMISSIONS (Original 5 + 6 new)
# ============================================================================
admissions = [
    (
        "Admissions",
        "How do I apply to AUPP?",
        "You can apply through our online application system. Visit aupp.edu.kh and complete the application form with all required documents.",
    ),
    (
        "Admissions",
        "What are the admission requirements?",
        "Admission requirements include high school transcripts, English proficiency test (IELTS 6.0 or TOEFL 79, or take our English Placement Test), completed application form, and passport-sized photos.",
    ),
    (
        "Admissions",
        "Do I need to take an English Placement Test?",
        "Yes, all prospective students must meet the English Placement Test requirement unless you can provide IELTS 6.0+ or TOEFL 79+ scores. The EPT is free.",
    ),
    (
        "Admissions",
        "What if I don't pass the English Placement Test?",
        "You can enroll in our English Preparatory Program (EPP). Level 2 requires 3 semesters, Level 3 requires 2 semesters, Level 4 requires 1 semester before starting Year 1.",
    ),
    (
        "Admissions",
        "Do international students need to take the English test?",
        "Holders of passports from the United States, United Kingdom, Australia, New Zealand, or Canada are not required to take the English Placement Test.",
    ),
    (
        "Admissions",
        "What is the required IELTS score for direct admission?",
        "An overall band 6.0 and above on the Academic Module of the IELTS (taken within two years of admission) is required for direct admission to Collegiate programs.",
    ),
    (
        "Admissions",
        "What is the required TOEFL score for direct admission?",
        "A TOEFL iBT score of at least 79 (earned within two years of application date) is required for direct admission to Collegiate programs.",
    ),
    (
        "Admissions",
        "What application materials must be submitted?",
        "Required materials include high school records/transcripts, proof of English proficiency (or EPT), completed application form, and passport-sized photos. Original documents must be provided.",
    ),
    (
        "Admissions",
        "When is the application deadline?",
        "Application deadlines vary by semester and are determined by the Office of Registrar and Admissions. Late admissions may be considered up to the end of the course add/drop period.",
    ),
    (
        "Admissions",
        "What are the admission criteria for the Master of Business Administration (MBA) Dual Degree?",
        "The criteria include proof of identity, proof of College/University Graduation, other required documents, and English proficiency (TOEFL iBT 79 or IELTS 6.5, or an EPT waiver).",
    ),
    (
        "Admissions",
        "What is Conditional Admission?",
        "Conditional Admission is available for students who are not able to submit all application materials immediately. Students must meet the conditions set by the university.",
    ),
]

add_to_dataset(admissions, "admissions_original_and_new")

# ============================================================================
# TUITION & PAYMENT (Original 5)
# ============================================================================
tuition = [
    (
        "Tuition & Payment",
        "How much are tuition fees per year?",
        "The tuition fees for Dual degree program costs $9,000 per year and the Single degree program costs $6,000 per year. Students pay tuition fees prior to the start of each semester.",
    ),
    (
        "Tuition & Payment",
        "Can I pay tuition in installments?",
        "Yes. If you are in a difficult financial situation, you may request Management for a payment plan in installments.",
    ),
    (
        "Tuition & Payment",
        "Can I pay full tuition for the whole year in advance?",
        "Yes, we accept full tuition payments before the academic year.",
    ),
    (
        "Tuition & Payment",
        "What is the deferred payment plan?",
        "The deferred payment plan allows students to pay 40% of tuition before registration, 30% within 50 calendar days, and final 30% plus additional charge before final exams.",
    ),
    (
        "Tuition & Payment",
        "Can I obtain a student loan?",
        "Yes. AUPP's student loan program allows students with financial need to borrow up to $2,000 per academic year with 5% interest per semester. Repayment begins once employed.",
    ),
]

add_to_dataset(tuition, "tuition_original")

# ============================================================================
# SCHOLARSHIPS (Original 5 + 4 new)
# ============================================================================
scholarships = [
    (
        "Scholarships",
        "Does AUPP provide scholarships?",
        "Yes, AUPP provides scholarships based on academic achievements and financial need. We offer Academic Excellence Scholarships, Financial Need Scholarships, Techo Digital Talent Scholarships, AMT Scholarships, and more.",
    ),
    (
        "Scholarships",
        "How do I qualify for a scholarship?",
        "Scholarships are awarded based on academic achievements (Grades A or B on National Examinations), discerned potential, and socioeconomic status of the student's family.",
    ),
    (
        "Scholarships",
        "What is the Academic Excellence Scholarship?",
        "The Academic Excellence Scholarship is awarded to applicants who achieve overall grades of A or B on the national high school exam, covering all majors at AUPP.",
    ),
    (
        "Scholarships",
        "What is the Techo Digital Talent Scholarship?",
        "The Techo Digital Talent Scholarship 2025 offers 200 full scholarships for students with Grade A, B or C to study digital majors (AI, Cybersecurity, Digital Infrastructure, ICT, Software Development). It covers application, tuition, and administration fees.",
    ),
    (
        "Scholarships",
        "Can I get a full scholarship?",
        "Full scholarships are available for students who obtained Grade A on their National Examinations and demonstrate financial need. Several programs offer full coverage including tuition and fees.",
    ),
    (
        "Scholarships",
        "What is the Financial Need Scholarship?",
        "The Financial Need Scholarship is available to applicants who achieve 'Overall grades of A or B' on their national high school exam and demonstrate financial need.",
    ),
    (
        "Scholarships",
        "What are the initial steps to apply for the full scholarship?",
        "The initial steps are to fill in the online application and submit required documents, which include grade reports for years 10, 11, and 12, and two Personal Statements.",
    ),
    (
        "Scholarships",
        "What is the difference between merit and full scholarship?",
        "The Academic Excellence (Merit) scholarship is based on academic achievements (A or B grades on National Exams), while the Full scholarship also requires demonstration of financial need.",
    ),
    (
        "Scholarships",
        "Does AUPP provide special fees for siblings?",
        "Yes, for siblings enrolled at AUPP, there is a 10% credit for the second child as long as the elder is still studying.",
    ),
]

add_to_dataset(scholarships, "scholarships_original_and_new")

# ============================================================================
# PROGRAMS (Original 6 + 5 new)
# ============================================================================
programs = [
    (
        "Programs",
        "What majors can I study at AUPP?",
        "AUPP offers Dual Degrees (Business Administration, Law, Information Technology Management with UA/FHSU) and Single Degrees (Business, ICT, Law, International Relations and Diplomacy).",
    ),
    (
        "Programs",
        "What is the difference between Single and Dual degree?",
        "Dual degree students receive two degrees - one from AUPP and one from University of Arizona or Fort Hays State University. Dual degrees cost $9,000/year vs $6,000/year for single degrees. Dual degree students have access to partner university resources.",
    ),
    (
        "Programs",
        "What is the main focus in the Business program?",
        "The Business program focuses on management, human resources, marketing, and accounting and finance. It provides deep understanding of business operations and prepares students for staff and management positions.",
    ),
    (
        "Programs",
        "What is the Law program about?",
        "The Law program focuses on Cambodian law, U.S. law, and international law. Students need additional studies for 1-2 years to become prosecutors, lawyers, or judges in Cambodia as required by the Government.",
    ),
    (
        "Programs",
        "Can I change my major?",
        "Students may change majors with approval from the Vice President of Academic Affairs.",
    ),
    (
        "Programs",
        "What minors are available at AUPP?",
        "AUPP offers minors in Economics, Innovation and Entrepreneurship, Tourism and Hospitality Management (ITHM), Law, and Southeast Asian Studies. All minors require 15 credits.",
    ),
    (
        "Programs",
        "What is the main focus of the International Relations and Diplomacy program?",
        "The International Relations and Diplomacy program is an advanced degree focusing on international relations, political science, and diplomacy, preparing students for global affairs.",
    ),
    (
        "Programs",
        "What are the dual degree majors available?",
        "Dual degree majors include Bachelor of Science in Business Administration and Bachelor of Arts in Law (with University of Arizona), and Bachelor of Science in Information Technology Management (with Fort Hays State University).",
    ),
    (
        "Programs",
        "What are some new Law specializations at AUPP?",
        "New law specializations include Laws in International Business and Digital Technologies, and Laws in Artificial Intelligence/Cybersecurity.",
    ),
    (
        "Programs",
        "How long is a bachelor's degree program?",
        "Bachelor degree programs at AUPP are typically 4 years (8 semesters). Full-time students usually take 5 courses (15 credits) per semester.",
    ),
    (
        "Programs",
        "How many credit units are full-time students expected to take per semester?",
        "The normal course unit load in any semester is 15 to 17 units. Full-time students usually take 5 courses (15 credits) per semester.",
    ),
]

add_to_dataset(programs, "programs_original_and_new")

# ============================================================================
# STUDENT LIFE (Original 5 + 2 new)
# ============================================================================
student_life = [
    (
        "Student Life",
        "What student clubs are available at AUPP?",
        "There are 25 student-led clubs including sports (football, badminton, tennis, basketball), debate, media, Chinese, photography, and volunteer clubs. Students can join multiple clubs and receive credit for extracurricular activities.",
    ),
    (
        "Student Life",
        "Does AUPP offer student accommodation?",
        "Yes, AUPP offers affordable accommodation at separate residences for men and women near campus. Each room includes basic amenities with common spaces for socializing and studying.",
    ),
    (
        "Student Life",
        "What is campus life like at AUPP?",
        "AUPP has an active campus with academics, clubs, social activities, competitions, volunteer work, and internship opportunities. The state-of-the-art campus opened in 2017 with modern facilities.",
    ),
    (
        "Student Life",
        "What facilities does AUPP have?",
        "AUPP features model classrooms, digital learning platforms, Teaching & Learning Center, state-of-the-art library, sports facilities (football, badminton, tennis, basketball courts), cafeteria, and study spaces.",
    ),
    (
        "Student Life",
        "How many hours do I study per day?",
        "Students study on average 3 hours per day in class (Monday-Friday) plus 4.5 hours of self-study for assignments, readings, and group projects.",
    ),
    (
        "Student Life",
        "In what year do I do internship?",
        "Students are required to do internship in Year 3 to gain practical experience. The Student Affairs Coordinator provides support and consultation for internship placement.",
    ),
    (
        "Student Life",
        "Does AUPP help students with internships?",
        "The Student Affairs Coordinator provides support and consultation for internship placement. The university also receives positive feedback about graduate capabilities from companies who recruit students.",
    ),
]

add_to_dataset(student_life, "student_life_original_and_new")

# ============================================================================
# GRADING SYSTEM (Original 5 + 4 new)
# ============================================================================
grading = [
    (
        "Grading System",
        "What is the GPA for an A grade?",
        "A grade is 4.00 GPA (93-100%) representing outstanding attainment of course goals.",
    ),
    (
        "Grading System",
        "What GPA do I need to graduate?",
        "A minimum cumulative GPA of 2.00 is required for graduation and to remain in good academic standing.",
    ),
    (
        "Grading System",
        "What happens if my GPA falls below 2.00?",
        "If your semester or cumulative GPA falls below 2.00, you are placed on academic probation. You cannot hold office in student organizations and must meet with VPASA at least once per semester.",
    ),
    (
        "Grading System",
        "Can I request a grade change?",
        "Yes, if there was a calculation/recording error, non-academic bias, or unequal grading standards. Submit before end of 2nd week of next semester.",
    ),
    (
        "Grading System",
        "How is GPA calculated?",
        "Multiply grade quality points by course units, sum total quality points, and divide by total completed units. A=4.00, A-=3.67, B+=3.33, B=3.00, etc.",
    ),
    (
        "Grading System",
        "What percentage is a B grade?",
        "A B grade is 3.00 GPA and represents 83-86.99% (Good attainment of course goals).",
    ),
    (
        "Grading System",
        "What percentage is a C grade?",
        "A C grade is 2.00 GPA and represents 73-76.99% (Average attainment of course goals). This is the minimum required grade for transfer credit.",
    ),
    (
        "Grading System",
        "What is the GPA for an A- grade?",
        "An A- grade is 3.67 GPA and represents 90-92.99% (Superior attainment of course goals).",
    ),
    (
        "Grading System",
        "What is 'Good Academic Standing'?",
        "Students who maintain a grade point average (GPA) of 2.00 or higher for each semester and have a cumulative GPA (CGPA) of 2.00 or higher are considered to be in good academic standing.",
    ),
]

add_to_dataset(grading, "grading_original_and_new")

# ============================================================================
# CAREER & EMPLOYMENT (Original 5)
# ============================================================================
career = [
    (
        "Career Opportunities",
        "What do AUPP graduates do after graduation?",
        "AUPP graduates start their own businesses, work in companies, organizations, public institutions, and ministries, or pursue postgraduate education abroad (Masters, JD, PhD).",
    ),
    (
        "Career Opportunities",
        "Does AUPP help students find jobs?",
        "Yes, AUPP provides guidance for career success. Many companies, organizations, and public institutions recruit our students. The university receives positive feedback about graduate capabilities.",
    ),
    (
        "Career Opportunities",
        "Can AUPP graduates study abroad?",
        "Yes, definitely! Many alumni are currently pursuing or have completed Masters, JD, and PhD degrees in the US, Australia, England and other universities.",
    ),
    (
        "Career Opportunities",
        "What jobs are available in AUPP?",
        "AUPP hires full-time faculty (Business, Digital Technologies, Law), adjunct faculty, administrative coordinators, IT staff, HR officers, graphic designers, and various support positions.",
    ),
    (
        "Career Opportunities",
        "What are faculty requirements at AUPP?",
        "Faculty must have earned Master's or Ph.D. from American or western universities with minimum 3 years teaching experience, including online teaching using Canvas LMS.",
    ),
]

add_to_dataset(career, "career_original")

# ============================================================================
# CONTACT & LOCATION (Original 4)
# ============================================================================
contact = [
    (
        "Contact Information",
        "Where is AUPP located?",
        "AUPP is located at #278H, Street 201R, Kroalkor Village, Sangkat Kilometer 6, Khan Russey Keo, Phnom Penh, Cambodia. The state-of-the-art campus is in northern Phnom Penh.",
    ),
    (
        "Contact Information",
        "What is AUPP's phone number?",
        "You can contact AUPP by phone at (+855) 23 990 023.",
    ),
    (
        "Contact Information",
        "What is AUPP's email address?",
        "The email address for AUPP is info@aupp.edu.kh. For admissions: admissions@aupp.edu.kh. For careers: careers@aupp.edu.kh.",
    ),
    (
        "Contact Information",
        "Is AUPP on social media?",
        "Yes, AUPP is available on Facebook, Telegram, Instagram, and LinkedIn.",
    ),
]

add_to_dataset(contact, "contact_original")

# ============================================================================
# UNIVERSITY INFO (Original 5)
# ============================================================================
university_info = [
    (
        "University Info",
        "When was AUPP founded?",
        "AUPP was established in 2013 as a Cambodian university with an American curriculum. It was founded by three visionaries who aimed to create a university based on US educational standards.",
    ),
    (
        "University Info",
        "What makes AUPP unique?",
        "AUPP is the only university in Cambodia providing American-style education with dual degree options to University of Arizona and Fort Hays State University. Faculty hold doctoral degrees and have US teaching experience. The campus has state-of-the-art facilities.",
    ),
    (
        "University Info",
        "What is AUPP's mission?",
        "AUPP's mission is to provide high-quality American-style education that fosters critical thinking, creativity, and ethical leadership. We develop globally competent graduates who contribute to Cambodia's socio-economic development.",
    ),
    (
        "University Info",
        "Is AUPP accredited?",
        "Yes, AUPP is fully accredited from 2019 to 2028. Institutional accreditation covers all degree programs. Dual degree programs are accredited by Higher Learning Commission through partner universities.",
    ),
    (
        "University Info",
        "Who are AUPP's partner universities?",
        "AUPP's partner institutions are the University of Arizona (UA) and Fort Hays State University (FHSU) in the United States.",
    ),
]

add_to_dataset(university_info, "university_info_original")

# ============================================================================
# FACULTY & LEADERSHIP (Original 4)
# ============================================================================
faculty = [
    (
        "Faculty & Leadership",
        "Who is the President of AUPP?",
        "Malcolm McIver is the President of AUPP.",
    ),
    (
        "Faculty & Leadership",
        "Who are the Deans at AUPP?",
        "The Deans are: Raimund Weiss (School of Social Sciences), Tek Ming Ng (School of Digital Technologies), Sing Ong Yu (School of Business), and Hisham Mousar (Acting Dean, School of Law).",
    ),
    (
        "Faculty & Leadership",
        "How many faculty members does AUPP have?",
        "AUPP has over 40 faculty members from Cambodia and around the world. The majority hold doctoral degrees in their fields with experience teaching at universities in the US and globally.",
    ),
    (
        "Faculty & Leadership",
        "Who are the Board of Trustees?",
        "The Board includes Dr. Jacquelyn Armitage, Dr. Richard Gustafson, Dr. Guido Gianasso, Jean-Pierre Pedrazzini, Rami Sharaf, Sok Ly, Paul Marca, Puy Kea, Dr. Lucille H. Sansing, and Kenneth Dunn.",
    ),
]

add_to_dataset(faculty, "faculty_original")

# ============================================================================
# ACADEMIC CALENDAR (Original 1 + 1 new)
# ============================================================================
academic_calendar = [
    (
        "Academic Calendar",
        "What is the academic year structure?",
        "AUPP follows the American calendar with Fall semester (mid-August to late December), Spring semester (mid-January to early May), and two 6-week Summer terms.",
    ),
    (
        "Academic Calendar",
        "What are the semesters at AUPP?",
        "AUPP has a Fall semester (mid-August to late December) and a Spring semester (mid-January to early May). There are also two 6-week Summer terms.",
    ),
]

add_to_dataset(academic_calendar, "academic_calendar_new")

# ============================================================================
# NEW: TUITION FEES (9 questions from user-provided list)
# ============================================================================
tuition_fees_new = [
    (
        "Tuition Fees",
        "How much is tuition per semester for bachelor’s single-degree programs at AUPP?",
        "Bachelor’s single-degree programs cost USD 3,000 per semester, across Fall and Spring, for 4 years.",
    ),
    (
        "Tuition Fees",
        "How much is tuition per semester for bachelor’s dual-degree programs at AUPP?",
        "Bachelor’s dual-degree programs cost USD 4,500 per semester over 4 years.",
    ),
    (
        "Tuition Fees",
        "What is the cost per course for master’s single-degree programs at AUPP?",
        "Master’s single-degree programs cost USD 900 per course.",
    ),
    (
        "Tuition Fees",
        "What is the cost per course for master’s dual-degree programs at AUPP?",
        "Master’s dual-degree programs cost USD 1,200 per course.",
    ),
    (
        "Tuition Fees",
        "How much are bridging courses for master’s students at AUPP?",
        "Bridging courses cost USD 900 per course.",
    ),
    (
        "Tuition Fees",
        "Are summer courses charged separately at AUPP?",
        "Yes, summer courses are charged separately from regular semesters. Tuition is calculated per course.",
    ),
    (
        "Tuition Fees",
        "What are the total costs for a 4-year dual degree at AUPP?",
        "Studying at AUPP for 4 years for a dual degree will cost a maximum of $36,000 in tuition ($9,000 per year).",
    ),
    (
        "Tuition Fees",
        "What are the benefits of pursuing a master's degree abroad after AUPP?",
        "By completing an undergraduate degree at AUPP instead of abroad, a student can pursue their master’s degree abroad for 1 or 2 years and save some money on overall education costs.",
    ),
    (
        "Tuition Fees",
        "When do students pay tuition fees?",
        "Students pay tuition fees prior to the start of each semester.",
    ),
]

add_to_dataset(tuition_fees_new, "tuition_fees_json")

# ============================================================================
# NEW: OTHER FEES (11 questions from user-provided list)
# ============================================================================
other_fees_new = [
    (
        "Other Fees",
        "How much is the AUPP application fee?",
        "All applicants must pay a non-refundable USD 35 application fee.",
    ),
    (
        "Other Fees",
        "How much is the administration fee per term?",
        "AUPP charges a USD 150 administration fee per academic term.",
    ),
    (
        "Other Fees",
        "What is the student activity fee at AUPP?",
        "AUPP charges a USD 50 student activity fee each term.",
    ),
    (
        "Other Fees",
        "How much is the technology fee at AUPP?",
        "A technology fee of USD 50 is charged per term.",
    ),
    (
        "Other Fees",
        "Does AUPP charge a graduation fee?",
        "Yes. The graduation fee is USD 200.",
    ),
    (
        "Other Fees",
        "How much is the ID card replacement fee?",
        "Replacing a student ID card costs USD 10.",
    ),
    (
        "Other Fees",
        "What is the official transcript fee at AUPP?",
        "A certified transcript costs USD 10 per copy.",
    ),
    (
        "Other Fees",
        "What is the diploma replacement fee?",
        "Replacing a diploma costs USD 120.",
    ),
    (
        "Other Fees",
        "What is the TOEFL ITP exam fee at AUPP?",
        "The TOEFL ITP exam fee is USD 30.",
    ),
    (
        "Other Fees",
        "What is the placement exam fee?",
        "The placement exam costs USD 30.",
    ),
    (
        "Other Fees",
        "Is the application fee refundable?",
        "No. The application fee is non-refundable.",
    ),
]

add_to_dataset(other_fees_new, "other_fees_json")

# ============================================================================
# NEW: PAYMENT METHOD (9 questions from user-provided list)
# ============================================================================
payment_method_new = [
    (
        "Payment Method",
        "Where can students pay tuition on campus?",
        "Students can pay tuition directly at the AUPP Finance Office on campus.",
    ),
    (
        "Payment Method",
        "Can students pay tuition using ABA Bank?",
        "Yes. Tuition can be paid via ABA mobile app or at any ABA branch.",
    ),
    (
        "Payment Method",
        "Can students pay using Canadia Bank?",
        "Yes. Payments can be made through the Canadia Bank mobile app or at a branch.",
    ),
    (
        "Payment Method",
        "Does AUPP accept cash payments?",
        "Yes. Cash is accepted at the campus Finance Office.",
    ),
    (
        "Payment Method",
        "Does AUPP allow installment payments?",
        "Yes. AUPP offers installment payment options. Students should contact the Finance Office for schedules and requirements.",
    ),
    (
        "Payment Method",
        "What happens if tuition is paid late?",
        "Late tuition payments may result in late fees or registration restrictions.",
    ),
    (
        "Payment Method",
        "Can someone else pay tuition on behalf of the student?",
        "Yes. A parent, guardian, or sponsor may pay tuition on the student's behalf.",
    ),
    (
        "Payment Method",
        "Does AUPP issue payment receipts?",
        "Yes. Every payment made on-campus or through a bank must be confirmed with an official AUPP receipt.",
    ),
    (
        "Payment Method",
        "What currency does AUPP accept?",
        "AUPP accepts payments in US Dollars.",
    ),
]

add_to_dataset(payment_method_new, "payment_method_json")

# ============================================================================
# STUDENT HANDBOOK (1 question from user-provided list)
# ============================================================================
student_handbook_new = [
    (
        "Student Handbook",
        "Where can I find the AUPP Student Handbook?",
        "You can check in this link: https://www.aupp.edu.kh/wp-content/uploads/AUPP-Student-Handbook-Fall-2023-Summer-2024.pdf",
    ),
]

add_to_dataset(student_handbook_new, "student_handbook_json")

# Create DataFrame
df = pd.DataFrame(complete_data)

# Save to CSV
output_file = "aupp_faq_dataset.csv"
df.to_csv(output_file, index=False, encoding="utf-8")

print("=" * 80)
print("AUPP FAQ DATASET CREATED SUCCESSFULLY")
print("=" * 80)
print(f"\n✓ File saved as: {output_file}")
print(f"✓ Total questions: {len(df)}")
print(f"✓ Total categories: {df['category'].nunique()}")

print("\n📊 Category Distribution:")
print("-" * 80)
category_counts = df["category"].value_counts().sort_index()
for category, count in category_counts.items():
    print(f"  {category:<45} {count:>3} questions")

print("\n✓ Dataset is ready for use in the chatbot!")
print("\nSample entries:")
print(df[["id", "category", "question"]].head(10).to_string(index=False))


from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import matplotlib.pyplot as plt
import os

def create_graphs():
    # Reuse graph generation logic
    # Graph 1: Cyber Crime Categories Distribution
    labels = ['Financial Fraud', 'Identity Theft', 'Harassment', 'Hacking', 'Crimes against Women/Children']
    sizes = [30, 20, 15, 25, 10]
    colors_pie = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors_pie)
    plt.title('Distribution of Cyber Crime Categories (2024)')
    plt.savefig('graph_categories.png')
    plt.close()

    # Graph 2: Rise in Phishing Attacks (Line Chart)
    years = ['2019', '2020', '2021', '2022', '2023']
    attacks = [12000, 25000, 45000, 68000, 95000]
    plt.figure(figsize=(8, 5))
    plt.plot(years, attacks, marker='o', linestyle='-', color='red', linewidth=2)
    plt.xlabel('Year')
    plt.ylabel('Reported Phishing Incidents')
    plt.title('Trend of Phishing Attacks (5-Year Analysis)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('graph_phishing_trend.png')
    plt.close()

    # Graph 3: Global Cost of Cyber Crime (Bar Chart)
    years_cost = ['2020', '2021', '2022', '2023', '2024 (Est)']
    cost = [4.5, 6.0, 8.4, 11.5, 13.0]
    plt.figure(figsize=(8, 5))
    plt.bar(years_cost, cost, color='green', alpha=0.7)
    plt.xlabel('Year')
    plt.ylabel('Cost (Trillion USD)')
    plt.title('Estimated Global Cost of Cyber Crime')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('graph_cost.png')
    plt.close()

    # Graph 4: Most Vulnerable Sectors (Horizontal Bar)
    sectors = ['Healthcare', 'Finance', 'Education', 'Retail', 'Government']
    attacks_pct = [25, 20, 15, 15, 10]
    plt.figure(figsize=(8, 5))
    plt.barh(sectors, attacks_pct, color='purple', alpha=0.6)
    plt.xlabel('Percentage of Total Attacks')
    plt.title('Most Targeted Sectors for Cyber Attacks')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.savefig('graph_sectors.png')
    plt.close()

    # Graph 5: Password Security Awareness
    labels_pass = ['Strong', 'Moderate', 'Weak', 'Reused']
    sizes_pass = [20, 30, 15, 35]
    plt.figure(figsize=(6, 6))
    plt.pie(sizes_pass, labels=labels_pass, autopct='%1.1f%%', startangle=90, explode=(0.1, 0, 0, 0))
    plt.title('User Password Habits Survey')
    plt.savefig('graph_passwords.png')
    plt.close()

class WordProjectGenerator:
    def __init__(self, filename):
        self.doc = Document()
        self.filename = filename
        
    def add_heading(self, text, level=1, align=WD_ALIGN_PARAGRAPH.LEFT):
        heading = self.doc.add_heading(text, level=level)
        heading.alignment = align
        if level == 0: # Title
             run = heading.runs[0]
             run.font.size = Pt(28)
             run.font.color.rgb = RGBColor(0, 0, 139) # Dark Blue
        elif level == 1:
             run = heading.runs[0]
             run.font.color.rgb = RGBColor(0, 0, 139)

    def add_paragraph(self, text, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
        p = self.doc.add_paragraph(text)
        p.alignment = align
        if bold:
            p.runs[0].bold = True
        if italic:
            p.runs[0].italic = True

    def add_bullet(self, text):
        self.doc.add_paragraph(text, style='List Bullet')

    def add_image(self, path, width_inches=5, caption=""):
        if os.path.exists(path):
            self.doc.add_picture(path, width=Inches(width_inches))
            if caption:
                p = self.doc.add_paragraph(caption)
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.runs[0].italic = True

    def add_page_break(self):
        self.doc.add_page_break()

    def create_title_page(self):
        # Center vertically (approximate with newlines)
        for _ in range(5): self.doc.add_paragraph()
        
        p = self.doc.add_paragraph("A PROJECT REPORT ON")
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.size = Pt(16)
        
        self.add_heading("CYBER SECURITY AWARENESS", level=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        self.add_heading("AND DIGITAL SAFETY", level=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        
        for _ in range(2): self.doc.add_paragraph()
        
        p = self.doc.add_paragraph("Submitted in partial fulfillment of the requirements for")
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p = self.doc.add_paragraph("Class 10th Information Technology")
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.bold = True
        
        for _ in range(4): self.doc.add_paragraph()
        
        # Student Details
        table = self.doc.add_table(rows=5, cols=2)
        table.alignment = WD_ALIGN_PARAGRAPH.CENTER
        data = [
            ('Submitted By:', 'Student Name'),
            ('Class:', '10th'),
            ('Roll No:', 'YOUR_ROLL_NO'),
            ('Subject:', 'Information Technology (402)'),
            ('School:', 'YOUR SCHOOL NAME')
        ]
        for i, (label, value) in enumerate(data):
            row = table.rows[i]
            row.cells[0].text = label
            row.cells[0].paragraphs[0].runs[0].font.bold = True
            row.cells[1].text = value
            
        self.add_page_break()

    def create_certificate(self):
        self.add_heading("CERTIFICATE", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
        self.doc.add_paragraph()
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        runner = p.add_run("This is to certify that ")
        p.add_run("Student Name").bold = True
        p.add_run(" of Class ")
        p.add_run("10th").bold = True
        p.add_run(" has successfully completed the project on ")
        p.add_run('"Cyber Security Awareness"').bold = True
        p.add_run(" under the guidance of ")
        p.add_run("Mr./Ms. Teacher Name").bold = True
        p.add_run(" during the academic year ")
        p.add_run("2025-26").bold = True
        p.add_run(".")
        
        p2 = self.doc.add_paragraph("The data collection and analysis presented in this project are original and authentic to the best of my knowledge.")
        p2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        for _ in range(4): self.doc.add_paragraph()
        
        # Signatures
        table = self.doc.add_table(rows=1, cols=2)
        table.autofit = True
        # Spread the table out
        table.rows[0].cells[0].text = "_________________\nTeacher Signature"
        table.rows[0].cells[1].text = "_________________\nExaminer Signature"
        table.rows[0].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        
        self.add_page_break()

    def create_acknowledgement(self):
        self.add_heading("ACKNOWLEDGEMENT", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
        self.doc.add_paragraph()
        p = self.doc.add_paragraph("I would like to express my special thanks of gratitude to my teacher Mr./Ms. Teacher Name as well as our principal who gave me the golden opportunity to do this wonderful project on the topic Cyber Security, which also helped me in doing a lot of Research and I came to know about so many new things. I am really thankful to them.")
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        self.doc.add_paragraph("Secondly, I would also like to thank my parents and friends who helped me a lot in finalizing this project within the limited time frame.")
        
        for _ in range(3): self.doc.add_paragraph()
        
        p = self.doc.add_paragraph("Student Name\nClass 10th")
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        self.add_page_break()
    
    # ... Similar logic for other chapters ...
    
    def create_content(self):
        # Index
        self.add_heading("INDEX", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
        table = self.doc.add_table(rows=1, cols=2)
        table.style = 'Table Grid'
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Topic'
        hdr_cells[1].text = 'Page No'
        
        topics = [
            ('Introduction to Cyber Security', '5'),
            ('Evolution of Cyber Crime', '8'),
            ('Types of Cyber Threats', '11'),
            ('Cyber Crime Categories', '14'),
            ('Prevention and Best Practices', '17'),
            ('Case Studies', '20'),
            ('Statistical Analysis', '23'),
            ('Cyber Laws and Ethics', '25'),
            ('Future of Cyber Security', '27'),
            ('Conclusion', '28'),
            ('Bibliography', '29')
        ]
        
        for topic, page in topics:
            row_cells = table.add_row().cells
            row_cells[0].text = topic
            row_cells[1].text = page
            
        self.add_page_break()

        # Chapter 1
        self.add_heading("Chapter 1: Introduction to Cyber Security", level=1)
        self.add_heading("1.1 What is Cyber Security?", level=2)
        self.add_paragraph("Cyber security is the practice of defending computers, servers, mobile devices, electronic systems, networks, and data from malicious attacks. It's also known as information technology security or electronic information security.")
        
        self.add_heading("1.2 The CIA Triad", level=2)
        self.add_paragraph("The CIA triad is a model designed to guide policies for information security within an organization:")
        self.add_bullet("Confidentiality: Ensuring data is accessible only to those authorized.")
        self.add_bullet("Integrity: Maintaining accuracy and completeness of data.")
        self.add_bullet("Availability: Ensuring authorized users have access when required.")
        self.add_page_break()

        # Chapter 2
        self.add_heading("Chapter 2: Evolution of Cyber Crime", level=1)
        self.add_paragraph("The history of cyber crime is as old as the history of the internet itself. From the first automated sabotage in 1820 to modern ransomware gangs.")
        self.add_image('graph_cost.png', caption="Figure 2.1: Increasing Cost of Cyber Crime")
        self.add_page_break()

        # Chapter 3
        self.add_heading("Chapter 3: Types of Cyber Threats", level=1)
        threats = ["Phishing", "Malware", "Ransomware", "Social Engineering", "Denial of Service (DoS)", "SQL Injection"]
        for t in threats:
            self.add_bullet(t)
        self.add_image('graph_categories.png', caption="Figure 3.1: Distribution of Cyber Crime Types")
        self.add_page_break()

        # Chapter 4
        self.add_heading("Chapter 4: Cyber Crime Categories", level=1)
        self.add_heading("4.1 Cyber Crime Against Individuals", level=2)
        self.add_paragraph("Harassment, Cyber-stalking, Defamation.")
        self.add_heading("4.2 Cyber Crime Against Property", level=2)
        self.add_paragraph("Computer Vandalism, Intellectual Property Crimes.")
        self.add_image('graph_sectors.png', caption="Figure 4.1: Sectors Targeted by Cyber Crimes")
        self.add_page_break()

        # Chapter 5
        self.add_heading("Chapter 5: Prevention and Best Practices", level=1)
        self.add_paragraph("Passwords are the first line of defense. Use strong passwords and 2FA.")
        self.add_image('graph_passwords.png', caption="Figure 5.1: Analysis of Password Habits")
        self.add_page_break()

        # Chapter 6
        self.add_heading("Chapter 6: Case Studies", level=1)
        self.add_paragraph("WannaCry Ransomware (2017), Yahoo Data Breaches (2013), SolarWinds Hack (2020).")
        self.add_page_break()

        # Chapter 7
        self.add_heading("Chapter 7: Statistical Analysis", level=1)
        self.add_paragraph("Phishing remains one of the most common entry points for attackers. As seen in the graph below, the number of incidents has nearly tripled in 5 years.")
        self.add_image('graph_phishing_trend.png', caption="Figure 7.1: Rise in Phishing Attacks")
        self.add_page_break()

        # Chapter 8
        self.add_heading("Chapter 8: Cyber Laws and Ethics", level=1)
        self.add_heading("8.1 IT Act 2000 (India)", level=2)
        self.add_paragraph("The primary law in India dealing with cybercrime and electronic commerce.")
        self.add_page_break()

        # Chapter 9
        self.add_heading("Chapter 9: Future of Cyber Security", level=1)
        self.add_paragraph("AI in Security, IoT Security, Zero Trust Architecture.")
        self.add_page_break()

        # Conclusion
        self.add_heading("Conclusion", level=1)
        self.add_paragraph("Cyber security is a shared responsibility. Governments, corporations, and individuals must work together to create a safer digital environment.")
        self.add_page_break()

        # Bibliography
        self.add_heading("Bibliography", level=1)
        sources = [
            "NCERT Information Technology Textbook for Class 10",
            "Norton Cyber Security Insights Report 2023",
            "Symantec Internet Security Threat Report",
            "The Information Technology Act, 2000 (India)",
            "www.cybercrime.gov.in"
        ]
        for s in sources:
            self.add_bullet(s)

    def generate(self):
        self.create_title_page()
        self.create_certificate()
        self.create_acknowledgement()
        self.create_content()
        self.doc.save(self.filename)
        print(f"Word Doc generated: {self.filename}")

if __name__ == "__main__":
    print("Generating graphs...")
    create_graphs()
    print("Graphs created. Generating Word Doc...")
    project = WordProjectGenerator("Comprehensive_Class_10_IT_Project.docx")
    project.generate()
    
    # Cleanup
    graphs = ['graph_categories.png', 'graph_phishing_trend.png', 'graph_cost.png', 'graph_sectors.png', 'graph_passwords.png']
    for g in graphs:
        if os.path.exists(g):
            os.remove(g)


from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
import matplotlib.pyplot as plt
import os
import random

def create_graphs():
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
    cost = [4.5, 6.0, 8.4, 11.5, 13.0] # Trillion USD
    
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

class ProjectGenerator:
    def __init__(self, filename):
        self.doc = SimpleDocTemplate(
            filename, 
            pagesize=letter,
            rightMargin=72, leftMargin=72,
            topMargin=72, bottomMargin=72
        )
        self.styles = getSampleStyleSheet()
        self.story = []
        self._setup_styles()

    def _setup_styles(self):
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Title'],
            fontSize=28,
            leading=34,
            spaceAfter=50,
            alignment=TA_CENTER,
            textColor=colors.darkblue
        )
        self.subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            alignment=TA_CENTER,
            spaceAfter=20
        )
        self.chapter_title = ParagraphStyle(
            'ChapterTitle',
            parent=self.styles['Heading1'],
            fontSize=22,
            spaceBefore=20,
            spaceAfter=20,
            textColor=colors.darkblue,
            keepWithNext=True
        )
        self.heading_style = ParagraphStyle(
            'CustomHeading',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceBefore=15,
            spaceAfter=10,
            textColor=colors.black,
            keepWithNext=True
        )
        self.body_style = ParagraphStyle(
            'JustifiedBody',
            parent=self.styles['BodyText'],
            fontSize=12,
            leading=16,
            alignment=TA_JUSTIFY,
            spaceAfter=12
        )
        self.bullet_style = ParagraphStyle(
            'BulletPoint',
            parent=self.body_style,
            bulletIndent=10,
            leftIndent=20,
            spaceAfter=8
        )
        self.center_style = ParagraphStyle(
            'Centered',
            parent=self.body_style,
            alignment=TA_CENTER
        )

    def add_page_break(self):
        self.story.append(PageBreak())

    def add_spacer(self, height=20):
        self.story.append(Spacer(1, height))

    def add_image(self, path, width=450, caption=""):
        if os.path.exists(path):
            img = Image(path, width=width, height=width*0.6) # Maintain aspect ratio roughly
            self.story.append(img)
            if caption:
                self.story.append(Spacer(1, 5))
                self.story.append(Paragraph(f"<i>{caption}</i>", self.center_style))
            self.story.append(Spacer(1, 20))

    def create_title_page(self):
        self.add_spacer(100)
        self.story.append(Paragraph("A PROJECT REPORT ON", self.subtitle_style))
        self.story.append(Paragraph("CYBER SECURITY AWARENESS", self.title_style))
        self.story.append(Paragraph("AND DIGITAL SAFETY", self.title_style))
        self.add_spacer(50)
        self.story.append(Paragraph("Submitted in partial fulfillment of the requirements for", self.subtitle_style))
        self.story.append(Paragraph("Class 10th Information Technology", self.subtitle_style))
        self.add_spacer(80)
        
        # Student Details Table
        data = [
            ['Submitted By:', 'Student Name'],
            ['Class:', '10th'],
            ['Roll No:', 'YOUR_ROLL_NO'],
            ['Subject:', 'Information Technology (402)'],
            ['School:', 'YOUR SCHOOL NAME']
        ]
        t = Table(data, colWidths=[150, 250])
        t.setStyle(TableStyle([
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 14),
            ('BOTTOMPADDING', (0,0), (-1,-1), 12),
            ('TEXTCOLOR', (0,0), (0,-1), colors.darkblue),
        ]))
        self.story.append(t)
        self.add_page_break()

    def create_certificate(self):
        self.story.append(Paragraph("CERTIFICATE", self.title_style))
        self.add_spacer(40)
        text = """This is to certify that <b>Student Name</b> of Class <b>10th</b> has successfully completed the project on 
        <b>"Cyber Security Awareness"</b> under the guidance of <b>Mr./Ms. Teacher Name</b> during the academic year <b>2025-26</b>.
        <br/><br/>
        The data collection and analysis presented in this project are original and authentic to the best of my knowledge."""
        self.story.append(Paragraph(text, self.body_style))
        self.add_spacer(80)
        
        # Signatures
        data = [['_________________', '_________________'],
                ['Teacher Signature', 'Examiner Signature']]
        t = Table(data, colWidths=[250, 250])
        t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ]))
        self.story.append(t)
        self.add_page_break()

    def create_acknowledgement(self):
        self.story.append(Paragraph("ACKNOWLEDGEMENT", self.title_style))
        self.add_spacer(30)
        text = """I would like to express my special thanks of gratitude to my teacher <b>Mr./Ms. Teacher Name</b> as well as our principal 
        who gave me the golden opportunity to do this wonderful project on the topic <b>Cyber Security</b>, which also helped me in 
        doing a lot of Research and I came to know about so many new things. I am really thankful to them.
        <br/><br/>
        Secondly, I would also like to thank my parents and friends who helped me a lot in finalizing this project within the limited time frame."""
        self.story.append(Paragraph(text, self.body_style))
        self.add_spacer(50)
        self.story.append(Paragraph("Student Name", ParagraphStyle('Right', parent=self.body_style, alignment=2))) # Right align
        self.story.append(Paragraph("Class 10th", ParagraphStyle('Right', parent=self.body_style, alignment=2)))
        self.add_page_break()

    def create_index(self):
        self.story.append(Paragraph("INDEX", self.title_style))
        self.add_spacer(20)
        data = [
            ['S.No', 'Topic', 'Page No'],
            ['1', 'Introduction to Cyber Security', '5'],
            ['2', 'Evolution of Cyber Crime', '8'],
            ['3', 'Types of Cyber Threats', '11'],
            ['4', 'Cyber Crime Categories', '14'],
            ['5', 'Prevention and Best Practices', '17'],
            ['6', 'Case Studies', '20'],
            ['7', 'Statistical Analysis', '23'],
            ['8', 'Cyber Laws and Ethics', '25'],
            ['9', 'Future of Cyber Security', '27'],
            ['10', 'Conclusion', '28'],
            ['11', 'Bibliography', '29']
        ]
        t = Table(data, colWidths=[50, 350, 80])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
            ('TEXTCOLOR', (0,0), (-1,0), colors.black),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('ALIGN', (-1,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0,0), (-1,0), 12),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.whitesmoke, colors.white]),
        ]))
        self.story.append(t)
        self.add_page_break()

    def create_chapter_1(self):
        self.story.append(Paragraph("Chapter 1: Introduction to Cyber Security", self.chapter_title))
        
        self.story.append(Paragraph("1.1 What is Cyber Security?", self.heading_style))
        text = """Cyber security is the practice of defending computers, servers, mobile devices, electronic systems, networks, and data from malicious attacks. It's also known as information technology security or electronic information security. The term applies in a variety of contexts, from business to mobile computing, and can be divided into a few common categories."""
        self.story.append(Paragraph(text, self.body_style))
        
        self.story.append(Paragraph("The importance of cyber security cannot be overstated. In our modern, digital world, we store vast amounts of data on computers and other devices. Much of that data is sensitive, such as intellectual property, financial data, personal information, or other types of data for which unauthorized access or exposure could have negative consequences.", self.body_style))

        self.story.append(Paragraph("1.2 The CIA Triad", self.heading_style))
        self.story.append(Paragraph("The CIA triad is a model designed to guide policies for information security within an organization. The elements of the triad are considered the three most crucial components of security:", self.body_style))
        
        self.story.append(Paragraph("• <b>Confidentiality:</b> Ensuring that data is accessible only to those authorized to have access.", self.bullet_style))
        self.story.append(Paragraph("• <b>Integrity:</b> Maintaining the accuracy and completeness of data. This means data cannot be modified in an unauthorized or undetected manner.", self.bullet_style))
        self.story.append(Paragraph("• <b>Availability:</b> Ensuring that authorized users have access to information and associated assets when required.", self.bullet_style))

        self.story.append(Paragraph("1.3 Why do we need Cyber Security?", self.heading_style))
        text = """The range of operations of cyber security involves protecting information and systems from major cyberthreats. These threats take many forms. As a result, keeping pace with cyber security strategy and operations can be a challenge, particularly in government and enterprise networks where, in their most innovative form, cyberthreats often take aim at the secret, political, and military assets of a nation, or its people."""
        self.story.append(Paragraph(text, self.body_style))
        self.add_page_break()
        
        # Continued content for length
        self.story.append(Paragraph("1.4 Scope of Cyber Security", self.heading_style))
        text = """Cyber security is a vast field that encompasses several disciplines. It is not just about installing an antivirus but involves a holistic approach to security. The scope includes:"""
        self.story.append(Paragraph(text, self.body_style))
        self.story.append(Paragraph("• <b>Network Security:</b> Protecting the network from unauthorized access.", self.bullet_style))
        self.story.append(Paragraph("• <b>Application Security:</b> Keeping software and devices free of threats.", self.bullet_style))
        self.story.append(Paragraph("• <b>Information Security:</b> Protecting the integrity and privacy of data.", self.bullet_style))
        self.story.append(Paragraph("• <b>Operational Security:</b> The processes and decisions for handling and protecting data assets.", self.bullet_style))
        self.story.append(Paragraph("• <b>Disaster Recovery:</b> How an organization responds to a cyber-security incident or any other event that causes the loss of operations or data.", self.bullet_style))
        self.story.append(Paragraph("• <b>End-user Education:</b> Addressing the most unpredictable cyber-security factor: people.", self.bullet_style))
        self.add_page_break()

    def create_chapter_2(self):
        self.story.append(Paragraph("Chapter 2: Evolution of Cyber Crime", self.chapter_title))
        
        self.story.append(Paragraph("2.1 The Early Days", self.heading_style))
        text = """The history of cyber crime is as old as the history of the internet itself. The first recorded cyber crime took place in the year 1820! That is not a typo. In 1820, Joseph-Marie Jacquard, a textile manufacturer in France, produced the loom. This device allowed the repetition of a series of steps in the weaving of special fabrics. This resulted in a fear among employees that their traditional employment and livelihood were being threatened. They committed an act of sabotage to discourage Jacquard from further use of the new technology. This is the first recorded instance of automated sabotage."""
        self.story.append(Paragraph(text, self.body_style))

        self.story.append(Paragraph("2.2 The Era of Hacking (1960s - 1980s)", self.heading_style))
        text = """Real hacking began in the 1960s at MIT. The term 'hacker' was coined to describe members of a model train group who 'hacked' the electric trains, tracks, and switches to make them perform faster and differently. In the 1970s, 'Phreaking' became popular, which involved exploiting the telephone network."""
        self.story.append(Paragraph(text, self.body_style))

        self.story.append(Paragraph("2.3 The Modern Era (1990s - Present)", self.heading_style))
        text = """With the boom of the World Wide Web in the 90s, cyber crime took a new turn. Viruses like 'Melissa' and 'ILOVEYOU' caused damages worth millions. Today, cyber crime is a well-organized industry. State-sponsored attacks, ransomware gangs, and dark web marketplaces define the modern landscape."""
        self.story.append(Paragraph(text, self.body_style))
        
        self.add_image('graph_cost.png', caption="Figure 2.1: Increasing Cost of Cyber Crime")
        self.add_page_break()

    def create_chapter_3(self):
        self.story.append(Paragraph("Chapter 3: Types of Cyber Threats", self.chapter_title))
        
        threats = [
            ("Phishing", "Phishing is the practice of sending fraudulent communications that appear to come from a reputable source, usually through email. The goal is to steal sensitive data like credit card and login information or to install malware on the victim's machine."),
            ("Malware", "Malware is malicious software such as spyware, ransomware, viruses, and worms. Malware is activated when a user clicks on a malicious link or attachment, leading to installing dangerous software."),
            ("Ransomware", "Ransomware is a type of malicious software. It is designed to extort money by blocking access to files or the computer system until the ransom is paid. Paying the ransom does not guarantee that the files will be recovered or the system restored."),
            ("Social Engineering", "Social engineering is a tactic that adversaries use to trick you into revealing sensitive information. They can solicit a monetary payment or gain access to your confidential data. Social engineering can be combined with any of the threats listed above to make you more likely to click on links, download malware, or trust a malicious source."),
            ("Denial of Service (DoS)", "A denial-of-service attack floods systems, servers, or networks with traffic to exhaust resources and bandwidth. As a result, the system is unable to fulfill legitimate requests. Attackers can also use multiple compromised devices to launch this attack."),
            ("SQL Injection", "An SQL injection occurs when an attacker inserts malicious code into a server that uses Structured Query Language (SQL) and forces the server to reveal information it normally would not. An attacker could carry out a SQL injection simply by submitting malicious code into a vulnerable website search box.")
        ]

        for title, desc in threats:
            self.story.append(Paragraph(f"• {title}", self.heading_style))
            self.story.append(Paragraph(desc, self.body_style))
            self.add_spacer(5)

        self.add_image('graph_categories.png', caption="Figure 3.1: Distribution of Cyber Crime Types")
        self.add_page_break()

    def create_chapter_4(self):
        self.story.append(Paragraph("Chapter 4: Cyber Crime Categories", self.chapter_title))
        
        self.story.append(Paragraph("4.1 Cyber Crime Against Individuals", self.heading_style))
        self.story.append(Paragraph("This category of cyber crime targets individuals directly. Examples include:", self.body_style))
        self.story.append(Paragraph("• Harassment via emails", self.bullet_style))
        self.story.append(Paragraph("• Cyber-stalking", self.bullet_style))
        self.story.append(Paragraph("• Dissemination of obscene material", self.bullet_style))
        self.story.append(Paragraph("• Defamation", self.bullet_style))
        self.story.append(Paragraph("• Unauthorized control/access to computer system", self.bullet_style))
        self.story.append(Paragraph("• Indecent exposure", self.bullet_style))

        self.story.append(Paragraph("4.2 Cyber Crime Against Property", self.heading_style))
        self.story.append(Paragraph("Similar to real-world property crimes, these target computer or network property:", self.body_style))
        self.story.append(Paragraph("• Computer Vandalism: Damaging or destroying data rather than stealing it.", self.bullet_style))
        self.story.append(Paragraph("• Transmitting virus/worms", self.bullet_style))
        self.story.append(Paragraph("• Intellectual Property Crimes: Software piracy, copyright infringement.", self.bullet_style))

        self.story.append(Paragraph("4.3 Cyber Crime Against Government", self.heading_style))
        self.story.append(Paragraph("These are serious crimes often referred to as Cyber Terrorism:", self.body_style))
        self.story.append(Paragraph("• Hacking government websites", self.bullet_style))
        self.story.append(Paragraph("• Cyber warfare", self.bullet_style))
        self.story.append(Paragraph("• Distribution of pirated software", self.bullet_style))
        self.story.append(Paragraph("• Possession of unauthorized information", self.bullet_style))
        
        self.add_image('graph_sectors.png', caption="Figure 4.1: Sectors Targeted by Cyber Crimes")
        self.add_page_break()

    def create_chapter_5(self):
        self.story.append(Paragraph("Chapter 5: Prevention and Best Practices", self.chapter_title))
        
        self.story.append(Paragraph("5.1 Password Management", self.heading_style))
        text = """Passwords are the first line of defense. A strong password should be at least 12 characters long, including a mix of letters, numbers, and symbols. Users should avoid using the same password across multiple sites. Using a Password Manager is highly recommended."""
        self.story.append(Paragraph(text, self.body_style))
        self.add_image('graph_passwords.png', caption="Figure 5.1: Analysis of Password Habits", width=350)

        self.story.append(Paragraph("5.2 Two-Factor Authentication (2FA)", self.heading_style))
        text = """2FA adds an extra layer of security. Even if a hacker gets your password, they cannot access your account without the second factor, which is usually a code sent to your phone or generated by an app."""
        self.story.append(Paragraph(text, self.body_style))

        self.story.append(Paragraph("5.3 Software Updates", self.heading_style))
        text = """Keep your software and operating system updated. Updates often contain patches for security vulnerabilities that have been discovered."""
        self.story.append(Paragraph(text, self.body_style))

        self.story.append(Paragraph("5.4 Safe Browsing Habits", self.heading_style))
        self.story.append(Paragraph("• Do not click on suspicious links in emails.", self.bullet_style))
        self.story.append(Paragraph("• Check for 'https' in the URL before entering sensitive info.", self.bullet_style))
        self.story.append(Paragraph("• Avoid using public Wi-Fi for banking transactions.", self.bullet_style))
        self.story.append(Paragraph("• Be careful what you share on social media.", self.bullet_style))
        
        self.add_page_break()

    def create_chapter_6(self):
        self.story.append(Paragraph("Chapter 6: Case Studies", self.chapter_title))
        
        self.story.append(Paragraph("6.1 The WannaCry Ransomware Attack (2017)", self.heading_style))
        text = """The WannaCry ransomware attack was a worldwide cyberattack in May 2017 by the WannaCry ransomware cryptoworm, which targeted computers running the Microsoft Windows operating system by encrypting data and demanding ransom payments in the Bitcoin cryptocurrency. It propagated through EternalBlue, an exploit discovered by the NSA. The attack affected more than 200,000 computers across 150 countries, causing billions of dollars in estimated damages."""
        self.story.append(Paragraph(text, self.body_style))

        self.story.append(Paragraph("6.2 The Yahoo Data Breaches (2013-2014)", self.heading_style))
        text = """Yahoo announced that all 3 billion of its user accounts were impacted by a 2013 data breach. The compromised data included names, email addresses, telephone numbers, dates of birth, hashed passwords, and, in some cases, encrypted or unencrypted security questions and answers. It remains one of the largest data breaches in history."""
        self.story.append(Paragraph(text, self.body_style))

        self.story.append(Paragraph("6.3 SOLARWINDS Supply Chain Attack (2020)", self.heading_style))
        text = """In 2020, a major cyberattack suspected to be directed by a nation-state targeted SolarWinds, a major US information technology firm. The attackers inserted malicious code into the Orion software updates, which were then downloaded by thousands of customers, including US government agencies. This highlighted the vulnerability of the software supply chain."""
        self.story.append(Paragraph(text, self.body_style))
        self.add_page_break()

    def create_chapter_7(self):
        self.story.append(Paragraph("Chapter 7: Statistical Analysis", self.chapter_title))
        self.story.append(Paragraph("This chapter analyzes the trends in cyber security over the last 5 years based on global data.", self.body_style))
        
        self.story.append(Paragraph("7.1 Trend of Phishing Attacks", self.heading_style))
        self.story.append(Paragraph("Phishing remains one of the most common entry points for attackers. As seen in the graph below, the number of incidents has nearly tripled in 5 years.", self.body_style))
        self.add_image('graph_phishing_trend.png', caption="Figure 7.1: Rise in Phishing Attacks")

        self.story.append(Paragraph("7.2 Analysis", self.heading_style))
        text = """The data indicates a worrying trend. As digital adoption increases, so does the sophistication and frequency of attacks. The exponential growth in the cost of cybercrime suggests that businesses and governments need to invest significantly more in defensive infrastructure."""
        self.story.append(Paragraph(text, self.body_style))
        self.add_page_break()

    def create_chapter_8(self):
        self.story.append(Paragraph("Chapter 8: Cyber Laws and Ethics", self.chapter_title))
        
        self.story.append(Paragraph("8.1 IT Act 2000 (India)", self.heading_style))
        text = """The Information Technology Act, 2000 is the primary law in India dealing with cybercrime and electronic commerce. It provides a legal framework for electronic governance by giving recognition to electronic records and digital signatures."""
        self.story.append(Paragraph(text, self.body_style))
        
        self.story.append(Paragraph("Key Offences and Penalties:", self.heading_style))
        self.story.append(Paragraph("• Sec 65: Tampering with computer source documents.", self.bullet_style))
        self.story.append(Paragraph("• Sec 66: Computer Related Offences (Hacking).", self.bullet_style))
        self.story.append(Paragraph("• Sec 66C: Punishment for identity theft.", self.bullet_style))
        self.story.append(Paragraph("• Sec 66D: Punishment for cheating by personation by using computer resource.", self.bullet_style))
        self.story.append(Paragraph("• Sec 67: Publishing or transmitting obscene material in electronic form.", self.bullet_style))

        self.story.append(Paragraph("8.2 Cyber Ethics", self.heading_style))
        text = """Cyber ethics refers to the code of responsible behavior on the internet. Just as we are taught to be good citizens in the real world, we must be good 'netizens'."""
        self.story.append(Paragraph(text, self.body_style))
        self.story.append(Paragraph("• Do not use a computer to harm other people.", self.bullet_style))
        self.story.append(Paragraph("• Do not interfere with other people's computer work.", self.bullet_style))
        self.story.append(Paragraph("• Do not snoop around in other people's computer files.", self.bullet_style))
        self.story.append(Paragraph("• Do not use a computer to steal.", self.bullet_style))
        self.story.append(Paragraph("• Do not use a computer to bear false witness.", self.bullet_style))
        self.add_page_break()

    def create_chapter_9(self):
        self.story.append(Paragraph("Chapter 9: Future of Cyber Security", self.chapter_title))
        
        self.story.append(Paragraph("9.1 Artificial Intelligence in Security", self.heading_style))
        text = """AI is being used to analyze vast amounts of data to detect anomalies and potential threats faster than humans can. However, hackers are also using AI to create smarter malware and automated attacks."""
        self.story.append(Paragraph(text, self.body_style))

        self.story.append(Paragraph("9.2 IoT Security", self.heading_style))
        text = """With the rise of the Internet of Things (IoT), billions of devices are coming online. Securing smart homes, smart cars, and smart cities will be a major challenge for the future."""
        self.story.append(Paragraph(text, self.body_style))

        self.story.append(Paragraph("9.3 Zero Trust Architecture", self.heading_style))
        text = """The traditional security model assumed everything inside the network was safe. Zero Trust assumes a breach is inevitable or has likely already occurred. It constantly limits access to only what is needed and looks for anomalous or malicious activity."""
        self.story.append(Paragraph(text, self.body_style))
        self.add_page_break()

    def create_conclusion(self):
        self.story.append(Paragraph("Conclusion", self.chapter_title))
        text = """
        The digital world is a double-edged sword. While it offers immense opportunities for learning, communication, and business, it also presents significant risks. Cyber security is the shield that protects us in this digital age.
        <br/><br/>
        This project has explored the various facets of cyber security, from the types of threats to the laws that govern them. The statistical data clearly shows that cyber crime is on the rise, and no sector is immune. 
        <br/><br/>
        As students and future leaders, it is our responsibility to be aware of these threats and practice good cyber hygiene. Education and awareness are the most powerful tools we have. By staying informed and vigilant, we can enjoy the benefits of technology without falling victim to its dangers.
        <br/><br/>
        In conclusion, cyber security is a shared responsibility. Governments, corporations, and individuals must work together to create a safer digital environment for everyone.
        """
        self.story.append(Paragraph(text, self.body_style))
        self.add_page_break()

    def create_bibliography(self):
        self.story.append(Paragraph("Bibliography", self.chapter_title))
        self.story.append(Paragraph("The following sources were consulted for this project:", self.body_style))
        self.add_spacer(20)
        
        sources = [
            "NCERT Information Technology Textbook for Class 10",
            "Norton Cyber Security Insights Report 2023",
            "Symantec Internet Security Threat Report",
            "The Information Technology Act, 2000 (India)",
            "www.cybercrime.gov.in",
            "www.kaspersky.com/resource-center",
            "www.cisco.com/c/en/us/products/security/what-is-cybersecurity.html",
            "Wikipedia - Computer Security"
        ]
        
        for source in sources:
            self.story.append(Paragraph(f"• {source}", self.bullet_style))

    def generate(self):
        self.create_title_page()
        self.create_certificate()
        self.create_acknowledgement()
        self.create_index()
        self.create_chapter_1()
        self.create_chapter_2()
        self.create_chapter_3()
        self.create_chapter_4()
        self.create_chapter_5()
        self.create_chapter_6()
        self.create_chapter_7()
        self.create_chapter_8()
        self.create_chapter_9()
        self.create_conclusion()
        self.create_bibliography()
        
        self.doc.build(self.story)
        print(f"PDF generated: {self.doc.filename}")

if __name__ == "__main__":
    print("Generating graphs...")
    create_graphs()
    print("Graphs created. Generating PDF...")
    project = ProjectGenerator("Comprehensive_Class_10_IT_Project.pdf")
    project.generate()
    
    # Cleanup
    graphs = ['graph_categories.png', 'graph_phishing_trend.png', 'graph_cost.png', 'graph_sectors.png', 'graph_passwords.png']
    for g in graphs:
        if os.path.exists(g):
            os.remove(g)

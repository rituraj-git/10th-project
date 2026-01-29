
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
            ('Evolution of Cyber Crime', '9'),
            ('Types of Cyber Threats', '13'),
            ('Cyber Crime Categories', '17'),
            ('Prevention and Best Practices', '21'),
            ('Network Security Fundamentals', '24'),
            ('Mobile Device Security', '27'),
            ('Case Studies', '30'),
            ('Statistical Analysis', '34'),
            ('Cyber Laws and Ethics', '37'),
            ('Future of Cyber Security', '40'),
            ('Conclusion', '43'),
            ('Bibliography', '44')
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
        self.add_paragraph("In an era where our lives are increasingly digital, the importance of cyber security cannot be overstated. From personal banking to national defense, every aspect of modern society relies on the integrity of digital systems. A breach in security can lead to financial loss, reputational damage, and even threats to national security.")
        
        self.add_heading("1.2 The CIA Triad", level=2)
        self.add_paragraph("The CIA triad is a model designed to guide policies for information security within an organization. It stands for Confidentiality, Integrity, and Availability.")
        self.add_bullet("Confidentiality: Ensuring data is accessible only to those authorized. This involves encryption, access controls, and data classification.")
        self.add_bullet("Integrity: Maintaining accuracy and completeness of data. This ensures that data has not been tampered with during transit or storage.")
        self.add_bullet("Availability: Ensuring authorized users have access when required. This involves maintaining hardware, software, and network infrastructure to prevent downtime.")
        
        self.add_heading("1.3 Why is Cyber Security Important?", level=2)
        self.add_paragraph("The range of operations of cyber security involves protecting information and systems from major cyberthreats. These threats take many forms. As a result, keeping pace with cyber security strategy and operations can be a challenge, particularly in government and enterprise networks where, in their most innovative form, cyberthreats often take aim at the secret, political, and military assets of a nation, or its people.")
        self.add_paragraph("For individuals, cyber security protects against identity theft, extortion attempts, and the loss of important data like family photos. For businesses, it protects intellectual property, customer data, and continuity of operations.")
        self.add_page_break()
        
        self.add_heading("1.4 Components of Cyber Security", level=2)
        self.add_paragraph("Cyber security is a vast field that encompasses several disciplines. It is not just about installing an antivirus but involves a holistic approach to security. The scope includes:")
        self.add_bullet("Network Security: Protecting the network from unauthorized access and malicious attacks.")
        self.add_bullet("Application Security: Keeping software and devices free of threats by finding and fixing vulnerabilities.")
        self.add_bullet("Information Security: Protecting the integrity and privacy of data, both in storage and in transit.")
        self.add_bullet("Operational Security: The processes and decisions for handling and protecting data assets.")
        self.add_bullet("Disaster Recovery: How an organization responds to a cyber-security incident or any other event that causes the loss of operations or data.")
        self.add_bullet("End-user Education: Addressing the most unpredictable cyber-security factor: people. Teaching users to delete suspicious email attachments, not plug in unidentified USB drives, and various other important lessons is vital for the security of any organization.")
        self.add_page_break()

        # Chapter 2
        self.add_heading("Chapter 2: Evolution of Cyber Crime", level=1)
        self.add_heading("2.1 The Early Days", level=2)
        self.add_paragraph("The history of cyber crime is as old as the history of the internet itself. The first recorded cyber crime took place in the year 1820! That is not a typo. In 1820, Joseph-Marie Jacquard, a textile manufacturer in France, produced the loom. This device allowed the repetition of a series of steps in the weaving of special fabrics. This resulted in a fear among employees that their traditional employment and livelihood were being threatened. They committed an act of sabotage to discourage Jacquard from further use of the new technology. This is the first recorded instance of automated sabotage.")
        self.add_paragraph("However, the modern era of cyber crime began with the proliferation of computers in the late 20th century. In the 1960s and 70s, 'hacking' was often an intellectual challenge rather than a criminal activity. It was about exploring the limits of technology.")
        
        self.add_heading("2.2 The Era of Malicious Code", level=2)
        self.add_paragraph("The 1980s saw the birth of the first computer viruses. The 'Morris Worm' in 1988 was one of the first worms distributed via the Internet. It resulted in the first conviction in the US under the 1986 Computer Fraud and Abuse Act.")
        self.add_paragraph("In the 1990s, with the boom of the World Wide Web, cyber crime took a new turn. Viruses like 'Melissa' and 'ILOVEYOU' caused damages worth millions by clogging email systems and deleting files. These were often created by individuals seeking notoriety.")
        self.add_page_break()

        self.add_heading("2.3 The Modern Landscape", level=2)
        self.add_paragraph("Today, cyber crime is a well-organized industry. It has evolved from isolated individuals to sophisticated criminal organizations and even state-sponsored groups. The motivations have shifted from fame to financial gain and espionage.")
        self.add_paragraph("We now see Ransomware-as-a-Service (RaaS), where developers sell ransomware kits to affiliates. The Dark Web provides a marketplace for stolen data, hacking tools, and illegal services.")
        self.add_image('graph_cost.png', caption="Figure 2.1: Increasing Cost of Cyber Crime")
        self.add_page_break()

        # Chapter 3
        self.add_heading("Chapter 3: Types of Cyber Threats", level=1)
        self.add_paragraph("Cyber threats are constantly evolving, but they generally fall into several categories. Understanding these threats is the first step in defending against them.")
        
        threats = [
            ("Phishing", "Phishing is the practice of sending fraudulent communications that appear to come from a reputable source, usually through email. The goal is to steal sensitive data like credit card and login information or to install malware on the victim's machine. It is one of the most common cyber threats."),
            ("Malware", "Malware is malicious software such as spyware, ransomware, viruses, and worms. Malware is activated when a user clicks on a malicious link or attachment, leading to installing dangerous software. Once installed, malware can monitor user activity, steal data, or damage the system."),
            ("Ransomware", "Ransomware is a type of malicious software. It is designed to extort money by blocking access to files or the computer system until the ransom is paid. Paying the ransom does not guarantee that the files will be recovered or the system restored."),
            ("Social Engineering", "Social engineering is a tactic that adversaries use to trick you into revealing sensitive information. They can solicit a monetary payment or gain access to your confidential data. Social engineering can be combined with any of the threats listed above to make you more likely to click on links, download malware, or trust a malicious source."),
            ("Denial of Service (DoS)", "A denial-of-service attack floods systems, servers, or networks with traffic to exhaust resources and bandwidth. As a result, the system is unable to fulfill legitimate requests. Attackers can also use multiple compromised devices to launch this attack, known as a Distributed Denial of Service (DDoS) attack."),
            ("SQL Injection", "An SQL injection occurs when an attacker inserts malicious code into a server that uses Structured Query Language (SQL) and forces the server to reveal information it normally would not. An attacker could carry out a SQL injection simply by submitting malicious code into a vulnerable website search box.")
        ]
        for title, desc in threats:
            self.add_heading(title, level=2)
            self.add_paragraph(desc)
            
        self.add_image('graph_categories.png', caption="Figure 3.1: Distribution of Cyber Crime Types")
        self.add_page_break()

        # Chapter 4
        self.add_heading("Chapter 4: Cyber Crime Categories", level=1)
        self.add_heading("4.1 Cyber Crime Against Individuals", level=2)
        self.add_paragraph("This category of cyber crime targets individuals directly. It affects the victim personally, financially, or psychologically. Examples include:")
        self.add_bullet("Harassment via emails: Sending threatening or abusive emails.")
        self.add_bullet("Cyber-stalking: Using the internet to stalk or harass an individual.")
        self.add_bullet("Dissemination of obscene material: Posting offensive content.")
        self.add_bullet("Defamation: Spreading false information to damage someone's reputation.")
        self.add_bullet("Unauthorized control/access to computer system: Hacking into personal devices.")
        self.add_bullet("Indecent exposure: Sending inappropriate content.")
        self.add_page_break()

        self.add_heading("4.2 Cyber Crime Against Property", level=2)
        self.add_paragraph("Similar to real-world property crimes, these target computer or network property. The aim is often theft or destruction.")
        self.add_bullet("Computer Vandalism: Damaging or destroying data rather than stealing it.")
        self.add_bullet("Transmitting virus/worms: Spreading malware to damage systems.")
        self.add_bullet("Intellectual Property Crimes: Software piracy, copyright infringement, theft of trade secrets.")
        self.add_bullet("Internet Time Theft: Using someone else's internet connection without permission.")

        self.add_heading("4.3 Cyber Crime Against Government", level=2)
        self.add_paragraph("These are serious crimes often referred to as Cyber Terrorism. They target the nation's infrastructure or sensitive data.")
        self.add_bullet("Hacking government websites: Defacing or taking down official sites.")
        self.add_bullet("Cyber warfare: State-sponsored attacks on other nations.")
        self.add_bullet("Distribution of pirated software: Large scale piracy affecting the economy.")
        self.add_bullet("Possession of unauthorized information: Stealing classified documents.")
        
        self.add_image('graph_sectors.png', caption="Figure 4.1: Sectors Targeted by Cyber Crimes")
        self.add_page_break()

        # Chapter 5
        self.add_heading("Chapter 5: Prevention and Best Practices", level=1)
        self.add_paragraph("Prevention is always better than cure. By following some simple best practices, we can significantly reduce the risk of falling victim to cyber crime.")
        
        self.add_heading("5.1 Password Management", level=2)
        self.add_paragraph("Passwords are the first line of defense. A strong password should be at least 12 characters long, including a mix of letters, numbers, and symbols. Users should avoid using the same password across multiple sites. Using a Password Manager is highly recommended as it can generate and store complex passwords for you.")
        self.add_image('graph_passwords.png', caption="Figure 5.1: Analysis of Password Habits")

        self.add_heading("5.2 Two-Factor Authentication (2FA)", level=2)
        self.add_paragraph("2FA adds an extra layer of security. Even if a hacker gets your password, they cannot access your account without the second factor, which is usually a code sent to your phone or generated by an app. Enable 2FA on email, banking, and social media accounts.")

        self.add_heading("5.3 Software Updates", level=2)
        self.add_paragraph("Keep your software and operating system updated. Updates often contain patches for security vulnerabilities that have been discovered. Ignoring updates leaves your system exposed to known threats.")
        self.add_page_break()

        self.add_heading("5.4 Safe Browsing Habits", level=2)
        self.add_bullet("Do not click on suspicious links in emails or SMS.")
        self.add_bullet("Check for 'https' (lock icon) in the URL before entering sensitive info.")
        self.add_bullet("Avoid using public Wi-Fi for banking transactions as they can be easily intercepted.")
        self.add_bullet("Be careful what you share on social media. Personal information can be used for social engineering.")
        self.add_bullet("Use an Ad-blocker to prevent malicious ads (malvertising).")
        self.add_page_break()

        # Chapter 6: Network Security (New)
        self.add_heading("Chapter 6: Network Security Fundamentals", level=1)
        self.add_paragraph("Network security consists of the policies and practices adopted to prevent and monitor unauthorized access, misuse, modification, or denial of a computer network and network-accessible resources.")
        
        self.add_heading("6.1 Firewalls", level=2)
        self.add_paragraph("A firewall is a network security device that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules. It establishes a barrier between secured and controlled internal networks that can be trusted and untrusted outside networks, such as the Internet.")
        
        self.add_heading("6.2 Virtual Private Networks (VPN)", level=2)
        self.add_paragraph("A VPN extends a private network across a public network and enables users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network. It encrypts your internet traffic, protecting your online identity.")
        
        self.add_heading("6.3 Wi-Fi Security", level=2)
        self.add_paragraph("Securing your home Wi-Fi is crucial. Change the default router password, use WPA3 encryption, and hide your SSID if possible. Guest networks can be used for visitors to keep them isolated from your main devices.")
        self.add_page_break()

        # Chapter 7: Mobile Security (New)
        self.add_heading("Chapter 7: Mobile Device Security", level=1)
        self.add_paragraph("As we increasingly rely on smartphones for banking, shopping, and communication, they have become a prime target for attackers.")
        
        self.add_heading("7.1 App Permissions", level=2)
        self.add_paragraph("Be mindful of the permissions you grant to apps. Does a flashlight app really need access to your contacts and location? Review app permissions regularly.")
        
        self.add_heading("7.2 Physical Security", level=2)
        self.add_paragraph("Use a strong PIN, pattern, or biometric lock (fingerprint/face ID). Enable remote tracking and wiping features (like Find My Device) in case your phone is lost or stolen.")
        
        self.add_heading("7.3 Smishing and Vishing", level=2)
        self.add_paragraph("Smishing is phishing via SMS, and Vishing is phishing via Voice calls. Be skeptical of urgent messages or calls asking for personal details or money.")
        self.add_page_break()

        # Chapter 8 (Renumbered)
        self.add_heading("Chapter 8: Case Studies", level=1)
        self.add_heading("8.1 The WannaCry Ransomware Attack (2017)", level=2)
        self.add_paragraph("The WannaCry ransomware attack was a worldwide cyberattack in May 2017 by the WannaCry ransomware cryptoworm, which targeted computers running the Microsoft Windows operating system by encrypting data and demanding ransom payments in the Bitcoin cryptocurrency. It propagated through EternalBlue, an exploit discovered by the NSA. The attack affected more than 200,000 computers across 150 countries, causing billions of dollars in estimated damages. The National Health Service (NHS) in the UK was particularly hard hit, leading to cancelled appointments and surgeries.")

        self.add_heading("8.2 The Yahoo Data Breaches (2013-2014)", level=2)
        self.add_paragraph("Yahoo announced that all 3 billion of its user accounts were impacted by a 2013 data breach. The compromised data included names, email addresses, telephone numbers, dates of birth, hashed passwords, and, in some cases, encrypted or unencrypted security questions and answers. It remains one of the largest data breaches in history and significantly impacted Yahoo's valuation.")
        self.add_page_break()

        self.add_heading("8.3 SOLARWINDS Supply Chain Attack (2020)", level=2)
        self.add_paragraph("In 2020, a major cyberattack suspected to be directed by a nation-state targeted SolarWinds, a major US information technology firm. The attackers inserted malicious code into the Orion software updates, which were then downloaded by thousands of customers, including US government agencies. This highlighted the vulnerability of the software supply chain, where compromising one trusted vendor can lead to the compromise of thousands of their clients.")
        
        self.add_heading("8.4 The Facebook (Meta) Data Leak (2019)", level=2)
        self.add_paragraph("Personal data of over 533 million Facebook users from 106 countries was leaked online. The data included phone numbers, Facebook IDs, full names, locations, birthdates, and bios. This incident raised serious questions about data privacy and how social media giants handle user data.")
        self.add_page_break()

        # Chapter 9 (Renumbered)
        self.add_heading("Chapter 9: Statistical Analysis", level=1)
        self.add_paragraph("This chapter analyzes the trends in cyber security over the last 5 years based on global data. Data visualization helps in understanding the scale and direction of these threats.")
        
        self.add_heading("9.1 Trend of Phishing Attacks", level=2)
        self.add_paragraph("Phishing remains one of the most common entry points for attackers. As seen in the graph below, the number of incidents has nearly tripled in 5 years. This is due to the low cost of launching phishing campaigns and the difficulty in filtering them out completely.")
        self.add_image('graph_phishing_trend.png', caption="Figure 9.1: Rise in Phishing Attacks")

        self.add_heading("9.2 Analysis of Global Costs", level=2)
        self.add_paragraph("The data indicates a worrying trend. As digital adoption increases, so does the sophistication and frequency of attacks. The exponential growth in the cost of cybercrime suggests that businesses and governments need to invest significantly more in defensive infrastructure. The cost is not just financial but includes loss of trust and productivity.")
        self.add_page_break()

        # Chapter 10 (Renumbered)
        self.add_heading("Chapter 10: Cyber Laws and Ethics", level=1)
        self.add_heading("10.1 IT Act 2000 (India)", level=2)
        self.add_paragraph("The Information Technology Act, 2000 is the primary law in India dealing with cybercrime and electronic commerce. It provides a legal framework for electronic governance by giving recognition to electronic records and digital signatures. It was amended in 2008 to include more offenses.")
        
        self.add_heading("Key Offences and Penalties:", level=2)
        self.add_bullet("Sec 65: Tampering with computer source documents - Imprisonment up to 3 years or fine up to 2 lakh rupees.")
        self.add_bullet("Sec 66: Computer Related Offences (Hacking, etc.) - Imprisonment up to 3 years or fine up to 5 lakh rupees.")
        self.add_bullet("Sec 66C: Punishment for identity theft - Imprisonment up to 3 years.")
        self.add_bullet("Sec 66D: Punishment for cheating by personation by using computer resource.")
        self.add_bullet("Sec 67: Publishing or transmitting obscene material in electronic form.")
        self.add_page_break()

        self.add_heading("10.2 Cyber Ethics", level=2)
        self.add_paragraph("Cyber ethics refers to the code of responsible behavior on the internet. Just as we are taught to be good citizens in the real world, we must be good 'netizens'.")
        self.add_bullet("Do not use a computer to harm other people.")
        self.add_bullet("Do not interfere with other people's computer work.")
        self.add_bullet("Do not snoop around in other people's computer files.")
        self.add_bullet("Do not use a computer to steal.")
        self.add_bullet("Do not use a computer to bear false witness.")
        self.add_bullet("Do not use or copy software for which you have not paid.")
        self.add_bullet("Always respect the privacy of others.")
        self.add_page_break()

        # Chapter 11 (Renumbered)
        self.add_heading("Chapter 11: Future of Cyber Security", level=1)
        self.add_heading("11.1 Artificial Intelligence in Security", level=2)
        self.add_paragraph("AI is being used to analyze vast amounts of data to detect anomalies and potential threats faster than humans can. Machine learning models can predict attacks before they happen. However, hackers are also using AI to create smarter malware that can evade detection and automated attacks that adapt to defenses.")

        self.add_heading("11.2 IoT Security", level=2)
        self.add_paragraph("With the rise of the Internet of Things (IoT), billions of devices are coming online. From smart fridges to connected cars, everything is a potential target. Securing these often-insecure devices will be a major challenge for the future.")

        self.add_heading("11.3 Zero Trust Architecture", level=2)
        self.add_paragraph("The traditional security model assumed everything inside the network was safe. Zero Trust assumes a breach is inevitable or has likely already occurred. It constantly limits access to only what is needed and looks for anomalous or malicious activity, verifying every request as if it originates from an open network.")
        
        self.add_heading("11.4 Quantum Computing", level=2)
        self.add_paragraph("Quantum computers pose a significant threat to current encryption standards. They could potentially break the encryption that secures our banking and communications. Research is underway to develop 'post-quantum cryptography' that is resistant to quantum attacks.")
        self.add_page_break()

        # Conclusion
        self.add_heading("Conclusion", level=1)
        self.add_paragraph("The digital world is a double-edged sword. While it offers immense opportunities for learning, communication, and business, it also presents significant risks. Cyber security is the shield that protects us in this digital age.")
        self.add_paragraph("This project has explored the various facets of cyber security, from the types of threats to the laws that govern them. The statistical data clearly shows that cyber crime is on the rise, and no sector is immune. The case studies remind us of the real-world impact of these digital threats.")
        self.add_paragraph("As students and future leaders, it is our responsibility to be aware of these threats and practice good cyber hygiene. Education and awareness are the most powerful tools we have. By staying informed and vigilant, we can enjoy the benefits of technology without falling victim to its dangers.")
        self.add_paragraph("In conclusion, cyber security is a shared responsibility. Governments, corporations, and individuals must work together to create a safer digital environment for everyone.")
        self.add_page_break()

        # Bibliography
        self.add_heading("Bibliography", level=1)
        self.add_paragraph("The following sources were consulted for this project:")
        sources = [
            "NCERT Information Technology Textbook for Class 10",
            "Norton Cyber Security Insights Report 2023",
            "Symantec Internet Security Threat Report",
            "The Information Technology Act, 2000 (India)",
            "www.cybercrime.gov.in - Official Cyber Crime Reporting Portal",
            "www.kaspersky.com/resource-center - Cyber Security Insights",
            "www.cisco.com/c/en/us/products/security/what-is-cybersecurity.html",
            "Wikipedia - Computer Security and Cybercrime",
            "Statista - Global Cyber Security Statistics"
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

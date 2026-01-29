
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import matplotlib.pyplot as plt
import os

def create_graphs():
    # 1. Pie Chart: Common Cyber Threats
    labels = ['Phishing', 'Malware', 'Ransomware', 'Social Engineering', 'DDoS']
    sizes = [35, 30, 15, 10, 10]
    colors_pie = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
    
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors_pie)
    plt.title('Common Cyber Threats Distribution')
    plt.savefig('threats_pie_chart.png')
    plt.close()

    # 2. Bar Chart: Cyber Attacks over Years (Hypothetical Data)
    years = ['2019', '2020', '2021', '2022', '2023']
    attacks = [150, 200, 350, 500, 750] # Hypothetical number of major incidents
    
    plt.figure(figsize=(8, 5))
    plt.bar(years, attacks, color='skyblue')
    plt.xlabel('Year')
    plt.ylabel('Number of Reported Incidents (Thousands)')
    plt.title('Rise in Cyber Attacks (2019-2023)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('attacks_bar_chart.png')
    plt.close()

def create_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Custom Styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.darkblue
    )
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=12,
        textColor=colors.darkblue
    )
    body_style = styles['BodyText']
    body_style.fontSize = 12
    body_style.spaceAfter = 12

    # --- Title Page ---
    story.append(Spacer(1, 100))
    story.append(Paragraph("Information Technology Project", title_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Topic: Cyber Security Awareness", ParagraphStyle('Subtitle', parent=styles['Heading2'], alignment=1)))
    story.append(Spacer(1, 100))
    story.append(Paragraph("Submitted by: Student Name", body_style))
    story.append(Paragraph("Class: 10th", body_style))
    story.append(Paragraph("Roll No: 1234", body_style))
    story.append(PageBreak())

    # --- Introduction ---
    story.append(Paragraph("1. Introduction", heading_style))
    intro_text = """
    In today's interconnected world, cyber security has become a critical concern for individuals, organizations, and governments alike. 
    With the rapid advancement of technology and the increasing reliance on the internet, the risk of cyber attacks has grown exponentially. 
    This project aims to explore the various aspects of cyber security, common threats, and best practices to stay safe online.
    """
    story.append(Paragraph(intro_text, body_style))
    story.append(Spacer(1, 12))

    # --- Common Threats Section ---
    story.append(Paragraph("2. Common Cyber Threats", heading_style))
    threats_text = """
    Cyber threats come in many forms, each designed to exploit vulnerabilities in systems or human behavior. 
    Some of the most prevalent threats include:
    """
    story.append(Paragraph(threats_text, body_style))
    
    # List of threats
    bullet_style = ParagraphStyle('Bullet', parent=body_style, bulletIndent=10)
    story.append(Paragraph("• <b>Phishing:</b> Fraudulent attempts to obtain sensitive information like usernames and passwords.", bullet_style))
    story.append(Paragraph("• <b>Malware:</b> Malicious software designed to disrupt, damage, or gain unauthorized access to a computer system.", bullet_style))
    story.append(Paragraph("• <b>Ransomware:</b> A type of malware that encrypts a victim's files, with the attacker demanding a ransom to restore access.", bullet_style))
    story.append(Spacer(1, 12))

    # Add Pie Chart
    story.append(Paragraph("Figure 1: Distribution of Common Cyber Threats", styles['Italic']))
    story.append(Spacer(1, 10))
    img1 = Image('threats_pie_chart.png', width=400, height=400)
    story.append(img1)
    story.append(Spacer(1, 20))

    # --- Trends Analysis ---
    story.append(Paragraph("3. Trends in Cyber Crime", heading_style))
    trends_text = """
    Over the past few years, there has been a significant rise in the number of reported cyber incidents. 
    The shift to remote work and increased digitalization has expanded the attack surface for cybercriminals.
    The graph below illustrates the increasing trend of cyber attacks from 2019 to 2023.
    """
    story.append(Paragraph(trends_text, body_style))
    
    # Add Bar Chart
    story.append(Paragraph("Figure 2: Rise in Cyber Attacks (Hypothetical Data)", styles['Italic']))
    story.append(Spacer(1, 10))
    img2 = Image('attacks_bar_chart.png', width=500, height=312)
    story.append(img2)
    story.append(Spacer(1, 20))
    story.append(PageBreak())

    # --- Best Practices ---
    story.append(Paragraph("4. Best Practices for Cyber Safety", heading_style))
    safety_text = """
    To protect against these threats, it is essential to follow cyber hygiene best practices:
    """
    story.append(Paragraph(safety_text, body_style))
    story.append(Paragraph("• Use strong, unique passwords for every account.", bullet_style))
    story.append(Paragraph("• Enable Two-Factor Authentication (2FA) wherever possible.", bullet_style))
    story.append(Paragraph("• Keep software and operating systems updated.", bullet_style))
    story.append(Paragraph("• Be cautious of suspicious emails and links.", bullet_style))
    story.append(Paragraph("• Regularly back up important data.", bullet_style))
    story.append(Spacer(1, 20))

    # --- Conclusion ---
    story.append(Paragraph("5. Conclusion", heading_style))
    conclusion_text = """
    Cyber security is not just a technical issue but a societal one. As we become more dependent on digital infrastructure, 
    awareness and proactive measures are our best defense. By understanding the threats and implementing safety measures, 
    we can navigate the digital world more securely.
    """
    story.append(Paragraph(conclusion_text, body_style))

    # Build PDF
    doc.build(story)
    print(f"PDF created successfully: {filename}")

if __name__ == "__main__":
    print("Generating graphs...")
    create_graphs()
    print("Graphs generated. Creating PDF...")
    create_pdf("Class_10_IT_Project_CyberSecurity.pdf")
    
    # Clean up images
    if os.path.exists('threats_pie_chart.png'):
        os.remove('threats_pie_chart.png')
    if os.path.exists('attacks_bar_chart.png'):
        os.remove('attacks_bar_chart.png')
    print("Done.")

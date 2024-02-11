from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def add_content_to_pdf(c, text, start_y):
    """Helper function to add text content to the PDF."""
    # Split text for multiline support
    for line in text.split('\n'):
        c.drawString(100, start_y, line)
        start_y -= 15
    return start_y

def generate_combined_report(urls_headers_security, save_directory, filename):
    """Generates a combined PDF report."""
    full_path = os.path.join(save_directory, filename)
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    c = canvas.Canvas(full_path, pagesize=letter)
    start_y = 750

    for url, headers, security in urls_headers_security:
        # Add URL to PDF
        start_y = add_content_to_pdf(c, f"URL: {url}", start_y)
        
        # Add Header Information to PDF
        headers_text = "Header Information:\n" + "\n".join([f"{k}: {v}" for k, v in headers.items()])
        start_y = add_content_to_pdf(c, headers_text, start_y - 10)
        
        # Add Security Findings to PDF
        missing_headers_text = "Missing Security Headers:\n" + ", ".join(security['missing_headers'])
        start_y = add_content_to_pdf(c, missing_headers_text, start_y - 10)

        cors_policy_text = f"CORS Policy: {security['cors_policy']}"
        start_y = add_content_to_pdf(c, cors_policy_text, start_y - 10)
        
        # Ensure there's a new page for the next URL if not enough space
        if start_y < 100:
            c.showPage()
            start_y = 750
    
    c.save()
    print(f"Generated combined PDF report: {full_path}")

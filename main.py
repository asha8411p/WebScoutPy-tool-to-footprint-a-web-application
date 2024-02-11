import os
from webscout import fetch_urls
from security_scanner import check_security_headers, check_cors_policy
from report_generator import generate_combined_report

def main():
    file_path = 'recon.txt'
    # Use the SAVE_DIRECTORY environment variable, defaulting to a local path if not set
    save_directory = os.getenv('SAVE_DIRECTORY', 'E:\\Coding\\Python Projects\\WebScoutPy-tool to footprint a web application')
    filename = 'ABC__combined_report.pdf' #Choose the name of your file
    urls_headers = fetch_urls(file_path)
    
    urls_headers_security = []
    for url, headers in urls_headers:
        missing_headers = check_security_headers(url)
        cors_policy = check_cors_policy(url)
        urls_headers_security.append((url, headers, {'missing_headers': missing_headers, 'cors_policy': cors_policy}))
    
    generate_combined_report(urls_headers_security, save_directory, filename)

if __name__ == "__main__":
    main()

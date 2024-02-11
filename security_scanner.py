# Contains functions check_security_headers and check_cors_policy
import requests

def check_security_headers(url):
    response = requests.get(url)
    headers = response.headers
    important_headers = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options",
                        "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy", "X-XSS-Protection"]
    missing_headers = [header for header in important_headers if header not in headers]
    return missing_headers

def check_cors_policy(url):
    response = requests.options(url)
    if 'Access-Control-Allow-Origin' in response.headers and response.headers['Access-Control-Allow-Origin'] == '*':
        return "CORS misconfigured: Allows any origin"
    return "CORS configured properly or not present"

"""
Track 16: Application Security, Cryptography & Defense in Depth

Description: Master Senior Python Track 16: Application Security, Cryptography & Defense in Depth. OWASP defenses, SSRF IP blocking, Argon2id/bcrypt password hashing, hmac.compare_digest timing protection, and JWT RS256 hardening.
Level: Senior
URL: http://127.0.0.1:5000/python/senior/security_cryptography_defense
"""

# --- Code Snippet 1 ---
WHERE id = :id AND org_id = :user_org_id

# --- Code Snippet 2 ---
import ipaddress, socket, urllib.parse

def is_safe_ssrf_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https":
        return False
    ip_str = socket.gethostbyname(parsed.hostname)
    ip = ipaddress.ip_address(ip_str)
    # Reject loopback (127.0.0.0/8), private (10.0.0.0/8, 192.168.0.0/16), and link-local (169.254.169.254)
    return not (ip.is_private or ip.is_loopback or ip.is_link_local)

# --- Code Snippet 3 ---
import hmac

# Constant-Time Comparison prevents timing attacks (vs '==' short-circuit)
def safe_verify_secret(provided_token: str, expected_token: str) -> bool:
    return hmac.compare_digest(provided_token.encode('utf-8'), expected_token.encode('utf-8'))


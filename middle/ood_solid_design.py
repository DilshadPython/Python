"""
Section 3: Object-Oriented Design & SOLID Architecture

Description: Master Object-Oriented Design and SOLID principles in Python: Encapsulation, Abstraction, Inheritance, Polymorphism, SRP, OCP, LSP, ISP, and DIP. Decouple services with Repository and Injection patterns.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/ood_solid_design
"""

# --- Code Snippet 1 ---
class UserService:
    def register_user(self, email, raw_password):
        # ❌ 1. Input Validation
        if "@" not in email:
            raise ValueError("Invalid email")
            
        # ❌ 2. Password Hashing
        hashed_pw = f"hash_{raw_password}"
        
        # ❌ 3. Direct SQL Database Query
        db = sqlite3.connect("app.db")
        db.execute("INSERT INTO users...")
        
        # ❌ 4. Direct Email Network Call
        smtplib.SMTP("smtp.app.com").sendmail(...)
        
        # ❌ 5. Direct Token Generation
        token = jwt.encode(...)
        return token

# --- Code Snippet 2 ---
class UserService:
    """High-level orchestration service obeying SRP & DIP."""
    
    def __init__(
        self,
        repository: UserRepository,
        email_service: EmailService,
        token_service: TokenService,
        hasher: PasswordHasher
    ) -> None:
        self.repository = repository
        self.email_service = email_service
        self.token_service = token_service
        self.hasher = hasher

    def register_user(self, email: str, raw_password: str) -> dict:
        hashed_pw = self.hasher.hash_password(raw_password)
        user_id = self.repository.save(email, hashed_pw)
        
        self.email_service.send_welcome_email(email)
        token = self.token_service.generate_token(user_id, email)
        
        return {"user_id": user_id, "token": token}


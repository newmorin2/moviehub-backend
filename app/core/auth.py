
import firebase_admin
from firebase_admin import credentials, auth
import glob
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


DEFAULT_CRED_PATH = "secrets/firebase-admin.json"


def _resolve_cred_path() -> str:
    cred_path = os.getenv("FIREBASE_ADMIN_CREDENTIALS", DEFAULT_CRED_PATH)

    if os.path.exists(cred_path):
        return cred_path

    secret_files = glob.glob(os.path.join("secrets", "*firebase-adminsdk*.json"))
    if secret_files:
        return secret_files[0]

    raise FileNotFoundError(
        f"Firebase admin credential file not found. "
        f"Looked for '{cred_path}' and in 'secrets/' directory. "
        f"Set FIREBASE_ADMIN_CREDENTIALS if needed."
    )


def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(_resolve_cred_path())
        firebase_admin.initialize_app(cred)

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        
        decoded_token = auth.verify_id_token(token)
        return decoded_token  
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
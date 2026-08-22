from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import jwt
import requests
from jwt import PyJWKClient

from app.config import (
    OPENID_CONFIG_URL,
    ISSUER,
    ALGORITHM,
)

security = HTTPBearer()



openid_config = requests.get(OPENID_CONFIG_URL).json()

JWKS_URI = openid_config["jwks_uri"]

jwks_client = PyJWKClient(JWKS_URI)


def get_current_token(
    credentials: HTTPAuthorizationCredentials = Security(security),
):
    token = credentials.credentials

    try:
        signing_key = jwks_client.get_signing_key_from_jwt(token)

        payload = jwt.decode(
            token,
            signing_key.key,
            algorithms=[ALGORITHM],
            issuer=ISSUER,
            options={
                "verify_aud": False
            }
        )

        return payload


  

    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token."
        )


def require_customer_role(claims: dict):
    roles = claims.get("realm_access", {}).get("roles", [])

    if "customer" not in roles:
        raise HTTPException(
            status_code=403,
            detail="Access denied. Customer role required."
        )

    return claims        
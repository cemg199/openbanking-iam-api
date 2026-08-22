import os

KEYCLOAK_SERVER = os.getenv(
    "KEYCLOAK_SERVER",
    "http://localhost:8080"
)

REALM = os.getenv(
    "REALM",
    "OpenBanking"
)

CLIENT_ID = os.getenv(
    "CLIENT_ID",
    "bank-api"
)

ALGORITHM = "RS256"

ISSUER = f"{KEYCLOAK_SERVER}/realms/{REALM}"

OPENID_CONFIG_URL = (
    f"{KEYCLOAK_SERVER}/realms/{REALM}/.well-known/openid-configuration"
)


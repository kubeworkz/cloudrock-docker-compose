CLOUDROCK_CORE['AUTHENTICATION_METHODS'] = ["LOCAL_SIGNIN", "SOCIAL_SIGNUP"]

CLOUDROCK_CORE['SITE_NAME'] = 'test'

CLOUDROCK_CORE['SITE_LOGO'] = '/etc/cloudrock/logo.png'

CLOUDROCK_CORE['CREATE_DEFAULT_PROJECT_ON_ORGANIZATION_CREATION'] = True

# Disable geoip location till HomePort releases maps to a stable deployment
CLOUDROCK_CORE['ENABLE_GEOIP'] = False

CLOUDROCK_AUTH_SOCIAL.update({'KEYCLOAK_AUTH_URL': '/auth/realms/Cloudrock/protocol/openid-connect/auth',
 'KEYCLOAK_CLIENT_ID': 'cloudrock',
 'KEYCLOAK_SECRET': env.get('KEYCLOAK_SECRET'),
 'KEYCLOAK_TOKEN_URL': 'http://keycloak:8080/auth/realms/Cloudrock/protocol/openid-connect/token',
 'KEYCLOAK_USERINFO_URL': 'http://keycloak:8080/auth/realms/Cloudrock/protocol/openid-connect/userinfo'
})

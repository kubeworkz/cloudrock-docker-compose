CLOUDROCK_CORE['AUTHENTICATION_METHODS'] = ["LOCAL_SIGNIN", "SOCIAL_SIGNUP"]

CLOUDROCK_CORE['SITE_NAME'] = 'test'

CLOUDROCK_CORE['SITE_LOGO'] = '/etc/cloudrock/logo.png'

CLOUDROCK_CORE['CREATE_DEFAULT_PROJECT_ON_ORGANIZATION_CREATION'] = True

# Disable geoip location till HomePort releases maps to a stable deployment
CLOUDROCK_CORE['ENABLE_GEOIP'] = False

CLOUDROCK_AUTH_SOCIAL.update({'KEYCLOAK_AUTH_URL': 'http://localhost:8080/auth/realms/kcrealm/protocol/openid-connect/auth',
 'KEYCLOAK_CLIENT_ID': 'cloudrock',
 'KEYCLOAK_SECRET': env.get('KEYCLOAK_SECRET'),
 'KEYCLOAK_TOKEN_URL': 'http://fckeycloak:8080/auth/realms/kcrealm/protocol/openid-connect/token',
 'KEYCLOAK_USERINFO_URL': 'http://fckeycloak:8080/auth/realms/kcrealm/protocol/openid-connect/userinfo'
})

CLOUDROCK_FREEIPA.update({
    'ENABLED': True,
    'GROUPNAME_PREFIX': 'hpc_',
    'HOSTNAME': 'ipa.demo1.freeipa.org',
    'PASSWORD': 'Secret123',
    'USERNAME': 'admin',
    'USERNAME_PREFIX': 'hpcu_',
})

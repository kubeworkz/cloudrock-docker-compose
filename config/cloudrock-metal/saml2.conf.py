# Custom SAML2 configuration
CLOUDROCK_AUTH_SAML2.update({
    # PEM formatted certificate chain file
    'CERT_FILE': '/etc/cloudrock/saml2/credentials/sp.crt',
    # PEM formatted certificate key file
    'KEY_FILE': '/etc/cloudrock/saml2/credentials/sp.pem',
})

# Expected file list

- login-logo.png
- sidebar-logo.png
- privacy.html
- privacy-full.html
- tos.html
- favicon.ico

Don't forget to adjust `config/cloudrock-ui/nginx.conf`, e.g.:

```nginx
    location /login-logo.png {
        alias /opt/cloudrock-ui/login-logo.png;
    }

    location /sidebar-logo.png {
        alias /opt/cloudrock-ui/sidebar-logo.png;
    }

    location /views/policy/privacy.html {
        alias /opt/cloudrock-ui/privacy.html;
    }

    location /views/policy/privacy-full.html {
        alias /opt/cloudrock-ui/privacy-full.html;
    }

    location /views/tos/index.html {
        alias /opt/cloudrock-ui/tos.html;
    }
```

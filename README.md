# check_ssl_chain_certificate

### DESCRIPTION
```
when we config https to application, sometimes forgot to include ssl chain certification into web server configuration.

This may encounter 'CERTIFICATE_VERIFY_FAILED' message to user.
You need to Check your ssl chain cerification configuration and fix it.
```

### USAGE
```
# python check.py
[-] ERROR:: https://mydomain.com CERTIFICATE_VERIFY_FAILED
...
...
[-] ERROR:: https://mydomain2.com CERTIFICATE_VERIFY_FAILED
[-] OK:: https://google.com 200 gws
```

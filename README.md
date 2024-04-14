UPDATE SAVE IP API
==================

A Simple script that could be run from a container to update [SaveIpApi](https://github.com/theninth/SaveIpApi).

## Example produktion docker-compose.yaml-file

```yaml
services:
  saveipapi:
    image: thenajnth/py_update_save_ip_api:3
    container_name: pyupdatesaveipapi
    env_file:
      - .env

```

This file should be accompanied with a .env-file to override appsettings.json. For example:

```
SAVEIPAPI_KEY=somevalue
SAVEIPAPI_BASEURL=https://saveipapi.example.com
SAVEIPAPI_APIKEY=my_super_secret_apikey
```
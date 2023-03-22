# lambda-serverless-1

This repository is used for deploying microservice lambda-serverless-1. It is possible to use files from this directory to deploy service.

## Regex option

If you need to change the value of regex parameter, it's necessary to edit Simloudfile.yaml.
There are 2 possible options for regex value:
- true - for service, the regex rules will be applied based on the already set and specifically configured regex rules in Simloudfile.yaml. It could be a custom value that suits a customer needs
- false - service will be deployed without any regex rules and according to already specified configuration in URL path.

Example of code block:

```
regex:
    enabled: false
    rewrite-target: /$2$3$4
````
```
regex:
    enabled: true
    rewrite-target: /$2$3$4
```

**Additional documentation is placed by links:**
- [**"Simloudfile.yaml"**](https://prod--simloud-docs.netlify.app/en/simloudfile.yaml/)

- [**"How to use Simloud files"**](https://prod--simloud-docs.netlify.app/en/how-to-use-simloud-files/)

- [**"How to create and manage your SSH keys"**](https://stage--simloud-docs.netlify.app/en/getting-started/#managing-the-ssh-keys)

- [**"How to work with repositories"**](https://stage--simloud-docs.netlify.app/en/getting-started/#add-new-git-repositories-services)

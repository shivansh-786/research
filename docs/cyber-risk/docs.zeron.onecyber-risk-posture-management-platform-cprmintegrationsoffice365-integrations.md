  1. [Integrations](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations)


# OFFICE365 Integrations
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252Fes2Z0LT3qpNXLB3ydfKA%252Foffice365-ae73b095e9a8de9d1ecfc0b78e44392e.png%3Falt%3Dmedia%26token%3Ddc23a2db-d892-4bbe-ba0c-b86ecb5a0bce&width=768&dpr=4&quality=100&sign=44d05305&sv=2)
Copy```
tenant_id: <your tenant id> #Tenant id of your application registered in Azure. 
client_id: <your client id> #Client id of your application registered in Azure. 
client_secret_path: < your client secret path > # Path of the file that contains the client secret value of your application registered in Azure. Incompatible with client_secret option. 
client_secret: <Your client secret> #Client secret value of your application registered in Azure. 
```

Subscriptions:
  * Audit.AzureActiveDirectory #User identity management
  * Audit.SharePoint #Web-based collaborative platform 
  * Audit.General #Includes all other workloads not included in the previous content types 
  * DLP.All #Data loss prevention workloads 


Save the configuration and send them to Zeron Team 
For Zensor to successfully connect to the Office365 API, an authentication process is required. To do this, we must provide the tenant_id, client_id, and client_secret of the application that we authorize in the organization 
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/office365-integrations#register-your-app)
Register your app
**To authenticate with the Microsoft identity platform endpoint, you need to register an app in your Microsoft Azure portal app registrations section. Once there click on New registration :**
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FNmya3apGVWNTbB8W5jkC%252Fapp_registration-ae5bfdc9399c786fd8fdd2e16428ffd5.png%3Falt%3Dmedia%26token%3Dd75d2444-319a-4f44-9593-72e223eec68e&width=768&dpr=4&quality=100&sign=a3e57fb2&sv=2)
**Fill in the name of your app, choose the desired account type and click on the Register button :**
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F6FQh3PVBzrcpWzNM18I2%252Fregistration_application-9490d23fac03e3b54d4ea47f2098b7d6.jpeg%3Falt%3Dmedia%26token%3D1aa0e300-b0ce-47e2-a627-3d2cbabd2264&width=768&dpr=4&quality=100&sign=c3f578ba&sv=2)
**The app is now registered, and you can see information about it in its Overview section, at this point we can get the client and tenant IDs :**
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FGspPwb6QuNpEfnMXHIc8%252Foverview.png%3Falt%3Dmedia%26token%3Def896527-7d6f-467a-ba0e-aa194e26f477&width=768&dpr=4&quality=100&sign=949db6f7&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/office365-integrations#certificates-and-secrets)
Certificates & secrets
You can generate a password to use during the authentication process. **Go to Certificates & secrets and click on New client secret, then the name and the expiration date of the New client secret are requested :**
`Copy and save the value section`
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FyBGw90TUY2NpLlmKcoSD%252Fcerti_secrets_value-fb693f5de67b4b359be12ce8a23763b6.png%3Falt%3Dmedia%26token%3D79e23146-0bd4-423a-b0f9-bd4729c9dee1&width=768&dpr=4&quality=100&sign=67e2d449&sv=2)
Note Make sure you write it down because the UI won’t let you copy it afterward.
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/office365-integrations#api-permissions)
API Permissions
The application needs specific API permissions to be able to request the Office 365 activity events. In this case, you are looking for permissions related to the https://manage.office.com resource. To configure the application permissions, go to the API permissions page and choose Add a permission. Select the Office 365 Management APIs and click on Application permissions. You need to add the following permissions under the ActivityFeed group: ActivityFeed.Read. Read activity data for your organization. ActivityFeed.ReadDlp. Read DLP policy events including detected sensitive data
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FsYdptGEqyWQPhw6ksQhs%252Fadd_permission.png%3Falt%3Dmedia%26token%3Df0bafd48-9ee4-41f1-9103-16bdd002a285&width=768&dpr=4&quality=100&sign=9f670a25&sv=2)
**Note -** Admin consent is required for API permission changes 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FkfgkpmWjgQk8ibadKIVn%252Fapi_permission-6dbf05416694e6efeade29afdf3de716.png%3Falt%3Dmedia%26token%3D9aeab746-79c8-4142-9219-ecdc2155bf3e&width=768&dpr=4&quality=100&sign=e8d67034&sv=2)
Last updated 4 months ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

  1. [Integrations](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations)


# Azure Integrations
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252Fkf7aPx8JjWZ1KHufTw74%252Fazure.png%3Falt%3Dmedia%26token%3Dfcf7a353-81b6-4e73-96d1-5d018346f8ab&width=768&dpr=4&quality=100&sign=8e94d225&sv=2)
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#zeron-could-be-integrated-with-microsoft-azure-via-the-following-methods)
Zeron could be integrated with Microsoft Azure via the following methods :
  * **Azure Graph Log API -** To monitor Azure Active Directory
  * **Azure Log Analytics -** To monitor Azure Platform and Services
  * **Azure Storage -** To monitor Azure Platform and Services


#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#requirement-for-log-analytics)
Requirement for Log Analytics :
  * Application ID
  * Application Key
  * Tenant-Domain
  * Subscription ID
  * Workspace


#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#requirement-for-graph-api)
Requirement for Graph API :
  * Application ID
  * Application Key
  * Tenant Domain


#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#requirement-for-azure-storage)
Requirement for Azure Storage :
  * Container Name
  * Account Name
  * Account Key


## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#configuring-azure-credentials)
Configuring Azure credentials
It is necessary to provide access credentials to the Zensor Azure module so it can successfully connect to Azure. The credentials required vary depending on the type of monitoring. Getting access credentials for Microsoft Graph and Log Analytics
For Microsoft Graph and Log Analytics valid application_id and application_key values are required. **The necessary application_key value for a given App Registration in Azure Active Directory can be obtained from the Certificates & secrets section while the application_id can be obtained from the Overview section : **
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FLK3IOg5SqcYn3589ZEk2%252Fazure-csr.png%3Falt%3Dmedia%26token%3D1ee3127b-48a1-41f5-ae11-7cc11a3e25d3&width=768&dpr=4&quality=100&sign=9bee940e&sv=2)
`Click New Client Secret`
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252Fj1kj1LfWo0F1BzpN75nJ%252FnewClient.png%3Falt%3Dmedia%26token%3D59097855-ef2e-4202-a55e-89fecf4002a6&width=768&dpr=4&quality=100&sign=8718b5f8&sv=2)
`Save the credentials (application ID and application key values) and send them to Zeron Team.`
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#getting-access-credentials-for-storage)
Getting access credentials for Storage
Azure Storage requires valid account_name and account_key values. **They can be obtained in the Access keys section of Storage accounts :**
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FaC06yXgJtCiTrf8Sl880%252FaccessKey.png%3Falt%3Dmedia%26token%3Dcbfe0464-0361-4d75-ad8c-9d1a94b1defc&width=768&dpr=4&quality=100&sign=b5c160ba&sv=2)
`ave the credentials (account_name , account_key and application ID and application key values) and send them to Zeron Team. Tenantdomain is required`
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#azure-storage-configuration)
Azure Storage Configuration
Azure Storage refers to the Microsoft Azure cloud storage solution, a service that provides a massively scalable object store for data objects, a messaging store for reliable messaging, a file system service for the cloud, and a NoSQL store. | As an alternative to the Azure Log Analytics REST API, Zeron offers the possibility to access Azure Storage accounts in a simple way. The activity logs of the Microsoft Azure infrastructure can be exported to the storage accounts. | This section explains how to use the Azure portal to archive the Azure activity log in a storage account and how to configure the azure-logs module. A use case is included to show a practical example
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#configuring-the-activity-log-export)
Configuring the Activity log export 
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#audit-logs)
Audit logs : 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FG6Hc7cYLmaTHmNnjWQpW%252FauditLogs-a30fdf6fa4ccbb017a101eeaf1f23581.png%3Falt%3Dmedia%26token%3D57f0db10-c624-41a7-8953-aa6030aac8fb&width=768&dpr=4&quality=100&sign=bd28eabe&sv=2)
To export the logs, search for the Activity log service. It can be found by typing “Activity” in the search engine. From there, access the Audit Logs section and click on Export Data Settings 
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#click-on-add-diagnostic-setting)
Click on Add diagnostic setting : 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F5njLMaYIbzpEzlEO3Jjq%252Fdiagonastics.png%3Falt%3Dmedia%26token%3D87665eca-dc84-4ab9-b219-6f3bb4ae67a1&width=768&dpr=4&quality=100&sign=2ccb1fbc&sv=2)
Diagnostics Logs : 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FgUg2Nea294c9wzkRwKad%252FdiagonasticsLogs.png%3Falt%3Dmedia%26token%3D7d9b5f27-e839-415d-8e79-49a0a3b14d09&width=768&dpr=4&quality=100&sign=2bbbe850&sv=2)
Check the AuditLogs box and the Archive to storage account, selecting the name of the subscription and the Storage account to export the logs 
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#azure-log-analytics)
Azure Log Analytics
Azure Log Analytics is a service that monitors your infrastructure offering query capabilities that allow you to perform advanced searches specific to your data. The Log Analytics solution helps you to analyse and search the Azure activity log in all your Azure subscriptions, providing information about the operations performed with the resources of your subscriptions. The data collected by Log Analytics can be consulted through the Azure Log Analytics REST API. The Azure Log Analytics API uses the Azure Active Directory authentication scheme. A qualified application or client is required to use the Azure Log Analytics REST API. This must be configured manually on the Microsoft Azure portal 
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#setting-up-the-application)
Setting up the application
The process explained below details the creation of an application that will use the Azure Log Analytics REST API. It is also possible to configure an existing application. If this is the case, skip the Creating the application step 
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#creating-the-application)
Creating the application 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F13PIHFgVyMpTy04IHIgD%252FappRegistration-02414fc58ad0b13915982a793cf50c7c.png%3Falt%3Dmedia%26token%3D4ca20531-60fd-4b3a-a886-9f04dfa24c6a&width=768&dpr=4&quality=100&sign=5a642b5f&sv=2)
In the Azure Active Directory panel, select the option App registrations. Then, select New registration 
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#giving-permissions-to-the-application)
Giving permissions to the application
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#application-client-id)
Application (client) ID : 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FD35EpJrUuQC9j0uKWFUc%252FappID-a11beaf6260f1d88d8a91c9e2c14e88e.png%3Falt%3Dmedia%26token%3D38b58173-9d13-4870-8cc9-568eb1e964ee&width=768&dpr=4&quality=100&sign=bc0cc470&sv=2)
Go to the Overview section and save the Application (client) ID for later authentication 
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#api-permission)
API Permission : 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FPw83y5xcShSDO9BWruLy%252FapiPermission-92ef20238268f79d1cc351414b045ff0.png%3Falt%3Dmedia%26token%3Dc6bb800f-fcc5-4206-9832-92ce91740994&width=768&dpr=4&quality=100&sign=82715aca&sv=2)
Go to the API permissions section and add the required permissions to the application 
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#log-analytics-api)
Log Analytics API : 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F85Mtv2tgPx1ofBmH3tqH%252FanalyticsAPI-99bb56a6bb3b3cd4c36479f1e94b1852.png%3Falt%3Dmedia%26token%3Df4a5c5ce-57f7-4a30-be49-36c511092d89&width=768&dpr=4&quality=100&sign=6e7a1c70&sv=2)
Search for the Log Analytics API 
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#add-permission)
Add Permission : 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FKR4E8wNT7HVUTDmBboli%252FaddPermission-bea3ca10156df609d34e2fd07949f03d.png%3Falt%3Dmedia%26token%3D7939bd5d-c062-496e-a304-f3d30512e706&width=768&dpr=4&quality=100&sign=c3bc0069&sv=2)
Select the Read Log Analytics data permission from Applications permissions 
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#grant-admin-consent)
Grant admin consent : 
Grant admin consent for the tenant domain used for the permission added in the previous step. This must be done by an admin user 
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#obtaining-the-application-key-for-authentication)
Obtaining the application key for authentication
Select Certificates & secrets and fill in the Description and Expires fields. Copy the value once the key is saved. This is required to authenticate the application in order to use the Log Analytics API. | You can view previous topic configuring azure credentials
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#giving-our-application-access-to-the-log-analytics-api)
Giving our application access to the Log Analytics API
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#create-a-new-workspace)
Create a new workspace : 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F6eoTJwcN4SGaYBhGOfrJ%252Fazure-log-analytics.png%3Falt%3Dmedia%26token%3Ddf387601-6513-4fb5-85fa-5fbaa2e3dcef&width=768&dpr=4&quality=100&sign=98bb8566&sv=2)
Access Log Analytics workspaces and create a new workspace or choose an existing one. Then, copy the Workspace Id value from the Overview section. This will be used in the Zeron configuration to allow making requests to the API 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FmxTqM9GQYvSCPIR82RZx%252Fframeworktest-6808313227a2711845a8f468e75db5c4.png%3Falt%3Dmedia%26token%3D19f3bffb-3da4-4a0a-8d08-e4af436f91fe&width=768&dpr=4&quality=100&sign=f3e52e64&sv=2)
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#add-iam-role)
Add IAM Role : 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FQ76zzCQPiGjj61fL5GEY%252Fazure_Iam_role-5c5f580450d154225d52e694776efb3d.png%3Falt%3Dmedia%26token%3D1f74b830-4a13-4bcd-8767-73bc514fc96e&width=768&dpr=4&quality=100&sign=1e3a122b&sv=2)
Add the required role to the application in the Access Control (IAM) section by clicking the Add and selecting Add Role assignment 
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/azure-integrations#add-role-assignment)
Add Role assignment : 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FArAjFmHaXBBkNLEpTgwR%252Fadd_role_assignment.png%3Falt%3Dmedia%26token%3D4c6e0aeb-b542-4382-9f79-5fa1f5f0a4c7&width=768&dpr=4&quality=100&sign=d1c47e53&sv=2)
Fill in the required fields and click save. It is important to choose the User, group, or service principal option in the drop-down menu and to type the full application name in the Select field 
Last updated 4 months ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject


Was this helpful?
# Accops ZTNA (HySecure)
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F4211542702-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FQPfbdyLrtbE8w5R9rmvH%252Fuploads%252FZjTGYh9RrSE0rgZEZFq3%252FAccops_Logo.653bdac-2.svg%3Falt%3Dmedia%26token%3D59a4227e-e4bd-4a0f-ac11-2c3c66cf8d83&width=768&dpr=4&quality=100&sign=18ab0155&sv=2)
This document outlines how to integrate the ZERON platform with Accops HySecure (ZTNA Gateway) using HySecure’s APIs to collect user information and endpoint IP addresses. **The integration focuses solely on retrieving :**
  * Registered Users from the ZTNA system 
  * Active Users with their associated endpoint WAN IP addresses 


No logs or event data will be collected 
**Authentication and Credential Setup**[](https://docs.zeron.one/integrations/accops-ztna-hysecure#authentication-and-credential-setup)
  * **Creating API Credentials :**
    * **Step 1 -** Log into HySecure Management Console as a Security Officer or Administrator 
    * **Step 2 -** Navigate to Users > Local Users 
    * **Step 3 - Click Add, then fill in :**
      * **User ID -** zeron_api 
      * **Role -** Monitoring User 
      * **Password -** <StrongPassword!123>
    * **Step 4 -** Enable the user and optionally select "Password never expires"


  * **Required Permissions :**
    * **Minimum Role -** Monitoring User 
    * **Required access rights :**
      * View Registered Users 
      * View Active Users/Sessions 


  * **Testing the Credentials :**


Copy```
curl -k -u "zeron_api:StrongPassword!123" https://<HySecure-IP>/monitor/active_users.csv -o active_users.csv
```

  * **Expected -** A downloadable CSV with currently active sessions and endpoint IPs 
  * **Requirements :**
    * HySecure Endpoints
    * Username
    * Password


Last updated 4 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

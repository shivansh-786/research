
# CyberArk Privileged Access Manager (PAM)
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FQPfbdyLrtbE8w5R9rmvH%2Fblobs%2FV9PgE04FkZYDJCZAro0D%2FCyberArk-Logo.png&width=768&dpr=4&quality=100&sign=5f113aa9&sv=2)
CyberArk is a leader in Privileged Access Management (PAM), helping organizations secure, monitor, and manage privileged accounts. Integrating CyberArk with Zeron enhances your security operations by bringing privileged access data into your centralized risk and compliance platform 
**With this integration, you can :**
  * Monitor privileged session activities in real time
  * Automate the collection of audit logs and access history
  * Correlate CyberArk data with other tools in your stack
  * Receive alerts on suspicious or non-compliant behaviour 
  * Improve visibility across your security posture


This guide provides a step-by-step walkthrough to configure the integration for both CyberArk PAM On-Premises and CyberArk Privilege Cloud (SaaS) environments 
**Prerequisites**[](https://docs.zeron.one/integrations/cyberark-privileged-access-manager-pam#prerequisites)
**Before beginning the integration process, please ensure the following :**
**CyberArk Account**
You must have access to a CyberArk environment—either On-Prem or SaaS
**Admin Access**
Ability to create users and assign roles within the CyberArk Password Vault Web Access (PVWA) portal
**Service User**
A dedicated CyberArk user for API authentication and data retrieval
**How to Get Credentials**[](https://docs.zeron.one/integrations/cyberark-privileged-access-manager-pam#how-to-get-credentials)
**For CyberArk Self-Hosted PAM (On-Prem) :**
**Step 1 - Access the CyberArk PVWA**
  * **Open a browser and navigate to :**
https://<PVWA_Server_Address>/PasswordVault
  * Log in using an administrator account


**Step 2 - Create a New User**
  * **Go to :**
Administration → Users → Add User
  * **Fill out required fields :**
    * Username: e.g., zeron_api_user
    * Full Name, Email, etc


**Step 3 - Assign Vault Permissions**
  * **Under Vault Authorization, assign these permissions :**
    * UseAccounts
    * RetrieveAccounts
    * ViewAuditLog
    * AddUpdateUsers (optional, only if needed for managing users)
  * **Group membership :**
    * Add user to groups like PVWAUsers, Vault Admins (based on your security policy)


**Step 4 - Enable API Access**
  * Uncheck “Component User” unless using a machine service account
  * **Under Allowed Interfaces :**
    * Ensure API and CLI are enabled
    * GUI can remain disabled for service accounts


curl -X POST "https://<PVWA_Server_Address>/PasswordVault/API/Auth/CyberArk/Logon" \
-H "Content-Type: application/json" \
-d '{
"username": "zeron_api_user",
"password": "your_password"
}'
curl -X GET "https://<PVWA_Server_Address>/some/protected/endpoint" \
-H "Authorization: Bearer xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
**For CyberArk Privilege Cloud (SaaS) :**
**Step 1 – Log in to Admin Portal :**
  * Access your CyberArk Privilege Cloud admin console with an account that has user management rights


**Step 2 – Create a Service User for Zeron :**
  * **Create a dedicated service account (e.g., zeron_api_user) and assign the following permissions :**
    * **UseAccounts** – allows Zeron to utilize privileged accounts during integration 
    * **RetrieveAccounts** – enables Zeron to securely pull account information
    * **ViewAuditLog** – provides access to audit trails and session logs
    * **ListAccounts** – required for identifying available accounts 
  * Ensure the user is added to the right groups (like PVWAUsers) and scoped with least-privilege access


**Step 3 – Enable API Access :**
  * Ensure API access is allowed for the service user under “Allowed Interfaces”
  * Uncheck “Component User” unless this is a machine account 


**Step 4 – Find Your API Gateway :**
  * CyberArk provides region-specific API URLs (e.g., https://us.privilegecloud.cyberark.com)
  * If unsure, refer to CyberArk documentation or contact your administrator 


**How to Integrate with Zeron**[](https://docs.zeron.one/integrations/cyberark-privileged-access-manager-pam#how-to-integrate-with-zeron)
Once you have your API session token and endpoint, follow these steps within Zeron to complete the integration 
**Step-by-Step integration with Zeron :**
  * **Step 1 - Navigate to Integrations :**
    * Login to your Zeron workspace
    * Go to Others → Management → Integrations
    * Select CyberArk PAM
  * **Step 2 - Choose Environment Type :**
    * Self-Hosted (On-Prem) or Privilege Cloud (SaaS)
  * **Step 3 - Provide Configuration Details :**
    * **CyberArk API Endpoint :**
      * e.g., https://<PVWA_Server_Address>/PasswordVault/
  * **Step 4 - Test Connection :**
    * Zeron will validate the API endpoint 
  * **Step 5 - Save and Activate :**
    * Enable the integration toggle to begin data ingestion
  * **Step 6 - Verification :**
    * Visit the Audit Logs or Data Streams section in Zeron
    * Confirm that CyberArk logs and session data are appearing


**Expected Data After Integration**[](https://docs.zeron.one/integrations/cyberark-privileged-access-manager-pam#expected-data-after-integration)
After successful integration, Zeron continuously pulls and analyzes privileged access data from CyberArk. **The following is a representative overview of the data and insights Zeron will surface post-integration :**
**Data Type**
Description
**Session Recordings**
Full audit trail of session activities
**Privileged Account Logs**
Who accessed which account, when, and how
**Audit Events**
Password changes, vault access logs, policy violations
**User Behavior Metrics**
Frequency, duration, and location of logins
**Security Alerts**
Triggers based on predefined policy breaches
**This information enhances your ability to :**
  * Detect anomalies and insider threats
  * Maintain audit readiness for compliance (e.g., ISO, SOC2, HIPAA)
  * Enforce least-privilege principles
  * Correlate PAM activity with endpoint and network telemetry in Zeron 


**Support & Troubleshooting **[](https://docs.zeron.one/integrations/cyberark-privileged-access-manager-pam#support-and-troubleshooting)
**Common Issues :**
**Issue**
Solution
**Token expired**
Refresh using the Logon API periodically
**API 403/401 Errors**
Verify user roles and allowed interfaces
**Connection failure**
Check endpoint URL, VPN/firewall settings, or proxy requirements
**Missing logs in Zeron**
Confirm correct permissions (ViewAuditLog, RetrieveAccounts) are applied
If you encounter any issues during setup or require further customization, please reach out to our support team at support@zeron.one 
**References** [](https://docs.zeron.one/integrations/cyberark-privileged-access-manager-pam#references)
[CyberArk Documentation Portal](https://www.cyberark.com/documentation/)
Last updated 9 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

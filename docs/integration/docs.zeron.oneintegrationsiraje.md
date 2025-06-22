
# Iraje
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F4211542702-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FQPfbdyLrtbE8w5R9rmvH%252Fuploads%252FwX3lTRaNUuqmM5Ws4Ni4%252Fclient-logo.png%3Falt%3Dmedia%26token%3D81659e0c-777c-48fb-b711-d5f2d3dd43d4&width=768&dpr=4&quality=100&sign=da02c7d1&sv=2)
Integrating Iraje Privileged Access Manager (PAM) with the Zeron platform allows Zeron to fetch critical data from Iraje PAM for unified risk analysis. This integration uses Iraje PAM’s RESTful API interface to pull two key data sets: (a) the list of host systems managed via Iraje PAM, and (b) logs of users logging in through Iraje PAM. The instructions below assume you are using the latest version of Iraje PAM (version 8.2.x as of 2024). (Iraje PAM version 8.2.08 was noted on a recent deployment, and version 9.0 is anticipated soon) 
**Note -** Iraje’s APIs are RESTful but not publicly documented online. You will need to obtain the official API documentation from Iraje’s customer portal or support team. The guidance here is based on available integration information and best practices. Ensure to verify exact API endpoints and parameters from the official Iraje PAM API guide once you have access to it 
**Creating API Credentials for Iraje PAM**[](https://docs.zeron.one/integrations/iraje#creating-api-credentials-for-iraje-pam)
To allow Zeron to access Iraje PAM data, you must create a dedicated API/service account in Iraje PAM for authentication. Using a separate integration user ensures you can control its permissions and track its usage independently. **Follow these steps to create the credentials :**
  * **Step 1 - Log in as Admin -** Sign in to Iraje PAM with a super-administrator or another account that has rights to manage users 
  * **Step 2 - Navigate to User Management -** Go to the Access Control Manager module in the PAM dashboard, then find the Maintain User section and choose Create User. (In Iraje PAM’s UI, user management is often under Access Control or a similar settings area) 
  * **Step 3 - Create a New User -** Enter a username and a strong password for the new integration account. It’s recommended to name it clearly (e.g. “zeron_integration_user”) and disable Multi-Factor Authentication (MFA) for this account if MFA is globally enforced. This is to ensure automated API access isn’t blocked by OTP requirements 
  * **Step 4 - Domain Selection -** If your PAM is integrated with Active Directory or multiple domains, decide whether to create a local PAM user or use an AD account. Creating a local user within Iraje PAM (i.e. under the PAM’s own domain) is often simplest for an API account, as it won’t be subject to external AD password policies or account changes. In the PAM UI’s Domain dropdown, select the local or appropriate domain for this service user. 
  * **Step 5 - Assign Roles and Permissions -** Grant the new user the minimal privileges required to read the needed data. **For this integration, the account needs read access to :**
    * **Host/Asset Inventory -** the list of devices and systems stored in PAM (so it can retrieve host details) 
    * **User Activity Logs -** specifically, the login/session logs of users accessing systems via PAM 
    * **Ensure no excessive permissions are given –** this account should not be able to create or modify users, change configurations, or checkout credentials. Adhering to the principle of least privilege protects your PAM environment. If Iraje PAM provides a built-in “Read-only” or “Auditor” role, use that; otherwise, configure a custom role with view-only access to Reports/Logs and Assets. (For example, allow it to view session logs and device lists, but not initiate sessions or manage accounts) 


  * **Step 6 - MFA/Network Restrictions -** Confirm that the integration user can authenticate using only its username and password via the API. If your PAM enforces IP whitelisting or time-based access for users, make sure the conditions allow Zeron’s connection (e.g. whitelist the IP address of the Zeron connector or cloud service) 


After these steps, you will have the Username and Password for the integration account, which will be used by Zeron to authenticate to Iraje PAM’s API 
**Required Permissions for the API Credentials**[](https://docs.zeron.one/integrations/iraje#required-permissions-for-the-api-credentials)
When configuring the above integration account, ensure it only has permissions necessary for data retrieval and nothing more. **In summary, the account should be limited to read-only access for the relevant data points :**
  * **View Hosts/Devices -** It should be able to list all servers, network devices, databases, and other assets that are onboarded in Iraje PAM. This typically corresponds to viewing entries in the “Access Control Directory” or device inventory. (For instance, Iraje PAM’s Access Control module contains records of each integrated host along with details like IP, hostname, type, etc) 
  * **View User Login/Session Logs -** It should have access to audit logs that show which users logged into Iraje PAM and when, as well as possibly what privileged sessions they initiated. These logs are usually under a reporting or monitoring section (often labeled as Session Logs or Audit Logs in Iraje PAM). The integration account needs to retrieve these records via API 


No write or admin privileges are needed. Do not assign this account the ability to perform sensitive actions like password vault checkout, user management, or configuration changes. The goal is strictly to retrieve data (GET requests) for hosts and user logins. By limiting the role, even if the credentials are compromised, the risk is minimized 
**Best Practice -** Coordinate with your Iraje PAM administrator to create a custom role for “API Integration” that only has view permissions on the “Reports/Logs” and “Devices” modules. This ensures compliance with security policy and avoids violating the principle of least privilege 
**Data to Be Collected from Iraje PAM**[](https://docs.zeron.one/integrations/iraje#data-to-be-collected-from-iraje-pam)
Next, identify the exact data fields Zeron will pull from Iraje PAM. **Two categories of information will be collected :**
  * **Host Details (Managed Systems) :**
    * This is the inventory of all endpoints and devices that are connected to (and managed by) Iraje PAM. **Each host entry typically includes :**
      * **Host Name -** The name or identifier of the system as shown in PAM (often the hostname or an alias) 
      * **IP Address or DNS -** The network address of the host 
      * **Device Type -** Category of asset (e.g. Windows Server, Linux Server, Database, Network Switch, etc.). Iraje supports a variety of device types (servers via RDP/SSH, databases, network devices, etc)
      * **Domain/Group -** If applicable, which domain or grouping the device belongs to (for Windows domain-joined systems, etc) 
      * **Connection Details -** Possibly the protocol/port used (e.g. RDP, SSH, etc.) or any tags. (For instance, when adding a Windows host, PAM records if it’s a domain controller or child server; for network devices, it records if connection is via SSH or Telnet)
      * **Unique ID -** An internal ID or GUID for the device (used by the API for referencing the device) 
    * Zeron will use this host information to understand what assets are being protected by Iraje PAM and to correlate with other security data. Ensure that all relevant host records are included – if your PAM segregates assets by categories or access control lists, the API user must be able to retrieve the full list 


  * **User Login/Session Logs :**
    * These are the audit records of user activity, focusing on logins through the PAM system. Specifically, we are interested in logs that show when a privileged user accesses a system via Iraje PAM. **Key data points in these logs likely include :**
      * Username - The account (often an AD user or local PAM user) that initiated a login through Iraje PAM 
      * **Login Timestamp -** Date and time of the login event. This could include both the time the user logged into the PAM web portal and/or the time they launched a session to a target system 
      * **Source IP (Client IP) -** The IP address from which the user initiated the PAM session (helpful for security auditing) 
      * **Target Host (if applicable) -** If the log is for a session launch, it might record which host or device the user connected to via PAM. For basic “user logged into PAM portal” events, a target may not apply, but for session logs it would (e.g. “User X started a session on Server Y at 10:00 AM”) 
      * **Session ID or Log ID -** An identifier for the event or session, used if further details or video recordings need to be fetched (Iraje PAM records sessions and even allows live viewing, so each session will have an ID) 
      * **Action/Status -** The type of event (e.g., “User Login Success”, “User Login Failed”, “Session Start”, “Session End”) and whether it was successful. Since you might specifically need “users logging in using Iraje PAM”, that likely means successful login events to the PAM system or through it 


These logs give insight into privileged user activity. Zeron will ingest them for real-time monitoring of internal access, complementing external threat data. For instance, integrating these logs into Zeron’s Cyber Risk Posture Management can help detect anomalous behavior (like logins at odd hours or from new locations). Iraje PAM’s own documentation highlights that feeding PAM logs into a SIEM provides comprehensive internal monitoring 
**Note -** Iraje PAM supports sending real-time alerts for certain events (like PAM bypass attempts, sensitive device access, etc.). While this integration primarily fetches logs on demand, ensure that any critical security alerts (if available via the API) are also captured or separately configured if needed. Initially, focusing on login/session logs is a good start 
**Testing the API Credentials**[](https://docs.zeron.one/integrations/iraje#testing-the-api-credentials)
Before configuring Zeron to use the new credentials, it’s important to test that the API access works. This ensures the user account and its permissions are correctly set up. **You can perform a quick test using a tool like cURL or Postman :**
  * **Identify the API Endpoint URL -** Typically, Iraje PAM’s API is accessible at the same host as the web interface. For example, if your PAM web console is at `https://pam.company.com`, the API base URL might be `https://pam.company.com/api/ `(or a specific path like `/rest/` or `/API/`). Check the Iraje documentation for the exact base path. By default, the PAM web runs on HTTPS port 443; if your deployment uses a custom port for the web UI or API, include that. (In one integration example, the host and port were specified as JSON: e.g. `{"host": "pam.company.com", "custom_port": "8443"}` if not using 443) 


  * **Perform an Authentication Call -** Using the integration username and password, attempt to authenticate. **Depending on Iraje’s API design, this could be :**
    * **Basic Auth Test -** Some APIs accept basic HTTP auth. You can try a simple GET request to a trivial endpoint with basic credentials. **For instance :**


Copy```
curl -u "zeron_integration_user:<password>" -k https://pam.company.com/api/status
```

  * **(** Here we assume `/api/status` or similar endpoint returns a basic status or version. Replace with an actual lightweight endpoint from the Iraje API documentation, such as one that fetches the current user’s info or a server time) 
  * If the credentials are correct and the user has access, you should get a 200 OK and some response data. A 401 Unauthorized indicates an auth problem (check username/password and that the account isn’t locked or requiring 2FA) 
  * Token-based Auth Test: If the API requires obtaining a session token (JWT or session ID) via a login endpoint, use the credentials in that specific request. For example, Iraje might have an authentication endpoint like POST https://pam.company.com/api/auth/login with a JSON body containing username and password. **The response would include a token. Use cURL to POST the credentials and see if you receive a token :**


Copy```
curl -X POST https://pam.company.com/api/auth/login \
   -H "Content-Type: application/json" \
   -d '{"username": "zeron_integration_user", "password": "<password>"}'
```

  * (The exact endpoint and JSON schema should come from Iraje’s docs – adjust accordingly) 
  * A successful response typically returns an authentication token or session cookie. Copy that token for the next step
    * **Test Data Retrieval - Once authenticated (either via Basic or with a token), attempt to call one of the target data endpoints :**
      * **For example, test the hosts retrieval :**


Copy```
curl -H "Authorization: Bearer <YOUR_TOKEN_IF_USED>" \
   https://pam.company.com/api/v1/hosts
```

  * **Or if using basic auth and no separate token :**


Copy```
curl -u "zeron_integration_user:<password>" \
   https://pam.company.com/api/v1/hosts
```

  * This should return a JSON list of hosts/devices. Verify that the output contains the fields you expect (names, IPs, etc.) and that it’s not an error. If the list is long, the response might be paginated or truncated (we cover pagination below) 
  * **Similarly, test the user log retrieval :**


Copy```
curl -H "Authorization: Bearer <TOKEN>" \
   "https://pam.company.com/api/v1/logs?type=login&startDate=2025-06-01"
```

  * (The query parameters like `type=login` and `startDate` are hypothetical examples – use actual parameters as defined by Iraje’s API to filter log types or date ranges) 
  * The response should contain log entries. If the account’s permissions are correct, you’ll see events for various users. If the account is too restricted (e.g., only can see its own logs), you might only get that user’s activity – in that case, adjust the role to allow viewing all users’ login events 
  * **Validate Data -** Check a few entries from the responses for accuracy. For instance, pick a host from the JSON and cross-verify its details with what’s shown in the Iraje PAM UI. Likewise, verify that a recent login event appears in the API output and matches the PAM’s audit logs. This ensures the integration user indeed has visibility to all required data 
  * If all tests succeed (valid response data received), the credentials and API endpoints are working. You’re now ready to plug these into Zeron 


**Providing Information to the Zeron Team**[](https://docs.zeron.one/integrations/iraje#providing-information-to-the-zeron-team)
With a functioning integration account and tested endpoints, gather the details that the Zeron team (or the Zeron platform configuration) will need. **Typically, you should prepare the following :**
  * **Iraje PAM Host URL -** The base URL of your Iraje PAM instance. For example, `pam.company.com` (and port if non-standard). Provide the hostname or IP address and confirm the port (default 443 for HTTPS, unless changed). Zeron will use this to know where to connect 
  * **API Credentials -** The username and password of the integration account created for Zeron. Share these through a secure channel. If the API instead uses an API key or token, provide the key/token and any associated ID. (In our case, Iraje uses user credentials; an “API key” concept isn’t explicitly mentioned in public docs. The integration will handle obtaining a token if needed by using these credentials) 
  * **API Endpoint Info -** If applicable, specify the API endpoints or the API module version. For instance, let them know if the integration should use `/api/v1/...` endpoints or if there’s a particular path for the logs. The Zeron team likely has this knowledge for Iraje PAM integration, but it’s good to confirm the version of API (especially if your PAM is a newer major version) 
  * **Iraje PAM Version -** Communicate the version number of Iraje PAM you are running (e.g., 8.2.08 or 8.x). This helps Zeron ensure compatibility. The integration should work for the latest version, but if there are any version-specific quirks (for example, if you were on an older 7.x version), the team should know 
  * **Network Access Details -** Coordinate on how Zeron will connect. If Zeron is delivered as a cloud service, you might need to allow inbound API calls from Zeron’s IP ranges to your PAM (unless you deploy a local Zeron connector). Ensure any firewalls or NAC devices allow the traffic. Provide the Zeron team any required connection info such as a proxy to use, etc., if applicable 
  * **SSL Certificate Requirements -** If your Iraje PAM is using a self-signed SSL certificate (common for internal tools), inform Zeron. They may need a copy of the PAM server’s certificate or its CA to avoid validation issues when connecting. Alternatively, using a valid certificate from a trusted CA on the PAM host is ideal 
  * **Specific Configuration Notes -** Mention any customizations in your Iraje deployment that the integrator should be aware of (for example, if certain logs are turned off, or if you’ve changed default settings like record retention that might affect available data) 


Provide all the above to Zeron’s integration engineer or via the Zeron UI configuration form for Iraje PAM. Once they have the host URL and credentials, they can proceed to configure the data connector on their end. Typically in Zeron’s platform, you (or the team) will input the URL, username, password, and test the connection — since we already did a manual test, it should succeed 
**Additional Notes**[](https://docs.zeron.one/integrations/iraje#additional-notes)
**API Documentation Access -** Since Iraje PAM’s API documentation isn’t public, request the API reference guide from Iraje Support or check if it’s available in your Iraje documentation portal (sometimes the vendor provides PDF guides or an online help section for APIs). This will give the exact endpoints, parameters, and example responses. Having this on hand is valuable for advanced troubleshooting or if you plan to extend the integration (for example, to fetch additional data like password rotation alerts or compliance reports in the future). If unsure how to get it, contact your Iraje account manager or open a support ticket asking for “REST API documentation for Iraje PAM (version X)” 
Last updated 4 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

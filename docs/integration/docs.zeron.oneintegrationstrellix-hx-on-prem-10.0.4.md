
# Trellix HX On-Prem 10.0.4
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F4211542702-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FQPfbdyLrtbE8w5R9rmvH%252Fuploads%252FwPZuTyRaU8lNcvTUXZOa%252Ffeatured-removebg-preview.png%3Falt%3Dmedia%26token%3Dadc9298b-f4f5-4613-8e59-a91fb2c69d5b&width=768&dpr=4&quality=100&sign=e332fa25&sv=2)
This guide provides a detailed, step-by-step process to integrate Trellix HX On-Prem 10.0.4 with Zeron. It is designed for security teams and system administrators seeking centralized visibility into endpoint assets and vulnerabilities using Trellix’s RESTful APIs 
Trellix HX On-Prem provides powerful endpoint detection and response (EDR) features. **With the Zeron integration, customers can :**
  * View Trellix-managed endpoint metadata within Zeron 
  * Monitor active and resolved vulnerabilities via automated polling 
  * Reduce manual triaging through real-time insights 
  * Meet compliance and audit requirements faster with consolidated reporting


By integrating Trellix HX with Zeron, organizations can automate data ingestion, improve vulnerability tracking, and streamline incident response — all without manual intervention 
**Prerequisites**[](https://docs.zeron.one/integrations/trellix-hx-on-prem-10.0.4#prerequisites)
**Please ensure the following prerequisites are met before starting the integration process :**
Requirement
Description
**Trellix HX Version**
Must be version 10.0.4 (On-Prem)
**API User Role**
Trellix user account with api_analyst (recommended) or api_admin role
**Audits Module Enabled**
Required for vulnerability data collection
**API Documentation Module**
Should be active in Trellix if API calls are failing unexpectedly
**How to Obtain API Credentials**[](https://docs.zeron.one/integrations/trellix-hx-on-prem-10.0.4#how-to-obtain-api-credentials)
**Create an API User in Trellix HX :**
  * Log in to the Trellix HX Web Console with admin privileges
  * Navigate to Admin > User Accounts
  * **Click Add New User and fill in :**
    * **Username -** e.g., zeron_api_user
    * **Password -** Secure and complex password
    * **Role - Choose one :**
**Role**
**Access Scope**
**Recommended For**
**api_analyst**
Read-only API access
General integrations 
**api_admin**
Full API access
Only if actions are required
  * Click Save 


**Integration Setup in Zeron**[](https://docs.zeron.one/integrations/trellix-hx-on-prem-10.0.4#integration-setup-in-zeron)
**Configure Zeron :**
  * **In the Zeron platform :**
    * Go to Others → Management → Integrations → Trellix HX
    * **Provide the following :**
**Field**
**Value/Description**
**API Base URL**
https://<HX_Server>:3000/hx/api/v3/
**API Token**
Paste the token obtained earlier
**Polling Interval**
e.g., every 60 minutes
    * Save and activate the integration 


**Data Pulled into Zeron**[](https://docs.zeron.one/integrations/trellix-hx-on-prem-10.0.4#data-pulled-into-zeron)
  * #### 
[](https://docs.zeron.one/integrations/trellix-hx-on-prem-10.0.4#host-metadata)
Host Metadata : 


**Field**
**Use in Zeron**
**Hostname**
Asset Inventory / Search
**IP Address**
Network mapping and policy checks
**OS**
Compliance grouping
**Agent Version**
Agent health / update monitoring
**Status**
Online / Contained / Offline indicators
  * #### 
[](https://docs.zeron.one/integrations/trellix-hx-on-prem-10.0.4#vulnerability-data)
Vulnerability Data : 


**Field**
**Use in Zeron**
**CVE ID**
Risk scoring and patch prioritization
**Severity**
Alert filtering and incident response
**Description**
Analyst context
**Status**
Tracks remediation progress
**First Seen / Solved**
Timeline-based reports
**Support & Troubleshooting **[](https://docs.zeron.one/integrations/trellix-hx-on-prem-10.0.4#support-and-troubleshooting)
  * #### 
[](https://docs.zeron.one/integrations/trellix-hx-on-prem-10.0.4#common-issues-and-fixes)
Common Issues & Fixes : 


**Symptom / Code**
**Root Cause**
**Recommended Fix**
**401 Unauthorized**
Invalid or expired token
Regenerate token using valid credentials
**403 Forbidden**
Insufficient user permissions
Assign api_analyst or api_admin role
**1101 Error**
API role not assigned
Confirm API role in Trellix console
**Timeout/Connection refused**
Port 3000 not open or DNS issue
Check firewall/DNS settings
**No hosts or audit data**
Audits not run or hosts not reporting
Run audits; check agent check-ins
If you encounter any issues during setup or require further customization, please reach out to our support team at support@zeron.one 
**References** [](https://docs.zeron.one/integrations/trellix-hx-on-prem-10.0.4#references)
<https://docs.trellix.com/>
Last updated 9 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

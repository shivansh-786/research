
# CloudFlare
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F4211542702-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FQPfbdyLrtbE8w5R9rmvH%252Fuploads%252Fp835KLnyZ7Kt9Ydzytp6%252Fimages-removebg-preview.png%3Falt%3Dmedia%26token%3D92ae9b98-f9d8-4c8f-9abf-2b037788f4f2&width=768&dpr=4&quality=100&sign=ae6e0e1f&sv=2)
This document provides step-by-step instructions for Zeron customers to integrate their Cloudflare account with the Zeron platform. The purpose of this integration is to provide visibility into protected domains, subdomains, and IPsthat are managed through Cloudflare 
The integration relies on read-only access to Cloudflare data via an API Token created in your Cloudflare dashboard. All actions are non-invasive and do not change any settings on your Cloudflare account 
**Prerequisites** [](https://docs.zeron.one/integrations/cloudflare#prerequisites)
**To complete this integration, ensure the following prerequisites are met :**
  * You must have an active Cloudflare account 
  * You must have access to the Cloudflare Dashboard 
  * You need to be able to generate a custom API Token with read-only permissions 
  * You should know or be able to locate your Cloudflare Account ID and Zone ID(s) for the domains you want to integrate


**Credentials Required**[](https://docs.zeron.one/integrations/cloudflare#credentials-required)
**Please prepare and securely share the following credentials with the Zeron team to enable the integration :**
**Credential**
**Purpose**
**Cloudflare Account ID**
Identifies your Cloudflare account globally
**Cloudflare Zone ID(s)**
Identifies each specific domain within your account
**Cloudflare API Token**
Authorizes Zeron to access data (read-only scope)
**Step-by-Step - How to Generate API Credentials**[](https://docs.zeron.one/integrations/cloudflare#step-by-step-how-to-generate-api-credentials)
**The Steps to generate API Credentials are as follows :**
  * **Step 1 - Log in to Cloudflare Dashboard :**
    * **Navigate to :**
      * <https://dash.cloudflare.com/>
  * **Step 2 - Go to API Token Section :**
    * **Once logged in, go to :**
      * My Profile > API Tokens > Create Token 
  * **Step 3 - Create Custom Token :**
    * Click on Create Custom Token
    * Set the Token Name as Zeron Integration - Read Only
  * **Step 4 - Assign the Following Permissions :**


**Category**
**Permission**
**Access**
Zone
Zone
Read
Zone
DNS
Read
  * **Step 5 - Select the Resources :**
    * **You can either :**
      * Select All Zones (recommended if you wish to integrate all domains), or 
      * Select specific domains you want Zeron to monitor 
  * **Step 6 - Finalize and Create the Token :**
    * Click Continue to Summary 
    * Click Create Token 
    * Immediately copy the generated API token. It will not be shown again later 
  * **Step 7 - Share the Credentials with Zeron :**
    * **Provide the following securely to Zeron :**
      * API Token
      * Account ID
      * Zone ID(s)


**Integration Setup in Zeron**[](https://docs.zeron.one/integrations/cloudflare#integration-setup-in-zeron)
**Configure Zeron :**
  * **In the Zeron platform :**
    * Go to Others → Management → Integrations → Cloudflare 
    * **Provide the following :**
      * Cloudflare Account ID
      * Cloudflare Zone ID(s)
      * Cloudflare API Token
    * Save and activate the integration 


**Expected Data After Integration**[](https://docs.zeron.one/integrations/cloudflare#expected-data-after-integration)
**Once the integration is complete, Zeron will receive read-only visibility into :**
  * Protected domains registered under your Cloudflare account
  * Subdomains associated with each domain
  * IP addresses linked to your DNS records
  * DNS record configurations


All of this data is accessed securely through the permissions defined in the API Token and used to enhance Zeron’s monitoring capabilities 
**References** [](https://docs.zeron.one/integrations/cloudflare#references)
Last updated 9 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject


# Elastic SIEM
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F4211542702-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FQPfbdyLrtbE8w5R9rmvH%252Fuploads%252FWYX71b5BHMaVi7th5pa6%252Felastic-logo-removebg-preview.png%3Falt%3Dmedia%26token%3Dd319f750-af6a-49f8-9edc-02c34e91a4c3&width=768&dpr=4&quality=100&sign=96b010d7&sv=2)
This document guides you through integrating Elastic Security (Elastic SIEM) version 8.18 with the Zeron CRPM platform. This integration leverages the Kibana Endpoint Metadata API to pull rich endpoint metadata for enhanced visibility and risk posture analytics within Zeron 
With this integration, organizations gain centralized insights into endpoint health, agent versions, host details, and connectivity status, enabling timely and informed security decisions 
**Prerequisites**[](https://docs.zeron.one/integrations/elastic-siem#prerequisites)
**To successfully integrate Elastic SIEM with Zeron CRPM, ensure the following components and permissions are in place :**
**Component**
**Requirement**
**Elastic SIEM**
Version 8.18 (Elastic Cloud or Self-managed)
**API Endpoint**
/api/endpoint/metadata via Kibana
**Kibana Access**
Access to Kibana URL and appropriate space ID
**Authentication**
API Key (preferred) or Basic Authentication
**Required Kibana Privileges**
Read access to .fleet-agents*, .security-endpoint*, and metrics-endpoint.metadata-*Access to Kibana Security App
**How to Get Credentials**[](https://docs.zeron.one/integrations/elastic-siem#how-to-get-credentials)
Zeron supports both API Key-based authentication (preferred for automation and security) and Basic Auth 
#### 
[](https://docs.zeron.one/integrations/elastic-siem#create-api-key)
Create API Key : 
  * **Your Kibana user account must have :**
    * Permission to manage API keys
    * **Permission to read from :**
      * .fleet-agents* 
      * .security-endpoint* 
      * metrics-endpoint.metadata-* 
    * Access to the Security app within Kibana 
  * **Steps to Generate API Key :**
    * **Step 1 -** Log in to Kibana with a superuser or custom privileged role 
    * **Step 2 -Navigate to :**
      * Management → Stack Management → API Keys
    * **Step 3 -** Click Create API Key 
    * **Step 4 -** Provide a meaningful name (e.g., zeron-crpm-integration) 
    * **Step 5 -Assign appropriate role :**
      * Use superuser, OR
      * **A custom role with :**
        * Read access to the required indices
        * Kibana application access
    * **Step 6 -** Click Create 
    * **Step 7 -** Copy the Base64-encoded API key displayed and store it securely 
    * Always use HTTPS for secure transmission


#### 
[](https://docs.zeron.one/integrations/elastic-siem#use-basic-authentication)
Use Basic Authentication : 
  * **If API key generation is restricted or unsupported, use username/password credentials :**
    * curl -X GET "https://:5601/api/endpoint/metadata?hostStatuses=healthy" -u ":" -H "kbn-xsrf: true"
  * Use only with secured HTTPS endpoints, and ensure the user has the same permissions as API Key-based access


**Integration Steps in Zeron CRPM**[](https://docs.zeron.one/integrations/elastic-siem#integration-steps-in-zeron-crpm)
**Once credentials are ready, follow these steps to establish a secure integration :**
  * **Step 1 -** Log in to Zeron CRPM 
  * **Step 2 -** Navigate to Others → Management → Integrations 
  * **Step 3 -** Select Elastic SIEM 
  * **Step 4 - Provide :**
    * Kibana URL (e.g., https://kibana.mycompany.com:5601)
    * Kibana Space ID (e.g., /s/default)
    * Authentication credentials (API Key or Username/Password)
    * Host statuses to fetch (e.g., healthy, offline, updating) 
  * **Step 5 -** Save and test the connection
  * **Step 6 -** If successful, endpoint metadata will begin flowing into the Zeron dashboard 


**Expected Data After Integration**[](https://docs.zeron.one/integrations/elastic-siem#expected-data-after-integration)
**Zeron CRPM extracts key host metadata from Elastic SIEM’s API for posture and risk evaluation :**
**Field**
**Description**
**host.id**
Unique host identifier
**host.hostname / host.name**
Hostname of the endpoint
**host.ip**
List of associated IP addresses (Zeron selects primary)
**host.status**
Agent status (e.g., healthy, offline, updating)
**metadata.agent.version**
Version of the deployed Elastic Agent
**metadata.agent.id**
Unique identifier of the Elastic Agent
**Support and Troubleshooting**[](https://docs.zeron.one/integrations/elastic-siem#support-and-troubleshooting)
**If you encounter issues during or after integration, use the table below to identify and resolve common problems :**
**Symptom**
**Cause**
**Recommended Resolution**
**401 Unauthorized**
API Key expired or invalid
Regenerate API Key from Kibana and reconfigure Zeron
**No data in Zeron**
Incorrect permissions or API filters
Check assigned roles and hostStatuses parameters
**403 Forbidden**
Role lacks index or API privileges
Use superuser or correct custom role
**Timeout or failed API response**
Network latency or Kibana overload
Verify network health; increase timeout; retry after delay
**Authentication success but no data**
Endpoint agents not reporting
Confirm Elastic agents are healthy and reporting metadata
If you encounter any issues during setup or require further customization, please reach out to our support team at support@zeron.one 
**References** [](https://docs.zeron.one/integrations/elastic-siem#references)
Last updated 9 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

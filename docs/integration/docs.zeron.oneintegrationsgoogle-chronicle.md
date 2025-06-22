
# Google Chronicle
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F4211542702-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FQPfbdyLrtbE8w5R9rmvH%252Fuploads%252FBJj6PBbCgpMZd4lAUXjG%252FChronicle_Logo.webp%3Falt%3Dmedia%26token%3D3c0f8727-1d0b-4405-b377-d758fc00d28a&width=768&dpr=4&quality=100&sign=95900756&sv=2)
**This document guides you through integrating Google Chronicle (Google Security Operations) with ZERON to collect :**
  * Host details protected by Chronicle 
  * All log sources reporting to Chronicle 

**How to Create Credentials for API Authentication**[](https://docs.zeron.one/integrations/google-chronicle#how-to-create-credentials-for-api-authentication)
To enable ZERON to fetch data from Chronicle, you must create a Google Cloud Service Account and share the credentials securely. **Steps :**
  * **Step 1 -** Go to Google Cloud Console 
  * **Step 2 -** Navigate to IAM & Admin → Service Accounts → Create Service Account 
  * **Step 3 -** Provide a name like zeron-chronicle-integration 
  * **Step 4 -** Click Create and Continue 
  * **Step 5 - Assign only the following role :**
    * Chronicle API Viewer (roles/chronicle.viewer) 
  * **Step 6 -** Click Done 
  * **Step 7 -** Go to the newly created service account → Keys tab → Add Key → Create New Key 
  * **Step 8 -** Select JSON format → Download the key 
  * **Step 9 -** Share this JSON file securely with the ZERON team


**Permissions Required on the Credentials**[](https://docs.zeron.one/integrations/google-chronicle#permissions-required-on-the-credentials)
**Only assign the read-only permissions required to fetch host and log source details :**
**Permission**
**Description**
**chronicle.feeds.list**
View cloud/API-based data feeds
**chronicle.forwarders.list**
View on-premise forwarders (agents)
**chronicle.collectors.list**
View collectors configured under forwarders
**chronicle.assets.list**
View asset (host) metadata seen by Chronicle
Use Chronicle API Viewer (roles/chronicle.viewer) to cover all these 
**What Data Will Be Collected by ZERON**[](https://docs.zeron.one/integrations/google-chronicle#what-data-will-be-collected-by-zeron)
**ZERON will collect the following from Chronicle :**
**Data Type**
**Source**
**Description**
**Host Details**
Chronicle Assets
Hostnames, IPs, asset metadata (seen in logs)
**Log Sources**
Feeds
External sources pushing logs (e.g., GCP, Azure, etc.)
Forwarders
On-premise agents forwarding logs to Chronicle
Collectors
Specific collectors configured under each forwarder
**How to Test the Credentials**[](https://docs.zeron.one/integrations/google-chronicle#how-to-test-the-credentials)
  * **Step 1 -** Install Google Cloud SDK: bash


`gcloud auth activate-service-account --key-file=zeron-chronicle.jsongcloud auth print-access-token`
  * **Step 2 -** Use this token in a test curl: bash


`curl -H "Authorization: Bearer <access_token>" \ "https://chronicle.googleapis.com/v1alpha/projects/<project_id>/locations/<region>/instances/<instance_id>/feeds"`
You should get a JSON response with feed details. If `403 Forbidden`, check assigned permissions
**What to Share with ZERON Team**[](https://docs.zeron.one/integrations/google-chronicle#what-to-share-with-zeron-team)
**To enable integration, share the following with the ZERON onboarding/security team :**
**Item**
**Description**
**Service Account JSON File**
Credential to authenticate API access
**Chronicle Project ID**
Found in GCP dashboard
**Chronicle Instance ID**
Typically shared during Chronicle setup
**Chronicle Region**
**Example -**`us` , `europe-west1`, etc.
Last updated 4 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

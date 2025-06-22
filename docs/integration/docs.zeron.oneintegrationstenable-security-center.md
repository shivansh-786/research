
# Tenable Security Center
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F4211542702-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FQPfbdyLrtbE8w5R9rmvH%252Fuploads%252FQMdoSa8VoePNeuwNOeRC%252Fimages-2-removebg-preview.png%3Falt%3Dmedia%26token%3D768c1da7-e3b5-433a-a8ab-2d6ba6d71a20&width=768&dpr=4&quality=100&sign=4031b603&sv=2)
Zeron integrates with Tenable Security Center version 6.6 by accessing vulnerability and asset information using API-based communication. To establish this integration, Zeron requires Read-Only API credentials from your Tenable Security Center instance 
The information below will guide you step-by-step on how to generate the necessary API credentials and what information will be accessed by Zeron after integration 
**Prerequisites** [](https://docs.zeron.one/integrations/tenable-security-center#prerequisites)
**Before beginning the integration process, ensure that the following conditions are met :**
**Item**
**Requirement**
**Tenable Version**
Tenable Security Center v6.6
**User Role**
Administrator or Organizational User with appropriate permissions
**Interface Access**
Access to the Tenable Security Center User Interface
**Permission Settings**
User must have permissions to access the API and generate API keys
**Authentication Mode**
API Key Authentication must be enabled before key generation
**Secure Sharing**
API credentials must be securely shared with the Zeron team
**How to Get Credentials**[](https://docs.zeron.one/integrations/tenable-security-center#how-to-get-credentials)
**The credential setup process is divided into two parts :**
  * **Step 1 - Enable API Key Authentication :**
    * This step allows users to authenticate API requests using API keys 
    * **Required Role :**
      * Administrator
      * Organizational User with the required permissions
    * **Steps to Enable API Key Authentication :**
      * **Step 1 -** Log in to the Tenable Security Center user interface
      * **Step 2 -** From the left-hand menu, click System > Configuration
      * **Step 3 -** The Configuration page will appear
      * **Step 4 -** Click on the Security tile to open Security Configuration
      * **Step 5 -** In the Authentication Settings section, toggle Allow API Keys to Enabled 
      * **Step 6 -** Click Submit to save the settings 
    * **Note -** Once submitted, API Key Authentication will be enabled in your Tenable instance
  * **Step 2 - Generate API Keys :**
    * API Keys allow Zeron to authenticate and fetch vulnerability and asset data for integration 
    * **Important Notes :**
      * Only users with proper roles can generate API keys 
      * If API keys are regenerated, previous keys become invalid 
      * API Secret Key is only visible once during creation 
    * **Required Roles :**
      * Administrator 
      * Organizational User with same role permissions 
    * **Steps to Generate API Keys :**
      * **Step 1 -** Log in to Tenable Security Center
      * **Step 2 -** Navigate to Users > Users 
      * **Step 3 -** Locate the user for whom the API key needs to be created 
      * **Step 4 - Perform either of the following :**
        * Right-click on the user’s row and click API Keys > Generate API Key, or 
        * Select the checkbox for the user, then click API Keys > Generate API Key from the top menu 
      * **Step 5 -** A confirmation dialog will appear. Click Generate 
      * **Step 6 - The Your API Key window will appear, displaying :**
        * Access Key
        * Secret Key
      * **Step 7 - Securely save the API keys :**
        * _The Secret Key will not be viewable again_
    * **Important Reminder :**
      * If you lose the secret key, you will need to generate new API keys 
      * API requests made with old keys will be deauthorized upon generation of new keys or deletion of existing ones 


**Integration with Zeron**[](https://docs.zeron.one/integrations/tenable-security-center#integration-with-zeron)
**Once the API Access Key and Secret Key have been securely shared, Zeron will use the following API endpoints from Tenable Security Center to fetch required data :**
**Data Type**
**HTTP Method**
**API Endpoint**
**Vulnerabilities**
POST
/rest/analysis{parameters}
**Assets**
GET
/rest/asset?filter=filter,...&fields=field,...
Zeron will utilize these endpoints to extract the relevant data for integration and display it within its own interface for analysis and reporting 
**Expected Data After Integration**[](https://docs.zeron.one/integrations/tenable-security-center#expected-data-after-integration)
**Once integration is completed, Zeron will have access to the following datasets from Tenable Security Center :**
**Data Fetched**
**Description**
**Vulnerabilities**
Data retrieved using the POST /rest/analysis{parameters} endpoint, containing vulnerability information based on specified filters and parameters.
**Assets**
Data fetched via the GET /rest/asset endpoint, which includes asset details filtered and structured through API query parameters.
This enables Zeron to provide a consolidated view of your security posture by aligning asset and vulnerability data within its ecosystem 
**References** [](https://docs.zeron.one/integrations/tenable-security-center#references)
[Enable API Keys](https://docs.tenable.com/security-center/Content/EnableAPIKeys.htm)
[Generate API Key](https://docs.tenable.com/security-center/Content/GenerateAPIKey.htm)
[User Roles](https://docs.tenable.com/security-center/Content/UserRoles.htm)
[API Key Authentication](https://docs.tenable.com/security-center/Content/APIKeyAuthentication.htm)
[Retrieve Vulnerability Data](https://docs.tenable.com/security-center/best-practices/api/Content/RetrieveVulnerabilityDataForSpecificTimeRange.htm)
[Retrieve Asset Data](https://docs.tenable.com/security-center/best-practices/api/Content/RetrieveAssetDataFromSC.htm)
[API Key Authorization Guide](https://docs.tenable.com/security-center/best-practices/api/Content/APIKeyAuthorization.htm)
Last updated 9 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

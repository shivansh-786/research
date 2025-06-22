
# Microsoft Defender for Endpoint (MDE)/Cloud
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2Fcontent.gitbook.com%2Fcontent%2FQPfbdyLrtbE8w5R9rmvH%2Fblobs%2FEt1dmPI7VxvXLQjpBp0q%2Fmicrosoft-defender-antivirus-endpoint-security-solutions-removebg-preview.png&width=768&dpr=4&quality=100&sign=85011a50&sv=2)
This guide outlines the integration process between Microsoft Defender (either Microsoft Defender for Endpoint or Microsoft Defender for Cloud) and Zeron. The integration enables Zeron to retrieve relevant security and vulnerability data from Microsoft Defender using authorized APIs through Microsoft Entra ID (formerly Azure Active Directory) 
The document is focused on reducing operational overhead by clearly guiding the user through credential generation and setup necessary for integration within the Zeron platform 
**Prerequisites** [](https://docs.zeron.one/integrations/microsoft-defender-for-endpoint-mde-cloud#prerequisites)
**Before initiating the integration, ensure the following components and permissions are in place :**
**Component**
**Requirement**
**Microsoft Defender Subscription**
Active subscription to either:– Microsoft Defender for Endpoint– Microsoft Defender for Cloud
**Microsoft Entra ID Access**
Administrative access to Microsoft Entra ID (formerly Azure Active Directory) for application registration and permission configuration
**Appropriate Permissions**
Admin privileges to register and configure applications within the organization’s Entra ID
**How to Get Credentials**[](https://docs.zeron.one/integrations/microsoft-defender-for-endpoint-mde-cloud#how-to-get-credentials)
**To enable integration with Zeron, you’ll need the following credentials from Microsoft Entra :**
  * Application (Client) ID 
  * Directory (Tenant) ID
  * Client Secret


These are obtained by registering a new application and configuring the necessary permissions 
**Register a New Application :**
  * **Step 1 - Access Microsoft Entra Admin Center :**
    * **Navigate to -** [https://entra.microsoft.com](https://entra.microsoft.com/)
    * Sign in using your administrator credentials
  * **Step 2 - Register the Application :**
    * From the left-hand navigation pane, select “App registrations” 
    * Click “New registration” 
    * **In the registration form :**
      * **Name -** e.g., Defender Integration App
      * **Supported account types -** Select _“Accounts in this organizational directory only”_
      * **Redirect URI -** Optional – can be left blank if not applicable
    * Click “Register” 
  * **Step 3 - Record the Application Details :**
    * **After successful registration, from the Application Overview page, note down :**
      * Application (client) ID
      * Directory (tenant) ID 


**Assign API Permissions :**
  * **Step 1 - Open the API Permissions Page :**
    * Within the registered application, navigate to “API permissions” on the left panel 
  * **Step 2 - Add Permissions :**
    * Click “Add a permission”
    * Choose “APIs my organization uses”
    * **Search and select the appropriate API based on your Defender product :**
      * **For Defender for Endpoint -** Select WindowsDefenderATP
      * **For Defender for Cloud -** Select Azure Security Center
  * **Step 3 - Select Required Permissions :**
    * **Below are the commonly required permissions based on integration needs :**
**Microsoft Defender Product**
**Permission Scope**
**Description**
**Defender for Endpoint**
Machine.Read.All
Grants read access to all machine-related information, such as device inventory and status.
**Defender for Endpoint**
Vulnerability.Read.All
Grants access to vulnerability data from Threat & Vulnerability Management (TVM).


**Create a Client Secret :**
  * **Step 1 - Navigate to Certificates & Secrets : **
    * In the application menu, go to “Certificates & secrets” 
  * **Step 2 - Generate a New Client Secret :**
    * Click on “New client secret”
    * **Fill in :**
      * **Description -** e.g., Defender API Secret
      * **Expiration -** Choose based on your organization’s policy
      * Click “Add”
  * **Step 3 - Save the Secret Value :**
    * Immediately copy and securely store the client secret value


**How to Integrate with Zeron**[](https://docs.zeron.one/integrations/microsoft-defender-for-endpoint-mde-cloud#how-to-integrate-with-zeron)
Once the Client ID, Tenant ID, and Client Secret are ready, use them in Zeron’s integration portal. **While the PDF does not provide step-by-step Zeron UI instructions, based on standard practice, the integration process typically includes :**
  * **In the Zeron platform :**
    * Go to Others → Management → Integrations → Microsoft Defender
    * **Provide the following :**
      * Client ID
      * Tenant ID
      * Client Secret 
    * **Choosing the Defender product type -** Endpoint or Cloud
    * Saving and testing the connection


**Expected Data After Integration**[](https://docs.zeron.one/integrations/microsoft-defender-for-endpoint-mde-cloud#expected-data-after-integration)
**Once the integration is active, Zeron will begin retrieving and using the following data based on the Defender product integrated :**
**Defender Type**
**Data Fetched**
**Defender for Endpoint**
Machine metadata, Discovered vulnerabilities from Threat & Vulnerability Management
**Defender for Cloud**
Security posture information, Cloud-specific vulnerability data
**References** [](https://docs.zeron.one/integrations/microsoft-defender-for-endpoint-mde-cloud#references)
Last updated 9 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

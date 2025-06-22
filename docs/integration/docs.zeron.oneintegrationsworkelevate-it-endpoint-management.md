
# Workelevate IT Endpoint Management
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F4211542702-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FQPfbdyLrtbE8w5R9rmvH%252Fuploads%252FaxWac9ozywiozZk02rUH%252Fwe-black-logo.png%3Falt%3Dmedia%26token%3Ddf5084c1-99c8-4aa8-81af-1b063210755f&width=768&dpr=4&quality=100&sign=2cda6621&sv=2)
Integrating Workelevate IT Endpoint Management with the Zeron cyber risk platform allows Zeron to fetch detailed host inventory data from Workelevate. Workelevate provides open APIs for integration, so Zeron can pull information about all endpoints (hosts) managed by Workelevate. This guide covers how to set up credentials, the permissions and data involved, and the steps to configure and test the integration. It also details the API endpoints, authentication process, pagination handling, and example cURL requests for fetching host details. The integration is read-only, meaning Zeron will only retrieve data from Workelevate and not modify anything on Workelevate’s side 
**Creating API Credentials in Workelevate**[](https://docs.zeron.one/integrations/workelevate-it-endpoint-management#creating-api-credentials-in-workelevate)
Before Zeron can access Workelevate’s API, you need to create API access credentials in the Workelevate platform. **Typically, this involves generating an API token or creating a service account with the proper permissions :**
  * **API Token (Preferred) -** Many modern platforms allow administrators to generate an API token (or API key) for integration. Check Workelevate’s admin console or settings for an “API Access” or “Integrations” section. If available, generate a new API token for Zeron integration. Workelevate is designed to be easy to connect via open APIs, so it likely supports issuing API keys or tokens for external tools 
  * **Service Account User -** If a direct API token option is not provided, create a dedicated service account (a user account meant for integrations) in Workelevate. This account will be used by Zeron to authenticate. Use a strong password and note the username/email and password for API use. In some cases, Workelevate might support authenticating via basic HTTP auth using this account, or using it to obtain a bearer token (more on authentication in a later section) 
  * **OAuth 2.0 / JWT (If supported) -** If Workelevate’s documentation indicates support for OAuth 2.0 or JWT-based auth, you may need to register an API client (with client ID/secret) in Workelevate. This would allow Zeron to obtain an OAuth token to access the APIs. This is less common for custom integrations, but worth checking if available. If provided, follow Workelevate’s steps to create an OAuth client and get the client ID and secret 


**Note -** As of now, Workelevate’s public API documentation or base URL is not readily discoverable online (it’s likely provided privately to customers). You may need to request the API documentation or base endpoint URL from Workelevate support or your implementation team. For example, the API base URL could be something like `https://api.workelevate.com/v1 `or a tenant-specific domain (e.g., `https://yourcompany.workelevate.com/api/v1`). Ensure you have this base URL from the Workelevate team or documentation to configure the integration 
**Permissions Required for the API Credentials**[](https://docs.zeron.one/integrations/workelevate-it-endpoint-management#permissions-required-for-the-api-credentials)
When creating the above credentials (token or service account), assign the minimum necessary permissions to adhere to the principle of least privilege. The integration only needs to read host data, so the credentials should only have read access to endpoint information and not broader administrative rights if possible. **Specifically :**
  * **Endpoint/Asset Read Access -** The account or token should be permitted to retrieve endpoint inventory data. In Workelevate, this may correspond to a role like Endpoint Management Viewer, Asset Read-Only, or similar. If Workelevate uses role-based access control (RBAC), ensure the role grants visibility into device lists and their details 
  * **No Write or Admin Privileges -** Do not give the integration credentials permissions to create, modify, or delete data in Workelevate. Zeron only needs to fetch data (read-only integration). Removing unnecessary privileges reduces security risks 
  * **Limited Scope -** If Workelevate API tokens support scoping, request a token scoped only to the required endpoints (e.g., a scope for read:devices or read:endpoints). This ensures the API can only access the host information and nothing else 
  * **Account Use -** Do not use a personal admin account for integration. Always use a dedicated integration account/token so its permissions can be tightly controlled and monitored. This also allows you to revoke or rotate credentials without affecting any human users 


By granting only the minimum access needed, you protect both systems and follow best practices for API security. If unsure about the exact permission name, consult Workelevate’s documentation or support to identify a read-only role for endpoint data 
**Data to be Collected from Workelevate (Host Details)**[](https://docs.zeron.one/integrations/workelevate-it-endpoint-management#data-to-be-collected-from-workelevate-host-details)
The goal of this integration is to collect host details from Workelevate’s endpoint management module, so that Zeron can use this data for cyber risk analysis and inventory tracking. Workelevate’s agent and platform provide detailed hardware and software information for each managed endpoint. **The integration should fetch all relevant host attributes, which typically include :**
  * **Host Identification -** Hostname (device name), unique device ID or GUID as used in Workelevate, and possibly the asset tag or serial number 
  * **Network Details -** IP address(es) of the device, MAC address, and last known network location (if available) 
  * **Operating System -** OS name (e.g., Windows, macOS, Linux) and version/build number. This may also include OS edition and patch level 
  * **Hardware Specifications -** CPU type, RAM size, disk capacity, and other hardware details that Workelevate collects (e.g., model, manufacturer). Workelevate’s agent can retrieve detailed hardware data from each node 
  * **User Information -** The username of the last logged-in user or the primary user of the device (if Workelevate tracks device assignment) 
  * **Status and Activity -** Last check-in or last seen timestamp (when the device last reported to Workelevate), device online/offline status, and possibly uptime or last reboot time 
  * **Security Posture -** If available via Workelevate, whether endpoint protection is enabled. For example, antivirus status (installed/running, definitions updated), firewall status, disk encryption status, or compliance state. Since Workelevate is a unified endpoint management tool, it might have insight into some security settings or whether the device is compliant with policies 
  * **Installed Software/Patches -** A list of key software installed or recent patch status could be available. However, pulling full software lists might be beyond “host details” and could be a separate endpoint. Primarily, the focus is on inventory data for the device itself 
  * **Asset Metadata -** Any tags, organizational units, or groups the device belongs to (for instance, location, department, or device category), if those are recorded in Workelevate 


Ensure that the integration captures all fields that Zeron requires for its risk assessments. “All related to host” essentially means the full asset inventory record for each device. It’s better to fetch more details and let Zeron decide which to use, than to miss critical attributes. If Workelevate’s API offers a specific endpoint for host inventory export, that may bundle many of these details in one response. Otherwise, you might have to gather them from multiple endpoints (for example, one for basic device info and another for installed security software). Start with the primary host details endpoint, and expand if needed 
**Note -** Without a sample response from Workelevate’s API, the exact field names and structure can’t be shown here. **But typically, a device object in JSON might look like :**
Copy```
{
 "deviceId": "12345",
 "hostname": "HOST-001",
 "os": "Windows 11 Pro",
 "osVersion": "10.0.22621",
 "ipAddress": "10.0.5.12",
 "macAddress": "00-1A-2B-3C-4D-5E",
 "lastUser": "jdoe",
 "lastSeen": "2025-06-10T14:30:00Z",
 "status": "online",
 "cpu": "Intel Core i7-8665U",
 "ramGB": 16,
 "diskGB": 512,
 "antivirus": "Enabled (Windows Defender)",
 "firewall": "Enabled",
 "bitlocker": "Enabled",
 "assetTag": "IT-1001",
 "location": "Headquarters",
 "department": "Engineering"
}

```

This is an illustrative example. The actual JSON fields and structure will depend on Workelevate’s API. Consult the Workelevate API documentation for the precise schema of the host details 
**Testing the API Credentials**[](https://docs.zeron.one/integrations/workelevate-it-endpoint-management#testing-the-api-credentials)
Once you have the API base URL and credentials set up, it’s important to test the connection before configuring Zeron. This ensures that the credentials are correct and have the right permissions, and that you can successfully retrieve data. **Here’s how to test the Workelevate API access :**
  * **Step 1 - Use a REST client or cURL -** A simple way to test is by using a tool like Postman or the command-line tool cURL. Make sure you have the base URL for the Workelevate API (e.g., `https://api.workelevate.com/v1 `or whichever URL applies to your environment) 
  * **Step 2 - Authentication Test -** If you need to obtain a token first (for example, via an auth endpoint), try that request first. **For instance, using cURL :**


Copy```
# Example: obtaining a token (if using username/password authentication)
curl -X POST "https://api.workelevate.com/v1/auth/login" \
   -H "Content-Type: application/json" \
   -d '{"username": "api_service_account", "password": "YourPassword"}'
```

  * This is a hypothetical endpoint (`/auth/login`); the actual path may differ (it could be `/api/v1/token` or an OAuth token URL). If correct, the response should include an authentication token (e.g., JWT or API token string). Copy this token for the next step 
  * **Step 3 - Test Data Fetch -** Use the token or API key to make a test GET request to the host data endpoint. **For example :**


Copy```
curl -X GET "https://api.workelevate.com/v1/devices?limit=1" \
   -H "Authorization: Bearer <YOUR_TOKEN_HERE>"
```

  * In this example, we attempt to fetch just 1 device (`limit=1`) as a quick test. Adjust the endpoint path (`/devices`) and any query parameters according to the actual API. If using an API key instead of a bearer token, the header might be different (e.g., `-H "X-API-Key: <YOUR_API_KEY>"` or whatever key name Workelevate expects) 


  * **Step 4 - Verify the Response -** A successful response should return HTTP status 200 OK and some JSON data. Even if you requested one device, the response likely contains a JSON array or object with device details. Verify that the data fields appear as expected (e.g., you see a hostname, OS, etc. in the output). This confirms the credentials work and that the account has permission to view device data 
  * **Step 5 - Handle Errors - If you get an authentication error (401 Unauthorized or 403 Forbidden) :**
    * Double-check the token or credentials (password, API key) are correct 
    * Ensure the account has the proper permissions (it might be logged in but forbidden from the endpoint if roles are insufficient) 
    * Confirm you are hitting the correct URL (sometimes a wrong path or version can cause auth issues) 
  * If you get a not found (404), the endpoint path might be incorrect – check documentation for the correct endpoint for listing devices 
  * **Step 6 - Test with Pagination (if applicable) -** If the API returns only a portion of data by default, try adding pagination parameters (like `page=1&limit=10`) and see if the structure includes links or indications of more pages. This helps confirm how to retrieve all data 
  * Performing these tests manually helps identify any issues early. Only once you can successfully fetch host data via API should you proceed to plug these details into Zeron’s integration configuration 


**Providing Information to Zeron for Configuration**[](https://docs.zeron.one/integrations/workelevate-it-endpoint-management#providing-information-to-zeron-for-configuration)
After verifying the API access, you will need to provide certain information to the Zeron team (or input it into Zeron’s integration module) so that Zeron can be configured to pull data from Workelevate. **Ensure you share the following details with the Zeron configuration team or interface :**
  * **API Base URL -** The root URL for the Workelevate API. For example: `https://api.workelevate.com/v1 `(or a similar endpoint). If Workelevate uses tenant-specific URLs or region-specific domains, provide the exact base URL to use. This tells Zeron where to send API requests 
  * **Authentication Details -** Provide the necessary credentials for Zeron to authenticate. **This could be :**
    * An API Token (Bearer token string) if you generated one. Ensure it’s active and not expired. It’s best to transmit this securely 
    * If using username/password (basic auth or token retrieval), provide the service account username and password. (Again, do this through a secure channel, not plain email) 
    * If using OAuth2, provide the client ID, client secret, token URL, and scopes needed – essentially all pieces Zeron needs to obtain a token. Also share the tenant ID or any identifier if Workelevate’s OAuth requires it 


  * **API Endpoints or Queries -** Inform what endpoints and parameters Zeron should call to get the data. In many cases, Zeron’s integration for Workelevate might already know the endpoints. But if needed, specify that the host inventory endpoint (e.g., `/devices` or `/endpoints`) is the one to use, and any query parameters for filtering or pagination. For instance, if you only want to fetch active devices, or if a certain parameter like `status=active` is required, mention that 
  * **Pagination/Iteration Instructions -** If the data needs to be fetched in chunks, clarify how Zeron should handle it (e.g., “Keep requesting `?page=N&size=100` until no more results”). We discuss pagination details in the next section, and you can share those with the Zeron team so they configure the connector correctly 
  * **Certificate or Network Requirements -** if Workelevate’s API is hosted in a way that requires firewall rules or certificates (for on-premise deployments, perhaps), provide the necessary connection details. For cloud SaaS, this is usually not an issue as Zeron can reach it over HTTPS. But if an IP allowlist is needed (some APIs restrict access to known IPs), you might need to whitelist Zeron’s servers’ IP addresses in Workelevate or your firewall 
  * **Data Mapping Information -** Optionally, clarify how fields should be mapped or used in Zeron. For example, “Use Workelevate’s `deviceId` as the unique asset ID in Zeron, hostname as asset name, etc.” Zeron’s integration likely handles this automatically, but any custom expectations should be noted 


Make sure these details are communicated securely. With the base URL and credentials provided, the Zeron team can configure the integration plugin/connector for Workelevate. They will input the API endpoint and credentials into Zeron’s system so that it can start pulling the data at regular intervals 
Last updated 4 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

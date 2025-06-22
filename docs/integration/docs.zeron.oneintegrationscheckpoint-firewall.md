
# CheckPoint Firewall
Integrating Check Point firewalls with the ZERON platform involves two data collection methods: API integration and Syslog integration. Through the Management API, ZERON can pull configuration and inventory data (such as host objects and firewall device details) from the Check Point Security Management Server. In parallel, the Check Point firewall can be configured to forward syslog logs (security events and traffic logs) to ZERON for real-time monitoring. This guide outlines the setup for both methods on Check Point (assuming Check Point R80.40 or R81.10 management), and details the requirements, configuration steps, and example API calls. By following this guide, you will prepare the Check Point environment so that ZERON (a Cyber Risk Posture Management platform) can securely fetch data and receive log events from your Check Point firewall
**Note on Versions -** The instructions below apply to Check Point R80.x and R81.x (e.g. R80.40, R81.10). These versions include the modern Management API and the Log Exporter feature for syslog. If you run older versions (R77.x or earlier), the integration would require different steps (OPSEC/LEA for logs, etc.), which are not covered here.**Data Collected: ZERON will collect two primary categories of data from Check Point :**
  * **Configuration/Host Data via API -** A list of host objects and network devices defined in the Check Point management database (including hostnames, IP addresses, etc.), as well as details of the firewall gateways/cluster members (name, version, blades enabled). This gives ZERON an inventory of the assets protected by the firewall and the firewall itself. 
  * **Security Event Logs via Syslog -** Real-time logs of traffic and security events (allow/deny decisions, threat prevention alerts, etc.) will be sent from Check Point to ZERON’s log collector over syslog. This provides visibility into firewall events for analysis and correlation in ZERON.


**Integration architecture -** ZERON uses the Check Point Management API to retrieve host and device information, and the Check Point Management Server (or Log Server) sends firewall logs via syslog to the ZERON collector 
**Prerequisites and Access Requirements**[](https://docs.zeron.one/integrations/checkpoint-firewall#prerequisites-and-access-requirements)
**Before configuring the integration, ensure the following prerequisites are in place :**
  * **Check Point Management Access -** You have administrator access to the Check Point Security Management Server (SmartConsole or Gaia UI) to create accounts and modify settings
  * **Network Connectivity -** ZERON’s server/collector can reach the Check Point Management Server over HTTPS (port 443, or customized API port) for API calls, and the Check Point server can reach the ZERON log collector over UDP/TCP for syslog. Ensure any firewalls between them allow this communication 
  * **Check Point API Enabled -** The Management API must be enabled on the Check Point server. By default, in R80+ it is usually enabled (if the management has sufficient RAM), but if not, you can enable it via SmartConsole (`Manage & Settings -> Blades -> Management API -> Advanced Settings`) and publish changes. Also run `api restart` on the management server if required.
  * **Allowed API Clients -** The ZERON platform’s IP address must be permitted to use the API. In SmartConsole, navigate to Manage & Settings -> Blades -> Management API -> Advanced Settings and set the API accessibility. You can choose “All IP addresses that can use GUI clients” (and ensure ZERON’s IP is defined as a GUI client) or explicitly add ZERON’s IP as an allowed API client. This prevents unauthorized hosts from calling the API
  * **Check Point Login Credentials for API -** A dedicated API service account on Check Point (username/password or API key) with the appropriate permissions (read-only) – steps detailed below
  * **Syslog Target Details -** Identify the ZERON syslog collector IP/hostname and port that will receive Check Point logs. (For example, UDP 514 or another port as specified by ZERON. In this guide we will use `<ZERON_SYSLOG_IP>` and port `514` as placeholders – replace these with the actual details for your environment.) No specific hostname is required from ZERON’s side; you can use a placeholder or environment-specific setting in the Check Point config


**Creating an API User Credential on Check Point**[](https://docs.zeron.one/integrations/checkpoint-firewall#creating-an-api-user-credential-on-check-point)
To allow ZERON to call the Check Point Management API, create a dedicated administrator account for API access. This account will be used by ZERON to authenticate and retrieve data. **Follow these steps in the Check Point SmartConsole :**
  * **Navigate to Administrators -** Open SmartConsole and go to Manage & Settings > Permissions & Administrators > Administrators 
  * **Create New Administrator -** Click New Administrator to create a new admin account. Give it a recognizable name (e.g., “zeron_api_user”) 
  * **Authentication Method** - Set an authentication method for this API user. The simplest is Check Point Password, then specify a strong password for the account. Alternatively, if running R80.40 or above, you can choose to use an API Key for this user instead of a password (in R80.40+, SmartConsole allows generating an API key for an admin user). Using an API key is convenient for automation – if you select “API Key” as the authentication method, SmartConsole will generate a secure API key string for the user (ensure to copy this key; it will serve as the credential) 
  * **Permissions Profile -** Assign the minimum necessary permissions to this account. We recommend using the built-in Read Only All permission profile, which grants read access to all configurations and logs but no write privileges. This profile is sufficient for querying objects and fetching log data, and adheres to the principle of least privilege. Do not use super-user or write access unless required. If a suitable read-only profile doesn’t exist, create a custom profile that at least includes read access to all relevant data (policies, network objects, logs) but no policy installation or write permissions 
  * **Enable API Access -** In the new administrator’s properties, make sure “Management API access” (sometimes labeled API Login) is enabled for the account. In R80+, an admin can be allowed or disallowed API login separately from GUI login. Ensure this option is turned on so that the account can authenticate via the web API 
  * **Secure the Account -** You may set this account to non-expiring (or note the expiration) and optionally restrict its access by IP (Trusted Clients) if desired, though typically the API client IP restriction is handled globally as noted earlier. After configuring, click OK and Publish changes in SmartConsole to apply the new admin 


At this point, you have an API user account (and API key, if applicable) ready for ZERON to use. **Example -** You might have created user “zeron_api_user” with password “(secret)” and Read-Only permissions, or generated an API Key like `ABCD-1234-XYZ...` for this user. This credential will be provided to the ZERON team in a later step
**API Key vs Password -** If you created an API key (R80.40+), ZERON will authenticate using that key instead of a username/password. API keys cannot be used in SmartConsole login (they’re meant for automation), so this method effectively ensures the account is used only for API access. If using an API key, make sure to store it securely as it grants API access with the user’s privileges
**Required Permissions for the API User**[](https://docs.zeron.one/integrations/checkpoint-firewall#required-permissions-for-the-api-user)
As mentioned, the API account should have only the permissions needed to retrieve the required data, and nothing more (“least privilege” approach). Do not assign full admin rights or policy installation capabilities if not necessary. For ZERON’s data collection, the account needs the ability to read objects and logs from the management server. The built-in Read Only All profile on Check Point is ideal, as it permits viewing all configurations and logs without making changes. This profile includes read access to network objects (hosts, networks, groups), rule bases, and log entries, which covers ZERON’s use cases
If using a custom profile, ensure it includes at least: Read access to all policy packages, all network objects, and the ability to open logs (if ZERON were to query logs via API, though in our integration logs will come via syslog). In Check Point R80+, the permission profiles are quite granular; however, Read Only All already encapsulates all read permissions needed and is the recommended choice for simplicity 
Finally, confirm that the account can indeed use the API (the “Management API login” flag must be allowed). In summary, the account should effectively be a read-only API user. This way, even if the credentials were compromised, the account cannot alter any firewall settings
**Configuring API Connectivity (Trusted Clients and API Settings)**[](https://docs.zeron.one/integrations/checkpoint-firewall#configuring-api-connectivity-trusted-clients-and-api-settings)
**With the API user ready, a couple of management settings need review to ensure ZERON can connect :**
  * **Allowed Clients -** Verify that the Check Point management is configured to accept API connections from the IP address of the ZERON platform (or the collector/server that will initiate API calls). In SmartConsole under Manage & Settings > Blades > Management API, you have an API Settings dialog. If the setting is “All IP addresses (Any computer)”, then any host can attempt API login. If it is “All IP addresses that can be used for GUI clients”, then the ZERON host must be defined as a GUI client (under Manage & Settings > Permissions & Administrators > Trusted Clients). Add the ZERON server’s IP here if not already present. After adding, publish the changes. (By default, many deployments allow all GUI clients or even all IPs for API, but it’s good to explicitly include ZERON’s IP to avoid any connection issues) 
  * **API Service Accessibility -** Ensure the API port is open and reachable. By default, Check Point API listens on port 443 (HTTPS) on the management server. If your management server is behind a firewall, allow inbound HTTPS from the ZERON host. If you changed the default port (in $FWDIR/conf/web_api.conf or via SmartConsole) or if using a Multi-Domain Server, note the correct port/domain. ZERON will need the management server address and port. For example, if the management server is `10.0.0.10` and API on 443, that will be the base URL; if using a custom port, e.g., 4434, ZERON needs to know that (e.g., `https://10.0.0.10:4434`) 


  * **Certificate Consideration -** The API uses HTTPS. By default, Check Point uses a self-signed SSL certificate for the API server. ZERON’s connector may either ignore certificate verification or require the certificate to be trusted. If there is an option in ZERON to skip SSL verification (often called “insecure” mode), you can use that. Otherwise, you might need to export the Check Point management server’s certificate and provide it to ZERON to trust it. (For example, some integrations simply use `curl -k` to ignore SSL issues in testing). Check with the ZERON team which approach they use. For now, be aware that if ZERON’s API client rejects the server cert, you’ll need to address this (either by toggling “trust any certificate” on the ZERON side or configuring a valid cert on Check Point) 


Once the above is done, the Check Point management is essentially prepared for API access by ZERON
**Testing the API Credentials**[](https://docs.zeron.one/integrations/checkpoint-firewall#testing-the-api-credentials)
Before integrating with ZERON, it’s prudent to manually test that the API credentials and connectivity work. **You can do this using a tool like cURL or Postman to simulate what ZERON will do :**
  * **Login via API -** Use a login call to obtain an API session SID (session ID). **For example, from a machine that can reach the management server, run :**


Copy```
curl -k -X POST https://<MGMT_SERVER>/web_api/login \
   -H "Content-Type: application/json" \
   -d '{ "user": "<API_USERNAME>", "password": "<API_PASSWORD>" }'
```

  * Replace `<MGMT_SERVER>` with your Check Point management IP or hostname (and port if not 443), and insert the API username/password you created. The `-k` option in cURL is used here to ignore SSL certificate verification (only use this for testing, or if ZERON will also not verify the cert). If using an API key instead of user/password, use a payload like `-d '{ "api-key": "<API_KEY>" }'` in the login request 


  * **A successful response will be JSON containing an**`**"sid"**`**field (session ID), for example :**


Copy```
{ "sid" : "eQEgwk_XYz12AbCdEfGh...", "uid" : "..." , "login-time" : 1678912345, ... }

```

  * **Test an API call (show hosts) -** Once you have an `sid`, you can try an actual data query. **For example :**


Copy```
curl -k -X POST https://<MGMT_SERVER>/web_api/show-hosts \
   -H "Content-Type: application/json" \
   -H "X-chkp-sid: <SID_FROM_LOGIN>" \
   -d '{ "limit": 5 }'
```

  * This should retrieve a list of host objects (up to 5 in this example) from Check Point. The response JSON will contain an array of objects with details like name, IP address, UID, etc. (The `X-chkp-sid` header carries your session token for authorization). If this returns data successfully, your API user is working correctly. **You can also try**`**show-gateways-and-servers**`**similarly to fetch firewall gateway info :**


Copy```
curl -k -X POST https://<MGMT_SERVER>/web_api/show-gateways-and-servers \
   -H "Content-Type: application/json" \
   -H "X-chkp-sid: <SID_FROM_LOGIN>" \
   -d '{ "limit": 5 }'
```

  * This should return information on your Security Gateways/Cluster Members (names, types, versions, blades, etc) 
  * **Logout - Finally, you can log out to close the session (optional but good practice), using the**`**logout**`**command :**


Copy```
curl -k -X POST https://<MGMT_SERVER>/web_api/logout \
   -H "Content-Type: application/json" \
   -H "X-chkp-sid: <SID_FROM_LOGIN>" \
   -d '{}'   
```

  * The logout call requires the session ID and an (empty) JSON body. It will return a message like `{"message": "OK"}` on success. This frees up the session on the server 
  * If all the above steps succeed (login → retrieve data → logout), the API integration part is functioning. You have confirmed that the credentials are correct and the Check Point management is reachable from the ZERON side. Keep the API username/password or API key handy, as well as the management server URL/port – these will be input into the ZERON system 


**Information to Provide to ZERON**[](https://docs.zeron.one/integrations/checkpoint-firewall#information-to-provide-to-zeron)
With the Check Point side configured, you will need to share certain details with the ZERON team (or input them into the ZERON platform’s integration configuration) so they can set up the connector. **Typically, provide the following :**
  * **Management Server URL/IP and Port -** The address of the Check Point Management Server (Security Management or Multi-Domain Management) that ZERON will connect to. For example: `10.0.0.10` (and port `443` if default, otherwise specify port). If it’s a Multi-Domain Server (MDS), also provide the Domain name or UID that ZERON should connect to (the API domain parameter) – usually ZERON will have a field for Domain if needed 
  * **API Credentials -** The username and password of the API account you created or the API key. If a username/password is used, provide both. If an API key is used, provide the key string and the username (if required). Ensure this is communicated securely since it grants access 
  * **Check Point Version (Optional) -** It can be helpful to inform ZERON which Check Point version you are on (e.g., R81.10), so they know which API version to use. ZERON likely auto-detects or is compatible with multiple versions, but sharing it can help troubleshoot if needed 
  * **Additional API Parameters -** If your environment has any special requirements (for example, if the API user only has access to certain domains or data, or if a Proxy is needed), communicate that. In most cases, just the base URL, credentials, and maybe domain are needed 
  * **Syslog Receiver Details -** Confirm the IP/hostname and port on ZERON’s side where Check Point will send syslogs. For instance, “Please listen for Check Point logs from IP `<MgmtIP>` on UDP port `514`.” This is more for your internal configuration, but ZERON might want to verify that they are expecting logs from the correct source. ZERON may provide an IP or hostname for a collector that you must configure as the syslog target on Check Point – use that in the next section. If ZERON provided a specific format or protocol (e.g., CEF), note that as well. (In our case, we will use the default Check Point log format over syslog, which ZERON can parse) 


In summary, fill in ZERON’s integration settings with: CheckPoint Management URL, API username (or key), API password (if not using key), and the syslog target (which we’ll configure on Check Point next). ZERON’s team will use this information to finalize the integration on their side 
(**Placeholders -** if any IP addresses or hostnames were mentioned in this document for ZERON’s side, remember to replace them with your actual values when configuring)
**Configuring Check Point to Send Syslog Logs to ZERON**[](https://docs.zeron.one/integrations/checkpoint-firewall#configuring-check-point-to-send-syslog-logs-to-zeron)
Next, set up log forwarding so that all relevant Check Point logs are transmitted to ZERON’s collector via syslog. Check Point provides a feature called Log Exporter (available in R80.10+ and integrated natively from R80.20 onwards) that can send logs to external systems in various formats (Syslog, CEF, etc.). We will use Log Exporter to send logs in “syslog” format (the native Check Point log format) over UDP or TCP to ZERON 
**Note -** The default “syslog” format from Check Point is a raw, key-value log format that includes fields like timestamp, action, rule, source, destination, service, etc., similar to what you see in SmartView Tracker. This is the format ZERON’s parser expects (not CEF or LEEF unless specified otherwise). For completeness: Check Point Log Exporter supports other formats like `cef`, `json`, `leef`, etc., but here we will stick to the default. The default is `syslog` format 
**Steps to configure Log Exporter (on the Management or Log Server) :**
  * **Step 1 - Connect to the Check Point CLI -** SSH into the Check Point Management Server (or dedicated Log Server, if your logs are on a separate server). You need expert mode (Linux shell) access with appropriate privileges 
  * **Step 2 - Add a Log Exporter target -** Run the `cp_log_export` command to add a new target. **For example :**


Copy```
cp_log_export add name "ZERON_export" \
  target-server <ZERON_SYSLOG_IP> target-port 514 \
  protocol udp format syslog
```

  * **Let’s break down this command :**
    * **name "ZERON_export" -** Give a name to this export configuration (can be any label, e.g., “ZERON_export”) 
    * **target-server**`**<ZERON_SYSLOG_IP>**`**-** The IP address or hostname of the ZERON syslog collector (replace this placeholder with the actual IP provided by ZERON) 
    * **target-port 514 -** The port on the ZERON side for syslog. Commonly 514 for UDP syslog, but use whatever port ZERON expects (they might use a custom port) 
    * **protocol udp -** Use UDP for syslog (typical for syslog, unless TCP is preferred for reliability – Check Point supports both). If ZERON requests TCP syslog or an encrypted channel, you could use `protocol tcp `
    * **format syslog -** Use the default syslog format (raw Check Point logs). This ensures logs are not transformed into another schema 
    * **Example - If ZERON’s collector is at IP 192.168.1.100 and listening on UDP 514, the command becomes :**
`cp_log_export add name "ZERON_export" target-server 192.168.1.100 target-port 514 protocol udp format syslog`
    * This command creates a new export configuration. (If you prefer a different format like CEF, you would put `format cef`, but again, for ZERON we use `syslog` as per current requirements 


  * **Step 3 - Start the Log Exporter - After adding, start the exporter process for that target :**


Copy```
cp_log_export restart name "ZERON_export"
```

  * This activates the log forwarding. The management server will now begin sending logs to the specified target. You can verify the status by running `cp_log_export show name "ZERON_export"` to see if it’s running and how many logs exported, etc 
  * **Step 4 - Verify log flow -** It’s important to check that logs are indeed leaving the Check Point and reaching ZERON. On the Check Point side, you can use tcpdump to see outbound traffic to ZERON’s IP on port 514. On the ZERON side (or using their interface), confirm that some logs have been received. It might take a few minutes for logs to start flowing. Also, ensure that your security policy is not blocking these syslog packets (the management server needs to be allowed to send outbound traffic to ZERON) 


Last updated 4 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

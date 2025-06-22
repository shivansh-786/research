
# Fortinet Firewall
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F4211542702-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FQPfbdyLrtbE8w5R9rmvH%252Fuploads%252F75T9R8F4o0IcfNhxeX5w%252F651bcbfad90d60a6dface6bc_5f3322f59b165f9de9392630_Fortinet_Logo_Black-Red-PMS485-removebg-preview.png%3Falt%3Dmedia%26token%3D9825de7a-c25c-49bd-a6d2-511a0b812a16&width=768&dpr=4&quality=100&sign=c7024202&sv=2)
This document outlines the process for integrating the Fortinet FortiGate Firewall with the Zeron platform. The integration enables the forwarding of firewall logs to Zeron, allowing automated ingestion and analysis of data 
By following this guide, users will be able to configure their Fortinet firewall to send logs to Zeron via a Syslog server. Once the setup is complete, Zeron will begin receiving firewall logs in real-time and display associated metrics on its dashboards 
**Prerequisites** [](https://docs.zeron.one/integrations/fortinet-firewall#prerequisites)
**Before beginning the integration, ensure the following :**
  * You have access to a Syslog server 
  * You are able to configure the Fortinet FortiGate Firewall to forward logs to that server 
  * UDP Port 514 is open and available between the Syslog server and the Zeron platform 
  * Access to the Fortinet configuration interface, either through CLI or GUI 


No additional API credentials, tokens, or platform-side configurations are needed for this integration 
**How to Get Credentials**[](https://docs.zeron.one/integrations/fortinet-firewall#how-to-get-credentials)
This integration does not require user credentials, API keys, or tokens. The only setup needed is on the firewall and Syslog server side. Once logs are forwarded as specified, Zeron will automatically ingest and process them 
**Integration Steps**[](https://docs.zeron.one/integrations/fortinet-firewall#integration-steps)
**Step 1 - Create a Syslog Server :**
  * The first step is to configure a Syslog server that is capable of receiving and forwarding Fortinet FortiGate firewall logs 
  * **Refer to Fortinet’s official documentation for detailed steps on how to create and configure the Syslog server :**
    * [Fortinet Syslog Configuration Guide](https://help.fortinet.com/fadc/4-5-1/olh/Content/FortiADC/handbook/log_remote.htm)
  * This documentation provides comprehensive guidance on setting up remote logging 


**Step 2 - Configure Log Forwarding to UDP Port 514 :**
  * **Once the Syslog server is set up, ensure that :**
    * The Syslog server is configured to send data to UDP port 514
    * This port should be accessible from the Syslog server to the Zeron platform endpoint 
  * No further configuration is needed on the Fortinet firewall or on Zeron’s end


**Data Expected After Integration**[](https://docs.zeron.one/integrations/fortinet-firewall#data-expected-after-integration)
**Once logs are received by Zeron :**
  * The Zeron dashboard will begin displaying detailed KPIs and KRIs based on the firewall log data 
  * These insights are derived directly from the log information being forwarded from the Fortinet firewall 


**References** [](https://docs.zeron.one/integrations/fortinet-firewall#references)
[https://help.fortinet.com/fadc/4-5-1/olh/Content/FortiADC/handbook/log_remote.htm](https://help.fortinet.com/fadc/4-5-1/olh/Content/FortiADC/handbook/log_remote.htm)
Last updated 9 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

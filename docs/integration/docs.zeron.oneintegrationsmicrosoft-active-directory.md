
# Microsoft Active Directory
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F4211542702-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FQPfbdyLrtbE8w5R9rmvH%252Fuploads%252Fmp8dnQTZ8Qm4nMLFEJwE%252Fwhat-is-active-directory-and-why-is-it-used-removebg-preview.png%3Falt%3Dmedia%26token%3D87dad638-4e73-4146-991b-90c941aa1774&width=768&dpr=4&quality=100&sign=e46226a1&sv=2)
This guide provides comprehensive instructions for collecting data from Active Directory (AD) using LDAP queries. It includes details on the necessary package installations, domain joining, and usage of LDAP search operations for administrative tasks within the bsli.com domain 
The integration with Zeron, the Cyber Risk Posture Management (CRPM) platform, enables visibility into your AD environment to support informed cybersecurity decision-making 
**Prerequisites** [](https://docs.zeron.one/integrations/microsoft-active-directory#prerequisites)
**Required Packages List :**
**Package Name**
**Description**
**sssd**
System Security Services Daemon
**realmd**
Tool to configure realm enrollment
**oddjob**
Support service for account tasks
**oddjob-mkhomedir**
Module to create home directories
**adcli**
Tool for joining AD domains
**samba-common**
Required for Samba compatibility
**samba-common-tools**
Utility tools for Samba
**krb5-workstation**
Kerberos client utilities
**openldap-clients**
LDAP client commands
**policycoreutils-python**
Required for SELinux tools
**Before initiating the integration process, ensure the following packages are installed :**
  * yum install sssd realmd oddjob oddjob-mkhomedir adcli samba-common samba-common-tools krb5-workstation openldap-clients policycoreutils-python


**How to Get Credentials**[](https://docs.zeron.one/integrations/microsoft-active-directory#how-to-get-credentials)
**To perform the LDAP queries and join operations, the following are needed :**
  * A domain user account with permissions to bind and search via LDAP
  * Domain Controller hostname or IP address
  * LDAP Distinguished Name (DN) paths relevant to your AD structure (e.g., dc=bsli,dc=com)


These credentials should be secured and provided by your AD administrator
**How to Integrate**[](https://docs.zeron.one/integrations/microsoft-active-directory#how-to-integrate)
**If the domain controller cannot be pinged, add it manually to your /etc/hosts file :**
  * echo <server-IP> <domain-controller> <name> >> /etc/hosts


**To join the machine to your Active Directory domain :**
  * sudo realm join --user=<user-name> <domain-controller>


**After joining, verify the domain connection with :**
  * realm list 


**To bind to LDAP and perform queries, use the following :**
  * ldapsearch -x -h <domain_name> -D "<username>@<domain_name>" -W -b "cn=<user>,dc=<DC>,dc=<DC>


**If ldapsearch is not available :**
  * yum -y install openldap-clients 


**Example of ldapsearch :**
  * ldapsearch -x -b "<domain_user>" -h <domain_controller>


**To disjoin the machine from the domain :**
  * sudo realm leave <domain_controller>


**What Data is Expected After Integration**[](https://docs.zeron.one/integrations/microsoft-active-directory#what-data-is-expected-after-integration)
Once integrated, LDAP queries can be used to collect a wide variety of data from AD. Below is a list of specific queries included in the guide, categorized by use case 
**Users not logged in the last 90 days but ID is active :**
  * ./ldapsearch -x -H ldap://<DC> -D "<username>@<DC>" -W -b "ou=Users,ou=G-Corp,ou=<ou>,DC=<DC>,DC=<DC>" "(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2)(lastlogontimestamp>=133276740690000000))" samAccountName lastlogontimestamp 


**Users who haven’t reset password in last 45 days :**
  * ./ldapsearch -x -H ldap://<DC> -D "<username>@<DC>" -W -b "ou=Users,ou=G-Corp,ou=<ou>,DC=<DC>,DC=<DC>" "(&(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2))(pwdLastSet<=133303524690000000))" samAccountName 


**Computers not logged in last 30 days :**
  * ./ldapsearch -x -H ldap://<DC> -D "<username>@<DC>" -W -b "DC=<DC>,DC=<DC>" "(&(objectClass=computer)(!(userAccountControl:1.2.840.113556.1.4.803:=2))(pwdLastSet<=133303524690000000))" distinguishedName objectClass 


**Users with password complexity not matched :**
  * ./ldapsearch -x -H ldap://<DC> -D "<username>@<DC>" -W -b "ou=<OU>,DC=<DC>,DC=<DC>" "(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=65536)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))" distinguishedName 


**Users with password never expiry enabled :**
  * ./ldapsearch -x -H ldap://<DC> -D "<username>@<DC>" -W -b "ou=<OU>,DC=<DC>,DC=<DC>" "(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=65536))" distinguishedName 


**Users having USB access :**
  * ./ldapsearch -x -H ldap://<DC> -D "<username>@<DC>" -W -b "DC=<DC>,DC=<DC>" "(&(objectClass=top)(memberOf=CN=ABML Usb Write Enable,CN=Users,DC=,DC=))" 


**Users with full internet access :**
  * ./ldapsearch -x -H ldap://<DC> -D "<username>@<DC>" -W -b "DC=<DC>,DC=<DC>" "(&(objectClass=computer)(InternetAccess=Full))" 
  * ./ldapsearch -x -H ldap://<DC> -D "<username>@<DC>" -W -b "DC=<DC>,DC=<DC>" -E "pr=15/noprompt" "(&(objectClass=*)(msRTCSIP-InternetAccessEnabled=TRUE))" 


**Users with domain admin access :**
  * ./ldapsearch -x -H ldap://<DC> -D "<username>@<DC>" -W -b "ou=Users,ou=G-Corp,ou=<OU>,dc=<DC>,dc=<DC>" "(&(objectClass=user)(memberOf=CN=Domain Admins,CN=Users,DC=<DC>,DC=<DC>))"


**User account reactivated in last 24 hours :**
  * ./ldapsearch -x -H ldap://<DC> -D "<username>@<DC>" -W -b "ou=Users,ou=G-Corp,ou=<OU>,dc=<DC>,dc=<DC>" "(&(objectClass=user)(whenChanged>=133277604690000000))"


**Top 10 computers with most days without login :**
  * ./ldapsearch -x -H ldap://<DC> -D "<username>@<DC>" -W -b "dc=<DC>,dc=<DC>" "(&(objectClass=computer)(!(lastLogonTimestamp=*)))"


**Get user details :**
  * ./ldapsearch -x -H ldap://<DC> -b "dc=<DC>,dc=<DC>" -D <username>"@<DC>" -W -LLL "(sAMAccountName=<>)"


**Search Group Policy Objects :**
  * ./ldapsearch -x -D "<username>@<DC>" -H ldap://<DC> -b "dc=<DC>,dc=<DC>" "(objectClass=groupPolicyContainer)"


**References**[](https://docs.zeron.one/integrations/microsoft-active-directory#references)
Last updated 9 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

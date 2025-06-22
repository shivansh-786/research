
# Cisco Duo APIs
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F4211542702-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FQPfbdyLrtbE8w5R9rmvH%252Fuploads%252Fd6BY3ln3tLXJY4Vo1CmA%252FCisco-Duo.png-removebg-preview.png%3Falt%3Dmedia%26token%3D44b41867-8839-4006-9c30-23d7b8b2c7cc&width=768&dpr=4&quality=100&sign=42b339a7&sv=2)
This document describes the process of integrating the Cisco Duo Admin API with the Zeron platform to retrieve a list of users who have Multi-Factor Authentication (MFA) configured. The integration relies on the /admin/v2/users endpoint, which provides detailed user information, including enrolled MFA methods such as phones, hardware tokens, and WebAuthn credentials 
**Prerequisites**[](https://docs.zeron.one/integrations/cisco-duo-apis#prerequisites)
**To proceed with the integration, you will need :**
**Requirement**
**Details**
**Cisco Duo Account**
Admin/Owner access to the Duo Admin Panel
**Duo Admin API Application**
An application configured under “Admin API” in Duo
**Permissions**
“Grant read resource” enabled in the Admin API application
**Secure Storage**
A vault or similar method for securely storing the Secret Key
**How to Get Credentials**[](https://docs.zeron.one/integrations/cisco-duo-apis#how-to-get-credentials)
**Step-by-Step Instructions :**
  * **Step 1 - Log into the Duo Admin Panel :**
    * Use an account with Owner or Administrator privileges.
  * **Step 2 - Create an Admin API Application :**
    * Go to Applications > Protect an Application 
    * Select Admin API and click Protect 
  * **Step 3 - Configure Permissions :**
    * Enable Grant read resource 
    * (Optional) Set allowed IP addresses under Networks for API Access 
  * **Step 4 - Record the Following Details from the App Configuration :**
    * Integration Key (ikey), example - DIWJ8X6AEYOR5OMC6TQ1
    * Secret Key (skey), example - Zh5eGmUq9zpfQnyUIu5OL9iWoMMv5ZNmk3zLJ4Ep
    * API Hostname (e.g., api-xxxxxxxx.duosecurity.com), example - api-xxxxxxxx.duosecurity.com 
  * **Step 5 - Save and Secure :**
    * Click Save Changes 
    * Store the Secret Key securely. Regenerate it if compromised 


**Integration Steps**[](https://docs.zeron.one/integrations/cisco-duo-apis#integration-steps)
**API Authentication :**
  * Cisco Duo uses HMAC-SHA1-based HTTP Basic Authentication 
  * **Required Headers :**
    * **Date -** Timestamp in RFC 2822 format
    * **Authorization -** Formatted as Basic base64(ikey:signature) 


**Generating the HMAC-SHA1 Signature :**
  * **Build a Canonical String with the following :**
    * Current date (e.g., Tue, 06 May 2025 12:14:18 -0000)
    * HTTP method (e.g., GET)
    * Lowercase API hostname
    * Request path (/admin/v2/users)
    * Sorted query parameters (e.g., limit=100&offset=0)
  * **Generate the Signature :**
    * Create an HMAC-SHA1 of the canonical string using the skey 
  * **Format the Header :**
    * Combine ikey:signature and base64 encode the result 
    * Set the Authorization header accordingly 
  * **Python Example :**


Copy```
def sign(method, host, path, params, skey, ikey):
  import base64, email.utils, hmac, hashlib, urllib.parse
  now = email.utils.formatdate()
  canon = [now, method.upper(), host.lower(), path]
  args = [f"{urllib.parse.quote(k)}={urllib.parse.quote(str(v))}" for k, v in sorted(params.items())]
  canon.append("&".join(args))
  canon_str = "\n".join(canon)
  sig = hmac.new(skey.encode(), canon_str.encode(), hashlib.sha1)
  auth = f"{ikey}:{sig.hexdigest()}"
  return {
    "Date": now,
    "Authorization": f"Basic {base64.b64encode(auth.encode()).decode()}"
  }
```

**Calling the DUO API :**
  * **Endpoint -** GET /admin/v2/users
  * **Host -** Your Duo API Hostname
  * **Parameters :**
    * **limit -** Number of users per page (max 500)
    * **offset -** For pagination
    * **username -** (optional)
    * **sort -** (optional, e.g., username:asc)
  * **Example Request Header :**
    * GET /admin/v2/users?limit=100&offset=0 Host: api-xxxxxxxx.duosecurity.com Date: Tue, 06 May 2025 12:14:18 -0000 Authorization: Basic 


**Handling Pagination :**
  * Start with offset=0 and a limit (e.g., 100) 
  * Check metadata.next_offset in the response 
  * Repeat the request using the new offset value until no next_offset is returned 
  * **Example Python Code :**


Copy```
def fetch_users(ikey, skey, host):
  import requests, time
  url = f"https://{host}/admin/v2/users"
  users = []
  offset = 0
  limit = 100
  while True:
    params = {"limit": limit, "offset": offset}
    headers = sign("GET", host, "/admin/v2/users", params, skey, ikey)
    response = requests.get(url, headers=headers, params=params).json()
    if response["stat"] != "OK":
      raise Exception(f"API error: {response['message']}")
    users.extend(response["response"])
    offset = response.get("metadata", {}).get("next_offset")
    if not offset:
      break
    time.sleep(1)
  return users
```

**Expected Data After Integration**[](https://docs.zeron.one/integrations/cisco-duo-apis#expected-data-after-integration)
**Sample Response :**
Copy```
{
 "stat": "OK",
 "response": [
  {
   "user_id": "DU1234567890",
   "username": "jdoe",
   "email": "jdoe@example.com",
   "status": "active",
   "phones": [
    {
     "number": "+1-555-555-5555",
     "type": "Mobile",
     "platform": "iPhone",
     "activated": true
    }
   ],
   "tokens": [],
   "webauthncredentials": []
  }
 ],
 "metadata": {
  "total_objects": 150,
  "next_offset": 100
 }
}
```

**Interpreting MFA Status :**
  * **A user is considered MFA-enabled if any of the following arrays are non-empty :**
    * phones
    * tokens
    * webauthncredentials


**Python Count Example :**
Copy```
def count_mfa_users(users):
  return sum(1 for user in users if user.get("phones") or user.get("tokens") or user.get("webauthncredentials"))
```

**Support and Troubleshooting**[](https://docs.zeron.one/integrations/cisco-duo-apis#support-and-troubleshooting)
**Error**
**Cause**
**Resolution**
**401 Unauthorized**
Invalid key or signature
Verify ikey, skey, and signature logic
**400 Bad Request**
Incorrect pagination or query params
Adjust parameters (e.g., limit, offset)
**429 Too Many Requests**
Rate limit exceeded
Use exponential backoff or add delay
**5xx Errors**
Server-side errors from Duo
Retry after some time or contact Duo support
If you encounter any issues during setup or require further customization, please reach out to our support team at support@zeron.one 
**References** [](https://docs.zeron.one/integrations/cisco-duo-apis#references)
[Duo Admin API Documentation](https://duo.com/docs/adminapi)
[Users Endpoint Documentation](https://duo.com/docs/adminapi#users)
[Duo Security Best Practices](https://duo.com/docs/security)
Last updated 9 days ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

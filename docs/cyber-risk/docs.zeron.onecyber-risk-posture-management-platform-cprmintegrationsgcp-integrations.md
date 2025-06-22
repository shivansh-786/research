  1. [Integrations](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations)


# GCP Integrations
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#requirements)
Requirements
The GCP integration requires a credentials file in JSON format containing the private key to access Google Cloud Pub/Sub or Google Cloud Storage bucket 
  * **project_id -** This tag indicates the Google Cloud project ID 
  * **subscription_name -** This string specifies the name of the subscription to read from 
  * c**redentials_file (Attach credentials.json) -** This setting specifies the path to the Google Cloud credentials file in JW Tokens
  * bucket_name


## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#architecture)
Architecture
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FrTJFAtPO3WtAJVnzRIYN%252Fgcd.png%3Falt%3Dmedia%26token%3Db87d8430-bc3f-4a42-847b-d82849b8efa6&width=768&dpr=4&quality=100&sign=40ddb7b5&sv=2)
  * Configuring GCP credentials
  * Configuring Google Cloud Pub/Sub
  * Considerations for configuration


## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#configuring-gcp-credentials)
Configuring GCP credentials
In order to make the Zensor GCP module pull log data from Google Pub/Sub or Google Storage, it will be necessary to provide access credentials so that it can connect to them 
To do this, it is recommended to create a service account with the Pub/Sub or Storage permissions and then create a key. It is important to save this key as a JSON file as it will be used as the authentication method for the GCP module 
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#creating-a-service-account)
Creating a service account
Within the Service Accounts section, create a new service account and add the following roles depending on which module to use: gcp-pubsub, gcp-bucket, or both 
  * For gcp-pubsub, add two roles with Pub/Sub permissions: Pub/Sub Publisher and Pub/Sub Subscriber.
  * For gcp-bucket, add the following role with Google Cloud Storage bucket permissions: Storage Legacy Bucket Writer.


#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#creating-a-private-key)
Creating a private key 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FkIPN5NsTcmPSdPJI8GAX%252Fcreate_private_key.png%3Falt%3Dmedia%26token%3D09b95671-f9ae-4032-a998-1a7d06af401b&width=768&dpr=4&quality=100&sign=f7747c4&sv=2)
After creating a service account, add a new key to it. To do this, click Create Key, select JSON, and click Create to complete the action 
Copy```
The new key should have this format :
```json
{ 
  "type": "service_account", 
  "project_id": "your-gcp-project-id", 
  "private_key_id": "your-private-key-id", 
  "private_key": "-----BEGIN PRIVATE KEY-----\n[YOUR_PRIVATE_KEY_CONTENT]\n-----END PRIVATE KEY-----\n", 
  "client_email": "your-service-account@your-project.iam.gserviceaccount.com", 
  "client_id": "your-client-id", 
  "auth_uri": "https://accounts.google.com/o/oauth2/auth", 
  "token_uri": "https://oauth2.googleapis.com/token", 
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", 
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account%40your-project.iam.gserviceaccount.com" 
}
```
```

`Check the official Google Cloud Pub/Sub documentation to learn more about how to configure the GCP credentials JSON file`
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#authentication-options)
Authentication options
Currently, the GCP integration only allows the credentials to be provided using an authentication file 
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#using-an-authentication-file)
Using an authentication file
As explained before, the GCP integration requires a credentials file in JSON format containing the private key to access Google Cloud Pub/Sub or Google Cloud Storage bucket 
Copy```
For gcp-Pub/Sub
project_id 
subscription_name 
credentials_file (Attach credentials.json) 
For google cloud storage bucket 
bucket_name 
project_id 
subscription_name 
credentials_file (Attach credentials.json)

```

### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#configuring-google-cloud-pub-sub)
Configuring Google Cloud Pub/Sub
Google Cloud Pub/Sub is a fully-managed real-time messaging service that allows you to send and receive messages between independent applications 
We use it to get security events from the Google Cloud instances without creating a special logic to avoid reprocessing events 
In this section, we see how to create a topic, a subscription, and a sink to fully configure Google Cloud Pub/Sub to work with Zensor 
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#create-a-topic)
Create a topic
Every publishing application sends messages to topics. Zensor will retrieve the logs from this topic 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FWnBCsHULStVVVNHoIjZH%252Fcreate_topic.png%3Falt%3Dmedia%26token%3Dddd39928-7248-4710-9a40-ecb47e679f3f&width=768&dpr=4&quality=100&sign=a8f27661&sv=2)
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#get-your-credentials)
Get your credentials
If you do not have credentials yet, follow the steps in the credentials section
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#create-a-subscription)
Create a subscription
**Follow the steps below to fill in the Create subscription form :**
  * Fill in the Subscription ID
  * Select a topic from Select a Cloud Pub/Sub topic
  * Choose Pull in the Delivery type field
  * Select the duration of the Message retention duration
  * Select the duration in days of the Expiration period


![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FUTs3U9Q365CBuFXxh7HC%252Fcreate_subscription.png%3Falt%3Dmedia%26token%3Dcc561335-bb16-47ed-930b-ecef1abc8575&width=768&dpr=4&quality=100&sign=6b6616e0&sv=2)
At this point, the Pub/Sub environment is ready to manage the message flow between the publishing and subscribing applications 
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/integrations/gcp-integrations#export-logs-via-sink)
Export logs via sink
Log activities should appear under the Logs Router section. Cloud Audit logs can be published to a Cloud Pub/Sub topic through the sinks. Create a sink and use the topic as a destination 
**Follow the steps below to complete the Create logs routing sink form :**
  * **Sink details -** provide a name and description for logs routing sink
  * S**ink destination -** select the sink service type and destination
  * **Choose logs to include in sink -** create an inclusion filter to determine which logs are included
  * **Choose logs to filter out to sink -** create exclusion filters to determine which logs are excluded
  * Click the CREATE SINK button 


![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FlLobFv9THYwVpb68gTwx%252Fcreate_logs_routing.png%3Falt%3Dmedia%26token%3D77153479-f613-482a-a4b3-6b9719c7134f&width=768&dpr=4&quality=100&sign=dac322c&sv=2)
`After you set everything up, you should see activity in the Log Viewer section. Follow the link if you need help setting up Cloud Pub/Sub topic and subscription `
Last updated 4 months ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject

Issues with the Infrastructure:

1. Terminating SSL at the Load Balancer Level:

Issue: SSL termination at the load balancer decrypts traffic before forwarding it to web servers, making the internal communication unencrypted.
Solution: Implement end-to-end encryption by maintaining SSL encryption between the load balancer and web servers. Use SSL passthrough or re-encrypt traffic within the internal network.

2. Single MySQL Server Accepting Writes:

Issue: A single MySQL server accepting writes is a potential single point of failure. If it fails, write operations are impacted.
Solution: Implement a Primary-Replica (Master-Slave) configuration for MySQL to ensure high availability and distribute the load.

3. Identical Servers (Database, Web Server, and Application Server):

Issue: Uniformity across servers may lead to a lack of diversity and create a risk if a common vulnerability affects all servers.
Solution: Introduce diversity in server configurations, versions, or components to mitigate the risk of widespread vulnerabilities.

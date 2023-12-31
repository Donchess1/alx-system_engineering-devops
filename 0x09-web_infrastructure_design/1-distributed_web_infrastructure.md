Issues with the Infrastructure:

1. Single Point of Failure (SPOF):

Issue: The load balancer (HAproxy) is a potential single point of failure.
Solution: Introduce redundancy for the load balancer using techniques like clustering or a secondary load balancer.

2. Security Issues (No Firewall, No HTTPS):

Issues:
Lack of firewall protection exposes servers to potential security threats.
Absence of HTTPS poses a security risk for data in transit.
Solutions:
Implement a firewall to control incoming and outgoing traffic.
Enable HTTPS using SSL/TLS certificates to encrypt data in transit.

3. No Monitoring:

Issue: Absence of monitoring tools makes it challenging to detect and address performance issues or outages promptly.
Solution: Implement monitoring tools to track server health, resource usage, and overall system performance.

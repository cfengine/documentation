* [CFEngine Enterprise Features](#cfengine-enterprise-features)
	* [Increased scalability](#increased-scalability)
	* [Configurable Data Feeds](#configurable-data-feeds)
	* [Federation and SQL Reporting](#federation-and-sql-reporting)

* [Design Center Beta](#design-center-beta)
	* [Graphical User Interface for Design Center](#graphical-user-interface-for-design-center)
	* [Design Center sketches with integrated monitoring and reporting](#design-center-sketches-with-integrated-monitoring-and-reporting)
	* [Version Control for Sketches](#version-control-for-sketches)
	* [Delegation of System Administrator Tasks](#delegation-of-system-administrator-tasks)

## CFEngine Enterprise Features ##

### Increased scalability ###

CFEngine Enterprise already had a reputation for strong scalability, with 1,000's of servers being able to be managed from a single Policy Server. New parallel processing of policy requests by the Policy Server in version 3.5 multiplies the scalability further. 
	  	
### Configurable Data Feeds ###

The ‘Mission Portal’ of CFEngine Enterprise provides System Administrators with detailed information about the actual state of the IT infrastructure and how that compares with the desired state. New in version 3.5 is that the type of information collected can be defined in policy, so network traffic from hosts back to the CFEngine database can be reduced by collecting just the necessary information.

### Federation and SQL Reporting ###

CFEngine Enterprise is very flexible in creating federated structures, in which parts of organizations can have their own configuration policies, while the central IT organization may impose some policies that are more global in nature. New in CFEngine Enterprise 3.5 is that it now supports federated reporting as well. With a single SQL-query information from distributed policy servers can be retrieved and offer a holistic view of all infrastructure across all parts of the organization - all under RBAC control.

## Design Center Beta ## 

### Graphical User Interface for Design Center ###

Configure and deploy infrastructure policies with ease. Browse for the right template ("sketch"), fill in the details and select the hosts that need to be impacted. Deploy with a single click and watch as the reports come in about the progress of the deployment. From basic sysadmin tasks to full application deployments, on physical servers or in the cloud, at any scale.  

### Design Center sketches with integrated monitoring and reporting ###

The CFEngine policy templates, "Sketches", are created with reporting in mind. When deployed, you'll receive continuous detailed reports about compliance with the policies, repairs and about failures of hosts to match their desired state.

### Delegation of System Administrator Tasks ###

CFEngine experts can create their own Sketches, that match the exact needs of the organization in which they are used. They can be hosted in the Design Center repository, so that other administrators, developers and line-of-business users can use them to perform sophisticated sysadmin tasks without the need for detailed CFEngine knowledge. For example, developer teams can automatically provision correctly configured test servers and take them down after completion of the test run, all with a simple point-and-click operations.

### Version Control for Sketches ###

CFEngine Enterprise keeps track of all changes in sketches and sketch-deployments, using Git-integration to track autors, source-code and meta-information about policy deployments.


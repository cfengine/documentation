* [CFEngine Enterprise Features][#cfengine-enterprise-features]
	* [Increased scalability][#increased-scalability]
	* [Configurable Data Feeds][#configurable-data-feeds]
	* [Federation and SQL Reporting][#federation-and-sql-reporting]

* [Design Center Beta][#design-center-beta]
	* [Graphical User Interface for Design Center][#graphical-user-interface-for-design-center]
	* [Design Center sketches with integrated monitoring and reporting][#design-center-sketches-with-integrated-monitoring-and-reporting]
	* [Version Control for Sketches][#version-control-for-sketches]
	* [Delegation of System Administrator Tasks][#delegation-of-system-administrator-tasks]

## CFEngine Enterprise Features ##

### Increased scalability ###

CFEngine Enterprise can manage 1,000's of hosts from a single Policy Server, and parallel processing of policy requests by the Policy Server multiplies the scalability further. 
	  	
### Configurable Data Feeds ###

The CFEngine Enterprise `Mission Portal` provides System Administrators with detailed information about the actual state of the IT infrastructure and how that compares with the desired state. 

### Federation and SQL Reporting ###

CFEngine Enterprise is very flexible in creating federated structures, in which parts of organizations can have their own configuration policies, while the central IT organization may impose some policies that are more global in nature. With a single SQL-query information from distributed policy servers can be retrieved and offer a holistic view of all infrastructure across all parts of the organization - all under RBAC control.

## Design Center Beta ##

### Graphical User Interface for Design Center ###

Configure and deploy infrastructure policies using "Sketches", by first filling in the details, selecting the hosts that need to be impacted, then tracking the progress of the deployment via the Mission Portal user interface.  

### Design Center sketches with integrated monitoring and reporting ###

When deploying CFEngine policy templates ("Sketches"), continual reporting becomes available that details compliance with policies, repairs and any failures of hosts to match their desired state.

### Delegation of System Administrator Tasks ###

CFEngine experts can create their own Sketches, that match the exact needs of the organization in which they are used. They can be hosted in the Design Center repository, so that other administrators, developers and line-of-business users can use them to perform sophisticated sysadmin tasks without the need for detailed CFEngine knowledge. 

### Version Control for Sketches ###

CFEngine Enterprise keeps track of all changes in sketches and sketch-deployments, using Git-integration to track autors, source-code and meta-information about policy deployments.


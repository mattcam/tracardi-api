    TRACARDI is an open-source Customer Data Platform (CDP).
    It offers a low-code/no-code solution for businesses to leverage customer data.
    TRACARDI is API-first and can be integrated with new and legacy systems.
    It ingests, aggregates, and stores customer data from multiple sources in real-time.
    Provides tools for managing and modeling customer data, including rule-based data shaping.
    Enables customer segmentation and targeted content delivery for personalized user experiences.
    Offers tools for unifying customer data and creating a single profile.
    Supports de-duplication of customer records and blending multiple accounts into one.
    Can be used for marketing automation and data integration with other systems.
    TRACARDI helps businesses manage, understand, and utilize customer data effectively.
    Tracardi is an open-source system for customer engagement and enhancing the consumer experience.
    It collects data from customer journeys, which are the complete interactions a customer has with a brand.
    The data is in the form of events, which are actions or occurrences recognized by the software.
    Each event is assigned to a profile that is maintained throughout the customer interaction.
    Tracardi aggregates customer journey data in the profile using a graphical editor.
    The administrator defines the method of attaching data to the profile in the graphical editor.
    Tracardi can track and analyze customer behavior, enabling companies to understand and engage with their customers better.
    It provides tools for data processing and decision-making, including integration with AI systems for analysis.
    Customer interactions and contact depend on the consents granted by the customer.
    Tracardi can increase customer engagement through micro applications, pop-ups on websites that collect customer answers.
    It integrates with other contact methods like SMS notifications, emails, and external systems.
    Tracardi is particularly useful for retailers, helping them understand customers, improve customer experience, optimize website content and navigation, optimize search, decrease unsolicited messaging, and integrate data.
    While Tracardi does not support marketing campaigns, it helps with consent management, subscriptions, unsubscriptions, and integration of marketing data with other platforms.
    Tracardi is a distributed system with several components working together to track and analyze customer data.
    The core components include a database for storing events, a data processing library, a RESTful API, and a graphical user interface (GUI).
    The data processing library handles the workflow for selected events and enables the development of Tracardi plugins.
    The GUI is a browser-based interface for end users to interact with the system.
    Background workers perform processes like merging and segmentation in the background.
    Tracardi components can be installed and run separately, with multiple instances to meet business needs.
    At least four elements must be activated for the system to work fully: the database, API, GUI, and background import worker.
    The GUI connects to the API, which in turn connects to the database.
    Additional elements like background processes for merging and segmentation, data bridges for external system connections, and microservices can be part of the Tracardi system.
    Graphical interface for creating, editing, and managing workflows.
    Nodes represent actions within the workflow.
    Connections define the flow of data between nodes.
    Parameters can be configured to customize the behavior of each node.
    Workflows are executed in response to events.
    Testing capabilities for simulating events and verifying workflow logic.
    Debugging tools for troubleshooting errors and unexpected behavior.
    Versioning support for managing multiple versions of workflows.
    Seamless integration with other Tracardi components.
    Enables automation of complex data processing tasks.
    Customizable data pipelines and personalized experiences.
    Traffic:
    
        Incoming traffic: Data sent to Tracardi from sources like websites and internal systems.
        Outgoing traffic: Data sent from Tracardi to external systems or destinations.
    
    Bridge: Software that connects two systems, allowing them to exchange data.
    
        Collects data from a specific source (e.g., queue, email, social media).
        Transfers data through event sources.
        Different bridges available (e.g., API bridge, Kafka bridge).
    
    Event source: Inbound traffic source for Tracardi.
    
        Identified by a unique identifier (ID) generated by Tracardi.
        Requires a bridge for data transfer.
        Can be set as ephemeral, where data is not permanently stored.
    
    Resource: Service or application accessed over a network or the Internet.
    
        Can provide various functions and capabilities.
        Accessed and queried for data in Tracardi.
        May require authentication (passwords, tokens) for access.
    
    Session: Data associated with a visit to a website or application.
    
        Session ID set when data is sent to Tracardi.
        Contains context information about the event's launch.
        Typically temporary and not persisted for long-term storage.
    
    Event: Representation of an action happening at a specific time.
    
        Tracks visitor behavior (e.g., clicks, logins, page views).
        Can capture additional data related to the event.
        Stored in Tracardi or passed to workflows for processing.
    
    Routing rule: Determines which workflow to execute based on event arrival.
    
        Consists of a condition and associated workflow name.
        Condition checks event type and source.
        Automates workflow execution based on specific events.
    
    Workflow: Series of actions executed in response to an event.
    
        Represented as a graph of nodes in Tracardi.
        Actions assigned to individual nodes.
        Actions can perform various tasks and data manipulations.
    
    Actions: Individual tasks performed within a workflow.
    
        Receive data through input ports and send data through output ports.
        Code-based tasks mapped to input parameters and return values.
        Actions can be extended by custom code written by programmers.
    
    Profile: Detailed record or representation of an individual or entity.
    
        Contains information about characteristics, interests, and activities.
        Updated based on incoming events and data from external systems.
        Includes both public and private data.
    
    Segment: Group of customer profiles based on shared characteristics or behavior.
    
        Defined using logical rules or AI models.
        Part of the customer's profile.
        Used for targeted marketing and personalized experiences

    Destination - Outbound traffic:
        External system where profile data is sent from Tracardi.
        Requires a specific resource (API endpoint, queue service) for data processing.
        Not all resources are available as destinations in Tracardi.

    Customer consent:
        Permission obtained from individuals to collect, use, or share their personal data.
        Obtained through agreements, click-throughs, consent forms, etc.
        Important for data privacy and empowers individuals to control their data.

    Data compliance:
        Adherence to laws, regulations, and guidelines for handling data.
        Protects privacy, ensures transparency, and prevents misuse.
        Builds trust and confidence in data practices.

    Identification point:
        Feature allowing the system to identify customers during their journey.
        Anonymous until the identification point is reached.
        Monitors events to match anonymous data with identified profiles.
        Enables merging of previous interactions/events with the identified profile.

    Data flow stages in Tracardi:
        Source validation: Event source must be defined and enabled.
        Event data validation: Tracardi can validate the event data schema.
        Identity resolution: Identifies events that serve as identification points.
        Event reshaping: Tracardi can modify the event schema if necessary.
        Event collection: Events are saved in Tracardi.
        Event routing: Rules determine which workflow processes the event.
        Processing: Workflows enhance, process, and route event data.
        Profile merging: Checks if profiles can be merged after processing.
        Profile segmentation: Profiles are segmented based on system administrator's rules.

    Source validation:
        Data enters Tracardi through API endpoints (/track and /collect).
        Event sources must be enabled by the system administrator.
        Event source creation generates a token for data transfer.

    Event data validation:
        Ensures accuracy, completeness, and consistency of event data.
        Verifies data format and required fields.
        Important for data quality and reliable insights.

    Event collection:
        Gathering data about events in Tracardi.
        Events are described by types (e.g., purchase-order event).
        Events are stored in a central Elasticsearch database.
        Events can be saved or processed without an assigned user.

        Encrypted Connection:
        Set up an encrypted connection (HTTPS) when accessing the Tracardi API.
        Encode traffic sent to the load balancer for secure external communication.
        Consider preparing HTTPS versions of Tracardi Docker images for end-to-end encryption.

    Separation of Track Server and GUI API:
        Have two Tracardi API clusters: one for GUI and one for event collection.
        Configure the event collecting cluster with EXPOSE_GUI_API=no to limit available endpoints.
        Configure the GUI cluster with EXPOSE_GUI_API=yes to allow control of Tracardi through the GUI.

    Scaling:
        Scaling involves increasing or decreasing the capacity of the system to handle incoming traffic.
        Tracardi is stateless, making it easier to scale by adding or removing instances.
        Use Kubernetes, a container orchestration platform, to manage scaling and maintenance.
        Tracardi does not require long-lasting sticky sessions, allowing for easy instance restarts.

    Automated System Update:
        Automated system update is available from version 0.7.0 onward.
        Previous versions could only update the code and not the system data.
        Starting from version 0.7.0, Tracardi keeps information about indexes and uses aliases for data access.

    Update Process:
        During the upgrade, old version indexes are not modified and marked as previous versions (with .prev suffix).
        New empty indexes are created, along with new aliases.
        If the schema of the old index has not changed, the data pointer is switched to the new index.
        If the schema has changed, a migration script is used to rewrite and copy data between indexes.

    Prerequisites:
        Install dockers with tagged versions to ensure data continuity.
        The latest version may contain incorrect data, which can disrupt the update process.

    Installation of Version 0.7.0:
        Versions prior to 0.7.0 are not aware of previous data schemas.
        Manual data migration is required, such as re-indexing.
        If previous data is not important or can be lost, a fresh install is recommended.

    Manual Data Transfer:
        Check the existing indexes in Elasticsearch through Tracardi's Monitoring / Elasticsearch indices section.
        Connected indexes are currently in use and prefixed with a version number.
        Old indexes from previous versions are marked as Not Connected and have no prefix.
        Use the Elasticsearch reindex function to transfer data between indexes.
        Reindexing involves copying data from one index to another.

    To install Tracardi as a Docker container, follow these steps:

    Start Elasticsearch:

        Pull and run the Elasticsearch single-node Docker container with the following command:

        docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.13.2
    
        Note: Running a single instance of Elasticsearch is not suitable for production. For production purposes, you should set up an Elasticsearch cluster.

    Start Redis:
    
        Run the Redis instance with the following command:
    
        docker run -p 6379:6379 redis
    
    Start Tracardi API:
    
        Pull and run the Tracardi API Docker container:
    
        docker run -p 8686:80 -e ELASTIC_HOST=http://<your-laptop-ip>:9200 -e REDIS_HOST=redis://<your-laptop-ip>:6379 tracardi/tracardi-api
    
        Replace <your-laptop-ip> with the IP address of your machine.
        Make sure to set the ELASTIC_HOST variable to reference your Elasticsearch instance.
    
    Start Tracardi GUI:
    
        Pull and run the Tracardi GUI Docker container:
    
        docker run -p 8787:80 -e API_URL=//127.0.0.1:8686 tracardi/tracardi-gui
    
        Replace 127.0.0.1 with the IP address pointing to the Tracardi API.
    
    Import worker:
    
        To run the import worker, start the tracardi/update-worker Docker container:
    
        docker run -e REDIS_HOST=redis://<redis-ip>:6379 -d tracardi/update-worker:0.8.0
    
        Replace <redis-ip> with the IP address of the Redis instance.
    
    Access Tracardi GUI:
    
        Visit http://127.0.0.1:8787 in your web browser to access the Tracardi Graphical User Interface.
        Follow the instructions to set up Tracardi.
    
    Access System Documentation:
    
        For the local copy of the documentation, visit http://127.0.0.1:8585 in your web browser. Make sure the documentation Docker container is running.
    
    Access API Documentation:
    
        For the API documentation, visit http://127.0.0.1:8686/docs in your web browser.

    To build the Tracardi Docker image yourself, follow these steps:

        Clone the Tracardi repository:
    
        git clone https://github.com/tracardi/tracardi-api.git
        
        Navigate to the tracardi-api folder:
        
        cd tracardi-api/
        
        Build the Docker image:
        
        docker build . -t tracardi-api
        
        This command will build the Docker image with the tag tracardi-api. It may take some time to complete.
        
        Run the Docker container:
        
        docker run -p 8686:80 -e ELASTIC_HOST=http://<your-laptop-ip>:9200 tracardi-api
        
        Replace <your-laptop-ip> with the IP address of your machine.
        
        Note: When connecting to Elasticsearch, make sure to provide the external IP address instead of using localhost as it refers to the Docker container itself.
        
        On Windows, you can use the ipconfig command in the Command Prompt or PowerShell to find out your laptop's IP address.

    Software prerequisites:

        Docker
        Python 3.8
        Pip
        Python Virtual Environment
        PyCharm
        Git
    
    Launching Elasticsearch on Ubuntu:
    
        Option 1: Installing Elasticsearch as a Service:
            Import Elasticsearch public GPG key into APT using cURL.
            Add Elastic source list to the sources.list.d directory.
            Update package lists with APT.
            Install Elasticsearch using APT.
            Configure Elasticsearch by editing the elasticsearch.yml file.
            Start the Elasticsearch service with systemctl.
    
        Option 2: Installing Elasticsearch as a Docker container:
            Run the Elasticsearch Docker container command.
    
    Setting up Redis:
    
        Start Redis container using Docker.
    
    Downloading the source code:
    
        Clone the Tracardi and Tracardi API repositories using Git.
    
    Creating virtual environments:
    
        Create a Python virtual environment for Tracardi API and Tracardi.
    
    Installing dependencies:
    
        Activate the virtual environment for Tracardi API.
        Install wheel package.
        Install dependencies using pip.
    
    Running Tracardi:
    
        Run the Tracardi API with the specified command.
    
    Note: Make sure to replace placeholders like <your-laptop-ip> and <redis-ip> with appropriate values as mentioned in the installation instructions.

    Tracardi API Cluster:

        Set up a cluster with at least 5 instances of Tracardi API.
        Configure one cluster for public access and another for internal access.
        For the public cluster, set the EXPOSE_GUI_API environment variable to "no" to only allow access to the /track endpoint for event collection.
        For the internal cluster, set the EXPOSE_GUI_API environment variable to "yes" to enable GUI control of Tracardi.
    
    Tracardi GUI Cluster:
    
        Set up a cluster with 2 instances of Tracardi GUI.
        Restrict access to the GUI cluster to a trusted network or specific IP addresses for security reasons.
    
    Load Balancing:
    
        Hide the clusters behind a load balancer to expose a single IP to the world and distribute external traffic to individual instances.
        Create multiple load balancer instances to avoid a single point of failure.
        Configure DNS servers to return multiple A records (IP addresses) for your domain to support load balancing.
    
    Scalability and Failure Handling:
    
        Each instance of Tracardi API should be run on a separate server to enable failover in case of an instance failure.
        Install Tracardi inside a Kubernetes (k8s) environment to benefit from automatic recovery of failed Docker instances.
    
    HTTPS Configuration:
    
        If Tracardi is running in HTTPS mode, ensure the load balancer accepts encrypted traffic.
        Requests within the cluster can remain unencrypted to simplify certificate management for each Tracardi instance.


    Tracardi installation:
        
        Services:
        
            GUI: Not exposed to the internet, accessible only via VPN.
            Collector API: Exposed to the internet, limited to data collection, no GUI functionality.
            Production API: Not exposed to the internet, accessible via VPN, provides access to production data.
            Staging API: Not exposed to the internet, accessible via VPN, provides access to test data.
            Scheduler: Service for rescheduling delayed events.
            Scheduler Worker: Executes delayed events.
            Segmentation Job: Periodically checks profiles for segmentation.
            Segmentation Worker: Runs the defined segmentation process.
            Update and Migration: Workers for system migration and data import.
            Bridges: Services for collecting data from different channels and bridging the transportation protocol to the Tracardi event source.
        
        Docker Containers:
        
            GUI: Docker container for the GUI service.
            Collector API: Docker container for the Collector API service.
            Production API: Docker container for the Production API service.
            Staging API: Docker container for the Staging API service.
            Scheduler: Docker container for the Scheduler service.
            Scheduler Worker: Docker container for the Scheduler Worker service.
            Segmentation Job: Docker container for the Segmentation Job service.
            Segmentation Worker: Docker container for the Segmentation Worker service.
            Update and Migration: Docker container for the Update and Migration service.
            Bridges: Docker containers for the Bridges services.

    Staging Server Deployment:

        Install a separate copy of Tracardi designated as the staging server.
        Set the "PRODUCTION" environment variable to "no" during installation.
        Create a new set of Elasticsearch indices for the staging server.
        Expose the staging server on a different port than the production server.
        Ensure that the staging server is not accessible from the internet and is only accessible within the internal network, preferably through a VPN.
    
    Production Server Deployment:
    
        Install another copy of Tracardi designated as the production server.
        Set the "PRODUCTION" environment variable to "yes" during installation.
        Create a new set of Elasticsearch indices prefixed with "prod-" for the production server.
    
    Staging Server Security and Networking:
    
        Separate the staging and production servers by assigning different API IP addresses.
        Ensure that the staging server is not exposed to the internet and is only accessible within the internal network, preferably through a VPN.
        Limit access to the production server, allowing only a single admin account and marketing accounts with view-only access to data.
    
    Licensing Commercial Version:
    
        Commercial licenses for Tracardi cover both staging and production servers, so separate licenses are not required.
    
    Best Practices For Using Tracardi:
    
        Make changes to Tracardi on the staging server and thoroughly test them before deploying to the production system.
        Avoid editing the production server directly.
        Copy data from the staging server to the production server during deployment, excluding certain data like events, profiles, or error logs to maintain the integrity of the production data.

    Steps to install commercial version

        Login to Docker Hub with your credentials by running the following command:
        
        docker login
        
        Paste the credentials that have been provided to you.
        
        Create a file named .env-docker and paste the license key provided to you into it. The file should contain the following line:
        
        API_LICENSE="paste license here"
        
        If you are using Linux, run the following commands to set environment variables:
        
        set -a
        source .env-docker
        
        Run the com-docker-compose.yaml file as the Docker Compose configuration:
        
        docker-compose -f com-docker-compose.yaml up

        Javascript Integration

            To integrate Tracardi, send events to the /track endpoint using the POST method.
            The payload should be in JSON format and include the following fields:
                source.id: UUID that identifies the source.
                session.id: UUID generated and saved on the client side to track a session.
                profile.id: UUID of the profile ID that remains unchanged during the customer journey.
                context: JSON data describing the context of the event (e.g., agent type, service name).
                properties: An object for event-specific properties.
                events: A collection of event objects, each with a type, properties, options, and context.
                options: Additional key-value pairs for options.
            Tracardi can handle multiple events in a single request.
            The required fields are source.id, session.id, profile.id, and at least one event in the events collection.
            You can obtain the profile ID by sending the tracker payload without setting the profile ID, and Tracardi will return the generated profile ID in the response.
            The profile ID and session ID should be included in every call to the /track endpoint.
            Tracardi aims to keep the profile unchanged, so it's important to save and include the correct profile ID in subsequent requests.
            Sessions in Tracardi represent visits and can change when the user closes the browser or logs out.
            Changing the session ID while keeping the profile unchanged is possible by providing the profile ID with a new session ID.
            It's recommended to generate a new session ID for each visit to ensure accurate tracking and profiling of user behavior.

    Integrating Tracardi with mobile apps or external systems:

        Obtain Tracardi JavaScript Snippet (for web apps): Tracardi provides a JavaScript snippet for web apps, but manual integration is required for mobile apps or external systems.
    
        Save Profile ID and Session ID: Manually save the Profile ID and Session ID on the customer's device or within the backend system. For mobile apps, use local storage or appropriate storage mechanisms. For backend systems, save them within the defined user session (e.g., PHPSESSIONID or relevant tokens).
    
        Track Events Manually: Construct and send the tracker payload to the Tracardi /track endpoint when relevant events occur in the mobile app or external systems. Follow the tracker payload format, including necessary fields and event-specific data.
    
        Consistent Profile ID and Session ID: Maintain consistency between the saved Profile ID and Session ID, including them in every call to the /track endpoint. If the received profile ID differs, update the saved profile ID to avoid synchronization issues.
    
        Ensure Accurate Tracking and Personalization: Saving and including the correct Profile ID and Session ID enables Tracardi to accurately track and personalize customer interactions. This data forms the foundation for effective marketing automation, personalization, and analysis in Tracardi.

     Integration with a web page using the JavaScript snippet.
        
        Step 1: Connecting the JavaScript Snippet
        
            Paste the provided JavaScript snippet at the beginning of the <script> tag in the header of your web page.
            The snippet includes the Tracardi JavaScript code and allows you to configure the tracker URL and event source ID.
            Make sure to replace <your-event-source-id-HERE> with the actual event source ID from Tracardi.
        
        Step 2: Sending Events via JavaScript
        
            Define events in a separate script section.
            Use the window.tracker.track function to send events with their respective event types and additional data.
            Place the event code after the configuration code to ensure proper execution.
        
        Step 3: Refreshing the Page and Verifying the Response
        
            After refreshing the web page, you may encounter an "Access denied. Invalid source" response from Tracardi.
            This occurs when the event source ID is not defined or incorrect in the JavaScript snippet.
            To resolve this, create an event source in Tracardi and replace the event source ID in the snippet with the actual ID from Tracardi.
            Additionally, replace the IP address in the snippet (192.168.1.103) with the address of your Tracardi server.

    The Tracardi JavaScript integration allows you to extend event information and configure various settings. Here's an explanation of the different aspects:
    
        Event Context: Event context in Tracardi allows you to pass additional information about events. This data is saved in the session and remains constant throughout the session. The default context includes browser data, screen data, and page data. You can extend the context with cookies and local storage data by setting storage: true in the context configuration.
    
        Event Performance Metrics: By enabling tracker.context.performance, you can include performance metrics in the event context. This includes data such as page load times, network timings, etc.
    
        Append Profile ID to External Links: The tracking script can include the current profile ID, session ID, and source ID in the URL parameters of external links. This allows for consistent profile ID persistence across domains that use the same Tracardi system. You can enable this functionality by adding trackExternalLinks: ['example.com', 'tracardi.com'] in the settings. Any links with URLs ending in the specified domains will be updated with the profile ID and source ID parameters.
    
        Disabling Parameters and Session Context: If you want to disable the profile ID and source ID parameters (__tr_pid, __tr_src) and turn off session context, you can set tracardiPass: false in the tracker context.
    
        Respecting Do Not Track (DNT): You can respect the user's browser setting for Do Not Track (DNT) by setting respectDoNotTrack: true in the settings. If the user has enabled DNT, Tracardi will not load the tracking script.

    In Tracardi, event options allow you to customize the behavior of events and add contextual information to them. When triggering events using the Tracardi JavaScript snippet, default context information is automatically included, such as browser details and metadata. Here's an overview of event options in Tracardi:

        Default Event Context: The default event context includes information about the current page, such as its URL, path, hash, title, referer information, and browsing history length. It also includes the user's IP address.

    Customizing Event Context: You can add additional context information to events by including a "context" key in the options when triggering events. This allows you to include custom data that is relevant to your specific use case. For example:

        window.tracker.track("page-view", {}, {"context": {"tag": "search"}});
        
        In the above example, a custom context object with the key "tag" and value "search" is added to the event options.
        
            Beacon Tracks: Beacon events in Tracardi are events that are sent even if the customer leaves the page. These events allow you to track user interactions that occur after a user has navigated away from a page. To configure a beacon event, you can add the asBeacon: true option to the track configuration. For example:
        
        window.tracker.track("page-view", {}, {"fire": true, "asBeacon": true});
        
        In the above example, the asBeacon option is set to true, indicating that the "page-view" event should be sent as a beacon event, even if the customer leaves the page. Beacon events are useful for tracking interactions that occur outside of the webpage.
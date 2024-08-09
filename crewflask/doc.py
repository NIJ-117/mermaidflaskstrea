mermaid_documentation="""Certainly! Let's verify and correct the example code for creating mind maps using Mermaid.js. Here are the key points and corrected examples:

### 1. Basic Mindmap Syntax

```mermaid
mindmap
    Root
        A
            B
            C
```

### 2. Different Shapes

Mermaid mind maps can display nodes using various shapes. Here’s how to specify them:

```mermaid
mindmap
    root((Root))
        A(Square)
        B((Rounded Square))
        C(Circle)

```


### 4. Complex Example with Multiple Levels

Here’s a more detailed example with multiple levels, shapes, and icons:

```mermaid
mindmap
    root((mindmap))
        Origins
            "Long history" ::icon(fa fa-book)
            Popularisation
                "British popular psychology author Tony Buzan"
        Research
            "On effectiveness<br/>and features"
            "On Automatic creation"
                Uses
                    "Creative techniques"
                    "Strategic planning"
                    "Argument mapping"
        Tools
            "Pen and paper"
            Mermaid
```

### 5. Practical Examples

Mind mapping can be used in various scenarios such as IT solution design and business decision-making. Here’s another practical example:

```mermaid
mindmap
    Goals
        "Family"
            "Plan a trip together"
            "Call parents weekly"
        "Health"
            "Less Carbs"
            "Gym"
            "Nature walks"
        "Career"
            "Learn new skill"
            "Read more books"
        "Fun"
            "Join Swim class"
            "Go to theatre plays"
```

### Common Issues and Fixes

- **Indentation:** Ensure that the indentation is consistent as Mermaid.js relies on indentation to determine the hierarchy.
- **Special Characters:** Use quotes for node labels that contain spaces or special characters.
- **Line Breaks:** Use `<br/>` for line breaks within node labels.



"""

flowchart_documentation="""

# Advanced Network Diagram Documentation with Mermaid.js

This guide provides detailed instructions on creating advanced network diagrams using Mermaid.js, with a focus on the use of subgraphs and advanced techniques. The documentation includes examples ranging from simple setups to complex, multi-tier architectures, tailored to network visualization.

## Basic Syntax

### 1. **Graph Definition**
   - Start your network diagrams with a graph definition.
   - Syntax: `graph LR` (Left to Right), `graph TB` (Top to Bottom).
   - Example: `graph TB` is often used for hierarchical network diagrams.

### 2. **Nodes**
   - Nodes represent network devices, services, or other components.
   - Syntax: `[ID]["Node Label"]`.
   - Example: `LB["Load Balancer"]`.

### 3. **Edges**
   - Edges depict the connections between nodes, such as data flow or network links.
   - Syntax: `[ID1] --> [ID2]` for a direct connection.
   - Example: `LB --> WS` shows a connection from a Load Balancer to Web Servers.

### 4. **Direction**
   - Choose the direction that best suits your network layout.
   - Options: `LR` (Left to Right), `TB` (Top to Bottom), `RL` (Right to Left), `BT` (Bottom to Top).

## Advanced Features

### 1. **Subgraphs**
   - Subgraphs are essential for organizing complex network diagrams, allowing you to group related components.
   - Syntax:
     ```mermaid
     subgraph "Group Name"
         [ID1] --> [ID2]
     end
     ```
   - Example:
     ```mermaid
     subgraph "Backend Services"
         APIG["API Gateway"] --> AS["Application Servers"]
         AS --> DB["Database Cluster"]
     end
     ```
   - **Advanced Usage**:
     - Use subgraphs to represent entire data centers, cloud regions, or network segments.
     - Nest subgraphs to show hierarchical relationships, such as a service cluster within a data center.

### 2. **Styling**
   - Customize nodes and edges to visually distinguish different network elements.
   - Example: `[DB]["Database"] {stroke: #333; fill: #FFF}` can be used to highlight a database node.

### 3. **Special Arrows and Links**
   - Different arrow types can be used to represent different types of connections, such as encrypted links, replication paths, or VPNs.
   - Example: `[ID1] -.-> [ID2]` represents a dotted arrow, useful for indicating non-critical paths like backup links.

### 4. **Interactive Elements**
   - Bind click events to nodes to link them to external resources, such as documentation, monitoring dashboards, or management interfaces.
   - Example:
     ```html
     click LB "http://your-dashboard-url.com" "Load Balancer Dashboard"
     ```

## Examples

### 1. **Simple Network Diagram**
   ```mermaid
   graph TB
     LB["Load Balancer"] --> WS["Web Server"]
     WS --> DB["Database"]
   ```
   **Explanation**:
   - A basic network diagram illustrating a Load Balancer connecting to a Web Server, which in turn connects to a Database.

### 2. **Network Diagram with Subgraphs**
   ```mermaid
   graph TB
     subgraph "Frontend Services"
         LB["Load Balancer"] --> WS["Web Servers"]
         WS --> FE["Frontend Application"]
     end
     subgraph "Backend Services"
         APIG["API Gateway"] --> AS["Application Servers"]
         AS --> DB["Database Cluster"]
         AS --> CA["Cache"]
     end
     FE --> APIG
   ```
   **Explanation**:
   - The diagram uses subgraphs to organize frontend and backend services, showing clear connections between these components.

### 3. **Advanced Network with Redundancy**
   ```mermaid
   graph LR
     subgraph "Data Center 1"
         LB1["Load Balancer 1"] --> WS1["Web Server 1"]
         WS1 --> DB1["Database 1"]
         DB1 -.-> BA1["Backup Server 1"]
     end
     subgraph "Data Center 2"
         LB2["Load Balancer 2"] --> WS2["Web Server 2"]
         WS2 --> DB2["Database 2"]
         DB2 -.-> BA2["Backup Server 2"]
     end
     LB1 -.-> LB2
     DB1 -.-> DB2
   ```
   **Explanation**:
   - This diagram represents a more advanced setup with redundancy across two data centers, including load balancers, web servers, databases, and backup servers.

### 4. **Complex Multi-Region Cloud Architecture**
   ```mermaid
   graph TB
     subgraph "AWS Region 1"
         direction TB
         FW1["Firewall"] --> VPC1["VPC 1"]
         VPC1 --> LB1["Load Balancer"]
         LB1 --> WS1["Web Server"]
         WS1 --> AS1["Application Server"]
         AS1 --> RDS1["RDS Database"]
     end
     subgraph "AWS Region 2"
         direction TB
         FW2["Firewall"] --> VPC2["VPC 2"]
         VPC2 --> LB2["Load Balancer"]
         LB2 --> WS2["Web Server"]
         WS2 --> AS2["Application Server"]
         AS2 --> RDS2["RDS Database"]
     end
     subgraph "Centralized Services"
         MON["Monitoring System"] --> LOG["Logging Service"]
         AS1 --> LOG
         AS2 --> LOG
     end
     RDS1 -. Replication .-> RDS2
     LB1 -.-> LB2
   ```
   **Explanation**:
   - This complex diagram represents a multi-region cloud architecture using AWS, with redundancy and replication between regions, and centralized monitoring and logging services.

### 5. **Microservices with Message Queue and Monitoring**
   ```mermaid
   graph TB
     subgraph "Frontend"
         LB["Load Balancer"] --> FE["Frontend Application"]
     end
     subgraph "Microservices"
         AUTH["Auth Service"] --> USER["User Service"]
         AUTH --> ORD["Order Service"]
         USER --> PROD["Product Service"]
         PROD --> ORD
         ORD --> MQ["Message Queue"]
     end
     subgraph "Data Storage"
         USER_DB["User Database"] --> USER
         PROD_DB["Product Database"] --> PROD
         ORD_DB["Order Database"] --> ORD
     end
     subgraph "Monitoring & Logging"
         MON["Monitoring System"] --> LOG["Logging Service"]
         AUTH --> LOG
         USER --> LOG
         PROD --> LOG
         ORD --> LOG
         MQ --> MON
         MQ --> LOG
     end
     FE --> AUTH
     FE --> USER
     FE --> PROD
     MQ --> MON
   ```
   **Explanation**:
   - This example shows a microservices architecture with a message queue for asynchronous communication and a monitoring system to track the performance of each service.

### 6. **Network Security Architecture**
   ```mermaid
   graph TB
     subgraph "Perimeter Security"
         FW["Firewall"] --> IDS["Intrusion Detection System"]
         IDS --> WAF["Web Application Firewall"]
     end
     subgraph "Internal Network"
         VPN["VPN Gateway"] --> LB["Load Balancer"]
         LB --> WS["Web Server"]
         WS --> DB["Database"]
     end
     subgraph "Backup & Recovery"
         DR["Disaster Recovery Site"] --> BA["Backup Server"]
         BA -.-> DB
     end
     WAF --> VPN
     DB --> DR
   ```
   **Explanation**:
   - This diagram focuses on network security, including perimeter defenses (firewall, IDS, WAF) and internal protections (VPN, load balancing), with a disaster recovery plan in place.

### 7. **Complex Workflow with Multiple Decisions and Parallel Processes**
   ```mermaid
   graph TB
     A["Start"] --> B{"Choose option"}
     B -->|Option 1| C1["Process 1"]
     B -->|Option 2| C2["Process 2"]
     B -->|Option 3| C3["Process 3"]
     C1 --> D["Parallel Process"]
     C2 --> D
     C3 --> D
     D --> E{"Check condition"}
     E -->|Condition Met| F["Final Step"]
     E -->|Condition Not Met| G["Re-evaluate"]
     G --> B
     F --> H["End"]
   ```
   **Explanation**:
   - **Decision Point (B)**: The workflow starts with a decision node where the user can choose between three options (Option 1, Option 2, Option 3). Each option leads to a different process (C1, C2, C3).
   - **Parallel Process (D)**: All three processes converge at a parallel processing node (D), where they proceed together.
   - **Conditional Check (E)**: After the parallel process, the workflow encounters another decision point where a condition is checked. Depending on the outcome:
     - If the condition is met, the workflow proceeds to the final step (F).
     - If the condition is not met, the workflow loops back to the initial decision point (B) for re-evaluation.
   - **End (H)**: The workflow ends after completing the final step.

   **Common Errors to Avoid**:
   - **Misformatted Connections**: Ensure that the

 conditions are correctly formatted within the connections. For example, the correct format is `E -->|Condition Met| F["Final Step"]`. An incorrect format would be `E -->|Condition Met| >F["Final Step"]`.
   - **Arrow Directions**: Ensure that all arrows (`-->`, `---`, etc.) are pointing in the correct direction, especially when dealing with parallel processes or loops.
   - **Consistent Labeling**: Ensure that node labels are consistently used and match exactly in all references.

## Best Practices for Network Diagrams

1. **Organize Components Logically**: Use subgraphs to group related network elements, such as all services in a particular region or data center.
2. **Clear and Descriptive Labels**: Ensure all nodes and edges are clearly labeled for easy interpretation.
3. **Utilize Styling for Clarity**: Differentiate between types of nodes (e.g., servers, databases, firewalls) and connections (e.g., secure vs. non-secure) with custom styles.
4. **Add Interactivity**: Where applicable, make diagrams interactive by linking nodes to additional resources or management tools.
5. **Show Redundancy and Failover Paths**: Highlight critical paths, redundancy, and failover mechanisms to ensure the diagram communicates the resilience of the network architecture.

---

This updated documentation provides a comprehensive resource for creating sophisticated network diagrams with Mermaid.js, including a variety of examples and advanced techniques to enhance your diagrams' clarity and functionality.
"""

Class_documentation="""
### Mermaid.js Class Diagram Documentation with Intermediate Examples

Mermaid.js provides a simple yet powerful syntax for creating class diagrams, which are essential for visualizing the structure of object-oriented systems. Below is a comprehensive guide to help you understand and utilize Mermaid.js for class diagrams.

#### Basic Syntax
1. **Class Definition**:
   - Classes are defined using the `class` keyword followed by the class name and its members.
   - Example:
     ```mermaid
     classDiagramimport os
from crewai import Agent, Task, Crew, Process
from agent import network_architect
from task import task1

question="How can Kubernetes clusters be deployed and managed across AWS, GCP, and Azure for a seamless multi-cloud strategy?"

crew=Crew(
  agents=[network_architect],
  tasks=[task1],
  verbose=2  # You can set it to 1 or 2 for different logging levels
)

re= crew.kickoff()ifiers**:
   - `+` for public members.
   - `-` for private members.
   - `#` for protected members.
   - `~` for package/internal members.
   - Example:
     ```mermaid
     class Animal {
       +String name
       -int age
       #eat()
     }
     ```

3. **Relationships**:
   - Inheritance: `<|--`
   - Composition: `*--`
   - Aggregation: `o--`
   - Association: `-->`
   - Example:
     ```mermaid
     classDiagram
       Animal <|-- Dog
       Animal <|-- Cat
       Dog o-- Owner
     ```

4. **Annotations**:
   - Annotations can denote special types like `<<interface>>`, `<<abstract>>`, etc.
   - Example:
     ```mermaid
     classDiagram
       class Animal {
         +String name
         +int age
         +eat()
       }
       class Dog {
         +String breed
       }
       class Cat {
         +String furColor
       }
       Animal <|-- Dog
       Animal <|-- Cat
     ```

#### Intermediate Examples

1. **Class Diagram with Interfaces and Abstract Classes**:
   ```mermaid
   classDiagram
     class GameObject {
       +String name
       +int x
       +int y
       +render()
     }
     class Character {
       <<abstract>>
       +int health
       +move()
     }
     class Player {
       +String username
       +int score
     }
     class Enemy {
       +String type
       +int damage
     }
     GameObject <|-- Character
     Character <|-- Player
     Character <|-- Enemy
   ```

   **Explanation**:
   - `GameObject` is a base class.
   - `Character` is an abstract class with health and move methods.
   - `Player` and `Enemy` inherit from `Character`.

2. **Class Diagram with Generics and Static Members**:
   ```mermaid
   classDiagram
     class Repository~T~ {
       -List~T~ items
       +addItem(T item)
       +getItem(int index) T
     }
     class Item {
       +String name
       +double price
     }
     Repository~Item~ *-- Item
   ```

   **Explanation**:
   - `Repository~T~` is a generic class.
   - `Item` is a class representing items.
   - The repository manages items with a composition relationship.

3. **Complex Class Diagram with Notes and Multiplicity**:
   ```mermaid
   classDiagram
     note "This is a note for the whole diagram"
     note for Player "This class represents the player character"
     class Game {
       +String title
       +start()
     }
     class Player {
       +String name
       +int level
       +gainXP(int xp)
     }
     class Enemy {
       +String type
       +int health
       +attack(Player player)
     }
     Game "1" --> "*" Player
     Game "1" --> "*" Enemy
   ```

   **Explanation**:
   - The diagram includes notes for additional context.
   - `Game` has one-to-many relationships with `Player` and `Enemy`.

These examples and the comprehensive syntax guide should help you get started with creating detailed class diagrams using Mermaid.js. For more detailed information and additional features, you can refer to the [official Mermaid.js documentation](https://mermaid.js.org/syntax/classDiagram.html) and other resources such as [Swimm](https://swimm.io) and [New Dev's Guide](https://newdevsguide.com).
"""

Sequence_Documentation="""
### Mermaid.js Sequence Diagram Documentation

Sequence diagrams in Mermaid.js are a powerful way to visualize interactions between components or participants in a system. Here’s a comprehensive guide to creating sequence diagrams with Mermaid.js, including intermediate examples.

#### Basic Syntax

1. **Participants**:
   - Define participants using the `participant` keyword.
   - Example:
     ```mermaid
     sequenceDiagram
       participant Alice
       participant Bob
     ```

2. **Messages**:
   - Messages are represented by arrows between participants.
   - Types of arrows include:
     - `->` Solid line without arrowhead
     - `->>` Solid line with arrowhead
     - `-->` Dotted line without arrowhead
     - `-->>` Dotted line with arrowhead
   - Example:
     ```mermaid
     sequenceDiagram
       Alice->>Bob: Hello Bob
       Bob-->>Alice: Hi Alice
     ```

3. **Activations**:
   - Activate a participant using `activate` and `deactivate`.
   - Shortcut: Use `+` to activate and `-` to deactivate.
   - Example:
     ```mermaid
     sequenceDiagram
       Alice->>+Bob: Hello Bob
       Bob-->>-Alice: Hi Alice
     ```

4. **Notes**:
   - Add notes to provide additional context.
   - Example:
     ```mermaid
     sequenceDiagram
       Alice->>Bob: Hello Bob
       Note right of Bob: Bob thinks
       Bob-->>Alice: Hi Alice
     ```

5. **Loops and Conditionals**:
   - Use `loop`, `alt`, `opt`, and `par` for complex control flows.
   - Example:
     ```mermaid
     sequenceDiagram
       participant Alice
       participant Bob
       loop Every day
         Alice->>Bob: Hello Bob
         alt Is Bob there?
           Bob-->>Alice: Hi Alice
         else
           Bob-->>Alice: I am not available
         end
       end
     ```

6. **Background Highlighting**:
   - Highlight parts of the diagram using `rect`.
   - Example:
     ```mermaid
     sequenceDiagram
       participant Alice
       participant Bob
       rect rgb(191, 223, 255)
       Alice->>Bob: Hello Bob
       Bob-->>Alice: Hi Alice
       end
     ```

7. **Comments**:
   - Add comments using `%%`.
   - Example:
     ```mermaid
     sequenceDiagram
       %% This is a comment
       Alice->>Bob: Hello Bob
     ```

#### Intermediate Examples

1. **Login Process with Conditions**:
   ```mermaid
   sequenceDiagram
     autonumber
     actor Client
     participant Server
     participant DB as Database
     Client->>+Server: Login (Username, Password)
     Server->>+DB: Select User Info
     note over DB: Password is not stored in database
     DB-->>-Server: Salt & Hash
     Server->>Server: Check Computed Hash using Salt
     alt Computed Hash Matches
       Server->>Server: Generate JWT
       Server-->>Client: 200 OK & JWT
     else No user or wrong password
       Server-->>Client: 401 Unauthorized
     end
     note over Client, Server: Subsequent requests include JWT
   ```

2. **Complex Workflow with Parallel Actions**:
   ```mermaid
   sequenceDiagram
     participant Frontend
     participant Backend
     participant DB as Database
     par
       Frontend->>Backend: Request Data
       and
       Backend->>DB: Query Database
       DB-->>Backend: Return Data
       and
       Backend-->>Frontend: Response Data
     end
   ```

3. **Activation and Deactivation with Nested Conditions**:
   ```mermaid
   sequenceDiagram
     actor User
     participant AuthServer as Authentication Server
     participant App as Application
     User->>+AuthServer: Login Request
     activate AuthServer
       AuthServer->>+DB: Verify Credentials
       activate DB
         DB-->>-AuthServer: Verification Result
       deactivate DB
       alt Valid Credentials
         AuthServer->>App: Provide Token
         App-->>User: Login Success
       else Invalid Credentials
         AuthServer-->>User: Login Failure
       end
     deactivate AuthServer
     ```

                                                                                  
"""



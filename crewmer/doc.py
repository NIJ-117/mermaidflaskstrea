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
Creating comprehensive documentation for Mermaid.js flowcharts involves covering basic syntax, advanced features, and various examples. Here's a detailed guide to help you understand and utilize Mermaid.js effectively:

### Basic Syntax

1. **Graph Definition**:
   - Mermaid flowcharts begin with a graph definition.
   - Syntax: `graph LR` (Left to Right), `graph TB` (Top to Bottom).

2. **Nodes**:
   - Nodes are defined with unique identifiers followed by square brackets containing the node label.
   - Example: `A["Node A"]`.

3. **Edges**:
   - Edges are arrows or lines that connect nodes.
   - Syntax: `A --> B` (arrow), `A --- B` (line).

4. **Direction**:
   - The direction of the graph can be specified as `LR` (Left to Right), `TB` (Top to Bottom), `RL` (Right to Left), `BT` (Bottom to Top).

### Advanced Features

1. **Subgraphs**:
   - Group related nodes together for better organization.
   - Syntax:
     ```mermaid
     subgraph "Subgraph Title"
         A --> B
         B --> C
     end
     ```

2. **Styling**:
   - Customize the appearance of nodes and edges using CSS-like syntax.
   - Example: `A["Node A"] {stroke: #333; fill: #FFF}`.

3. **Special Arrows and Links**:
   - Support for different arrow types (normal, thick, dotted).
   - Example: `A ==> B` (thick arrow), `A -.-> B` (dotted arrow).

4. **Markdown Strings**:
   - Support for text formatting within node labels using Markdown.
   - Example: `A["**Bold Text** and *italic text*"]`.

5. **Interactive Elements**:
   - Bind click events to nodes, linking to JavaScript functions or URLs.
   - Example:
     ```html
     click A callback "Tooltip text"
     ```

### Examples

1. **Simple Flowchart**:
   ```mermaid
   graph TD
     A["Start"] --> B{"Is it?"}
     B -->|Yes| C["OK"]
     B -->|No| D["Not OK"]
   ```

2. **Complex Flowchart with Subgraphs**:
   ```mermaid
   graph LR
     subgraph "Cluster 1"
       A["Node A"] --> B["Node B"]
     end
     subgraph "Cluster 2"
       C["Node C"] --> D["Node D"]
     end
     A --> C
   ```

3. **Customized Shapes and Links**:
   ```mermaid
   graph TD
     A["Client"] --> B["Server"]
     B --> C["(Database)"]
     C -.-> D{"Decision"}
   ```

### Intermediate to Advanced Examples

#### Example 1: Flowchart with Conditionals and Loops

This example demonstrates how to create a flowchart that includes decision points and loops, common in programming logic and workflow diagrams.

```mermaid
graph TD
  A["Start"] --> B{"Is it a weekday?"}
  B -->|Yes| C["Go to work"]
  B -->|No| D["Stay at home"]
  C --> E{"Do you have meetings?"}
  E -->|Yes| F["Prepare for meetings"]
  E -->|No| G["Do regular work"]
  F --> H["Meetings finished"]
  G --> H
  H --> I["End of day"]
  D --> I
```

**Explanation**:
- The flowchart starts at node `A`.
- At node `B`, a decision is made whether it's a weekday or not.
- Depending on the decision, the flow either goes to `C` (Go to work) or `D` (Stay at home).
- If at work, another decision at `E` checks for meetings, leading to either `F` (Prepare for meetings) or `G` (Do regular work).
- The flow eventually leads to `I` (End of day).

#### Example 2: Flowchart with Subgraphs

This example uses subgraphs to group related nodes, which is useful for depicting different modules or systems within a larger process.

```mermaid
graph LR
  subgraph "Backend"
    A["Server"] --> B["Database"]
    B --> C["Cache"]
  end
  subgraph "Frontend"
    D["Browser"] --> E["API"]
  end
  E --> A
```

**Explanation**:
- The `Backend` subgraph contains nodes for the server, database, and cache.
- The `Frontend` subgraph contains nodes for the browser and API.
- The API connects to the server, indicating interaction between the frontend and backend.

#### Example 3: Customized Flowchart with Styling and Icons

This example shows how to apply custom styles and use Font Awesome icons to enhance the visual representation of a flowchart.

```mermaid
graph LR
  subgraph "Azure"
    S["fa:fa-server Server"] --> D["(fa:fa-database Database)"]
  end
  subgraph "Netlify"
    C["fa:fa-user Client"]
  end
  C -- "HTTP GET" --> S
  S -- "SQL Query" --> D
  D -. "Result Set" .-> S
  S -. "JSON" .-> C
```

**Explanation**:
- The `Azure` subgraph includes a server and database with icons.
- The `Netlify` subgraph includes a client with an icon.
- The flow includes HTTP and SQL interactions between the client, server, and database.

#### Example 4: Complex Workflow with Multiple Decisions and Parallel Processes

This advanced example demonstrates a complex workflow involving multiple decision points and parallel processes.

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
- The workflow starts at `A`.
- A decision at `B` leads to three different processes (`C1`, `C2`, `C3`).
- All processes converge at `D`, a parallel process node.
- A condition check at `E` determines the next step, leading to either `F` (Final Step) or `G` (Re-evaluate).
- If re-evaluating, the flow loops back to the initial decision point `B`.

flowchart TD
  %% Subgraph for Backend Services
  subgraph Backend Services
    direction TB
    A["Database"] --> B["API Server"]
    B --> C["Authentication Service"]
    C --> D["Cache"]
  end

  %% Subgraph for Frontend Services
  subgraph Frontend Services
    direction TB
    E["Load Balancer"] --> F["Web Server"]
    F --> G["Frontend Application"]
  end

  %% Connections between subgraphs
  D --> E
  G -->|"User Request"| H[("User")]




By using double quotes for node labels, you ensure that any special characters, including brackets, are properly handled, reducing the risk of syntax errors in your Mermaid diagrams.

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



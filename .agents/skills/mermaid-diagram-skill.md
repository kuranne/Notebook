---
name: mermaid-diagram-expert
description: >-
  Authoritative, syntax-complete reference and design guidelines for creating Mermaid diagrams
  (Flowcharts, Sequence, Class, ER, State, GitGraph, Gantt, Mindmap) inside Obsidian and Markdown vaults.
when_to_use: |
  - Creating architectural diagrams, program flowcharts, or system state machines in Markdown
  - Modeling object-oriented class hierarchies and database entity-relationships (ERD)
  - Visualizing sequence interactions, microservice protocols, and Git workflows
  - Debugging Mermaid rendering syntax errors in Obsidian
license: MIT
metadata:
  author: Gemini Notebook
  version: 1.0.0
---

# Mermaid Diagram Specification & Design Patterns Skill

## Purpose
This skill provides comprehensive instructions, code templates, relationship markers, and formatting patterns for writing spec-compliant Mermaid diagrams inside Obsidian notes.

---

## 1. Syntax Foundations & Fencing

All Mermaid diagrams in Markdown must be enclosed in fenced code blocks tagged with `mermaid`:

````markdown
```mermaid
flowchart TD
    A[Start] --> B{Condition}
    B -- Yes --> C[Process]
    B -- No --> D[Alternative]
    C --> E[End]
    D --> E
```
````

### Rules for Obsidian Compatibility:
1. **Node IDs**: Must be alphanumeric without spaces or punctuation (e.g., `userAuthService`, `node_1`). Use display labels for text.
2. **Text Escaping**: Any label containing parentheses `()`, brackets `[]`, braces `{}`, or colons `:` **must be enclosed in double quotes**: `nodeA["Function: processData(x)"]`.
3. **Directional Flow**:
   - `TD` / `TB`: Top-Down / Top-to-Bottom
   - `BT`: Bottom-to-Top
   - `LR`: Left-to-Right
   - `RL`: Right-to-Left

---

## 2. Flowcharts (`flowchart TD` / `flowchart LR`)

### 2.1 Node Shapes

| Shape Name | Syntax | Description |
| :--- | :--- | :--- |
| **Rectangle (Default)** | `id[Text]` | Standard process step |
| **Rounded Rectangle** | `id(Text)` | Start / End / Soft step |
| **Stadium (Pill)** | `id([Text])` | Terminal / Program boundary |
| **Subroutine** | `id[[Text]]` | Predefined process / module |
| **Cylindrical (Database)** | `id[(Database / Storage)]` | Database, cache, or storage |
| **Circle** | `id((Text))` | State / Connector |
| **Asymmetric Flag** | `id>Text]` | Flag / Message trigger |
| **Rhombus (Diamond)** | `id{Decision / Condition}` | Conditional branch |
| **Hexagon** | `id{{Preparation / Loop}}` | Setup, verification, or loop header |
| **Parallelogram** | `id[/Data Input / Output/]` | I/O operation |
| **Trapezoid** | `id[/Manual Operation\]` | User interaction |
| **Inverted Trapezoid** | `id[\Summary / Aggregation/]` | Collated data / aggregation |

### 2.2 Link Styles & Labels

```mermaid
flowchart LR
    A1 --> B1
    A2 --- B2
    A3 -.-> B3
    A4 ==> B4
    A5 -->|Direct Label| B5
    A6 -- "Quoted Label: (OK)" --> B6
    A7 -. "Dotted with text" .-> B7
    A8 == "Thick with text" ==> B8
    A9 <--> B9
    A10 x--x B10
    A11 o--o B11
```

```markdown
A1 --> B1              %% Directed arrow
A2 --- B2              %% Open link (no arrow)
A3 -.-> B3             %% Dotted arrow
A4 ==> B4              %% Thick solid arrow
A5 -->|Direct Label| B5 %% Arrow with text label
A6 -- "Quoted Label" --> B6
A7 -. "Text" .-> B7    %% Dotted arrow with text
A8 == "Text" ==> B8    %% Thick arrow with text
A9 <--> B9             %% Bidirectional arrow
A10 x--x B10           %% Cross-head connection
A11 o--o B11           %% Circle-head connection
```

### 2.3 Subgraphs & Visual Boundaries

```mermaid
flowchart TD
    subgraph Frontend["Frontend Tier (Client)"]
        UI["React / Vue SPA"]
        State["Redux Store"]
        UI <--> State
    end

    subgraph Backend["Backend Tier (Server)"]
        API["FastAPI Gateway"]
        Auth["OAuth2 Service"]
        API --> Auth
    end

    subgraph Storage["Data Persistence Tier"]
        DB[(PostgreSQL)]
        Cache[(Redis Cache)]
    end

    UI -->|HTTPS REST| API
    API --> DB
    API --> Cache
```

### 2.4 Styling & Custom Themes

```markdown
%% Individual Node Styling
style NodeID fill:#2d3748,stroke:#4a5568,stroke-width:2px,color:#ffffff

%% Class Definition & Reusable Styling
classDef primary fill:#2563eb,stroke:#1d4ed8,stroke-width:2px,color:#ffffff;
classDef success fill:#16a34a,stroke:#15803d,stroke-width:2px,color:#ffffff;
classDef warning fill:#d97706,stroke:#b45309,stroke-width:2px,color:#ffffff;

class NodeA,NodeB primary;
NodeC:::success
```

---

## 3. Sequence Diagrams (`sequenceDiagram`)

Used to visualize message passing, API calls, and asynchronous interactions across lifecycles:

```mermaid
sequenceDiagram
    autonumber
    actor User as Client (Browser)
    participant GW as API Gateway
    participant Auth as Auth Service
    participant DB as PostgreSQL DB

    User->>GW: POST /api/login (credentials)
    activate GW
    GW->>Auth: ValidateCredentials(user, pass)
    activate Auth
    Auth->>DB: SELECT * FROM users WHERE email = ?
    activate DB
    DB-->>Auth: UserRecord (hash)
    deactivate DB

    alt Valid Password
        Auth-->>GW: JWT Token (Signed)
        GW-->>User: 200 OK (Set-Cookie / Access Token)
    else Invalid Password
        Auth-->>GW: 401 Unauthorized Error
        GW-->>User: 401 Invalid Credentials
    end
    deactivate Auth
    deactivate GW

    opt Refresh Token
        User->>GW: POST /api/refresh
        GW-->>User: 200 OK (New Token)
    end
```

### Key Sequence Diagram Operators:
- `->>` : Synchronous request with solid arrow
- `-->>` : Asynchronous reply with dotted arrow
- `-x` / `--x` : Lost message / connection drop
- `activate Component` / `deactivate Component` : Activation bars
- `Note over A,B: Description` : Contextual annotation note
- `alt ... else ... end` : Alternative execution branch
- `opt ... end` : Optional execution branch
- `loop ... end` : Repeated execution loop
- `par ... and ... end` : Parallel concurrent actions

---

## 4. Class Diagrams (`classDiagram`)

Standard UML class diagrams for Object-Oriented software architectures:

```mermaid
classDiagram
    class Shape {
        <<abstract>>
        #String color
        #Point origin
        +getColor() String
        +setColor(String color) void
        +calculateArea()* double
        +calculatePerimeter()* double
    }

    class Circle {
        -double radius
        +Circle(String color, double radius)
        +getRadius() double
        +setRadius(double r) void
        +calculateArea() double
        +calculatePerimeter() double
    }

    class Rectangle {
        -double width
        -double height
        +Rectangle(String color, double w, double h)
        +calculateArea() double
        +calculatePerimeter() double
    }

    class Canvas {
        -List~Shape~ shapes
        +addShape(Shape s) void
        +renderAll() void
    }

    Shape <|-- Circle : Inheritance
    Shape <|-- Rectangle : Inheritance
    Canvas o-- Shape : Aggregation (1 to Many)
```

### UML Relationships in Mermaid:

| Relationship | Mermaid Syntax | Description |
| :--- | :---: | :--- |
| **Inheritance / Generalization** | `<|--` | Subclass inherits from Superclass (`Derived <|-- Base`) |
| **Realization / Implementation** | `<|..` | Class implements Interface (`ConcreteClass <|.. IInterface`) |
| **Composition** | `*--` | Whole-part relationship where parts cannot exist without the whole |
| **Aggregation** | `o--` | Whole-part relationship where parts have independent lifecycles |
| **Association** | `-->` | Directed relationship (`ClassA --> ClassB`) |
| **Dependency** | `..>` | Temporary usage (`ClassA ..> UtilityService`) |

### Visibility Modifiers:
- `+` : Public
- `-` : Private
- `#` : Protected
- `~` : Package-Private / Internal
- `*` : Abstract method
- `$` : Static member

---

## 5. Entity-Relationship Diagrams (`erDiagram`)

Ideal for relational database schemas and data science models:

```mermaid
erDiagram
    STUDENT ||--o{ ENROLLMENT : places
    COURSE ||--o{ ENROLLMENT : contains
    STUDENT {
        string student_id PK "Student unique ID"
        string full_name
        string email UK "Unique student email"
        date birth_date
        float gpa
    }
    COURSE {
        string course_code PK "e.g. CS213, CS221"
        string title
        int credits
        string department
    }
    ENROLLMENT {
        int enrollment_id PK
        string student_id FK
        string course_code FK
        date enrollment_date
        string grade
    }
```

### ER Cardinality Notation:

| Left Symbol | Right Symbol | Relationship Meaning |
| :---: | :---: | :--- |
| `\|\|` | `\|\|` | Exactly one to Exactly one ($1:1$) |
| `\|\|` | `o\|` / `\|o` | Exactly one to Zero or one ($1:0..1$) |
| `\|\|` | `o{` / `}o` | Exactly one to Zero or more ($1:N$) |
| `\|\|` | `\|{` / `{\|` | Exactly one to One or more ($1:1..N$) |
| `}o` | `o{` | Zero or more to Zero or more ($M:N$) |

---

## 6. State Diagrams (`stateDiagram-v2`)

Used to visualize finite state machines (FSM), lifecycles, and network protocol states:

```mermaid
stateDiagram-v2
    [*] --> Idle

    Idle --> Authenticating : SubmitCredentials
    Authenticating --> Active : Success [Valid Auth]
    Authenticating --> Locked : Failure [Retries >= 5]
    
    state Active {
        [*] --> ViewingDashboard
        ViewingDashboard --> EditingProfile : ClickEdit
        EditingProfile --> ViewingDashboard : SaveChanges
    }

    Active --> SessionExpired : Timeout [Idle > 30m]
    SessionExpired --> Idle : Relogin
    Locked --> Idle : AdminUnlock

    Active --> [*] : Logout
```

---

## 7. Git Graphs (`gitGraph`)

Visualizes branching, commits, tags, and pull request merges:

```mermaid
gitGraph
    commit id: "Initial Commit"
    commit id: "Setup Project"
    branch develop
    checkout develop
    commit id: "Add Database Models"
    branch feature/auth
    checkout feature/auth
    commit id: "Implement OAuth2"
    commit id: "Unit Tests for Auth"
    checkout develop
    merge feature/auth id: "Merge Auth PR"
    checkout main
    merge develop tag: "v1.0.0" id: "Production Release"
```

---

## 8. Common Pitfalls & Troubleshooting Checklist

1. **Avoid Reserved Words in Node IDs**: Never use words like `end`, `subgraph`, `style`, or `class` as raw Node IDs.
2. **Text Wrap & Line Breaks**: Use `<br>` or `
` inside quoted string labels for multi-line node descriptions: `nodeA["First Line<br>Second Line"]`.
3. **Escaping Math in Mermaid**: If embedding math inside Mermaid nodes, write standard text equivalents or wrap LaTeX in clean string literals to prevent parser crashes.
4. **Validating Direction**: Always place the direction statement immediately following the diagram type opener (e.g., `flowchart TD`, not `flowchart
TD`).

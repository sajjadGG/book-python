* ``ASSIGNMENT`` relates to ``one MISSION``
* ``ASSIGNMENT`` assigns ``one ASTRONAUT``
* ``ASSIGNMENT`` defines ``one ROLE``

* ``MISSION`` is related to ``zero or many ASSIGNMENT``
* ``ASTRONAUT`` is assigned to ``zero or many ASSIGNMENT``
* ``ROLE`` is defined in ``one ASSIGNMENT``



```mermaid
erDiagram

ASSIGNMENT }o..|| MISSION : "relates to"
ASSIGNMENT }o..|| ASTRONAUT : "assigns"
ASSIGNMENT ||..|| ROLE : "defines"

ASSIGNMENT {
    primary_key id
    foreign_key mission_id
    foreign_key astronaut_id
    str role
} 

ROLE {
    primary_key id
    str name
}

ASTRONAUT {
    primary_key id 
    str firstName
    str lastName
    int age
}

MISSION {
    primary_key id
    int year
    int name
}
```

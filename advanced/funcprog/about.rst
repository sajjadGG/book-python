FuncProg About
==============


Rationale
---------
* Programming paradigm
* Programs are constructed by applying and composing functions
* Functions are treated as first-class citizens

* Functions can be bound to names (including local identifiers), passed
  as arguments, and returned from other functions, just as any other data
  type can [#WikipediaFunc]_

* Functional programming avoids side effects, which are used in imperative
  programming to implement state and I/O

* Pure functional programming completely prevents side-effects and
  provides referential transparency

* Higher-order functions are rarely used in older imperative programming.

* Imperative program will use a loop to traverse and modify a list, while
  a functional program, would prefer using a higher-order ``map`` function
  that takes a function and a list, generating and returning a new list by
  applying the function to each list item [#Spiewak2008]_

* Restricting side effects, can decrease number of bugs, be easier to
  debug and test, and be more suited to formal verification [#Hughes1984]_
  [#Hudak1989]_

* Functional programming languages are typically less efficient in their
  use of CPU and memory than imperative languages such as C, Java, Python
  [#Paulson1996]_

* This is due that some mutable data structures like arrays have a very
  straightforward implementation using present hardware


References
----------
.. [#WikipediaFunc] Functional programming. Retrieved: 2020-10-09. URL: https://en.wikipedia.org/wiki/Functional_programming
.. [#Hudak1989] Hudak, Paul. "Conception, evolution, and application of functional programming languages". ACM Computing Surveys. 21 (3): 359–411. doi:10.1145/72551.72554. S2CID 207637854. 1989.
.. [#Hughes1984] Hughes, John. "Why Functional Programming Matters". Chalmers University of Technology. 1984.
.. [#Spiewak2008] Spiewak, Daniel. "Implementing Persistent Vectors in Scala". Code Commit. 2008.
.. [#Paulson1996] Paulson, Larry C. "ML for the Working Programmer". Cambridge University Press. ISBN: 978-0-521-56543-1. Retrieved: 2013-02-10. 1996.

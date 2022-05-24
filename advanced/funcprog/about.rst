FuncProg About
==============
* Programming paradigm
* Programs are constructed by applying and composing functions
* Functions are treated as first-class citizens
* Functional programming avoids side effects
* Functional programming provides referential transparency
* Instead of loop use ``map`` and recurrence
* Functions can be bound to names (including local identifiers), passed
  as arguments, and returned from other functions, just as any other data
  type can [#WikipediaFunc]_
* Imperative program will use a loop to traverse and modify a list, while
  a functional program, would prefer using a higher-order ``map`` function
  that takes a function and a list, generating and returning a new list by
  applying the function to each list item [#Spiewak2008]_
* Restricting side effects, can decrease number of bugs, be easier to
  debug and test, and be more suited to formal verification [#Hughes1984]_
  [#Hudak1989]_
* Functional Design Patterns - Scott Wlaschin https://www.youtube.com/watch?v=srQt1NAHYC0
* The Functional Programmer's Toolkit - Scott Wlaschin - https://www.youtube.com/watch?v=Nrp_LZ-XGsY

Further Reading
---------------
* Functional Design Patterns - Scott Wlaschin - https://www.youtube.com/watch?v=srQt1NAHYC0
* The Functional Programmer's Toolkit - Scott Wlaschin - https://www.youtube.com/watch?v=Nrp_LZ-XGsY


References
----------
.. [#WikipediaFunc] Functional programming. Retrieved: 2020-10-09. URL: https://en.wikipedia.org/wiki/Functional_programming
.. [#Hudak1989] Hudak, Paul. "Conception, evolution, and application of functional programming languages". ACM Computing Surveys. 21 (3): 359–411. doi:10.1145/72551.72554. S2CID 207637854. 1989.
.. [#Hughes1984] Hughes, John. "Why Functional Programming Matters". Chalmers University of Technology. 1984.
.. [#Spiewak2008] Spiewak, Daniel. "Implementing Persistent Vectors in Scala". Code Commit. 2008.
.. [#Paulson1996] Paulson, Larry C. "ML for the Working Programmer". Cambridge University Press. ISBN: 978-0-521-56543-1. Retrieved: 2013-02-10. 1996.

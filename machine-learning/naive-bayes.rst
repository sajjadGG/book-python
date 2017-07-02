***********
Naive Bayes
***********

Bayes' rule expresses the conditional probability of the event :math:`A` given the event :math:`B` in terms of the conditional probability of the event :math:`B` given the event A and the unconditional probability of :math:`A`:

.. math::

    P(H|D) = \frac{P(D|H)P(H)}{P(D)}

- :math:`P(H|D)`: Probability that the hypothesis is true given the data.
- :math:`P(D|H)`: Probability of the data arising given the hypothesis.
- :math:`P(H)`: Probability that the hypothesis is true, globally.
- :math:`P(D)`: Probability of the data arising, globally.

In this expression, the unconditional probability of :math:`A` is also called the prior probability of :math:`A`, because it is the probability assigned to A prior to observing any data. Similarly, in this context, :math:`P(A|B)` is called the posterior probability of :math:`A` given :math:`B`, because it is the probability of :math:`A` updated to reflect (i.e., to condition on) the fact that :math:`B` was observed to occur.


Problemy
========

Parameter Estimation
--------------------

Is the true value equal to :math:`X`?

Control vs. Treatment comparision
---------------------------------


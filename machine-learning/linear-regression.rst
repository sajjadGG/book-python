*****************
Linear Regression
*****************

* Najprostszy przypadek sieci neuronowych

Problemy
========
Predicting output on data matrix


Podstawowe pojęcia
==================
* Loss Function
* Parameters
* Gradient
* Gradient descent
* Overshoot
* Undershoot
* Goldi Locks
* Chain rule
* Weight
* Computatiion Graph
* Forward Propagation
* Backpropagation


Regression
==========
How does the actual machine learning thing work? With supervised learning, you have features and labels. The features are the descriptive attributes, and the label is what you're attempting to predict or forecast. Another common example with regression might be to try to predict the dollar value of an insurance policy premium for someone. The company may collect your age, past driving infractions, public criminal record, and your credit score for example. The company will use past customers, taking this data, and feeding in the amount of the "ideal premium" that they think should have been given to that customer, or they will use the one they actually used if they thought it was a profitable amount.

Thus, for training the machine learning classifier, the features are customer attributes, the label is the premium associated with those attributes.

.. code-block:: python

    import quandl

    df = quandl.get('WIKI/GOOGL', api_key='sbaiDFKSHYv8TLdoWKzW')
    df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

    df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
    df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

    df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

    print(df.head())

    """
    Date        Adj. Close    HL_PCT  PCT_change  Adj. Volume

    2004-08-19   50.322842  3.712563    0.324968   44659000.0
    2004-08-20   54.322689  0.710922    7.227007   22834300.0
    2004-08-23   54.869377  3.729433   -1.227880   18256100.0
    2004-08-24   52.597363  6.417469   -5.726357   15247300.0
    2004-08-25   53.164113  1.886792    1.183658    9188600.0
    """


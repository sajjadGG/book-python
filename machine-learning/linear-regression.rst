*****************
Linear Regression
*****************

Co to jest Linear Regression?
=============================
The straight line can be seen in the plot, showing how linear regression attempts to draw a straight line that will best minimize the residual sum of squares between the observed responses in the dataset, and the responses predicted by the linear approximation.

The coefficients, the residual sum of squares and the variance score are also calculated.

* Najprostszy przypadek sieci neuronowych

Problemy
========
Predicting output on data matrix

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn import datasets, linear_model

    # Load the diabetes dataset
    diabetes = datasets.load_diabetes()

    # Use only one feature
    diabetes_features = diabetes.data[:, np.newaxis, 2]

    # Split the data into training/testing sets
    features_train = diabetes_features[:-20]
    features_test = diabetes_features[-20:]

    # Split the targets into training/testing sets
    labels_train = diabetes.target[:-20]
    labels_test = diabetes.target[-20:]

    # Create linear regression object
    model = linear_model.LinearRegression()

    # Train the model using the training sets
    model.fit(features_train, labels_train)

    # The coefficients
    print('Coefficients: \n{model.coef_}')

    # The mean squared error
    print("Mean squared error: %.2f"
          % np.mean((model.predict(features_test) - labels_test) ** 2))

    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % model.score(features_test, labels_test))

    # Plot outputs
    plt.scatter(features_test, labels_test, color='black')
    plt.plot(features_test, model.predict(features_test), color='blue', linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()

Coefficients: [ 938.23786125]
Mean squared error: 2548.07
Variance score: 0.4

.. figure:: img/linear-regression.png
    :scale: 75%
    :align: center

    The straight line can be seen in the plot, showing how linear regression attempts to draw a straight line that will best minimize the residual sum of squares between the observed responses in the dataset, and the responses predicted by the linear approximation.

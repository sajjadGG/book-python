********
Graphviz
********

.. code-block:: python

    import graphviz
    import pandas as pd
    from sklearn import linear_model, neighbors, svm, tree, datasets
    from sklearn.model_selection import train_test_split


    iris_ds = datasets.load_iris()
    iris = pd.DataFrame(iris_ds.data, columns=iris_ds.feature_names).assign(target=iris_ds.target)
    iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target']
    iris_train, iris_test = train_test_split(iris, test_size=0.2)

    features = ['sepal_length', 'sepal_width']
    dtc = tree.DecisionTreeClassifier()
    dtc.fit(iris_train[features], iris_train['target'])

    dot_data = tree.export_graphviz(dtc,
        out_file=None,
        feature_names=features,
        class_names=iris_ds.target_names,
        filled=True,
        rounded=True,
        special_characters=True)

    graph = graphviz.Source(dot_data, )
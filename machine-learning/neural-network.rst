**************
Neural Network
**************

What Is a Neural Network?
=========================
It’s a technique for building a computer program that learns from data. It is based very loosely on how we think the human brain works. First, a collection of software "neurons" are created and connected together, allowing them to send messages to each other. Next, the network is asked to solve a problem, which it attempts to do over and over, each time strengthening the connections that lead to success and diminishing those that lead to failure. For a more detailed introduction to neural networks, `Michael Nielsen’s Neural Networks <http://neuralnetworksanddeeplearning.com/index.html>`_ and `Deep Learning <http://www.deeplearningbook.org/>`_ is a good place to start. For a more technical overview, try Deep Learning by Ian Goodfellow, Yoshua Bengio, and Aaron Courville.

Tool
----
* TensorFlow (Google) - http://playground.tensorflow.org/


Construction
------------

Learning
--------

Optimizing
----------

Przykłady praktyczne
====================

Image Classification using ``TensorFlow for Poets``
---------------------------------------------------
* https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#1

.. code-block:: console

    # download around 218MB of data
    $ curl -O http://download.tensorflow.org/example_images/flower_photos.tgz
    $ tar xzf flower_photos.tgz
    $ ls flower_photos

.. warning:: Training on this much data can take 30+ minutes on a small computer. If you want to reduce data:

    .. code-block:: console

        $ ls flower_photos/roses | wc -l
        $ rm flower_photos/*/[3-9]*
        $ ls flower_photos/roses | wc -l

.. code-block:: python

    from sklearn import metrics
    from sklearn import model_selection
    import tensorflow as tf
    from tensorflow.contrib import learn


    # Load dataset
    iris = learn.datasets.load_dataset('iris')
    x_train, x_test, y_train, y_test = model_selection.train_test_split(
        iris.data,
        iris.target,
        test_size=0.2,
        random_state=42
    )

    # Build 3 layer Deep Neural Network (DNN) with 10, 20, 10 units respectively.
    classifier = learn.DNNClassifier(hidden_units=[10, 20, 10], n_classes=3)

    # Fit and predict.
    classifier.fit(x_train, y_train, steps=200)
    score = metrics.accuracy_score(y_test, classifier.predict(x_test))

    print(f'Accuracy {score:f}')

.. code-block:: console

    $ curl -O https://raw.githubusercontent.com/tensorflow/tensorflow/r1.1/tensorflow/examples/image_retraining/retrain.py

    $ python retrain.py \
      --bottleneck_dir=bottlenecks \
      --how_many_training_steps=500 \
      --model_dir=inception \
      --summaries_dir=training_summaries/basic \
      --output_graph=retrained_graph.pb \
      --output_labels=retrained_labels.txt \
      --image_dir=flower_photos

    $ curl -L https://goo.gl/3lTKZs > label_image.py

    $ python label_image.py flower_photos/daisy/21652746_cc379e0eea_m.jpg
    $ python label_image.py flower_photos/roses/2414954629_3708a1a04d.jpg
    daisy (score = 0.99071)
    sunflowers (score = 0.00595)
    dandelion (score = 0.00252)
    roses (score = 0.00049)
    tulips (score = 0.00032)


Inception
^^^^^^^^^
* One of Google's best image classifiers
* Open Source
* Trained on 1.2 milion images
* Training took 2 weeks on 8GPU machine

Retraining
^^^^^^^^^^
* Also known as Transfer Learning
* Saves a lot of time
* Uses prior work


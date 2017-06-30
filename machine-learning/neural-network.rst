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


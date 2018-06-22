from sklearn import metrics
from scipy.spatial import distance
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


class NearestNeighborClassifier:
    def fit(self, features, labels):
        self.features_train = features
        self.labels_train = labels

    def predict(self, features_test):
        predictions = []

        for row in features_test:
            label = self._closest(row)
            predictions.append(label)

        return predictions

    def _closest(self, row):
        current_best_dist = distance.euclidean(row, self.features_train[0])
        best_index = 0

        for i in range(0, len(self.features_train)):
            dist = distance.euclidean(row, self.features_train[i])
            if dist < current_best_dist:
                current_best_dist = dist
                best_index = i

        return self.labels_train[best_index]


iris = load_iris()

x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.5)

model = NearestNeighborClassifier()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
accuracy = metrics.accuracy_score(y_test, predictions)

print(accuracy)

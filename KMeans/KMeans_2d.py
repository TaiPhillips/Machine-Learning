import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

plt.style.use('seaborn')

x, _ = make_blobs(n_samples=100, centers=3, n_features=2,
                  cluster_std=2.25, random_state=7)

K = 3  # number of clusters to find
MAX_ITERS = 300  # max number of steps to take
centroids = {i: x[i] for i in range(K)}  # initializing centroids
history = []  # record for visualization

# -------------------------------FITTING-----------------------------
for i in range(MAX_ITERS):
    # dict that holds samples of each class
    classifications = {i: [] for i in range(K)}

    # calculate euclidean distance and classify data points
    for features in x:
        distances = [np.linalg.norm(features - centroids[centroid]) for centroid in centroids]
        class_ = distances.index(min(distances))
        classifications[class_].append(features)

    # set centroid to mean of clustered data
    for i in range(K):
        centroids[i] = np.mean(classifications[i], axis=0)

    history.append(centroids)


# -----------------------------VISUALIZATION--------------------------
# TODO: Add video animation
# TODO: Do the same in 3D using 4 clusters

def predict_class(data):
    distances = [np.linalg.norm(data - centroids[c]) for c in centroids]
    class_ = distances.index(min(distances))
    return class_


y = [predict_class(sample) for sample in x]

dataset = {
    'Class 1': np.array([x[i] for i in range(len(x)) if y[i] == 0]),
    'Class 2': np.array([x[i] for i in range(len(x)) if y[i] == 1]),
    'Class 3': np.array([x[i] for i in range(len(x)) if y[i] == 2]),
}

# scatter all available data color coded according to the class
plt.scatter(dataset['Class 1'][:, 0], dataset['Class 1'][:, 1], color='r', alpha=0.5, label='Class 1')
plt.scatter(centroids[0][0], centroids[0][1], c='r', s=200)
plt.scatter(dataset['Class 2'][:, 0], dataset['Class 2'][:, 1], color='k', alpha=0.5, label='Class 2')
plt.scatter(centroids[1][0], centroids[1][1], c='k', s=200)
plt.scatter(dataset['Class 3'][:, 0], dataset['Class 3'][:, 1], color='g', alpha=0.5, label='Class 3')
plt.scatter(centroids[2][0], centroids[2][1], c='g', s=200)
plt.legend()
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title(f'K Means - {K} Clusters')
plt.savefig('Animations/KMeans_2d.png')
plt.show()

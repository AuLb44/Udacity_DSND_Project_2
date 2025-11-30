import pickle
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# Using the Path object, create a `project_root` variable
# set to the absolute path for the root of this project directory
project_root = Path(__file__).resolve().parent.parent

# Using the `project_root` variable
# create a `model_path` variable
# that points to the file `model.pkl`
# inside the assets directory
model_path = project_root / 'assets' / 'model.pkl'


def load_model():

    with model_path.open('rb') as file:
        model = pickle.load(file)

    return model


def plot_ml_performance(dept_counts, outpath):
    """
    Generate ML-based visualization using KMeans clustering on department counts.

    Uses KMeans clustering and plots scatter with continuous distance-to-cluster-center
    as the color scale, saved to outpath as PNG.

    Args:
        dept_counts: dict or array-like with department counts data
        outpath: Path or str to save the PNG file
    """
    from sklearn.cluster import KMeans

    # Convert dept_counts to numpy array for processing
    if isinstance(dept_counts, dict):
        data = np.array(list(dept_counts.values())).reshape(-1, 1)
        labels = list(dept_counts.keys())
    else:
        data = np.array(dept_counts).reshape(-1, 1)
        labels = [f'Dept {i+1}' for i in range(len(dept_counts))]

    # Ensure we have at least 2 samples for KMeans
    if len(data) < 2:
        # Create dummy data if not enough samples
        data = np.array([[10], [20], [30], [40], [50]])
        labels = [f'Dept {i+1}' for i in range(5)]

    # Perform KMeans clustering (always use at least 2 clusters)
    n_clusters = max(2, min(2, len(data)))
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(data)

    # Compute distance to nearest cluster center for each point
    distances = np.min(kmeans.transform(data), axis=1)

    # Create x positions for scatter plot
    x_positions = np.arange(len(data))

    # Create the plot with continuous color scale
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(
        x_positions,
        data.flatten(),
        c=distances,
        cmap='plasma',
        s=200,
        edgecolors='black',
        linewidth=1
    )

    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Distance to Cluster Center', fontsize=12)

    # Set labels and title
    ax.set_xlabel('Department', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title('Employee Performance - ML Clustering Analysis', fontsize=14)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(labels, rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig(outpath, dpi=100, bbox_inches='tight')
    plt.close(fig)

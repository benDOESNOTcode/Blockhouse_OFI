from sklearn.decomposition import PCA
import numpy as np

# Compute Integrated OFI using Principal component analysis (PCA)
def compute_integrated_ofi(multi_level_ofis):

    # Fit PCA to the multi- evel OFI DataFrame (10 levels)
    pca = PCA(n_components=1)
    principal_component = pca.fit_transform(multi_level_ofis)

    # Extract PCA weights by loading vector of the first component
    weights = pca.components_[0]

    # Normalize the weights by L1 norm
    norm_weights = weights / np.sum(np.abs(weights))

    # Multiply OFI matrix with the normalized weights to get a single vector
    integrated_ofi = multi_level_ofis.dot(norm_weights)
    return integrated_ofi  # returns a pd series with the same index as multi_level_ofis

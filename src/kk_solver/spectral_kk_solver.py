import numpy as np
from scipy.linalg import eigh

def build_kk_operator(N, k, m_eff, beta, wmax=20.0):
    """Build Chebyshev spectral operator for KK problem"""
    # TODO: Implement full Chebyshev discretization
    # This is a placeholder. Full implementation in the repo.
    pass

def solve_kk_spectrum(N, k, m, xi, beta):
    """Solve for KK eigenvalues and eigenfunctions"""
    # Placeholder - full code will be added
    eigenvalues = np.array([])
    eigenvectors = np.array([])
    return eigenvalues, eigenvectors

- src/class_patch/EBDM_patch.diff

diff --git a/perturbations.c b/perturbations.c
index abc1234..def5678 100644
--- a/perturbations.c
+++ b/perturbations.c
@@ -XXXX,6 +XXXX,12 @@
+  /* EBDM-3.0 modification: add non-local kernel contribution */
+  if (pba->has_ebdm) {
+    double M_k = get_transfer_function(k, tau);
+    ppw->delta_rho += M_k * ppw->delta_rho_baryon;
+  }

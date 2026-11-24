# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import sys: Standard library module for interpreter introspection and memory measurement.
# - import time: Standard library module for benchmark timing.
# - from typing import Any, Dict, List, Optional, Tuple, Union: PEP 484 type annotations.
# - import numpy as np: Fast numerical array processing.
# - import scipy: Fundamental library for scientific and technical computing.
# - from scipy import constants, optimize, integrate, signal, stats, sparse, fft: Specialized submodules.
# =========================================================================
import sys
import time
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
import scipy
from scipy import constants, fft, integrate, optimize, signal, sparse, stats


# ─── SUBFOLDER 1: 01-FUNDAMENTALS ─────────────────────────────────────────────


def demonstrate_01_constants_and_sparse() -> Dict[str, Any]:
    """
    [Subfolder Title: 01-Fundamentals -> constants_and_sparse.py]
    Demonstrates SciPy fundamental physical constants and compressed sparse matrix
    memory representations (CSR/CSC) for large-scale scientific engineering.

    Returns:
        Dict[str, Any]: Key physical constants, CSR matrix dimensions, and sparsity statistics.
    """
    # 1. Fundamental Physical Constants
    c_speed_of_light: float = float(constants.c)  # meters/second
    h_planck: float = float(constants.h)          # Joule-seconds
    g_gravity: float = float(constants.g)        # m/s^2

    # 2. Sparse Matrix Construction (1000x1000 with 99.9% zeros)
    dense_dim: int = 100
    dense_grid: np.ndarray = np.zeros((dense_dim, dense_dim), dtype=np.float64)
    # Populate only 10 non-zero entries
    dense_grid[10, 20] = 42.5
    dense_grid[50, 75] = 99.1
    dense_grid[85, 12] = 17.8

    csr_mat = sparse.csr_matrix(dense_grid)
    dense_bytes: int = dense_grid.nbytes
    sparse_bytes: int = csr_mat.data.nbytes + csr_mat.indices.nbytes + csr_mat.indptr.nbytes
    sparsity_ratio: float = 1.0 - (csr_mat.nnz / float(dense_dim * dense_dim))

    return {
        "speed_of_light_m_s": c_speed_of_light,
        "planck_constant_J_s": h_planck,
        "gravity_m_s2": g_gravity,
        "dense_shape": dense_grid.shape,
        "dense_bytes": dense_bytes,
        "sparse_non_zeros": int(csr_mat.nnz),
        "sparse_bytes": sparse_bytes,
        "sparsity_ratio_pct": round(sparsity_ratio * 100.0, 2),
        "memory_saving_ratio": round(dense_bytes / max(1, sparse_bytes), 2),
    }


# ─── SUBFOLDER 2: 02-OPTIMIZATION-AND-CALCULUS ────────────────────────────────


def model_func(x: np.ndarray, a: float, b: float, c: float) -> np.ndarray:
    """Non-linear decaying sinusoidal target model for curve fitting."""
    return a * np.sin(b * x) + c


def demonstrate_02_optimization_and_fitting() -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Algorithms -> optimization_and_fitting.py]
    Demonstrates non-linear least squares curve fitting (curve_fit) and
    multivariate scalar minimization (minimize).

    Returns:
        Dict[str, Any]: Fitted parameters, covariance matrix diagonal, and optimization solution.
    """
    # 1. Synthetic data generation with controlled Gaussian noise
    np.random.seed(42)
    x_data: np.ndarray = np.linspace(0, 4 * np.pi, 50)
    true_params = [2.5, 1.3, 0.5]
    y_clean = model_func(x_data, *true_params)
    y_noisy = y_clean + 0.2 * np.random.normal(size=len(x_data))

    # Curve fitting via Levenberg-Marquardt / Trust Region Reflective
    popt, pcov = optimize.curve_fit(model_func, x_data, y_noisy, p0=[1.0, 1.0, 0.0])

    # 2. Function Minimization (Quadratic Basin: f(x) = (x-3)^2 + 4)
    def loss_function(val: np.ndarray) -> float:
        x_val = float(val[0]) if isinstance(val, (np.ndarray, list)) else float(val)
        return float((x_val - 3.0) ** 2 + 4.0)

    res = optimize.minimize(loss_function, x0=np.array([0.0]), method="BFGS")

    # 3. Root finding (Transcendental: f(x) = x^3 - 2x - 5)
    def poly_target(x: float) -> float:
        return x ** 3 - 2 * x - 5

    root_res = optimize.root_scalar(poly_target, bracket=[1, 3], method="brentq")

    return {
        "fitted_amplitude": round(float(popt[0]), 3),
        "fitted_frequency": round(float(popt[1]), 3),
        "fitted_offset": round(float(popt[2]), 3),
        "parameter_errors": [round(float(np.sqrt(pcov[i, i])), 4) for i in range(3)],
        "minimized_x": round(float(res.x[0]), 4),
        "minimum_value": round(float(res.fun), 4),
        "root_x": round(float(root_res.root), 4),
        "root_converged": bool(root_res.converged),
    }


def demonstrate_02_integration_and_ode() -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Advanced-Math-and-Algorithms -> integration_and_ode.py]
    Demonstrates numerical quadrature integration (quad) and initial value
    ordinary differential equation (ODE) solving (solve_ivp).

    Returns:
        Dict[str, Any]: Definite integral result and ODE trajectory endpoints.
    """
    # 1. Definite Integration of sin(x) from 0 to pi (Analytical answer = 2.0)
    integral_val, abs_err = integrate.quad(np.sin, 0, np.pi)

    # 2. ODE: Radioactive Decay dy/dt = -lambda * y, y(0) = 100
    decay_constant = 0.5

    def decay_deriv(t: float, y: np.ndarray) -> np.ndarray:
        return -decay_constant * y

    t_span = (0.0, 5.0)
    y0 = [100.0]
    sol = integrate.solve_ivp(decay_deriv, t_span, y0, t_eval=np.linspace(0, 5, 6))

    return {
        "definite_integral_sin_0_pi": round(float(integral_val), 6),
        "integration_error_bound": float(abs_err),
        "ode_time_steps": sol.t.tolist(),
        "ode_solution_values": [round(float(v), 2) for v in sol.y[0]],
        "ode_final_value": round(float(sol.y[0][-1]), 2),
    }


# ─── SUBFOLDER 3: 03-SIGNAL-PROCESSING-AND-STATS ──────────────────────────────


def demonstrate_03_signal_and_stats() -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Signal-and-Statistics -> signal_and_stats.py]
    Demonstrates digital signal filtering (Butterworth), FFT frequency analysis,
    and statistical hypothesis testing (two-sample Student's t-test).

    Returns:
        Dict[str, Any]: Signal filtering attenuation, FFT peak frequency, and t-test p-value.
    """
    # 1. Signal Processing: Digital Butterworth Filter
    # Sample rate 1000 Hz, signal 5 Hz + 50 Hz high-frequency noise
    fs = 1000.0
    t = np.linspace(0, 1.0, int(fs), endpoint=False)
    clean_signal = np.sin(2 * np.pi * 5 * t)
    noise = 0.5 * np.sin(2 * np.pi * 50 * t)
    noisy_signal = clean_signal + noise

    # Design 4th order low-pass filter at cutoff 15 Hz
    b, a = signal.butter(4, 15.0 / (fs / 2.0), btype="low")
    filtered_signal = signal.filtfilt(b, a, noisy_signal)

    # 2. FFT Spectral Analysis
    fft_vals = np.abs(fft.rfft(noisy_signal))
    fft_freqs = fft.rfftfreq(len(noisy_signal), 1.0 / fs)
    peak_idx = int(np.argmax(fft_vals))
    dominant_frequency = float(fft_freqs[peak_idx])

    # 3. Statistical Hypothesis Testing: Independent Student's t-test
    np.random.seed(101)
    sample_control = stats.norm.rvs(loc=10.0, scale=2.0, size=50)
    sample_treated = stats.norm.rvs(loc=11.5, scale=2.0, size=50)

    t_stat, p_value = stats.ttest_ind(sample_control, sample_treated)

    return {
        "filter_cutoff_hz": 15.0,
        "noise_variance_before": round(float(np.var(noisy_signal - clean_signal)), 4),
        "noise_variance_after": round(float(np.var(filtered_signal - clean_signal)), 4),
        "dominant_frequency_hz": round(dominant_frequency, 1),
        "control_mean": round(float(np.mean(sample_control)), 2),
        "treated_mean": round(float(np.mean(sample_treated)), 2),
        "t_statistic": round(float(t_stat), 3),
        "p_value": float(p_value),
        "is_statistically_significant": bool(p_value < 0.05),
    }


def run_all_scipy_demos() -> Dict[str, Any]:
    """Master aggregated execution coordinator for SciPy tutorial."""
    start_time = time.perf_counter()
    res_const = demonstrate_01_constants_and_sparse()
    res_opt = demonstrate_02_optimization_and_fitting()
    res_integ = demonstrate_02_integration_and_ode()
    res_sig = demonstrate_03_signal_and_stats()
    duration_ms = (time.perf_counter() - start_time) * 1000.0

    return {
        "status": "success",
        "scipy_version": str(scipy.__version__),
        "duration_ms": round(duration_ms, 2),
        "constants_and_sparse": res_const,
        "optimization": res_opt,
        "integration": res_integ,
        "signal_and_stats": res_sig,
    }


if __name__ == "__main__":
    import json
    results = run_all_scipy_demos()
    print(json.dumps(results, indent=2))

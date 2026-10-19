# 🔬 SciPy Mastery: Numerical Algorithms, Calculus & Physics Engineering Guide

> **Module Scope:** Optimization (`scipy.optimize`), Numerical Quadrature & ODEs (`scipy.integrate`), Sparse Linear Algebra (`scipy.sparse`), Signal Conditioning (`scipy.signal`), and Statistical Inference (`scipy.stats`).

---

## 📌 Table of Contents
1. [Core Mental Model: Bridging NumPy to Compiled Algorithms](#1-core-mental-model-bridging-numpy-to-compiled-algorithms)
2. [Submodule Architecture Ecosystem](#2-submodule-architecture-ecosystem)
3. [Sparse Matrices: CSR vs CSC & Memory Efficiency](#3-sparse-matrices-csr-vs-csc--memory-efficiency)
4. [Optimization: Minimization, Roots & Curve Fitting](#4-optimization-minimization-roots--curve-fitting)
5. [Numerical Calculus: Quadrature (Integrals) & ODEs](#5-numerical-calculus-quadrature-integrals--odes)
6. [Signal Processing: Digital Filters & FFT Analysis](#6-signal-processing-digital-filters--fft-analysis)
7. [Statistical Inference & Hypothesis Testing ($t$-tests)](#7-statistical-inference--hypothesis-testing-t-tests)
8. [Common Developer Pitfalls & Numerical Instabilities](#8-common-developer-pitfalls--numerical-instabilities)
9. [SciPy Quick-Reference Cheat Sheet](#9-scipy-quick-reference-cheat-sheet)

---

## 1. Core Mental Model: Bridging NumPy to Compiled Algorithms

While **NumPy** provides dense N-dimensional memory buffers, **SciPy** wraps century-proven numerical libraries written in Fortran and C (such as LAPACK, MINPACK, QUADPACK, and FFTPACK).

SciPy operates with zero Python interpreter overhead: arguments are converted into C structs, executed within compiled binary loops without GIL contention, and returned as standard `np.ndarray` instances.

---

## 2. Submodule Architecture Ecosystem

SciPy is organized into specialized domain modules:

```
                  ┌──────────────────────────────┐
                  │       SciPy Core Root        │
                  └──────────────┬───────────────┘
          ┌──────────────────────┼──────────────────────┐
          ▼                      ▼                      ▼
┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐
│  scipy.optimize   │  │  scipy.integrate  │  │   scipy.sparse    │
│  - minimize()     │  │  - quad()         │  │  - csr_matrix     │
│  - curve_fit()    │  │  - solve_ivp()    │  │  - csc_matrix     │
│  - root_scalar()  │  │  - dblquad()      │  │  - sparse.linalg  │
└───────────────────┘  └───────────────────┘  └───────────────────┘
          │                      │                      │
          ▼                      ▼                      ▼
┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐
│   scipy.signal    │  │    scipy.stats    │  │  scipy.constants  │
│  - butter()       │  │  - norm, t        │  │  - c, h, G, e     │
│  - filtfilt()     │  │  - ttest_ind()    │  │  - unit scales    │
│  - spectrogram()  │  │  - pearsonr()     │  │  - physical data  │
└───────────────────┘  └───────────────────┘  └───────────────────┘
```

---

## 3. Sparse Matrices: CSR vs CSC & Memory Efficiency

When managing massive grids (e.g. graph networks, finite element meshes, recommendation systems) where 95%+ of elements are zero, dense NumPy arrays waste gigabytes of RAM.

### When to Use CSR vs CSC:
* **`scipy.sparse.csr_matrix` (Compressed Sparse Row)**: Optimized for fast row slicing and matrix-vector products ($A \mathbf{x}$).
* **`scipy.sparse.csc_matrix` (Compressed Sparse Column)**: Optimized for fast column slicing.

```python
import numpy as np
from scipy import sparse

# Create 10,000 x 10,000 grid with only 5 non-zero values
dense_grid = np.zeros((10000, 10000), dtype=np.float64)
dense_grid[42, 99] = 15.5
dense_grid[500, 8000] = 77.2

# Compress to CSR format:
csr = sparse.csr_matrix(dense_grid)

print(f"Dense RAM:  {dense_grid.nbytes / (1024**2):.1f} MB")  # ~762.9 MB!
print(f"Sparse RAM: {csr.data.nbytes / 1024:.2f} KB")        # ~0.02 KB!
# 99.999% RAM savings
```

---

## 4. Optimization: Minimization, Roots & Curve Fitting

### A. Non-linear Least Squares Curve Fitting (`curve_fit`)
Fit mathematical parameters directly to experimental or noisy sensor observations:

```python
import numpy as np
from scipy.optimize import curve_fit

def damped_wave(t, amplitude, decay, frequency):
    return amplitude * np.exp(-decay * t) * np.cos(2 * np.pi * frequency * t)

# Fit parameters to noisy readings:
popt, pcov = curve_fit(damped_wave, time_data, signal_data, p0=[1.0, 0.1, 5.0])
amp, dec, freq = popt
# Diagonal of covariance matrix yields standard error:
param_errors = np.sqrt(np.diag(pcov))
```

### B. Multivariate Scalar Minimization (`minimize`)
Find the input values that minimize an objective cost function:

```python
from scipy.optimize import minimize

# Loss surface: Rosenbrock Banana Function
def rosenbrock(x):
    return (1.0 - x[0])**2 + 100.0 * (x[1] - x[0]**2)**2

res = minimize(rosenbrock, x0=[0.0, 0.0], method="BFGS")
print("Optimal Parameters:", res.x)      # Converges to [1.0, 1.0]
print("Minimum Loss:       ", res.fun)    # Minimum value 0.0
```

---

## 5. Numerical Calculus: Quadrature (Integrals) & ODEs

### A. Definite Integration via Adaptive Quadrature (`quad`)
$$\int_0^\pi \sin(x) \, dx = 2.0$$

```python
from scipy.integrate import quad
import numpy as np

area, abs_error = quad(np.sin, 0, np.pi)
print(f"Computed Integral: {area:.8f} (Error: {abs_error:.2e})")
```

### B. Initial Value Ordinary Differential Equations (`solve_ivp`)
Simulate physical dynamical systems (e.g. cooling, population dynamics, orbital decay):
$$\frac{dy}{dt} = -k \cdot y, \quad y(0) = 100$$

```python
from scipy.integrate import solve_ivp

def exponential_decay(t, y, k=0.3):
    return -k * y

# Solve over time span t=[0, 10]
solution = solve_ivp(exponential_decay, (0, 10), [100.0], t_eval=np.linspace(0, 10, 11))
print("Time Steps:", solution.t)
print("System State y(t):", solution.y[0])
```

---

## 6. Signal Processing: Digital Filters & FFT Analysis

### A. Zero-Phase Low-Pass Butterworth Filter (`filtfilt`)
Remove high-frequency electromagnetic noise without introducing phase shift:

```python
from scipy.signal import butter, filtfilt

fs = 1000.0        # Sampling frequency (Hz)
cutoff = 25.0       # Target cutoff frequency (Hz)
order = 4           # 4th order filter

# Design normalized Butterworth coefficients
b, a = butter(order, cutoff / (fs / 2.0), btype="low")

# Apply forward-backward zero-phase filter
clean_signal = filtfilt(b, a, noisy_sensor_stream)
```

### B. Fast Fourier Transform (`scipy.fft`)
Decompose complex time-series signals into dominant frequency spectrums:

```python
from scipy import fft

fft_magnitudes = np.abs(fft.rfft(sensor_readings))
fft_frequencies = fft.rfftfreq(len(sensor_readings), 1.0 / fs)
dominant_freq = fft_frequencies[np.argmax(fft_magnitudes)]
```

---

## 7. Statistical Inference & Hypothesis Testing ($t$-tests)

SciPy provides rigorous tools to validate whether observed differences between groups are real or random noise:

```python
from scipy.stats import ttest_ind

# Two-sample independent Student's t-test
t_stat, p_val = ttest_ind(group_a_conversions, group_b_conversions)

print(f"t-statistic: {t_stat:.3f}")
print(f"p-value:     {p_val:.4f}")

if p_val < 0.05:
    print("Decision: Reject Null Hypothesis (Statistically Significant Effect)")
else:
    print("Decision: Retain Null Hypothesis (No Significant Difference)")
```

---

## 8. Common Developer Pitfalls & Numerical Instabilities

### ❌ Pitfall 1: Converting a large sparse matrix to dense
```python
# DISASTROUS: Instantly crashes system RAM (OOM kill)
dense_mat = csr_matrix.toarray()

# CORRECT: Keep it sparse and use scipy.sparse.linalg
from scipy.sparse.linalg import spsolve
x = spsolve(csr_matrix, b_vector)
```

### ❌ Pitfall 2: Using procedural loops for numerical integration
```python
# BAD (Slow Riemann sum with poor precision):
dx = 0.0001
area = sum(np.sin(x) * dx for x in np.arange(0, np.pi, dx))

# 100x FASTER & MACHINE PRECISION:
area, _ = quad(np.sin, 0, np.pi)
```

---

## 9. SciPy Quick-Reference Cheat Sheet

```python
# Optimization
optimize.minimize(func, x0, method="BFGS")   # Function minimization
optimize.curve_fit(model, x, y)              # Non-linear parameter fit
optimize.root_scalar(func, bracket=[a, b])   # Scalar root finder

# Calculus
integrate.quad(func, a, b)                   # 1D Definite integral
integrate.solve_ivp(deriv_func, t_span, y0)  # ODE initial value solver

# Sparse
sparse.csr_matrix(arr)                       # Compressed row matrix
sparse.linalg.spsolve(A, b)                  # Sparse linear solver

# Signal & Statistics
signal.butter(N, Wn, btype="low")            # Digital filter design
signal.filtfilt(b, a, data)                  # Zero-phase filter application
stats.ttest_ind(sample_a, sample_b)          # Two-sample t-test
```

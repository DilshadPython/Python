# 📊 Matplotlib Mastery: Data Storytelling & Headless Web Visualization Guide

> **Module Scope:** Figure/Axes OOP Architecture, Multi-Axis Dashboards, Scientific Heatmaps, Server-Side Headless Rendering (`Agg`), and Zero-Leak Memory Management in Flask/WSGI.

---

## 📌 Table of Contents
1. [Core Mental Model: The Figure & Axes OOP Architecture](#1-core-mental-model-the-figure--axes-oop-architecture)
2. [Procedural `pyplot` vs OOP Interface: The Industry Standard](#2-procedural-pyplot-vs-oop-interface-the-industry-standard)
3. [Multi-Panel Dashboards & Subplot Layouts](#3-multi-panel-dashboards--subplot-layouts)
4. [Master Visualization Types (Lines, Bars, Histograms & Heatmaps)](#4-master-visualization-types-lines-bars-histograms--heatmaps)
5. [Headless Web Production in Flask/Gunicorn (`'Agg'`)](#5-headless-web-production-in-flaskgunicorn-agg)
6. [In-Memory Base64 Serialization (Zero Disk Clutter)](#6-in-memory-base64-serialization-zero-disk-clutter)
7. [Memory Leak Prevention: The `plt.close(fig)` Rule](#7-memory-leak-prevention-the-pltclosefig-rule)
8. [Professional Styling & Dark Mode Themes](#8-professional-styling--dark-mode-themes)
9. [Common Developer Pitfalls & Anti-Patterns](#9-common-developer-pitfalls--anti-patterns)
10. [Matplotlib Quick-Reference Cheat Sheet](#10-matplotlib-quick-reference-cheat-sheet)

---

## 1. Core Mental Model: The Figure & Axes OOP Architecture

Matplotlib's internal architecture is structured in a clear two-tier hierarchy:

```
┌─────────────────────────────────────────────────────────────┐
│  Figure (The overall window canvas / export container)     │
│                                                             │
│   ┌──────────────────────────┐  ┌────────────────────────┐  │
│   │  Axes 1 (Plot Sub-area)  │  │  Axes 2 (Plot Sub-area)│  │
│   │  - X-Axis & Y-Axis       │  │  - X-Axis & Y-Axis     │  │
│   │  - Title & Labels        │  │  - Bar charts / Lines  │  │
│   │  - Spines & Ticks        │  │  - Legend & Colorbar   │  │
│   │  - Grid lines            │  │  - Annotations         │  │
│   └──────────────────────────┘  └────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

* **`Figure`**: The top-level canvas holding everything (dimensions, background color, DPI, and subplots).
* **`Axes`**: The actual plotting coordinate system where data points, lines, bars, and markers are drawn.

---

## 2. Procedural `pyplot` vs OOP Interface: The Industry Standard

> [!WARNING]
> Using procedural functions like `plt.plot()`, `plt.title()`, and `plt.xlabel()` relies on implicit global state machines. In concurrent web applications or multi-plot dashboards, this causes plots to bleed into one another.

### Compare the Two Styles:

```python
# ❌ ANTI-PATTERN: Procedural State Machine (DO NOT USE IN PRODUCTION)
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.title("Revenue Trend")
plt.xlabel("Month")

# ✅ PRODUCTION STANDARD: Explicit Object-Oriented Interface
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, color="#38bdf8", linewidth=2.0, label="Revenue")
ax.set_title("Revenue Trend", fontsize=12, fontweight="bold")
ax.set_xlabel("Month", fontsize=10)
ax.legend()
```

---

## 3. Multi-Panel Dashboards & Subplot Layouts

Create structured analytical grids using `plt.subplots(nrows, ncols)`:

```python
fig, axs = plt.subplots(2, 2, figsize=(10, 7), constrained_layout=True)

# Panel (0, 0): Top-Left
axs[0, 0].plot(time_data, signal_data, color="#38bdf8")
axs[0, 0].set_title("Raw Waveform")

# Panel (0, 1): Top-Right
axs[0, 1].bar(["A", "B", "C"], [10, 25, 18], color="#10b981")
axs[0, 1].set_title("Category Volume")

# Panel (1, 0): Bottom-Left
axs[1, 0].hist(distribution_data, bins=20, color="#f472b6")
axs[1, 0].set_title("Frequency Distribution")

# Panel (1, 1): Bottom-Right
axs[1, 1].scatter(x_feat, y_feat, color="#fbbf24")
axs[1, 1].set_title("Feature Correlation")
```

---

## 4. Master Visualization Types

### A. Line & Shaded Area Plots (`ax.fill_between`)
Ideal for time-series forecasting, uncertainty intervals, or confidence bands:
```python
ax.plot(x, mean_prediction, color="#38bdf8", label="Forecast")
ax.fill_between(x, lower_bound, upper_bound, color="#38bdf8", alpha=0.2, label="95% CI")
```

### B. Horizontal Benchmark Bars (`ax.barh`)
Best for comparing names or categories with long string labels:
```python
y_pos = np.arange(len(models))
ax.barh(y_pos, latency_ms, color="#10b981", height=0.6)
ax.set_yticks(y_pos)
ax.set_yticklabels(models)
ax.invert_yaxis()  # Top-ranked model appears first
```

### C. 2D Correlation Heatmaps (`ax.imshow`)
```python
im = ax.imshow(correlation_matrix, cmap="viridis", interpolation="nearest")
cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label("Correlation Coefficient", rotation=270, labelpad=15)
```

---

## 5. Headless Web Production in Flask/Gunicorn (`'Agg'`)

When running inside background WSGI workers or Docker containers without an active GUI window server, importing default Matplotlib triggers `_tkinter.TclError: no display name`.

### The Mandatory Initialization Pattern:
```python
import os
# Configure cache to a writable path in restricted containers:
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib_cache")

import matplotlib
# Enforce thread-safe non-GUI backend:
matplotlib.use("Agg")
import matplotlib.pyplot as plt
```

---

## 6. In-Memory Base64 Serialization (Zero Disk Clutter)

Avoid saving charts to temporary `.png` files on disk. Render the figure directly into a byte buffer:

```python
import io
import base64

def render_figure_to_base64(fig: plt.Figure) -> str:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=100)
    plt.close(fig)  # Free figure resources immediately
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode("utf-8")
```

### In Flask Route:
```python
@python_bp.route("/api/chart")
def get_chart():
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot([1, 2, 3], [10, 20, 15])
    b64_str = render_figure_to_base64(fig)
    return jsonify({"image_base64": b64_str})
```

### In HTML / Jinja2 Template:
```html
<img src="data:image/png;base64,{{ image_base64 }}" alt="Dynamic Chart">
```

---

## 7. Memory Leak Prevention: The `plt.close(fig)` Rule

Every instantiated Figure object is retained inside Matplotlib's global tracking registry until explicitly closed.

```python
# DISASTROUS IN A WEB SERVER (Accumulates gigabytes of leaked RAM):
def leak_request():
    fig, ax = plt.subplots()
    return render(fig)  # Figure stays alive forever!

# CORRECT (Zero memory leak):
def safe_request():
    fig, ax = plt.subplots()
    try:
        return render(fig)
    finally:
        plt.close(fig)   # Destroys C-buffers & cleans registry
```

---

## 8. Professional Styling & Dark Mode Themes

To match platforms like **Teach Cloud**, configure global or context-managed styling:

```python
DARK_THEME = {
    "figure.facecolor": "#0f172a",  # Slate 900
    "axes.facecolor": "#1e293b",    # Slate 800
    "axes.edgecolor": "#334155",    # Slate 700
    "text.color": "#f8fafc",        # Slate 50
    "axes.labelcolor": "#94a3b8",   # Slate 400
    "xtick.color": "#94a3b8",
    "ytick.color": "#94a3b8",
    "grid.color": "#334155",
    "grid.linestyle": "--",
}

with plt.rc_context(DARK_THEME):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid(True)
```

---

## 9. Common Developer Pitfalls & Anti-Patterns

### ❌ Pitfall 1: Calling `plt.show()` inside a Web Server
`plt.show()` blocks worker process execution while waiting for a desktop GUI window that will never open.

### ❌ Pitfall 2: Overcrowded Tick Labels
When dates or numbers overlap, rotate or downsample ticks:
```python
fig.autofmt_xdate(rotation=45)
# OR:
ax.tick_params(axis='x', rotation=45)
```

---

## 10. Matplotlib Quick-Reference Cheat Sheet

```python
# Setup
fig, ax = plt.subplots(figsize=(8, 4))       # 1 Figure, 1 Subplot
fig, axs = plt.subplots(2, 2)               # 2x2 Grid of Subplots

# Common Plot Types
ax.plot(x, y, color="blue", lw=2)           # Line plot
ax.scatter(x, y, s=30, alpha=0.7)           # Scatter plot
ax.bar(categories, values)                  # Vertical bars
ax.barh(categories, values)                 # Horizontal bars
ax.hist(data, bins=25, density=True)        # Histogram
ax.imshow(matrix, cmap="viridis")           # Heatmap / Matrix

# Decoration & Polish
ax.set_title("Title", fontsize=12)          # Plot title
ax.set_xlabel("X Label")                    # Axis label
ax.set_xlim(0, 100)                         # Range limit
ax.grid(True, linestyle="--", alpha=0.5)    # Grid lines
ax.legend(loc="upper right")                # Legend box

# Output & Teardown
plt.tight_layout()                          # Auto spacing
fig.savefig("output.png", dpi=150)          # Disk save
plt.close(fig)                              # Memory cleanup
```

---

## 11. 3D Scientific Visualizations & Optimization Landscapes (`projection='3d'`)

For computational physics, machine learning loss surfaces, and 3D geometric modeling, Matplotlib provides `mpl_toolkits.mplot3d`:

```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(9, 6), facecolor="#0f172a")
ax = fig.add_subplot(111, projection="3d")
ax.set_facecolor("#0f172a")

# 1. 2D Coordinate Grid & Multimodal Loss Function
x = np.linspace(-3.0, 3.0, 55)
y = np.linspace(-3.0, 3.0, 55)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2) + 1e-6
Z = np.sin(2.0 * R) / R + 0.15 * (X**2 + Y**2)

# 2. 3D Surface Mesh with Antialiased Shading
surf = ax.plot_surface(X, Y, Z, cmap="plasma", alpha=0.88, edgecolor="#1e293b", linewidth=0.25)

# 3. Projected 2D Iso-Contour Lines on the Floor Plane
z_min = float(np.min(Z) - 0.4)
ax.contour(X, Y, Z, zdir="z", offset=z_min, levels=14, cmap="plasma")

# 4. Gradient Descent Optimization Trajectory Overlay
t = np.linspace(0, 1, 35)
tx, ty = 2.4 * np.exp(-2.2 * t) * np.cos(3.5 * t), 2.4 * np.exp(-2.2 * t) * np.sin(3.5 * t)
tr = np.sqrt(tx**2 + ty**2) + 1e-6
tz = np.sin(2.0 * tr) / tr + 0.15 * (tx**2 + ty**2)
ax.plot(tx, ty, tz, color="#38bdf8", lw=2.5, marker="o", markersize=3, label="Optimizer Trajectory")

# 5. Camera Positioning
ax.view_init(elev=28, azim=132)
ax.set_title("3D Loss Surface & Optimization Trajectory", color="#f8fafc", fontweight="bold")
ax.legend(facecolor="#0f172a", edgecolor="#334155")
```

---

## 12. Production Cloud Observability & Status Dashboard Layouts

For monitoring real-time pipelines, DevOps SLAs, and microservice fleets, combine heterogeneous plots onto a unified status dashboard canvas:

```python
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(11, 7.5), facecolor="#0f172a")

# Panel 1: Microservice SLA Health Cards
services = ["Ingestion Gateway", "Vector DB", "Inference Fleet", "Postgres Meta"]
health = [99.98, 99.85, 96.40, 100.0]
colors = ["#10b981", "#10b981", "#f59e0b", "#10b981"]
bars = axs[0, 0].barh(services, health, color=colors, height=0.52)
axs[0, 0].set_xlim(90, 101)
axs[0, 0].set_title("Microservice Fleet Health & SLA Status", color="#f8fafc", fontweight="bold")

# Panel 2: Pipeline Stage Latencies
stages = ["1. Ingest", "2. Preprocess", "3. Inference", "4. Sink & Cache"]
latencies = [45, 128, 310, 35]
axs[0, 1].bar(stages, latencies, color=["#38bdf8", "#818cf8", "#f43f5e", "#34d399"], width=0.5)
axs[0, 1].set_title("Pipeline Stage Execution Latencies (ms)", color="#f8fafc", fontweight="bold")

# Panel 3: Live CPU/RAM Utilization vs SLA Alert Thresholds
t = np.linspace(0, 60, 60)
cpu = 52 + 18 * np.sin(t / 7)
axs[1, 0].plot(t, cpu, color="#38bdf8", lw=2, label="CPU %")
axs[1, 0].axhline(80, color="#f59e0b", linestyle="--", label="Warning (80%)")
axs[1, 0].axhline(90, color="#ef4444", linestyle=":", label="Critical SLA (90%)")
axs[1, 0].fill_between(t, 80, 100, color="#ef4444", alpha=0.1)
axs[1, 0].set_title("Cluster Node Telemetry Stream (60m)", color="#f8fafc", fontweight="bold")
axs[1, 0].legend()

# Panel 4: HTTP Status Code Ingress Distribution Donut
axs[1, 1].pie([98.42, 1.15, 0.35, 0.08], labels=["200 OK", "304", "429", "500"], autopct="%1.1f%%",
              colors=["#10b981", "#38bdf8", "#f59e0b", "#ef4444"], wedgeprops=dict(width=0.45))
axs[1, 1].set_title("HTTP Ingress Status Distribution (24h)", color="#f8fafc", fontweight="bold")

plt.tight_layout()
```

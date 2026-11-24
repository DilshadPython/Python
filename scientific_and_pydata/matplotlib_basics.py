# =========================================================================
# IMPORT NOTES & MODULE DEPENDENCIES:
# - import base64: In-memory binary serialization for HTML5 data-URI rendering.
# - import io: In-memory byte streaming without writing temporary files to disk.
# - from typing import Any, Dict, List, Optional, Tuple, Union: PEP 484 type annotations.
# - import numpy as np: Numerical array generation for plot data points.
# - import matplotlib: Non-interactive headless backend configuration ('Agg').
# - import matplotlib.pyplot as plt: State-machine & OOP plotting interface.
# =========================================================================
import base64
import io
import os
import time
from typing import Any, Dict, List, Optional, Tuple, Union

# Set writable cache dir for headless environment before importing matplotlib
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib_cache")

import matplotlib
# Enforce thread-safe headless backend for Web/WSGI servers (Gunicorn/Flask)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


# ─── THEME CONFIGURATION (MATCHING TEACH CLOUD DARK MODE) ─────────────────────

TEACH_CLOUD_STYLE = {
    "figure.facecolor": "#0f172a",      # Slate 900
    "axes.facecolor": "#1e293b",        # Slate 800
    "axes.edgecolor": "#334155",        # Slate 700
    "axes.labelcolor": "#94a3b8",       # Slate 400
    "xtick.color": "#94a3b8",
    "ytick.color": "#94a3b8",
    "text.color": "#f8fafc",            # Slate 50
    "grid.color": "#334155",
    "grid.linestyle": "--",
    "grid.alpha": 0.5,
    "font.sans-serif": ["Inter", "DejaVu Sans", "Helvetica", "Arial"],
}


def _fig_to_base64(fig: plt.Figure) -> str:
    """Serializes a Matplotlib figure into a clean base64 data URI string."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=110, facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode("utf-8")


# ─── SUBFOLDER 1: 01-OOP-FOUNDATIONS (LINE & DUAL AXIS) ──────────────────────


def generate_line_and_sine_plot() -> Dict[str, Any]:
    """
    [Subfolder Title: 01-OOP-Foundations -> line_and_signals.py]
    Generates a dual-frequency wave signal with customized markers, line styles,
    and annotations demonstrating the Object-Oriented Figure/Axes pattern.

    Returns:
        Dict[str, Any]: Base64 image string, point counts, and metadata.
    """
    with plt.rc_context(TEACH_CLOUD_STYLE):
        fig, ax = plt.subplots(figsize=(8, 4.2))

        x = np.linspace(0, 10, 200)
        y_signal = np.sin(x) * np.exp(-x / 6.0)
        y_carrier = np.cos(2 * x) * 0.4

        ax.plot(x, y_signal, color="#38bdf8", linewidth=2.5, label="Damped Signal: sin(x)*e^(-x/6)")
        ax.plot(x, y_carrier, color="#f472b6", linewidth=1.8, linestyle="--", label="High-Freq Carrier: 0.4*cos(2x)")

        # Annotation of local maximum
        max_idx = int(np.argmax(y_signal))
        ax.annotate(
            f"Peak: ({x[max_idx]:.2f}, {y_signal[max_idx]:.2f})",
            xy=(x[max_idx], y_signal[max_idx]),
            xytext=(x[max_idx] + 1.2, y_signal[max_idx] + 0.2),
            arrowprops=dict(facecolor="#34d399", edgecolor="#34d399", shrink=0.08, width=1.5, headwidth=6),
            color="#34d399",
            fontweight="bold",
            fontsize=9,
        )

        ax.set_title("Scientific Signal Waveform (OOP Figure & Axes)", fontsize=13, fontweight="bold", pad=12, color="#f8fafc")
        ax.set_xlabel("Time Horizon (Seconds)", fontsize=10)
        ax.set_ylabel("Amplitude Voltage (mV)", fontsize=10)
        ax.grid(True)
        ax.legend(loc="upper right", framealpha=0.3, facecolor="#0f172a", edgecolor="#334155")

        b64_img = _fig_to_base64(fig)

    return {
        "plot_type": "line_signal",
        "data_points": len(x),
        "peak_x": round(float(x[max_idx]), 3),
        "peak_y": round(float(y_signal[max_idx]), 3),
        "image_base64": b64_img,
    }


# ─── SUBFOLDER 2: 02-STATISTICS & COMPARISONS ─────────────────────────────────


def generate_bar_and_performance_plot() -> Dict[str, Any]:
    """
    [Subfolder Title: 02-Statistics-and-Comparisons -> bar_comparisons.py]
    Generates horizontal benchmark comparison bars showing execution speedup
    across Pure Python, NumPy Vectorized, and SciPy BLAS routines.

    Returns:
        Dict[str, Any]: Base64 image string and comparative speedup factors.
    """
    frameworks = ["Pure Python Loop", "Pandas Apply", "NumPy Vectorized", "SciPy Compiled"]
    latencies_ms = [420.5, 98.2, 5.4, 2.1]
    colors = ["#ef4444", "#f59e0b", "#38bdf8", "#10b981"]

    with plt.rc_context(TEACH_CLOUD_STYLE):
        fig, ax = plt.subplots(figsize=(8, 4.0))

        y_pos = np.arange(len(frameworks))
        bars = ax.barh(y_pos, latencies_ms, color=colors, height=0.55, edgecolor="#0f172a")

        ax.set_yticks(y_pos)
        ax.set_yticklabels(frameworks, fontsize=10, fontweight="bold")
        ax.invert_yaxis()  # Top-down hierarchy
        ax.set_xlabel("Execution Time (ms) — Lower is Better", fontsize=10)
        ax.set_title("Benchmarking Matrix Multiplication (1,000 x 1,000)", fontsize=13, fontweight="bold", pad=12, color="#f8fafc")
        ax.grid(axis="x")

        # Value labels next to bars
        for bar in bars:
            width = bar.get_width()
            ax.text(
                width + 8,
                bar.get_y() + bar.get_height() / 2,
                f"{width:.1f} ms",
                va="center",
                ha="left",
                color="#f8fafc",
                fontweight="bold",
                fontsize=9,
            )

        ax.set_xlim(0, max(latencies_ms) * 1.15)
        b64_img = _fig_to_base64(fig)

    return {
        "plot_type": "bar_benchmark",
        "frameworks": frameworks,
        "latencies_ms": latencies_ms,
        "speedup_vs_pure_python": round(latencies_ms[0] / latencies_ms[2], 1),
        "image_base64": b64_img,
    }


# ─── SUBFOLDER 3: 03-MULTI-PANEL DASHBOARD & HEATMAP ─────────────────────────


def generate_multiaxis_dashboard() -> Dict[str, Any]:
    """
    [Subfolder Title: 03-Dashboards-and-Heatmaps -> multi_axis_dashboard.py]
    Constructs a 2x2 multi-axis analytics dashboard comprising:
    (1) Normal distribution histogram with Gaussian curve
    (2) 2D Correlation heatmap matrix
    (3) Scatter plot with regression line
    (4) Cumulative trend area chart

    Returns:
        Dict[str, Any]: Base64 image string and sub-panel metrics.
    """
    np.random.seed(42)

    with plt.rc_context(TEACH_CLOUD_STYLE):
        fig, axs = plt.subplots(2, 2, figsize=(10, 7.5))
        fig.suptitle("Teach Cloud Scientific Analytics Studio — 2x2 Dashboard", fontsize=14, fontweight="bold", color="#38bdf8")

        # Panel 1: Histogram & PDF
        data_norm = np.random.normal(loc=50, scale=10, size=500)
        axs[0, 0].hist(data_norm, bins=25, density=True, color="#38bdf8", alpha=0.65, edgecolor="#0f172a")
        x_eval = np.linspace(20, 80, 100)
        pdf = (1 / (10 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_eval - 50) / 10) ** 2)
        axs[0, 0].plot(x_eval, pdf, color="#f43f5e", linewidth=2.0)
        axs[0, 0].set_title("Gaussian Distribution (N=500)", fontsize=11, fontweight="bold")
        axs[0, 0].grid(True)

        # Panel 2: 2D Heatmap Matrix
        corr_matrix = np.random.uniform(0.1, 0.95, (5, 5))
        np.fill_diagonal(corr_matrix, 1.0)
        im = axs[0, 1].imshow(corr_matrix, cmap="viridis", interpolation="nearest")
        axs[0, 1].set_title("Feature Correlation Heatmap", fontsize=11, fontweight="bold")
        cbar = fig.colorbar(im, ax=axs[0, 1], fraction=0.046, pad=0.04)
        cbar.ax.tick_params(colors="#94a3b8")

        # Panel 3: Scatter & Trend Line
        x_scat = np.linspace(1, 20, 30)
        y_scat = 2.5 * x_scat + np.random.normal(0, 5, len(x_scat))
        axs[1, 0].scatter(x_scat, y_scat, color="#34d399", s=35, alpha=0.85, edgecolors="#0f172a")
        m, b = np.polyfit(x_scat, y_scat, 1)
        axs[1, 0].plot(x_scat, m * x_scat + b, color="#fbbf24", linestyle="--", linewidth=2)
        axs[1, 0].set_title(f"Linear Fit: y = {m:.2f}x + {b:.2f}", fontsize=11, fontweight="bold")
        axs[1, 0].grid(True)

        # Panel 4: Cumulative Area Trend
        t_steps = np.arange(1, 31)
        growth = np.cumsum(np.random.poisson(lam=12, size=30))
        axs[1, 1].fill_between(t_steps, growth, color="#818cf8", alpha=0.35)
        axs[1, 1].plot(t_steps, growth, color="#818cf8", linewidth=2.2)
        axs[1, 1].set_title("Cumulative Pipeline Ingestion (30 Days)", fontsize=11, fontweight="bold")
        axs[1, 1].grid(True)

        plt.tight_layout()
        b64_img = _fig_to_base64(fig)

    return {
        "plot_type": "multiaxis_dashboard",
        "panels_count": 4,
        "regression_slope": round(float(m), 3),
        "total_cumulative_ingestion": int(growth[-1]),
        "image_base64": b64_img,
    }


# ─── SUBFOLDER 4: 04-3D-SURFACES-AND-OPTIMIZATION ────────────────────────────


def generate_3d_surface_plot() -> Dict[str, Any]:
    """
    [Subfolder Title: 04-3D-Surfaces-and-Meshes -> surface_loss_landscape.py]
    Generates a 3D scientific loss surface and wireframe with:
    - 3D Surface mesh with Plasma/Viridis colormap and anti-aliasing
    - Projected 2D floor contour curves (zdir='z')
    - 3D Gradient descent optimizer trajectory
    - Marked global optimum point with coordinates
    - Camera azimuth/elevation angle positioning

    Returns:
        Dict[str, Any]: Base64 image string, grid resolution, and optimal point.
    """
    with plt.rc_context(TEACH_CLOUD_STYLE):
        fig = plt.figure(figsize=(9, 6.5))
        ax = fig.add_subplot(111, projection="3d")

        # 1. Generate 2D coordinate grid
        x = np.linspace(-3.0, 3.0, 55)
        y = np.linspace(-3.0, 3.0, 55)
        X, Y = np.meshgrid(x, y)

        # 2. Bivariate multimodal loss landscape function
        R = np.sqrt(X**2 + Y**2) + 1e-6
        Z = np.sin(2.0 * R) / R + 0.15 * (X**2 + Y**2)

        # Floor offset for projected contour
        z_offset = float(np.min(Z) - 0.4)

        # 3. 3D Surface mesh with antialiasing and transparency
        surf = ax.plot_surface(
            X, Y, Z,
            cmap="plasma",
            alpha=0.88,
            edgecolor="#1e293b",
            linewidth=0.25,
            antialiased=True,
            rstride=1,
            cstride=1,
        )

        # 4. Projected 2D contour lines on the floor plane
        ax.contour(X, Y, Z, zdir="z", offset=z_offset, levels=14, cmap="plasma", linewidths=1.2)

        # 5. Simulated Gradient Descent trajectory curve
        t_steps = np.linspace(0, 1, 35)
        traj_x = 2.4 * np.exp(-2.2 * t_steps) * np.cos(3.5 * t_steps)
        traj_y = 2.4 * np.exp(-2.2 * t_steps) * np.sin(3.5 * t_steps)
        traj_r = np.sqrt(traj_x**2 + traj_y**2) + 1e-6
        traj_z = np.sin(2.0 * traj_r) / traj_r + 0.15 * (traj_x**2 + traj_y**2)

        ax.plot(
            traj_x, traj_y, traj_z,
            color="#38bdf8",
            linewidth=2.6,
            marker="o",
            markersize=3.5,
            label="Optimizer Trajectory (Adam/SGD)",
            zorder=10,
        )

        # 6. Mark Global Optimum
        min_idx = np.unravel_index(np.argmin(Z), Z.shape)
        opt_x, opt_y, opt_z = float(X[min_idx]), float(Y[min_idx]), float(Z[min_idx])
        ax.scatter(
            [opt_x], [opt_y], [opt_z],
            color="#34d399",
            s=140,
            marker="*",
            edgecolor="#ffffff",
            linewidth=1.2,
            label=f"Optimum: ({opt_x:.2f}, {opt_y:.2f})",
            zorder=11,
        )

        # 7. Configure camera view and dark theme panes
        ax.view_init(elev=28, azim=132)
        ax.set_zlim(z_offset, float(np.max(Z) * 1.05))

        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_edgecolor("#334155")
        ax.yaxis.pane.set_edgecolor("#334155")
        ax.zaxis.pane.set_edgecolor("#334155")
        ax.grid(True, color="#334155", linestyle="--", alpha=0.5)

        ax.set_title("3D Loss Landscape & Optimizer Trajectory", fontsize=13, fontweight="bold", pad=14, color="#f8fafc")
        ax.set_xlabel("Parameter X₁", fontsize=9, labelpad=8)
        ax.set_ylabel("Parameter X₂", fontsize=9, labelpad=8)
        ax.set_zlabel("Objective Loss J(θ)", fontsize=9, labelpad=8)

        # Colorbar
        cbar = fig.colorbar(surf, ax=ax, shrink=0.55, aspect=14, pad=0.08)
        cbar.set_label("Loss Value", color="#94a3b8", fontsize=9)
        cbar.ax.tick_params(colors="#94a3b8", labelsize=8)

        ax.legend(loc="upper left", framealpha=0.35, facecolor="#0f172a", edgecolor="#334155", fontsize=8)

        plt.tight_layout()
        b64_img = _fig_to_base64(fig)

    return {
        "plot_type": "3d_surface",
        "grid_resolution": f"{len(x)}x{len(y)}",
        "optimal_point": {"x": round(opt_x, 3), "y": round(opt_y, 3), "loss": round(opt_z, 3)},
        "image_base64": b64_img,
    }


# ─── SUBFOLDER 5: 05-STATUS & OBSERVABILITY DASHBOARDS ────────────────────────


def generate_status_observability_dashboard() -> Dict[str, Any]:
    """
    [Subfolder Title: 05-Observability-Dashboards -> system_status_dashboard.py]
    Generates a production Cloud & ML Data Pipeline Observability Status Dashboard:
    - Service Health & SLA Matrix with status badges
    - Pipeline Stage Execution Status Gantt with completion percentages
    - Real-Time Resource Utilization stream with SLA Warning/Critical thresholds
    - HTTP Status Code Breakdown & Request distribution

    Returns:
        Dict[str, Any]: Base64 image string, pipeline metrics, and system status summary.
    """
    with plt.rc_context(TEACH_CLOUD_STYLE):
        fig, axs = plt.subplots(2, 2, figsize=(11, 7.5))
        fig.suptitle("Production Data Pipeline & Observability Status Dashboard", fontsize=14, fontweight="bold", color="#38bdf8", y=0.98)

        # ── Panel 1: Microservice SLA & Health Status ───────────────────────
        services = ["Ingestion Gateway", "Vector Search DB", "Inference Fleet", "Postgres Meta"]
        health_scores = [99.98, 99.85, 96.40, 100.0]
        status_tags = ["HEALTHY", "HEALTHY", "DEGRADED", "HEALTHY"]
        colors = ["#10b981", "#10b981", "#f59e0b", "#10b981"]

        y_pos = np.arange(len(services))
        bars = axs[0, 0].barh(y_pos, health_scores, color=colors, height=0.52, edgecolor="#0f172a")
        axs[0, 0].set_yticks(y_pos)
        axs[0, 0].set_yticklabels(services, fontsize=9.5, fontweight="bold")
        axs[0, 0].invert_yaxis()
        axs[0, 0].set_xlim(90, 101)
        axs[0, 0].set_xlabel("SLA Uptime (%) — Target >= 99.9%", fontsize=9)
        axs[0, 0].set_title("Microservice Fleet Health & SLA Status", fontsize=11, fontweight="bold")
        axs[0, 0].grid(axis="x", linestyle="--", alpha=0.5)

        for bar, tag, score in zip(bars, status_tags, health_scores):
            axs[0, 0].text(
                score - 1.8,
                bar.get_y() + bar.get_height() / 2,
                f"{score:.2f}% [{tag}]",
                va="center",
                ha="right",
                color="#ffffff",
                fontweight="bold",
                fontsize=8,
            )

        # ── Panel 2: Pipeline Stage Execution Flow & Latency ─────────────────
        stages = ["1. Ingestion", "2. Clean & Preprocess", "3. Batch Inference", "4. Sink & Cache"]
        durations_ms = [45, 128, 310, 35]
        stage_colors = ["#38bdf8", "#818cf8", "#f43f5e", "#34d399"]

        stage_bars = axs[0, 1].bar(stages, durations_ms, color=stage_colors, width=0.5, edgecolor="#0f172a")
        axs[0, 1].set_ylabel("Stage Execution Time (ms)", fontsize=9)
        axs[0, 1].set_title("Pipeline Execution Stage Latencies", fontsize=11, fontweight="bold")
        axs[0, 1].tick_params(axis="x", labelsize=8.5)
        axs[0, 1].grid(axis="y", linestyle="--", alpha=0.5)

        for sbar in stage_bars:
            h = sbar.get_height()
            axs[0, 1].text(
                sbar.get_x() + sbar.get_width() / 2,
                h + 8,
                f"{int(h)}ms",
                ha="center",
                va="bottom",
                color="#f8fafc",
                fontweight="bold",
                fontsize=8.5,
            )
        axs[0, 1].set_ylim(0, max(durations_ms) * 1.25)

        # ── Panel 3: Resource Utilization vs SLA Alert Thresholds ───────────
        time_mins = np.linspace(0, 60, 60)
        np.random.seed(101)
        cpu_load = 52 + 18 * np.sin(time_mins / 7) + np.random.normal(0, 3.5, 60)
        mem_load = 62 + 6 * (time_mins / 60) + np.random.normal(0, 1.5, 60)

        axs[1, 0].plot(time_mins, cpu_load, color="#38bdf8", linewidth=2.0, label="CPU Usage (%)")
        axs[1, 0].plot(time_mins, mem_load, color="#a78bfa", linewidth=2.0, label="RAM Usage (%)")

        # Thresholds
        axs[1, 0].axhline(80, color="#f59e0b", linestyle="--", linewidth=1.4, label="Warning (80%)")
        axs[1, 0].axhline(90, color="#ef4444", linestyle=":", linewidth=1.6, label="Critical SLA (90%)")
        axs[1, 0].fill_between(time_mins, 80, 100, color="#ef4444", alpha=0.10)

        axs[1, 0].set_title("Cluster Node Telemetry Stream (Last 60m)", fontsize=11, fontweight="bold")
        axs[1, 0].set_xlabel("Elapsed Time (Minutes)", fontsize=9)
        axs[1, 0].set_ylabel("Utilization (%)", fontsize=9)
        axs[1, 0].set_ylim(35, 100)
        axs[1, 0].grid(True, linestyle="--", alpha=0.5)
        axs[1, 0].legend(loc="lower right", framealpha=0.35, facecolor="#0f172a", edgecolor="#334155", fontsize=7.5)

        # ── Panel 4: HTTP Status Code Distribution & Throughput ─────────────
        status_labels = ["200 OK", "304 Cached", "429 RateLimit", "500 Error"]
        status_shares = [98.42, 1.15, 0.35, 0.08]
        status_bar_colors = ["#10b981", "#38bdf8", "#f59e0b", "#ef4444"]

        wedges, texts, autotexts = axs[1, 1].pie(
            status_shares,
            labels=status_labels,
            autopct="%1.1f%%",
            startangle=140,
            colors=status_bar_colors,
            wedgeprops=dict(width=0.45, edgecolor="#0f172a", linewidth=1.5),
            pctdistance=0.75,
        )
        for t in texts:
            t.set_color("#cbd5e1")
            t.set_fontsize(8.5)
        for at in autotexts:
            at.set_color("#0f172a")
            at.set_fontweight("bold")
            at.set_fontsize(7.5)

        axs[1, 1].set_title("HTTP Ingress Status Distribution (24h)", fontsize=11, fontweight="bold")

        plt.tight_layout()
        b64_img = _fig_to_base64(fig)

    return {
        "plot_type": "status_observability_dashboard",
        "services_monitored": len(services),
        "pipeline_total_ms": sum(durations_ms),
        "peak_cpu_percent": round(float(np.max(cpu_load)), 2),
        "image_base64": b64_img,
    }


def render_preset(preset_id: int) -> Dict[str, Any]:
    """Preset dispatcher for live web sandbox integration."""
    start_time = time.perf_counter()
    if preset_id == 1:
        res = generate_line_and_sine_plot()
    elif preset_id == 2:
        res = generate_bar_and_performance_plot()
    elif preset_id == 3:
        res = generate_multiaxis_dashboard()
    elif preset_id == 4:
        res = generate_3d_surface_plot()
    elif preset_id == 5:
        res = generate_status_observability_dashboard()
    else:
        res = generate_line_and_sine_plot()

    res["duration_ms"] = round((time.perf_counter() - start_time) * 1000.0, 2)
    res["matplotlib_version"] = str(matplotlib.__version__)
    return res


if __name__ == "__main__":
    demo = render_preset(1)
    print(f"Generated {demo['plot_type']} in {demo['duration_ms']}ms. Base64 length: {len(demo['image_base64'])}")


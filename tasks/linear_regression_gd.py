"""
Linear Regression Using Gradient Descent
=========================================
Solves the full task: build LinearRegressionGD from scratch (no sklearn),
train it, predict, visualize convergence, and run learning-rate experiments.
"""

import numpy as np
import matplotlib.pyplot as plt


class LinearRegressionGD:
    """Simple Linear Regression (one feature) trained with batch Gradient Descent."""

    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.theta_0 = 0.0   # intercept
        self.theta_1 = 0.0   # slope
        self.sse_history = []

    def predict(self, X):
        X = np.asarray(X, dtype=float)
        return self.theta_0 + self.theta_1 * X

    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        n = len(X)
        self.sse_history = []

        for _ in range(self.n_iters):
            y_pred = self.predict(X)
            error = y_pred - y

            # Gradients of SSE = sum(error^2) w.r.t. theta_0, theta_1
            d_theta_0 = 2 * np.sum(error)
            d_theta_1 = 2 * np.sum(error * X)

            self.theta_0 -= self.learning_rate * d_theta_0 / n
            self.theta_1 -= self.learning_rate * d_theta_1 / n

            sse = np.sum(error ** 2)
            self.sse_history.append(sse)

        return self

    def mse(self, X, y):
        """Bonus: Mean Squared Error."""
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        y_pred = self.predict(X)
        return np.mean((y_pred - y) ** 2)

    def plot_training(self, X, y, save_path=None):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)

        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        # SSE over iterations
        axes[0].plot(range(1, self.n_iters + 1), self.sse_history, color="#2563eb")
        axes[0].set_xlabel("Iteration")
        axes[0].set_ylabel("SSE")
        axes[0].set_title("SSE over Iterations")
        axes[0].grid(alpha=0.3)

        # Regression line with data points
        axes[1].scatter(X, y, color="#111827", label="Data")
        x_line = np.linspace(X.min() - 5, X.max() + 5, 100)
        axes[1].plot(x_line, self.predict(x_line), color="#dc2626", label="Regression line")
        axes[1].set_xlabel("House size (m²)")
        axes[1].set_ylabel("Price (thousands)")
        axes[1].set_title("Regression Fit")
        axes[1].legend()
        axes[1].grid(alpha=0.3)

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=150)
        plt.close(fig)


if __name__ == "__main__":
    # ---------- 1. Load & understand the data ----------
    X = [50, 60, 70, 80, 90]
    y = [150, 180, 210, 240, 270]  # house price in thousands

    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    # ---------- 2. Create and train the model ----------
    model = LinearRegressionGD(learning_rate=0.001, n_iters=100)
    model.fit(X, y)

    print("=== Base model (lr=0.001, n_iters=100) ===")
    print(f"theta_0 (intercept): {model.theta_0:.6f}")
    print(f"theta_1 (slope):     {model.theta_1:.6f}")

    # ---------- 3. Prediction ----------
    size = 70
    predicted_price = model.predict(size)
    print(f"\nPredicted price for a {size} m² house: {predicted_price:.4f} (thousands)")

    # ---------- 4. Visualization ----------
    model.plot_training(X, y, save_path="/home/claude/base_model_plots.png")

    # ---------- 5. Experimentation: learning rates ----------
    print("\n=== Learning rate experiments (n_iters=100) ===")
    results = {}
    for lr, label in [(1.0, "very large"), (0.0001, "very small")]:
        m = LinearRegressionGD(learning_rate=lr, n_iters=100)
        m.fit(X, y)
        final_sse = m.sse_history[-1]
        results[label] = (m, final_sse)
        print(f"\nlr={lr} ({label}):")
        print(f"  theta_0 = {m.theta_0:.6f}, theta_1 = {m.theta_1:.6f}")
        print(f"  final SSE = {final_sse}")
        print(f"  SSE history (first 5): {m.sse_history[:5]}")

    # Plot comparison of SSE curves for lr experiments
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(range(1, 101), model.sse_history, label="lr=0.001 (base)", color="#16a34a")
    # very small lr is safe to show on same scale
    ax.plot(range(1, 101), results["very small"][0].sse_history, label="lr=0.0001 (very small)", color="#2563eb")
    ax.set_yscale("log")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("SSE (log scale)")
    ax.set_title("SSE Convergence: base vs. very small learning rate")
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("/home/claude/lr_comparison_plot.png", dpi=150)
    plt.close(fig)

    # Show what happens with the very large lr (diverging / exploding values)
    print("\nNote: with lr=1.0 the SSE explodes / diverges (see printed values above),")
    print("so it is not plotted on the same log-scale chart as the others.")

    # ---------- Bonus ----------
    print(f"\n=== Bonus: MSE of base model on training data ===")
    print(f"MSE = {model.mse(X, y):.6e}")

    # ---------- Bonus: normalize X and compare ----------
    print("\n=== Bonus: training on normalized X (lr=0.001, n_iters=100) ===")
    X_norm = (X - X.mean()) / X.std()
    model_norm = LinearRegressionGD(learning_rate=0.001, n_iters=100)
    model_norm.fit(X_norm, y)
    print(f"theta_0 = {model_norm.theta_0:.6f}, theta_1 = {model_norm.theta_1:.6f}")
    print(f"final SSE = {model_norm.sse_history[-1]:.6f}")
    pred_norm = model_norm.predict((70 - X.mean()) / X.std())
    print(f"Predicted price for 70 m² (normalized-feature model): {pred_norm:.4f}")

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(range(1, 101), model_norm.sse_history, color="#7c3aed")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("SSE")
    ax.set_title("SSE Convergence with Normalized X (lr=0.001)")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("/home/claude/normalized_plot.png", dpi=150)
    plt.close(fig)

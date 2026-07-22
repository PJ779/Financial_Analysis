import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def boxplot(df, columns):
    n_cols = 2
    n_rows = np.ceil(len(columns) / n_cols)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 5 * n_rows))
    axes = axes.flatten()

    for ax, col in zip(axes, columns):
        ax.boxplot(df[col].dropna(), patch_artist=True)
        ax.set_title(f"{col}\nSkew: {df[col].skew():.2f}")
        ax.set_ylabel("Value")

        # Print outlier stats
        q1, q3 = df[col].quantile(0.25), df[col].quantile(0.75)
        iqr = q3 - q1
        outlier_count = ((df[col] < q1 - 1.5*iqr) | (df[col] > q3 + 1.5*iqr)).sum()
        print(f"{col}: Q1={q1:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}, Outliers={outlier_count} ({outlier_count/len(df)*100:.1f}%)")

        # Remove empty axes
    for ax in axes[len(columns):]:
        fig.delaxes(ax)

    fig.suptitle("Boxplots for Outlier Detection", fontsize=16,)

    plt.tight_layout()
    plt.show()


def plot_distribution(df, columns):
    n_cols = 3
    n_rows = np.ceil(len(columns) / n_cols)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 5 * n_rows))
    axes = axes.flatten()

    for ax, col in zip(axes, columns):
        sns.hisplot(df[col].dropna(), df[col].dropna(), kde=True, bins=30, ax=ax)
        ax.set_title(f"{col}\nSkew: {df[col].skew():.2f}")
        ax.set_ylabel("Value")

        ax.set_xlabel("")
        ax.set_ylabel("Frequency")

       # Remove unused subplots
    for ax in axes[len(columns):]:
        fig.delaxes(ax)

    fig.suptitle("Feature Distributions", fontsize=16,)

    plt.tight_layout()
    plt.show()


def correlation_heatmap(df, method="pearson",
    figsize=(14, 12),
    annot=True,
    cmap="coolwarm"
):

    corr = df.select_dtypes(include="number").corr(method=method)
    # Create a heatmap
    g = sns.clustermap(
        corr,
        cmap=cmap,
        annot=annot,
        fmt=".2f",
        figsize=figsize,
        dendrogram_ratio=0.15,
        cbar_pos=(0.02, 0.8, 0.03, 0.15),
        linewidths=0.5,
    )

    # Rotate labels to prevent overlap
    plt.setp(g.ax_heatmap.get_xticklabels(), rotation=45, ha='right')
    plt.setp(g.ax_heatmap.get_yticklabels(), rotation=0)

    g.figure.suptitle('Clustered Feature Correlation: Multi-Collinearity Blocks', y=1.02, fontsize=16)
    plt.show()
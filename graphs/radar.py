import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
import numpy as np


def generate_radar_image(labels, values, output_path='radar.png'):
    """Generate a radar chart image.

    Args:
        labels (list[str]): Labels for each axis.
        values (list[float]): Numeric values corresponding to labels.
        output_path (str): Where to save the generated image.
    """
    num_vars = len(labels)

    # Compute angle of each axis in the plot (in radians)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # The plot is a circle, so we need to "complete the loop"
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.plot(angles, values, 'o-', linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax.set_ylim(0, max(values) if values else 1)

    plt.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    return output_path

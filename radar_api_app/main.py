"""Module dispatching graph generation functions."""

from graphs import radar


def execute(module: str, data: dict) -> str:
    """Execute a graph module based on its name.

    Parameters
    ----------
    module: str
        Name of the graph module (e.g. ``"radar"``).
    data: dict
        JSON payload received via the HTTP request.

    Returns
    -------
    str
        Message describing the action performed.

    Raises
    ------
    ValueError
        If ``module`` does not correspond to a known graph module.
    """

    if module == "radar":
        labels = data.get("labels", [])
        values = data.get("values", [])
        radar.generate_radar_image(labels, values)
        return "Radar Image generated succesfully"

    raise ValueError(f"Unknown module: {module}")



import math


def calc_dg_from_nm(kd_nm: float, temp_celsius: float = 25.0) -> float:
    """
    Calculates the change in Gibbs free energy (ΔG) in kcal/mol
    from a dissociation constant (Kd) provided in nanomolar (nM).

    Parameters:
    kd_nm (float): Dissociation constant in nanomolar (nM).
    temp_celsius (float): Temperature in degrees Celsius. Defaults to 25.0.

    Returns:
    float: ΔG in kcal/mol.
    """
    # Ideal gas constant in kcal/(K*mol)
    R = 0.001987204

    # Convert temperature to Kelvin
    T = temp_celsius + 273.15

    # Convert Kd from nM to Molar (M)
    kd_molar = kd_nm * 1e-9

    # Calculate ΔG = RT ln(Kd)
    delta_g = R * T * math.log(kd_molar)

    return delta_g



print(calc_dg_from_nm(10))



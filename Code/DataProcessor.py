import numpy as np

def voltage_to_strain(raw_voltage: float|np.ndarray[float]) -> float|np.ndarray[float]:
    '''
    Convert raw voltage readings from a strain gauge circuit to strain.

    The function assumes a Wheatstone bridge circuit with a strain gauge 
    and uses the following relationship:
    
    strain = (raw_voltage / Vex / Gain) * (2 / GF)
    
    Args:
        raw_voltage (float): The measured voltage output from the Wheatstone bridge circuit (in volts).
        
    Constants:
        Vex  (float): Excitation voltage applied to the Wheatstone bridge (in volts). Default is 4.98 V.
        GF   (float): Gauge factor of the strain gauge (dimensionless). Default is 2.12.
        Rg   (float): Resistance of the strain gauge (in ohms). Default is 350 Ohm.
        Gain (float): Amplification factor of the signal (dimensionless). Default is 1000.
    
    Returns:
        float: Calculated strain (dimensionless).
    
    Example:
        >>> voltage_to_strain(0.002)
        1.9178082191780822e-06
    '''
    Vex = 4.98    # Excitation voltage in volts
    GF = 2.12     # Gauge factor
    Rg = 350      # Resistance of strain gauge in ohms (not directly used)
    Gain = 1000   # Amplification factor
    
    strain = raw_voltage / Vex / Gain * 2 / GF
    
    return strain


def shear_strain_to_stress(E: float, poisson_ratio: float, strain: float|np.ndarray[float]) -> float|np.ndarray[float]:
    '''
    Calculate stress from shear strain by converting Young's modulus (E) to shear modulus (G).
    
    Args:
        E (float): Young's modulus (elastic modulus) in units of stress (e.g., Pa).
        strain (float): Shear strain (dimensionless).
        poisson_ratio (float): Poisson's ratio (dimensionless).
        
    Returns:
        float: Shear stress in the same units as Young's modulus.
    '''
    
    G = E / (2 * (1 + poisson_ratio))
    stress = G * strain
    
    return stress
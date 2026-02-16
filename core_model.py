import math

# Constantes fundamentales
c = 299_792_458                 # m/s
m_e = 9.109_383_56e-31          # kg
K = 1.7e-28                     # kg·m^3/s^2 ← CALIBRADO EMPÍRICAMENTE

def masa_efectiva(Zef: float, nval: int) -> float:
    """
    m* = m_e · (Zef / nval)^0.85
    Representa el gradiente de densidad inercial en la capa activa.
    """
    return m_e * (Zef / nval) ** 0.85

def radio_atomico(lambda_nm: float, m_eff: float) -> float:
    """
    r = ( λ² K / (4π² c² m*) )^(1/3)
    Retorna el radio en metros.
    """
    lambda_m = lambda_nm * 1e-9
    return ((lambda_m ** 2 * K) / (4 * math.pi ** 2 * c ** 2 * m_eff)) ** (1/3)
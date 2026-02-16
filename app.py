#!/usr/bin/env python3
"""
Dinámica Inducida – Cartografía Espectral Inversa (Web)
Flask app para calcular radios atómicos desde λ usando tu ontología.
"""
import math
from flask import Flask, render_template, request

app = Flask(__name__)

# Constantes fundamentales
c = 299_792_458                 # m/s
m_e = 9.109_383_56e-31          # kg
K = 2.42e-47                    # kg·m^3/s^2

def masa_efectiva(Zef: float, nval: int) -> float:
    """m* = m_e · (Zef / nval)^0.85"""
    return m_e * (Zef / nval)**0.85

def radio_atomico(lambda_nm: float, m_eff: float) -> float:
    """r = ( λ² K / (4π² c² m*) )^(1/3), devuelve r en metros."""
    lambda_m = lambda_nm * 1e-9
    return ((lambda_m**2 * K) / (4 * math.pi**2 * c**2 * m_eff))**(1/3)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None
    
    if request.method == "POST":
        try:
            elemento = request.form.get("elemento", "").strip() or "Elemento"
            Zef = float(request.form["Zef"])
            nval = int(request.form["nval"])
            lambda_nm = float(request.form["lambda_nm"])
            
            radio_exp_nm = request.form.get("radio_exp_nm", "").strip()
            radio_exp_nm = float(radio_exp_nm) if radio_exp_nm else None
            
            # Cálculos
            m_eff = masa_efectiva(Zef, nval)
            r_m = radio_atomico(lambda_nm, m_eff)
            r_nm = r_m * 1e9
            
            # Error si hay radio experimental
            error_pct = None
            if radio_exp_nm is not None:
                error_pct = 100 * (r_nm - radio_exp_nm) / radio_exp_nm
            
            resultado = {
                "elemento": elemento,
                "Zef": Zef,
                "nval": nval,
                "lambda_nm": lambda_nm,
                "m_eff": m_eff,
                "radio_derivado_nm": r_nm,
                "radio_exp_nm": radio_exp_nm,
                "error_pct": error_pct,
                "exito": abs(error_pct) < 15 if error_pct is not None else None
            }
            
        except Exception as e:
            error = f"Error en los datos: {e}"
    
    return render_template("index.html", resultado=resultado, error=error)

if __name__ == "__main__":
    app.run(debug=True)
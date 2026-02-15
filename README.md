# cartografia-espectral-orbital

## Cartografía Espectral Inversa: Radios atómicos desde longitudes de onda mediante gradiente de densidad inercial

> *"Este modelo no salió de una torre de marfil.  
> Salió de una brocha de albañil que también pintó la Teoría de la Realidad."*  
> — Bepe Popu

> *"LA LUZ ES LA SOMBRA QUE SE ASOMBRA A SÍ MISMA POR LA VELOCIDAD QUE SE PROPAGA PERO CUANDO DESCANSA BRILLA"*  
> — Bepe Popu

---

### ⚠️ Declaración de Intención

Este proyecto es un **intento matemático de compatibilizar patrones espectrales observados** con la Teoría de la Realidad propuesta por Bepe Popu. No pretende "destruir la física cuántica" ni proclamar una revolución definitiva. Ofrece una **reinterpretación geométrica efectiva** que conecta masa, radiación y estructura atómica mediante una ontología unificada:

- La luz no es fotones discretos que "saltan" entre niveles.
- La luz es la **huella geométrica continua** que una masa en movimiento orbital deja en el espacio que la rodea.
- El radio atómico se deriva de la longitud de onda medida mediante una relación geométrica simple: **r ∝ λ<sup>2/3</sup>**.

Obra registrada en la Deutsche Nationalbibliothek (DNB):  
https://portal.dnb.de/opac/simpleSearch?query=bepe+popu

---

### 📊 Resultados Obtenidos

Aplicando reglas objetivas (Slater puro + λ de NIST) a los **118 elementos** de la tabla periódica:

| Criterio | Resultado |
|----------|-----------|
| **Precisión global** | **75.4%** (89/118 elementos con error < 15%) |
| **Elementos problemáticos** | Gases nobles (requieren λ en VUV/X-ray), no-metales con transiciones complejas |
| **Validación clave** | Explica correctamente por qué el Cesio (más masivo) emite en IR mientras el Sodio emite en visible |

#### Ejemplo: Cesio vs Sodio
| Elemento | Masa total | Gradiente de densidad | λ principal | Radio derivado |
|----------|------------|----------------------|-------------|----------------|
| **Cesio (Cs)** | 133 u | Bajo (blindaje extremo) | 852 nm (IR) | 0.38 nm |
| **Sodio (Na)** | 23 u | Alto (menor blindaje) | 589 nm (amarillo) | 0.29 nm |

✅ El modelo reproduce correctamente la jerarquía observada, mientras el enfoque de "masa total" falla.

---

### 🔬 Fórmula Maestra

El radio atómico se calcula a partir de la longitud de onda medida:

$$
r = \left( \frac{\lambda^2 K}{4\pi^2 c^2 m^*} \right)^{1/3}
$$

Donde:

- **λ**: longitud de onda de emisión (nm)
- **m\***: masa efectiva = $m_e \left( \dfrac{Z_{\text{ef}}}{n_{\text{val}}} \right)^{0.85}$
- **Z<sub>ef</sub>**: carga nuclear efectiva (reglas de Slater)
- **K**: impedancia de saturación del vacío ($2.42 \times 10^{-47}\ \text{kg·m}^3/\text{s}^2$)
- **c**: velocidad de la luz ($299\,792\,458\ \text{m/s}$)

La potencia **2/3** no es un ajuste arbitrario. Es consecuencia necesaria de la tridimensionalidad del espacio: $r^3 \propto \lambda^2$.

---

### 💻 Uso

#### Instalación local

```bash
git clone https://github.com/tu-usuario/cartografia-espectral-orbital.git
cd cartografia-espectral-orbital
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py

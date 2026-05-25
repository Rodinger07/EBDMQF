# EBDM-3.0

**Emergent Dark Matter from Quantum Fields in Warped Branes: Controlled Semiclassical Predictions and Multi-Probe Falsifiability**

This repository contains the complete numerical pipeline, data, and LaTeX source for the paper:

> Ricardo G. De Quevedo, "Emergent Dark Matter from Quantum Fields in Warped Branes: Controlled Semiclassical Predictions and Multi-Probe Falsifiability in EBDM-3.0", (2026).

## Quick Start

### Using Docker (Recommended)

```bash
git clone https://github.com/rdequevedo/EBDM-3.0.git
cd EBDM-3.0
docker build -t ebdm3.0 .
docker run -it --rm ebdm3.0


---

### 2. `requirements.txt`

```txt
numpy>=1.24
scipy>=1.10
matplotlib>=3.7
mpmath>=1.3
fenics>=2019.1.0
petsc4py>=3.18
slepc4py>=3.18
classy>=3.2.0
corner>=2.2.2
getdist>=1.4
pandas>=2.0
jupyter>=1.0

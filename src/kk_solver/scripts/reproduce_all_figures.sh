#!/bin/bash
echo "Reproducing all figures from EBDM-3.0..."

python src/analysis/generate_figures.py --all

echo "Done. Figures saved in figures/"

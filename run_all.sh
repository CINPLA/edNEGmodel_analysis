echo "Creating data for Figure 2..."
python3 figure2_PR_weak.py
python3 figure2_PR_strong.py
python3 figure2_edNEG_weak.py
python3 figure2_edNEG_strong.py
echo "Figure 2 done."

echo "Creating data for Figure 3..."
python3 figure3.py
echo "Figure 3 done."

echo "Creating data for Figure 4 and Figure 5..."
python3 figure4_figure5.py
echo "Figure 4 and 5 done."

echo "Creating data for Figure 6..."
python3 figure6_I.py
python3 figure6_II.py
echo "Figure 6 done."

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


batas_bawah_mu = #
batas_atas_mu = #

chi2_kiri = #
chi2_kanan = #

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

x_norm = np.linspace(60, 100, 1000)
se = # 
y_norm = stats.norm.pdf(x_norm, #, se)

ax1.plot(x_norm, y_norm, color='blue', linewidth=2)
ax1.axvline(79.03, color='black', linestyle='--', label=f'Rata-rata = {#}')
ax1.axvline(batas_bawah_mu, color='red', linestyle=':', label=f'Batas Bawah = {batas_bawah_mu:.3f}')
ax1.axvline(batas_atas_mu, color='red', linestyle=':', label=f'Batas Atas = {batas_atas_mu:.3f}')

x_fill_norm = np.linspace(batas_bawah_mu, batas_atas_mu, 100)
y_fill_norm = stats.norm.pdf(x_fill_norm, #, se)
ax1.fill_between(x_fill_norm, y_fill_norm, color='lightblue', alpha=0.5)

ax1.set_title('Distribusi Normal (Tingkat Kepercayaan #%)')
ax1.legend()
ax1.grid(alpha=0.3)


# --- Grafik 2: Distribusi Chi-Square (Untuk Variansi) ---
x_chi = np.linspace(30, 100, 1000)

y_chi = stats.chi2.pdf(x_chi, 60)

ax2.plot(x_chi, y_chi, color='green', linewidth=2)
ax2.axvline(60, color='black', linestyle='--', label=f'v = {60}')
ax2.axvline(chi2_kiri, color='red', linestyle=':', label=f'Batas Kritis Kiri = {chi2_kiri:.3f}')
ax2.axvline(chi2_kanan, color='red', linestyle=':', label=f'Batas Kritis Kanan = {chi2_kanan:.3f}')

x_fill_chi = np.linspace(chi2_kiri, chi2_kanan, 100)
y_fill_chi = stats.chi2.pdf(x_fill_chi, 60)
ax2.fill_between(x_fill_chi, y_fill_chi, color='lightgreen', alpha=0.5)

ax2.set_title('Distribusi Chi-Square (Tingkat Kepercayaan #%, Batasan v=60)')
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df1 = 49
df2 = 49
f_hitung = 4.18
f_05 = 1.61
f_01 = 1.975

batas_x = max(f_hitung, f_01) + 1.0 
x = np.linspace(0, batas_x, 1000)

y = stats.f.pdf(x, df1, df2)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y, color='cornflowerblue', linewidth=1.5)

x_biru = np.linspace(f_05, f_01, 100)
y_biru = stats.f.pdf(x_biru, df1, df2)
ax.fill_between(x_biru, y_biru, color='royalblue', alpha=0.9)

x_hijau = np.linspace(f_01, batas_x, 100)
y_hijau = stats.f.pdf(x_hijau, df1, df2)
ax.fill_between(x_hijau, y_hijau, color='lightgreen', alpha=0.9)

tinggi_kurva_f = stats.f.pdf(f_hitung, df1, df2)
tinggi_garis = max(tinggi_kurva_f, 0.15)  

ax.vlines(x=f_hitung, ymin=0, ymax=tinggi_garis, color='chocolate', linewidth=2)

ax.set_xticks([0, f_05, f_01, f_hitung])
ax.set_xticklabels(['0', f'f0.05={f_05}', f'f0.01={f_01}', f'F={f_hitung}'])

label_x = ax.get_xticklabels()
label_x[1].set_color('royalblue')
label_x[2].set_color('green')
label_x[3].set_color('chocolate')

ax.get_yaxis().set_visible(False)

ax.set_xlim(0, batas_x)
ax.set_ylim(bottom=0)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)

plt.title('Visualisasi Posisi Rasio Variansi Terhadap Titik Kritis F', pad=20)
plt.tight_layout()
plt.show()
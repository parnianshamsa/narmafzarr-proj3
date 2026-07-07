import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "پروژه 3 (1).xlsx"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Excel file not found at: {file_path}")

df = pd.read_excel(file_path, index_col=0)
df.columns = df.columns.str.strip()
df.index = df.index.str.strip()

print("--- Initial Data Read from Excel ---")
print(df)
print("\n" + "="*50 + "\n")

new_row_name = '700KB'
new_row_data = {'Alg.1': 80, 'Alg.2': 320, 'Alg.3': 700}

if new_row_name not in df.index:
    df_updated = pd.concat([df, pd.DataFrame([new_row_data], index=[new_row_name])])
else:
    df_updated = df.copy()

print("--- Data After Updating (700KB Added) ---")
print(df_updated)
print("\n" + "="*50 + "\n")

mean_alg2_initial = df.iloc[:, 1].mean()
mean_alg2_updated = df_updated.iloc[:, 1].mean()

print(f"Mean execution time for Alg.2 (100KB to 600KB): {mean_alg2_initial:.2f}")
print(f"Mean execution time for Alg.2 after update (100KB to 700KB): {mean_alg2_updated:.2f}")
print("\n" + "="*50 + "\n")

sns.set_theme(style="whitegrid")

# ── نمودار ۱: خطی ──
fig1, ax1 = plt.subplots(figsize=(8, 5))
for col in df_updated.columns:
    ax1.plot(df_updated.index, df_updated[col], marker='o', label=col)
ax1.set_title('Line Plot: Run Time vs Data Size')
ax1.set_xlabel('Data Size')
ax1.set_ylabel('Execution Time')
ax1.legend()
plt.tight_layout()
plt.show()

# ── نمودار ۲: میله‌ای ──
fig2, ax2 = plt.subplots(figsize=(8, 5))
df_updated.plot(kind='bar', ax=ax2)
ax2.set_title('Bar Plot: Algorithm Comparison')
ax2.set_xlabel('Data Size')
ax2.set_ylabel('Execution Time')
ax2.set_xticklabels(df_updated.index, rotation=0)
plt.tight_layout()
plt.show()

# ── نمودار ۳: جعبه‌ای ──
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df_updated, ax=ax3)
ax3.set_title('Box Plot: Run Time Distribution')
ax3.set_xlabel('Algorithms')
ax3.set_ylabel('Execution Time')
plt.tight_layout()
plt.show()

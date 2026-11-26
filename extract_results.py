import os
import glob
import re

log_files = glob.glob("docking_results/*_log.txt")
results = []

for log in log_files:
    filename = os.path.basename(log)
    name = filename.replace("_log.txt", "")
    
    if name == "test_out" or name == "ligands102":
        continue
        
    # 提取数字ID，比如 ligands15 -> 15
    match_id = re.search(r'\d+', name)
    if not match_id:
        continue
    num_id = int(match_id.group())
    
    # 分配组别
    if 1 <= num_id <= 4:
        group = "已知抑制剂"
    elif 5 <= num_id <= 54:
        group = "随机分子"
    else:
        group = "AI生成分子"
        
    with open(log, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    match_score = re.search(r'^\s*1\s+(-?\d+\.\d+)', content, re.MULTILINE)
    
    if match_score:
        score = float(match_score.group(1))
        results.append({"Ligand": name, "Group": group, "Affinity(kcal/mol)": score})

# 排序
results.sort(key=lambda x: x["Affinity(kcal/mol)"])

# 写入 CSV
with open("docking_scores_with_groups.csv", "w", encoding="utf-8-sig") as f:
    f.write("配体名字,组别,结合能(kcal/mol)\n")
    for r in results:
        f.write(f"{r['Ligand']},{r['Group']},{r['Affinity(kcal/mol)']}\n")
        
print(f"提取完成，包含组别标签！共 {len(results)} 个。")
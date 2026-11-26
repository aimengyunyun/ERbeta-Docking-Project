import os
import subprocess
import glob

vina_exe = r".\bin\vina.exe"
config_file = "config.txt"
ligand_dir = "ligands_pdbqt"
out_dir = "docking_results"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# 获取所有配体文件，并按文件名里的数字大小进行排序
ligands = glob.glob(os.path.join(ligand_dir, "*.pdbqt"))
ligands.sort(key=lambda x: int(''.join(filter(str.isdigit, os.path.basename(x).split('.')[0]))))

print(f"找到 {len(ligands)} 个配体文件，开始批量对接...")

success_count = 0
fail_count = 0

for lig in ligands:
    base_name = os.path.splitext(os.path.basename(lig))[0]
    out_file = os.path.join(out_dir, f"{base_name}_out.pdbqt")
    log_file = os.path.join(out_dir, f"{base_name}_log.txt")
    
    # 如果结果文件已经存在（比如刚才跑的4个），就跳过不重复跑了
    if os.path.exists(out_file) and os.path.exists(log_file):
        print(f"⏭️ {base_name} 已经存在，跳过。")
        success_count += 1
        continue

    print(f"正在对接: {base_name} ...")
    
    cmd = [
        vina_exe,
        "--config", config_file,
        "--ligand", lig,
        "--out", out_file
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ {base_name} 对接失败！(跳过)")
        fail_count += 1
        continue  # 关键修改：遇到错误跳过，继续下一个！
    else:
        with open(log_file, "w") as f:
            f.write(result.stdout)
        success_count += 1

print(f"\n全部对接完成！成功: {success_count} 个，失败: {fail_count} 个。")
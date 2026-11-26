# ERbeta-Docking-Proje# ERbeta-Docking-Project

## 📌 项目简介
本项目基于 AutoDock Vina 对靶点 ERβ (PDB ID: 1U3Q) 进行虚拟筛选。比较了已知抑制剂、随机分子库及 AI 生成分子库的对接打分结果，并通过 PyMOL 进行了结合模式的人工审查。

## 📂 文件目录结构
* `run_docking.py` / `extract_results.py`: 批量调用 Vina 及自动化提取打分的 Python 脚本。
* `docking_scores_with_groups.xlsx`: 最终提取的分子打分及组别统计表。
* `ligands_pdbqt.zip`: 102 个配体的 PDBQT 文件（解压后可用）。
* `docking_results.zip`: 所有对接输出的 log 和构象文件。
* `config.txt` / `all_ligands.smi`: 对接网格配置及化合物 SMILES 汇总。

## 📊 核心结果摘要
* 成功完成对接分子数：99 个
* **AI 生成分子平均得分 (-21.82 kcal/mol)** 优于随机分子 (-21.04 kcal/mol)。
* Top 10 分子中，AI 生成分子占据 7 席，证明了生成式 AI 在探索全新化学空间方面的潜力。

## 🛠️ 依赖工具
* PyMOL (结构清理与可视化)
* OpenBabel (格式转换与三维构象生成)
* AutoDock Vina (分子对接引擎)
* Python 3.10 (流程自动化)ct

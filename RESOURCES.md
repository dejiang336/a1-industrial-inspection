# A1 权威资料表（查阅用）

> **这是字典，不是课程表。** 不按顺序读、不要求「学完」、不打卡。
> 只在三种场景打开：① 阶段开始看该会什么（考纲）；② 写代码时查 API（字典）；③ 某个概念卡住（理论补丁）。
> 规则：单次 ≤15 分钟；读完当次在代码里用一次；同一问题查两个来源仍不懂 → 记卡点，换任务。
> 阅读约 31-47 小时，动手约 76-92 小时，阶段 1-6 合计约 107-139 小时（中位约 126h）；加可选阶段 7 和缓冲到 140 小时+。

---

## 总览

| 阶段 | 必查资源 | 阅读 | 动手 | artifact |
|---|---|---|---|---|
| 1 Python | Python 官方教程相关章节 + OpenCV 摄像头页 | 3-4.5h | 5-6h | `capture.py` |
| 2 OpenCV | OpenCV Python tutorials + NumPy 速查 | 4-5.5h | 8-10h | 10 行区域数对照表 + 对比图（可选） |
| 3a 采集 | 自写 `DATA.md` + 打光常识 + MVTec 缺陷定义 | 2.5-4.5h | 15-19h | 原图 + manifest |
| 3b 标注 | Label Studio / Roboflow quickstart | 3-5h | 9-11h | 标注数据集 v1 |
| 4 模型 | Anomalib quickstart + Folder 数据集 + metrics | 7-11h | 23-26h | 基线 + PatchCore + AUROC/F1 |
| 5 服务化 | FastAPI 中文教程三页 + sqlite3 文档 | 6.5-9h | 9-11h | API + 数据库 + `/docs` 截图 |
| 6 指标 | sklearn metrics + ML Yearning 错误分析章 | 4.5-7h | 7-9h | `reports/metrics.md` + 讲述稿 |
| 7 RAG（可选） | DeepSeek API + Prompt Guide RAG 章 | 3-5h | 7-9h | 检索/引用/拒答 demo |

---

## 阶段 1｜Python 基础

| 资源 | 类型/语言 | 用途 | 只读哪些 / 跳过哪些 | 投入 |
|---|---|---|---|---|
| Python 官方中文教程（docs.python.org/zh-cn/3/tutorial/） | 官方文档｜中文 | 考纲 + 字典 | 函数、文件、异常三节；按需查数据结构、模块。跳过 venv/pip、类、网络、并发 | 2.5-3h |
| 廖雪峰 Python 教程（liaoxuefeng.com） | 教程｜中文 | 字典 | 只查函数、文件两节；跳过 Web/异步/数据库 | 0-1h |
| OpenCV 摄像头入门页（docs.opencv.org → Python tutorials → Getting Started with Videos） | 官方文档｜英文，代码为主 | 字典 | `VideoCapture` / `read` / `imshow` / `waitKey` / `release` | 0.5h |

**边界**：类、venv/pip 本阶段跳过——类等 FastAPI 用到时学，venv 等 12 月装 torch 时学。你不是「学 Python」，是「用 Python 写出 `capture.py`」。

---

## 阶段 2｜NumPy + OpenCV

| 资源 | 类型/语言 | 用途 | 只读哪些 / 跳过哪些 | 投入 |
|---|---|---|---|---|
| OpenCV-Python Tutorials（docs.opencv.org，4.x → Python tutorials） | 官方文档｜英文，代码为主 | 考纲 + 字典 | GUI（读图/视频/绘图）、Core Operations（像素/ROI/通道/位运算）、Image Processing（颜色空间/阈值/滤波/形态学/Canny/轮廓）、Contour Features。跳过特征匹配、相机标定、3D、视频分析、ML 模块 | 3-3.5h |
| NumPy 官方 Quickstart + absolute basics（numpy.org/doc/stable/user/） | 官方文档｜英文，代码为主 | 考纲 | 数组创建、shape/dtype、索引切片、广播、reshape、axis、布尔索引。跳过线代/FFT/随机数细节 | 1-1.5h |
| matplotlib Pyplot tutorial（可选） | 官方文档｜英文 | 字典 | `imshow`、`subplot`、直方图；用来看颜色分布 | 0-0.5h |

**边界**：文档当字典，不顺序读；只查当前用到的 6-8 个函数页。不学 SIFT/ORB、相机标定、光流。你的缺陷是颜色/形状/位置问题，阈值 + 形态学 + 轮廓足够做 v1。

---

## 阶段 3a｜数据采集

| 资源 | 类型/语言 | 用途 | 只读哪些 / 跳过哪些 | 投入 |
|---|---|---|---|---|
| 自写 `DATA.md` | 项目文件｜中文 | 考纲 + SOP | 标签版式、三类缺陷造法、拍摄 SOP、manifest 字段 | 1-2h 写 |
| MVTec AD 官方页（mvtec.com/research-teaching/datasets/mvtec-ad） | 数据集页｜英文 | 理论补丁：缺陷词典 | 只看缺陷类型定义、采集条件、标注方式。**不下载训练、不报 MVTec 分数** | 0.5-1h |
| 康耐视中文照明技术文章（搜「机器视觉照明技术」） | 厂商文章｜中文（需核实具体篇目） | 理论补丁：打光 | 直接光、漫射/同轴、环形光、背光、低角度暗场；反光/阴影/色温。选 1-2 种台灯+白纸能复现的方案 | 1-1.5h |

**边界**：不追求工业级打光。目标是「同一个人、同一套设备、隔天能重拍出相似结果」，不是「拍得好看」。v1 只采 3 类缺陷 + 正常，正常 ≥50 张、缺陷合计 ≥30 张。

---

## 阶段 3b｜标注

| 资源 | 类型/语言 | 用途 | 只读哪些 / 跳过哪些 | 投入 |
|---|---|---|---|---|
| Label Studio 官方文档（labelstud.io/guide/） | 官方文档｜英文界面 | 考纲 + 操作 | Install、建项目、Labeling Setup（图像分类）、Import、Export | 2-3h |
| Roboflow 官方文档（docs.roboflow.com） | 官方文档｜英文 | 对照 | 上传、标注、数据集版本、导出。只用免费额度 | 1-2h |
| CVAT（备选） | 官方文档｜英文 | 备选 | 只在 Label Studio 装不上时替换，**不两个都学** | 0 |

**边界**：v1 只做图像级标签（normal / abnormal + 缺陷类型），导出 `normal/`、`normal_test/`、`abnormal/` 三个目录 + CSV；**不画框、不导 YOLO/COCO、不做分割**。框和 YOLO 是 v2。

---

## 阶段 4｜模型（只跑 PatchCore）

| 资源 | 类型/语言 | 用途 | 只读哪些 / 跳过哪些 | 投入 |
|---|---|---|---|---|
| Anomalib 官方文档（anomalib.readthedocs.io） | 官方文档｜英文，中等门槛 | 考纲 + 操作 | Installation、「Anomalib in 15 Minutes」、Folder 数据集（normal/abnormal）、PatchCore、metrics（AUROC/F1）、export。跳过自写模型、全部算法、分布式 | 5-6h |
| PyTorch 官方 Transfer Learning 教程 | 官方教程｜英文 | 理论补丁 | 只读一篇：Dataset/DataLoader、冻结 backbone、只训最后一层、train/val 循环 | 2-3h |
| 李宏毅机器学习 2023 春（可选，不进入验收） | 公开课｜中文 | 理论补丁 | 只挑 CNN、过拟合/训练技巧、迁移学习 3 讲；不做作业。**PatchCore 跑通后、周六大块 ≤2h** | 0-2h |

**边界**：只跑 PatchCore + 基线（阈值/模板匹配）；**不训第二个模型**。PaDiM/EfficientAD 是 v2 可选。不手推反向传播、不写自定义损失、不跑全部 Anomalib 模型。

---

## 阶段 5｜FastAPI + SQLite

| 资源 | 类型/语言 | 用途 | 只读哪些 / 跳过哪些 | 投入 |
|---|---|---|---|---|
| FastAPI 官方中文教程（fastapi.tiangolo.com/zh/tutorial/） | 官方文档｜中文 | 考纲 + 字典 | 第一步、路径/查询参数、请求体、请求文件、响应模型、错误处理、SQL 数据库、多文件应用、测试。跳过安全/OAuth2/JWT、WebSocket、SSE、后台任务 | 5-6h |
| Python 官方 sqlite3 文档（docs.python.org/zh-cn/3/library/sqlite3.html） | 官方文档｜中文 | 字典 | connect/cursor/execute/commit/close、参数化查询、`row_factory`、事务 | 1-2h |
| SQLite 官方 SQL 语法（sqlite.org/lang.html） | 官方文档｜英文，代码为主 | 字典 | CREATE/INSERT/SELECT/WHERE/ORDER BY/LIMIT/索引 | 0.5-1h |

**边界**：不引入 ORM。FastAPI 教程里的 SQLModel 章节只看思路，实际用标准库 `sqlite3`。v1 的 `/predict` 只返回 status/score/latency，不返回缺陷类别。

---

## 阶段 6｜指标与错误分析

| 资源 | 类型/语言 | 用途 | 只读哪些 / 跳过哪些 | 投入 |
|---|---|---|---|---|
| scikit-learn Metrics and scoring + Confusion matrix | 官方文档｜英文，中低门槛 | 考纲 + 字典 | precision/recall/F1、`confusion_matrix`、`classification_report`、宏/微平均、ROC-AUC | 2-3h |
| 吴恩达《Machine Learning Yearning》中文版（需核实译者/版本，以官方英文 PDF 为准） | 免费书｜中文 | 理论补丁 | 第 13-19 章为主，第 26、53-54 章选读；不看全书 | 2-3h |
| Anomalib Metrics 文档 | 官方文档｜英文 | 字典 | image-level vs pixel-level、AUROC/AUPRO/F1 的输出格式 | 0.5-1h |

**边界**：不学统计检验、不写论文级分析。测试集 <30 张时只报整体 AUROC/F1 + 错例表；缺陷类型只出现在错例表，不作为指标列。

---

## 阶段 7｜可选 RAG

| 资源 | 类型/语言 | 用途 | 只读哪些 / 跳过哪些 | 投入 |
|---|---|---|---|---|
| DeepSeek API 官方中文文档（api-docs.deepseek.com/zh-cn/） | 官方文档｜中文 | 考纲 + 字典 | 首次调用、模型与价格、JSON 输出、function calling、上下文缓存 | 1-2h |
| Prompt Engineering Guide（promptingguide.ai，有中文） | 教程｜中英 | 理论补丁 | 基本提示、few-shot、结构化输出、RAG 章节；跳过 agents/fine-tuning | 1-2h |
| BGE 中文 embedding 模型卡（BAAI/bge-small-zh-v1.5）+ sentence-transformers 文档 | 模型卡/文档｜中英 | 字典 | 加载、`encode`、余弦相似度；小于 1000 条记录不需要向量数据库 | 1h |

**边界**：不学 LangChain/LlamaIndex。数据量小，SQLite 存记录 + NumPy 余弦相似度就够，框架调试会吃掉这一周。

---

## 不整门学的清单

| 资源 | 为什么不要整门学 | 正确用法 |
|---|---|---|
| CS50P（哈佛 Python 课） | 约 10 周 + 英文 Problem Set，从「什么是编程」讲起；你有 C++/Java 底座 | 只在某个概念卡住时看单集，不做作业 |
| CS231n 全课 | 3 个大作业、手推反向传播；你用预训练模型和现成库 | 可选看 CNN/训练技巧 1 讲 |
| 李沐《动手学深度学习》全书 | 20+ 章，覆盖 RNN/Transformer，远超项目需要 | 按需看 CNN/微调 1-2 节 |
| 吴恩达深度学习专项 | 5 门课 100+ 小时，对「跑通项目」过重 | 用 ML Yearning 的错误分析章节替代 |
| 廖雪峰教程全站 | 含 Web/异步 IO/数据库/网络，项目一个都不用 | 只查函数、文件、异常几节 |
| OpenCV 全文档 | 特征匹配、相机标定、3D、视频分析，项目不碰 | 只读 GUI/Core/Image Processing/Contours |
| Anomalib 全模型 | 十几个算法逐个跑会变成刷榜 | 只跑 PatchCore + 基线；PaDiM 是 v2 |
| Ultralytics 全功能 | 跟踪/姿态/OBB/多卡，项目只用 classify 或 detect | v2 才用，只跑 train/val/predict/export |
| LangChain / LlamaIndex | 抽象层厚，小数据不需要向量库 | 直接调 API + SQLite + NumPy |
| 《流畅的Python》 | 描述符/元类/协程，现在看会挫败 | 项目跑通、找到工作后再看 |

---

## 版本坑速查

| 坑 | 现象 | 处理 |
|---|---|---|
| **OpenCV 显示不可用** | `cv2.imshow` 报 `The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support`；`getBuildInformation()` 显示 `GUI: NONE` | 装的是 `opencv-python-headless`。**不要按报错字面去重编译**。先用 `where python` + `sys.executable` 确认 `python` 和 `pip` 是同一解释器；`python -m pip show opencv-python-headless` 确认后，`python -m pip uninstall -y opencv-python-headless`，再 `python -m pip install opencv-python==4.13.0.92 -i https://pypi.tuna.tsinghua.edu.cn/simple`（默认 PyPI 在本机可能被重置，用清华镜像） |
| Python 3.14 装 Anomalib | Anomalib 2.7 官方 classifiers 只标到 3.12；PyTorch 2.12+ 已有 cp314 wheel，但 Anomalib 不在支持矩阵 | 12 月中建 3.11 venv 探针（先装 Python 3.11，预算 60 分钟）；不在 3.14 上硬装 Anomalib |
| OpenCV 4.x `findContours` | 返回 2 个值，旧教程写 3 个 | `contours, hierarchy = cv2.findContours(...)` |
| Anomalib v2 API | 旧博客用 v0.x 的 config/旧 CLI；v1 起用 Engine/Trainer | 只跟当前 readthedocs 版本；锁版本 |
| Ultralytics 版本迭代快 | YOLOv8/YOLO11/YOLO26 命名和参数变化 | 锁 `ultralytics==x.y.z`；能复现优先 |
| FastAPI/Pydantic v2 | 旧教程用 `orm_mode`，v2 是 `from_attributes` | 只跟官方中文教程当前版 |
| Windows 中文路径 | `cv2.imread` 返回 `None`，不报错 | 目录名用英文；必须中文时用 `np.fromfile` + `cv2.imdecode` |
| 摄像头被占用 | `isOpened()` 为 True 但读到黑屏 | 关掉其他占用程序；可试 `cv2.CAP_DSHOW` |
| SQLite 多进程写 | `database is locked` | demo 用单 worker；写库加 try/except 和超时 |
| Label Studio 导出压缩 | 导出图被缩放/压缩，指标偏低 | 评估尽量用原图；导出时选原始质量 |
| NumPy 2.x | 旧代码的 `np.float_` 等别名被移除 | 跟当前文档，不抄 2020 年前博客 |

---

## 附录：JD 校准（12 月中打开一次）

> 这不是日常资料，只在 12 月中、寒假第 3-4 周、2027-03-01 前使用。

### 选 JD 的 5 条硬标准

1. 岗位名匹配：工业视觉、机器视觉、视觉算法（应用向）、AI 应用开发（工业方向）。
2. 本科可投：至少 2 条；纯硕士算法岗只用来知道上限，不作为 checklist 依据。
3. 时间匹配：2027 届校招/实习或 2028 届提前批，发布时间不超过 6 个月。
4. 有完整正文：只有标题、薪资、学历的不算。
5. 来源分散：设备商、工业软件、AI 公司、制造业甲方/集成商，各 1 条。

### 七步操作

| 步骤 | 动作 | 产出 |
|---|---|---|
| 1 收集 | 5 条 JD 全文复制到一张表，保留链接、来源、日期 | 原始 JD 表 |
| 2 拆句 | 每条要求拆成「动词 + 对象 + 可验证证据」，删掉「熟悉/了解/优先/良好」等形容词 | 原子要求列表 |
| 3 映射 | 每条原子要求映射到阶段 1-7；映射不进去的记「项目外」 | 阶段映射 |
| 4 计数 | 统计每个阶段被几条 JD 提到（0-5），同时统计「项目外」 | 覆盖计数 |
| 5 盘点 | 给自己的证据打档：A 有代码+指标+能讲；B 跑过 demo 没改过；C 没有 | 差距表 |
| 6 定优先级 | ≥3/5 必做；1-2/5 做最小版；0/5 不做（闭环必需除外） | 寒假优先级 |
| 7 写回 | 在 PROGRESS 新增「JD 校准」一节，只追加 | 下月动作 |

### 判定规则

- 同一要求出现 **≥3/5** 条 = 必做，且要能演示、有数字。
- 出现 **1-2/5** 条 = 做最小版，不追深度。
- 出现 **0/5** 条 = 不做；唯一例外是项目闭环必需（如 FastAPI，即使 0 条也要最小版）。
- 只调整阶段内的深度和顺序，**不新增阶段、不扩工具链**。
- 社招 3-5 年 JD 不作为校准样本；算法研究岗的「手写算子/论文复现」不纳入 checklist。
- 翻译 JD 黑话：「熟悉 PyTorch」= 能跑通训练/推理、会看 loss，不是会写 CUDA；「了解工业视觉」= 知道打光/相机/缺陷类型，不是 5 年产线经验。

### 节奏

| 时间 | 动作 | 产出 |
|---|---|---|
| 12 月中 | 首批 5 条 JD | 覆盖计数 + 寒假优先级 |
| 寒假第 3-4 周 | 用 JD 对照误检和指标 | 继续 A1 / 切换的判断依据 |
| 2027-03-01 | 20 条 JD 全表 | 简历 bullet 逐条对照 |
| 每次投递前 | 目标公司 3 条硬要求 | 简历对应 3 行改写 |

**一句话原则**：用 5 条 JD 的**并集**做能力词典，用**交集**做必做清单。单条 JD 不决策，课程资源也不决策，只有「JD 高频项 + 你手上的 artifact」能决定下一步。

# A1 调试与断档手册

> 卡住超过 15 分钟、或连续两天不想打开项目时读。角色卡 `CLAUDE.md` 只留触发条件，细节在这里。

## 1. 卡住：10-25-40

- **0-10 分钟**：从报错最后一行往上读；打印 `type(x)`、`x.shape`、`len(x)`。
- **10-25 分钟**：用报错原文搜官方文档；对照最小 example；只查当前这一个问题。
- **25-40 分钟**：按下面的模板问 AI，**「我猜原因」空着就不答**。
- **40 分钟**：停。在 PROGRESS 记现象、已排除、下一步猜什么；**不删代码**；换小任务或收工。
- 贴别人的代码试通后，必须删掉重写一遍，否则不算修好。

### 求助模板

```
我想让：（目标）
我写了：（10 行以内）
现象/报错：（原文，不转述）
我已试过：（1-3 条）
我猜原因是：（一句话，必须先写；写「不知道」也算缺）
```

### 环境报错 vs 代码报错

先判断是哪一类，再决定要不要改代码：

| 现象 | 多半是 | 先做什么 |
|---|---|---|
| `imshow` 报 `The function is not implemented / Rebuild the library` | 装了 headless 版 OpenCV | 查 `RESOURCES.md` 版本坑表；不要按字面重编译 |
| `VideoCapture` 返回 `isOpened() == False` | 摄像头被占用 / 权限 / 驱动 | 关掉其他用摄像头的软件；试 `cv2.CAP_DSHOW` |
| 窗口一闪而过 | 单帧用了 `waitKey(1)` 且没有循环 | 单帧用 `waitKey(0)`；连续画面才用循环 + `waitKey(1)` |
| 按键没反应 | 图像窗口没有焦点 | 先点一下图像窗口，再按键 |
| 按键要按回车才生效 / 弹输入法候选框 | 中文输入法截走了字母键（`waitKey` 只拿 ASCII 码） | 切英文输入法（Shift 或 Win+Space）后再点窗口按键 |
| 看不到窗口 | 窗口在编辑器后面 | Alt+Tab / 看任务栏 |
| `imshow` 报 `-215 ... !_src.empty()` | `read()` 返回 `ret=False`，`frame` 是 `None` | 先 `print(ret, type(frame))`，`ret is False` 就打印并退出 |
| `ModuleNotFoundError: No module named 'cv2'` | 装到了另一个解释器 | `where python`、`sys.executable`、`cv2.__file__` 三条对齐 |

### 窗口残留 / 资源释放（2026-11-04 实测）

- 一次性脚本里**不调** `cv2.destroyAllWindows()`，进程退出后 Windows 照样回收窗口——注释掉后连跑两次，残留 0 个。它真正防的是**进程不退出**的场景：服务化、交互式调试、异常被捕获后继续跑。
- 下一次运行黑帧 / 打不开，通常不是窗口没关，而是 `cap.release()` 没执行到。释放放 `finally`：`cap = None` 在 try 前，`finally` 里 `if cap is not None: cap.release()`。

### 常见报错索引

| 报错关键词 | 最常见原因 | 下一步打印什么 |
|---|---|---|
| `ModuleNotFoundError` | 解释器不对 / 没装 | `sys.executable`、`pip -V` |
| `FileNotFoundError` | 路径错 / 工作目录错 | `os.getcwd()`、`os.path.exists(path)` |
| `cv2.error` / `(-215:Assertion failed)` | 图是 `None`、通道数不对、尺寸不对 | `type(img)`、`img.shape`、`img.dtype` |
| `ValueError: operands could not be broadcast` | 数组 shape 不匹配 | 两个数组的 `.shape` |
| `TypeError: 'NoneType' object is not subscriptable` | 上一步返回了 `None` | 上一步的返回值 |
| `UnicodeDecodeError` | 读文件没指定编码 | `open(..., encoding="utf-8")` |
| `Address already in use` | 端口被占 | 换端口 / 关旧进程 |

## 2. 断档

- **1-3 天**：正常接，不补。
- **4-7 天**：只做 15 分钟回归——跑最近脚本、读最后一条 PROGRESS，不学新内容。
- **8-14 天**：本周目标降到「一个脚本能跑」；11-12 月则提前触发 12 月中检查点。
- **超过 14 天**：写 5 行「重新立项」——为什么停 / 还想不想 / 最小一步 / 什么时候做 / 需要什么帮助。想继续就从最小一步开始；不想就写「暂停」并归档。
- **主线断档不降维护线**（那条规则只适用于算法/英语）。主线只做「下次 15 分钟最小动作」。
- 任何断档都不补进度、不追日历。

## 3. 想放弃

先分类，别混在一起处理：

- **A 技术卡点**（有明确报错）→ 走 10-25-40。
- **B 重复劳动**（采集/标注/调参）→ 45 分钟一段；写进度条「还差 N 张」；一次只标一类；允许放背景音。
- **C 对方向没兴趣** → 这是检查点的数据，不是当天要解决的问题；写 1-5 分 + 一句原因，收工。

最小动作：打开项目 15 分钟，只跑一个已有脚本。跑完还想停就停，不记账、不补时长。

**去留只在两处决定**：12 月中（换不换项目）、寒假第 3-4 周（继续/回 C/降档）。依据是 PROGRESS 的分数曲线和产出计数，不是当天情绪。**项目可以停，但不能挂着**：要么明确暂停（写一行），要么做 15 分钟。

# A1 术语表

> 每个术语：一句人话 + C++/Java 对照。只记实战中真正用过的，不提前囤。

## 工作目录（current working directory）
程序运行时所在的目录；相对路径都从它算起，**不是**从脚本文件所在目录算起。
C++：`ofstream("out.txt")` 存到哪，也看从哪个目录启动的程序。Java：`new File("data/x.jpg")` 同理。

## 绝对路径 / 相对路径
绝对路径从盘符或根目录写起（`C:\...`）；相对路径从工作目录算起（`data/raw`）。`os.path.abspath()` 把相对路径转成绝对路径——但它只是把**工作目录**拼在前面，并不锁定到脚本所在目录；换个目录启动，图就存到别处。

## 静默失败（silent failure）
函数失败但不抛异常，只通过**返回值**告诉你。`cv2.imwrite` 存不成时返回 `False`，程序照跑。
C++：`ofstream` 打开失败后 `is_open()` 为 false，但没人检查。Java：`File.createNewFile()` 返回 false。

## 哨兵值（sentinel value）
用一个特殊值表示「还没有」，例如 `last_path = None`；之后用 `if last_path:` 判断有没有。
C++：`nullptr`；Java：`null`。判断写成 `if (p != nullptr)` / `if (p != null)`。

## MD5
文件内容的指纹，内容相同则指纹相同、内容不同则指纹几乎必然不同。用来验证「两张图是不是同一帧」。

## 键盘码（key code）
`waitKey` 返回的整数：没按键是 -1，按键是对应字符的 ASCII 码（字母用 `ord('q')` 换算），Esc 是 27。高 8 位可能被后端塞修饰键，所以只取低 8 位 `key & 0xFF` 再比较。中文输入法开着时字母键会被 IME 截走，切英文才收得到。
C++：`_getch()` 拿键码；Java：AWT 的 `KeyEvent.getKeyCode()`。

## VideoCapture 对象 / `read()` 的返回值
`cv2.VideoCapture(0)` 返回**一个摄像头对象（句柄）**，代表「已和 0 号摄像头建立连接」——不是画面，也不是 `ret, frame` 元组。打开成功与否用 `cap.isOpened()` 查。
`ret, frame = cap.read()` 才返回两个值：`ret` 是**这一帧有没有读到**（True/False），`frame` 是**画面本身**——NumPy 数组，`shape=(480, 640, 3)` = 480 行 × 640 列 × 3 个颜色通道。
C++：`cv::VideoCapture cap(0);` 是对象，`cap.read(frame)` 返回 bool；Java：`new FileInputStream(path)` 拿到的是流对象，不是文件内容。

## ndarray（NumPy 数组）/ `shape`
`cv2.imread` 读进来的不是「图片」，是**一个 NumPy 多维数组**：图像每个像素的每个通道值，就是数组里的一个数。`.shape` 是**属性**（没有括号），返回元组：
`(行数, 列数, 通道数)` = `(高, 宽, 3)`。索引顺序同理：`img[y, x]`，第一个下标是行（往下），第二个才是列（往右）。
**宽在前是直觉陷阱**：`(640, 480)` 是错的写法，除非你在调 Java 风格接口。
C++：`cv::Mat` 的 `rows / cols / channels()`，同样「行在前」；Java：`BufferedImage.getHeight()/getWidth()`，这个反而是高在前、宽在后，名字里写清楚了。

## 灰度图（grayscale）
每个像素只剩一个数（0-255，0 最黑、255 最白）的**二维**图：`shape=(高, 宽)`，**没有通道维**；`(480,640,1)` 是三维，多了一个无意义的轴。维度是用来回答「还要再选一次什么」的——`gray[y, x]` 已经唯一确定一个数，所以到此为止。
C++：`cv::Mat` 灰度图 `channels()==1` 但 `dims==2`；Java：`int[480][640]` 与 `int[480][640][1]` 不是一回事。

## 返回值：状态还是数据
两种返回值别混：`cv2.imwrite` 返回 `True/False`（**状态**：存没存成）；`cv2.threshold` 返回 `ret`（**数据**：这次实际用的阈值，float）——Otsu 模式下函数自己算阈值，所以必须把用到的值还给你。
判断口诀：看到返回值先问「它是状态还是数据」，不要默认是状态。

## 真假判断（truthiness）
`if x:` 不要求 `x` 是 `bool`：`None`、`0`、`""`、`[]`、`()`、`{}` 算假，**其他都算真**。
坑：`return frame.shape` 返回 `(480, 640, 3)`，非空元组恒为真，`if` 永远进 True 分支——看着像判了成败，实际什么都没判。要判成败就返回**真正表示成败的值**（如 `imwrite` 的 bool）。
**ndarray 不一样，它不是恒真，是拒绝判断**：`if img:` 先调 `bool(img)`，元素多于 1 个时直接抛 `ValueError: The truth value of an array with more than one element is ambiguous`。所以「可能为 `None`」的对象一律用 `is None` / `is not None` 判空，不用真假判断。
C++：没有对应写法，`if (tuple)` 编不过；Java 必须是 boolean。Python 的宽松是这里唯一的新东西。

## `if __name__ == "__main__"`
每个 `.py` 被 Python 自动塞一个变量 `__name__`：**直接运行**该文件时等于 `"__main__"`，**被 import** 时等于模块名（`capture`）。
所以这行的人话是「只有别人直接运行我时才执行下面的启动动作」；没有它，任何 `import capture` 都会立刻开摄像头弹窗。
C++：`main()` 不会因为链接就被调用；Java：import 一个类不会执行它的 `main()`。

## 事件泵（event pump）
`waitKey(n)` 不只是「等 n 毫秒按键」，它还负责处理窗口的键盘/鼠标/重绘消息。`waitKey(1)` 每圈放行 1 毫秒，循环自己转；`waitKey(0)` 无限等，**按键成了循环的「发条」**——不按键，画面不刷新，循环体里的 30 秒判断也永远走不到。

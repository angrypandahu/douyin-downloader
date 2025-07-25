# douyin-downloader 图形界面（GUI）改造与跨平台打包方案

## 一、目标

- 将现有命令行/配置文件操作的抖音批量下载工具，升级为**图形化界面**，让用户无需命令行即可便捷操作。
- 支持**Windows**、**macOS**双平台一键安装和使用。

---

## 二、技术选型

### 1. GUI 框架

- **QFluentWidgets + PySide6**  
  - QFluentWidgets 是一套基于 Fluent Design 的高颜值 PySide6/PyQt6 组件库，适合现代化跨平台桌面应用开发。
  - 官网设计器可视化拖拽，极大提升开发效率：[QFluentWidgets Designer](https://qfluentwidgets.com/zh/pages/designer/)
  - 兼容 Windows/macOS/Linux，界面美观，体验优秀。

### 2. 打包工具

- **PyInstaller**  
  - 支持 Windows、macOS，能将 Python 项目打包为独立的可执行文件（.exe/.app）。
- 可选：`cx_Freeze`、`briefcase`、`nuitka`等。

---

## 三、功能界面设计

### 1. 主界面

- **链接输入区**：支持批量粘贴抖音链接
- **Cookie 配置区**：引导用户填写关键 Cookie 字段
- **下载选项**：多选框（视频/图片/音乐/封面/头像/JSON）
- **下载模式**：单选/多选（作品/喜欢/合集/音乐合集等）
- **数量与线程设置**：输入框
- **保存路径选择**：文件夹选择器
- **启动下载按钮**：一键开始
- **日志输出区**：实时显示下载进度与错误

### 2. 配置管理

- **导入/导出配置**（YAML/JSON）
- **参数记忆**：自动保存上次设置

### 3. 进阶功能

- **数据库开关**、**增量下载**、**时间范围过滤**等高级参数

---

## 四、主要改造点

1. **核心下载逻辑与界面解耦**  
   - 将 `DouYinCommand.py` 的参数解析、配置加载、日志输出等与下载主流程分离，封装为可调用的函数/类。
2. **GUI 事件驱动**  
   - 用户在界面上设置参数，点击“下载”后，调用核心下载逻辑。
3. **日志与进度回调**  
   - 日志输出、进度条等通过信号/回调与界面联动。
4. **配置文件兼容**  
   - 保持对 YAML 配置文件的兼容，支持导入/导出。

---

## 五、打包与分发

### 1. 依赖整理

- 新增依赖：`PySide6`、`QFluentWidgets`
- 保持原有依赖（见 `requirements.txt`）

### 2. 打包命令示例

- **Windows/macOS**（需在对应系统下打包）：
  ```bash
  pip install pyinstaller
  pyinstaller -F -w -i img/logo.png gui_main.py
  ```
  - `-F`：单文件
  - `-w`：无控制台窗口（GUI）
  - `-i`：图标

- **生成的文件**：
  - Windows：`dist/gui_main.exe`
  - macOS：`dist/gui_main.app` 或 `dist/gui_main`

### 3. 安装包制作（可选）

- Windows 可用 `Inno Setup` 制作安装向导
- macOS 可用 `create-dmg` 制作 DMG 安装包

---

## 六、开发步骤建议

1. **重构核心逻辑为可复用模块**
2. **设计并实现 GUI 界面（推荐用 QFluentWidgets Designer 拖拽生成 UI）**
3. **实现参数与配置的双向绑定**
4. **集成日志与进度反馈**
5. **本地测试与多平台打包**
6. **完善文档与用户指引**

---

## 七、参考目录结构

```
douyin-downloader/
├── gui/                        # GUI相关代码（QFluentWidgets+PySide6）
│   ├── __init__.py
│   ├── main_window.py          # 主窗口逻辑
│   ├── widgets/                # 自定义控件
│   ├── designer/               # QFluentWidgets Designer生成的UI文件
│   └── resources/              # 图标、图片等资源
├── core/                       # 核心业务逻辑（与界面解耦，便于复用/测试）
│   ├── __init__.py
│   ├── downloader.py           # 下载主流程（原DouYinCommand.py重构）
│   ├── config.py               # 配置加载与校验
│   ├── api.py                  # 抖音API相关
│   └── utils.py                # 通用工具
├── apiproxy/                   # 低层API代理（保持原有结构）
│   ├── __init__.py
│   ├── common/
│   ├── douyin/
│   └── tiktok/
├── tests/                      # 单元测试
│   ├── __init__.py
│   └── test_downloader.py
├── img/                        # 项目图片/LOGO
├── docs/                       # 文档
│   ├── gui_改造与打包方案.md
│   └── examples.md
├── requirements.txt            # 兼容pip的依赖清单（可选）
├── pyproject.toml              # 现代依赖与项目管理
├── README.md
├── main.py                     # CLI/GUI统一入口（可根据参数启动GUI或命令行）
└── .gitignore
```

---

## 八、后续可扩展

- 支持多任务/队列下载
- 支持多平台自动更新
- 支持多语言界面

---

# 参考资料
- QFluentWidgets 官网：[https://qfluentwidgets.com/zh/pages/designer/](https://qfluentwidgets.com/zh/pages/designer/) 
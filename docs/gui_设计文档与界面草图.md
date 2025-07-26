# douyin-downloader GUI 设计文档（QFluentWidgets风格）

## 1. 总体布局

- **主窗口**：采用 Fluent Design 风格，左侧为导航栏，右侧为主内容区。
- **导航栏**：常驻左侧，包含“批量下载”、“配置管理”、“日志/进度”、“关于”等入口。
- **主内容区**：根据导航切换不同功能页面。

---

## 2. 主要页面与功能

### 2.1 批量下载页

- **链接输入区**：多行文本框，支持批量粘贴抖音链接。
- **Cookie 配置区**：表单，分字段填写（msToken、ttwid、odin_tt、passport_csrf_token、sid_guard）。
- **下载选项**：多选框（视频、图片、音乐、封面、头像、JSON）。
- **下载模式**：多选框（作品、喜欢、合集、音乐合集）。
- **数量与线程设置**：数字输入框。
- **保存路径选择**：文件夹选择器。
- **启动下载按钮**：主操作按钮。
- **进度条**：展示当前下载进度。
- **实时日志输出区**：滚动文本框，显示下载日志。

### 2.2 配置管理页

- **导入/导出配置**：按钮，支持YAML/JSON。
- **参数记忆**：显示/编辑上次设置。

### 2.3 日志/进度页

- **历史日志查询**：日志列表+详情。
- **进度统计**：图表或进度条。

### 2.4 关于页

- **项目信息**、**联系方式**、**开源协议**等。

---

## 3. 交互说明

- 所有表单项均有提示和校验。
- 下载时主按钮变为“停止”，支持中断。
- 日志区支持复制、清空。
- 导航栏支持高亮当前页面。

---

# HTML 设计图（结构草图）

```html
<!-- 仅为结构草图，风格参考QFluentWidgets，实际UI更美观 -->
<div class="main-window">
  <aside class="nav-bar">
    <div class="logo">Douyin Downloader</div>
    <nav>
      <a class="nav-item active">批量下载</a>
      <a class="nav-item">配置管理</a>
      <a class="nav-item">日志/进度</a>
      <a class="nav-item">关于</a>
    </nav>
  </aside>
  <section class="content">
    <!-- 批量下载页 -->
    <div class="page page-download">
      <h2>批量下载</h2>
      <div class="form-row">
        <label>抖音链接</label>
        <textarea placeholder="每行一个抖音链接"></textarea>
      </div>
      <div class="form-row">
        <label>Cookie 配置</label>
        <input placeholder="msToken" />
        <input placeholder="ttwid" />
        <input placeholder="odin_tt" />
        <input placeholder="passport_csrf_token" />
        <input placeholder="sid_guard" />
      </div>
      <div class="form-row">
        <label>下载选项</label>
        <input type="checkbox" /> 视频
        <input type="checkbox" /> 图片
        <input type="checkbox" /> 音乐
        <input type="checkbox" /> 封面
        <input type="checkbox" /> 头像
        <input type="checkbox" /> JSON
      </div>
      <div class="form-row">
        <label>下载模式</label>
        <input type="checkbox" /> 作品
        <input type="checkbox" /> 喜欢
        <input type="checkbox" /> 合集
        <input type="checkbox" /> 音乐合集
      </div>
      <div class="form-row">
        <label>数量限制</label>
        <input type="number" placeholder="每类数量" />
        <label>线程数</label>
        <input type="number" placeholder="线程数" />
      </div>
      <div class="form-row">
        <label>保存路径</label>
        <input type="text" placeholder="选择文件夹" />
        <button>选择</button>
      </div>
      <div class="form-row">
        <button class="primary">开始下载</button>
      </div>
      <div class="form-row">
        <progress value="0" max="100"></progress>
      </div>
      <div class="form-row">
        <label>日志输出</label>
        <textarea readonly style="height:100px"></textarea>
      </div>
    </div>
    <!-- 其他页面结构类似，省略 -->
  </section>
</div>
```

---

# 设计要点说明

- **风格**：所有控件、按钮、进度条、导航栏均采用 QFluentWidgets 的 Fluent Design 风格，圆角、阴影、动画、主题色等。
- **布局**：主窗口采用左右结构，左侧导航，右侧内容区自适应切换。
- **可扩展性**：后续可轻松增加新页面或功能。
- **可用性**：所有输入项均有placeholder和校验，操作流畅。

---

## 参考文档

- [PyQt Fluent Widgets 官方文档](https://pyqt-fluent-widgets.readthedocs.io/zh-cn/latest/index.html)
- [QFluentWidgets Designer 使用说明](https://qfluentwidgets.com/zh/pages/designer/) 

已为你生成 QFluentWidgets 风格的主窗口 .ui 文件，路径为：

```
src/gui/designer/main_window.ui
```

你可以用 Qt Designer 或 QFluentWidgets Designer 打开和继续编辑。  
如需生成其他页面的 .ui 文件或自动生成 Python 代码，请随时告知！ 
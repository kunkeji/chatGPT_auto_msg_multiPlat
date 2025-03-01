# ChatGPT 自动消息多平台管理系统

一个强大的多平台自动化消息管理系统，支持多平台客服消息自动回复和管理。

## 🌟 特性

- 💬 多平台支持：集成千牛等多个电商平台的消息系统
- 🤖 智能自动回复：基于ChatGPT的智能消息回复
- 📊 数据管理：完整的消息历史记录和数据统计
- 🔒 安全可靠：支持SSL加密的WebSocket通信
- 🎯 精准营销：支持商品信息自动推送
- 🛠 可视化界面：基于PySide6的现代化GUI界面
- 🔄 实时同步：支持多客户端实时消息同步
- 📝 敏感词过滤：内置敏感词管理功能

## 🚀 快速开始

### 系统要求

- Python 3.8+
- Windows 10/11

### 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/kunkeji/chatGPT_auto_msg_multiPlat.git
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行程序：
```bash
python app.py
```

## 🔧 使用说明
https://github.com/kunkeji/chatGPT_auto_msg_multiPlat/issues/1

## 测试账号
账号：admin
密码：123456
最好自己注册账号，测试账号仅供测试使用。

注意，采用单账号登录，请勿多人共用账号。测试完成后请注册账号，可以联系我获取权限。

 
## 📦 打包指南

使用 auto-py-to-exe 工具打包时推荐配置：

1. 基础设置：
   - 脚本路径：`app.py`
   - 单文件打包：❌ 不勾选（推荐目录模式）
   - 控制台窗口：✅ 勾选（方便调试）

2. 附加文件：
   ```bash
   data;data/
   src;src/
   static;static/
   ```

3. 图标设置：
   - 使用项目根目录的 `logo.ico`

4. 高级配置：
   - 添加参数：`--noconfirm --clean`
   - 排除模块：`PyQt5,PyQt6`

5. 版本信息（可选）：
   - 产品名称：壳林智能客服
   - 申请管理员权限：✅ 勾选

安装打包工具：

```bash
pip install auto-py-to-exe
```

命令行打包方式（替代方案）：
```bash

pyinstaller app.py --noconsole --onefile --icon=logo.ico --add-data "data;data" --add-data "src;src" --add-data "static;static" --exclude-module PyQt5 --exclude-module PyQt6

```

打包后文件位于 `./dist` 目录，首次启动可能需要10-30秒初始化时间。若杀毒软件误报，请添加白名单。



## 📦 主要功能

- **用户管理**
  - 用户登录/注册
  - 权限管理
  
- **消息管理**
  - 自动回复设置
  - 消息历史记录
  - 敏感词过滤
  
- **商品管理**
  - 商品信息导入
  - 自动商品推送
  
- **数据统计**
  - 消息统计
  - 性能监控
  
## 🔧 配置说明

系统配置文件位于 `config.json`，主要配置项包括：

- 服务器配置
- 数据库设置
- API密钥配置
- 自动回复规则

## 📚 目录结构

```
├── app.py              # 主程序入口
├── src/               # 源代码目录
├── static/            # 静态资源
├── utils/             # 工具函数
├── data/              # 数据文件
├── msglog/            # 消息日志
└── browser_data/      # 浏览器数据
```

## 🤝 贡献指南

欢迎提交问题和功能需求！如果您想贡献代码：

1. Fork 本仓库
2. 创建您的特性分支
3. 提交您的更改
4. 确保代码符合规范
5. 提交 Pull Request

## 📄 版权说明

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🔄 版本历史

- v1.0.0.13 - 当前版本
  - 功能优化和bug修复
  - 新增自动更新功能
  - 性能提升

## 📞 技术支持

如有问题，请通过以下方式联系：

- 提交 Issue
- 发送邮件至：kunkeji@qq.com
- 访问官方网站：kunkeji.com
- 微信：kunkeji2021


## 🙏 致谢

感谢所有为这个项目做出贡献的开发者！
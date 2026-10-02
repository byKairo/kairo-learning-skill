<div align="center">

# 🧭 kairo-learning

### 把一次提问，变成真正学会的过程

面向 Codex 及其他 Agent 的自适应学习 Skill。它会查证资料、解释概念、设计练习、根据表现调整难度，并把进度留给下一次对话。

[![Skill](https://img.shields.io/badge/Agent%20Skill-kairo--learning-6f42c1?style=flat-square)](skills/kairo-learning-skill/SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-2ea44f?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-public%20preview-f59e0b?style=flat-square)](docs/validation.md)

[快速安装](#-安装) · [开始学习](#-怎么使用) · [更新](#-更新) · [卸载](#-卸载) · [完整教程](docs/getting-started.md)

</div>

---

## 💡 为什么做这个 Skill

普通 AI 对话很容易停在“解释过了”：回答很完整，用户也看懂了，但换一个情境仍然不会做；下一次打开对话，又要重新交代目标、基础和学到哪里。

kairo-learning 把学习从一次性回答改成一个连续循环：先判断你现在需要快速理解还是系统学习，再用实际回答和作品判断掌握程度，最后只保存有续学价值的记录。

它适合两类时刻：

| 你现在的状态 | kairo-learning 怎么做 |
| --- | --- |
| 有明确目标，例如“独立写出 SQL 查询” | 了解目标和基础，拆分近期路径，用练习与作品持续校准 |
| 只是好奇，例如“什么是 token？” | 直接给短解释和例子，沿你的追问继续展开，不强制启动课程 |

## ✨ 核心功能

| | 能力 | 实际作用 |
| --- | --- | --- |
| 🎯 | **目标导向学习** | 把“我想学……”变成可完成、可检查的近期任务 |
| 🔎 | **检索与查证** | 学习新主题前查找可靠资料，区分事实依据与教学方法 |
| 🧩 | **渐进式讲解** | 每次推进一个小目标，用短解释、例子、图示或交互降低理解负担 |
| 🧪 | **练习与反馈** | 根据你的回答或作品指出证据、误区和下一步修正 |
| 🧠 | **ICAP 学习活动** | 从被动接收逐步走向主动生成、建构联系和互动推理 |
| 📈 | **动态调整路径** | 按真实表现增减提示、改变难度或补齐前置知识 |
| 💾 | **跨会话续学** | 保存目标、进度、误区和下一步，下次从原位置继续 |
| 🔄 | **对话内更新** | 直接说“更新 kairo-learning”，覆盖旧版本并保留学习档案 |

## 🗺️ 它如何工作

![kairo-learning 的系统学习与问答探索流程](docs/learning-flow.svg)

## 📦 安装

### 安装到所有支持的 Agent

```bash
npx -y skills add byKairo/kairo-learning-skill -g --all
```

### 只安装到 Codex

```bash
npx -y skills add byKairo/kairo-learning-skill -g -a codex -y
```

安装前需要准备：

- Node.js 与 npm
- 支持 Agent Skills 的 Codex 或其他 Agent
- 若要使用检索与进度保存，还需允许 Agent 访问网络和本地文件

安装器来自 [vercel-labs/skills](https://github.com/vercel-labs/skills)。安装完成后，请打开一个新的 Agent 会话，让新 Skill 被加载。

## 🚀 怎么使用

你不需要学习固定命令，直接说出想学什么即可。

### 系统学习一个主题

```text
使用 $kairo-learning，带我学习 SQL。
我的目标是能够独立查询业务数据，每天可以学习 30 分钟。
```

### 快速理解一个概念

```text
什么是 token？请用一个简单例子解释，先不要展开太多。
```

### 用图示帮助理解

```text
使用 $kairo-learning，用流程图解释循环什么时候继续、什么时候停止。
```

### 针对作品获得反馈

```text
使用 $kairo-learning，检查这篇给初学者看的文章。
请根据结构、表达和可读性告诉我下一步先改什么。
```

### 继续上次学习

```text
使用 $kairo-learning，继续上次学习。
```

其他 Agent 的显式调用语法可能不同。无法使用 `$kairo-learning` 时，也可以直接说“使用 kairo-learning”。更多完整对话见 [使用教程](docs/getting-started.md) 和 [对话示例](examples/conversations.md)。

## 🧠 学习方法

Skill 会按任务选择合适的方法，不要求每次把所有方法走一遍。

| 方法 | 在学习中的用法 |
| --- | --- |
| 主动回忆 | 先尝试回答，再查看解释 |
| 间隔复习 | 隔一段时间重新检验，而不是把当天答对视为长期掌握 |
| 样例学习 | 先看一个完整例子，再逐步独立完成 |
| 渐退提示 | 掌握提高后减少提示，避免一直依赖模板 |
| 自我解释 | 让学习者说清为什么这样做，暴露模糊理解 |
| 迁移练习 | 换一个情境应用，判断是否真的会用 |
| ICAP | 根据学习者的实际产出，在被动、主动、建构和互动参与之间调整活动 |

这些研究支持的是具体学习机制，并不代表本 Skill 的整体效果已经经过实验验证。理论边界与来源见 [方法与证据](skills/kairo-learning-skill/references/methods.md) 和 [ICAP 参与框架](skills/kairo-learning-skill/references/icap.md)。

## 💾 学习档案与隐私

持续学习时，Agent 会把目标、必要的练习证据、误区和下一步保存在你自己的本地学习库中。默认入口位于用户文档目录的 `Codex/learning-records`，也可以由你指定其他位置。

```text
把我的学习档案保存在我指定的学习目录，以后从这里继续。
```

学习档案不会保存全部对话或整篇检索资料。跨会话恢复需要 Agent 能访问同一个目录；跨设备使用时，需要你自行同步该目录。模型服务如何处理对话和文件，取决于所使用的 Agent 与服务商。

## 🔄 更新

已经安装的用户无需先卸载。在 Codex 或其他支持 Skills 的 Agent 中直接说：

```text
更新 kairo-learning
```

也可以手动覆盖安装：

```bash
npx -y skills add byKairo/kairo-learning-skill -g --all
```

只更新 Codex：

```bash
npx -y skills add byKairo/kairo-learning-skill -g -a codex -y
```

更新只替换 Skill 的规则与资源，不删除独立存放的学习档案。

## 🗑️ 卸载

移除全局安装：

```bash
npx skills remove kairo-learning -g
```

只从 Codex 移除：

```bash
npx skills remove kairo-learning -g -a codex
```

如果当初安装在某个项目中而没有使用 `-g`，请进入该项目目录运行命令，并去掉 `-g`。

卸载只移除 Skill，不会自动删除学习档案。若要清除学习记录，请先确认实际保存位置并自行备份或删除，不要直接删除整个文档目录。详细说明见 [更新与卸载](docs/getting-started.md#5-更新和卸载)。

## 📂 仓库结构

```text
kairo-learning-skill/
├── skills/kairo-learning-skill/       # 可安装的 Skill
│   ├── SKILL.md                  # 核心规则与模式路由
│   ├── agents/openai.yaml        # Agent 展示信息
│   ├── references/               # 教学、检索、ICAP、档案和更新规则
│   └── assets/                   # 学习档案模板
├── docs/                         # 使用与验证文档
├── examples/                     # 对话示例
└── README.md
```

## 🧪 当前状态

kairo-learning 目前是公开试用版本。仓库结构、本机入口以及 `npx skills add` 安装流程已经验证；完整多轮教学、跨会话恢复和长期学习效果仍需更多真实使用反馈。示例用于展示交互方式，不构成学习效果证明。

- [查看安装与结构验证](docs/validation.md)
- [查看维护者验证环境](docs/maintainer-validation.md)
- [提交问题或参与改进](CONTRIBUTING.md)
- [查看版本记录](CHANGELOG.md)

## 📄 许可

本仓库原创内容采用 [MIT License](LICENSE)。引用资料的权利归原作者所有，链接不改变其许可。

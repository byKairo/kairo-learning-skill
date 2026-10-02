# kairo-learning

为 Codex 和其他支持 Skills 的 Agent 提供分步教学、简短问答和跨会话续学。仓库及源码文件夹为 `kairo-learning-skill`，调用名为 `kairo-learning`。

## 能做什么

| 情境 | 处理方式 |
| --- | --- |
| 有具体能力目标 | 了解基础，检索资料，制定近期路线，通过练习与作品调整教学 |
| 想弄懂一个概念 | 用短解释和例子回答，按需配图，不强制问诊或建档 |
| 希望接着上次学习 | 从本地档案恢复目标、误区、待答任务与下一步 |

学习方法包括主动回忆、间隔复习、费曼式讲解、自我解释、样例学习、交错练习与迁移检验，按任务选择。费曼式讲解要求学习者用日常语言解释并补例子，用于发现理解缺口；讲得通俗不代表具备实践能力。方法依据见 [方法与证据](skills/kairo-learning-skill/references/methods.md)。

![系统学习与问答探索流程](docs/learning-flow.svg)

## 安装

需要 Node.js、npm 和支持 Skills 的 Agent；资料检索和档案保存还需要所在环境的网络与文件能力。

安装到支持的 Agent：

```bash
npx -y skills add byKairo/kairo-learning-skill -g --all
```

只安装到 Codex：

```bash
npx -y skills add byKairo/kairo-learning-skill -g -a codex -y
```

安装后在新会话中使用：

```text
$kairo-learning 带我学习 SQL，目标是独立查询业务数据。
$kairo-learning 什么是 token？先用一个例子解释。
$kairo-learning 继续上次学习。
```

## 档案与更新

持续学习时保存目标、实际表现、误区和下一步。默认入口位于用户文档目录的 `Codex/learning-records`；可以指定其他位置。跨会话恢复需要访问同一目录。

直接说“更新 kairo-learning”，或重新执行原安装命令。更新规则资源时保留独立学习档案；本地手动修改过规则时先比较差异。

卸载：

```bash
npx skills remove kairo-learning -g
```

仅从 Codex 移除时添加 `-a codex`。项目内安装去掉 `-g`。卸载不删除独立学习档案。

## 资料与验证

- [使用教程](docs/getting-started.md)与[对话示例](examples/conversations.md)
- [验证范围](docs/validation.md)与[维护方法](docs/maintainer-validation.md)
- [版本记录](CHANGELOG.md)与[参与改进](CONTRIBUTING.md)

研究依据支持的是具体学习机制；本 Skill 的长期学习效果尚未验证。原创内容采用 [MIT License](LICENSE)。

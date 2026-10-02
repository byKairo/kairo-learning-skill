# 维护与验证

运行仓库自带的结构校验器，仅需 Python 3 标准库：

```bash
python3 scripts/validate_skill.py
```

它检查调用名、界面元数据、资源和相对引用。源码文件夹为 `kairo-learning-skill`，调用名为 `kairo-learning`；两者按项目约定区分。无需其他 Skill，也不依赖维护者电脑上的路径。

修改教学规则后，还需用实际对话验证相关行为：首次问诊、单次问答、跳过练习、开放作品反馈、纠错、保存后恢复。结构校验不能证明教学效果。

修改安装说明后，在新建的临时目录中验证：

```bash
npx -y skills add byKairo/kairo-learning-skill -a codex -y
```

比较安装后的 `SKILL.md`、`agents/`、`references/`、`assets/` 与源目录；用完只清理临时目录。不要用真实学习档案做公开测试，不把 `.env`、本机路径、缓存或个人学习记录提交到仓库。

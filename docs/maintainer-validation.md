# 维护者验证环境

本仓库的 Skill 本体是 Markdown 规则文件，用户安装和使用 kairo-learning 不需要 Python 依赖；`kairo-learning` 是安装器和显式调用使用的稳定 Skill id。

维护者在修改 Skill 后，可运行 Codex `skill-creator` 自带的结构校验脚本：

```bash
python /Users/dealer/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/kairo-learning-skill
```

该脚本需要 Python 包 `PyYAML` 来读取 `SKILL.md` 的 YAML frontmatter。若当前 Python 环境没有安装该依赖，会出现：

```text
ModuleNotFoundError: No module named 'yaml'
```

这只表示结构校验脚本没有启动成功，不表示 Skill 无法安装或运行。

## 推荐设置

不要依赖系统 Python 的全局包。维护者可在仓库根目录创建本地虚拟环境：

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install PyYAML
python /Users/dealer/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/kairo-learning-skill
```

`.venv` 是本地维护环境，不应提交到仓库。

## 需要检查什么

每次修改 Skill 规则或引用文件后，至少检查：

- `quick_validate.py skills/kairo-learning-skill` 能通过；
- Markdown 内部链接指向存在的文件；
- 新增 reference 已在 `SKILL.md` 中有明确路由；
- 文档中的安装、更新和卸载说明没有要求用户删除学习库；
- 若修改了公开安装命令，从干净临时项目实测安装。

若暂时无法安装 `PyYAML`，可以继续做 Markdown 链接和人工 diff 检查，但提交说明或交付记录中应注明 `quick_validate.py` 未运行成功及原因。

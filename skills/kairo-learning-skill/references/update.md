# 更新 kairo-learning

当用户要求“更新 kairo-learning”或“更新 kairo-learning skill”或类似说法时，按更新处理，不要求用户先删除当前 Skill。

## 原则

- 优先重新运行安装命令覆盖现有 Skill 规则资源；不要先执行 `skills remove`。
- 学习档案与 Skill 安装目录分开，更新 Skill 不需要移动或删除学习库。
- 若用户手动改过 Skill 安装目录中的规则文件，更新可能覆盖这些改动。先告知这一点；用户仍要求更新时继续。
- 只在执行会写入本地安装位置、下载网络资源或推送远端时按宿主权限机制请求授权。不要把更新说明扩大成删除、清理或重建学习库。

## 常用命令

全局更新所有支持宿主：

```bash
npx -y skills add byKairo/kairo-learning-skill -g --all
```

只更新 Codex：

```bash
npx -y skills add byKairo/kairo-learning-skill -g -a codex -y
```

项目内安装过的用户，应在原项目目录去掉 `-g` 后运行对应命令。

## 更新后检查

运行：

```bash
npx skills ls -g
```

若是项目内安装，运行：

```bash
npx skills ls
```

确认 `kairo-learning` 仍存在。随后打开新 Agent 会话，直接说：

```text
使用 kairo-learning，继续上次学习。
```

如果没有自动找到学习记录，提供原学习库路径；不要删除 Skill 或学习库来排查。

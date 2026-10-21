# CHANGELOG

## v1.1.1 — 2026-10-21

**新增**
- 第 12 项能力 `superpowers/`：开发方法论（obra/superpowers，15 个组合式技能：brainstorming / writing-plans / test-driven-development / subagent-driven-development / systematic-debugging / verification-before-completion / code-review 等），含总入口 `SKILL.md`。

**变更**
- 内置工作流升级为「快速 / 工程」双模式（嫁接点①）：第三步新增工程模式——设计定稿后走 superpowers（计划 → TDD → 子代理执行 → 验证 → 评审）交付已验证代码。
- 第一步需求模糊时触发 `superpowers/brainstorming` 收敛（嫁接点②）；新增第四步「完成前验证」——声称完成前必须跑测试/构建并附证据（嫁接点③）。
- 全局铁律新增 3 条：TDD 不可跳过、计划先行、完成前验证（方案 C 铁律融合）。
- README 与 SKILL.md 同步：能力表 11 → 12、路由/决策树/分册索引/技能关系/铁律/工作流全量更新；版本号 1.1.0 → 1.1.1。

> 本版总结：嫁接 superpowers 开发方法论为第 12 项能力，内置工作流实现「设计（CHT-UI-SKILLS）× 工程（superpowers）」接口对接：需求模糊先头脑风暴、代码生成可切工程模式、完成前强制验证。

## v1.1.0 — 2026-10-20

**新增**
- 第 11 项能力 `m3e-canvas/`：可拖拽 UI 设计（AI 生成 Material 3 设计 JSON → 分享链接 → 侧边栏/浏览器拖改 → 导出 vibe-coding 提示词），含 `scripts/make_link.py` 与 M3E 协议全文 `references/agent-spec.md`。
- `CHANGELOG.md`：版本迭代记录。

**变更**
- 内置工作流第七节升级为「方案矩阵」：第一步从 oil-ui 3 套方向升级为「oil-ui 调性 × 8 大分册技术气质 × 交互形态」多维组合（默认 6–9 版，可出十几版）。
- 第二步增加分支选择闸门：分支甲 draw-ui 出静态精细稿（原路径）；分支乙 m3e-canvas 出可拖改原型（新路径）。
- 第三步分支乙路径：改完原型导出 prompt，按用户指令喂给 AI 代码生成（默认不自动执行）。
- README 与 SKILL.md 同步：能力表 10 → 11、路由/决策树/分册索引/技能关系全量更新；版本号 1.0.0 → 1.1.0。

> 本版总结：技能集由 10 大能力扩至 11 大，新增可拖拽 UI 设计能力，并将内置工作流升级为「风格×技术×形态」方案矩阵 + 双分支出稿。

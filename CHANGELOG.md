# CHANGELOG

## v1.2.0 — 2026-10-23

**新增（AI 审美三件套）**
- 第 13 项能力 `frontend-design/`（`anthropics/skills`，Anthropic 官方）：设计哲学底座——像设计工作室主设那样思考，主题优先、避默认字体、列出并避开 5 大 AI 默认陷阱、两遍流程（先 token 设计计划 → 审校 → 再写码）。
- 第 14 项能力 `taste-skill/`（`Leonxlnx/taste-skill`，name: design-taste-frontend）：研究方向引擎——`scripts/draw.mjs` 从 247 个策展站提炼的 20 个研究方向发牌，`library/` 提供 type/palette/hero/section 蓝图，`scripts/inspect.mjs` 真实浏览器实测，三宽度截图 + rubric + fix 的 look-and-fix 循环；含 11 篇 `references/` 方法论文档。
- 第 15 项能力 `garden-skills/`（`ConardLi/garden-skills`）：风格配方库 + 设计工程师全流程——`skills/web-design-engineer` 内置 25 种锚定风格配方（Linear/Aesop/Pentagram/Bloomberg/Stripe…）+ Step 0 事实核查 + Design Direction Advisor 模式；另含 `web-video-presentation`/`gpt-image-2`/`beautiful-article`/`kb-retriever`/`motion-showreel` 共 6 技能。

**变更（深入嫁接，非仅入表）**
- 内置工作流第一步新增「审美打底（接口④，frontend-design）」与「采集方向素材（接口⑤，taste-skill/garden-skills）」两步，收尾用 taste-skill look-and-fix 做实测验收闭环。
- 全局铁律新增 3 条：12 反 AI 默认陷阱（frontend-design 5 tells）、13 实测而非空想（taste-skill）、14 事实先于设计（garden web-design-engineer Step 0）。
- README 与 SKILL.md 同步：能力表 12 → 15、frontmatter description/tags、决策树、触发词索引、「与其它技能的关系」（三者定位为审美底座/方向引擎/配方库）、组合模式新增「AI 审美三件套」；版本号 1.1.1 → 1.2.0。

> 本版总结：嫁接 Anthropic frontend-design、Leonxlnx/taste-skill、ConardLi/garden-skills 为第 13/14/15 项能力，把「审美哲学 + 方向引擎 + 风格配方」深度织入内置工作流第一步与全局铁律，专治 AI 生成界面的「模板味 / AI 味」。

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

---
name: superpowers
display_name: "Superpowers 开发方法论"
display_name_en: "Superpowers"
description: "给 AI 编程代理的一整套软件开发方法论技能集（obra/superpowers，MIT，第 12 项能力）。AI 拿到开发任务时不直接写代码，而是按流程走：头脑风暴收敛需求 → 拆解计划 → 测试驱动开发（TDD）→ 子代理驱动执行 → 系统化调试 → 完成前验证 → 代码评审。共 15 个可组合技能，按任务路由到 skills/ 对应子技能。"
category: development
version: 1.0.0
author: obra
tags:
  - development
  - tdd
  - planning
  - debugging
  - code-review
  - methodology
  - agent-skills
allowed-tools: Read,Write,Bash
---

# 12 · Superpowers 开发方法论 — 实战分册

> 给 AI 编程代理的一整套**组合式开发方法论**（上游：`obra/superpowers`，MIT）。核心思路：AI 接到开发任务时不直接动手写码，而是
> **先收敛需求 → 出实现计划 → 真·红绿 TDD → 子代理驱动执行 → 验证 → 评审**，全程按流程干活。
> 与 CHT-UI-SKILLS 的对接点：内置工作流第一步（需求模糊时触发 brainstorming）与第三步（工程模式：设计定稿后用本方法论把设计交付物变成已验证代码）。

## 核心工作流（自动触发）

```
接到开发任务
   ↓
① brainstorming（头脑风暴收敛需求，出 spec）
   ↓
② writing-plans（写实现计划，清晰到"热情但没品味的初级工程师"能执行）
   ↓ 用户说 go
③ subagent-driven-development（子代理驱动执行，TDD 红绿循环）
   ↓
④ systematic-debugging（系统化调试，按需）
   ↓
⑤ verification-before-completion（完成前验证）
   ↓
⑥ requesting-code-review / receiving-code-review（请求/接收代码评审）
   ↓
⑦ finishing-a-development-branch（收尾开发分支）
```

## 15 个技能一览（触发词 → skills/ 子技能）

| # | 技能 | 触发场景 |
|---|------|----------|
| 1 | `using-superpowers` | 总览：Superpowers 如何工作、何时触发 |
| 2 | `brainstorming` | 需求模糊、要探索方案、写 spec 前 |
| 3 | `writing-plans` | 需求已定，写可执行实现计划 |
| 4 | `executing-plans` | 计划已定，按计划逐步执行 |
| 5 | `test-driven-development` | 实现任何 feature/bugfix，写实现代码之前 |
| 6 | `subagent-driven-development` | 大任务拆给子代理并行驱动 |
| 7 | `dispatching-parallel-agents` | 需要并行调度多个 agent |
| 8 | `systematic-debugging` | 调试复杂 bug、原因不明 |
| 9 | `verification-before-completion` | 声称完成前，验证是否真的完成 |
| 10 | `requesting-code-review` | 请求他人/其他 agent 评审代码 |
| 11 | `receiving-code-review` | 收到评审意见后如何消化处理 |
| 12 | `finishing-a-development-branch` | 完成分支、合并、收尾 |
| 13 | `using-git-worktrees` | 多分支并行开发时用 worktree |
| 14 | `writing-skills` | 为 agent 编写新技能 |
| 15 | `diagnosing-superpowers` | Superpowers 自身行为异常时的诊断 |

## 全局铁律（并入 CHT-UI-SKILLS 主入口，见其第四节）

1. **TDD 不可跳过**：写任何实现代码前先写测试，且必须亲眼看过测试失败（红）再写实现到通过（绿）。
2. **YAGNI / DRY**：不做多余的东西；重复代码必须抽象。
3. **计划先行**：需求未收敛不进实现；计划未确认不动手。
4. **完成前验证**：声称"完成"前，必须运行验证（测试/构建/检查）并给出证据。

## 文件结构

```
superpowers/
├── SKILL.md                 # 本文件（总入口与路由）
└── skills/                  # 15 个组合式技能（标准 SKILL.md 格式，每技能自带 scripts/）
```

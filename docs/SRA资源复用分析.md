# SRA 资源复用分析

> **源**: [StarRailAssistant (Shasnow)](https://github.com/Shasnow/StarRailAssistant) — PC 端 1920×1080，同为星穹铁道
> **我们的 MaaFramework Pipeline 命名 vs SRA 文件名映射**
> 下载链接格式: `https://raw.githubusercontent.com/Shasnow/StarRailAssistant/main/resources/img/{路径}`

---

## 一、common/ — 通用按钮（4 张）

| 我们的文件名 | SRA 对应文件 | 匹配度 | 下载链接 |
|-------------|-------------|--------|----------|
| `CloseButton.png` | `receive_rewards/` 下有 `close.png`（但 SRA 没有专用的通用关闭图在各目录中） | ⚠️ 部分 | 需在 divergent_universe/close.png 找到或用 img/quit.png |
| `HomeButton.png` | 无直接匹配 | ❌ 需自截 | - |
| `Loading.png` | 无直接匹配 | ❌ 需自截 | - |
| `ExitButton.png` | `img/quit.png` 或 `img/quit2.png` | ⭐ 很可能能用 | `resources/img/quit.png` |

> **结论**: common/ 大多需自截，SRA 没有通用的 UI 按钮库。

---

## 二、login/ — 登录（3 张）

| 我们的文件名 | SRA 对应文件 | 匹配度 | 说明 |
|-------------|-------------|--------|------|
| `LoginButton.png` | `img/enter.png` | ⭐ 可能 | 进入游戏的按钮 |
| `MissionButton.png` | 无直接匹配 | ❌ 需自截 | 星穹列车主页的作战按钮，SRA 可能是程序化识别的 |
| `TitleLoading.png` | 无直接匹配 | ❌ 需自截 | 标题画面 |

> **结论**: login/ 基本需自截。

---

## 三、combat/ — 刷副本（8 张） ⭐ SRA 有大量资源

| 我们的文件名 | SRA 对应文件 | 匹配度 | 说明 |
|-------------|-------------|--------|------|
| `MissionButton.png` | 无 | ❌ | 主界面作战按钮 |
| `IntoMissionButton.png` | `tp/enter.png` | ⭐ 可能 | 进入关卡按钮 |
| `IntoMissionButton-White.png` | - | ❌ | 灰色不可点击态 |
| `EquimentButton.png` | `tp/caver_of_corrosion.png` | ⭐⭐ 可用 | 侵蚀隧洞的标签，SRA 有 16 张变体 |
| `Battle.png` | `tp/battle.png` 或 `currency_wars/battle.png` | ⭐⭐ 可用 | 挑战按钮 |
| `StartBattle.png` | `tp/battle.png` | ⭐ 可能 | 确认出战 |
| `AutoBattle.png` | `tp/battle_star.png` | ⭐ 可能 | 自动战斗按钮 |
| `BattlePause.png` | 无 | ❌ | 暂停按钮 |

> **结论**: 约 4/8 可以从 SRA 借用。

---

## 四、daily/ — 日常奖励（5 张） ⭐⭐⭐ SRA 资源最丰富

| 我们的文件名 | SRA 对应文件 | 匹配度 | 下载链接 |
|-------------|-------------|--------|----------|
| `DailyMissionsButton.png` | `receive_rewards/daily_reward.png` | ⭐⭐ 可用 | `resources/img/receive_rewards/daily_reward.png` |
| `NamelessHonorButton.png` | `receive_rewards/nameless_honor_start.png` | ⭐⭐ 可用 | `resources/img/receive_rewards/nameless_honor_start.png` |
| `ClaimAllRewards.png` | `receive_rewards/nameless_honor_reward_receive.png` | ⭐⭐ 可用 | `resources/img/receive_rewards/nameless_honor_reward_receive.png` |
| `MailButton.png` | `img/m.png` 或 `receive_rewards/claim_all_mail.png` | ⭐⭐ 可用 | `resources/img/receive_rewards/claim_all_mail.png` |
| `ClaimAllMail.png` | `receive_rewards/claim_all_mail.png` | ⭐⭐ 可用 | 同上 |

> **结论**: daily/ 几乎可以全部从 SRA 借，5/5！

---

## 五、dispatch/ — 委托派遣（4 张）

| 我们的文件名 | SRA 对应文件 | 匹配度 | 说明 |
|-------------|-------------|--------|------|
| `DispatchButton.png` | `receive_rewards/assignment_page.png` | ⭐ 可能 | 委托页面 |
| `ClaimDispatch.png` | `receive_rewards/assignments_reward.png` | ⭐⭐ 可用 | 领取已完成委托 |
| `DispatchSlot.png` | `receive_rewards/assignments_none.png` | ⭐ 可能 | 空槽位 |
| `ConfirmDispatch.png` | `receive_rewards/assign_again.png` 或 `automatic_placement.png` | ⭐ 可能 | 确认派遣 |

> **结论**: 4/4 可能可从 SRA 借。

---

## 六、weekly/ — 周常（2 张）

| 我们的文件名 | SRA 对应文件 | 匹配度 | 说明 |
|-------------|-------------|--------|------|
| `EchoOfWarButton.png` | `tp/echo_of_war.png` | ⭐⭐ 可用 | SRA 有 8 张历战余响变体 |
| `StartBattle.png` | `tp/battle.png` | ⭐ 可用 | 复用 combat |

> **结论**: 2/2 可从 SRA 借。

---

## 七、universe/ — 模拟宇宙（8 张） ⭐⭐⭐ SRA 最完整

| 我们的文件名 | SRA 对应文件 | 匹配度 | 下载链接 |
|-------------|-------------|--------|----------|
| `UniverseButton.png` | `img/cosmic_strife.png` | ⭐ 可能 | 模拟宇宙入口 |
| `EnterUniverse.png` | `divergent_universe/divergent_universe_start.png` | ⭐⭐ 可用 | `resources/img/divergent_universe/divergent_universe_start.png` |
| `NavigationArrow.png` | 无 | ❌ 需自截 | 走格子前进 |
| `BattleIcon.png` | `currency_wars/encounter_node.png` | ⭐ 可能 | 战斗节点 |
| `EventIcon.png` | 无 | ❌ 需自截 | 事件节点 |
| `ShopIcon.png` | 无 | ❌ 需自截 | 商店节点 |
| `MoneyWarButton.png` | `currency_wars/logo.png` 或 `img/survival_index.png` | ⭐⭐ 可用 | `resources/img/currency_wars/logo.png` |
| `StartMoneyWar.png` | `currency_wars/start_currency_wars.png` | ⭐⭐ 可用 | `resources/img/currency_wars/start_currency_wars.png` |

> **结论**: 4/8 可从 SRA 借。

---

## 📊 汇总

| 模块 | 总需 | 可从 SRA 借 | 需自截 | 借用率 |
|------|------|------------|--------|--------|
| common | 4 | 1 | 3 | 25% |
| login | 3 | 0 | 3 | 0% |
| combat | 8 | 4 | 4 | 50% |
| daily | 5 | 5 | 0 | **100%** ✅ |
| dispatch | 4 | 4 | 0 | **100%** ✅ |
| weekly | 2 | 2 | 0 | **100%** ✅ |
| universe | 8 | 4 | 4 | 50% |
| **合计** | **34** | **20** | **14** | **59%** |

> 🎉 **超过一半的图片可以直接用！自截工作量从 34 张降到 14 张。**

---

## 🛠 批量下载脚本

```bash
# 在 HonkaiStarRailAssistant 根目录执行

BASE="https://raw.githubusercontent.com/Shasnow/StarRailAssistant/main/resources/img"

# === daily/ (5张) ===
curl -sL "$BASE/receive_rewards/daily_reward.png" -o assets/resource/base/image/daily/DailyMissionsButton.png
curl -sL "$BASE/receive_rewards/nameless_honor_start.png" -o assets/resource/base/image/daily/NamelessHonorButton.png
curl -sL "$BASE/receive_rewards/nameless_honor_reward_receive.png" -o assets/resource/base/image/daily/ClaimAllRewards.png
curl -sL "$BASE/m.png" -o assets/resource/base/image/daily/MailButton.png
curl -sL "$BASE/receive_rewards/claim_all_mail.png" -o assets/resource/base/image/daily/ClaimAllMail.png

# === common/ (1张) ===
curl -sL "$BASE/quit.png" -o assets/resource/base/image/common/ExitButton.png

# === dispatch/ (4张) ===
curl -sL "$BASE/receive_rewards/assignment_page.png" -o assets/resource/base/image/dispatch/DispatchButton.png
curl -sL "$BASE/receive_rewards/assignments_reward.png" -o assets/resource/base/image/dispatch/ClaimDispatch.png
curl -sL "$BASE/receive_rewards/assignments_none.png" -o assets/resource/base/image/dispatch/DispatchSlot.png
curl -sL "$BASE/receive_rewards/automatic_placement.png" -o assets/resource/base/image/dispatch/ConfirmDispatch.png

# === weekly/ (2张) ===
curl -sL "$BASE/tp/echo_of_war.png" -o assets/resource/base/image/weekly/EchoOfWarButton.png
# StartBattle.png 从 combat 复制

# === combat/ (4张) ===
curl -sL "$BASE/tp/battle.png" -o assets/resource/base/image/combat/Battle.png
curl -sL "$BASE/tp/battle.png" -o assets/resource/base/image/combat/StartBattle.png
curl -sL "$BASE/tp/battle_star.png" -o assets/resource/base/image/combat/AutoBattle.png
curl -sL "$BASE/tp/caver_of_corrosion.png" -o assets/resource/base/image/combat/EquimentButton.png
# 也复制到 weekly 需要的地方
cp assets/resource/base/image/combat/StartBattle.png assets/resource/base/image/weekly/StartBattle.png

# === universe/ (4张) ===
curl -sL "$BASE/divergent_universe/divergent_universe_start.png" -o assets/resource/base/image/universe/EnterUniverse.png
curl -sL "$BASE/currency_wars/logo.png" -o assets/resource/base/image/universe/MoneyWarButton.png
curl -sL "$BASE/currency_wars/start_currency_wars.png" -o assets/resource/base/image/universe/StartMoneyWar.png
curl -sL "$BASE/currency_wars/encounter_node.png" -o assets/resource/base/image/universe/BattleIcon.png

echo "✅ 下载完成！"
```

---

## ⚠️ 注意事项

1. **分辨率适配**: SRA 也是 1920×1080，理论上直接兼容，但游戏版本更新可能导致按钮位置/样式变化
2. **MaaFramework 兼容性**: SRA 的图片可能包含更多边距，MaaFramework 的 TemplateMatch 可能需要更精确的裁剪
3. **测试验证**: 下载后务必用 MaaDebugger 或实际运行测试每张图的识别准确率
4. **授权**: SRA 使用 AGPL-3.0 许可证，使用其资源需遵守相同协议

---

## ❌ 仍需自截的 14 张

| 模块 | 文件 | 原因 |
|------|------|------|
| common | `CloseButton.png` | SRA 没有通用的干净关闭按钮 |
| common | `HomeButton.png` | 各游戏的主页按钮样式不同 |
| common | `Loading.png` | 需要截加载动画的一帧 |
| login | `LoginButton.png` | SRA 可能是程序化处理的登录 |
| login | `MissionButton.png` | 星穹列车主页的作战图标 |
| login | `TitleLoading.png` | 标题画面 |
| combat | `MissionButton.png` | 与 login 相同，共用 |
| combat | `IntoMissionButton.png` | 进入关卡按钮 |
| combat | `IntoMissionButton-White.png` | 灰色不可点击态 |
| combat | `BattlePause.png` | 战斗中暂停按钮 |
| universe | `UniverseButton.png` | 模拟宇宙入口 |
| universe | `NavigationArrow.png` | 走格子导航 |
| universe | `EventIcon.png` | 事件节点 |
| universe | `ShopIcon.png` | 商店节点 |

# 2026-10-25-low-temperature-spray-dryer-market-report

日期：2026-10-25｜检索截止：北京时间 08:34｜项目：低温喷雾干燥机每日行业情报
依据：本项目 AGENTS.md 与 config/keywords.json；关键词配置保持不变。

**当日判断：本次公开检索未核实到 10 月 25 日首发的 35°C 进风商业化突破、直接设备采购或冻干产能短缺公告。** 今日新增分析重点是雾化前物性、植物提取物货架稳定性、QS-21 供应链瓶颈的真实位置。以下注明发布日期与证据层级；没有新闻不等于没有市场需求，也不把抓取时间当新闻日期。

## 1. 全球市场动态（Global Market Dynamics）

### 🔵 药用喷雾：从入口温度转向雾化前质量控制
**已验证事实：** Droplet Lab 的 10 月 18 日供应商案例描述一家未具名 pharmaceutical CDMO 在内部测量配方表面张力，以支持喷雾液滴尺寸目标。[S1] 本次首次打开成功，进一步读取超时，后续以同站检索摘要复核；仅采用上述有限事实。
**来源推断：** 药用喷雾工艺开发会涉及配方物性与雾化耦合；未具名案例不能用于客户身份、产量或改善百分比判断。
**我方可切入机会：** 将黏度、表面张力、固含和雾化参数加入低温小试数据包；先确认液滴与最终干粉粒径的差异。

### 🔵 GLP-1 / peptide CDMO：服务能力是筛选信号，不是订单
**已验证事实：** Aurigene 的 CPHI Milan 2026 官方页面列出 peptide expertise、biologics 及药物开发服务；活动日期为 10 月 6—8 日。页面同时声明其能力数字需按项目确认。[S2]
**来源推断：** 多肽及蛋白工艺团队可作为技术评估入口，但该页面不证明某条 GLP-1 生产线存在冻干瓶颈。
**我方可切入机会：** 向药物原料工艺开发岗位准备“现有干燥步骤—质量损失—批次周期”诊断表，不将通用多肽能力写成已确认 GLP-1 客户。

### 🔵 疫苗佐剂：QS-21 瓶颈涉及原料与纯化
**已验证事实：** CPHI 官方 10 月 7 日议程介绍 Indena—Desert King 合作，议题包括 Quillaja 生物质供应、加工瓶颈及 GMP 提取/色谱纯化放大。[S3] Indena 2025 年 4 月官方材料称 QS-21 以最终冻干获得高纯产品。[S4]
**来源推断：** 这是全供应链问题；历史上使用冻干，不等于冻干本身是当前唯一限产环节。
**我方可切入机会：** 在既有质量要求下评估最终干燥对收率和稳定性的贡献。该工艺历史背景不作为 2026 年新采购公告，更不能直接建议替换已验证疫苗佐剂工艺。

### 🔵 生物制剂与食品原料：已有技术需求，证据成熟度不同
Lonza 10 月 1 日公告将 aseptic spray drying 推进到临床前平台开发及客户验证阶段，属于此前日报已覆盖的背景，今天没有核实到新的商业验证进展。[S5]
10 月 22 日植物提取物储存稳定性综述预印本强调包装内储存、吸湿和玻璃化转变；**该版本未经同行评审**，仅作为研发检查项来源。[S6]
本轮同时覆盖 enzymes、probiotics、functional food encapsulation、natural extracts、heat-sensitive new materials、energy saving 和 lab-to-market scale-up；未核实这些领域当天新增设备订单或直接相关监管变更。

## 2. 研发工艺匹配报告（R&D & Process Alignment Report）

### 🔴 35°C 进风的证明链
“35C inlet low-temperature spray dryer”应同时给出实际 Tin、Tout、入口露点、腔体绝压、风量、进料固含与稳态蒸发量。低温入口并不自动证明 activity retention、低水活度、无菌性、节能或全面替代 lyophilization / freeze drying。必须核实设备在目标负荷下能否持续成粉，而非只有空载温度。

今日新增建议字段：FeedViscosity_mPa_s、SurfaceTension_mN_m、MeasurementTemp_C、AtomizationSetting、DropletD50_um。液滴 D50 与干粉 D50 分开记录；物性测量需注明温度与方法。字段是试验表建议，本次没有连接设备或修改 PLC 标签。

### 🔴 最小案例：先验雾化与成粉，再比较活性
选择一款成分明确、可获得分析方法的非无菌酶制剂，同一原液设置原液基线、当前冻干基准、35°C 进风喷雾，必要时增加现行常规喷雾对照。建议每个干燥条件至少三次独立批次；预先按用途定义验收指标，不设虚构通用阈值。
先用无活性模拟液确认进料物性、稳定雾化、收粉与物料衡算，再进行真实物料对照。若低温样品必须二次干燥，则将后处理并入总周期、能耗与活性回收率。

| 物料 | 必测质量与稳定性 | 特别关注 |
|---|---|---|
| GLP-1 / peptides | 活性保留率、含水率、水活度、粒径分布、复溶性、结构稳定性；HPLC/LC-MS 化学稳定性 | 分子、盐型、辅料和溶剂逐项确认，不能以含量代替效价 |
| biologics / proteins | 上述六类指标，加 SEC 聚集、亚可见颗粒和构象/效价 | 区分雾化界面、脱水与热损伤；注射用途另验无菌及内毒素 |
| 酶制剂 | 活性保留率、含水率、水活度、粒径、复溶性、结构稳定性 | U/g 干基及总活性回收同时报告，加入储存后活性 |
| 益生菌 | 活菌保留率、含水率、水活度、粒径、复水性、细胞结构/膜完整性 | CFU/g 干基及总活菌回收；菌株、壁材、包装与货架期绑定 |
| 天然提取物 / 功能食品 | 标志物、氧化/香气、粒径、含水与水活度、分散性、吸湿结块 | 成粉包埋率不等于货架期；参考预印本提出的储存验证方向，不视为法规要求 [S6] |
| PHA / 热敏新材料 | 粒径与团聚、再分散、残溶/水分、分子量或目标材料性能 | CÉPROCQ 列有 PHA 干燥放大应用；不证明 35°C 工艺已验证 [S7] |

### 🔴 放大与节能必须统一比较边界
保留 Tin_C、Tout_C、InletDewPoint_C、ChamberPressure_kPaAbs、ResidenceTime_s、FeedSolids_wtPct、Evaporation_kg_h、ResidualMoisture_wtPct、WaterActivity、D10_um、D50_um、D90_um、ActivityRetention_pct、PowderRecovery_pct、Reconstitution_s。
活性回收按“合格收集粉中的总活性 / 原始投料总活性”计算，同时单列干燥后比活性和储存保留；避免高比活性掩盖挂壁损失。
energy saving 对照必须统计加热、制冷/除湿再生、真空、压缩空气、风机、辅助干燥、启停与清洗，报告 kWh/kg 蒸发水及 kWh/kg 合格粉。continuous production 的价值需用连续稳态时长、合格率、清洗停机和换批损失验证。

## 3. 市场与前景评估报告（Market & Outlook Report）

**已验证事实：** 存在多肽/生物制剂服务平台、无菌喷雾开发项目及食品/生物基中试应用。[S2][S5][S7] 本次没有获得足以计算 35°C 细分市场规模、替代比例、客户预算或采购期限的数据。

**来源推断：** pharmaceutical spray drying 的 ASD/SDD、无菌生物制剂、非无菌食品和材料干燥应分开评估。温度标签不足以构成竞争优势，合格粉收率、储存稳定性和放大一致性更接近客户验收目标。

**我方可切入机会与优先级（顾问判断）：**
1. 优先以非无菌酶、天然提取物或功能食品开展可付费对照小试，形成质量与能耗数据包。
2. 益生菌把菌株存活和货架期放在单次成粉之前；合格后再讨论连续放大。
3. peptide CDMO 与 biologics 先做联合可行性评估；无菌及注册变更成本使其更适合中长期协作。
4. 新材料作为第二验证方向；需要客户提供分子量、再分散或催化性能目标，不能由食品活性结果外推。

QS-21 案例尤其提醒：先识别限产单元，再决定是否改干燥。不得将供应链紧张直接转译成“冻干替代设备有订单”。

## 4. 每日精准潜在客户画像（Potential Customers & Leads）

以下均为公开资料筛选的线索，尚未联系；没有已确认采购意向。优先级按验证可行性，不代表成交概率。

| 潜在线索 | 已知依据与匹配方向 | 建议对接岗位与首个问题 | 状态 |
|---|---|---|---|
| 🟢 CÉPROCQ，加拿大 | 官方中试页覆盖蛋白、树皮提取物及 PHA；可作为工艺对照合作方 [S7] | R&D / 技术服务：能否提供同批次常规喷雾与低温方案的质量、能耗对照？ | 优先验证；已知有设备，不推定需采购 |
| 🟢 Aurigene Pharmaceutical Services，印度及国际业务 | 官方列出 peptides 和 biologics 服务 [S2] | Drug Substance Process Development：目标项目当前干燥步骤及损失点是什么？ | 多肽合作线索；GLP-1 具体需求未确认 |
| 🟢 Indena / Desert King，意大利与国际原料链 | QS-21 提取纯化放大合作、历史最终冻干工艺 [S3][S4] | 工艺研发 / 分析开发：瓶颈究竟在原料、纯化还是最终干燥？ | 长期技术评估；不建议直接替换注册工艺 |
| 🟢 Lonza，美国 Bend / 全球 | 无菌喷雾临床前平台公告 [S5] | Particle Engineering / Formulation Development：是否存在非竞争性材料筛选或测试合作？ | 既有平台方兼潜在竞合对象；非新增订单 |

CÉPROCQ 页面所列最大蒸发量随进出风条件变化，不能作为 35°C 产能参照。未具名 CDMO 案例不列为可直接联系客户。

## 5. 当日行动建议（Action Items）

1. **研发优先：** 为一个可获得样品的酶或植物提取物建立小试表，补充黏度、表面张力、测量温度和液滴/干粉粒径双记录；先过模拟液闭环。
2. **市场优先：** 按上表准备资格筛选问题，收集具体物料、用途、批量、现工艺及质量门槛；本任务不代发邮件或联系客户。
3. **资料门槛：** 35°C 宣传必须附真实入口测点、蒸发负荷、连续时长和质量结果。销售材料采用“有条件的替代候选”，不使用“完美替代所有冻干”。
4. **储存验证：** 植物提取物、益生菌和酶都增加实际包装中的稳定性考察；试验条件由用途与目标市场确认，不直接套用预印本条件为统一标准。
5. **下次检索：** 优先找 10 月 25 日之后新增官方公告、具体客户工艺需求和同行评审数据；今日旧公告不再作为明日新闻重复计数。

本日已完成公开资料研究和报告编制；未执行实际试验、设备控制、客户沟通或采购承诺。

## 6. 来源链接（Sources）

- [S1 Droplet Lab：Pharma CDMO surface tension case](https://dropletlab.com/validation/case-studies/pharmaceutical-cdmo-spray-drying-surface-tension/) — 2026-10-18；供应商未具名案例，初次打开及检索摘要，详细读取超时；不采用性能数字。
- [S2 Aurigene：CPHI Milan 2026](https://www.aurigeneservices.com/cphi-milan-2026) — 官方能力/活动页，活动 2026-10-06—08；能力按项目确认，非当日扩产公告。
- [S3 CPHI：Overcoming QS-21 Supply Constraints](https://visitor.cphieventplanner.com/widget/event/cphi-milan-2026/planning/UGxhbm5pbmdfNDQzNjMwNA==) — 官方 2026-10-07 议程摘要；证明议题和合作陈述，不证明会后所有成果已兑现。
- [S4 Indena：CPHI Japan 2025 官方新闻稿](https://www.indena.com/indena_files/2025/04/Press-release-Indena%40CPHI-Japan-2025.pdf) — 2025 年历史工艺依据；本次检索读取官方 PDF 摘要。
- [S5 Lonza：Preclinical aseptic spray drying](https://www.lonza.com/media-advisories/2026-10-01-14-00) — 2026-10-01 官方公告；历史背景，非今日新增。
- [S6 Botanical extract storage stability preprint v1](https://www.preprints.org/manuscript/202610.2265) — 2026-10-22；作者预印本，未同行评审，仅作研究检查项。
- [S7 CÉPROCQ：Pilot-Scale Spray Dryer](https://ceprocq.com/en/equipements/pilot-scale-spray-dryer/) — 2026-10-02 官方设备页；食品、生物基及 PHA 中试方向，非 35°C 验证。

检索边界：公开网页可访问性与搜索索引存在限制；未核实到不代表不存在。供应商陈述、预印本、会议议程与我方推断分别标识；没有采用二手市场规模预测或无依据节能百分比。

— 报告结束 —

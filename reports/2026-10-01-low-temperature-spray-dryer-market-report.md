# 2026-10-01-low-temperature-spray-dryer-market-report

低温喷雾干燥机行业情报日报｜市场部与研发部

数据截止：2026-10-01 08:36（Asia/Shanghai）。依据本项目 AGENTS.md 与 config/keywords.json；关键词完整，未修改配置。已对照 9 月 30 日报告并检索历史报告去重。公开检索不代表覆盖全天或穷尽全球信息；“今日新增纳入”不等于“今日发布”。

**今日判断：** 药用喷干商业化投资继续推进，但未核实到 10 月 1 日新发布的 35℃进风商业验证或采购公告。今日新增重点是 Serán 9 月 29 日融资扩产公告，以及同日发表的益生菌包埋研究。应把“特定物料的合格粉产出、活性与稳定性”作为价值证明，不能宣称普适或完美替代冻干。

## 1. 全球市场动态 (Global Market Dynamics)

### 🔵 美国：Serán 新投资支持喷干商业化扩张

**已验证事实：** Serán 官网原公告日期为 2026-09-29，Biospring Partners 领投，既有投资者继续参与。新商业设施预计 2027 年第三季度完成，将支持 OEB4 制造及喷干、纳米研磨等粒子工程能力。金额未在该公告披露。9 月 30 日媒体转载不是第二次融资。[S1](https://www.seranbio.com/news/seran-bioscience-strengthens-spray-dry-capabilities-with-growth-investment-from-biospring-partners-to-accelerate-commercial-expansion-and-meet-surging-customer-demand)

**来源推断：** pharmaceutical spray drying CDMO 正在强化从开发到商业供应的完整服务。**我方可切入机会：** 研究已有平台尚未覆盖的热敏水系工况；不能由融资推导出我方设备采购或冻干全面退出。

其现有生物药技术页列有 peptides、proteins、RNA/LNP 等开发方向及 50 mg—20 kg 喷干规模，属于企业能力陈述，未给出 35℃进风验证；该范围不是 kg/h 处理量。[S2](https://www.seranbio.com/solutions/biologics-spray-drying)

### 🔵 巴西：益生菌与天然副产物包埋出现新研究

**已验证事实：** 9 月 29 日论文研究海藻酸盐与葡萄渣粉保护 Lacticaseibacillus rhamnosus GG；采用滴入钙盐溶液的离子凝胶路线，评价冷藏和食品体系中的存活。[S4](https://link.springer.com/article/10.1007/s12602-026-11228-y)

**来源推断：** functional food encapsulation 的竞争需要同时解决配方保护与使用场景。**我方可切入机会：** 探索可雾化配方的干粉化合作，但这篇研究不是喷干或冻干对照。原文以 log CFU 数值之比计算包埋效率，不能直接当作按实际菌数计算的存活率；本报告不将其百分比列为设备性能基准。

### 🔵 欧洲：无菌与冻干扩建仍需独立看待

**已验证事实，历史背景：** CordenPharma 9 月 10 日公告披露 Caponago 多年期无菌制剂扩张，规划空间包含大规模冻干选项。[S5](https://cordenpharma.com/articles/press-release-cordenpharma-boosts-aseptic-fill-finish-capacity-to-500-million-sterile-injectable-units-per-year/)

**来源推断：** 客户同时投资多种制剂路线；扩产本身不足以证明冻干是项目唯一瓶颈。**我方可切入机会：** 先拆分原液准备、干燥、收粉、无菌转移和灌装周期，确认瓶颈位置，再讨论 lyophilization / freeze drying 替代。

### 🔵 去重、缺口与近期交流窗口

- Serán 官方列出 CPHI Milan 10 月 6—8 日、展位 10.K.40，可作为市场团队技术交流窗口，尚未报名或预约。[S3](https://www.seranbio.com/news/cphi-milan)
- Piramal Turbhe 喷干套间原始公告为 8 月 4 日，9 月转载不计新增；项目历史日报已覆盖。[S6](https://www.piramalpharmasolutions.com/news/press-releases)
- 印加果油—草本乳液研究已在 9 月日报覆盖；140℃进风条件下粉体回收数据不是 35℃验证，也不是活性保留率。[S7](https://onlinelibrary.wiley.com/doi/10.1002/appl.70190)
- GLP-1、peptide CDMO、酶制剂、天然提取物、疫苗/mRNA、热敏新材料、节能及中试放大均纳入关键词检索。本轮未核实这些领域当日新增的 35℃设备 RFQ、成交、量产验收或直接适用的新监管政策。没有据此推断全球没有相关事件。

## 2. 研发工艺匹配报告 (R&D & Process Alignment Report)

### 🔴 工况定义与关键词驱动

核心设备：**35C inlet low-temperature spray dryer**。35℃是指定测点的进风温度，不是产品温度、出风温度或生物活性保证。下列字段作为建议的小试记录变量，尚未写入真实设备或控制系统：

- 工况：inlet_temperature、outlet_temperature、inlet_dew_point、absolute_pressure、dry_air_flow、feed_rate、feed_solids、atomization_setting、residence_time。
- 质量：residual_moisture、water_activity、particle_size_distribution、activity_retention_rate、reconstitution_behavior。
- 专项：peptide_chemical_stability、protein_aggregation、probiotic_viability。
- 经济性：qualified_powder_yield、total_activity_recovery、kWh_per_kg_water、kWh_per_kg_qualified_powder、full_cycle_time。

每条记录绑定 sample_id、batch_id、method_id、单位及测点；原料、工况、检测结果必须可追溯。35℃下能否达到残水和水活度目标取决于传热传质、气体湿度、压力及负荷，不能仅凭温度判定可行。

### 🔴 按物料定义小试，不用一个指标代替全部质量

以下为我方工程建议，不是本轮实验结果。

- **GLP-1 / 多肽：** 必测活性保留率、含水率、水活度、粒径、复溶性、结构稳定性；补充化学稳定性、杂质、盐型及残留溶剂。HPLC 纯度不单独代表药理活性。
- **Biologics / proteins：** 同样六项必测；增加可溶/不可溶聚集、构象及功能检测。喷干可行性与 aseptic spray drying 的整链无菌保障分别验证。
- **酶制剂：** 同样六项必测；同时报告单位干物质酶活、全批次总酶活回收和粉体收率，区分失活与收粉损失。
- **益生菌：** 同样六项必测；活性用菌株适配的活菌计数，结构用膜完整性等方法，复溶用复水恢复评价。总 CFU 回收按线性菌数及整批质量/体积核算；不能将 log 数值比作为实际活菌回收。
- **功能食品 / 天然提取物：** 除质量六项的适配测定外，评价标志成分、氧化、风味、壁材稀释和货架期；化学抗氧化检测不能外推人体功效。
- **热敏新材料：** 验证初级粒子、干粉团聚与再分散粒径、结构及目标功能；纳米研磨、喷干造粒和纳米粒子形成应分别描述。有机溶剂体系需另行确认密闭、惰化与回收能力。

### 🔴 最小验证及通过条件

1. **先验证水/载体：** 在声明的 35℃、露点、压力和气量下测净蒸发量、沉积及固体衡算，确认可达到拟定终点。
2. **再验证单一酶：** 同批物料设未处理、仅雾化、现行冻干、35℃喷干四组；建议至少三次独立重复。六项质量指标加总活性回收同时比较。
3. **益生菌另设配方门槛：** 先评价黏度、悬浮稳定性与雾化适应性，不将已交联湿凝胶直接视为可泵送喷干进料；增加配方空白和包装储存对照。
4. **能耗边界完整：** 除湿再生、冷却、风机、真空、压缩空气、加热、后干燥与清洁均计入；比较相同质量要求下 kWh/kg 蒸发水与 kWh/kg 合格粉。
5. **放大门槛：** 达成客户预设的六项质量与储存指标后，再扩展连续运行、收粉、沉积、清洁和批间一致性。activity retention、continuous production、lab-to-market scale-up、energy saving、shorter cycle time 均为待验证目标，不预设改善百分比。

## 3. 市场与前景评估报告 (Market & Outlook Report)

🔵 **已验证事实：** 新融资支持商业喷干建设，既有生物药开发平台具有粒子工程能力，无菌制剂企业也继续规划冻干选项；三者属于不同业务边界。[S1](https://www.seranbio.com/news/seran-bioscience-strengthens-spray-dry-capabilities-with-growth-investment-from-biospring-partners-to-accelerate-commercial-expansion-and-meet-surging-customer-demand) [S2](https://www.seranbio.com/solutions/biologics-spray-drying) [S5](https://cordenpharma.com/articles/press-release-cordenpharma-boosts-aseptic-fill-finish-capacity-to-500-million-sterile-injectable-units-per-year/)

🔴 **来源推断：** “已有喷干市场”不等于“35℃设备需求已成立”。对现有 CDMO，切入点需证明新增物料窗口、质量或成本优势；spray-dried dispersion 的小分子生物利用度业务不能直接等同于水系蛋白脱水。

🟢 **我方可切入机会：** 近期优先形成酶或食品原料的可比小试包；中期以热敏水系样品进入 CDMO 工艺评估；无菌注射用蛋白及 GLP-1 大规模替换属于验证周期较长的机会。客户排序依据技术关联度，不代表购买概率。

不引用缺乏口径一致性的一揽子市场规模、CAGR、冻干排队周期或节能率。当前证据不足以量化市场替代份额，也未确认我方相关采购预算或订单。

## 4. 每日精准潜在客户画像 (Potential Customers & Leads)

### 🟢 Serán Bioscience｜美国 Bend｜P1 技术资格确认

- 状态：既有技术对标对象，今日新增融资扩产事件；不是首次识别公司。
- 目标角色：Process Engineering、Biologics Formulation、Technology Evaluation。
- 需求假设：现有平台之外的热敏水系干燥或更高合格粉回收；需由对方确认。
- 入口：官网合作渠道；CPHI 交流信息见 S3。
- 首问：现有进风/出风/压力窗口有哪些未满足的物料？能否在相同质量标准下提供对照样品？
- 升级条件：获得明确痛点、样品许可和试验指标。公开融资与完工时间不代表设备采购窗口。

### 🟢 UTFPR Londrina / Universidade Estadual de Londrina｜巴西｜P2 新增科研合作线索

- 依据：S4 的食品技术与微生物研究团队；Luciana Furlaneto Maia 等参与。
- 匹配：益生菌与植物副产物保护体系，适合讨论干粉化及配方可雾化性。
- 首问：是否计划干燥？现有湿凝胶体系能否转为适合雾化的配方？能否提供线性 CFU 原始数据？
- 边界：论文未证明喷干适配，也未披露购机预算；合作建议为我方推断。

### 🟢 Piramal Pharma Solutions / Turbhe｜印度｜P2 既有线索维护

- 依据：S6 已有 peptide API 喷干扩建，非当日新增。
- 目标角色：Peptide Process Development、Particle Engineering。
- 首问：现有设备是否有低温水系、收率或清洁换批缺口？若无明确缺口，不推进重复设备报价。
- 边界：仅为工艺合作候选，未核实采购计划。

本轮未发送邮件、预约会议、申请样品或联系任何客户。优先级为内部分析排序。

## 5. 当日行动建议 (Action Items)

1. **市场 P1：** 为 Serán 准备一页技术资格问题与小试能力清单，围绕未覆盖的工况和可测质量价值；如团队原有参展安排，可利用 10 月 6—8 日窗口。
2. **研发 P1：** 建立上述 sample_id—工况—检测关联表，先水/载体验证，再进行单酶四组对照。
3. **食品 P1：** 将 S4 放入“包埋配方参考”而非“喷干成功案例”；核对线性 CFU 与全批次回收，避免以 log 比值形成营销数字。
4. **市场 P2：** 客户访谈拆分冻干全流程瓶颈；未取得真实排产、周期和质量数据前不声称客户受制于冻干产能。
5. **情报 P2：** 后续只在 Serán 建设状态、具体技术数据或采购线索变化时升级；Piramal 和已覆盖食品论文继续去重。
6. **归档：** 本地 Markdown → Notion infomation 同名子页面 → fetch 检查祖先及正文 → GitHub main。同步结果以本次回执为准。

## 6. 来源链接 (Sources)

- **S1｜Serán 原始企业公告｜2026-09-29：** [Growth investment and commercial expansion](https://www.seranbio.com/news/seran-bioscience-strengthens-spray-dry-capabilities-with-growth-investment-from-biospring-partners-to-accelerate-commercial-expansion-and-meet-surging-customer-demand)。已读官网正文；完工为计划，非投运结果。
- **S2｜Serán 官方能力页｜未注明发布日期：** [Spray Drying of Biologics](https://www.seranbio.com/solutions/biologics-spray-drying)。已读；能力陈述不是独立性能验证。
- **S3｜Serán 官方活动页｜活动 2026-10-06—08：** [CPHI Milan](https://www.seranbio.com/news/cphi-milan)。已读日期和展位；不代表已经预约。
- **S4｜原始研究｜2026-09-29：** [Alginate–Grape Pomace Flour Microcapsules](https://link.springer.com/article/10.1007/s12602-026-11228-y)。DOI 10.1007/s12602-026-11228-y；已读方法及机构，离子凝胶路线，不能外推喷干性能。
- **S5｜CordenPharma 企业公告｜2026-09-10：** [Aseptic fill-finish capacity expansion](https://cordenpharma.com/articles/press-release-cordenpharma-boosts-aseptic-fill-finish-capacity-to-500-million-sterile-injectable-units-per-year/)。历史背景，规划选项不等于已建冻干线。
- **S6｜Piramal 官方新闻目录｜相关公告 2026-08-04：** [Press releases](https://www.piramalpharmasolutions.com/news/press-releases)。本轮用于确认原始日期；不将转载日期作为新事件。
- **S7｜Applied Research 原始研究｜2026-09-07：** [Oil–herbal extract spray-drying study](https://onlinelibrary.wiley.com/doi/10.1002/appl.70190)。已读出版商正文，历史去重；其工况不等于 35℃工况。

报告边界：未开展实验或客户接洽；未证明 35℃进风普适替代冻干，未验证节能比例，未确认采购订单。

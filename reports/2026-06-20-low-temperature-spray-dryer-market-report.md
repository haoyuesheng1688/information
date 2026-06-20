# 2026-06-20 低温喷雾干燥机行业情报日报

1. 执行摘要
- 🔵 Novo Nordisk 于 2026-06-17 宣布在捷克启用新工厂生产“下一代糖尿病与肥胖症药物的支持性蛋白”，并追加在天津注射笔产能投资，显示GLP-1上下游产能仍在扩张，短期供应与放量并存。([fiercepharma.com](https://www.fiercepharma.com/manufacturing/novo-nordisk-opens-czech-plant-unveils-29m-upgrade-china-facility))
- 🔵 EMA 近期更新 Wegovy（司美格鲁肽）标签，允许在受控条件下于30°C内保存48小时，反映监管端对冷链风险的“合理放宽”，或间接推升对室温稳定干粉/固体制剂工艺的兴趣。([fiercepharma.com](https://www.fiercepharma.com/pharma/fierce-pharma-regulatory-tracker-2026?utm_source=openai))
- 🔵 Catalent 于 2026-06-17 发布企业级AI质量管理工具（Qai），显示头部CDMO在GxP质量体系与数据治理加速上云与智能化，利于新工艺（含连续/低温喷雾）更快通过验证与放行。([pharmamanufacturing.com](https://www.pharmamanufacturing.com/industry-news/news/55384900/catalent-launches-enterprise-ai-tool-to-strengthen-quality-management-systems?utm_source=openai))
- 🔴 最新计算流体与相变研究提示：两流体雾化近喷嘴区可出现“闪速降温到-130°C以下并快速冻融”，对热敏活性物（肽、蛋白、益生菌）构成潜在冻融/剪切复合损伤；低温进风与低露点工况更需关注喷嘴区气体温度与GLR控制。([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))
- 🔵 近一周会展与活动动向：BIO 2026 将于下周在圣迭戈设立BPI Theater聚焦“全球供应链与CDMO产能”；微生态国际大会IPC 2026 将于下周在克拉科夫召开，益生菌/后生元稳定化与干粉化为热点。([bioprocessintl.com](https://www.bioprocessintl.com/events/bioprocess-international-theater-bio-2026?utm_source=openai))

2. 全球市场动态 (Global Market Dynamics)
- 🔵 GLP‑1产业链
  - Novo Nordisk 捷克新厂投产“支持性蛋白”，并在中国天津追加2,900万美元注射笔产能升级，表明对中长期放量的信心。［已验证事实］([fiercepharma.com](https://www.fiercepharma.com/manufacturing/novo-nordisk-opens-czech-plant-unveils-29m-upgrade-china-facility))
  - EMA 对 Wegovy 的短时常温存放（≤30°C、≤48h）标签更新，显示监管对实际用药场景的适配性增强，利好下游配送与患者依从性。［已验证事实，趋势判断属来源推断］([fiercepharma.com](https://www.fiercepharma.com/pharma/fierce-pharma-regulatory-tracker-2026?utm_source=openai))
- 🔵 CDMO与质量数字化
  - Catalent 推出企业级AI质量管理工具Qai，聚焦偏差/变更/培训闭环与数据完整性，或缩短新工艺技术转移与放行时间。［已验证事实；对工艺验证周期缩短为来源推断］([pharmamanufacturing.com](https://www.pharmamanufacturing.com/industry-news/news/55384900/catalent-launches-enterprise-ai-tool-to-strengthen-quality-management-systems?utm_source=openai))
- 🔵 事件/会议
  - BPI Theater @ BIO 2026（6/23–24）议题包含“全球供应链与CDMO产能、病毒安全”等；IPC 2026（6/22–24）将聚焦益生菌/后生元最新稳定化路径与法规更新。［已验证事实］([bioprocessintl.com](https://www.bioprocessintl.com/events/bioprocess-international-theater-bio-2026?utm_source=openai))
- 🔴 工艺痛点信号
  - 计算与实验研究揭示两流体喷嘴在雾化区因气体绝热膨胀出现瞬时极低温并导致微滴快速冻结—解冻循环，这一“近喷嘴区隐性冻融应力”或为低温喷雾干燥导致活性丧失的关键机制之一。［已验证事实；对生物活性影响为工程推断］([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))
- 🔵 监管与政策碎片
  -（背景补充）FDA与各国监管对复方、标签与质量系统的持续更新，强化对声称与稳定性的核查，为干粉/低温喷雾路线的CMC与稳定性设计提出更细要求。［来源综合判断；实例见近月FDA与EMA多项通告］([fiercepharma.com](https://www.fiercepharma.com/pharma/fierce-pharma-regulatory-tracker-2026?utm_source=openai))

3. 研发工艺匹配报告 (R&D & Process Alignment Report)
- 适配性边界声明
  - 我们不泛化宣称“35°C进风低温喷雾干燥适用于所有物料”。对强亲水蛋白/多肽、含高盐缓冲、悬浮纳米颗粒（如mRNA‑LNP）与活菌，需要逐级小试验证，重点验证近喷嘴区温度—剪切—冻融协同应力与二次干燥/析晶风险。［工程原则，结合最新研究］([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))
- 工艺—物料维度的关键匹配（示例指标为可验证小试KPI—建议在3–10批DoE内获取）
  - GLP‑1/多肽（注：多为固相合成产物，主杂为去酰胺/异构化/氧化）
    - 小试配方与工艺KPI（目标范围为工艺可达建议，不代表法规规格）：
      - 出口温度：≤40–45°C；总停留时间：≤2–5 s；残余水分：1.5–3.0%（KF）；水活度aw：≤0.25；粒径D50：依用途选型（口服分散/包埋：50–150 μm；吸入：1–5 μm需二次分级）；主峰纯度变化Δ≤1.0%（HPLC）；关键降解（去酰胺/异构化/氧化）≤0.3%；重溶时间≤60 s。［来源推断+行业通行KPI建议；需小试实证］
      - 重点工艺控制：雾化气预热/露点控制，GLR≤12或雾化气≥110°C以避免近喷嘴冻结（若材料耐受），并引入封端/抗氧策略与中性/微酸pH以抑制化学降解。［工程推断，机理依据］([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))
  - 蛋白/生物大分子（如mAb悬浮、可溶性酶）
    - KPI：单体含量≥95%（SEC）；可溶性聚集体≤2%（DLS/SEC）；比活保持率≥80–90%（对酶制剂）；残余水分1–2%；aw≤0.20；重溶≤90 s；喷干悬浮体系的固含与玻璃化助剂（海藻糖/甘露醇/亮氨酸）优化以获得可重分散“湿化悬浮”。［背景综述与最新观点支持喷干蛋白悬浮作为高浓度皮下给药替代策略］([link.springer.com](https://link.springer.com/article/10.1186/s41120-026-00160-8?utm_source=openai))
    - 风险提示：开放式喷干的无菌保障复杂，注射用制剂多仍以（无菌）冻干为主；可考虑无菌喷干或作为中间体/口鼻用干粉。［事实+评论］([bioprocessintl.com](https://www.bioprocessintl.com/sponsored-content/dry-to-die-freezing-can-replace-spray-drying-for-bulk-intermediates?utm_source=openai))
  - 酶制剂与吸入用干粉
    - 案例参考：重组人脱氧核糖核酸酶（Dornase alfa）干粉吸入研究验证喷干可行性。KPI：酶活保持≥85%；气动粒径FPF<5 μm ≥60–70%；D50≈1–3 μm；水分≤3%。［已验证事实+可操作KPI建议］([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/41679558/?utm_source=openai))
  - 益生菌/益生元/功能食品
    - 最新文献与综述支持通过壁材与参数优化提高喷干生存率与贮藏稳定性；但非芽孢菌对热/渗透/氧化极为敏感。KPI：即刻存活率≥50–70%（视菌株）；制品≥1×10^9 CFU/份；加速条件（40°C/75%RH, 7天）降幅≤0.5 log；水分≤4%；aw≤0.25；胃肠道体外消化后≥6 log CFU/g。［已验证事实+KPI建议］([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0963996925024524?utm_source=openai))
  - mRNA‑LNP/疫苗干粉（研发探索阶段）
    - 文献显示喷雾/喷雾冻干均可得到可吸入或口服干粉，但需酸性/赋形协同稳定与纳米结构保护。KPI：转染效能相对液体对照≥80%；RNA 完整性保持；粒径/多分散性维持；aw≤0.20；室温稳定性目标≥3–6个月（应以加速数据外推）。［已验证事实+研发KPI建议］([doi.org](https://doi.org/10.1186/s41120-026-00146-6?utm_source=openai))
- 工程化要点与“红色痛点”
  - 🔴 近喷嘴区“瞬时冰冻—解冻”与高剪切并存：需通过雾化气温度、GLR、喷帽结构（旋流/非旋流）与露点治理协同优化，必要时改用压力喷嘴/超声/FEA等替代雾化方式，或采用SFD/真空喷雾混合路线。［工程对策，机理支撑］([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))

4. 市场与前景评估报告 (Market & Outlook Report)
- GLP‑1放量与常温化趋势
  - 🔵 产能：Novo捷克与中国线的扩建与改造，配合美国口服司美格鲁肽放量，短中期将带来“更多原料与辅料/器械配套需求”。［事实+推断］([fiercepharma.com](https://www.fiercepharma.com/manufacturing/novo-nordisk-opens-czech-plant-unveils-29m-upgrade-china-facility))
  - 🔵 冷链与依从性：EMA 对 Wegovy 的短时常温标签更新，预计促进“室温稳定”理念渗透，也将提升对“低温喷雾/喷雾冻干/后生元”等热稳态产品的关注。［事实+推断］([fiercepharma.com](https://www.fiercepharma.com/pharma/fierce-pharma-regulatory-tracker-2026?utm_source=openai))
- 质量与数字化
  - 🔵 AI‑QMS 正在成为头部CDMO竞争点，潜在缩短验证与放行，利于连续/低温喷雾等新工艺的合规落地。［事实+推断］([pharmamanufacturing.com](https://www.pharmamanufacturing.com/industry-news/news/55384900/catalent-launches-enterprise-ai-tool-to-strengthen-quality-management-systems?utm_source=openai))
- 工艺路线竞争
  - 🔴 注射用生物制品仍以（无菌）冻干为主流；但口鼻吸入、口服分散、益生菌/酶制剂等场景对“低温连续喷干+配方玻璃化”需求明确。［综述与行业评论］([bioprocessintl.com](https://www.bioprocessintl.com/sponsored-content/dry-to-die-freezing-can-replace-spray-drying-for-bulk-intermediates?utm_source=openai))
- 总体判断（来源推断）
  - 未来6–18个月，“冻干+（低温）喷雾/喷雾冻干”的分工将更清晰：注射用/无菌高风险→冻干；非无菌或鼻/吸入/口服固体→喷雾/喷雾冻干/后生元。对“35°C进风级”的设备，定位在“活性敏感、允许适度水分、追求连续效率”的场景，并以可验证KPI驱动落地。

5. 每日精准潜在客户画像 (Potential Customers & Leads)
- 🟢 Novo Nordisk（捷克“支持性蛋白”新厂；天津注射笔升级）
  - 画像：全球GLP‑1龙头，非CDMO但在蛋白与给药装置端扩产；对稳定性与供应链韧性高度敏感。
  - 需求猜测：对固体/干粉中间体（非无菌）与鼻腔/口服新剂型的探索与加速评估窗口。［来源推断］([fiercepharma.com](https://www.fiercepharma.com/manufacturing/novo-nordisk-opens-czech-plant-unveils-29m-upgrade-china-facility))
- 🟢 CordenPharma（收购AmbioPharm后美国/中国双基地肽API网络）
  - 画像：GLP‑1肽API主力，纵深布局产能与区域多元化。
  - 需求猜测：对口服/经皮等“固体化稳定策略”的联合开发与放大服务；可能需要低温喷雾中试验证与质量研究支持。［来源推断］([outsourcedpharma.com](https://www.outsourcedpharma.com/doc/cordenpharma-acquires-ambiopharm-to-expand-global-peptide-api-capacity-0001?utm_source=openai))
- 🟢 Asymchem（TJ4 TIDES一体化矩阵）
  - 画像：TIDES（肽/寡核苷酸）从API到制剂一体化，强调工艺放大与商用化。
  - 需求猜测：固体分散/包埋与低温喷雾在口服肽制剂中的可行性验证与设备选型。［来源推断］([prnewswire.com](https://www.prnewswire.com/news-releases/asymchem-unveils-its-fully-integrated-tides-commercial-supply-matrix--supporting-partners-from-molecule-to-market-302741446.html?utm_source=openai))
- 🟢 Symeres（新泽西扩展喷雾干燥能力）
  - 画像：CRDMO侧重早期与难溶小分子，但已布局喷雾干燥平台。
  - 需求猜测：对“低温进风/短停留时间”的验证与客户示范批需求。［来源推断］([genengnews.com](https://www.genengnews.com/topics/bioprocessing/symeres-expands-spray-drying-capabilities-at-its-us-new-jersey-site/?utm_source=openai))
- 🟢 益生菌/功能食品平台（如 Probi、Vitaquest）
  - 画像：从活菌到后生元的产品矩阵扩展，强调常温稳定与配方兼容。
  - 需求猜测：针对活菌与后生元的“低温喷雾微囊+加速稳定”方案与批量化工艺包。［来源推断］([probi.com](https://www.probi.com/press-releases/2026/probi-enters-the-fast-growing-postbiotic-market-with-rham271h-launch-at-vitafoods-europe/?utm_source=openai))

6. 当日行动建议
- 针对“红色痛点”立即开展喷嘴区热力学实测与建模：配置可加热雾化气与露点控制模块，DoE考察GLR、雾化气温度（含>110°C情形）与进风35–60°C组合，对比活性保持与粒径分布。［依据机理文献］([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))
- 生成“四类小试验证包”（GLP‑1多肽、蛋白/酶、益生菌、mRNA‑LNP）标准KPI与方法学（KF、aw、SEC/DLS、HPLC纯度/降解、气动粒径/重溶、CFU存活/体外消化），并在下周BIO 2026期间用于客户技术洽谈。([bioprocessintl.com](https://www.bioprocessintl.com/events/bioprocess-international-theater-bio-2026?utm_source=openai))
- 对接Catalent等AI‑QMS先行者/同业，学习偏差与放行数据结构，制定“低温喷雾工艺验证数据字典”（批记录、偏差、稳定性关联）以提升客户审计通过率。([pharmamanufacturing.com](https://www.pharmamanufacturing.com/industry-news/news/55384900/catalent-launches-enterprise-ai-tool-to-strengthen-quality-management-systems?utm_source=openai))
- 针对益生菌客户，优先推介“低温进风+高玻璃化壁材+短停留”的组合工艺，并提供7天40°C/75%RH加速筛选服务（目标降幅≤0.5 log）。([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0963996925024524?utm_source=openai))
- 关注EMA对GLP‑1储存标签与各国冷链指南的细化更新，准备“常温短时暴露—活性/稳定性”桥接实验方案，以支持客户注册变更或新适应症申请。([fiercepharma.com](https://www.fiercepharma.com/pharma/fierce-pharma-regulatory-tracker-2026?utm_source=openai))
- 与CordenPharma/Asymchem/ Symeres建立小试合作意向，提出“35°C进风/露点<–20°C/GLR≤12”的演示性批次与稳定性包报价（区分口服肽、吸入、功能食品三条主线）。［市场机会落地建议，含工程边界］([fiercepharma.com](https://www.fiercepharma.com/manufacturing/glp-1-manufacturer-cordenpharma-strikes-deal-peptide-cdmo-lining-new-production-sites?utm_source=openai))

7. 来源链接
以下为今日情报所据公开来源（可点击URL）：
```
https://www.fiercepharma.com/manufacturing/novo-nordisk-opens-czech-plant-unveils-29m-upgrade-china-facility
https://www.fiercepharma.com/pharma/fierce-pharma-regulatory-tracker-2026
https://www.pharmamanufacturing.com/industry-news/news/55384900/catalent-launches-enterprise-ai-tool-to-strengthen-quality-management-systems
https://arxiv.org/abs/2601.13716
https://www.bioprocessintl.com/events/bioprocess-international-theater-bio-2026
https://www.nutraingredients.com/Events/international-probiotics-conference-2026-ipc/
https://link.springer.com/article/10.1186/s41120-026-00160-8
https://pubmed.ncbi.nlm.nih.gov/41679558/
https://www.sciencedirect.com/science/article/pii/S0963996925024524
https://www.sciencedirect.com/science/article/abs/pii/S2212619826000094
https://www.hovione.com/press-room/article/hovione-eyeing-manufacturing-expansion-both-sides-atlantic
https://www.fiercepharma.com/manufacturing/glp-1-manufacturer-cordenpharma-strikes-deal-peptide-cdmo-lining-new-production-sites
https://www.genengnews.com/topics/bioprocessing/symeres-expands-spray-drying-capabilities-at-its-us-new-jersey-site/
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6882394
https://www.pharmaceutical-networking.com/dec-group-brings-game-changing-rheofreed-to-pharmaceutical-freeze-drying/
```

说明
- 已验证事实均附有来源；带“来源推断/我方机会”的内容系基于公开信息的保守推理与工程经验，需通过小试/稳定性数据进一步验证。
- 我方严格避免泛化宣称“35°C进风低温喷雾干燥”适用于所有物料；报告中所有适配性判断均限定于小试可验证范围与明确的KPI目标。

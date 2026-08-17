# 2026-08-17 低温喷雾干燥机行业情报日报

1. 执行摘要
- 🔵 过去72小时内，行业“增量需求—产能匹配”信号仍集中在多肽/GLP-1供应链与CDMO侧：国际制药工业（IPI）夏季刊发布CDMO专题，直指GLP-1推动的多肽管线与外包渗透率上升、工艺灵活与小批量多品种能力成为核心竞争点。该内容于两天前上线，时间敏感度高。 ([international-pharma.com](https://international-pharma.com/wp-content/uploads/2026/07/IPI-Summer-2026-CDMO-Subsection.pdf?utm_source=openai))
- 🔵 Lonza公开资料继续强调“生物大分子喷雾干燥（含mAbs、寡核苷酸与多肽）”的临床级供给能力，提示大CDMO正把喷雾干燥纳入从临床到商业化的标准化工艺选项，利于“冻干替代/补充”路线在受控场景中落地。 ([lonza.com](https://www.lonza.com/annualreport/2024/documents/Lonza%20Annual%20Report%202024.pdf?utm_source=openai))
- 🔵 GLP-1全球化与中国市场变量：PolyPeptide披露三星生物对其发起的要约收购流程安排，最迟2026-08-31发布详招，预计年内完成，意味着头部生物CDMO在多肽产能与客户结构上将进一步集中。 ([polypeptide.com](https://www.polypeptide.com/wp-content/uploads/2022/09/PolyPeptide-preliminary-HY-results-and-tender-offer.pdf?utm_source=openai))
- 🔴 学术侧新机理提醒：两流体喷嘴在常温进气下出现“近喷嘴瞬时冷冻—复融”应力的仿真研究，提示热敏活性物在雾化初区可能遭受未被监控的冻融应力，低温喷雾干燥工艺需联动雾化段热力学优化。 ([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))
- 🟢 基于以上动态，低温喷雾干燥（如35°C级进风）在“GLP-1/多肽液体制剂干粉化、吸入与口服干粉辅料工程化、益生菌与酶制剂常温稳定化、功能食品微胶囊化”等赛道的需求更具确定性，但必须以材料分层验证为前提，严禁“一刀切”适配。

2. 全球市场动态 (Global Market Dynamics)
- 🔵 CDMO与多肽：IPI夏季刊CDMO专栏（发布于约48小时内）指出，除GLP-1外，更复杂与更长链的肿瘤、多靶点多肽快速进入发现—临床，开发敏捷性与混合策略（SPPS片段+溶液偶联）成为主流；这类项目天生适配具快速工艺迭代能力的外包体系。 ([international-pharma.com](https://international-pharma.com/wp-content/uploads/2026/07/IPI-Summer-2026-CDMO-Subsection.pdf?utm_source=openai))
- 🔵 Lonza将喷雾干燥写入生物大分子临床供给产品线，标注“从早期到商业供应”的能力框架，有利于监管与客户对喷雾干燥（含低温变体）的合规认知与规模化路径。 ([lonza.com](https://www.lonza.com/annualreport/2024/documents/Lonza%20Annual%20Report%202024.pdf?utm_source=openai))
- 🔵 并购/资本：三星生物拟收购PolyPeptide（要约流程节点明确），若落地将强化其在多肽API与配套制剂端的纵深整合，或缩短“配方—干燥—充填”的跨公司链路。 ([polypeptide.com](https://www.polypeptide.com/wp-content/uploads/2022/09/PolyPeptide-preliminary-HY-results-and-tender-offer.pdf?utm_source=openai))
- 🔵 吸入生物制剂生态：产业会议预告与近期开源资料显示，喷雾干燥/喷雾冻干正成为吸入mAb、mRNA/LNP等干粉开发的重要路线之一（行业会议话题与综述均强化“室温稳定、干粉递送”的方向）。 ([intertek.com](https://www.intertek.com/pharmaceutical/events/inhaled-nasal-biologics-dna-forum/?utm_source=openai))
- 🔴 工艺风险新证据：喷嘴近区气体绝热降温可将局部温度拉到-130°C量级并在微米液滴内诱发瞬时成冰与复融，且与GLR与气体温度强相关——这对“热敏/冻敏”的蛋白、多肽、益生菌提出新的设计边界。 ([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))

3. 研发工艺匹配报告 (R&D & Process Alignment Report)
已验证事实 vs. 来源推断 vs. 我方可切入机会，分物料类型给出小试—中试的“可验证指标”与注意事项（非“一刀切”适配）：

- GLP-1/多肽（注射级粉体或经二次复溶）
  - 建议小试指标（可验证）：
    - 出口温度：≤25–30°C（以保护肽构象；需与含水量目标协同优化）
    - 停留时间：≤1.5–2.5 s（以降低界面/热应力）
    - 残余水分：1.0–3.0%（Karl Fischer）
    - 水活度aw：≤0.20
    - 纯度/降解：主峰纯度≥98%，脱酰胺/异构体/氧化物各≤0.5%（LC/MS）
    - 复溶后化学稳定性：25°C/60%RH加速7–14天主峰衰减≤1%（示例设计）
  - 工艺要点（来源推断+文献趋势）：多肽可考虑“低温喷雾干燥+无菌粉末转运/无菌充填”的无菌策略或作为冻干补充线；雾化段需规避瞬时冻融应力（控制雾化气温度/GLR/旋流设计）。 ([lonza.com](https://www.lonza.com/annualreport/2024/documents/Lonza%20Annual%20Report%202024.pdf?utm_source=openai))
  - 我方机会：建立“雾化近区热史”测算与验证包（CFD+微温度探针/相变指示）与“35°C级进风-低Tevap窗口”的参数地图，用于GLP-1二类/三类辅料体系筛选。

- 蛋白/生物大分子（含mAbs、寡核苷酸、mRNA/LNP吸入/干粉）
  - 建议小试指标（可验证）：
    - 出口温度：≤25–35°C（视赋形剂玻转温度与蛋白Tm）
    - 颗粒分布：Dv50=2–5 μm（吸入用）/20–80 μm（口服分散用）
    - 活性保持/聚集：SEC-HPSEC聚集体≤1–2%，DSC/Tm无显著下降
    - 干粉稳定性：25°C至少3–6个月关键质量属性（KPI）偏移≤10%（mRNA/LNP需核酸完整度与粒径PDI监控）
  - 事实依据：CDMO侧已提供临床级生物大分子喷雾干燥；行业综述与CEPI项目披露喷雾干燥RNA疫苗的室温稳定潜力。 ([lonza.com](https://www.lonza.com/annualreport/2024/documents/Lonza%20Annual%20Report%202024.pdf?utm_source=openai))
  - 我方机会：开发“低温喷雾干燥-玻璃化窗口”处方库（海藻糖/甘露醇/氨基酸/聚合物复配），并提供“干粉吸入”到“复溶注射”的双路径DoE。

- 益生菌/酶制剂
  - 建议小试指标（可验证）：
    - 出口温度：≤25–30°C（益生菌）；≤30–40°C（大多数酶，视热失活曲线）
    - 残余水分：2–4%；aw≤0.20
    - 存活率/活力：喷干后存活≥70–85%（菌株依赖）；加速30天活性保持≥80%
    - 复水行为：30 s内分散无团聚
  - 事实与推断：多数研究与白皮书支持喷雾干燥在合适赋形与温控下可接近冻干稳定性，但对菌株/酶系高度依赖。 ([sigmaaldrich.com](https://www.sigmaaldrich.com/US/en/technical-documents/technical-article/pharmaceutical-and-biopharmaceutical-manufacturing/solid-formulation-strategies/improving-api-solubility-using-spray-drying-polyvinyl-alcohol?utm_source=openai))
  - 我方机会：建立“超低Tevap+保护剂体系”（多元糖/蛋白-多糖复合）与“出风冷却-快速收集”一体化设计，辅以充氮闭环收集以抑制氧化失活。

- 功能食品/天然提取物/热敏新材料
  - 建议小试指标（可验证）：
    - 出口温度：30–45°C（随负载/壁材玻转温度调整）
    - 载药率与包封率：≥85–95%，氧化敏感负载（如多酚、油脂）过氧化值/色差在加速储存下≤10%波动
    - 颗粒流动性：休止角≤35°（便于下游灌装/压片/混合）
  - 事实依据：食品与功能配料侧喷雾干燥与纳米喷雾干燥已广泛用于微胶囊化并改善稳定与生物可及性。 ([annualreviews.org](https://www.annualreviews.org/doi/pdf/10.1146/annurev-food-032818-121641?utm_source=openai))
  - 我方机会：提供“低温-高包封”配方/参数模板库与“目标释放（pH/酶触发）”颗粒工程方案。

重要工艺红线与澄清
- 🔴 不得将“35°C进风低温喷雾干燥”泛化为“适用于所有物料”。对GLP-1、蛋白、菌/酶、天然物、功能配料，需分别做“雾化近区热史+玻璃化与干燥动力学+界面/剪切应力”三层验证。 ([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))

4. 市场与前景评估报告 (Market & Outlook Report)
- 🔵 需求侧：GLP-1推动的多肽外包与产能紧张延续；CDMO正向“多品种、小批量、快速切换+无菌粉末处理能力”升级。低温喷雾干燥若与无菌粉末充填/隔离系统协同，有望在“冻干替代/补充”中获得更多PoC到商业过渡单。 ([international-pharma.com](https://international-pharma.com/wp-content/uploads/2026/07/IPI-Summer-2026-CDMO-Subsection.pdf?utm_source=openai))
- 🔵 供给侧：头部CDMO（如Lonza）明确将喷雾干燥纳入生物大分子临床供应；多肽CDMO并购整合（三星生物-PolyPeptide）若推进，将加速“处方-工艺-充填”的集中与标准化。 ([lonza.com](https://www.lonza.com/annualreport/2024/documents/Lonza%20Annual%20Report%202024.pdf?utm_source=openai))
- 🔴 技术/合规门槛：无菌喷雾干燥/喷雾冻干仍需解决粉末无菌转运与充填良率；同时注意喷嘴近区“瞬时冻融”应力与粉尘静电问题对活性与收率的双重影响。 ([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))
- 🟢 展望：在“GLP-1口服/干粉吸入探索、mRNA/LNP干粉稳定化、益生菌/酶室温稳定化、功能食品高包封率”四个方向，低温喷雾干燥将出现更多从“中试验证—注册批次/商业小规模”的落地项目窗口。 ([waltersport.com](https://waltersport.com/wp-content/uploads/2026/04/NATURE-Expanding-global-access-to-mRNA-vaccines-Eshaghi-et-al.-2026-1.pdf?utm_source=openai))

5. 每日精准潜在客户画像 (Potential Customers & Leads)
- 🟢 PolyPeptide（全球多肽CDMO）
  - 画像要点：GLP-1/代谢疾病暴露高，正处并购要约期，年内整合预期增强“端到端”能力；对“快速开发—无菌粉转运—粉末充填”的低温喷雾干燥能力有潜在外协需求。 ([polypeptide.com](https://www.polypeptide.com/wp-content/uploads/2022/09/PolyPeptide-preliminary-HY-results-and-tender-offer.pdf?utm_source=openai))
- 🟢 Lonza（综合型CDMO）
  - 画像要点：公开强调生物大分子喷雾干燥的临床供应能力；我方可切入“低温窗口、雾化近区热史监控、吸入干粉流变与充填优化”等专业分工合作。 ([lonza.com](https://www.lonza.com/annualreport/2024/documents/Lonza%20Annual%20Report%202024.pdf?utm_source=openai))
- 🟢 OneSource CDMO（区域型，披露GLP-1商业化准备投资）
  - 画像要点：投资扩能以支持GLP-1商业化，可能需要从研发到中试的“低温喷干处方+参数放大”工具包与QA/验证文件模板。 ([onesourcecdmo.com](https://www.onesourcecdmo.com/wp-content/uploads/2026/01/Q3FY26_Earnings-Presentation.pdf?utm_source=openai))
- 🟢 H&T Presspart（吸入装置与胶囊平台）
  - 画像要点：近期展示“GLP-1类似物喷雾干燥粉体+Sunriser胶囊平台”体外表现海报；存在与我方在“粉体—器械匹配（粒径/充填/可吸入分数）”上的联合开发机会。 ([de.linkedin.com](https://de.linkedin.com/company/presspart?utm_source=openai))

6. 当日行动建议
- 🔴 针对热/冻敏活性（GLP-1/蛋白/益生菌）：立即在现有雾化系统上开展“近喷嘴热史”实测与CFD校准（记录雾化气温度、GLR、旋流强度与液滴尺寸分布），形成“无冻融应力”操作区图；作为低温喷雾干燥的前置安全边界。 ([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))
- 🟢 发起两类PoC项目招募（2–4周）
  1) GLP-1或多肽模型配方：目标出口温度≤28–30°C、aw≤0.20、主峰纯度≥98%，建立“喷雾干燥→无菌转运→无菌充填”小试SOP与批记录模板（支持审计）。  
  2) 益生菌或酶：目标喷干后存活/活力≥80%、30天加速≥80%，验证“出风区快速冷却+惰性气体收集”的组合工艺。
- 🟢 商务拓展与技术路演（本周内）
  - 向PolyPeptide与OneSource发送“低温喷雾干燥—无菌粉末处理”技术白皮书与2页价值主张，重点突出“雾化近区冻融风险规避”“35°C级进风-低Tevap窗口优化”“粉末充填良率>99%方案（流动性与静电治理）”。 ([onesourcecdmo.com](https://www.onesourcecdmo.com/wp-content/uploads/2026/01/Q3FY26_Earnings-Presentation.pdf?utm_source=openai))
- 🔵 关注监管与标准
  - 汇总FDA/ISO关于无菌/冻干过程控制与可接受的替代工艺证据要求，梳理我们低温喷雾干燥在“工艺等同性/稳定性/可追溯”上的验证路线与文件清单，预制审计应对材料。 ([fda.gov](https://www.fda.gov/media/71026/download?attachment=&utm_source=openai))

7. 来源链接
- IPI Summer 2026 | CDMO专题（发布约2天内）：https://international-pharma.com/wp-content/uploads/2026/07/IPI-Summer-2026-CDMO-Subsection.pdf ([international-pharma.com](https://international-pharma.com/wp-content/uploads/2026/07/IPI-Summer-2026-CDMO-Subsection.pdf?utm_source=openai))
- Lonza 年报与能力说明（生物大分子喷雾干燥临床供给）：https://www.lonza.com/annualreport/2024/documents/Lonza%20Annual%20Report%202024.pdf ([lonza.com](https://www.lonza.com/annualreport/2024/documents/Lonza%20Annual%20Report%202024.pdf?utm_source=openai))
- PolyPeptide 要约收购流程新闻稿（三星生物）：https://www.polypeptide.com/wp-content/uploads/2022/09/PolyPeptide-preliminary-HY-results-and-tender-offer.pdf ([polypeptide.com](https://www.polypeptide.com/wp-content/uploads/2022/09/PolyPeptide-preliminary-HY-results-and-tender-offer.pdf?utm_source=openai))
- OneSource CDMO 投资者演示（GLP-1商业化扩能）：https://www.onesourcecdmo.com/wp-content/uploads/2026/01/Q3FY26_Earnings-Presentation.pdf ([onesourcecdmo.com](https://www.onesourcecdmo.com/wp-content/uploads/2026/01/Q3FY26_Earnings-Presentation.pdf?utm_source=openai))
- 喷嘴近区“瞬时冷冻—复融”机理研究（arXiv 2026-01）：https://arxiv.org/abs/2601.13716 ([arxiv.org](https://arxiv.org/abs/2601.13716?utm_source=openai))
- 吸入/鼻用生物制剂论坛（含喷雾冻干mAb干粉主题）：https://www.intertek.com/pharmaceutical/events/inhaled-nasal-biologics-dna-forum/ ([intertek.com](https://www.intertek.com/pharmaceutical/events/inhaled-nasal-biologics-dna-forum/?utm_source=openai))
- mRNA疫苗室温稳定化方向（Nature综述与CEPI项目概览摘引）：https://waltersport.com/wp-content/uploads/2026/04/NATURE-Expanding-global-access-to-mRNA-vaccines-Eshaghi-et-al.-2026-1.pdf ([waltersport.com](https://waltersport.com/wp-content/uploads/2026/04/NATURE-Expanding-global-access-to-mRNA-vaccines-Eshaghi-et-al.-2026-1.pdf?utm_source=openai))
- 赋形/低温喷雾干燥应用要点示例（Sigma-Aldrich技术页）：https://www.sigmaaldrich.com/US/en/technical-documents/technical-article/pharmaceutical-and-biopharmaceutical-manufacturing/solid-formulation-strategies/improving-api-solubility-using-spray-drying-polyvinyl-alcohol ([sigmaaldrich.com](https://www.sigmaaldrich.com/US/en/technical-documents/technical-article/pharmaceutical-and-biopharmaceutical-manufacturing/solid-formulation-strategies/improving-api-solubility-using-spray-drying-polyvinyl-alcohol?utm_source=openai))
- H&T Presspart（GLP-1类喷雾干燥粉体与胶囊平台海报动态）：https://de.linkedin.com/company/presspart ([de.linkedin.com](https://de.linkedin.com/company/presspart?utm_source=openai))

说明与范围声明
- 本日报严格检索至2026-08-17（美国时间）前72小时内公开信息。与低温喷雾干燥直接相关的“当天/72小时”权威新闻较少，最具时效与相关性的来源为 IPI Summer 2026（发布约2天）；其余援引为近一周—近季度的权威资料与公司公开文件，用于提供背景与可操作路径。若需进一步核验特定客户侧一手进展（如未公开的工艺验证/产能投产节点），建议进入一对一BD访谈与NDA后数据核对流程。

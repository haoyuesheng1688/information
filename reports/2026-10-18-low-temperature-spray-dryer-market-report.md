# 2026-10-18 低温喷雾干燥机行业情报日报

- 检索截止：2026-10-18 08:38，北京时间；不代表全天完整覆盖。
- 依据：本项目 AGENTS.md 与 config/keywords.json；关键词完整，本次未修改。
- 增量基线：10月17日本地报告。今日新增关注 ISPE 会期、多肽小流量密闭喷干的工程要求及天然提取物评价指标之间的取舍；旧资料保留原日期。
- 本轮未检得10月18日新发布且可核验的35°C进风商业验证、普适替代冻干或明确采购公告。未检得不等于不存在。
- 证据口径：“已验证事实”指原始来源确有披露；企业自述、论文摘要均不是我方独立复现实验。“来源推断”和“我方可切入机会”不等于已成交需求。

## 1. 全球市场动态（Global Market Dynamics）

### 🔵 当日相关事件：ISPE年会进入预定会期，注意时差

**已验证事实：** ISPE官方日程为2026年10月18—21日，地点在美国华盛顿地区，支持线上参与；议程注明使用美国东部时间。北京时间本次截止时，美国东部仍为10月17日晚，因此只可称“即将进入当地会期”，不能称已取得今天的会议成果。[S1](https://ispe.org/conferences/2026-annual-meeting-expo/agenda)

**来源推断：** 工程、运行及质量系统议题可用于审查制药设备准入要求。**我方可切入机会：** 整理低温干燥的工艺数据完整性、清洁验证和密闭收粉问题清单；尚无证据证明特定参会企业采购35°C设备。

### 🔵 多肽喷干：已披露工程配置比“低温”标签更有商业含义

**已验证事实：** Piramal于8月4日发布Turbhe多肽工厂新增喷干套间公告，提及Band 5隔离。当前可读的官方白皮书描述约0.01—1 L/h进料范围、氮气闭路、溶剂冷凝、氧监测和隔离收粉；网页未见明确发布日期，不能当作今日新投产。白皮书还使用“Once fully validated”的措辞，不足以确认特定产品已完成全部验证。[S2](https://www.prnewswire.com/news-releases/piramal-pharma-solutions-expands-peptide-api-facility-with-advanced-spray-drying-suite-302842218.html) [S3](https://www.piramalpharmasolutions.com/resources/white-paper/advancing-peptide-manufacturing-through-spray-drying-technology)

**来源推断：** peptide CDMO可先从小流量、高价值物料工艺开发切入，工程隔离成本可能超过单纯加热成本。**我方可切入机会：** 提供经实测的小试比较包；不能将该设备视为35°C验证或GLP-1订单。

### 🔵 大规模制药喷干投资仍以明确产品平台为中心

**已验证事实：** Lonza于9月10日宣布在美国Bend建设商业PSD-4喷干设施，预计2029年完成，面向喷雾干燥分散体（SDD）需求。这是建设计划，非已投产实绩。[S4](https://www.lonza.com/news/2026-09-10-07-00)

**来源推断：** pharmaceutical spray drying CDMO有扩产信号，但难溶小分子SDD市场不等于热敏蛋白或多肽冻干替代市场。**我方可切入机会：** 对标从开发到商业放大的交付体系，不据此推算35°C设备市场规模。

### 🔴 天然提取物：喷干与冻干可能各有优胜指标

**已验证事实：** 1月19日发表的蒲公英叶提取物研究摘要称，喷干样品的包埋效率优于冻干样品，而冻干样品的抗氧化活性更高。本次获取的是出版商检索摘要，全文打开失败；不外推其工况至35°C。[S5](https://pubs.rsc.org/en/content/articlelanding/2026/fb/d5fb00693g)

**来源推断：** 单一包埋效率不足以证明活性保留与货架期更优。**我方可切入机会：** 将功能食品、植物提取物的保活、复溶与储存稳定性作为联合验收条件。

## 2. 研发工艺匹配报告（R&D & Process Alignment Report）

### 🔴 最小验证案例：同批物料、同一质量目标、全过程能耗

以下为建议实验，不代表已经执行。先用一种非高活性、非无菌要求的模型酶制剂建立小试闭环，确认后再进入客户样品。

- 分组：进料原液基准、现有冻干基准、35°C进风喷干试验；保持固形物和保护剂可比较，记录配方差异。
- 运行记录：inlet/outlet temperature、进气露点、气量、进料速率、固含量、雾化条件、压力、停留时间估计及估计方法；闭路系统另记氧含量与冷凝负荷。
- 通用输出：活性保留率、含水率、水活度、粒径分布D10/D50/D90、复溶性、结构稳定性、干基收率及储存后变化。
- 活性采用同一干基或同一有效物质量归一；另报告总活性回收率，避免只看收集粉体的比活而掩盖壁损。
- 能耗边界包含加热、除湿、制冷、真空、压缩气体及启停清洁；分别比较kWh/kg蒸发水和kWh/kg合格粉体，不预设节能百分比。
- 验收门槛由样品用途和客户规格事先确定；达不到水分、活性或收率要求即暂停放大，先定位配方、干燥驱动力或收粉损失。

### 🔴 各物料必须补齐的判据

- **GLP-1/多肽：** 在六项通用指标之外，测peptide chemical stability、有关物质、氧化/脱酰胺、必要的残留溶剂和功能效价；不能用纯度代替效价。
- **Biologics/proteins：** 在六项通用指标之外，测protein aggregation、SEC单体比例、适当的结构分析与功能活性；若要求无菌，需独立确认aseptic spray drying整条路径，低温不是灭菌步骤。
- **酶制剂：** 在六项通用指标之外，明确底物与酶活测定法、比活、总活性回收及储存失活。8月15日的除湿空气辅助纤维素分解酶喷干研究可作为后续阅读入口，本次仅核验出版商题录，未引用其未读实验数值。[S6](https://www.mdpi.com/2076-3417/16/16/8135)
- **益生菌：** 在六项通用指标之外，按菌株测probiotic viability、CFU及log损失，并评价储存期存活；比较前后固形物与稀释倍数。2026年1月综述把热、氧和壁材保护列为重要问题，但综述不构成某菌株35°C实证。[S7](https://pubmed.ncbi.nlm.nih.gov/41347266/)
- **天然提取物/功能食品：** 测标志成分、氧化指标、香气损失、包埋效率、流动性及应用端复溶；区分化学抗氧化测试与人体功效。
- **新材料/热敏聚合物：** 测再分散性、团聚、晶型和目标性能。近期AAPS PharmSciTech论文探索用一步喷干形成Eudragit L100纳米球粉体，提供工艺集成线索，但不证明35°C适用或工业订单。[S8](https://link.springer.com/article/10.1208/s12249-026-03458-8)

35°C仅是进风设定，不是物料全程温度、保活率或干燥能力保证。持续生产及lab-to-market scale-up还需验证长时间壁损、气体湿度积累、清洁切换和批间一致性。

## 3. 市场与前景评估报告（Market & Outlook Report）

**已验证事实：** 官方资料存在多肽小规模密闭喷干配置与大型SDD设施建设计划；论文体现不同干燥路线在不同指标上的取舍。[S3](https://www.piramalpharmasolutions.com/resources/white-paper/advancing-peptide-manufacturing-through-spray-drying-technology) [S4](https://www.lonza.com/news/2026-09-10-07-00) [S5](https://pubs.rsc.org/en/content/articlelanding/2026/fb/d5fb00693g)

**来源推断：** 当下更可信的价值主张是“指定物料在合格粉体目标下缩短周期、提高回收或降低全流程成本”。冻干设备投资和需求不能直接推算全球冻干产能缺口；本轮没有获得可比较的排产等待时间、利用率或每批总周期数据。

**我方可切入机会：**

1. 🟢 优先以酶制剂、天然提取物及非无菌功能原料完成可复核案例，形成activity retention与energy saving证据。
2. 🟢 多肽CDMO列为中期高价值合作对象，先评估溶剂、密闭等级与客户分析能力，再讨论中试。
3. 🔴 已批准的无菌注射蛋白终端冻干制剂替代难度高，不作为近期“直接替换”承诺。
4. 🔴 GLP-1行业热度不等于本设备可服务市场；不发布未经核验的市场规模、节能率、回本年限或“完美替代冻干”宣传。

## 4. 每日精准潜在客户画像（Potential Customers & Leads）

以下均为公开资料支持的研究/商务线索，不是采购确认；本轮未发送外联消息。

### 🟢 Piramal Pharma Solutions｜印度Turbhe｜多肽工艺开发与工程对标

- 已知匹配：多肽喷干套间及小流量密闭配置已有公开披露。[S3](https://www.piramalpharmasolutions.com/resources/white-paper/advancing-peptide-manufacturing-through-spray-drying-technology)
- 目标角色：Peptide Technical Services、Process Development、Engineering。
- 可切入问题：现有路线对哪些样品的残留溶剂、活性或收率不满足需求；低温路线能否带来可量化增益。
- 优先级：中。已有设备，不能默认需要新购；更适合差异化联合评价。

### 🟢 东北农业大学乳品科学团队及论文署名产业研发单位｜中国｜益生菌微胶囊

- 已知匹配：2026年综述署名单位包括东北农业大学、内蒙古乳业技术研究院及伊利相关团队。[S7](https://pubmed.ncbi.nlm.nih.gov/41347266/)
- 目标角色：菌种保护、微胶囊和干燥工艺研发。
- 可切入问题：提供一株菌、现有保护配方及冻干基线，比较即时与储存后CFU、aw和复溶性。
- 优先级：较高的合作验证线索；作者单位不等于设备采购主体，需先识别成果转化与中试负责人。

### 🟢 Lonza Bend｜美国｜粒子工程及制药喷干放大标杆

- 已知匹配：SDD商业喷干扩产计划。[S4](https://www.lonza.com/news/2026-09-10-07-00)
- 目标角色：Particle Engineering、Process Development、Capital Projects。
- 可切入问题：小试到中试参数迁移、收粉与清洁的验证证据。
- 优先级：低至中。现有大型平台成熟，应先作竞争与能力对标，不能据公告认定为35°C设备买家。

## 5. 当日行动建议（Action Items）

1. **研发优先：** 完成模型酶三组对照的试验卡，锁定检测方法与合格目标；仪表和数据字段按上述关键词命名，先完成一批数据回读，再扩展样品。
2. **市场优先：** 准备一页“适用物料—冻干基线—低温喷干质量—总周期—全流程能耗”问卷。当前仅准备资料，不自动外联。
3. **工艺采购判断：** 将Piramal的密闭、氧监测、溶剂回收与隔离收粉要求作为需求访谈参照；禁止把液体进料L/h写成粉体产能kg/h。
4. **情报跟踪：** 会期结束后再核验ISPE公开成果；当前只记录日程。继续查找客户真实冻干等待周期和中试样品需求。
5. **宣传边界：** 使用“可针对特定物料验证的冻干替代路线”，保留35°C进风的设备条件说明，所有保活及节能承诺须附测试边界。

## 6. 来源链接（Sources）

- S1｜ISPE官方议程，活动日期2026-10-18至21；本轮读取，非会后成果：[Agenda](https://ispe.org/conferences/2026-annual-meeting-expo/agenda)。
- S2｜Piramal企业新闻稿，2026-08-04：[Turbhe spray drying suite](https://www.prnewswire.com/news-releases/piramal-pharma-solutions-expands-peptide-api-facility-with-advanced-spray-drying-suite-302842218.html)。
- S3｜Piramal官方白皮书网页，发布日期未明确，本轮读取正文：[Advancing Peptide Manufacturing](https://www.piramalpharmasolutions.com/resources/white-paper/advancing-peptide-manufacturing-through-spray-drying-technology)。
- S4｜Lonza官方公告，2026-09-10：[Bend commercial spray-drying facility](https://www.lonza.com/news/2026-09-10-07-00)。
- S5｜RSC论文，2026-01-19，DOI 10.1039/D5FB00693G；出版商检索摘要，全文访问失败：[Dandelion spray versus freeze drying](https://pubs.rsc.org/en/content/articlelanding/2026/fb/d5fb00693g)。
- S6｜Applied Sciences，2026-08-15，DOI 10.3390/app16168135；仅题录，正文访问失败：[Dehumidified air-assisted enzyme spray drying](https://www.mdpi.com/2076-3417/16/16/8135)。
- S7｜综述，2026年1月卷期，PMID 41347266；PubMed摘要与署名：[Probiotic microcapsules](https://pubmed.ncbi.nlm.nih.gov/41347266/)。
- S8｜AAPS PharmSciTech，2026年论文，DOI 10.1208/s12249-026-03458-8；出版商页面：[Polymeric nanospheres via spray drying](https://link.springer.com/article/10.1208/s12249-026-03458-8)。

检索覆盖35C inlet low-temperature spray dryer、lyophilization/freeze drying replacement、GLP-1/peptide CDMO、biologics/proteins、enzymes/probiotics、functional food encapsulation、natural extracts、新材料及节能放大。未将搜索结果抓取时间作为事件日期，未将未经核验的媒体数字作为市场规模。

# 2026-09-16 低温喷雾干燥机行业情报日报

数据截止：2026-09-16 08:33（Asia/Shanghai）；仅覆盖本次运行可检索的公开信息，不代表全天动态。遵循本项目 AGENTS.md 与 config/keywords.json；已核对关键词，无缺项，未修改配置。去重基线为9月15日完整报告，并检索历史报告中的Piramal记录。“新增纳入”只表示相对昨日新增，不表示当天发布。

关键词：35C inlet low-temperature spray dryer；lyophilization / freeze drying；activity retention、continuous production、lab-to-market scale-up、energy saving、shorter cycle time；GLP-1、peptide CDMO、biologics、pharmaceutical spray drying、spray-dried dispersion、aseptic spray drying、functional food encapsulation。

## 全球市场动态 (Global Market Dynamics)

### 🔵 1. CordenPharma：无菌制剂扩产规划，不能折算为冻干替代市场｜新增纳入

**已验证事实：** 9月10日企业公告披露Caponago多年期8,000万欧元投入，预计总注射剂能力最高5亿支/年；两条新隔离器灌装线目标分别为2027年中、2028年完成。新空间包含大型冻干等可选配置。[S1](https://cordenpharma.com/articles/press-release-cordenpharma-boosts-aseptic-fill-finish-capacity-to-500-million-sterile-injectable-units-per-year/)

**来源推断：** 这是面向复杂注射剂的制造投入，5亿支不是已经投运的冻干瓶产能，更不是喷干设备需求。冻干仍是客户可选工艺，不能据此宣布被替代。

**我方可切入机会：** 先识别API干燥、无菌粉体制造和最终灌装的边界，再讨论工艺开发；暂不进入现有注册制剂替换承诺。

### 🔵 2. EMZI-UiTM：油脂与植物提取物共包埋，新增可核验研发线索

**已验证事实：** 9月7日Applied Research原始论文研究印加果油及植物提取物乳液喷干；在所测条件中，140°C入口、25%阿拉伯胶、油水比1:9获得93.8%粉体回收率。它是回收率，不能改写成活性保留率或包埋率。[S2](https://onlinelibrary.wiley.com/doi/10.1002/appl.70190)

🔴 **来源推断与边界：** 文中缺少进料对照来计算成分保留率，也未证明氧化或储存稳定性。单因素筛选及小样本机器学习不能外推35°C运行窗口。这与昨日双植物提取物论文不同，但属于同一产学团队的延伸线索。

**我方可切入机会：** 用进料—成品质量平衡和储存氧化数据建立差异化，而不是只比较收粉率。

### 🔵 3. Piramal：回查原始公告，作为历史跟踪

**已验证事实：** 官网原始PDF日期为8月4日，Turbhe新增多肽喷干套间，最高进料1 L/h，采用闭式惰性气体系统并具备Band 5 containment。历史日报已多次记录，本次不计新增事件。[S3](https://ppsazdevwebsitestg.blob.core.windows.net/public/uploads/generic_file_upload/040826103057-Piramal-Pharma-Solutions-Expands-Peptide-API-Facility-with-Advanced-Spray-Drying-Suite.pdf)

🔴 **来源推断：** 它证明小批量高效价分子喷干服务的具体应用场景，未披露35°C性能；职业暴露控制与无菌保障是不同要求。其能力不能默认继承给我方设备。

### 🔵 4. 益生菌与多肽线索：区分现状核验和新闻

**已验证事实：** NSF公开目录列有苏州Wecare Probiotics的粉剂等产品类别与包埋等工艺。搜索摘要和打开正文的“current as of”日期不一致，故仅作为待复核企业线索，不宣称9月15日新获证或本日证书有效性已确认。[S4](https://info.nsf.org/Certified/455GMP/Listings.asp?Company=C0238295&Standard=455-2GMP)

**已验证事实：** Sinopep官网列出9月28日至10月1日Boulder Peptide Symposium参展安排；属于未来交流窗口，并非新增干燥采购。[S5](https://www.sinopep.com/)

🔴 **检索空白：** 本轮未核验到9月16日当天发布的35°C突破或普适冻干替代证据；酶制剂、热敏催化剂/高端聚合物/纳米材料未发现足够直接的新商业事件。未找到可量化全球冻干瓶颈或新增相关政策变化的一手证据。旧文抓取日期、期刊卷期日期和未来活动不当作新闻发布日期。

## 研发工艺匹配报告 (R&D & Process Alignment Report)

### 🔴 今日最小验证：先确认35°C的脱水能力，再加真实物料

以下是**建议试验方案，未执行实体试验**。延续昨日四组对照思路，先增加低风险设备能力门槛；不默认装置具备真空、无菌、静电或有机溶剂处理能力。

1. 用已确认可处理的水系空白载体，固定35°C入口实测干球温度；记录入口露点、绝对压力、干气流量、进料量、固含量、出口温度与出粉状态。先按设备允许范围设置条件，不照搬文献140°C配方或历史日报的露点假设。
2. 若不能形成满足水分要求的粉体，先核对湿空气与热量衡算及回收系统，调整进料负荷等可控条件；不得用湿粉高回收率判定成功。
3. 能稳定出粉后，选择一种已有检测方法的模型酶：A未处理进料、B仅雾化收集、C现行冻干、D入口35°C喷干；同批原料、同配方。B组单独观察雾化/气液界面损伤。
4. 候选条件至少三次独立工艺重复，按产品预先约定的质量限度判定。无质量限度则只报告探索数据，不判“替代成功”。

**拟用记录关键词**（仅为试验记录字段，未配置PLC/HMI）：Batch_ID、Material_ID、Formulation_ID、Drying_Method、Inlet_T_C、Outlet_T_C、Gas_Dewpoint_C、Chamber_AbsPressure_kPa、Dry_Gas_Flow、Feed_Rate、Feed_Solids_pct、Residence_Time_s、Powder_Recovery_pct、Activity_Retention_pct、Residual_Moisture_pct、Water_Activity、PSD_D10_D50_D90_um、Reconstitution_Time_s、Structure_Stability、Total_Energy_kWh。停留时间须注明测量或估算方法。

### 🔴 各物料质量闭环

- **GLP-1/多肽：** 必测活性保留率、含水率、水活度、粒径、复溶性和结构稳定性；增加peptide chemical stability、HPLC/LC-MS杂质及残溶。先定位纯化后API的干燥节点，不把全部GLP-1销售额当作设备市场。
- **蛋白/biologics：** 六项共同指标全部检测；增加protein aggregation（SEC）、构象及复溶后颗粒。入口35°C不排除界面变性。
- **酶制剂：** 六项共同指标全部检测；同时记录干基比活与整批总酶活回收。载体比例和收粉损失必须计入。
- **益生菌：** 活性以probiotic viability、CFU保留及整批活菌回收衡量；同时测含水率、水活度、粒径、复水分散性、细胞膜/结构完整性。即时存活与包装条件下储存存活分开。
- **功能食品/天然提取物：** 增加标志物进出料质量平衡、表面油、氧化指标、风味和储存后分散性。粉体回收率不代替营养或活性保持。
- **疫苗/mRNA与新材料：** 保留探索级别；前者需效力和递送体系完整性，后者需催化/电化学等目标功能保持。无针对性原始数据，不类推通用替代。

### 🔴 节能与放大门槛

以整个干燥段为边界，纳入除湿、真空（如有）、压缩空气、冷却、启停、清洁和后处理。报告kWh/kg蒸发水与每单位合格活性产出能耗；35°C本身不能证明energy saving。周期比较从相同进料状态到同质量标准的可放行粉体，包含清洗换批。只有质量及质量平衡通过后，才评价continuous production、shorter cycle time和lab-to-market scale-up。

## 市场与前景评估报告 (Market & Outlook Report)

🔵 **已验证事实：** 本轮证据覆盖多肽小批量喷干服务、未来无菌注射剂扩产，以及配料共包埋研究；三者对应不同工艺节点，不能合并计算可替代市场。[S1](https://cordenpharma.com/articles/press-release-cordenpharma-boosts-aseptic-fill-finish-capacity-to-500-million-sterile-injectable-units-per-year/)；[S2](https://onlinelibrary.wiley.com/doi/10.1002/appl.70190)；[S3](https://ppsazdevwebsitestg.blob.core.windows.net/public/uploads/generic_file_upload/040826103057-Piramal-Pharma-Solutions-Expands-Peptide-API-Facility-with-Advanced-Spray-Drying-Suite.pdf)

🔴 **来源推断：** 35°C设备商业说服力应来自目标物料的合格活性产率和整段成本。低温能否同时满足脱水能力、收粉、稳定性和生产节拍，仍需实测；没有可靠渗透率与可替代比例，不给出TAM/CAGR数字。

🟢 **我方可切入机会与顺序：** 模型酶及天然提取物小试 → 菌株特定的稳定性验证 → 多肽API工艺开发 → 无菌蛋白/疫苗长期项目。该顺序是工程与开发负担的判断，不是已证实订单概率。

🔴 **冻干痛点的访谈证据：** 逐客户收集批周期、排队时间、单位能耗、清洁换批、放行损失和实际瓶颈节点。灌装扩产不能证明干燥瓶颈；小分子spray-dried dispersion增长也不能代替蛋白低温市场证明。

## 每日精准潜在客户画像 (Potential Customers & Leads)

以下均为资格筛选线索，未联系企业，未确认预算、采购或可公开使用的客户物料。P1/P2表示验证优先级。

### 🟢 EMZI-UiTM NANO-CORE / EMZI Holding｜马来西亚｜P1，延伸研究

触发为油脂—植物提取物论文[S2]。建议对接共同研究团队，先确认目标标志物、原乳液配方与储存包装。交付一页进出料质量平衡试验表；只有低温条件能够稳定出粉并改善质量时，再讨论联合中试。未确认设备采购。

### 🟢 Wecare Probiotics｜中国苏州｜P1，新增待复核线索

触发为NSF制造目录[S4]，并非喷干设备使用证据。建议对接菌粉工艺及稳定性团队，先复核目录时效、菌株、当前干燥路线和目标货架期。下一步准备同菌株/保护剂/包装方案；不满足储存后活菌指标即停止替代主张。

### 🟢 Piramal Pharma Solutions｜印度Turbhe｜P2，历史线索深化

触发为已验证的小批量多肽喷干套间[S3]。建议对接Peptide Process Development，识别现有路线未覆盖的物料，而非重复推销既有能力。先问溶剂体系、质量约束和技术缺口；我方能力未确认前不承接高效价或溶剂项目。

### 🟢 CordenPharma｜意大利Caponago｜P2，长期工艺评估

触发为无菌制剂规划[S1]。建议对接Drug Product Process Development，先厘清API与最终制剂责任边界。下一步形成工艺节点问题清单；尚无我方无菌粉体制造与转移证据，不进入商业替换报价。

### 🟢 Sinopep｜中国/全球客户｜P2，未来技术交流窗口

触发为官网多肽CDMO定位及未来活动[S5]。建议对接CMC/工艺开发，询问纯化后干燥是否存在实际瓶颈；准备质量、批量、周期与残溶问题单。参展安排不等于采购意向。

## 当日行动建议 (Action Items)

1. **研发P0：** 先做水系空白载体的35°C脱水门槛检查，再开展模型酶四组对照。今天交付方案，不将未做试验写成验证成功。
2. **市场P0：** 将“进风35°C”改写为待按物料验证的能力窗口；对外价值主张采用活性、回收、周期和总能耗的可验证指标。
3. **研发P1：** 为天然提取物增加进料基线与氧化检测；补齐完整质量平衡，避免将高收粉率误报为活性保持。
4. **线索P1：** 优先复核Wecare目录与工艺，深化EMZI-UiTM；Piramal归入历史跟踪，CordenPharma按未来里程碑跟踪。未发送对外消息。
5. **情报P1：** 继续检索酶制剂、新材料以及35°C一手性能数据；保持无结果栏目，不使用不相关论文填充。
6. **归档：** 写入项目Markdown、Notion指定父页，fetch回读完整正文及ancestor-path，再同步GitHub main。结果写入独立同步记录。

## 来源链接 (Sources)

全部于2026-09-16检索。企业公告属于企业披露，不等于独立验收；论文结果仅适用于原试验边界。

- **S1｜2026-09-10｜企业公告：** [CordenPharma Caponago扩产](https://cordenpharma.com/articles/press-release-cordenpharma-boosts-aseptic-fill-finish-capacity-to-500-million-sterile-injectable-units-per-year/)。已核验正文，明确预测产能与新线目标时间。
- **S2｜2026-09-07｜原始研究：** [Oil–herbal extract emulsions spray-drying study](https://onlinelibrary.wiley.com/doi/10.1002/appl.70190)。已查看正文方法、结果及局限；不外推35°C。
- **S3｜2026-08-04｜企业原始PDF，历史跟踪：** [Piramal peptide spray-drying suite](https://ppsazdevwebsitestg.blob.core.windows.net/public/uploads/generic_file_upload/040826103057-Piramal-Pharma-Solutions-Expands-Peptide-API-Facility-with-Advanced-Spray-Drying-Suite.pdf)。由官网新闻列表进入，核验两页PDF文本。
- **S4｜动态目录，日期冲突｜待复核线索：** [NSF Wecare Probiotics listing](https://info.nsf.org/Certified/455GMP/Listings.asp?Company=C0238295&Standard=455-2GMP)。搜索结果时间为9月15日，打开页面显示6月29日；不作为新获证新闻。
- **S5｜企业现状/未来活动：** [Sinopep官网](https://www.sinopep.com/)。本日回查，页面未提供对应内容的明确发布日期。

报告结束。今日重点：明确产能口径，以物料质量闭环判断35°C工艺价值；未发现普适替代冻干的新证据。


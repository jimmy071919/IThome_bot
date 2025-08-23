### Windows 11 24H2 及 Windows Server 2025 移除 PowerShell 2.0

*   微軟將於 8 月的 Windows 11 24H2 及 9 月的 Windows Server 2025 更新中移除 Windows 7 時代的 PowerShell 2.0，以提升安全性。
*   PowerShell 2.0 架構老舊，缺乏現代安全防護，易被駭客利用繞過安全機制。
*   大部分用戶不受影響，PowerShell 5.1 或 7.x 版仍受支援。
*   企業若有舊式腳本或軟體使用 PowerShell 2.0 需及早升級至 PowerShell 5.1 或 7，或尋求替代方案。

### 紐約州檢察總長指控 Zelle 存在詐欺風險

*   紐約州檢察總長指控 Zelle 缺乏安全功能，放任詐欺活動，導致受害者在 2017 年至 2023 年間損失超過 10 億美元。
*   Zelle 註冊流程缺乏驗證，易被詐騙者冒用，且轉帳立即且不可逆。
*   常見詐騙型態包括入侵帳號盜轉資金及冒充機構誘導轉帳。
*   紐約州檢察總長辦公室稱 EWS 與合作銀行明知 Zelle 存在詐騙，卻未採取有效行動。

### Fortinet FortiSIEM 存在遠端命令注入漏洞

*   資安業者 Fortinet 發布公告，指出 FortiSIEM 存在未經授權的遠端命令注入漏洞 (CVSS 9.8)。
*   攻擊者可透過特製 CLI 請求執行未經授權的程式碼。
*   所有 5.4 至 7.3 版本的 FortiSIEM 皆受影響，7.4 版不受影響。
*   建議升級至不受影響版本或限制 phMonitor 連接埠（7900 埠）的存取。
*   已有實際漏洞利用工具出現，可能被用於攻擊行動。

### 馬斯克指控蘋果 App Store 偏私 ChatGPT 引發爭議

*   馬斯克指控蘋果 App Store 偏私 ChatGPT，違反反壟斷法，並與 OpenAI 執行長 Sam Altman 隔空交火。
*   馬斯克質疑蘋果拒絕將 X 或 Grok 列入「Must Have」類別。
*   Altman 反批馬斯克操弄 X 演算法，偏私自己和自家公司。
*   蘋果否認操弄排行榜，稱 App Store 透過公正標準遴選 App。

### Rust 1.89 版本發布，提升語法可讀性與效能

*   Rust 團隊釋出 1.89 版本，帶來多項語言功能與編譯器更新。
*   主要亮點包括常數泛型引數開放使用底線符號 `_` 進行自動推斷，簡化泛型常數使用。
*   新增 `mismatched_lifetime_syntaxes` 預設警告，檢查函式輸入與輸出生命週期語法是否一致。
*   擴充 x86 平台目標功能設定，支援 SHA-512、SM3、SM4、KL 與 Wide KL 等指令集。
*   x86\_64-apple-darwin 從第一級支援降為第二級，短期內仍提供工具，長期可能影響相容性。

### 8 月資安更新：微軟修補漏洞數創新高，Fortinet VPN 遭攻擊

*   8 月軟體業者例行更新，微軟修補重大層級資安漏洞數創今年新高（17 個）。
*   Rapid7、Zero Day Initiative 提出警告，呼籲用戶優先處理部分漏洞。
*   SAP 公告兩項風險值達 9.9 分的漏洞，影響 S/4HANA、Landscape Transformation（SLT）系統。
*   駭客針對 Fortinet SSL VPN 系統發動攻擊，目標轉向網路管理平臺 FortiManager。
*   安聯人壽 Salesforce 系統遭駭，客戶資料外洩，ShinyHunters 疑似與 Scattered Spider 及 Lapsus$ 整合。
*   法國電信業者 Bouygues Telecom 遭網路攻擊，640 萬用戶資料外洩。
*   微軟修補 111 項漏洞，其中 Kerberos 零時差權限提升漏洞 CVE-2025-53779 已被公開利用。
*   SAP 修補 15 項漏洞，包含影響 S/4HANA 及 SLT 的程式碼注入漏洞 CVE-2025-42950、CVE-2025-42957。

### Fortinet SSL VPN 再次成為攻擊目標

*   駭客再次針對 Fortinet SSL VPN 系統發動攻擊，但這次目標轉向網路管理平臺 FortiManager。
*   攻擊者可能透過相同基礎設施或工具向不同 Fortinet 裝置下手。
*   GreyNoise 研判駭客的暴力破解工具初期可能在家用網路環境測試，或利用 VPN 隱匿行蹤。

### 新一代電腦使用介面 CoAct-1 結合 GUI 與程式碼操作

*   Salesforce、南加州大學與華盛頓大學合作發表 CoAct-1，一種結合 GUI 與程式碼操作的電腦使用介面。
*   在 OSWorld 基準測試中達成 60.76% 的成功率，刷新紀錄，並將平均完成任務步數降至約 11 步。
*   引入程式執行作為主要行動模式，提高長鏈任務與複雜操作的效率與穩定性。
*   採用多代理協作架構，包含 GUI Operator 與程式開發代理。
*   程式開發代理可直接在作業系統上撰寫並執行 Python 或 Bash 腳本，提高任務完成可靠性。

### SAP 更新漏洞 CVE-2025-27429 說明

*   SAP 在產品資安公告中更新了 S/4HANA 程式碼注入漏洞 CVE-2025-27429 的說明 (CVSS 9.9)。
*   Onapsis 透露，更新資訊添加在支援套件及修補程式的段落敘述中。

### Meta Threads 月活躍用戶突破 4 億

*   Meta 社交平臺 Threads 月活躍用戶數突破 4 億。
*   Threads 正迅速縮小與 X (Twitter) 的差距。
*   Threads 在今年 1 月開始測試廣告服務。

### 法國電信業者 Bouygues Telecom 用戶資料外洩

*   法國電信業者 Bouygues Telecom 遭網路攻擊，640 萬用戶資料外洩。
*   外洩資訊包含用戶聯絡資訊、合約、公民身份資料或企業用戶的公司資料，以及國際銀行帳號編號（IBAN）。
*   信用卡號及密碼不受影響。

### 美國執法單位與國際夥伴合作拆解 BlackSuit 勒索軟體基礎設施

*   美國國土安全調查局聯合多個執法單位與國際夥伴，成功拆解 BlackSuit 勒索軟體的關鍵基礎設施。
*   BlackSuit 被視為 Royal 勒索軟體的繼任者，兩者合計在美國鎖定超過 450 家受害機構，勒索金額估算約達 3.7 億美元。
*   此次行動查扣伺服器、網域與數位資產，並關閉勒索軟體部署、勒索及洗錢的基礎設施。

### AI 雲端運算業者 CoreWeave 第二季營收成長 200%

*   AI 雲端運算業者 CoreWeave 第二季營收 12.1 億美元，成長 200%，虧損 2.9 億美元。
*   CoreWeave 轉型為 AI 雲端平臺供應商後迅速成長，客戶包括微軟、OpenAI 及 Meta。
*   該公司正在迅速擴大規模，以滿足市場對 AI 的需求，並將成為全球首家大規模提供完整 Blackwell GPU 產品組合的公司。

### 安聯人壽 Salesforce 資料外洩，280 萬筆客戶資料遭公開

*   駭客公開竊自安聯人壽 Salesforce 系統的 280 萬筆客戶及合作夥伴資料。
*   攻擊者 ShinyHunters 疑似與 Scattered Spider 及 Lapsus$ 整合。
*   外洩資料包含姓名、地址、電子郵件、電話、生日、稅籍資料等。
*   ShinyHunters、Scattered Spider 去年遭國際警方執法破獲逮捕核心人物，促使二個組織合流。
### Windows 11 移除 PowerShell 2.0

微軟將於 8 月的 Windows 11 24H2 和 9 月的 Windows Server 2025 更新中移除 Windows 7 時代遺留的 PowerShell 2.0，以提升安全性。PowerShell 2.0 因架構老舊，缺乏現代安全防護措施，容易被濫用。企業若有舊程式使用 PowerShell 2.0 需及早升級至 PowerShell 5.1 或 7，或尋找替代方案。

### 紐約州檢察總長指控 Zelle 詐欺

紐約州檢察總長 Letitia James 指控 EWS 設計的 Zelle 缺乏安全功能，放任詐欺活動，導致受害者在 2017-2023 年間損失超過 10 億美元。Zelle 透過美國手機號碼或電子郵件識別收款人，註冊流程缺乏驗證，易被詐騙者冒用。紐約州檢察總長辦公室調查顯示 EWS 與合作銀行知情卻未有效行動，並虛假宣傳其安全性。

### Fortinet FortiSIEM 遠端命令注入漏洞

資安業者 Fortinet 發布公告，FortiSIEM 存在未經授權的遠端命令注入漏洞 (CVSS 9.8)，影響 5.4 至 7.3 版本。已有實際漏洞利用工具出現，可能被用於攻擊行動。建議用戶升級至 7.4 或限制 phMonitor 連接埠 (7900 埠) 的存取。

### 馬斯克與蘋果、OpenAI 爭端

馬斯克指控蘋果 App Store 偏私 ChatGPT，揚言控告，並與 OpenAI 執行長 Sam Altman 發生爭執。馬斯克認為蘋果拒絕將 X 或 Grok 列入「Must Have」類別違反反壟斷法。Altman 反擊指控馬斯克操弄 X 演算法偏私自己。蘋果否認指控，表示 App Store 排行榜由統計圖表、演算法推薦及專家根據公正標準遴選。

### Rust 1.89 版本更新

Rust 團隊釋出 1.89 版本，包含多項語言功能與編譯器更新，提升語法可讀性，調整平臺支援，最佳化跨平臺與硬體特性。主要亮點包括常數泛型引數開放使用底線符號 _ 進行自動推斷，新增 mismatched_lifetime_syntaxes 預設警告，擴充 x86 平臺目標功能設定，文件範例測試可跨平臺執行。x86_64-apple-darwin 從第一級支援降為第二級支援。

### 資安漏洞與攻擊事件

*   微軟 8 月例行更新修補 111 項漏洞，重大層級漏洞創今年新高，達 17 個。包含一個 Kerberos 零時差權限提升漏洞 CVE-2025-53779。
*   SAP 修補 15 項資安漏洞，包含兩個風險值 9.9 分的漏洞 CVE-2025-42950、CVE-2025-42957，影響 S/4HANA 和 SLT 系統，可被用於程式碼注入。
*   駭客針對 Fortinet SSL VPN 系統發動暴力破解攻擊，目標從防火牆作業系統 FortiOS 轉向網路管理平臺 FortiManager。
*   安聯人壽 Salesforce 系統遭駭，280 萬筆客戶及合作夥伴資料外洩，ShinyHunters 疑似與 Scattered Spider 及 Lapsus$ 整合。
*   法國電信業者 Bouygues Telecom 遭網路攻擊，640 萬用戶資料外洩，包含聯絡資訊、合約、公民身份資料、公司資料及 IBAN。

### Fortinet SSL VPN 暴力破解攻擊分析

GreyNoise 揭露針對 Fortinet SSL VPN 系統的暴力破解攻擊，第一波目標為 FortiOS 組態檔案，第二波轉向 FortiManager。攻擊者可能透過相同基礎設施或作案工具，向不同 Fortinet 裝置下手。

### CoAct-1 新一代電腦使用介面代理

Salesforce、南加州大學與華盛頓大學合作發表 CoAct-1，新一代電腦使用介面代理，在 OSWorld 基準測試中達成 60.76% 的成功率，創新點在於引入程式執行，以多代理協作架構進行任務分工，提高任務完成的可靠性。

### Threads 用戶數突破 4 億

Meta 社交平臺 Threads 用戶數再創新高，每月活躍用戶數突破 4 億，迅速縮小與 X 的差距。

### 美國拆解 BlackSuit 勒索軟體基礎設施

美國國土安全調查局聯合多個執法單位與國際夥伴，成功拆解 BlackSuit 勒索軟體的關鍵基礎設施。BlackSuit 被視為 Royal 勒索軟體的繼任者，自 2022 年起兩者合計已在美國鎖定超過 450 家已知受害機構，勒索金額估算約達 3.7 億美元。

### CoreWeave 第二季財報

AI 雲端運算業者 CoreWeave 第二季營收 12.1 億美元，成長 200%，虧損 2.9 億美元。盤後股價下跌 11.31%。
### Meta DINOv3 模型發布

Meta 宣布推出新一代自我監督式學習視覺模型 DINOv3，訓練規模達 17 億張影像，模型參數達 70 億。DINOv3 在語義分割、單一影像深度估測和影片追蹤等任務上表現超越前代及其他方案。Meta 已釋出商用授權的程式碼與預訓練骨幹模型，適用於邊緣運算和多任務部署，並已應用於環境監測，例如世界資源研究所使用 DINOv3 進行林冠高度估計，顯著降低誤差。Meta 提供多種規模的 DINOv3 骨幹，並附帶下游評估模型與範例 Notebook，方便開發者整合使用。

### 美國啟動開源多模態AI基礎設施加速科學計畫

美國國家科學基金會 (NSF) 與 Nvidia 合計資助 1.52 億美元，啟動「開源多模態 AI 基礎設施加速科學計畫」(OMAI)。該計畫由艾倫人工智慧研究所 (Ai2) 領導，旨在建立全國性開源多模態大型 AI 生態系統，加速科學發現並推進 AI 科學發展。OMAI 將開發可處理多種資料型態的多模態大型語言模型，並針對科學數據與文獻進行訓練，初期應用包括加速新材料發現、提升蛋白質功能預測精度，並改善當前大型語言模型的核心缺陷。所有模型、資料、程式碼、評測與文件都將向全球研究人員開放。

### Google Flights 推出 AI 驅動的 Flight Deals 功能

Google Flights 新推出 AI 驅動的 Flight Deals 功能，使用者可以自然語言描述旅行時間、地點和方式，Flight Deals 會找到最實惠的交易。該功能透過 AI 系統理解使用者需求，並利用 Google Flights 的即時資料，顯示來自數百家航空公司及預訂網站的選擇。Flight Deals 目前為測試版，預計下周進駐美國、加拿大及印度市場。

### 加拿大眾議院遭駭客入侵

加拿大眾議院疑似遭駭客透過微軟近日漏洞入侵系統，導致「重大」資訊外洩。駭客經由微軟漏洞未經授權存取了儲存員工電腦和行動裝置管理資訊的資料庫，可能外洩的資訊包括員工姓名、職稱、辦公室位置、電子郵件，以及列管的電腦和行動裝置資訊。加拿大官方未透露是哪種微軟漏洞被濫用，但從外洩資料性質來看，受駭的可能是 SharePoint Server。

### 資安事件與漏洞分析

*   **Curly COMrades 駭客組織：** Bitdefender 追蹤俄羅斯駭客組織 Curly COMrades，該組織針對喬治亞和摩爾多瓦的司法、政府機構及能源分配公司下手，植入 MucorAgent 後門程式，並濫用 Windows 內建的 NGEN 元件，建立持續存取的管道。
*   **Zelle 詐欺問題：** 紐約州檢察總長控告 P2P 數位支付平臺 Zelle 缺乏關鍵安全功能，放任詐欺活動，導致受害者損失超過 10 億美元。
*   **全錄 FreeFlow Core 漏洞：** 全錄列印流程自動化軟體 FreeFlow Core 存在 XXE 導致的 SSRF 漏洞 CVE-2025-8355，以及 RCE 路徑穿越漏洞 CVE-2025-8356，資安業者 Horizon3.ai 警告這些漏洞已被用於實際攻擊行動。
*   **NIST 發布 Ascon 輕量級加密標準：** 美國國家標準技術研究所 (NIST) 正式發布 SP 800-232 文件，針對物聯網等資源受限裝置提供 Ascon 輕量級加密標準，涵蓋 ASCON-128 AEAD、ASCON-Hash 256、ASCON-XOF 128 與 ASCON-CXOF 128 四種變體。
*   **微軟移除 PowerShell 2.0：** 微軟將從 Windows 11 24H2 及 Windows Server 2025 更新中移除 Windows 7 時代遺留下來的 PowerShell 2.0，以提升 Windows 環境的安全性。
*   **PyPI 強化上傳審核：** Python 官方套件庫 PyPI 宣布強化上傳審核流程，目標是封鎖利用 ZIP 解析差異的混淆攻擊。
*   **BlackSuit 勒索軟體基礎設施被拆解：** 美國國土安全調查局 (HSI) 聯合多個執法單位與國際夥伴，成功拆解 BlackSuit 勒索軟體的關鍵基礎設施。
*   **Gemma 3 270M 模型發布：** Google 推出 Gemma 系列中最輕量的版本 Gemma 3 270M，專為特定任務微調與裝置端部署設計，支援開發者針對分類、資料抽取、情緒分析等應用進行客製化。

### 全錄 FreeFlow Core 漏洞再次被強調

資安業者針對全錄 (Xerox) 印表機相關漏洞進行調查，並指出這些漏洞已被用於實際攻擊行動，用戶要儘速處理。全錄 FreeFlow Core 存在 XXE 導致的 SSRF 漏洞 CVE-2025-8355，以及 RCE 路徑穿越漏洞 CVE-2025-8356，Horizon3.ai 警告這些漏洞不僅能讓未經授權的攻擊者發動 RCE 攻擊，還相當容易利用。

### HTTP/2 MadeYouReset 漏洞

HTTP/2 存在 MadeYouReset 漏洞 (CVE-2025-8671)，可使攻擊者繞過 HTTP/2 的防護機制，發動大規模系統阻斷服務 (DoS) 攻擊，甚至系統崩潰。Apache Tomcat、F5 BIG-IP 和 Netty 等產品受到影響，相關廠商已釋出更新軟體或修補程式。

### APT 駭客使用寄生攻擊

資安業者追蹤長達一年的俄羅斯駭客組織 Curly COMrades，他們利用公開工具或受害電腦現成工具進行寄生攻擊 (LOLBin)，鎖定喬治亞和摩爾多瓦等國家的政府機構及能源公司，並植入 MucorAgent 後門程式。

### 美國政府考慮入股英特爾

《華爾街日報》、《金融時報》與彭博社報導，美國政府正在討論是否入股英特爾 (Intel)，以支持其晶圓代工服務 (IFS) 事業群。

### 蘋果 Apple Watch 血氧量測功能回歸

蘋果將為部份機種 Apple Watch 提供重新設計的血氧量測功能，透過軟體更新提供給美國銷售的部份 Apple Watch 9、10 和 Ultra 2，量測結果將在配對的 iPhone Health App 上顯示。

### NGINX 原生支援 ACME 協定

NGINX 原生支援 ACME (Automatic Certificate Management Environment) 協定，系統管理員可直接在設定檔中完成 TLS 憑證的申請與自動更新，無需額外安裝 Certbot 等外部工具。

### PoisonSeed 網釣套件分析

資安公司 Nviso 發布對駭客組織 PoisonSeed 使用的網釣套件進行技術分析，該工具具備繞過多因素驗證 (MFA) 的能力，主要目標包括 Google、SendGrid 與 Mailchimp 等郵件服務。

### NIST 正式發布 Ascon 輕量級加密標準

美國國家標準技術研究所 (NIST) 正式發布 SP 800-232 文件，針對物聯網等資源受限裝置提供 Ascon 輕量級加密標準。

### ShinyHunters 和 Scattered Spider 合作關係

資安業者 ReliaQuest 揭露駭客組織 ShinyHunters 與 Scattered Spider 合作，對多個領域採用 Salesforce 的知名企業發動攻擊，相關合作可追溯到 2024 年 7 月。

### 其他資安事件

*   **Docker 映像檔遭 XZ Utils 後門入侵：** 資安業者發現有 Docker 映像檔遭到 XZ Utils 後門入侵。
*   **OTP 漏洞 CVE-2025-32433 攻擊行動：** Palo Alto Networks 指出，開放電信平臺 (OTP) 的滿分漏洞 CVE-2025-32433 已遭到利用，約有七成的攻擊鎖定保護操作科技 (OT) 環境的防火牆而來。
*   **FortiSIEM 漏洞 CVE-2025-25256：** 資安廠商 Fortinet 發布公告，指出 FortiSIEM 存在高風險漏洞 CVE-2025-25256，而且已有實際的漏洞利用程式碼出現。
*   **Nvidia Triton 推論伺服器漏洞：** Nvidia 發布 Triton 推論伺服器與 Python 後端安全更新，修補高風險漏洞，允許未經驗證的遠端攻擊者取得伺服器的遠端程式碼執行權限。
*   **Windows 365 Reserve 服務：** 微軟公布 Windows 365 Reserve 服務，提供電腦故障的員工快速連上 Windows 雲端繼續作業。
### Google搜尋AI模式擴展及新功能實驗

*   Google將AI模式拓展至全球180多個國家，但目前僅支援英文。
*   AI模式基於Gemini 2.5模型，支援深度搜尋、複雜查詢、多模態輸入及聊天互動。
*   美國市場推出分享/協作功能，方便使用者共同編輯和討論AI模式的回應。
*   美國推出代理功能，AI可替使用者執行複雜任務，如餐廳訂位。
*   個人化功能利用使用者先前的對話紀錄和活動，提供個人化的搜尋結果，目前僅限美國市場的Labs實驗功能使用。

### Mozilla Firefox 142 安全更新

*   Mozilla發布Firefox 142，修復多項安全漏洞，包括5個高風險漏洞。
*   高風險漏洞包括Audio/Video GMP元件的無效指標（CVE-2025-9179）、Canvas 2D元件的同源政策繞過（CVE-2025-9180）以及多個記憶體安全漏洞（CVE-2025-9184、CVE-2025-9185、CVE-2025-9187）。
*   同時發布Firefox of iOS 142，修復一項高風險漏洞（CVE-2025-55030）及2個中度風險漏洞。

### 資安威脅與漏洞警報

*   駭客利用臉書粉絲頁版權爭議散布竊資軟體，手法更精進，借助AI翻譯並蒐集目標資訊。
*   FBI警告俄羅斯駭客濫用Cisco Smart Install軟體7年前的漏洞CVE-2018-0171攻擊全球基礎架構。
*   資安研究員發現Intel內部網站存在漏洞，可能導致27萬員工資料外洩，已完成修補。
*   研究人員公布能透過Windows修復環境繞過BitLocker保護的漏洞BitUnlocker，微軟已發布修補程式。
*   竊資軟體Noodlophile Stealer透過違反著作權網釣散布，針對亞太、歐美等地，利用Telegram作為C2。

### Google安卓虛擬機管理程式pKVM獲SESIP 5級認證

*   Google的安卓虛擬機管理程式pKVM取得SESIP 5級認證，為大規模消費性電子裝置部署的首例。
*   此認證為關鍵性隔離工作負載建立更可驗證的安全基礎，涵蓋裝置上人工智慧工作負載與敏感資料處理等應用情境。

### Intel內部網站漏洞細節

*   資安研究員Eaton Zveare揭露Intel內部網站存在多個漏洞，可能導致27萬員工資料外洩。
*   漏洞包括Intel India Operations名片訂購網站未經身分驗證即可存取，Product Hierarchy網站寫死帳密可下載員工資料，以及繞過SEIMS Supplier Site登入介面。

### Google Gemini for Government產品及OneGov合作協議

*   Google推出Gemini for Government產品，並與美國總務管理局（GSA）簽署OneGov合作協議。
*   美國聯邦機構可以每年0.47美元的價格訂閱Gemini for Government，有效期限至2026年。
*   OneGov旨在統一聯邦政府機構的採購模式，以市售產品及服務取代客製化服務。

### TRM Labs推出Beacon Network加密貨幣犯罪應對網路

*   TRM Labs推出Beacon Network，串連執法機構、加密貨幣交易平臺、支付公司及資安研究人員。
*   Beacon Network旨在建立即時預警網絡，在非法資金被套現或轉為法幣之前攔截。
*   創始成員包括Coinbase、Binance、PayPal、Robinhood、Stripe、Kraken、Ripple、Crypto.com等數十家業者。

### 各大零售業巨頭GenAI應用

*   **Walmart：** 採用適應式零售戰略，利用GenAI強化顧客體驗、供應鏈管理、生產力，加速數據處理和IT開發。
*   **Amazon：** 廣泛將GenAI應用於物流、顧客體驗、賣家體驗與RMN，並推出AI購物助理Rufus、AI交通指揮官Deepfleet等創新應用。
*   **Target：** 遵循由內而外的模式，先從內部資料整理，再應用於員工，最後才推出面向顧客的系統，例如GenAI店員助手Store Companion和購物助手Shopping Assistant。
*   **eBay：** 利用GenAI打造新的商品探索體驗Shop the Look，強化商品上架技術，應用於顧客體驗、RMN廣告等領域。
*   **Lowe's：** 推出Mylow生成式AI購物助理，提供家居領域的專業知識輔助，幫助顧客解決問題或完成特定作業，並提升員工AI素養。

### Anthropic 推出企業及團隊方案更新

*   Anthropic 為企業及團隊方案新增 Premium 授權名額，允許在同一訂閱中使用 Claude 和 Claude Code。
*   推出 Compliance API，協助企業即時監管使用狀況並滿足法遵需求。
*   強化使用分析，讓管理者掌握 Claude Code 的實際成效。
*   管理員可統一配置工具權限、檔案存取限制等。

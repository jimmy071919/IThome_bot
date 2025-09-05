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
## Google 資訊總結

*   **AI 模式全球擴展：** Google 將搜尋中的 AI 模式推廣至包含臺灣在內的 180 多個國家，但目前僅支援英文。
*   **AI 模式功能：**
    *   基於 Gemini 2.5 模型，具備強大的推理和多模態處理能力。
    *   支援深度搜尋、複雜查詢、後續問題追問，以及文字、語音、圖片等多種輸入方式。
    *   提供聊天式互動體驗，可接管搜尋並處理複雜問題。
*   **美國市場新功能：**
    *   **協作功能：** AI 模式用戶可分享回應連結，邀請他人協作。
    *   **代理功能：** AI 可替用戶執行複雜任務，例如餐廳訂位（目前僅限美國 Google AI Ultra 付費用戶，Labs 實驗功能）。
    *   **個人化功能：** 根據用戶先前的對話紀錄和搜尋活動提供個人化結果（目前僅限美國市場，Labs 實驗功能，專注於餐飲相關主題）。
*   **未來計畫：** Google 計畫推出本地服務預約、活動票券訂購等功能，可能延伸至旅行規劃、購物、醫療等生活服務。

## Mozilla 資訊總結

*   **Firefox 142 安全更新：** Mozilla 發布 Firefox 142 桌機版本，修復多項安全問題，包含 5 個高風險漏洞。
    *   **高風險漏洞：**
        *   CVE-2025-9179：Audio/Video GMP 元件存在無效指標，可能導致沙箱逃逸。
        *   CVE-2025-9180：Graphics: Canvas 2D 元件中的同源政策繞過漏洞，危及跨站安全性。
        *   CVE-2025-9184、CVE-2025-9185、CVE-2025-9187：記憶體安全漏洞，可能允許執行任意程式碼。
    *   **中度風險漏洞：** CVE-2025-9181：JavaScript 引擎元件的非初始化記憶體漏洞。
    *   **低風險漏洞：**
        *   CVE-2025-9186：Firefox Focus for Android 的網址列元件身份冒用漏洞。
        *   CVE-2025-9182：Graphics: WebRender 元件的服務阻斷漏洞。
*   **Firefox of iOS 142 安全更新：**
    *   **高風險漏洞：** CVE-2025-55030，可導致瀏覽器錯誤地將附件內容直接嵌入頁面顯示，可能被利用進行跨站腳本攻擊 (XSS)。
    *   **中度風險漏洞：**
        *   CVE-2025-55028：JavaScript 可觸發重複發送通知造成服務中斷。
        *   CVE-2025-55031：允許在藍牙連線範圍的攻擊者發送釣魚訊息騙取通行密鑰。
    *   **低度風險漏洞：** CVE-2025-55029，類似 CVE-2025-55028，但以觸發垃圾 popup 視窗造成 DoS。
*   **受影響版本：** 部分漏洞影響 Firefox ESR、Thunderbird ESR 及 Firefox/Thunderbird 142/115.27 版本。

## 資安威脅與漏洞資訊總結

*   **臉書粉絲頁版權爭議網釣攻擊：** 駭客利用 AI 精進網釣手法，針對企業臉書粉絲頁，以違反著作權為誘餌散布竊資軟體 Noodlophile Stealer。
    *   駭客手法：
        *   廣泛偵察並在信中列出臉書網頁 ID 和公司所有權等資訊。
        *   使用 AI 將信件內容翻譯成特定語言。
        *   透過 Gmail 寄送，挾帶偽裝成侵權證據的 PDF 檔案連結。
        *   利用 Haihaisoft PDF Reader 或其他存在弱點的應用程式，以 DLL 側載手法傳遞惡意酬載。
        *   利用 Telegram 架設 C2，並從 Telegram 群組簡介取得有效酬載 URL。
    *   Noodlophile Stealer 功能：迴避 AMSI、ETW，可能躲過 EDR 偵測，並積極開發螢幕截圖擷取、鍵盤偵錄、檔案外洩等功能。
*   **FBI 警告：俄羅斯駭客濫用思科漏洞：** 俄羅斯駭客 (FSB Center 16) 濫用思科 Cisco Smart Install 軟體的舊式網路設備漏洞 CVE-2018-0171 及 SNMP 攻擊全球公部門及企業基礎架構。
    *   CVE-2018-0171：Smart Install 功能的堆疊式緩衝溢位漏洞，可造成 DoS 或任意程式碼執行攻擊。
    *   駭客行為：蒐集思科網路裝置配置檔，修改配置檔以允許非授權存取，偵查網路，曝露工控系統相關協定和應用。
*   **英特爾內部網站漏洞：** 資安研究員發現英特爾內部網站存在弱點，可能導致 27 萬員工的敏感資訊外流。
    *   漏洞類型：
        *   竄改 JavaScript 檔案，未經身分驗證即可存取 Intel India Operations 的名片訂購網站，下載全公司員工資料。
        *   輕易解密寫死的帳密，從 Product Hierarchy 和 Product Onboarding 網站下載所有員工資料。
        *   繞過 SEIMS Supplier Site 的合作廠商登入介面，下載每個英特爾員工的詳細資料，並可能取得完整系統存取權限。
    *   英特爾回應：已完成修補，並持續評估和加強安全措施。
*   **BitLocker 繞過漏洞：** 研究人員公布能透過 Windows 修復環境 (WinRE) 截取 BitLocker 機敏資訊的弱點 BitUnlocker。
    *   漏洞編號：CVE-2025-48800、CVE-2025-48003、CVE-2025-48804、CVE-2025-48818，CVSS 風險評分皆為 6.8。
    *   攻擊方式：實際接觸目標電腦，重開機進入 WinRE 來觸發漏洞，無須登入電腦。
    *   微軟已於 7 月例行更新發布修補程式。

## Android pKVM 資訊總結

*   **Google pKVM 取得 SESIP 5 級認證：** Google 公開其安卓虛擬機管理程式 pKVM (Protected Kernel-based Virtual Machine) 已取得 SESIP 5 級認證。
*   **重要性：**
    *   這是第一個針對大規模消費性電子裝置部署，且通過此等級的軟體安全系統。
    *   為關鍵性隔離工作負載建立更可驗證的安全基礎，涵蓋裝置上人工智慧工作負載與敏感資料處理等應用情境。
    *   提供供應鏈法遵與市場信任的強力保障。
    *   降低開發者在敏感場景導入隔離執行環境的不確定性。

## 零售業生成式 AI 應用資訊總結

*   **零售業應用趨勢：** 生成式 AI 已成全球零售業巨頭融入實務的重要技術，支援購物體驗、內部營運、供應鏈管理等各式環節。
    *   應用方向：強化購物體驗、優化內部營運。
    *   常見模式：商品資訊處理、搜尋機制強化、第一線員工知識管理、特定商品分類或購物情境的 AI 助手。
*   **主要零售商應用案例：**
    *   **Walmart：** 大規模導入生成式 AI，強化 OMO 零售，強調「適應式零售」，利用 AI/ML 分析顧客喜好，生成對應零售體驗。
    *   **Amazon：** 廣泛導入 GenAI 到買家與賣家體驗、物流及 RMN。
    *   **Target：** 從內部資料整理開始，逐步走向員工應用，最後面向顧客，著重自有品牌推銷。
    *   **eBay：** 利用生成式 AI 提升商品資料品質，改善搜尋、推薦、行銷及整體購物體驗。
    *   **Lowe's：** 應用生成式 AI 降低家居領域服務及購物所需知識門檻，加速零售營運作業，提供家居知識問答，用於商品搜尋與推薦、裝潢建議、DIY 教學等。
*   **臺灣零售業建議：** 應結合臺灣獨特環境考量，找出自身應跟進的做法。
* **企業應用案例分析:**

    * **Walmart:**

        *  1. 適應式零售戰略: 全面升級技術力，強化顧客個人化零售體驗。
        * 2. GenAI應用實驗沙盒: 技術人員可自由探索應用，非技術人員提供 No-code 開發工具。
        * 3. 多LLM調度機制: 不同場景發揮模型特長，Wallaby系列LLM用於生成符合Walmart特性的內容。
        * 4. 顧客體驗優化: Ghotok智慧商品分類與搜尋、Sparky聊天機器人提供個人化購物建議、GenAI自動產生專屬電商入口網頁。
        * 5. 物流強化: AI地理空間平臺、AI主動管理倉儲與運輸系統、AI監控智慧攝影機與物流效能。
        * 6. AI助理: Wally（第三方市集商家用）、門市員工用的AI代理。
        * 7. 產品開發加速: Trend-to-Product縮短新成衣產品開發週期。
        * 8. 內勤生產力提升: SuperApp和My Assistant。
        * 9. 程式碼撰寫加速: 程式碼撰寫助手節省開發時間、AI代理負責舊程式碼新增功能、Pipeline Visualizer檢查程式碼。

    * **Amazon:**

        * 1. Project P.I.  商品瑕疵辨認系統: 在物流中心出貨前，識別受損或不符訂單規格的商品。
        * 2. Wellspring導航系統: 精準識別郵箱、車位和入口等具體位置，改善配送精準度。
        * 3.Deepfleet AI交通指揮官: 強化物流中心內機器人調度
        * 4. Rufus AI購物助理: 搜尋、比較商品價格及規格、回答商品相關問題及其他模糊問題、根據顧客過往資料給出個人化答覆
        * 5. Interests個人化商品推薦： 顧客自行設定追蹤任務，自動持續探索最新上架商品。
        * 6. Buy for me: 利用代理式AI技術，替顧客將加密過的姓名、地址、付款資料等資訊提供給外部品牌網站，來代為購物。
        * 7.  商家助理Project Amelia： 訓練資料包含自家零售營運知識，可回答複雜問題，協助賣家。

    * **Target:**

        * 1.GenAI維護商品資訊: 利用GenAI來總結顧客評論、寫商品描述，並將商品標題改得更明確、具體，以利顧客搜尋
        * 2.Store Companion 門市員工助手：此助手用門市常見問題及門市管理流程文件訓練而成，旨在回答門市內部流程問題、協助新員工培訓，並支援日常門市管理作業的即時問答
        * 3.GenAI 購物助手： Bullseye Gift Finder購物助手鎖定了兒童送禮場景、Shopping Assistant聊天機器人進行Target自有品牌商品的搜尋及問答

    * **eBay:**

        * 1. 強化圖像AI商品資料品質
        * 2. 二代商品輔助上架功能： 結合eBay站上的分類邏輯及後臺商品資料庫，自動生成商品標題、描述、生產日期、分類、建議售價、建議運費等資訊
        * 3. 互動式服飾購物體驗「Shop the Look」： 分析顧客購物歷史分析可能喜好，再生成一系列穿搭範例圖，可點擊圖片元件找商品
        * 4.AI代理購物： 與OpenAI合作，開放後者的AI代理Operator能推薦eBay商品，甚至直接代為購買商品

    * **Lowe's:**

        * 1.AI平台 串聯Nvidia、OpenAI、Palantir等外部廠商技術，並設立標準化AI與生成式AI應用開發流程
        * 2.Lowe's Product Expert 微調過的ChatGPT，以對話形式提供居家DIY建議與商品推薦。
        * 3.Mylow Companion店員助手： 用於提升客戶服務及加速新店員入職訓練
        * 4.Mylow 顧客GenAI助理：提供商品搜尋與推薦、裝潢建議、DIY教學、Lowe's服務推薦

## Anthropic 資訊總結

*   **Anthropic 推出 Claude Code 與 Compliance API：** Anthropic 為其企業（Enterprise）與團隊（Team）方案新增 Premium 授權名額，允許在同一訂閱中使用 Claude 與 Claude Code，並推出 Compliance API，協助企業監管使用狀況並滿足法遵需求。
*   **Premium 授權：**
    *   管理員可依組織角色分配標準或 Premium 名額。
    *   Premium 使用者可在 Claude 進行技術探索，再切換至 Claude Code 完成可部署的程式碼。
    *   團隊需要額外資源時，可開啟額外用量，以標準 API 費率計算，並可設定組織與個人層級的上限。
*   **監測與治理：**
    *   提供完整的使用分析，包括程式碼行數、建議採納率與使用模式等。
    *   強化政策設定，管理員可統一配置工具權限、檔案存取限制與 MCP 伺服器設定。
*   **Compliance API：**
    *   企業可透過程式化介面即時存取 Claude 的使用資料與內容，建置持續監測與自動化政策執行。
    *   支援將相關資訊整合至既有的法遵儀表板，並支援選擇性刪除。

## TRM Labs Beacon Network 資訊總結

*   **TRM Labs 推出 Beacon Network：** 區塊鏈情報業者 TRM Labs 推出 Beacon Network，為即時的加密貨幣犯罪應對網路。
*   **參與者：** 串連了執法機構、加密貨幣交易平臺、支付公司及資安研究人員。創始成員包括 Coinbase、Binance、PayPal、Robinhood、Stripe、Kraken、Ripple、Crypto.com 及 Blockchain.com 等數十家業者。
*   **目標：** 在非法資金被套現或轉為法幣之前進行攔截。
*   **運作方式：**
    *   執法機構或資安業者標記可疑錢包位址。
    *   Beacon 自動追蹤資金流出。
    *   資金到達合作平臺時觸發即時警報。
    *   加密貨幣平臺主動審查並保留被標記的存款，以阻止非法提現。
## Google AI 模式拓展至全球

*   Google將搜尋中的AI模式拓展至包含臺灣在內的180多個國家，目前僅支援英文。
*   在美國市場推出協作功能，並實驗代理（Agentic）及個人化功能。
*   AI模式基於Gemini 2.5模型，支援深度搜尋、複雜查詢、多模態輸入。
*   相較於AI Overview，AI模式提供聊天式互動體驗，能處理更複雜問題。
*   美國AI模式用戶可使用分享/協作功能，產生連結邀請他人協作。
*   代理功能讓AI可替使用者執行複雜任務，如餐廳訂位，目前僅限美國Google AI Ultra付費訂閱用戶。
*   未來計畫推出本地服務預約或活動票券訂購。
*   個人化功能利用使用者對話紀錄及搜尋活動推斷偏好，提供個人化餐飲建議，目前僅限美國市場。

## Mozilla Firefox 安全更新

*   Mozilla釋出Firefox 142桌機版本，解決多項安全問題，包含5個高風險漏洞。
*   修補了CVE-2025-9179至CVE-2025-9187等8項漏洞。
*   高風險漏洞包括：
    *   CVE-2025-9179：Audio/Video GMP元件存在無效指標，可能導致沙箱逃逸。
    *   CVE-2025-9180：Graphics: Canvas 2D元件中的同源政策繞過漏洞，危及跨站安全性。
    *   CVE-2025-9184、CVE-2025-9185、CVE-2025-9187：記憶體安全漏洞，可能允許執行任意程式碼。
*   中度風險漏洞：
    *   CVE-2025-9181：JavaScript引擎元件的非初始化記憶體漏洞。
*   低風險漏洞：
    *   CVE-2025-9186：Firefox Focus for Android的網址列元件身份冒用漏洞。
    *   CVE-2025-9182：Graphics: WebRender元件的服務阻斷漏洞。
*   同時發布Firefox of iOS 142，修補一項高風險漏洞及2個中度風險漏洞。
    *   CVE-2025-55030：高風險漏洞，可能導致跨站腳本攻擊。
    *   中度風險漏洞：CVE-2025-55028(JavaScript可觸發重覆發送通知造成服務中斷)、CVE-2025-55031(允許在藍牙連線範圍的攻擊者發送釣魚訊息騙取通行密鑰)。

## 資安事件與漏洞警報

*   **臉書粉絲頁版權爭議網釣攻擊手法升級：**
    *   駭客利用臉書粉絲頁版權爭議為誘餌散布惡意程式。
    *   借助AI翻譯信件內容，並搭配事前偵察，攻擊更難防範。
    *   透過Gmail寄送，挾帶偽裝成侵權證據的PDF檔案連結，利用DLL側載傳遞惡意酬載。
*   **FBI警告俄羅斯駭客濫用思科產品舊漏洞：**
    *   俄羅斯駭客濫用思科Cisco Smart Install軟體7年前的漏洞CVE-2018-0171及SNMP攻擊全球公部門及企業。
    *   FBI偵測到駭客蒐集美國多個基礎架構產業的思科網路裝置配置檔，可能用於偵查網路或修改配置檔進行未授權存取。
*   **英特爾內部網站存在漏洞：**
    *   資安研究員Eaton Zveare指出英特爾內部網站存在弱點，可能導致27萬員工資料外洩。
    *   英特爾已完成修補，但研究員未獲漏洞懸賞獎勵。
    *   最嚴重的漏洞出現在英特爾印度分公司的名片訂購網站，可未經身分驗證存取全公司員工資料。
    *   其他漏洞包括Product Hierarchy和Product Onboarding網站的寫死帳密，以及繞過SEIMS Supplier Site合作廠商登入介面的漏洞。
*   **BitLocker 繞過漏洞 (BitUnlocker)：**
    *   研究人員公布能透過系統復原機制繞過BitLocker的弱點。
    *   微軟已於7月發布修補程式，漏洞編號CVE-2025-48800、CVE-2025-48003、CVE-2025-48804、CVE-2025-48818。
*   **Noodlophile Stealer竊資軟體攻擊：**
    *   駭客透過違反著作權網釣散布Noodlophile Stealer竊資軟體，範圍遍及亞太、美國、歐洲、波羅的海國家。
    *   借助AI翻譯，並利用Haihaisoft PDF Reader DLL側載，躲避資安系統攔截。
    *   使用Recursive Stub Loading或Chained DLL Vulnerabilities手法載入惡意酬載。
    *   從Telegram群組獲取有效酬載URL，並利用Telegram架設C2。

## Google pKVM 取得 SESIP 5 級認證

*   Google的安卓虛擬機管理程式pKVM取得SESIP 5級認證，是首個大規模消費性電子裝置部署通過此等級的軟體安全系統。
*   為關鍵性隔離工作負載建立可驗證的安全基礎，涵蓋裝置上人工智慧工作負載與敏感資料處理等應用情境。
*   提供供應鏈法遵與市場信任的保障。

## 美國聯邦機構AI 採購

*   Google 推出 Gemini for Government，並與美國總務管理局簽署 OneGov 合作協議。
*   聯邦機構可以每年 0.47 美元的價格訂閱 Gemini for Government 至 2026 年。
*   Gemini for Government 是完整的人工智慧平台，包含企業搜尋、影片與圖片生成功能、 NotebookLM 工具、 Deep Research 及 Idea Generation 的 AI 助理。
*   遵循川普政府的 OneGov 策略，以市售產品取代客製化服務。

## TRM Labs 推出 Beacon Network 加密貨幣犯罪應對網路

*   TRM Labs 推出 Beacon Network，串連執法機構、加密貨幣交易平台、支付公司及資安研究人員。
*   目的是在非法資金被套現或轉為法幣之前就進行攔截。
*   Coinbase、Binance、PayPal、Robinhood、Stripe、Kraken、Ripple、Crypto.com 及 Blockchain.com 等數十家業者為創始成員。

## 零售業巨頭導入生成式 AI 應用

*   全球零售業巨頭將生成式 AI 融入實務，支援購物體驗、內部營運、供應鏈管理等環節。
*   應用方向包括：
    *   **改善購物體驗：** Walmart 的 Sparky 聊天機器人、 Lowe's 的 Mylow 居家購物助理、 eBay 的 Shop the Look 穿搭推薦。
    *   **優化供應鏈管理：** Walmart 利用 AI 地理空間平台優化物流資源調度、 Amazon 的 Project P.I. 辨認瑕疵商品。
    *   **提升內部生產力：** Walmart 的超級 App 內建多種生成式 AI 功能、 Target 的 Store Companion 店員助手。
    *   **加強商品資訊處理：** Target 利用 GenAI 總結顧客評論、 Walmart 利用 AI 驅動的商品屬性驗證機制。
    *   **推動數位行銷：** eBay 用 AI 生成數以百萬計的個人化電子郵件標題和預覽文字、 Amazon 將 AI 與自家串流服務結合推出 AI 生成串流廣告。

## Anthropic 推出 Claude Code

*   Anthropic 為 Claude 推出 Claude Code，並新增可升級的 Premium 授權名額，讓用戶在同一訂閱中同時使用 Claude 與 Claude Code。
*   同時推出 Compliance API，協助企業即時監管使用狀況並滿足法遵需求。
*   Premium 使用者可先透過 Claude 進行技術探索與架構討論，再切換到終端機內的 Claude Code 撰寫並完成可直接部署的程式碼。
*   系統提供更完整的使用分析，包括被採納的程式碼行數、建議採納率與使用模式等，讓管理者能更具體掌握 Claude Code 在團隊內的實際成效。
*   管理員可統一配置工具權限、檔案存取限制與 MCP 伺服器設定，將內部規範直接落實到使用端。### Google搜尋AI模式擴展及新功能實驗

*   **AI模式全球擴展：** Google將搜尋中的AI模式推廣至包括臺灣在內的180多個國家，但目前僅支援英文。
*   **AI模式功能：** 基於Gemini 2.5模型，提供深度搜尋、複雜查詢、後續追問，並支援文字、語音、圖片等多種輸入。
*   **與AI Overview比較：** AI模式提供聊天式互動，能處理更複雜問題，與AI Overview的一次性摘要回答不同。
*   **協作功能：** 美國用戶可使用分享功能，生成連結邀請他人協作。
*   **代理（Agentic）功能：** AI可替使用者執行複雜任務，如餐廳訂位，目前僅限美國Google AI Ultra付費用戶。
*   **個人化功能：** 僅限美國市場，利用使用者對話紀錄和搜尋活動提供個人化結果，初期專注餐飲相關主題。

### Mozilla Firefox安全更新及漏洞修補

*   **Firefox 142版本更新：** 修復多項安全問題，包括5個高風險漏洞。
*   **高風險漏洞：**
    *   CVE-2025-9179：Audio/Video GMP元件存在無效指標，導致記憶體毁損及沙箱逃逸。
    *   CVE-2025-9180：Graphics: Canvas 2D元件中的同源政策繞過漏洞，危及跨站安全性。
    *   CVE-2025-9184, CVE-2025-9185, CVE-2025-9187：記憶體安全漏洞，允許執行任意程式碼。
*   **中度風險漏洞：** CVE-2025-9181：JavaScript引擎元件的非初始化記憶體漏洞。
*   **低風險漏洞：** CVE-2025-9186（Android Firefox Focus身份冒用）及CVE-2025-9182（WebRender元件阻斷服務）。
*   **Firefox of iOS 142：** 修復一項高風險漏洞（CVE-2025-55030）及兩個中度風險漏洞（CVE-2025-55028, CVE-2025-55031）。

### 資安威脅與漏洞警報

*   **臉書粉絲頁版權爭議網釣：** 駭客利用AI精進網釣手法，偽稱違反著作權散布竊資軟體。
*   **FBI警告俄羅斯駭客攻擊：** 俄羅斯駭客濫用思科產品7年前的漏洞CVE-2018-0171攻擊全球基礎架構。
*   **英特爾內部網站漏洞：** 資安人員發現英特爾內部網站存在弱點，可能導致員工資料外洩，已修補。

### BitLocker繞過漏洞

*   **BitUnlocker漏洞：** 研究人員公布能透過Windows修復環境繞過BitLocker資料保護措施的弱點。
*   **漏洞編號：** CVE-2025-48800、CVE-2025-48003、CVE-2025-48804、CVE-2025-48818，CVSS風險評分皆為6.8。
*   **修補程式：** 微軟已於7月發布修補程式。

### Google安卓虛擬機管理程式pKVM獲SESIP 5級認證

*   **pKVM認證：** Google的安卓虛擬機管理程式pKVM取得SESIP 5級認證。
*   **目的：** 為關鍵性隔離工作負載建立更安全基礎，涵蓋裝置上人工智慧工作負載與敏感資料處理。

### 英特爾內部網站漏洞詳情

*   **Eaton Zveare發現漏洞：** 外部攻擊者可藉由竄改特定的JavaScript檔案，在未經身分驗證的情況下存取應用系統並下載員工資料。

### Noodlophile Stealer竊資軟體攻擊手法

*   **攻擊目標：** 遍及亞太地區、美國、歐洲、波羅的海國家。
*   **散布方式：** 透過違反著作權網釣，借助AI翻譯信件內容。
*   **技術細節：** 使用DLL側載、Recursive Stub Loading、Chained DLL Vulnerabilities等手法。
*   **C2架設：** 利用Telegram架設C2。
*   **功能：** 以.NET打造，具備螢幕截圖擷取、鍵盤偵錄、檔案外洩等功能。

### Google Gemini for Government及OneGov合作協議

*   **Gemini for Government：** 包含企業搜尋、影片與圖片生成功能等的人工智慧平臺。
*   **OneGov合作協議：** 美國聯邦機構以每年0.47美元的價格訂閱，至2026年。
*   **目的：** 統一聯邦政府機構的採購模式，降低建置成本。

### 思科Smart Install漏洞CVE-2018-0171

*   **漏洞描述：** 位於IOS及IOS XE中的Smart Install功能，未對輸入封包資料做必要驗證，可引發阻斷服務或任意程式碼執行攻擊。
*   **駭客組織：** FSB Center 16 (Berserk Bear, Dragonfly, Static Tundra)。

### 零售業生成式AI應用

*   **應用方向：** 購物體驗、內部營運、供應鏈管理。
*   **常見模式：** 適應式零售、AI購物助理、強化搜尋、供應鏈優化、客戶服務。
*   **重點案例：** Walmart、Amazon、Target、eBay、Lowe's。

### Lowe's生成式AI應用

*   **Mylow Companion：** 內部店員用助手，結合RAG技術，提供客戶服務及加速新店員入職訓練。
*   **Mylow：** 顧客用GenAI助理，提供商品搜尋與推薦、裝潢建議、DIY教學。
*   **強調成效：** 透過應用AI與生成式AI，每年省下10億美元成本。

### eBay生成式AI應用

*   **商品輔助上架：** 商家上傳商品圖片後，AI自動生成商品標題、描述等資訊。
*   **Shop the Look：** 根據顧客購物歷史生成穿搭範例圖，並推薦相似商品。
*   **AI代理購物：** 與OpenAI合作，開放AI代理Operator推薦eBay商品。

### Target生成式AI應用

*   **購物助手：** Bullseye Gift Finder鎖定兒童送禮場景，Shopping Assistant支援自有品牌商品。
*   **社群監聽：** 利用生成式AI捕捉社群媒體話題趨勢，加速商品上架和推廣。

### Anthropic新增Claude Code功能及Compliance API

*   **Claude Code：** Premium授權名額可同時使用Claude與Claude Code，用於技術探索與程式碼撰寫。
*   **Compliance API：** 企業可透過程式化介面即時存取Claude的使用資料，建置持續監測與自動化政策執行。

### TRM Labs推出Beacon Network加密貨幣犯罪應對網路

*   **目的：** 建立即時預警網絡，在非法資金被套現之前攔截。
*   **成員：** 包括Coinbase、Binance、PayPal、Ripple等數十家業者，以及全球執法機構與資安業者。

### Amazon生成式AI應用

*   **Project P.I.：** 商品瑕疵辨認系統，利用電腦視覺模型及多模態LLM，識別受損或不符訂單規格的商品。
*   **Wellspring：** 導航系統，利用生成式AI分析多種資訊，精準識別郵箱、車位和入口等具體位置。
*   **Deepfleet：** AI交通指揮官，強化物流中心內機器人調度。
*   **Rufus：** AI購物助理，搜尋、比較商品價格及規格、回答商品相關問題，並可根據顧客過往資料給出個人化答覆。
*   **Interests：** 個人化商品推薦功能，根據顧客自行設定的追蹤任務，自動探索最新上架商品。

### Walmart生成式AI應用

*   **適應式零售：** 利用AI/ML及生成式AI技術分析顧客喜好，生成對應零售體驗。
*   **Ghotok：** 智慧商品分類與搜尋工具，結合預測型AI及生成式AI技術，強化商品搜尋體驗。
*   **Sparky：** 生成式AI聊天機器人，提供商品問答、搜尋和比較，並可根據顧客情境提供個人化購物建議。
*   **Trend-to-Product：** 利用生成式AI加速自有品牌及合作廠商的產品開發周期。
*   **Wally：** 第三方市集商家AI助手，提供供應鏈管理及營運面分析建議。
*   **程式碼輔助工具：** 程式碼撰寫助手及Pipeline Visualizer，協助工程師撰寫及檢查程式碼，節省開發時間。
### Google AI模式拓展至全球，並實驗代理及個人化功能

*   Google將搜尋中的AI模式拓展至全球180多個國家，但目前僅支援英文。
*   AI模式基於Gemini 2.5模型，支援深度搜尋、複雜查詢、多模態輸入和聊天式互動。
*   美國市場推出協作功能，使用者可分享AI模式回應連結進行協作。
*   代理功能讓AI可主動替使用者執行複雜任務，如餐廳訂位，目前僅限美國Google AI Ultra付費用戶。
*   實驗中的個人化功能利用使用者對話紀錄和搜尋活動提供個人化結果，初期專注於餐飲主題，僅限美國市場。

### Mozilla Firefox 142修補多項安全漏洞

*   Mozilla發布Firefox 142，修補包括5個高風險漏洞在內的多項安全問題。
*   高風險漏洞包括GMP元件的無效指標（CVE-2025-9179）、Canvas 2D元件的同源政策繞過（CVE-2025-9180）以及記憶體安全漏洞（CVE-2025-9184、CVE-2025-9185、CVE-2025-9187）。
*   iOS版Firefox 142也修補了一項高風險漏洞（CVE-2025-55030）及多項中低風險漏洞。
*   多數漏洞也影響Firefox ESR及Thunderbird，Mozilla已發布更新修補。

### 資安威脅：臉書釣魚、俄駭入侵與英特爾漏洞

*   駭客利用臉書粉絲頁版權爭議散布竊資軟體，手法借助AI偵察和翻譯，更難防範。
*   FBI警告俄羅斯駭客濫用思科舊漏洞（CVE-2018-0171）攻擊全球公部門及企業基礎架構。
*   資安研究員揭露英特爾內部網站存在漏洞，可能導致27萬員工資料外洩，英特爾已修補。

### BitUnlocker漏洞繞過BitLocker保護

*   資安研究團隊發現能透過Windows修復環境（WinRE）截取BitLocker機敏資訊的一系列弱點BitUnlocker。
*   BitUnlocker總共被登記為4項漏洞，分別是CVE-2025-48800、CVE-2025-48003、CVE-2025-48804，以及CVE-2025-48818，CVSS風險評分皆為6.8。
*   微軟於7月例行更新發布修補程式。

### Google安卓虛擬機管理程式獲SESIP 5級認證

*   Google的安卓虛擬機管理程式pKVM取得SESIP 5級認證。
*   這是首個針對大規模消費性電子裝置部署，通過此等級的軟體安全系統。
*   此認證為關鍵性隔離工作負載建立更可驗證的安全基礎，涵蓋裝置上人工智慧工作負載與敏感資料處理等應用情境。

### Intel內部網站存在漏洞導致員工資料外洩風險

*   資安研究員Eaton Zveare指出，英特爾內部網站存在弱點，可能導致27萬員工資料外洩。
*   漏洞包括名片訂購網站、Product Hierarchy網站、Product Onboarding網站以及SEIMS Supplier Site的合作廠商登入介面。
*   英特爾已確認並修補漏洞。

### Noodlophile Stealer竊資軟體透過臉書釣魚散布

*   資安業者Morphisec揭露Noodlophile Stealer竊資軟體透過臉書違反著作權網釣進行攻擊，借助AI和廣泛偵察，手法更難防範。
*   駭客利用DLL側載手法傳遞惡意酬載，並利用Telegram架設C2。
*   Noodlophile Stealer具備迴避AMSI、ETW等功能，並積極開發螢幕截圖、鍵盤偵錄等功能。

### Google Gemini for Government產品與美國政府合作

*   Google推出Gemini for Government產品，並與美國總務管理局簽署OneGov合作協議。
*   美國聯邦機構可以每年0.47美元的價格訂閱Gemini for Government至2026年。
*   Gemini for Government是一個完整的人工智慧平臺，包含企業搜尋、影片與圖片生成等功能，並整合安全功能。

### 俄羅斯駭客濫用思科漏洞攻擊全球基礎架構

*   FBI警告俄羅斯駭客濫用思科Cisco Smart Install軟體的舊式網路設備漏洞CVE-2018-0171攻擊全球公部門及企業基礎架構。
*   駭客蒐集美國多個基礎架構產業的思科網路裝置配置檔，可能修改配置檔進行非授權存取。
*   主導攻擊的FSB Center 16過去曾駭入全球網路設備，並植入自製工具。

### 零售業巨頭應用生成式AI

*   全球零售業巨頭廣泛導入生成式AI，支援購物體驗、內部營運、供應鏈管理等環節。
*   沃爾瑪Walmart 利用 AI 強化購物體驗，升級供應鏈管理，提升員工生產力。
*   亞馬遜Amazon 將 GenAI 應用在買賣家體驗、物流和 RMN 方面。
*   連鎖超市Target 擁抱GenAI 用於內部資料整理、員工應用、顧客系統。
*   C2C平臺 eBay 用GenAI從多種面向提升商品資料品質。
*   家居零售業者 Lowe's 利用GenAI 降低服務及購物門檻、加速零售營運。

### Anthropic Claude新增Premium授權及Compliance API

*   Anthropic為其企業與團隊方案新增可升級的Premium授權名額，讓用戶同時使用Claude與Claude Code。
*   推出Compliance API，協助企業即時監管使用狀況並滿足法遵需求。
*   管理員可分配標準或Premium名額，Premium使用者可在同一工作流程中進行技術探索、架構討論和程式碼撰寫。

### TRM Labs推出Beacon Network加密貨幣犯罪應對網路

*   TRM Labs推出Beacon Network，串連執法機構、加密貨幣交易平臺、支付公司及資安研究人員，可在非法資金被套現前攔截。
*   Beacon Network的創始成員包括Coinbase、Binance、PayPal等數十家業者。
*   Beacon Network會由執法機構或資安業者標記可疑錢包位址，並自動追蹤資金流向，在資金到達合作平臺時觸發即時警報。
### Google發布開源嵌入模型 EmbeddingGemma

*   Google發布開源嵌入模型 EmbeddingGemma，旨在裝置端離線情境下提供語義搜尋與RAG所需的文字向量。
*   該模型擁有3.08億參數，在MTEB多語榜單中排名5億參數以下開源模型之首，支援100多種語言。
*   透過量化感知訓練降低記憶體占用，可在低於200MB記憶體環境執行。
*   EmbeddingGemma以Gemma 3架構為基礎，模型參數約1億，嵌入參數約2億，提供約2000 Token上下文長度，並與Gemma 3n共用分詞器。
*   採用Matryoshka Representation Learning（MRL），可輸出多種維度的向量（768、512、256、128）。
*   設計重點為離線與隱私，向量化在本地硬體完成，適用於個人資料、企業知識庫等本地檢索。
*   與常見工具鏈整合，提供瀏覽器端互動展示。
*   Google建議大規模伺服器端服務採用Gemini Embedding。

### Atlassian收購 The Browser Company

*   Atlassian 宣布以 6.1 億美元現金收購 The Browser Company，預計今年第四季完成交易。
*   Atlassian 成立於 2002 年，專注於開發團隊協作工具，如 Jira、Confluence、Trello 及 Bitbucket，擁有超過 30 萬全球客戶。
*   The Browser Company 成立於 2019 年，由 Josh Miller 和 Hursh Agrawal 創辦，致力於打造網頁瀏覽工具，已發表 Arc 1.0 和 AI 瀏覽器 Dia。
*   收購後，Miller 和 Agrawal 將繼續留任執行長與技術長，專注於開發 Dia，打造功能完整的瀏覽器。

### 資安威脅綜覽：DDoS攻擊、APT駭客與銀行木馬

*   Cloudflare 揭露一起峰值達 11.5 Tbps 的 DDoS 攻擊，流量來自多家雲端供應商及物聯網裝置，難以判定單一主要來源。
*   俄羅斯駭客 APT28 使用新的後門程式 NotDoor，透過 Outlook 的 VBA 巨集監控郵件，竊取資料。
*   北韓駭客 Lazarus 針對金融與加密貨幣產業，使用 PondRAT、ThemeForestRAT、RemotePE 三款遠端存取木馬。
*   中國駭客 Silver Fox 利用微軟簽署的 WatchDog 驅動程式繞過 Windows 安全機制，植入 ValleyRAT。
*   Android 銀行木馬 Anatsa 偽裝成工具型應用程式上架 Google Play，竊取金融憑證，針對 831 款金融與加密貨幣應用。
*   臺灣大型企業今年招募資安人才比例為 32%，平均擴編 2.9 名資安人員，服務業需求尤為明顯。

### APT28 新後門程式 NotDoor

*   俄羅斯駭客 APT28 使用新的後門程式 NotDoor 攻擊北約成員國企業。
*   NotDoor 實際上是 Outlook 的 VBA 巨集，可監控郵件、接收命令、竊取資料、上傳檔案、執行命令。
*   駭客濫用 OneDrive 應用程式執行檔，透過 DLL 側載手法植入 NotDoor，並停用巨集防護機制。
*   該後門程式隱蔽性高，僅少數防毒引擎能偵測。

### 輪胎大廠普利司通北美分公司遭遇網路攻擊

*   普利司通北美分公司（BSA）遭遇網路攻擊，影響工廠營運。
*   位於艾坎郡和魁北克省喬利埃特的工廠受影響，可能波及北美所有工廠，約1400名員工受影響。
*   BSA 初步認為客戶資料未受波及，已展開調查。
*   BSA 在 2022 年也曾遭受網路攻擊並發生資料外洩。

### LangChain 重大更新：以代理為核心，導入標準化訊息內容區塊

*   LangChain 團隊推出重大更新，重新定位為高階框架，基於 LangGraph 代理執行時系統。
*   導入標準化的訊息內容區塊，支援 Python 與 JavaScript。
*   LangGraph 升至 1.0，作為低階代理調度框架，提供持久執行、短期記憶、人類介入與串流等能力。
*   引入 .content_blocks 屬性，以更結構化的方式呈現文字、工具呼叫與回傳內容。

### 資安威脅新趨勢：自動化滲透工具與大型語言模型風險

*   駭客濫用滲透測試自動化平台 HexStrike-AI，快速將漏洞轉化為武器並用於攻擊。
*   全球有超過 1 千臺 Ollama 伺服器曝露在網際網路，近 2 成模型可在未經身分驗證的情況下執行模型推論，形成攻擊面。
*   數發部將持續推動 AI 產業、資安韌性、打詐等政策，加速數位憑證皮夾等數位政府建設。
*   Varonis 宣布收購 AI 原生電子郵件安全業者 SlashNext，以強化電子郵件安全防護。

### Zed編輯器整合Claude Code

*   Zed 編輯器透過開放協定 ACP 整合 Claude Code，支援跨檔案即時編輯。
*   ACP 定位為標準化通訊協定，讓任一代理可介接所有支援 ACP 的編輯器。
*   Zed 推出以 JSON-RPC 為基礎的 Claude Code 橋接器，以 Apache-2.0 授權開源。
*   使用者可在 Zed 代理面板選用 Claude Code 開始新工作，同步呈現跨檔案的候選修改。

### 英國超市Tesco控告VMware和博通違反永久授權合約

*   英國超市集團 Tesco 控告 VMware、博通及經銷商 Computacenter 違反 Tesco 原本所購 VMware 產品的永久授權合約，要求各自承擔至少 1 億英鎊損失。
*   博通收購 VMware 後不再提供永久授權，轉型為訂閱制，Tesco 認為被迫重複付費。
*   Tesco 指控博通違反合約，危及該公司營運，因 VMware 支撐了 Tesco 約 4 萬個伺服器的工作負載，包括收銀及物流系統。

### Cloudflare 攔截 11.5 Tbps DDoS 攻擊

*   Cloudflare 自動化防禦系統在數十秒內攔截峰值 11.5 Tbps 的 DDoS 攻擊，封包速率達 5.1 Bpps。
*   最初誤判攻擊流量主要來自 Google 雲端，後更正為多個 IoT 裝置與多家雲端供應商。
*   攻擊類型為 UDP 洪水攻擊，利用 UDP 無需連線交握特性，短時間內將龐大流量推送至邊界路由器，導致服務不可用。
*   Cloudflare 過去已多次披露相近規模的案例，顯示超高流量攻擊事件正成為常見威脅。

### 北韓駭客 Lazarus 使用多款遠端存取木馬攻擊金融與加密貨幣產業

*   北韓駭客組織 Lazarus 針對金融與加密貨幣產業，使用 PondRAT、ThemeForestRAT 和 RemotePE 三款遠端存取木馬（RAT）。
*   駭客透過社交工程取得初期存取管道，疑似利用零時差漏洞執行程式碼。
*   駭客會清除原本的木馬程式，更換為 RemotePE，以採取更高的安全層級，避免被防守方察覺。

### Varonis 收購 AI 原生電子郵件安全業者 SlashNext

*   資料安全公司 Varonis 收購 AI 原生電子郵件安全業者 SlashNext。
*   SlashNext 透過 AI 模型、電腦視覺、自然語言處理和虛擬瀏覽器等技術，偵測網釣攻擊，具備零時差防護能力。
*   SlashNext 號稱擁有全球最好的檢測引擎，對 BEC 和 QR code 攻擊的檢測率達 100%。

### LLM記憶體擴展方案的趨勢

*   LLM 的記憶體需求增長速度超過 GPU 供給，導致記憶體容量瓶頸。
*   記憶體擴展方案分為外部擴展和內部擴展兩條路線。
*   外部擴展方案利用 GPU 外部的 DRAM、SSD 或網路介接裝置，靈活但頻寬受限。
*   內部擴展方案（如 HBF）與 GPU 晶片層級整合，具備高頻寬但缺乏靈活性。

### LLM記憶體瓶頸

*   LLM 能力快速增長，導致記憶體需求暴漲，但 GPU 記憶體供給有限。
*   記憶體瓶頸影響 LLM 運作效率，浪費 GPU 資源。
*   影響記憶體占用的因素包括模型權重、梯度、啟動反應表徵、優化器狀態和 KV 快取。
*   GPU 記憶體配置增長速度落後於 LLM 記憶體需求。
*   擴展記憶體資源是解決 LLM 記憶體瓶頸的關鍵。### Google發布開源嵌入模型EmbeddingGemma

Google 發布開源嵌入模型 EmbeddingGemma，目標是在裝置端離線情境下提供語義搜尋與 RAG 功能。該模型以 3.08 億參數在 MTEB 多語榜單中名列前茅，支援 100 多種語言，並透過量化感知訓練降低記憶體占用，可在低於 200 MB 記憶體環境中執行。EmbeddingGemma 以 Gemma 3 架構為基礎，提供約 2,000 Token 上下文長度，並與 Gemma 3n 共用分詞器，方便在同一裝置上完成檢索與生成回答。EmbeddingGemma 採用 Matryoshka Representation Learning（MRL），提供 768、512、256 與 128 等多種向量尺寸選擇，讓開發者在檢索品質、延遲與儲存成本之間調整。Google 將 EmbeddingGemma 定位為裝置端的嵌入解決方案，適用於需要離線運作、注重資料主權或希望快速回應的應用，而大規模伺服器端服務則建議採用 Gemini Embedding。該模型與常見工具鏈整合，並提供瀏覽器端的互動展示。

---

### Atlassian 收購 The Browser Company

Atlassian 宣布以 6.1 億美元現金收購 The Browser Company，預計今年第四季完成交易。Atlassian 是一家開發團隊協作與開發工具的公司，產品包括 Jira、Confluence、Trello 及 Bitbucket 等。The Browser Company 由 Josh Miller 和 Hursh Agrawal 於 2019 年創辦，旨在打造一款解決使用者瀏覽及生產力問題的網頁瀏覽工具，其產品包括 Arc 1.0 和 AI 瀏覽器 Dia。收購後，Miller 和 Agrawal 將繼續留任，專注於開發 Dia，打造一個不受平臺限制、功能完整的瀏覽器。

---

### 資安威脅與防護快訊

Cloudflare 揭露，近期攔截到峰值 11.5 Tbps 的 DDoS 攻擊，流量最初被誤認為主要來自 Google 雲端，後修正為來自多家雲端供應商及物聯網裝置。俄羅斯駭客 APT28 使用新的後門程式 NotDoor 攻擊北約成員國企業，該後門為 Outlook 的 VBA 巨集，可監控郵件並執行命令。北韓駭客 Lazarus 針對金融與加密貨幣產業，使用多款遠端存取木馬（RAT），包括 PondRAT、ThemeForestRAT 及 RemotePE。中國駭客 Silver Fox 利用微軟簽署的 WatchDog Antimalware 驅動程式繞過 Windows 安全機制，植入遠端存取木馬 ValleyRAT。Android 銀行木馬 Anatsa 偽裝成工具型應用程式上架至 Google Play，竊取金融憑證，目前針對 831 款金融與加密貨幣應用。iThome 2025 年資安大調查顯示，臺灣大型企業今年招募資安人才的需求放緩，但仍有 3 成 2 的企業要徵求資安人才，人力需求持續存在。

---

### APT28 使用新後門程式 NotDoor 攻擊北約成員國

俄羅斯駭客 APT28 針對北約成員國企業組織發動攻擊，使用名為 NotDoor 的新型後門程式。該後門實際上是 Outlook 的 VBA 巨集，可監控傳入的郵件，接收攻擊者命令，竊取資料、上傳檔案或執行命令。駭客濫用 OneDrive 應用程式執行檔，透過 DLL 側載手法載入惡意檔案 SSPICLI.dll，在受害電腦植入 NotDoor 並停用巨集防護。NotDoor 透過特定事件觸發執行，具備執行命令、回傳結果、外洩資料及上傳檔案等功能，且具備高度隱蔽性。

---

### 輪胎大廠普利司通北美分公司遭遇網路攻擊

輪胎大廠普利司通北美分公司（BSA）遭遇網路攻擊，影響工廠營運。BSA 位於艾坎郡的兩座工廠受到局部資安事故影響，生產設備受到波及。BSA 全面啟動調查，初步認為客戶資料未受影響。BSA 位於魁北克省喬利埃特的輪胎製造工廠也因網路攻擊暫停營運。BSA 並非首次遭受網路攻擊，2022 年也曾發生資安事故，資料遭竊。

---

### LangChain 重新定位為高階框架，以代理為核心

LangChain 團隊宣布新版本，將 LangChain 重新定位為高階框架，建立在 LangGraph 代理執行時系統之上，並在 LangChain Core 導入標準化的訊息內容區塊。新架構透過 create_agent 提供統一入口，底層由 LangGraph 接手執行與管理狀態。LangGraph 升至 1.0，提供持久執行、短期記憶、人類介入與串流等能力。LangChain Core 引入 .content_blocks 屬性，以更結構化的方式呈現文字、工具呼叫與回傳內容。官方建議開發者在新專案中逐步嘗試，現有系統則可先透過 langchain-legacy 維持穩定。

---

### 資安威脅警報：駭客濫用自動化滲透測試工具及LLM伺服器曝險

資安業者 Check Point 揭露，駭客濫用滲透測試自動化平臺 HexStrike-AI，將漏洞武器化並用於實際攻擊。思科發現全球有超過 1 千臺 Ollama 伺服器曝露在網際網路上，近 2 成模型可在無須身分驗證的情況下執行模型推論，形成可被濫用的攻擊面。 Check Point 指出，駭客借助 Hexstrike-AI，原本需要數天才能找到利用漏洞的方法，現在只需不到 10 分鐘。思科調查發現，許多企業與個人部署大型語言模型（LLM）時忽視存取控制與網路隔離。美國網路安全暨基礎設施安全局（CISA）警告，TP-Link 無線 Wi-Fi 訊號延伸器資安漏洞 CVE-2020-24363 已遭利用。Google 發布安卓作業系統每月例行更新，修補 112 個資安漏洞，其中 4 個為重大層級，且有兩項高風險漏洞被用於針對性攻擊。數發部長林宜敬強調將延續先前施政方針，持續推動 AI 產業、資安韌性、打詐等政策。Varonis Systems 買下 AI 原生電子郵件安全業者 SlashNext。iThome CIO 暨資安大調查顯示，API Protection 是企業新興資安投資重點第一名。

---

### Zed 整合 Claude Code，透過 ACP 實現跨檔案即時編輯

Zed 以開放協定 ACP（Agent Client Protocol）整合 Claude Code，使用者可在 Zed 內直接啟動代理進行跨檔案即時編輯，並追蹤多檔案修改。Zed 將此 Claude Code 橋接器以 Apache-2.0 授權開源，供任何採用 ACP 的編輯器重用。使用者更新至 Zed 最新版本後，從代理面板即可選用 Claude Code 開始新工作。新功能支援 Claude Code 的自訂斜線指令，讓生成、修改、審查與提交的路徑維持在編輯器中完成。Neovim 編輯器的 CodeCompanion 外掛已採用 ACP，Claude Code 也可於 Neovim 運作。

---

### 英國超市 Tesco 起訴 VMware、博通及經銷商 Computacenter

英國超市集團 Tesco 已針對 VMware、博通（Broadcom）及經銷商 Computacenter 提出訴訟，指控廠商違反 Tesco 原本所購 VMware 產品的永久授權合約，要求各自承擔至少 1 億英鎊（1.34 億美元）的損失。博通在收購 VMware 後不再提供永久授權版，全面轉型為訂閱制。Tesco 認為，博通的新政策不僅違反合約，也可能危及該公司的營運，因為 VMware 支撐了 Tesco 約 4 萬個伺服器的工作負載，連接收銀及物流系統。

---

### Cloudflare 攔截 11.5 Tbps DDoS 攻擊，超高流量攻擊成常見威脅

Cloudflare 自動化防禦攔截到峰值 11.5 Tbps 的 DDoS 攻擊，封包速率最高達 5.1 Bpps，為 UDP 洪水攻擊，持續約 35 秒。攻擊流量來自多個 IoT 裝置與多家雲端供應商，Google 雲端只是其中之一。Cloudflare 過去已多次披露相近規模的案例，顯示超高流量攻擊事件正成為常見威脅型態。
## Google 發布開源嵌入模型 EmbeddingGemma

Google 發布開源嵌入模型 EmbeddingGemma，參數量為 3.08 億，在 MTEB 多語榜單中參數量 5 億以下的開源模型中排名最高，支援 100 多種語言。該模型透過量化感知訓練降低記憶體佔用，可在低於 200MB 記憶體環境下執行，適用於行動裝置、筆電和桌機在無網路下完成檢索與問答。EmbeddingGemma 基於 Gemma 3 架構，由約 1 億模型參數和約 2 億嵌入參數組成，提供約 2000 Token 上下文長度，並與 Gemma 3n 共用分詞器，便於在同一裝置上完成檢索和生成回答。官方強調在 EdgeTPU 上處理 256 Token 輸入時，嵌入推論延遲可低於 15ms。EmbeddingGemma 採用 Matryoshka Representation Learning (MRL)，單一模型可輸出多種維度的向量，提供 768、512、256 和 128 等尺寸選擇。該模型以離線與隱私為設計重點，向量化在本地硬體完成，可用於搜尋個人檔案或建立企業知識庫本地檢索入口。EmbeddingGemma 與常見工具鏈整合，並提供瀏覽器端的互動展示。Google 將 EmbeddingGemma 定位為裝置端的嵌入解決方案，面向大規模伺服器端服務建議採用 Gemini Embedding。

## Atlassian 收購 The Browser Company

Atlassian 已與 The Browser Company 達成最終收購協議，將以 6.1 億美元現金收購。Atlassian 主要開發團隊協作與開發工具，如 Jira、Confluence、Trello 及 Bitbucket，全球客戶超過 30 萬家。The Browser Company 創辦人為 Josh Miller 和 Hursh Agrawal，旨在打造一款可解決使用者瀏覽及生產力問題的網頁瀏覽工具，產品包括 Arc 1.0 和 AI 瀏覽器 Dia。Miller 和 Agrawal 將繼續留任執行長與技術長，專注於開發 Dia。收購案預計在 Atlassian 2026 財年第二季完成，價格計入了 The Browser Company 現有現金。

## DDoS 攻擊與資安威脅事件

Cloudflare 攔截到峰值 11.5 Tbps 的 DDoS 攻擊，最初認為主要來自 Google 雲端，後改口稱來自多家雲端供應商及物聯網裝置。UDP 洪水攻擊持續約 35 秒，封包速率最高達 5.1 Bpps。輪胎大廠普利司通北美分公司 (BSA) 遭遇網路攻擊，影響工廠營運。俄羅斯駭客 APT28 使用名為 NotDoor 的後門程式攻擊北約成員國企業，該後門為 Outlook 的 VBA 巨集，可監控郵件、竊取資料等。北韓駭客組織 Lazarus 使用多款 RAT 木馬攻擊金融與加密貨幣產業。中國駭客組織 Silver Fox 利用 WatchDog Antimalware 驅動程式繞過 Windows 安全機制，植入 ValleyRAT。Android 銀行木馬 Anatsa 透過偽裝成工具型應用程式上架 Google Play，竊取金融憑證，針對 831 款金融與加密貨幣應用。

## 企業資安人才需求

iThome 2025 年資安大調查顯示，32% 的臺灣大型企業計劃招募資安人才，服務業需求最高，達 40%。企業平均擴編約 2.9 名資安人員，需求增長率約 6%。

## APT28 使用新型後門程式 NotDoor

俄羅斯駭客 APT28 使用新的後門程式 NotDoor 攻擊北約成員國企業組織。NotDoor 實際上是 Outlook 的 VBA 巨集，功能是監控傳入的電子郵件，一旦出現特定的文字，就會試圖接收攻擊者的命令，然後竊取資料、上傳檔案，或是在受害電腦執行命令。為了迴避偵測，駭客濫用微軟檔案共享服務 OneDrive 的應用程式執行檔，透過 DLL 側載手法載入惡意檔案 SSPICLI.dll，於受害電腦植入 NotDoor，並停用巨集防護機制。NotDoor 具備執行命令、回傳執行結果、外洩資料和上傳檔案等功能。

## 普利司通北美分公司 (BSA) 遭遇網路攻擊

輪胎大廠普利司通北美分公司 (BSA) 遭遇網路攻擊，影響該公司的工廠營運，兩座位於艾坎郡的工廠遭遇局部資安事故，影響部分生產設備。BSA 位於魁北克省喬利埃特的輪胎製造工廠也因網路攻擊暫停營運，事故恐影響普利司通北美所有工廠，預計影響 1400 名員工。BSA 曾於 2022 年遭遇網路攻擊，導致生產中斷並竊得內部資料。

## LangChain 更新與 LangGraph 1.0

LangChain 團隊更新了 LangChain，支援 Python 與 JavaScript，並以代理為核心，重新定位為高階框架，建立在 LangGraph 代理執行時系統之上。新架構透過 create_agent 提供統一入口，底層由 LangGraph 接手執行與管理狀態。LangGraph 升至 1.0，提供持久執行、短期記憶、人類介入與串流等能力，已在 Uber、LinkedIn、Klarna 等公司使用。LangChain Core 引入 .content_blocks 屬性，以更結構化的方式呈現文字、工具呼叫與回傳內容。

## AI 資安威脅與 Ollama 伺服器曝險

資安業者 Check Point 發現駭客濫用滲透測試自動化平臺 HexStrike-AI，將漏洞打造成武器並用於實際攻擊行動，大幅縮短準備時間並廣泛尋找下手目標。思科發現全球有超過 1 千臺 Ollama 伺服器曝露在網際網路上，可公開存取，其中近 2 成可在無須身分驗證的情況下執行模型推論，形成可被濫用的攻擊面。

## 美國 CISA 警告 TP-Link Wi-Fi 訊號延伸器漏洞已遭利用

美國網路安全暨基礎設施安全局 (CISA) 提出警告，TP-Link 無線 Wi-Fi 訊號延伸器資安漏洞 CVE-2020-24363 已遭利用，並將其列入已遭利用的漏洞名單 (KEV)。此漏洞影響 TL-WA855RE 型號，允許攻擊者在未經授權的情況下發出特製請求，重置設備並恢復原廠設定。

## Google Android 例行性修補資安漏洞

Google 發布安卓作業系統的每月例行更新，修補 112 個資安漏洞，其中包含 4 個重大層級漏洞，以及 2 個高風險且已被用於針對性攻擊的漏洞。

## 臺灣數發部未來政策方向

臺灣數發部長林宜敬表示將延續先前施政方針，持續推動 AI 產業、資安韌性、打詐等政策，加速數位憑證皮夾等數位政府建設。

## Varonis Systems 併購 AI 電子郵件安全業者 SlashNext

專注於資料安全與治理的美國資安業者 Varonis Systems 宣布買下 AI 原生電子郵件安全業者 SlashNext。

## 企業資安投資新興方案

2025 年 iThome CIO 暨資安大調查顯示，API Protection 是企業資安投資重點首位，OT 安全和 SSE/SASE 也是企業關注的新興資安方案。

## Zed 編輯器整合 Claude Code

Zed 編輯器以開放協定 ACP (Agent Client Protocol) 整合 Claude Code，使用者可在 Zed 內直接啟動代理進行跨檔案即時編輯，並追蹤多檔案修改。Zed 以 JSON-RPC 為基礎推出 Claude Code 橋接器，並以 Apache-2.0 授權開源。使用者可透過代理面板選用 Claude Code 開始新工作，並支援 Claude Code 的自訂斜線指令。

## Tesco 起訴 VMware, 博通及經銷商 Computacenter

英國超市集團 Tesco 已針對 VMware、博通 (Broadcom) 及經銷商 Computacenter 提出訴訟，指控廠商違反 Tesco 原本所購 VMware 產品的永久授權合約，要求各自承擔至少 1 億英鎊（1.34 億美元）的損失。博通收購 VMware 後不再提供永久授權版，全面轉型為訂閱制，Tesco 認為博通的新政策違反合約，並可能危及該公司的營運。

## Cloudflare 攔截到峰值 11.5 Tbps 的 DDoS 攻擊

Cloudflare 自動化防禦攔截到峰值 11.5 Tbps 的 DDoS 攻擊，封包速率最高達 5.1 Bpps，是一場持續約 35 秒的 UDP 洪水攻擊。攻擊流量來自多個 IoT 裝置與多家雲端供應商。

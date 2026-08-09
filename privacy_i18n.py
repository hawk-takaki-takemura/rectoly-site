# -*- coding: utf-8 -*-
"""Rectoly Privacy Policy — i18n string table."""

LOCALES = [
    ("en", "English", "ltr"),
    ("ja", "日本語", "ltr"),
    ("de", "Deutsch", "ltr"),
    ("es", "Español", "ltr"),
    ("zh-Hans", "中文（简体）", "ltr"),
    ("zh-Hant", "中文（繁體）", "ltr"),
    ("fr", "Français", "ltr"),
    ("it", "Italiano", "ltr"),
    ("da", "Dansk", "ltr"),
    ("ko", "한국어", "ltr"),
    ("pt-BR", "Português (Brasil)", "ltr"),
    ("nl", "Nederlands", "ltr"),
    ("sv", "Svenska", "ltr"),
    ("nb", "Norsk Bokmål", "ltr"),
    ("pl", "Polski", "ltr"),
    ("ru", "Русский", "ltr"),
    ("ar", "العربية", "rtl"),
    ("tr", "Türkçe", "ltr"),
    ("hi", "हिन्दी", "ltr"),
    ("id", "Bahasa Indonesia", "ltr"),
]

TRANSLATIONS = {
    "en": {
        "title": 'Rectoly — Privacy Policy',
        "h1": 'Rectoly — Privacy Policy',
        "updated": 'Last updated August 9, 2026',
        "intro": (
            'Hawk Eye ("we," "us") develops Rectoly, an iPad app for reading, annotating, and syncing'
            ' academic PDFs with Mendeley Reference Manager. This policy explains what information'
            ' Rectoly collects, why, and how it is handled.'
        ),
        "h2_collect": 'Information we collect',
        "mendeley_label": 'Your Mendeley account connection.',
        "mendeley_body": (
            'When you sign in with Mendeley, Rectoly requests an OAuth access token to read and sync'
            " your library, documents, and annotations. This token is stored in your device's Keychain"
            " and is never sent to our servers — Rectoly talks directly to Mendeley's own API."
        ),
        "docs_label": 'Your documents and annotations.',
        "docs_body": (
            'PDFs you open, along with highlights, underlines, sticky notes, and any handwritten ink'
            ' you add, are stored on your device. If you enable iCloud backup, this data — and, if you'
            ' separately opt in, your handwriting — is backed up to your own iCloud account via'
            " Apple's CloudKit. We do not have access to this data; it is encrypted and scoped to your"
            ' Apple ID.'
        ),
        "crash_label": 'Crash and error reports.',
        "crash_body": (
            'Rectoly uses Sentry to automatically report crashes and errors so we can fix bugs. These'
            ' reports are configured to exclude personal information: no default user identifier or IP'
            ' address is collected, and document titles, file paths, email addresses, authentication'
            ' tokens, and annotation text are stripped before a report is sent.'
        ),
        "analytics_label": 'Anonymous usage analytics.',
        "analytics_body": (
            'Rectoly uses TelemetryDeck to collect anonymous, aggregated usage signals — for example,'
            ' which screens are opened, whether onboarding was completed, or whether a sync succeeded'
            ' or failed (as a general reason category, not raw error text). These signals never'
            ' include document titles, file paths, email addresses, or annotation content, and are not'
            ' tied to your identity.'
        ),
        "purchases_label": 'Purchases.',
        "purchases_body": (
            'Subscriptions and one-time purchases are handled entirely by Apple through StoreKit. We'
            ' receive confirmation that a purchase was made; Rectoly does not collect or store your'
            " payment details. Apple's own privacy policy governs that data."
        ),
        "h2_dont": "What we don't do",
        "dont_sell": 'We do not sell your data.',
        "dont_ads": 'We do not run advertising or ad-tracking SDKs.',
        "dont_read": (
            'We do not read the content of your documents or annotations ourselves — they remain on'
            ' your device and, if you enable it, in your own iCloud account.'
        ),
        "h2_third": 'Third-party services',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'your reference library and document sync',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'optional backup, governed by your Apple ID',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'crash and error reporting',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'anonymous product analytics',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'purchases and subscriptions',
        "third_note": 'Each of these operates under its own privacy policy, which we encourage you to review.',
        "h2_retention": 'Data retention and deletion',
        "retention_body": (
            'Your documents, annotations, and handwriting remain on your device until you delete them'
            " or delete the app. If iCloud backup is enabled, you can turn it off in Rectoly's"
            " settings, or remove the app's iCloud data from your device's Settings app. Disconnecting"
            ' your Mendeley account removes the locally stored access token immediately.'
        ),
        "h2_children": "Children's privacy",
        "children_body": 'Rectoly is not directed at children under 13, and we do not knowingly collect information from them.',
        "h2_changes": 'Changes to this policy',
        "changes_body": (
            'We may update this policy as the app changes. Material changes will be reflected here'
            ' with an updated date.'
        ),
        "h2_contact": 'Contact',
        "contact_before": 'Questions about this policy:',
        "footer": 'Rectoly is developed by Hawk Eye.',
        "languages_label": 'Languages',
    },
    "ja": {
        "title": 'Rectoly — プライバシーポリシー',
        "h1": 'Rectoly — プライバシーポリシー',
        "updated": '最終更新日 2026年8月9日',
        "intro": (
            'Hawk Eye（以下「当社」）は、Mendeley Reference Manager と連携して学術 PDF の閲覧・注釈・同期を行う iPad アプリ Rectoly'
            ' を開発しています。本ポリシーでは、Rectoly がどのような情報を収集し、なぜ収集し、どのように取り扱うかを説明します。'
        ),
        "h2_collect": '収集する情報',
        "mendeley_label": 'Mendeley アカウントとの連携。',
        "mendeley_body": (
            'Mendeley でサインインすると、Rectoly はライブラリ、文書、注釈の読み取りと同期のために OAuth アクセストークンを要求します。このトークンは端末の'
            ' Keychain に保存され、当社のサーバーに送信されることはありません。Rectoly は Mendeley 自身の API と直接通信します。'
        ),
        "docs_label": '文書と注釈。',
        "docs_body": (
            '開いた PDF、ならびにハイライト、下線、付箋メモ、手書きインクは、すべて端末上に保存されます。iCloud'
            ' バックアップを有効にすると、このデータ（および別途オプトインした場合は手書きデータ）は Apple の CloudKit 経由でご自身の iCloud'
            ' アカウントにバックアップされます。当社はこのデータにアクセスできません。データは暗号化され、お客様の Apple ID の範囲に限定されます。'
        ),
        "crash_label": 'クラッシュおよびエラーレポート。',
        "crash_body": (
            'Rectoly はバグ修正のため、Sentry を用いてクラッシュやエラーを自動的に報告します。これらのレポートは個人情報を除外するよう設定されています。既定のユーザー識別子や'
            ' IP アドレスは収集されず、文書タイトル、ファイルパス、メールアドレス、認証トークン、注釈テキストは送信前に除去されます。'
        ),
        "analytics_label": '匿名の利用状況分析。',
        "analytics_body": (
            'Rectoly は TelemetryDeck'
            ' を用いて、匿名かつ集計された利用シグナルを収集します。たとえば、どの画面が開かれたか、オンボーディングが完了したか、同期が成功または失敗したか（一般的な理由カテゴリであり、生のエラーテキストではありません）などです。これらのシグナルに文書タイトル、ファイルパス、メールアドレス、注釈内容は含まれず、お客様の身元とも紐づけられません。'
        ),
        "purchases_label": '購入。',
        "purchases_body": (
            'サブスクリプションおよび買い切りの購入は、すべて Apple が StoreKit を通じて処理します。当社は購入が行われたことの確認を受け取りますが、Rectoly'
            ' はお支払い情報を収集・保存しません。当該データは Apple 独自のプライバシーポリシーに従います。'
        ),
        "h2_dont": '行わないこと',
        "dont_sell": 'お客様のデータを販売しません。',
        "dont_ads": '広告や広告トラッキング用 SDK を使用しません。',
        "dont_read": 'お客様の文書や注釈の内容を当社が自ら読み取ることはありません。それらは端末上にあり、有効にした場合はご自身の iCloud アカウントに留まります。',
        "h2_third": '第三者サービス',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": '参考文献ライブラリおよび文書の同期',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": '任意のバックアップ（お客様の Apple ID により管理）',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'クラッシュおよびエラー報告',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": '匿名のプロダクト分析',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": '購入およびサブスクリプション',
        "third_note": 'これらはそれぞれ独自のプライバシーポリシーに基づいて運営されており、ご確認をおすすめします。',
        "h2_retention": 'データの保持と削除',
        "retention_body": (
            '文書、注釈、手書きデータは、削除するかアプリを削除するまで端末上に残ります。iCloud バックアップが有効な場合は、Rectoly'
            ' の設定で無効にするか、端末の「設定」アプリからアプリの iCloud データを削除できます。Mendeley'
            ' アカウントの連携を解除すると、ローカルに保存されたアクセストークンは直ちに削除されます。'
        ),
        "h2_children": 'お子様のプライバシー',
        "children_body": 'Rectoly は 13 歳未満のお子様を対象としておらず、知りながら情報を収集することはありません。',
        "h2_changes": '本ポリシーの変更',
        "changes_body": 'アプリの変更に伴い、本ポリシーを更新することがあります。重要な変更は、更新日とともにここに反映されます。',
        "h2_contact": 'お問い合わせ',
        "contact_before": '本ポリシーに関するお問い合わせ：',
        "footer": 'Rectoly は Hawk Eye が開発しています。',
        "languages_label": '言語',
    },
    "de": {
        "title": 'Rectoly — Datenschutzerklärung',
        "h1": 'Rectoly — Datenschutzerklärung',
        "updated": 'Zuletzt aktualisiert am 9. August 2026',
        "intro": (
            'Hawk Eye („wir“, „uns“) entwickelt Rectoly, eine iPad-App zum Lesen, Annotieren und'
            ' Synchronisieren akademischer PDFs mit Mendeley Reference Manager. Diese Erklärung'
            ' beschreibt, welche Informationen Rectoly erhebt, warum und wie sie verarbeitet werden.'
        ),
        "h2_collect": 'Informationen, die wir erheben',
        "mendeley_label": 'Ihre Mendeley-Kontoverbindung.',
        "mendeley_body": (
            'Wenn Sie sich mit Mendeley anmelden, fordert Rectoly ein OAuth-Zugriffstoken an, um Ihre'
            ' Bibliothek, Dokumente und Annotationen zu lesen und zu synchronisieren. Dieses Token'
            ' wird in der Keychain Ihres Geräts gespeichert und niemals an unsere Server gesendet —'
            ' Rectoly kommuniziert direkt mit der API von Mendeley.'
        ),
        "docs_label": 'Ihre Dokumente und Annotationen.',
        "docs_body": (
            'PDFs, die Sie öffnen, sowie Hervorhebungen, Unterstreichungen, Haftnotizen und'
            ' handschriftliche Tinte werden auf Ihrem Gerät gespeichert. Wenn Sie die iCloud-Sicherung'
            ' aktivieren, werden diese Daten — und, wenn Sie gesondert zustimmen, Ihre Handschrift —'
            ' über Apples CloudKit in Ihrem eigenen iCloud-Konto gesichert. Wir haben keinen Zugriff'
            ' auf diese Daten; sie sind verschlüsselt und an Ihre Apple ID gebunden.'
        ),
        "crash_label": 'Absturz- und Fehlerberichte.',
        "crash_body": (
            'Rectoly nutzt Sentry, um Abstürze und Fehler automatisch zu melden, damit wir Bugs'
            ' beheben können. Diese Berichte sind so konfiguriert, dass personenbezogene Daten'
            ' ausgeschlossen werden: Es wird kein Standard-Benutzeridentifikator und keine IP-Adresse'
            ' erfasst, und Dokumenttitel, Dateipfade, E-Mail-Adressen, Authentifizierungstoken und'
            ' Annotationstext werden vor dem Senden entfernt.'
        ),
        "analytics_label": 'Anonyme Nutzungsanalysen.',
        "analytics_body": (
            'Rectoly nutzt TelemetryDeck, um anonyme, aggregierte Nutzungssignale zu erfassen —'
            ' beispielsweise welche Bildschirme geöffnet werden, ob das Onboarding abgeschlossen wurde'
            ' oder ob eine Synchronisierung erfolgreich war oder fehlgeschlagen ist (als allgemeine'
            ' Ursachenkategorie, nicht als roher Fehlertext). Diese Signale enthalten niemals'
            ' Dokumenttitel, Dateipfade, E-Mail-Adressen oder Annotationsinhalte und sind nicht mit'
            ' Ihrer Identität verknüpft.'
        ),
        "purchases_label": 'Käufe.',
        "purchases_body": (
            'Abonnements und Einmalkäufe werden vollständig von Apple über StoreKit abgewickelt. Wir'
            ' erhalten eine Bestätigung, dass ein Kauf getätigt wurde; Rectoly erhebt oder speichert'
            ' keine Zahlungsdaten. Für diese Daten gilt Apples eigene Datenschutzerklärung.'
        ),
        "h2_dont": 'Was wir nicht tun',
        "dont_sell": 'Wir verkaufen Ihre Daten nicht.',
        "dont_ads": 'Wir setzen keine Werbe- oder Ad-Tracking-SDKs ein.',
        "dont_read": (
            'Wir lesen den Inhalt Ihrer Dokumente oder Annotationen nicht selbst — sie verbleiben auf'
            ' Ihrem Gerät und, falls aktiviert, in Ihrem eigenen iCloud-Konto.'
        ),
        "h2_third": 'Drittanbieterdienste',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'Ihre Referenzbibliothek und Dokumentsynchronisierung',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'optionale Sicherung, geregelt durch Ihre Apple ID',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'Absturz- und Fehlerberichterstattung',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'anonyme Produktanalysen',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'Käufe und Abonnements',
        "third_note": (
            'Jeder dieser Dienste unterliegt seiner eigenen Datenschutzerklärung, die wir Ihnen zur'
            ' Prüfung empfehlen.'
        ),
        "h2_retention": 'Datenspeicherung und Löschung',
        "retention_body": (
            'Ihre Dokumente, Annotationen und Handschrift verbleiben auf Ihrem Gerät, bis Sie sie'
            ' löschen oder die App löschen. Wenn die iCloud-Sicherung aktiviert ist, können Sie sie in'
            ' den Einstellungen von Rectoly deaktivieren oder die iCloud-Daten der App in der'
            ' Einstellungen-App Ihres Geräts entfernen. Das Trennen Ihres Mendeley-Kontos entfernt das'
            ' lokal gespeicherte Zugriffstoken sofort.'
        ),
        "h2_children": 'Datenschutz von Kindern',
        "children_body": (
            'Rectoly richtet sich nicht an Kinder unter 13 Jahren, und wir erheben wissentlich keine'
            ' Informationen von ihnen.'
        ),
        "h2_changes": 'Änderungen dieser Erklärung',
        "changes_body": (
            'Wir können diese Erklärung aktualisieren, wenn sich die App ändert. Wesentliche'
            ' Änderungen werden hier mit einem aktualisierten Datum ausgewiesen.'
        ),
        "h2_contact": 'Kontakt',
        "contact_before": 'Fragen zu dieser Erklärung:',
        "footer": 'Rectoly wird von Hawk Eye entwickelt.',
        "languages_label": 'Sprachen',
    },
    "es": {
        "title": 'Rectoly — Política de privacidad',
        "h1": 'Rectoly — Política de privacidad',
        "updated": 'Última actualización: 9 de agosto de 2026',
        "intro": (
            'Hawk Eye ("nosotros") desarrolla Rectoly, una app para iPad para leer, anotar y'
            ' sincronizar PDF académicos con Mendeley Reference Manager. Esta política explica qué'
            ' información recopila Rectoly, por qué y cómo se trata.'
        ),
        "h2_collect": 'Información que recopilamos',
        "mendeley_label": 'La conexión de su cuenta de Mendeley.',
        "mendeley_body": (
            'Cuando inicia sesión con Mendeley, Rectoly solicita un token de acceso OAuth para leer y'
            ' sincronizar su biblioteca, documentos y anotaciones. Este token se almacena en el'
            ' Keychain de su dispositivo y nunca se envía a nuestros servidores: Rectoly se comunica'
            ' directamente con la API de Mendeley.'
        ),
        "docs_label": 'Sus documentos y anotaciones.',
        "docs_body": (
            'Los PDF que abre, junto con resaltados, subrayados, notas adhesivas y cualquier tinta'
            ' manuscrita que añada, se almacenan en su dispositivo. Si activa la copia de seguridad de'
            ' iCloud, estos datos — y, si lo acepta por separado, su escritura a mano — se respaldan'
            ' en su propia cuenta de iCloud mediante CloudKit de Apple. No tenemos acceso a estos'
            ' datos; están cifrados y vinculados a su Apple ID.'
        ),
        "crash_label": 'Informes de fallos y errores.',
        "crash_body": (
            'Rectoly usa Sentry para informar automáticamente de fallos y errores y así poder'
            ' corregirlos. Estos informes están configurados para excluir información personal: no se'
            ' recopila un identificador de usuario predeterminado ni una dirección IP, y los títulos'
            ' de documentos, rutas de archivo, direcciones de correo, tokens de autenticación y texto'
            ' de anotaciones se eliminan antes de enviar un informe.'
        ),
        "analytics_label": 'Análisis de uso anónimo.',
        "analytics_body": (
            'Rectoly usa TelemetryDeck para recopilar señales de uso anónimas y agregadas — por'
            ' ejemplo, qué pantallas se abren, si se completó la incorporación o si una sincronización'
            ' tuvo éxito o falló (como categoría general de motivo, no como texto de error en bruto).'
            ' Estas señales nunca incluyen títulos de documentos, rutas de archivo, direcciones de'
            ' correo ni contenido de anotaciones, y no están vinculadas a su identidad.'
        ),
        "purchases_label": 'Compras.',
        "purchases_body": (
            'Las suscripciones y las compras únicas las gestiona íntegramente Apple a través de'
            ' StoreKit. Recibimos la confirmación de que se realizó una compra; Rectoly no recopila ni'
            ' almacena sus datos de pago. La política de privacidad de Apple rige esos datos.'
        ),
        "h2_dont": 'Lo que no hacemos',
        "dont_sell": 'No vendemos sus datos.',
        "dont_ads": 'No ejecutamos publicidad ni SDK de seguimiento publicitario.',
        "dont_read": (
            'No leemos nosotros mismos el contenido de sus documentos o anotaciones: permanecen en su'
            ' dispositivo y, si lo activa, en su propia cuenta de iCloud.'
        ),
        "h2_third": 'Servicios de terceros',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'su biblioteca de referencias y sincronización de documentos',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'copia de seguridad opcional, regida por su Apple ID',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'informes de fallos y errores',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'análisis anónimo del producto',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'compras y suscripciones',
        "third_note": 'Cada uno de estos opera bajo su propia política de privacidad, que le animamos a revisar.',
        "h2_retention": 'Retención y eliminación de datos',
        "retention_body": (
            'Sus documentos, anotaciones y escritura a mano permanecen en su dispositivo hasta que'
            ' los elimine o elimine la app. Si la copia de seguridad de iCloud está activada, puede'
            ' desactivarla en los ajustes de Rectoly o eliminar los datos de iCloud de la app desde la'
            ' app Ajustes del dispositivo. Al desconectar su cuenta de Mendeley se elimina de'
            ' inmediato el token de acceso almacenado localmente.'
        ),
        "h2_children": 'Privacidad de menores',
        "children_body": 'Rectoly no está dirigido a menores de 13 años y no recopilamos conscientemente información de ellos.',
        "h2_changes": 'Cambios en esta política',
        "changes_body": (
            'Podemos actualizar esta política a medida que cambie la app. Los cambios sustanciales se'
            ' reflejarán aquí con una fecha actualizada.'
        ),
        "h2_contact": 'Contacto',
        "contact_before": 'Preguntas sobre esta política:',
        "footer": 'Rectoly es desarrollado por Hawk Eye.',
        "languages_label": 'Idiomas',
    },
    "zh-Hans": {
        "title": 'Rectoly — 隐私政策',
        "h1": 'Rectoly — 隐私政策',
        "updated": '最后更新于 2026 年 8 月 9 日',
        "intro": (
            'Hawk Eye（以下简称“我们”）开发了 Rectoly，这是一款用于阅读、批注学术 PDF，并与 Mendeley Reference Manager 同步的 iPad'
            ' 应用。本政策说明 Rectoly 收集哪些信息、为何收集以及如何处理。'
        ),
        "h2_collect": '我们收集的信息',
        "mendeley_label": '您的 Mendeley 账户连接。',
        "mendeley_body": (
            '当您使用 Mendeley 登录时，Rectoly 会请求 OAuth 访问令牌，以读取并同步您的文献库、文档和批注。该令牌保存在设备的 Keychain'
            ' 中，绝不会发送到我们的服务器——Rectoly 直接与 Mendeley 自身的 API 通信。'
        ),
        "docs_label": '您的文档与批注。',
        "docs_body": (
            '您打开的 PDF，以及高亮、下划线、便签和您添加的任何手写墨迹，均存储在您的设备上。如果启用 iCloud 备份，这些数据——以及在您另行选择加入时的手写内容——会通过'
            ' Apple 的 CloudKit 备份到您自己的 iCloud 账户。我们无法访问这些数据；它们经过加密，并限定在您的 Apple ID 范围内。'
        ),
        "crash_label": '崩溃与错误报告。',
        "crash_body": (
            'Rectoly 使用 Sentry 自动报告崩溃和错误，以便我们修复缺陷。这些报告经配置会排除个人信息：不收集默认用户标识符或 IP'
            ' 地址，并且在发送报告前会剥离文档标题、文件路径、电子邮件地址、身份验证令牌和批注文本。'
        ),
        "analytics_label": '匿名使用分析。',
        "analytics_body": (
            'Rectoly 使用 TelemetryDeck'
            ' 收集匿名、汇总的使用信号——例如打开了哪些屏幕、是否完成新手引导，或同步成功还是失败（作为一般原因类别，而非原始错误文本）。这些信号绝不包含文档标题、文件路径、电子邮件地址或批注内容，也不与您的身份关联。'
        ),
        "purchases_label": '购买。',
        "purchases_body": '订阅和一次性购买完全由 Apple 通过 StoreKit 处理。我们仅收到购买已完成的确认；Rectoly 不会收集或存储您的付款详情。该数据受 Apple 自身隐私政策约束。',
        "h2_dont": '我们不会做的事',
        "dont_sell": '我们不会出售您的数据。',
        "dont_ads": '我们不会运行广告或广告追踪 SDK。',
        "dont_read": '我们不会自行阅读您的文档或批注内容——它们保留在您的设备上，若您启用备份，则保留在您自己的 iCloud 账户中。',
        "h2_third": '第三方服务',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": '您的参考文献库与文档同步',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": '可选备份，由您的 Apple ID 管理',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": '崩溃与错误报告',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": '匿名产品分析',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": '购买与订阅',
        "third_note": '上述各项均受其各自隐私政策约束，我们建议您查阅。',
        "h2_retention": '数据保留与删除',
        "retention_body": (
            '您的文档、批注和手写内容会保留在设备上，直到您删除它们或删除应用。若已启用 iCloud 备份，可在 Rectoly 的设置中关闭，或在设备的“设置”应用中删除该应用的'
            ' iCloud 数据。断开 Mendeley 账户会立即移除本地存储的访问令牌。'
        ),
        "h2_children": '儿童隐私',
        "children_body": 'Rectoly 不面向 13 岁以下儿童，我们也不会故意收集他们的信息。',
        "h2_changes": '本政策的变更',
        "changes_body": '我们可能随应用变更而更新本政策。重大变更将在此以更新日期体现。',
        "h2_contact": '联系方式',
        "contact_before": '有关本政策的问题：',
        "footer": 'Rectoly 由 Hawk Eye 开发。',
        "languages_label": '语言',
    },
    "zh-Hant": {
        "title": 'Rectoly — 隱私權政策',
        "h1": 'Rectoly — 隱私權政策',
        "updated": '最後更新於 2026 年 8 月 9 日',
        "intro": (
            'Hawk Eye（以下稱「我們」）開發了 Rectoly，這是一款用於閱讀、註解學術 PDF，並與 Mendeley Reference Manager 同步的 iPad'
            ' App。本政策說明 Rectoly 收集哪些資訊、為何收集以及如何處理。'
        ),
        "h2_collect": '我們收集的資訊',
        "mendeley_label": '您的 Mendeley 帳戶連線。',
        "mendeley_body": (
            '當您使用 Mendeley 登入時，Rectoly 會請求 OAuth 存取權杖，以讀取並同步您的文獻庫、文件與註解。此權杖儲存在裝置的 Keychain'
            ' 中，絕不會傳送到我們的伺服器——Rectoly 直接與 Mendeley 自身的 API 通訊。'
        ),
        "docs_label": '您的文件與註解。',
        "docs_body": (
            '您開啟的 PDF，以及螢光標示、底線、便利貼，以及您新增的任何手寫墨跡，均儲存在您的裝置上。若啟用 iCloud 備份，這些資料——以及在您另行選擇加入時的手寫內容——會透過'
            ' Apple 的 CloudKit 備份到您自己的 iCloud 帳戶。我們無法存取這些資料；它們經過加密，並限定在您的 Apple ID 範圍內。'
        ),
        "crash_label": '當機與錯誤報告。',
        "crash_body": (
            'Rectoly 使用 Sentry 自動回報當機與錯誤，以便我們修復缺陷。這些報告經設定會排除個人資訊：不收集預設使用者識別碼或 IP'
            ' 位址，並且在傳送報告前會移除文件標題、檔案路徑、電子郵件地址、驗證權杖與註解文字。'
        ),
        "analytics_label": '匿名使用分析。',
        "analytics_body": (
            'Rectoly 使用 TelemetryDeck'
            ' 收集匿名、彙總的使用訊號——例如開啟了哪些畫面、是否完成新手引導，或同步成功還是失敗（作為一般原因類別，而非原始錯誤文字）。這些訊號絕不包含文件標題、檔案路徑、電子郵件地址或註解內容，也不與您的身分關聯。'
        ),
        "purchases_label": '購買。',
        "purchases_body": '訂閱與一次性購買完全由 Apple 透過 StoreKit 處理。我們僅收到購買已完成的確認；Rectoly 不會收集或儲存您的付款詳細資料。該資料受 Apple 自身隱私權政策約束。',
        "h2_dont": '我們不會做的事',
        "dont_sell": '我們不會出售您的資料。',
        "dont_ads": '我們不會執行廣告或廣告追蹤 SDK。',
        "dont_read": '我們不會自行閱讀您的文件或註解內容——它們保留在您的裝置上，若您啟用備份，則保留在您自己的 iCloud 帳戶中。',
        "h2_third": '第三方服務',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": '您的參考文獻庫與文件同步',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": '選用備份，由您的 Apple ID 管理',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": '當機與錯誤回報',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": '匿名產品分析',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": '購買與訂閱',
        "third_note": '上述各項均受其各自隱私權政策約束，我們建議您查閱。',
        "h2_retention": '資料保留與刪除',
        "retention_body": (
            '您的文件、註解與手寫內容會保留在裝置上，直到您刪除它們或刪除 App。若已啟用 iCloud 備份，可在 Rectoly 的設定中關閉，或在裝置的「設定」App 中刪除該'
            ' App 的 iCloud 資料。中斷連線 Mendeley 帳戶會立即移除本機儲存的存取權杖。'
        ),
        "h2_children": '兒童隱私',
        "children_body": 'Rectoly 不針對 13 歲以下兒童，我們也不會故意收集他們的資訊。',
        "h2_changes": '本政策的變更',
        "changes_body": '我們可能隨 App 變更而更新本政策。重大變更將在此以更新日期呈現。',
        "h2_contact": '聯絡方式',
        "contact_before": '有關本政策的問題：',
        "footer": 'Rectoly 由 Hawk Eye 開發。',
        "languages_label": '語言',
    },
    "fr": {
        "title": 'Rectoly — Politique de confidentialité',
        "h1": 'Rectoly — Politique de confidentialité',
        "updated": 'Dernière mise à jour le 9 août 2026',
        "intro": (
            'Hawk Eye (« nous ») développe Rectoly, une app iPad pour lire, annoter et synchroniser'
            ' des PDF académiques avec Mendeley Reference Manager. Cette politique explique quelles'
            ' informations Rectoly collecte, pourquoi et comment elles sont traitées.'
        ),
        "h2_collect": 'Informations que nous collectons',
        "mendeley_label": 'La connexion de votre compte Mendeley.',
        "mendeley_body": (
            'Lorsque vous vous connectez avec Mendeley, Rectoly demande un jeton d’accès OAuth pour'
            ' lire et synchroniser votre bibliothèque, vos documents et vos annotations. Ce jeton est'
            ' stocké dans le Keychain de votre appareil et n’est jamais envoyé à nos serveurs —'
            ' Rectoly communique directement avec l’API de Mendeley.'
        ),
        "docs_label": 'Vos documents et annotations.',
        "docs_body": (
            'Les PDF que vous ouvrez, ainsi que les surlignages, soulignements, notes autocollantes'
            ' et toute encre manuscrite que vous ajoutez, sont stockés sur votre appareil. Si vous'
            ' activez la sauvegarde iCloud, ces données — et, si vous y consentez séparément, votre'
            ' écriture manuscrite — sont sauvegardées sur votre propre compte iCloud via CloudKit'
            ' d’Apple. Nous n’avons pas accès à ces données ; elles sont chiffrées et limitées à votre'
            ' Apple ID.'
        ),
        "crash_label": 'Rapports de plantages et d’erreurs.',
        "crash_body": (
            'Rectoly utilise Sentry pour signaler automatiquement les plantages et les erreurs afin'
            ' que nous puissions corriger les bugs. Ces rapports sont configurés pour exclure les'
            ' informations personnelles : aucun identifiant utilisateur par défaut ni adresse IP n’est'
            ' collecté, et les titres de documents, chemins de fichiers, adresses e-mail, jetons'
            ' d’authentification et textes d’annotation sont retirés avant l’envoi d’un rapport.'
        ),
        "analytics_label": 'Analyses d’utilisation anonymes.',
        "analytics_body": (
            'Rectoly utilise TelemetryDeck pour collecter des signaux d’utilisation anonymes et'
            ' agrégés — par exemple, quels écrans sont ouverts, si l’onboarding a été terminé, ou si'
            ' une synchronisation a réussi ou échoué (en tant que catégorie de motif générale, et non'
            ' en texte d’erreur brut). Ces signaux n’incluent jamais les titres de documents, chemins'
            ' de fichiers, adresses e-mail ou contenu d’annotations, et ne sont pas liés à votre'
            ' identité.'
        ),
        "purchases_label": 'Achats.',
        "purchases_body": (
            'Les abonnements et les achats uniques sont entièrement gérés par Apple via StoreKit.'
            ' Nous recevons la confirmation qu’un achat a été effectué ; Rectoly ne collecte ni ne'
            ' stocke vos informations de paiement. La politique de confidentialité d’Apple régit ces'
            ' données.'
        ),
        "h2_dont": 'Ce que nous ne faisons pas',
        "dont_sell": 'Nous ne vendons pas vos données.',
        "dont_ads": 'Nous n’utilisons pas de publicité ni de SDK de suivi publicitaire.',
        "dont_read": (
            'Nous ne lisons pas nous-mêmes le contenu de vos documents ou annotations — ils restent'
            ' sur votre appareil et, si vous l’activez, dans votre propre compte iCloud.'
        ),
        "h2_third": 'Services tiers',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'votre bibliothèque de références et la synchronisation des documents',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'sauvegarde facultative, régie par votre Apple ID',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'rapports de plantages et d’erreurs',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'analyses anonymes du produit',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'achats et abonnements',
        "third_note": (
            'Chacun de ces services fonctionne selon sa propre politique de confidentialité, que nous'
            ' vous encourageons à consulter.'
        ),
        "h2_retention": 'Conservation et suppression des données',
        "retention_body": (
            'Vos documents, annotations et écriture manuscrite restent sur votre appareil jusqu’à ce'
            ' que vous les supprimiez ou que vous supprimiez l’app. Si la sauvegarde iCloud est'
            ' activée, vous pouvez la désactiver dans les réglages de Rectoly, ou supprimer les'
            ' données iCloud de l’app depuis l’app Réglages de votre appareil. La déconnexion de votre'
            ' compte Mendeley supprime immédiatement le jeton d’accès stocké localement.'
        ),
        "h2_children": 'Confidentialité des enfants',
        "children_body": (
            'Rectoly ne s’adresse pas aux enfants de moins de 13 ans, et nous ne collectons pas'
            ' sciemment d’informations les concernant.'
        ),
        "h2_changes": 'Modifications de cette politique',
        "changes_body": (
            'Nous pouvons mettre à jour cette politique à mesure que l’app évolue. Les changements'
            ' importants seront reflétés ici avec une date mise à jour.'
        ),
        "h2_contact": 'Contact',
        "contact_before": 'Questions concernant cette politique :',
        "footer": 'Rectoly est développé par Hawk Eye.',
        "languages_label": 'Langues',
    },
    "it": {
        "title": 'Rectoly — Informativa sulla privacy',
        "h1": 'Rectoly — Informativa sulla privacy',
        "updated": 'Ultimo aggiornamento: 9 agosto 2026',
        "intro": (
            'Hawk Eye ("noi") sviluppa Rectoly, un\'app per iPad per leggere, annotare e sincronizzare'
            ' PDF accademici con Mendeley Reference Manager. Questa informativa spiega quali'
            ' informazioni Rectoly raccoglie, perché e come vengono gestite.'
        ),
        "h2_collect": 'Informazioni che raccogliamo',
        "mendeley_label": 'La connessione del tuo account Mendeley.',
        "mendeley_body": (
            'Quando accedi con Mendeley, Rectoly richiede un token di accesso OAuth per leggere e'
            ' sincronizzare la tua libreria, i documenti e le annotazioni. Questo token viene'
            ' memorizzato nel Keychain del tuo dispositivo e non viene mai inviato ai nostri server:'
            " Rectoly comunica direttamente con l'API di Mendeley."
        ),
        "docs_label": 'I tuoi documenti e le annotazioni.',
        "docs_body": (
            'I PDF che apri, insieme a evidenziazioni, sottolineature, note adesive e qualsiasi'
            ' inchiostro manoscritto che aggiungi, sono memorizzati sul tuo dispositivo. Se attivi il'
            ' backup di iCloud, questi dati — e, se acconsenti separatamente, la tua scrittura a mano'
            ' — vengono salvati sul tuo account iCloud tramite CloudKit di Apple. Non abbiamo accesso'
            ' a questi dati; sono crittografati e collegati al tuo Apple ID.'
        ),
        "crash_label": 'Segnalazioni di arresti anomali ed errori.',
        "crash_body": (
            'Rectoly usa Sentry per segnalare automaticamente arresti anomali ed errori così da poter'
            ' correggere i bug. Queste segnalazioni sono configurate per escludere informazioni'
            ' personali: non viene raccolto un identificatore utente predefinito né un indirizzo IP, e'
            ' titoli dei documenti, percorsi dei file, indirizzi e-mail, token di autenticazione e'
            " testo delle annotazioni vengono rimossi prima dell'invio di una segnalazione."
        ),
        "analytics_label": 'Analisi di utilizzo anonime.',
        "analytics_body": (
            'Rectoly usa TelemetryDeck per raccogliere segnali di utilizzo anonimi e aggregati — ad'
            " esempio, quali schermate vengono aperte, se l'onboarding è stato completato o se una"
            ' sincronizzazione è riuscita o fallita (come categoria generale di motivo, non come testo'
            ' di errore grezzo). Questi segnali non includono mai titoli di documenti, percorsi di'
            ' file, indirizzi e-mail o contenuto delle annotazioni, e non sono collegati alla tua'
            ' identità.'
        ),
        "purchases_label": 'Acquisti.',
        "purchases_body": (
            'Gli abbonamenti e gli acquisti una tantum sono gestiti interamente da Apple tramite'
            ' StoreKit. Riceviamo la conferma che un acquisto è stato effettuato; Rectoly non'
            " raccoglie né memorizza i tuoi dati di pagamento. L'informativa sulla privacy di Apple"
            ' regola tali dati.'
        ),
        "h2_dont": 'Cosa non facciamo',
        "dont_sell": 'Non vendiamo i tuoi dati.',
        "dont_ads": 'Non utilizziamo pubblicità né SDK di tracciamento pubblicitario.',
        "dont_read": (
            'Non leggiamo noi stessi il contenuto dei tuoi documenti o annotazioni: restano sul tuo'
            ' dispositivo e, se lo attivi, nel tuo account iCloud.'
        ),
        "h2_third": 'Servizi di terze parti',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'la tua libreria di riferimenti e la sincronizzazione dei documenti',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'backup opzionale, regolato dal tuo Apple ID',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'segnalazione di arresti anomali ed errori',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'analisi anonime del prodotto',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'acquisti e abbonamenti',
        "third_note": 'Ognuno di questi opera secondo la propria informativa sulla privacy, che ti invitiamo a consultare.',
        "h2_retention": 'Conservazione ed eliminazione dei dati',
        "retention_body": (
            'I tuoi documenti, annotazioni e scrittura a mano rimangono sul tuo dispositivo finché'
            " non li elimini o non elimini l'app. Se il backup di iCloud è attivato, puoi disattivarlo"
            " nelle impostazioni di Rectoly oppure rimuovere i dati iCloud dell'app dall'app"
            ' Impostazioni del dispositivo. La disconnessione del tuo account Mendeley rimuove'
            ' immediatamente il token di accesso memorizzato localmente.'
        ),
        "h2_children": 'Privacy dei minori',
        "children_body": 'Rectoly non è destinato a minori di 13 anni e non raccogliamo consapevolmente informazioni da loro.',
        "h2_changes": 'Modifiche a questa informativa',
        "changes_body": (
            "Potremmo aggiornare questa informativa man mano che l'app cambia. Le modifiche"
            ' sostanziali saranno riportate qui con una data aggiornata.'
        ),
        "h2_contact": 'Contatti',
        "contact_before": 'Domande su questa informativa:',
        "footer": 'Rectoly è sviluppato da Hawk Eye.',
        "languages_label": 'Lingue',
    },
    "da": {
        "title": 'Rectoly — Privatlivspolitik',
        "h1": 'Rectoly — Privatlivspolitik',
        "updated": 'Senest opdateret 9. august 2026',
        "intro": (
            'Hawk Eye ("vi", "os") udvikler Rectoly, en iPad-app til at læse, annotere og'
            " synkronisere akademiske PDF'er med Mendeley Reference Manager. Denne politik forklarer,"
            ' hvilke oplysninger Rectoly indsamler, hvorfor og hvordan de håndteres.'
        ),
        "h2_collect": 'Oplysninger, vi indsamler',
        "mendeley_label": 'Din Mendeley-kontoforbindelse.',
        "mendeley_body": (
            'Når du logger ind med Mendeley, anmoder Rectoly om et OAuth-adgangstoken for at læse og'
            ' synkronisere dit bibliotek, dokumenter og annotationer. Dette token gemmes i enhedens'
            ' Keychain og sendes aldrig til vores servere — Rectoly kommunikerer direkte med Mendeleys'
            ' egen API.'
        ),
        "docs_label": 'Dine dokumenter og annotationer.',
        "docs_body": (
            "PDF'er, du åbner, sammen med fremhævninger, understregninger, sticky notes og"
            ' håndskrevet blæk, du tilføjer, gemmes på din enhed. Hvis du aktiverer'
            ' iCloud-sikkerhedskopiering, sikkerhedskopieres disse data — og, hvis du særskilt'
            ' tilmelder dig, din håndskrift — til din egen iCloud-konto via Apples CloudKit. Vi har'
            ' ikke adgang til disse data; de er krypterede og knyttet til dit Apple ID.'
        ),
        "crash_label": 'Nedbruds- og fejlrapporter.',
        "crash_body": (
            'Rectoly bruger Sentry til automatisk at rapportere nedbrud og fejl, så vi kan rette'
            ' bugs. Disse rapporter er konfigureret til at udelukke personlige oplysninger: der'
            ' indsamles ingen standard brugeridentifikator eller IP-adresse, og dokumenttitler,'
            ' filstier, e-mailadresser, godkendelsestokens og annotationstekst fjernes, før en rapport'
            ' sendes.'
        ),
        "analytics_label": 'Anonym brugsanalyse.',
        "analytics_body": (
            'Rectoly bruger TelemetryDeck til at indsamle anonyme, aggregerede brugssignaler — for'
            ' eksempel hvilke skærme der åbnes, om onboarding blev fuldført, eller om en'
            ' synkronisering lykkedes eller mislykkedes (som en generel årsagskategori, ikke rå'
            ' fejltekst). Disse signaler indeholder aldrig dokumenttitler, filstier, e-mailadresser'
            ' eller annotationsindhold og er ikke knyttet til din identitet.'
        ),
        "purchases_label": 'Køb.',
        "purchases_body": (
            'Abonnementer og engangskøb håndteres udelukkende af Apple via StoreKit. Vi modtager'
            ' bekræftelse på, at et køb er foretaget; Rectoly indsamler eller gemmer ikke dine'
            ' betalingsoplysninger. Apples egen privatlivspolitik gælder for disse data.'
        ),
        "h2_dont": 'Hvad vi ikke gør',
        "dont_sell": 'Vi sælger ikke dine data.',
        "dont_ads": "Vi kører ikke reklamer eller ad-tracking-SDK'er.",
        "dont_read": (
            'Vi læser ikke selv indholdet af dine dokumenter eller annotationer — de forbliver på din'
            ' enhed og, hvis du aktiverer det, på din egen iCloud-konto.'
        ),
        "h2_third": 'Tredjepartstjenester',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'dit referencelbibliotek og dokumentsynkronisering',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'valgfri sikkerhedskopiering, styret af dit Apple ID',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'rapportering af nedbrud og fejl',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'anonym produktanalyse',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'køb og abonnementer',
        "third_note": 'Hver af disse opererer under sin egen privatlivspolitik, som vi opfordrer dig til at gennemgå.',
        "h2_retention": 'Dataopbevaring og sletning',
        "retention_body": (
            'Dine dokumenter, annotationer og håndskrift forbliver på din enhed, indtil du sletter'
            ' dem eller sletter appen. Hvis iCloud-sikkerhedskopiering er aktiveret, kan du slå den'
            ' fra i Rectolys indstillinger eller fjerne appens iCloud-data fra enhedens'
            ' Indstillinger-app. Frakobling af din Mendeley-konto fjerner straks det lokalt gemte'
            ' adgangstoken.'
        ),
        "h2_children": 'Børns privatliv',
        "children_body": 'Rectoly er ikke rettet mod børn under 13 år, og vi indsamler ikke bevidst oplysninger fra dem.',
        "h2_changes": 'Ændringer af denne politik',
        "changes_body": (
            'Vi kan opdatere denne politik, efterhånden som appen ændrer sig. Væsentlige ændringer'
            ' vil blive afspejlet her med en opdateret dato.'
        ),
        "h2_contact": 'Kontakt',
        "contact_before": 'Spørgsmål om denne politik:',
        "footer": 'Rectoly er udviklet af Hawk Eye.',
        "languages_label": 'Sprog',
    },
    "ko": {
        "title": 'Rectoly — 개인정보 처리방침',
        "h1": 'Rectoly — 개인정보 처리방침',
        "updated": '최종 업데이트: 2026년 8월 9일',
        "intro": (
            'Hawk Eye(“당사”)는 Mendeley Reference Manager와 함께 학술 PDF를 읽고, 주석을 달고, 동기화하는 iPad 앱 Rectoly를'
            ' 개발합니다. 본 방침은 Rectoly가 어떤 정보를 수집하는지, 왜 수집하는지, 어떻게 처리하는지를 설명합니다.'
        ),
        "h2_collect": '수집하는 정보',
        "mendeley_label": 'Mendeley 계정 연결.',
        "mendeley_body": (
            'Mendeley로 로그인하면 Rectoly는 라이브러리, 문서, 주석을 읽고 동기화하기 위해 OAuth 액세스 토큰을 요청합니다. 이 토큰은 기기의'
            ' Keychain에 저장되며 당사 서버로 전송되지 않습니다. Rectoly는 Mendeley 자체의 API와 직접 통신합니다.'
        ),
        "docs_label": '문서 및 주석.',
        "docs_body": (
            '열어본 PDF와 하이라이트, 밑줄, 스티키 노트, 추가한 손글씨 잉크는 모두 기기에 저장됩니다. iCloud 백업을 켜면 이 데이터(그리고 별도로 동의한 경우'
            ' 손글씨)가 Apple의 CloudKit을 통해 본인 iCloud 계정에 백업됩니다. 당사는 이 데이터에 접근할 수 없으며, 데이터는 암호화되어 Apple ID'
            ' 범위로 제한됩니다.'
        ),
        "crash_label": '충돌 및 오류 보고서.',
        "crash_body": (
            'Rectoly는 버그 수정을 위해 Sentry를 사용해 충돌과 오류를 자동으로 보고합니다. 이러한 보고서는 개인정보를 제외하도록 구성되어 있습니다. 기본'
            ' 사용자 식별자나 IP 주소는 수집되지 않으며, 문서 제목, 파일 경로, 이메일 주소, 인증 토큰, 주석 텍스트는 보고서가 전송되기 전에 제거됩니다.'
        ),
        "analytics_label": '익명 사용 분석.',
        "analytics_body": (
            'Rectoly는 TelemetryDeck을 사용해 익명·집계된 사용 신호를 수집합니다. 예를 들어 어떤 화면이 열렸는지, 온보딩이 완료되었는지, 동기화가'
            ' 성공했는지 또는 실패했는지(일반 사유 범주이며 원시 오류 텍스트가 아님) 등입니다. 이러한 신호에는 문서 제목, 파일 경로, 이메일 주소, 주석 내용이'
            ' 포함되지 않으며 신원과도 연결되지 않습니다.'
        ),
        "purchases_label": '구매.',
        "purchases_body": (
            '구독 및 일회성 구매는 전적으로 Apple이 StoreKit을 통해 처리합니다. 당사는 구매가 이루어졌다는 확인만 받으며, Rectoly는 결제 세부정보를'
            ' 수집하거나 저장하지 않습니다. 해당 데이터는 Apple 자체의 개인정보 처리방침이 적용됩니다.'
        ),
        "h2_dont": '하지 않는 일',
        "dont_sell": '귀하의 데이터를 판매하지 않습니다.',
        "dont_ads": '광고 또는 광고 추적 SDK를 실행하지 않습니다.',
        "dont_read": '문서나 주석의 내용을 당사가 직접 읽지 않습니다. 해당 내용은 기기에 남아 있으며, 활성화한 경우 본인 iCloud 계정에 남습니다.',
        "h2_third": '제3자 서비스',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": '참고문헌 라이브러리 및 문서 동기화',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": '선택적 백업(Apple ID로 관리)',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": '충돌 및 오류 보고',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": '익명 제품 분석',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": '구매 및 구독',
        "third_note": '각 서비스는 자체 개인정보 처리방침에 따라 운영되며, 검토를 권장합니다.',
        "h2_retention": '데이터 보관 및 삭제',
        "retention_body": (
            '문서, 주석, 손글씨는 삭제하거나 앱을 삭제할 때까지 기기에 남습니다. iCloud 백업이 켜져 있으면 Rectoly 설정에서 끄거나 기기의 설정 앱에서 해당'
            ' 앱의 iCloud 데이터를 제거할 수 있습니다. Mendeley 계정 연결을 해제하면 로컬에 저장된 액세스 토큰이 즉시 제거됩니다.'
        ),
        "h2_children": '아동의 개인정보',
        "children_body": 'Rectoly는 13세 미만 아동을 대상으로 하지 않으며, 고의로 아동의 정보를 수집하지 않습니다.',
        "h2_changes": '본 방침의 변경',
        "changes_body": '앱이 변경됨에 따라 본 방침을 업데이트할 수 있습니다. 중요한 변경 사항은 업데이트된 날짜와 함께 여기에 반영됩니다.',
        "h2_contact": '문의',
        "contact_before": '본 방침에 대한 문의:',
        "footer": 'Rectoly는 Hawk Eye가 개발합니다.',
        "languages_label": '언어',
    },
    "pt-BR": {
        "title": 'Rectoly — Política de Privacidade',
        "h1": 'Rectoly — Política de Privacidade',
        "updated": 'Última atualização em 9 de agosto de 2026',
        "intro": (
            'A Hawk Eye ("nós") desenvolve o Rectoly, um app para iPad para ler, anotar e sincronizar'
            ' PDFs acadêmicos com o Mendeley Reference Manager. Esta política explica quais'
            ' informações o Rectoly coleta, por quê e como elas são tratadas.'
        ),
        "h2_collect": 'Informações que coletamos',
        "mendeley_label": 'A conexão da sua conta Mendeley.',
        "mendeley_body": (
            'Ao entrar com o Mendeley, o Rectoly solicita um token de acesso OAuth para ler e'
            ' sincronizar sua biblioteca, documentos e anotações. Esse token é armazenado no Keychain'
            ' do seu dispositivo e nunca é enviado aos nossos servidores — o Rectoly se comunica'
            ' diretamente com a API do próprio Mendeley.'
        ),
        "docs_label": 'Seus documentos e anotações.',
        "docs_body": (
            'Os PDFs que você abre, juntamente com destaques, sublinhados, notas adesivas e qualquer'
            ' tinta manuscrita que adicionar, são armazenados no seu dispositivo. Se você ativar o'
            ' backup do iCloud, esses dados — e, se optar separadamente, sua escrita à mão — são'
            ' salvos na sua própria conta iCloud via CloudKit da Apple. Não temos acesso a esses'
            ' dados; eles são criptografados e vinculados ao seu Apple ID.'
        ),
        "crash_label": 'Relatórios de falhas e erros.',
        "crash_body": (
            'O Rectoly usa o Sentry para relatar automaticamente falhas e erros, para que possamos'
            ' corrigir bugs. Esses relatórios são configurados para excluir informações pessoais:'
            ' nenhum identificador de usuário padrão nem endereço IP é coletado, e títulos de'
            ' documentos, caminhos de arquivo, endereços de e-mail, tokens de autenticação e texto de'
            ' anotações são removidos antes do envio de um relatório.'
        ),
        "analytics_label": 'Análises de uso anônimas.',
        "analytics_body": (
            'O Rectoly usa o TelemetryDeck para coletar sinais de uso anônimos e agregados — por'
            ' exemplo, quais telas são abertas, se a introdução foi concluída ou se uma sincronização'
            ' teve êxito ou falhou (como categoria geral de motivo, não como texto bruto de erro).'
            ' Esses sinais nunca incluem títulos de documentos, caminhos de arquivo, endereços de'
            ' e-mail ou conteúdo de anotações, e não estão vinculados à sua identidade.'
        ),
        "purchases_label": 'Compras.',
        "purchases_body": (
            'Assinaturas e compras únicas são tratadas inteiramente pela Apple por meio do StoreKit.'
            ' Recebemos a confirmação de que uma compra foi feita; o Rectoly não coleta nem armazena'
            ' seus dados de pagamento. A própria política de privacidade da Apple rege esses dados.'
        ),
        "h2_dont": 'O que não fazemos',
        "dont_sell": 'Não vendemos seus dados.',
        "dont_ads": 'Não executamos publicidade nem SDKs de rastreamento de anúncios.',
        "dont_read": (
            'Não lemos nós mesmos o conteúdo dos seus documentos ou anotações — eles permanecem no'
            ' seu dispositivo e, se você ativar, na sua própria conta iCloud.'
        ),
        "h2_third": 'Serviços de terceiros',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'sua biblioteca de referências e sincronização de documentos',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'backup opcional, regido pelo seu Apple ID',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'relatórios de falhas e erros',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'análises anônimas do produto',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'compras e assinaturas',
        "third_note": 'Cada um deles opera sob sua própria política de privacidade, que recomendamos que você revise.',
        "h2_retention": 'Retenção e exclusão de dados',
        "retention_body": (
            'Seus documentos, anotações e escrita à mão permanecem no seu dispositivo até que você os'
            ' exclua ou exclua o app. Se o backup do iCloud estiver ativado, você pode desativá-lo nas'
            ' configurações do Rectoly ou remover os dados do iCloud do app no app Ajustes do'
            ' dispositivo. Desconectar sua conta Mendeley remove imediatamente o token de acesso'
            ' armazenado localmente.'
        ),
        "h2_children": 'Privacidade de crianças',
        "children_body": (
            'O Rectoly não é direcionado a crianças menores de 13 anos, e não coletamos'
            ' intencionalmente informações delas.'
        ),
        "h2_changes": 'Alterações nesta política',
        "changes_body": (
            'Podemos atualizar esta política conforme o app muda. Alterações materiais serão'
            ' refletidas aqui com uma data atualizada.'
        ),
        "h2_contact": 'Contato',
        "contact_before": 'Dúvidas sobre esta política:',
        "footer": 'O Rectoly é desenvolvido pela Hawk Eye.',
        "languages_label": 'Idiomas',
    },
    "nl": {
        "title": 'Rectoly — Privacybeleid',
        "h1": 'Rectoly — Privacybeleid',
        "updated": 'Laatst bijgewerkt op 9 augustus 2026',
        "intro": (
            'Hawk Eye ("wij", "ons") ontwikkelt Rectoly, een iPad-app voor het lezen, annoteren en'
            " synchroniseren van academische PDF's met Mendeley Reference Manager. Dit beleid legt uit"
            ' welke informatie Rectoly verzamelt, waarom en hoe deze wordt verwerkt.'
        ),
        "h2_collect": 'Informatie die we verzamelen',
        "mendeley_label": 'Uw Mendeley-accountkoppeling.',
        "mendeley_body": (
            'Wanneer u zich aanmeldt met Mendeley, vraagt Rectoly een OAuth-toegangstoken aan om uw'
            ' bibliotheek, documenten en annotaties te lezen en te synchroniseren. Dit token wordt'
            ' opgeslagen in de Keychain van uw apparaat en wordt nooit naar onze servers gestuurd —'
            ' Rectoly communiceert rechtstreeks met de API van Mendeley.'
        ),
        "docs_label": 'Uw documenten en annotaties.',
        "docs_body": (
            "PDF's die u opent, samen met markeringen, onderstrepingen, plaknotities en"
            ' handgeschreven inkt die u toevoegt, worden op uw apparaat opgeslagen. Als u'
            ' iCloud-back-up inschakelt, worden deze gegevens — en, als u daar apart voor kiest, uw'
            " handschrift — via Apple's CloudKit geback-upt naar uw eigen iCloud-account. Wij hebben"
            ' geen toegang tot deze gegevens; ze zijn versleuteld en gekoppeld aan uw Apple ID.'
        ),
        "crash_label": 'Crash- en foutrapporten.',
        "crash_body": (
            'Rectoly gebruikt Sentry om crashes en fouten automatisch te melden, zodat we bugs kunnen'
            ' oplossen. Deze rapporten zijn zo geconfigureerd dat persoonlijke informatie wordt'
            ' uitgesloten: er wordt geen standaard gebruikersidentificatie of IP-adres verzameld, en'
            ' documenttitels, bestandspaden, e-mailadressen, authenticatietokens en annotatietekst'
            ' worden verwijderd voordat een rapport wordt verzonden.'
        ),
        "analytics_label": 'Anonieme gebruiksanalyses.',
        "analytics_body": (
            'Rectoly gebruikt TelemetryDeck om anonieme, geaggregeerde gebruikssignalen te verzamelen'
            ' — bijvoorbeeld welke schermen worden geopend, of de onboarding is voltooid, of of een'
            ' synchronisatie is geslaagd of mislukt (als algemene redencategorie, niet als ruwe'
            ' fouttekst). Deze signalen bevatten nooit documenttitels, bestandspaden, e-mailadressen'
            ' of annotatie-inhoud, en zijn niet gekoppeld aan uw identiteit.'
        ),
        "purchases_label": 'Aankopen.',
        "purchases_body": (
            'Abonnementen en eenmalige aankopen worden volledig door Apple via StoreKit afgehandeld.'
            ' Wij ontvangen de bevestiging dat een aankoop is gedaan; Rectoly verzamelt of bewaart uw'
            ' betalingsgegevens niet. Het privacybeleid van Apple is van toepassing op die gegevens.'
        ),
        "h2_dont": 'Wat we niet doen',
        "dont_sell": 'Wij verkopen uw gegevens niet.',
        "dont_ads": "Wij gebruiken geen advertenties of ad-tracking-SDK's.",
        "dont_read": (
            'Wij lezen zelf niet de inhoud van uw documenten of annotaties — die blijven op uw'
            ' apparaat en, als u dit inschakelt, in uw eigen iCloud-account.'
        ),
        "h2_third": 'Diensten van derden',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'uw referentiebibliotheek en documentsynchronisatie',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'optionele back-up, beheerd via uw Apple ID',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'crash- en foutrapportage',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'anonieme productanalyses',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'aankopen en abonnementen',
        "third_note": 'Elk van deze diensten werkt volgens het eigen privacybeleid, dat we u aanraden te raadplegen.',
        "h2_retention": 'Gegevensbewaring en verwijdering',
        "retention_body": (
            'Uw documenten, annotaties en handschrift blijven op uw apparaat totdat u ze verwijdert'
            ' of de app verwijdert. Als iCloud-back-up is ingeschakeld, kunt u deze uitschakelen in de'
            ' instellingen van Rectoly, of de iCloud-gegevens van de app verwijderen via de'
            ' Instellingen-app van uw apparaat. Het ontkoppelen van uw Mendeley-account verwijdert het'
            ' lokaal opgeslagen toegangstoken onmiddellijk.'
        ),
        "h2_children": 'Privacy van kinderen',
        "children_body": 'Rectoly is niet gericht op kinderen onder de 13, en wij verzamelen niet bewust informatie van hen.',
        "h2_changes": 'Wijzigingen in dit beleid',
        "changes_body": (
            'Wij kunnen dit beleid bijwerken naarmate de app verandert. Materiële wijzigingen worden'
            ' hier weergegeven met een bijgewerkte datum.'
        ),
        "h2_contact": 'Contact',
        "contact_before": 'Vragen over dit beleid:',
        "footer": 'Rectoly wordt ontwikkeld door Hawk Eye.',
        "languages_label": 'Talen',
    },
    "sv": {
        "title": 'Rectoly — Integritetspolicy',
        "h1": 'Rectoly — Integritetspolicy',
        "updated": 'Senast uppdaterad den 9 augusti 2026',
        "intro": (
            'Hawk Eye ("vi", "oss") utvecklar Rectoly, en iPad-app för att läsa, annotera och'
            ' synkronisera akademiska PDF-filer med Mendeley Reference Manager. Denna policy förklarar'
            ' vilken information Rectoly samlar in, varför och hur den hanteras.'
        ),
        "h2_collect": 'Information vi samlar in',
        "mendeley_label": 'Din Mendeley-kontokoppling.',
        "mendeley_body": (
            'När du loggar in med Mendeley begär Rectoly en OAuth-åtkomsttoken för att läsa och'
            ' synkronisera ditt bibliotek, dokument och anteckningar. Denna token lagras i enhetens'
            ' Keychain och skickas aldrig till våra servrar — Rectoly kommunicerar direkt med'
            ' Mendeleys egen API.'
        ),
        "docs_label": 'Dina dokument och anteckningar.',
        "docs_body": (
            'PDF-filer du öppnar, tillsammans med markeringar, understrykningar, klisterlappar och'
            ' handskriven bläck som du lägger till, lagras på din enhet. Om du aktiverar'
            ' iCloud-säkerhetskopiering säkerhetskopieras dessa data — och, om du separat väljer det,'
            ' din handskrift — till ditt eget iCloud-konto via Apples CloudKit. Vi har inte tillgång'
            ' till dessa data; de är krypterade och knutna till ditt Apple-ID.'
        ),
        "crash_label": 'Kraschrapporter och felrapporter.',
        "crash_body": (
            'Rectoly använder Sentry för att automatiskt rapportera krascher och fel så att vi kan'
            ' åtgärda buggar. Dessa rapporter är konfigurerade att utesluta personlig information:'
            ' ingen standardanvändaridentifierare eller IP-adress samlas in, och dokumenttitlar,'
            ' filsökvägar, e-postadresser, autentiseringstokens och anteckningstext tas bort innan en'
            ' rapport skickas.'
        ),
        "analytics_label": 'Anonym användningsanalys.',
        "analytics_body": (
            'Rectoly använder TelemetryDeck för att samla in anonyma, aggregerade användningssignaler'
            ' — till exempel vilka skärmar som öppnas, om introduktionen slutfördes, eller om en'
            ' synkronisering lyckades eller misslyckades (som en allmän orsakskategori, inte rå'
            ' feltext). Dessa signaler inkluderar aldrig dokumenttitlar, filsökvägar, e-postadresser'
            ' eller anteckningsinnehåll och är inte knutna till din identitet.'
        ),
        "purchases_label": 'Köp.',
        "purchases_body": (
            'Prenumerationer och engångsköp hanteras helt av Apple via StoreKit. Vi får bekräftelse'
            ' på att ett köp har gjorts; Rectoly samlar inte in eller lagrar dina betalningsuppgifter.'
            ' Apples egen integritetspolicy gäller för dessa data.'
        ),
        "h2_dont": 'Vad vi inte gör',
        "dont_sell": 'Vi säljer inte dina data.',
        "dont_ads": 'Vi kör inte reklam eller SDK:er för annonsspårning.',
        "dont_read": (
            'Vi läser inte själva innehållet i dina dokument eller anteckningar — de finns kvar på'
            ' din enhet och, om du aktiverar det, i ditt eget iCloud-konto.'
        ),
        "h2_third": 'Tredjepartstjänster',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'ditt referensbibliotek och dokumentsynkronisering',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'valfri säkerhetskopiering, styrd av ditt Apple-ID',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'rapportering av krascher och fel',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'anonym produktanalys',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'köp och prenumerationer',
        "third_note": 'Var och en av dessa verkar under sin egen integritetspolicy, som vi uppmuntrar dig att granska.',
        "h2_retention": 'Datalagring och radering',
        "retention_body": (
            'Dina dokument, anteckningar och handskrift finns kvar på din enhet tills du raderar dem'
            ' eller raderar appen. Om iCloud-säkerhetskopiering är aktiverad kan du stänga av den i'
            ' Rectolys inställningar eller ta bort appens iCloud-data från enhetens Inställningar-app.'
            ' Om du kopplar bort ditt Mendeley-konto tas den lokalt lagrade åtkomsttoken bort'
            ' omedelbart.'
        ),
        "h2_children": 'Barns integritet',
        "children_body": 'Rectoly riktar sig inte till barn under 13 år, och vi samlar inte medvetet in information från dem.',
        "h2_changes": 'Ändringar av denna policy',
        "changes_body": (
            'Vi kan uppdatera denna policy när appen förändras. Väsentliga ändringar återspeglas här'
            ' med ett uppdaterat datum.'
        ),
        "h2_contact": 'Kontakt',
        "contact_before": 'Frågor om denna policy:',
        "footer": 'Rectoly utvecklas av Hawk Eye.',
        "languages_label": 'Språk',
    },
    "nb": {
        "title": 'Rectoly — Personvernerklæring',
        "h1": 'Rectoly — Personvernerklæring',
        "updated": 'Sist oppdatert 9. august 2026',
        "intro": (
            'Hawk Eye ("vi", "oss") utvikler Rectoly, en iPad-app for å lese, annotere og'
            ' synkronisere akademiske PDF-er med Mendeley Reference Manager. Denne erklæringen'
            ' forklarer hvilken informasjon Rectoly samler inn, hvorfor og hvordan den håndteres.'
        ),
        "h2_collect": 'Informasjon vi samler inn',
        "mendeley_label": 'Tilkoblingen til Mendeley-kontoen din.',
        "mendeley_body": (
            'Når du logger inn med Mendeley, ber Rectoly om et OAuth-tilgangstoken for å lese og'
            ' synkronisere biblioteket, dokumentene og annotasjonene dine. Dette tokenet lagres i'
            ' enhetens Keychain og sendes aldri til serverne våre — Rectoly kommuniserer direkte med'
            ' Mendeleys egen API.'
        ),
        "docs_label": 'Dokumentene og annotasjonene dine.',
        "docs_body": (
            'PDF-er du åpner, sammen med uthevinger, understreking, klistrelapper og håndskrevet'
            ' blekk du legger til, lagres på enheten din. Hvis du aktiverer'
            ' iCloud-sikkerhetskopiering, sikkerhetskopieres disse dataene — og, hvis du separat'
            ' velger det, håndskriften din — til din egen iCloud-konto via Apples CloudKit. Vi har'
            ' ikke tilgang til disse dataene; de er kryptert og knyttet til Apple-ID-en din.'
        ),
        "crash_label": 'Krasj- og feilrapporter.',
        "crash_body": (
            'Rectoly bruker Sentry til å rapportere krasj og feil automatisk, slik at vi kan rette'
            ' feil. Disse rapportene er konfigurert til å utelukke personlig informasjon: ingen'
            ' standard brukeridentifikator eller IP-adresse samles inn, og dokumenttitler, filbaner,'
            ' e-postadresser, autentiseringstokener og annotasjonstekst fjernes før en rapport sendes.'
        ),
        "analytics_label": 'Anonym bruksanalyse.',
        "analytics_body": (
            'Rectoly bruker TelemetryDeck til å samle inn anonyme, aggregerte brukssignaler — for'
            ' eksempel hvilke skjermer som åpnes, om onboarding ble fullført, eller om en'
            ' synkronisering lyktes eller mislyktes (som en generell årsakskategori, ikke rå'
            ' feiltekst). Disse signalene inkluderer aldri dokumenttitler, filbaner, e-postadresser'
            ' eller annotasjonsinnhold, og er ikke knyttet til identiteten din.'
        ),
        "purchases_label": 'Kjøp.',
        "purchases_body": (
            'Abonnementer og engangskjøp håndteres helt av Apple via StoreKit. Vi mottar bekreftelse'
            ' på at et kjøp er gjort; Rectoly samler ikke inn eller lagrer betalingsopplysningene'
            ' dine. Apples egen personvernerklæring gjelder for disse dataene.'
        ),
        "h2_dont": 'Det vi ikke gjør',
        "dont_sell": 'Vi selger ikke dataene dine.',
        "dont_ads": 'Vi kjører ikke reklame eller SDK-er for annonsesporing.',
        "dont_read": (
            'Vi leser ikke selv innholdet i dokumentene eller annotasjonene dine — de forblir på'
            ' enheten din og, hvis du aktiverer det, i din egen iCloud-konto.'
        ),
        "h2_third": 'Tredjepartstjenester',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'referansebiblioteket ditt og dokumentsynkronisering',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'valgfri sikkerhetskopiering, styrt av Apple-ID-en din',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'rapportering av krasj og feil',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'anonym produktanalyse',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'kjøp og abonnementer',
        "third_note": 'Hver av disse opererer under sin egen personvernerklæring, som vi oppfordrer deg til å gjennomgå.',
        "h2_retention": 'Datalagring og sletting',
        "retention_body": (
            'Dokumentene, annotasjonene og håndskriften din forblir på enheten din til du sletter dem'
            ' eller sletter appen. Hvis iCloud-sikkerhetskopiering er aktivert, kan du slå den av i'
            ' innstillingene til Rectoly, eller fjerne appens iCloud-data fra enhetens'
            ' Innstillinger-app. Frakobling av Mendeley-kontoen din fjerner umiddelbart'
            ' tilgangstokenet som er lagret lokalt.'
        ),
        "h2_children": 'Barns personvern',
        "children_body": 'Rectoly er ikke rettet mot barn under 13 år, og vi samler ikke bevisst inn informasjon fra dem.',
        "h2_changes": 'Endringer i denne erklæringen',
        "changes_body": (
            'Vi kan oppdatere denne erklæringen etter hvert som appen endres. Vesentlige endringer'
            ' vil bli gjenspeilet her med en oppdatert dato.'
        ),
        "h2_contact": 'Kontakt',
        "contact_before": 'Spørsmål om denne erklæringen:',
        "footer": 'Rectoly er utviklet av Hawk Eye.',
        "languages_label": 'Språk',
    },
    "pl": {
        "title": 'Rectoly — Polityka prywatności',
        "h1": 'Rectoly — Polityka prywatności',
        "updated": 'Ostatnia aktualizacja: 9 sierpnia 2026',
        "intro": (
            'Hawk Eye („my”) rozwija Rectoly — aplikację na iPada do czytania, annotowania i'
            ' synchronizowania akademickich plików PDF z Mendeley Reference Manager. Niniejsza'
            ' polityka wyjaśnia, jakie informacje zbiera Rectoly, dlaczego i w jaki sposób są one'
            ' przetwarzane.'
        ),
        "h2_collect": 'Informacje, które zbieramy',
        "mendeley_label": 'Połączenie z kontem Mendeley.',
        "mendeley_body": (
            'Gdy logujesz się przez Mendeley, Rectoly prosi o token dostępu OAuth, aby odczytywać i'
            ' synchronizować Twoją bibliotekę, dokumenty i adnotacje. Token jest przechowywany w'
            ' Keychain na Twoim urządzeniu i nigdy nie jest wysyłany na nasze serwery — Rectoly'
            ' komunikuje się bezpośrednio z API Mendeley.'
        ),
        "docs_label": 'Twoje dokumenty i adnotacje.',
        "docs_body": (
            'Otwierane pliki PDF wraz z wyróżnieniami, podkreśleniami, karteczkami i odręcznym'
            ' atramentem są przechowywane na Twoim urządzeniu. Jeśli włączysz kopię zapasową iCloud,'
            ' te dane — oraz, jeśli osobno wyrazisz zgodę, Twój odręczny zapis — są kopiowane na Twoje'
            ' własne konto iCloud przez CloudKit firmy Apple. Nie mamy dostępu do tych danych; są one'
            ' szyfrowane i powiązane z Twoim Apple ID.'
        ),
        "crash_label": 'Raporty o awariach i błędach.',
        "crash_body": (
            'Rectoly korzysta z Sentry, aby automatycznie zgłaszać awarie i błędy, dzięki czemu'
            ' możemy naprawiać usterki. Raporty te są skonfigurowane tak, aby wykluczać dane osobowe:'
            ' nie jest zbierany domyślny identyfikator użytkownika ani adres IP, a tytuły dokumentów,'
            ' ścieżki plików, adresy e-mail, tokeny uwierzytelniania i tekst adnotacji są usuwane'
            ' przed wysłaniem raportu.'
        ),
        "analytics_label": 'Anonimowa analityka użycia.',
        "analytics_body": (
            'Rectoly korzysta z TelemetryDeck, aby zbierać anonimowe, zagregowane sygnały użycia — na'
            ' przykład, które ekrany są otwierane, czy ukończono wprowadzenie, albo czy synchronizacja'
            ' zakończyła się powodzeniem czy niepowodzeniem (jako ogólna kategoria przyczyny, a nie'
            ' surowy tekst błędu). Sygnały te nigdy nie obejmują tytułów dokumentów, ścieżek plików,'
            ' adresów e-mail ani treści adnotacji i nie są powiązane z Twoją tożsamością.'
        ),
        "purchases_label": 'Zakupy.',
        "purchases_body": (
            'Subskrypcje i zakupy jednorazowe są w całości obsługiwane przez Apple za pośrednictwem'
            ' StoreKit. Otrzymujemy potwierdzenie dokonania zakupu; Rectoly nie zbiera ani nie'
            ' przechowuje danych płatniczych. Te dane podlegają własnej polityce prywatności Apple.'
        ),
        "h2_dont": 'Czego nie robimy',
        "dont_sell": 'Nie sprzedajemy Twoich danych.',
        "dont_ads": 'Nie uruchamiamy reklam ani SDK do śledzenia reklam.',
        "dont_read": (
            'Nie czytamy sami treści Twoich dokumentów ani adnotacji — pozostają one na Twoim'
            ' urządzeniu, a jeśli włączysz tę opcję, na Twoim własnym koncie iCloud.'
        ),
        "h2_third": 'Usługi stron trzecich',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'Twoja biblioteka referencyjna i synchronizacja dokumentów',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'opcjonalna kopia zapasowa, zarządzana przez Twoje Apple ID',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'zgłaszanie awarii i błędów',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'anonimowa analityka produktu',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'zakupy i subskrypcje',
        "third_note": 'Każda z tych usług działa zgodnie z własną polityką prywatności, którą zachęcamy Cię do przejrzenia.',
        "h2_retention": 'Przechowywanie i usuwanie danych',
        "retention_body": (
            'Twoje dokumenty, adnotacje i odręczny zapis pozostają na urządzeniu, dopóki ich nie'
            ' usuniesz lub nie usuniesz aplikacji. Jeśli kopia zapasowa iCloud jest włączona, możesz'
            ' ją wyłączyć w ustawieniach Rectoly lub usunąć dane iCloud aplikacji w aplikacji'
            ' Ustawienia na urządzeniu. Odłączenie konta Mendeley natychmiast usuwa lokalnie'
            ' przechowywany token dostępu.'
        ),
        "h2_children": 'Prywatność dzieci',
        "children_body": (
            'Rectoly nie jest skierowany do dzieci poniżej 13. roku życia i świadomie nie zbieramy od'
            ' nich informacji.'
        ),
        "h2_changes": 'Zmiany w niniejszej polityce',
        "changes_body": (
            'Możemy aktualizować tę politykę w miarę zmian w aplikacji. Istotne zmiany zostaną'
            ' odzwierciedlone tutaj wraz z zaktualizowaną datą.'
        ),
        "h2_contact": 'Kontakt',
        "contact_before": 'Pytania dotyczące tej polityki:',
        "footer": 'Rectoly jest rozwijany przez Hawk Eye.',
        "languages_label": 'Języki',
    },
    "ru": {
        "title": 'Rectoly — Политика конфиденциальности',
        "h1": 'Rectoly — Политика конфиденциальности',
        "updated": 'Последнее обновление: 9 августа 2026 г.',
        "intro": (
            'Hawk Eye («мы») разрабатывает Rectoly — приложение для iPad для чтения, аннотирования и'
            ' синхронизации академических PDF с Mendeley Reference Manager. Эта политика объясняет,'
            ' какую информацию собирает Rectoly, зачем и как она обрабатывается.'
        ),
        "h2_collect": 'Информация, которую мы собираем',
        "mendeley_label": 'Подключение вашей учётной записи Mendeley.',
        "mendeley_body": (
            'При входе через Mendeley Rectoly запрашивает OAuth-токен доступа для чтения и'
            ' синхронизации вашей библиотеки, документов и аннотаций. Этот токен хранится в Keychain'
            ' на вашем устройстве и никогда не отправляется на наши серверы — Rectoly взаимодействует'
            ' напрямую с API самого Mendeley.'
        ),
        "docs_label": 'Ваши документы и аннотации.',
        "docs_body": (
            'Открываемые PDF, а также выделения, подчёркивания, стикеры и рукописные чернила хранятся'
            ' на вашем устройстве. Если вы включите резервное копирование в iCloud, эти данные — и,'
            ' при отдельном согласии, ваш рукописный ввод — сохраняются в вашу учётную запись iCloud'
            ' через CloudKit от Apple. У нас нет доступа к этим данным; они зашифрованы и привязаны к'
            ' вашему Apple ID.'
        ),
        "crash_label": 'Отчёты о сбоях и ошибках.',
        "crash_body": (
            'Rectoly использует Sentry для автоматической отправки отчётов о сбоях и ошибках, чтобы'
            ' мы могли исправлять недочёты. Эти отчёты настроены так, чтобы исключать персональные'
            ' данные: не собираются стандартный идентификатор пользователя и IP-адрес, а названия'
            ' документов, пути к файлам, адреса электронной почты, токены аутентификации и текст'
            ' аннотаций удаляются перед отправкой отчёта.'
        ),
        "analytics_label": 'Анонимная аналитика использования.',
        "analytics_body": (
            'Rectoly использует TelemetryDeck для сбора анонимных агрегированных сигналов'
            ' использования — например, какие экраны открываются, завершён ли онбординг, или успешно'
            ' ли прошла синхронизация (как общая категория причины, а не сырой текст ошибки). Эти'
            ' сигналы никогда не включают названия документов, пути к файлам, адреса электронной почты'
            ' или содержимое аннотаций и не связаны с вашей личностью.'
        ),
        "purchases_label": 'Покупки.',
        "purchases_body": (
            'Подписки и разовые покупки полностью обрабатываются Apple через StoreKit. Мы получаем'
            ' подтверждение совершения покупки; Rectoly не собирает и не хранит ваши платёжные данные.'
            ' На эти данные распространяется собственная политика конфиденциальности Apple.'
        ),
        "h2_dont": 'Чего мы не делаем',
        "dont_sell": 'Мы не продаём ваши данные.',
        "dont_ads": 'Мы не используем рекламу и SDK для рекламного отслеживания.',
        "dont_read": (
            'Мы сами не читаем содержимое ваших документов или аннотаций — они остаются на вашем'
            ' устройстве и, если вы это включите, в вашей учётной записи iCloud.'
        ),
        "h2_third": 'Сторонние сервисы',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'ваша справочная библиотека и синхронизация документов',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'необязательное резервное копирование, управляемое вашим Apple ID',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'отчёты о сбоях и ошибках',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'анонимная продуктовая аналитика',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'покупки и подписки',
        "third_note": (
            'Каждый из этих сервисов действует в соответствии со своей политикой конфиденциальности;'
            ' рекомендуем ознакомиться с ними.'
        ),
        "h2_retention": 'Хранение и удаление данных',
        "retention_body": (
            'Ваши документы, аннотации и рукописный ввод остаются на устройстве, пока вы их не'
            ' удалите или не удалите приложение. Если включено резервное копирование в iCloud, вы'
            ' можете отключить его в настройках Rectoly или удалить данные iCloud приложения в'
            ' приложении «Настройки» на устройстве. Отключение учётной записи Mendeley немедленно'
            ' удаляет локально сохранённый токен доступа.'
        ),
        "h2_children": 'Конфиденциальность детей',
        "children_body": 'Rectoly не предназначен для детей младше 13 лет, и мы сознательно не собираем информацию о них.',
        "h2_changes": 'Изменения этой политики',
        "changes_body": (
            'Мы можем обновлять эту политику по мере изменения приложения. Существенные изменения'
            ' будут отражены здесь с обновлённой датой.'
        ),
        "h2_contact": 'Контакты',
        "contact_before": 'Вопросы по этой политике:',
        "footer": 'Rectoly разработан компанией Hawk Eye.',
        "languages_label": 'Языки',
    },
    "ar": {
        "title": 'Rectoly — سياسة الخصوصية',
        "h1": 'Rectoly — سياسة الخصوصية',
        "updated": 'آخر تحديث 9 أغسطس 2026',
        "intro": (
            'تطوّر Hawk Eye («نحن») تطبيق Rectoly لأجهزة iPad لقراءة ملفات PDF الأكاديمية والتعليق'
            ' عليها ومزامنتها مع Mendeley Reference Manager. توضح هذه السياسة المعلومات التي يجمعها'
            ' Rectoly ولماذا وكيف يتم التعامل معها.'
        ),
        "h2_collect": 'المعلومات التي نجمعها',
        "mendeley_label": 'اتصال حساب Mendeley الخاص بك.',
        "mendeley_body": (
            'عند تسجيل الدخول باستخدام Mendeley، يطلب Rectoly رمز وصول OAuth لقراءة مكتبتك ومستنداتك'
            ' وتعليقاتك ومزامنتها. يُخزَّن هذا الرمز في Keychain على جهازك ولا يُرسَل أبدًا إلى'
            ' خوادمنا — يتواصل Rectoly مباشرة مع واجهة برمجة التطبيقات الخاصة بـ Mendeley.'
        ),
        "docs_label": 'مستنداتك وتعليقاتك.',
        "docs_body": (
            'تُخزَّن ملفات PDF التي تفتحها، إلى جانب التمييز والتسطير والملاحظات اللاصقة وأي حبر'
            ' مكتوب بخط اليد تضيفه، على جهازك. إذا فعّلت النسخ الاحتياطي عبر iCloud، تُنسَخ هذه'
            ' البيانات — وإذا وافقت بشكل منفصل، خطك اليدوي — إلى حساب iCloud الخاص بك عبر CloudKit من'
            ' Apple. ليس لدينا حق الوصول إلى هذه البيانات؛ فهي مشفّرة ومقيّدة بمعرّف Apple ID الخاص'
            ' بك.'
        ),
        "crash_label": 'تقارير الأعطال والأخطاء.',
        "crash_body": (
            'يستخدم Rectoly خدمة Sentry للإبلاغ تلقائيًا عن الأعطال والأخطاء حتى نتمكّن من إصلاح'
            ' الأخطاء. تُعدَّ هذه التقارير لاستبعاد المعلومات الشخصية: لا يُجمع معرّف مستخدم افتراضي'
            ' ولا عنوان IP، وتُزال عناوين المستندات ومسارات الملفات وعناوين البريد الإلكتروني ورموز'
            ' المصادقة ونص التعليقات قبل إرسال التقرير.'
        ),
        "analytics_label": 'تحليلات الاستخدام مجهولة الهوية.',
        "analytics_body": (
            'يستخدم Rectoly خدمة TelemetryDeck لجمع إشارات استخدام مجهولة ومجمّعة — على سبيل المثال،'
            ' الشاشات التي تُفتح، وما إذا اكتملت عملية التعريف، أو ما إذا نجحت المزامنة أو فشلت (كفئة'
            ' سبب عامة وليس كنص خطأ خام). لا تتضمن هذه الإشارات أبدًا عناوين المستندات أو مسارات'
            ' الملفات أو عناوين البريد الإلكتروني أو محتوى التعليقات، ولا ترتبط بهويتك.'
        ),
        "purchases_label": 'المشتريات.',
        "purchases_body": (
            'تتم معالجة الاشتراكات والمشتريات لمرة واحدة بالكامل بواسطة Apple عبر StoreKit. نتلقّى'
            ' تأكيدًا بإتمام عملية شراء؛ ولا يجمع Rectoly بيانات الدفع الخاصة بك ولا يخزّنها. تخضع تلك'
            ' البيانات لسياسة خصوصية Apple الخاصة.'
        ),
        "h2_dont": 'ما لا نفعله',
        "dont_sell": 'نحن لا نبيع بياناتك.',
        "dont_ads": 'نحن لا نشغّل إعلانات ولا مجموعات تطوير برمجيات لتتبع الإعلانات.',
        "dont_read": (
            'نحن لا نقرأ بأنفسنا محتوى مستنداتك أو تعليقاتك — فهي تبقى على جهازك، وإذا فعّلت ذلك، في'
            ' حساب iCloud الخاص بك.'
        ),
        "h2_third": 'خدمات الطرف الثالث',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'مكتبة مراجعك ومزامنة المستندات',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'نسخ احتياطي اختياري يخضع لمعرّف Apple ID الخاص بك',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'الإبلاغ عن الأعطال والأخطاء',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'تحليلات المنتج مجهولة الهوية',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'المشتريات والاشتراكات',
        "third_note": 'تعمل كل من هذه الخدمات بموجب سياسة خصوصيتها الخاصة، ونشجّعك على مراجعتها.',
        "h2_retention": 'الاحتفاظ بالبيانات وحذفها',
        "retention_body": (
            'تبقى مستنداتك وتعليقاتك وخطك اليدوي على جهازك حتى تحذفها أو تحذف التطبيق. إذا كان النسخ'
            ' الاحتياطي عبر iCloud مفعّلًا، يمكنك إيقافه من إعدادات Rectoly، أو إزالة بيانات iCloud'
            ' الخاصة بالتطبيق من تطبيق الإعدادات على جهازك. يؤدي قطع اتصال حساب Mendeley إلى إزالة رمز'
            ' الوصول المخزَّن محليًا فورًا.'
        ),
        "h2_children": 'خصوصية الأطفال',
        "children_body": 'لا يستهدف Rectoly الأطفال دون سن 13 عامًا، ولا نجمع معلومات منهم عن علم.',
        "h2_changes": 'التغييرات على هذه السياسة',
        "changes_body": 'قد نحدّث هذه السياسة مع تغيّر التطبيق. ستنعكس التغييرات الجوهرية هنا مع تاريخ محدّث.',
        "h2_contact": 'التواصل',
        "contact_before": 'أسئلة حول هذه السياسة:',
        "footer": 'طُوِّر Rectoly بواسطة Hawk Eye.',
        "languages_label": 'اللغات',
    },
    "tr": {
        "title": 'Rectoly — Gizlilik Politikası',
        "h1": 'Rectoly — Gizlilik Politikası',
        "updated": 'Son güncelleme: 9 Ağustos 2026',
        "intro": (
            'Hawk Eye ("biz") Mendeley Reference Manager ile akademik PDF\'leri okumak, ek açıklama'
            " eklemek ve senkronize etmek için bir iPad uygulaması olan Rectoly'yi geliştirir. Bu"
            " politika, Rectoly'nin hangi bilgileri topladığını, neden ve nasıl işlediğini açıklar."
        ),
        "h2_collect": 'Topladığımız bilgiler',
        "mendeley_label": 'Mendeley hesabı bağlantınız.',
        "mendeley_body": (
            'Mendeley ile oturum açtığınızda Rectoly, kitaplığınızı, belgelerinizi ve ek'
            ' açıklamalarınızı okumak ve senkronize etmek için bir OAuth erişim jetonu ister. Bu jeton'
            " cihazınızın Keychain'inde saklanır ve sunucularımıza asla gönderilmez — Rectoly doğrudan"
            " Mendeley'in kendi API'siyle iletişim kurar."
        ),
        "docs_label": 'Belgeleriniz ve ek açıklamalarınız.',
        "docs_body": (
            "Açtığınız PDF'ler ile vurgular, altı çizgiler, yapışkan notlar ve eklediğiniz el yazısı"
            ' mürekkep cihazınızda saklanır. iCloud yedeklemesini etkinleştirirseniz bu veriler — ve'
            " ayrı olarak katılmayı seçerseniz el yazınız — Apple'ın CloudKit'i aracılığıyla kendi"
            ' iCloud hesabınıza yedeklenir. Bu verilere erişimimiz yoktur; veriler şifrelenir ve Apple'
            " ID'nize bağlıdır."
        ),
        "crash_label": 'Çökme ve hata raporları.',
        "crash_body": (
            'Rectoly, hataları düzeltebilmemiz için çökme ve hataları otomatik olarak bildirmek üzere'
            ' Sentry kullanır. Bu raporlar kişisel bilgileri hariç tutacak şekilde yapılandırılmıştır:'
            ' varsayılan bir kullanıcı tanımlayıcısı veya IP adresi toplanmaz; belge başlıkları, dosya'
            ' yolları, e-posta adresleri, kimlik doğrulama jetonları ve ek açıklama metni rapor'
            ' gönderilmeden önce çıkarılır.'
        ),
        "analytics_label": 'Anonim kullanım analitikleri.',
        "analytics_body": (
            'Rectoly, anonim ve toplu kullanım sinyalleri toplamak için TelemetryDeck kullanır —'
            ' örneğin hangi ekranların açıldığı, başlangıç rehberinin tamamlanıp tamamlanmadığı veya'
            ' bir senkronizasyonun başarılı mı yoksa başarısız mı olduğu (genel bir neden kategorisi'
            ' olarak; ham hata metni değil). Bu sinyaller asla belge başlıkları, dosya yolları,'
            ' e-posta adresleri veya ek açıklama içeriği içermez ve kimliğinize bağlı değildir.'
        ),
        "purchases_label": 'Satın almalar.',
        "purchases_body": (
            'Abonelikler ve tek seferlik satın almalar tamamen Apple tarafından StoreKit aracılığıyla'
            ' işlenir. Bir satın almanın yapıldığına dair onay alırız; Rectoly ödeme bilgilerinizi'
            " toplamaz veya saklamaz. Bu veriler Apple'ın kendi gizlilik politikasına tabidir."
        ),
        "h2_dont": 'Yapmadıklarımız',
        "dont_sell": 'Verilerinizi satmayız.',
        "dont_ads": "Reklam veya reklam izleme SDK'ları çalıştırmayız.",
        "dont_read": (
            'Belgelerinizin veya ek açıklamalarınızın içeriğini kendimiz okumayız — bunlar'
            ' cihazınızda ve etkinleştirirseniz kendi iCloud hesabınızda kalır.'
        ),
        "h2_third": 'Üçüncü taraf hizmetler',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'referans kitaplığınız ve belge senkronizasyonu',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": "isteğe bağlı yedekleme, Apple ID'nizle yönetilir",
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'çökme ve hata raporlama',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'anonim ürün analitikleri',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'satın almalar ve abonelikler',
        "third_note": 'Bunların her biri kendi gizlilik politikası kapsamında çalışır; incelemenizi öneririz.',
        "h2_retention": 'Veri saklama ve silme',
        "retention_body": (
            'Belgeleriniz, ek açıklamalarınız ve el yazınız, bunları silene veya uygulamayı silene'
            ' kadar cihazınızda kalır. iCloud yedeklemesi etkinse Rectoly ayarlarından kapatabilir'
            ' veya cihazınızın Ayarlar uygulamasından uygulamanın iCloud verilerini kaldırabilirsiniz.'
            ' Mendeley hesabınızın bağlantısını kesmek, yerel olarak saklanan erişim jetonunu hemen'
            ' kaldırır.'
        ),
        "h2_children": 'Çocukların gizliliği',
        "children_body": 'Rectoly 13 yaşın altındaki çocuklara yönelik değildir ve bilerek onlardan bilgi toplamayız.',
        "h2_changes": 'Bu politikadaki değişiklikler',
        "changes_body": (
            'Uygulama değiştikçe bu politikayı güncelleyebiliriz. Önemli değişiklikler burada'
            ' güncellenmiş bir tarihle yansıtılır.'
        ),
        "h2_contact": 'İletişim',
        "contact_before": 'Bu politika hakkında sorular:',
        "footer": 'Rectoly, Hawk Eye tarafından geliştirilmektedir.',
        "languages_label": 'Diller',
    },
    "hi": {
        "title": 'Rectoly — गोपनीयता नीति',
        "h1": 'Rectoly — गोपनीयता नीति',
        "updated": 'अंतिम अपडेट: 9 अगस्त 2026',
        "intro": (
            'Hawk Eye ("हम") Rectoly विकसित करता है — Mendeley Reference Manager के साथ शैक्षणिक PDF'
            ' पढ़ने, एनोटेट करने और सिंक करने के लिए एक iPad ऐप। यह नीति बताती है कि Rectoly कौन-सी'
            ' जानकारी एकत्र करता है, क्यों और उसे कैसे संभाला जाता है।'
        ),
        "h2_collect": 'हम जो जानकारी एकत्र करते हैं',
        "mendeley_label": 'आपका Mendeley खाता कनेक्शन।',
        "mendeley_body": (
            'जब आप Mendeley से साइन इन करते हैं, तो Rectoly आपकी लाइब्रेरी, दस्तावेज़ और एनोटेशन'
            ' पढ़ने तथा सिंक करने के लिए OAuth एक्सेस टोकन का अनुरोध करता है। यह टोकन आपके डिवाइस के'
            ' Keychain में संग्रहीत होता है और कभी हमारे सर्वर पर नहीं भेजा जाता — Rectoly सीधे'
            ' Mendeley की अपनी API से बात करता है।'
        ),
        "docs_label": 'आपके दस्तावेज़ और एनोटेशन।',
        "docs_body": (
            'आपके द्वारा खोले गए PDF, साथ ही हाइलाइट, अंडरलाइन, स्टिकी नोट्स और आपके द्वारा जोड़ी गई'
            ' कोई भी हस्तलिखित स्याही, आपके डिवाइस पर संग्रहीत होते हैं। यदि आप iCloud बैकअप सक्षम'
            ' करते हैं, तो यह डेटा — और, यदि आप अलग से ऑप्ट इन करते हैं, तो आपकी हस्तलिपि — Apple के'
            ' CloudKit के माध्यम से आपके स्वयं के iCloud खाते में बैकअप होता है। हमारे पास इस डेटा तक'
            ' पहुँच नहीं है; यह एन्क्रिप्टेड है और आपके Apple ID तक सीमित है।'
        ),
        "crash_label": 'क्रैश और त्रुटि रिपोर्ट।',
        "crash_body": (
            'Rectoly बग ठीक करने के लिए क्रैश और त्रुटियों की स्वचालित रिपोर्टिंग हेतु Sentry का'
            ' उपयोग करता है। ये रिपोर्ट व्यक्तिगत जानकारी को बाहर रखने के लिए कॉन्फ़िगर की गई हैं: कोई'
            ' डिफ़ॉल्ट उपयोगकर्ता पहचानकर्ता या IP पता एकत्र नहीं किया जाता, और दस्तावेज़ शीर्षक,'
            ' फ़ाइल पथ, ईमेल पते, प्रमाणीकरण टोकन और एनोटेशन टेक्स्ट रिपोर्ट भेजने से पहले हटा दिए'
            ' जाते हैं।'
        ),
        "analytics_label": 'अनाम उपयोग विश्लेषण।',
        "analytics_body": (
            'Rectoly अनाम, समेकित उपयोग संकेतों को एकत्र करने के लिए TelemetryDeck का उपयोग करता है —'
            ' उदाहरण के लिए, कौन-सी स्क्रीन खोली गईं, ऑनबोर्डिंग पूर्ण हुई या नहीं, या सिंक सफल हुआ या'
            ' विफल (सामान्य कारण श्रेणी के रूप में, कच्चा त्रुटि टेक्स्ट नहीं)। इन संकेतों में कभी'
            ' दस्तावेज़ शीर्षक, फ़ाइल पथ, ईमेल पते या एनोटेशन सामग्री शामिल नहीं होती, और ये आपकी'
            ' पहचान से जुड़े नहीं होते।'
        ),
        "purchases_label": 'खरीदारी।',
        "purchases_body": (
            'सदस्यता और एक बार की खरीदारी पूरी तरह Apple द्वारा StoreKit के माध्यम से संभाली जाती'
            ' हैं। हमें पुष्टि मिलती है कि खरीदारी हुई; Rectoly आपके भुगतान विवरण एकत्र या संग्रहीत'
            ' नहीं करता। उस डेटा पर Apple की अपनी गोपनीयता नीति लागू होती है।'
        ),
        "h2_dont": 'हम क्या नहीं करते',
        "dont_sell": 'हम आपका डेटा नहीं बेचते।',
        "dont_ads": 'हम विज्ञापन या विज्ञापन-ट्रैकिंग SDK नहीं चलाते।',
        "dont_read": (
            'हम स्वयं आपके दस्तावेज़ों या एनोटेशन की सामग्री नहीं पढ़ते — वे आपके डिवाइस पर रहते हैं'
            ' और, यदि आप सक्षम करते हैं, तो आपके स्वयं के iCloud खाते में।'
        ),
        "h2_third": 'तृतीय-पक्ष सेवाएँ',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'आपकी संदर्भ लाइब्रेरी और दस्तावेज़ सिंक',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'वैकल्पिक बैकअप, आपके Apple ID द्वारा नियंत्रित',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'क्रैश और त्रुटि रिपोर्टिंग',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'अनाम उत्पाद विश्लेषण',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'खरीदारी और सदस्यताएँ',
        "third_note": (
            'इनमें से प्रत्येक अपनी गोपनीयता नीति के अंतर्गत संचालित होता है, जिसे हम आपको समीक्षा'
            ' करने के लिए प्रोत्साहित करते हैं।'
        ),
        "h2_retention": 'डेटा प्रतिधारण और हटाना',
        "retention_body": (
            'आपके दस्तावेज़, एनोटेशन और हस्तलिपि आपके डिवाइस पर तब तक रहते हैं जब तक आप उन्हें हटा'
            ' नहीं देते या ऐप नहीं हटाते। यदि iCloud बैकअप सक्षम है, तो आप इसे Rectoly की सेटिंग्स में'
            ' बंद कर सकते हैं, या अपने डिवाइस के Settings ऐप से ऐप का iCloud डेटा हटा सकते हैं। अपना'
            ' Mendeley खाता डिस्कनेक्ट करने पर स्थानीय रूप से संग्रहीत एक्सेस टोकन तुरंत हट जाता है।'
        ),
        "h2_children": 'बच्चों की गोपनीयता',
        "children_body": 'Rectoly 13 वर्ष से कम उम्र के बच्चों के लिए नहीं है, और हम जानबूझकर उनसे जानकारी एकत्र नहीं करते।',
        "h2_changes": 'इस नीति में परिवर्तन',
        "changes_body": (
            'ऐप बदलने पर हम इस नीति को अपडेट कर सकते हैं। महत्वपूर्ण परिवर्तन यहाँ अपडेट की गई तिथि'
            ' के साथ दर्शाए जाएँगे।'
        ),
        "h2_contact": 'संपर्क',
        "contact_before": 'इस नीति के बारे में प्रश्न:',
        "footer": 'Rectoly का विकास Hawk Eye द्वारा किया गया है।',
        "languages_label": 'भाषाएँ',
    },
    "id": {
        "title": 'Rectoly — Kebijakan Privasi',
        "h1": 'Rectoly — Kebijakan Privasi',
        "updated": 'Terakhir diperbarui 9 Agustus 2026',
        "intro": (
            'Hawk Eye ("kami") mengembangkan Rectoly, aplikasi iPad untuk membaca, menganotasi, dan'
            ' menyinkronkan PDF akademik dengan Mendeley Reference Manager. Kebijakan ini menjelaskan'
            ' informasi apa yang dikumpulkan Rectoly, mengapa, dan bagaimana penanganannya.'
        ),
        "h2_collect": 'Informasi yang kami kumpulkan',
        "mendeley_label": 'Koneksi akun Mendeley Anda.',
        "mendeley_body": (
            'Saat Anda masuk dengan Mendeley, Rectoly meminta token akses OAuth untuk membaca dan'
            ' menyinkronkan pustaka, dokumen, dan anotasi Anda. Token ini disimpan di Keychain'
            ' perangkat Anda dan tidak pernah dikirim ke server kami — Rectoly berkomunikasi langsung'
            ' dengan API milik Mendeley.'
        ),
        "docs_label": 'Dokumen dan anotasi Anda.',
        "docs_body": (
            'PDF yang Anda buka, beserta sorotan, garis bawah, catatan tempel, dan tinta tulisan'
            ' tangan yang Anda tambahkan, disimpan di perangkat Anda. Jika Anda mengaktifkan cadangan'
            ' iCloud, data ini — dan, jika Anda ikut serta secara terpisah, tulisan tangan Anda —'
            ' dicadangkan ke akun iCloud Anda sendiri melalui CloudKit milik Apple. Kami tidak'
            ' memiliki akses ke data ini; data dienkripsi dan dibatasi pada Apple ID Anda.'
        ),
        "crash_label": 'Laporan kerusakan dan kesalahan.',
        "crash_body": (
            'Rectoly menggunakan Sentry untuk secara otomatis melaporkan kerusakan dan kesalahan agar'
            ' kami dapat memperbaiki bug. Laporan ini dikonfigurasi untuk mengecualikan informasi'
            ' pribadi: tidak ada pengenal pengguna default atau alamat IP yang dikumpulkan, dan judul'
            ' dokumen, jalur file, alamat email, token autentikasi, serta teks anotasi dihapus sebelum'
            ' laporan dikirim.'
        ),
        "analytics_label": 'Analitik penggunaan anonim.',
        "analytics_body": (
            'Rectoly menggunakan TelemetryDeck untuk mengumpulkan sinyal penggunaan anonim dan'
            ' teragregasi — misalnya, layar mana yang dibuka, apakah onboarding selesai, atau apakah'
            ' sinkronisasi berhasil atau gagal (sebagai kategori alasan umum, bukan teks kesalahan'
            ' mentah). Sinyal ini tidak pernah mencakup judul dokumen, jalur file, alamat email, atau'
            ' konten anotasi, dan tidak terikat pada identitas Anda.'
        ),
        "purchases_label": 'Pembelian.',
        "purchases_body": (
            'Langganan dan pembelian satu kali ditangani sepenuhnya oleh Apple melalui StoreKit. Kami'
            ' menerima konfirmasi bahwa pembelian telah dilakukan; Rectoly tidak mengumpulkan atau'
            ' menyimpan detail pembayaran Anda. Kebijakan privasi Apple sendiri mengatur data'
            ' tersebut.'
        ),
        "h2_dont": 'Yang tidak kami lakukan',
        "dont_sell": 'Kami tidak menjual data Anda.',
        "dont_ads": 'Kami tidak menjalankan iklan atau SDK pelacakan iklan.',
        "dont_read": (
            'Kami tidak membaca sendiri konten dokumen atau anotasi Anda — data itu tetap di'
            ' perangkat Anda dan, jika Anda mengaktifkannya, di akun iCloud Anda sendiri.'
        ),
        "h2_third": 'Layanan pihak ketiga',
        "third_mendeley_name": 'Mendeley (Elsevier)',
        "third_mendeley_desc": 'pustaka referensi dan sinkronisasi dokumen Anda',
        "third_icloud_name": 'Apple iCloud / CloudKit',
        "third_icloud_desc": 'cadangan opsional, diatur oleh Apple ID Anda',
        "third_sentry_name": 'Sentry',
        "third_sentry_desc": 'pelaporan kerusakan dan kesalahan',
        "third_telemetry_name": 'TelemetryDeck',
        "third_telemetry_desc": 'analitik produk anonim',
        "third_storekit_name": 'Apple StoreKit',
        "third_storekit_desc": 'pembelian dan langganan',
        "third_note": 'Masing-masing beroperasi berdasarkan kebijakan privasinya sendiri, yang kami sarankan Anda tinjau.',
        "h2_retention": 'Retensi dan penghapusan data',
        "retention_body": (
            'Dokumen, anotasi, dan tulisan tangan Anda tetap di perangkat hingga Anda menghapusnya'
            ' atau menghapus aplikasi. Jika cadangan iCloud diaktifkan, Anda dapat mematikannya di'
            ' pengaturan Rectoly, atau menghapus data iCloud aplikasi dari aplikasi Pengaturan'
            ' perangkat. Memutuskan akun Mendeley segera menghapus token akses yang tersimpan secara'
            ' lokal.'
        ),
        "h2_children": 'Privasi anak',
        "children_body": (
            'Rectoly tidak ditujukan untuk anak di bawah 13 tahun, dan kami tidak dengan sengaja'
            ' mengumpulkan informasi dari mereka.'
        ),
        "h2_changes": 'Perubahan kebijakan ini',
        "changes_body": (
            'Kami dapat memperbarui kebijakan ini seiring perubahan aplikasi. Perubahan material akan'
            ' tercermin di sini dengan tanggal yang diperbarui.'
        ),
        "h2_contact": 'Kontak',
        "contact_before": 'Pertanyaan tentang kebijakan ini:',
        "footer": 'Rectoly dikembangkan oleh Hawk Eye.',
        "languages_label": 'Bahasa',
    },
}

# Ensure every locale has the same keys as English.
_EN_KEYS = set(TRANSLATIONS["en"])
for _code, _name, _dir in LOCALES:
    assert _code in TRANSLATIONS, f"missing locale: {_code}"
    assert set(TRANSLATIONS[_code]) == _EN_KEYS, (
        f"key mismatch for {_code}: "
        f"missing={_EN_KEYS - set(TRANSLATIONS[_code])} "
        f"extra={set(TRANSLATIONS[_code]) - _EN_KEYS}"
    )

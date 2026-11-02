import streamlit as st

st.set_page_config(
    page_title="Pocket Hub - Marketplace Automation",
    page_icon="⚡",
    layout="wide"
)

# Inițializare stări
if "autentificat" not in st.session_state:
    st.session_state.autentificat = False

if "magazin_conectat" not in st.session_state:
    st.session_state.magazin_conectat = False

if "nume_magazin" not in st.session_state:
    st.session_state.nume_magazin = ""

# Dicționar cu conversațiile clienților
if "conversatii" not in st.session_state:
    st.session_state.conversatii = {
        "Mihai Popescu": [
            {"sender": "Mihai Popescu", "text": "Salut! Aveți puloverul din lână pe mărimea L în stoc?"},
            {"sender": "AI Sales Agent", "text": "Salut Mihai! Da, avem 12 bucăți disponibile pe mărimea L."}
        ],
        "Elena Dumitrescu": [
            {"sender": "Elena Dumitrescu", "text": "Bună ziua, când ajunge comanda #ORD-8920?"},
            {"sender": "Admin", "text": "Bună ziua Elena! Coletul a fost expediat astăzi și ajunge mâine."}
        ],
        "Alexandru Ionescu": [
            {"sender": "Alexandru Ionescu", "text": "Salut, mai aveți pe stoc șapca Newsboy?"}
        ]
    }

if "client_selectat" not in st.session_state:
    st.session_state.client_selectat = "Mihai Popescu"

# -------------------------------------------------------------------
# ECRAN DE LOGIN / AUTENTIFICARE
# -------------------------------------------------------------------
if not st.session_state.autentificat:
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #070514 0%, #110c2e 50%, #05030a 100%);
        }
        .social-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 10px;
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            color: white;
            font-weight: 500;
            text-decoration: none;
            margin-bottom: 8px;
        }
        .social-btn:hover {
            background: rgba(51, 65, 85, 0.9);
            border-color: #818cf8;
            color: #ffffff;
        }
        .social-icon {
            width: 18px;
            height: 18px;
            margin-right: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1.2, 1], gap="large")

    with col_left:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### 🛍️ **Pocket Hub**")
        st.caption("Marketplace Automation")
        st.markdown("# **Automatizează.<br>Vinde mai mult.<br><span style='color: #818cf8;'>Crește inteligent.</span>**", unsafe_allow_html=True)
        st.markdown("<p style='color: #94a3b8; font-size: 15px;'>Platforma ta completă pentru automatizarea vânzărilor pe marketplace-uri, cu puterea AI.</p>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2, b3, b4 = st.columns(4)
        with b1:
            st.info("⚡\n**AI**")
        with b2:
            st.info("📈\n**Rapid**")
        with b3:
            st.info("🛡️\n**Siguranță**")
        with b4:
            st.info("🎧\n**24/7**")

    with col_right:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("## **Bine ai revenit! 👋**")
        st.caption("Intră în contul tău pentru a continua")
        
        email = st.text_input("Email-ul tău", placeholder="nume@exemplu.com")
        parola = st.text_input("Parola ta", type="password", placeholder="••••••••")
        
        c_remember, c_forgot = st.columns(2)
        with c_remember:
            st.checkbox("Ține-mă minte")
        with c_forgot:
            st.markdown("<p style='text-align: right; font-size: 13px; color: #818cf8;'>Ai uitat parola?</p>", unsafe_allow_html=True)
        
        if st.button("Autentificare ➔", use_container_width=True, type="primary"):
            if email and parola:
                st.session_state.autentificat = True
                st.rerun()
            else:
                st.warning("Te rugăm să introduci emailul și parola.")
        
        st.markdown("<p style='text-align: center; color: #64748b; font-size: 13px; margin: 10px 0;'>sau conectează-te cu</p>", unsafe_allow_html=True)
        
        sc1, sc2, sc3 = st.columns(3)
        with sc1:
            if st.button("🌐 Google", use_container_width=True):
                st.session_state.autentificat = True
                st.rerun()
        with sc2:
            if st.button("🍎 Apple", use_container_width=True):
                st.session_state.autentificat = True
                st.rerun()
        with sc3:
            if st.button("🪟 Microsoft", use_container_width=True):
                st.session_state.autentificat = True
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔓 Acces Rapid în Dashboard", use_container_width=True):
            st.session_state.autentificat = True
            st.rerun()

# -------------------------------------------------------------------
# DASHBOARD COMPLET CU MESAJE CLIENȚI & CONECTARE MAGAZIN
# -------------------------------------------------------------------
else:
    st.markdown("""
        <style>
        .main {
            background-color: #0b0f19;
        }
        .stMetric {
            background-color: #1e293b;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #334155;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("### ⚡ Pocket Hub")
        st.caption("Marketplace Automation")
        st.markdown("---")
        
        menu = st.radio(
            "Navegare",
            [
                "🚀 Panou Vânzări Live", 
                "💬 Mesaje Clienți",
                "📦 Comenzi Magazin Live",
                "🔗 Conectare Directă Magazin",
                "🎯 Lead-uri & Pipeline", 
                "📊 Rapoarte & Conversii", 
                "⚙️ Setări Automatizări"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        if st.session_state.magazin_conectat:
            st.success(f"🟢 Sincronizat:\n**{st.session_state.nume_magazin}**")
        else:
            st.warning("⚠️ Niciun magazin conectat!")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚪 Deconectare", use_container_width=True):
            st.session_state.autentificat = False
            st.rerun()

    # 1. PANOU VÂNZĂRI LIVE
    if menu == "🚀 Panou Vânzări Live":
        st.markdown("## 🚀 Panou de Control & Vânzări în Timp Real")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Bani Încașați (Azi)", value="$6,240", delta="+21.4% vs ieri")
        with col2:
            st.metric(label="Venit Total", value="$248,750", delta="+14.2%")
        with col3:
            st.metric(label="Comenzi Active (Live)", value="24", delta="+4 noi")
        with col4:
            st.metric(label="Stoc Total Disponibil", value="512 buc", delta="Sincronizat")

        st.markdown("")

        chart_col, funnel_col = st.columns([2, 1])
        with chart_col:
            st.markdown("### 📈 Monitorizare Vânzări Live")
            sales_data = [120, 300, 450, 400, 750, 980, 1450]
            st.line_chart(sales_data)

        with funnel_col:
            st.markdown("### 🔻 Sincronizare Magazin")
            st.write("🔄 Status: **Conectat & Activ**")
            st.write("⚡ Viteză API: **14ms**")
            st.write("🛒 Coșuri Abandonate: **14**")
            st.write("💳 Procesator Plăți: **Stripe / Apple Pay**")

    # 2. MESAJE CLIENȚI (CONVERSAȚII ACTIVE)
    elif menu == "💬 Mesaje Clienți":
        st.title("💬 Mesaje Clienți")
        st.write("Selectează o persoană din listă pentru a citi conversația și a-i răspunde direct în timp real.")

        col_persoane, col_chat = st.columns([1, 2], gap="medium")

        with col_persoane:
            st.markdown("### 📥 Clienți")
            for client in st.session_state.conversatii.keys():
                if st.button(f"👤 {client}", use_container_width=True):
                    st.session_state.client_selectat = client
                    st.rerun()

        with col_chat:
            client_curent = st.session_state.client_selectat
            st.markdown(f"### 💬 Conversație cu: `{client_curent}`")
            st.markdown("---")

            chat_container = st.container()
            with chat_container:
                for msg in st.session_state.conversatii[client_curent]:
                    if msg["sender"] == client_curent:
                        st.info(f"**{msg['sender']}**: {msg['text']}")
                    else:
                        st.success(f"**{msg['sender']}**: {msg['text']}")

            st.markdown("<br>", unsafe_allow_html=True)
            
            mesaj_nou = st.text_input(f"Scrie un mesaj către {client_curent}...", key="input_mesaj_client")
            if st.button("Trimite mesajul ➔", type="primary"):
                if mesaj_nou:
                    st.session_state.conversatii[client_curent].append({"sender": "Admin (Tu)", "text": mesaj_nou})
                    st.rerun()

    # 3. COMENZI MAGAZIN LIVE
    elif menu == "📦 Comenzi Magazin Live":
        st.title("📦 Comenzi Active din Magazinul Tău")
        st.dataframe({
            "ID Comandă": ["#ORD-8921", "#ORD-8920", "#ORD-8919", "#ORD-8918"],
            "Client": ["Mihai Popescu", "Elena Dumitrescu", "Alexandru Ionescu", "Cristina Stan"],
            "Produs Cumpărat": ["Set Haină Cașmir", "Pulover Merino Wool", "Newsboy Cap", "Polo Ralph Quarter-Zip"],
            "Valoare": ["$350", "$180", "$65", "$140"],
            "Status Plată": ["Plătit (Stripe)", "Plătit (Apple Pay)", "Plătit (Card)", "Plătit (Card)"],
            "Livrare": ["În Pregătire", "Expediat", "Livrat", "În Pregătire"]
        }, use_container_width=True)

    # 4. CONECTARE DIRECTĂ MAGAZIN
    elif menu == "🔗 Conectare Directă Magazin":
        st.title("🔗 Conectare Directă cu Magazinul Tău")
        shop_url = st.text_input("Domeniu magazin (ex: magazin.myshopify.com sau site.ro):")
        if st.button("Conectare Instantanee", type="primary", use_container_width=True):
            if shop_url:
                st.session_state.magazin_conectat = True
                st.session_state.nume_magazin = shop_url
                st.success("🎉 Magazin conectat cu succes!")
                st.balloons()
            else:
                st.warning("Introdu adresa magazinului.")

        if st.session_state.magazin_conectat:
            st.markdown("---")
            st.info(f"Conectat la: **{st.session_state.nume_magazin}**")
            if st.button("Deconectare Magazin"):
                st.session_state.magazin_conectat = False
                st.session_state.nume_magazin = ""
                st.rerun()

    elif menu == "🎯 Lead-uri & Pipeline":
        st.title("🎯 Management Lead-uri & CRM")
        st.dataframe({
            "Client": ["SC Tech SRL", "Global Solutions", "Apex Trading", "Mihai Popescu"],
            "Valoare estimată": ["$4,500", "$12,000", "$2,800", "$7,500"],
            "Status": ["Negociere", "Contactat", "Închis / Câștigat", "Contactat"]
        }, use_container_width=True)

    elif menu == "📊 Rapoarte & Conversii":
        st.title("📊 Rapoarte Avansate")
        st.bar_chart([4500, 8200, 12000, 15400])

    elif menu == "⚙️ Setări Automatizări":
        st.title("⚙️ Setări Generale")
        st.text_input("Cheie API Gateway Plăți", value="sk_live_*******************")
        st.button("Actualizează Sistemul")
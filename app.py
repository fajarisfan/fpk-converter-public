import streamlit as st

st.set_page_config(page_title="FPK Converter", page_icon="⚡", layout="centered")

# ── GANTI INI DENGAN LINK VIDEO DARI VENDOR ──────────────────
VIDEO_URL = "https://www.youtube.com/watch?v=GANTI_DENGAN_LINK_VIDEO"
# Contoh: "https://www.youtube.com/watch?v=xxxxxxxxxxxx"
# Atau link Google Drive: "https://drive.google.com/file/d/xxxx/view"
# ─────────────────────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif !important; }
#MainMenu {visibility:hidden;} footer {visibility:hidden;} header {visibility:hidden;}

.stApp { background-color: #0d0d0d; }
.block-container { padding-top: 3rem; max-width: 620px; }

.stTextInput > div > div > input {
    background: #111111 !important; border: 3px solid #3a3a3a !important;
    border-radius: 0px !important; color: transparent !important;
    caret-color: #ff6b35 !important; padding: 14px 18px !important;
    font-size: 0.95rem !important; font-family: 'JetBrains Mono', monospace !important;
    letter-spacing: 4px !important;
}
.stTextInput > div > div > input:focus {
    border-color: #ff6b35 !important; box-shadow: 4px 4px 0px #ff6b35 !important;
}
.stTextInput label {
    color: #bbbbbb !important; font-size: 0.8rem !important; font-weight: 700 !important;
    letter-spacing: 2px !important; text-transform: uppercase !important;
    font-family: 'JetBrains Mono', monospace !important;
}
[data-testid="stTextInputHideShowButton"],
[data-baseweb="input"] button,
[data-baseweb="input"] [role="button"] {
    display: none !important; width: 0 !important; pointer-events: none !important;
}
input[type="password"]::-ms-reveal,
input[type="password"]::-ms-clear { display: none !important; }

.stButton > button {
    background: #ff6b35 !important; color: #f0f0f0 !important;
    border: 3px solid #f0f0f0 !important; border-radius: 0px !important;
    height: 52px !important; font-size: 0.9rem !important; font-weight: 800 !important;
    box-shadow: 4px 4px 0px #f0f0f0 !important; width: 100% !important;
    text-transform: uppercase !important; letter-spacing: 1px !important;
    transition: all 0.1s !important;
}
.stButton > button:hover {
    transform: translate(-2px, -2px) !important; box-shadow: 6px 6px 0px #f0f0f0 !important;
}
.stButton > button:active {
    transform: translate(2px, 2px) !important; box-shadow: 1px 1px 0px #f0f0f0 !important;
}

.video-card {
    background: #111; border: 3px solid #333; border-left: 5px solid #ffd700;
    padding: 1.4rem 1.5rem; margin: 0 auto 1.5rem; max-width: 480px;
    box-shadow: 5px 5px 0px #ffd700; text-align: left;
}
.video-btn {
    display: inline-flex; align-items: center; gap: 10px;
    background: #ffd700; border: 3px solid #f0f0f0; padding: 12px 24px;
    box-shadow: 4px 4px 0px #f0f0f0; text-decoration: none;
    font-family: 'Space Grotesk', sans-serif; font-size: 0.9rem;
    font-weight: 800; color: #111; letter-spacing: 1px;
    text-transform: uppercase; transition: all 0.1s; cursor: pointer;
    margin-top: 1rem;
}
.video-btn:hover {
    transform: translate(-2px, -2px); box-shadow: 6px 6px 0px #f0f0f0;
    text-decoration: none; color: #111;
}
</style>

<script>
(function() {
  function removeEye() {
    ['[data-testid="stTextInputHideShowButton"]',
     'button[aria-label="Show password text"]',
     'button[aria-label="Hide password text"]',
     '[data-baseweb="input"] button'
    ].forEach(function(sel) {
      document.querySelectorAll(sel).forEach(function(el) {
        el.parentNode && el.parentNode.removeChild(el);
      });
    });
  }
  removeEye();
  new MutationObserver(removeEye).observe(document.body, {childList:true, subtree:true});
})();
</script>
""", unsafe_allow_html=True)

# ── HEADER + LOCKED ──────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding: 2rem 1rem 1.5rem;">
    <div style="display:inline-block; background:#ff6b35; border:3px solid #f0f0f0;
        padding:6px 18px; margin-bottom:2rem; box-shadow:4px 4px 0px #f0f0f0;">
        <span style="font-family:'JetBrains Mono',monospace; font-size:11px;
            font-weight:800; color:#f0f0f0; letter-spacing:2px;">
            ⚡ FPK CONVERTER &nbsp;·&nbsp; V1.0
        </span>
    </div>

    <h1 style="font-family:'Space Grotesk',sans-serif; font-size:2.8rem; font-weight:800;
        color:#f0f0f0; line-height:1.15; margin:0 0 1.5rem; letter-spacing:-1.5px;
        text-transform:uppercase;">
        APLIKASI INI<br>
        <span style="color:#ff6b35; text-decoration:underline;
            text-decoration-thickness:5px; text-underline-offset:6px;">
            TIDAK DAPAT
        </span><br>DIAKSES
    </h1>

    <div style="background:#1a1a1a; border:3px solid #333; border-left:5px solid #ff6b35;
        padding:1.2rem 1.5rem; margin:0 auto 2rem; max-width:480px;
        box-shadow:4px 4px 0px #333; text-align:left;">
        <p style="font-family:'JetBrains Mono',monospace; font-size:0.75rem;
            color:#888; margin:0 0 0.6rem; letter-spacing:1px;">// NOTICE</p>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.95rem;
            color:#cccccc; margin:0; line-height:1.7; font-weight:500;">
            Aplikasi ini merupakan karya pribadi pengembangnya dan tidak lagi
            dapat diakses. Silakan hubungi pengembang atau bangun sistem Anda sendiri.
        </p>
    </div>

    <div style="display:flex; justify-content:center; gap:1.5rem; margin-bottom:2rem; flex-wrap:wrap;">
        <div style="background:#111; border:2px solid #222; padding:0.7rem 1.2rem;
            box-shadow:3px 3px 0px #222; text-align:center; min-width:100px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:9px;
                color:#555; letter-spacing:2px; margin-bottom:4px;">STATUS</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem;
                color:#ff4444; font-weight:800; letter-spacing:1px;">LOCKED</div>
        </div>
        <div style="background:#111; border:2px solid #222; padding:0.7rem 1.2rem;
            box-shadow:3px 3px 0px #222; text-align:center; min-width:100px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:9px;
                color:#555; letter-spacing:2px; margin-bottom:4px;">ACCESS</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem;
                color:#ff6b35; font-weight:800; letter-spacing:1px;">DENIED</div>
        </div>
        <div style="background:#111; border:2px solid #222; padding:0.7rem 1.2rem;
            box-shadow:3px 3px 0px #222; text-align:center; min-width:100px;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:9px;
                color:#555; letter-spacing:2px; margin-bottom:4px;">VERSION</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem;
                color:#ffd700; font-weight:800; letter-spacing:1px;">V1.0</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── DIVIDER ───────────────────────────────────────────────────
st.markdown("""
<div style="display:flex; align-items:center; gap:1rem; margin:0 0 1.5rem;">
    <div style="flex:1; height:3px; background:#1a1a1a;"></div>
    <span style="font-family:'JetBrains Mono',monospace; font-size:10px;
        color:#444; letter-spacing:2px; white-space:nowrap;">// CARA MANUAL</span>
    <div style="flex:1; height:3px; background:#1a1a1a;"></div>
</div>
""", unsafe_allow_html=True)

# ── VIDEO SECTION ─────────────────────────────────────────────
st.markdown(f"""
<div class="video-card">
    <p style="font-family:'JetBrains Mono',monospace; font-size:0.72rem;
        color:#ffd700; margin:0 0 0.5rem; letter-spacing:1px;">
        📼 PANDUAN VENDOR
    </p>
    <p style="font-family:'Space Grotesk',sans-serif; font-size:1.05rem;
        font-weight:700; color:#f0f0f0; margin:0 0 0.5rem;">
        Video Tutorial Manual FPK BPJS
    </p>
    <p style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem;
        color:#888; margin:0 0 1rem; line-height:1.6;">
        Inilah proses yang selama ini digantikan oleh aplikasi ini.
        Tanpa otomasi, setiap klaim harus dikerjakan manual seperti di video berikut.
    </p>
    <div style="background:#0d0d0d; border:2px solid #333; padding:0.8rem 1rem;
        margin-bottom:1rem; border-left:3px solid #555;">
        <p style="font-family:'JetBrains Mono',monospace; font-size:0.72rem;
            color:#555; margin:0 0 4px; letter-spacing:1px;">// SEBELUM APLIKASI INI</p>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.82rem;
            color:#666; margin:0; line-height:1.6;">
            ✗ &nbsp;Buka PDF satu per satu<br>
            ✗ &nbsp;Salin No.SEP secara manual<br>
            ✗ &nbsp;Input ke Excel satu per satu<br>
            ✗ &nbsp;Hitung nominal secara manual<br>
            ✗ &nbsp;Potensi salah input & duplikat
        </p>
    </div>
    <div style="background:#0d0d0d; border:2px solid #1a3a1a; padding:0.8rem 1rem;
        margin-bottom:1.2rem; border-left:3px solid #00c47a;">
        <p style="font-family:'JetBrains Mono',monospace; font-size:0.72rem;
            color:#00c47a; margin:0 0 4px; letter-spacing:1px;">// DENGAN APLIKASI INI</p>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.82rem;
            color:#666; margin:0; line-height:1.6;">
            ✓ &nbsp;Upload PDF → otomatis terbaca<br>
            ✓ &nbsp;No.SEP & nominal terekstrak otomatis<br>
            ✓ &nbsp;Deteksi duplikat otomatis<br>
            ✓ &nbsp;CSV siap pakai dalam hitungan detik<br>
            ✓ &nbsp;Riwayat & rekap tersimpan otomatis
        </p>
    </div>
    <a href="{VIDEO_URL}" target="_blank" class="video-btn">
        ▶ &nbsp;TONTON VIDEO MANUAL
    </a>
</div>
""", unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:1.5rem 1rem 2rem; margin-top:1rem;
    border-top:2px solid #1a1a1a;">
    <p style="font-family:'JetBrains Mono',monospace; font-size:0.68rem;
        color:#333; letter-spacing:1px; margin:0;">
        © 2025 Isfan Fajar Anugrah &nbsp;·&nbsp; All Rights Reserved<br>
        Dilarang digandakan atau digunakan tanpa izin tertulis dari pemilik
    </p>
</div>
""", unsafe_allow_html=True)

# ── PIN (selalu ditolak) ──────────────────────────────────────
pin_input = st.text_input("PIN AKSES", type="password", placeholder="", label_visibility="collapsed")
if st.button("Coba Akses →"):
    if pin_input:
        st.error("🔒 Aplikasi ini tidak dapat diakses. Silakan bangun sistem Anda sendiri.")
    else:
        st.warning("Masukkan PIN terlebih dahulu.")

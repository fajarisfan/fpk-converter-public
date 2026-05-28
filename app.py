import streamlit as st

st.set_page_config(page_title="FPK Converter", page_icon="⚡", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif !important; }
#MainMenu {visibility:hidden;} footer {visibility:hidden;} header {visibility:hidden;}
.stApp { background-color: #0d0d0d; }
.block-container { padding-top: 2rem; max-width: 620px; }
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
[data-testid="stTextInputHideShowButton"],
[data-baseweb="input"] button { display: none !important; }
input[type="password"]::-ms-reveal,
input[type="password"]::-ms-clear { display: none !important; }
.stButton > button {
    background: #ff6b35 !important; color: #f0f0f0 !important;
    border: 3px solid #f0f0f0 !important; border-radius: 0px !important;
    height: 52px !important; font-size: 0.9rem !important; font-weight: 800 !important;
    box-shadow: 4px 4px 0px #f0f0f0 !important; width: 100% !important;
    text-transform: uppercase !important; letter-spacing: 1px !important;
}
.stButton > button:hover {
    transform: translate(-2px,-2px) !important;
    box-shadow: 6px 6px 0px #f0f0f0 !important;
}
</style>
""", unsafe_allow_html=True)

if "pin_submitted" not in st.session_state:
    st.session_state.pin_submitted = False

# ── HALAMAN 1: FORM PIN ──
if not st.session_state.pin_submitted:
    st.markdown("""
    <div style="text-align:center; padding-top:3rem;">
      <div style="display:inline-block; background:#ff6b35; border:3px solid #f0f0f0;
          padding:6px 18px; margin-bottom:2rem; box-shadow:4px 4px 0px #f0f0f0;">
        <span style="font-family:'JetBrains Mono',monospace; font-size:11px;
            font-weight:800; color:#f0f0f0; letter-spacing:2px;">
          ⚡ FPK CONVERTER &nbsp;·&nbsp; V1.0
        </span>
      </div>
      <h1 style="font-family:'Space Grotesk',sans-serif; font-size:2.5rem; font-weight:800;
          color:#f0f0f0; line-height:1.2; margin:0 0 0.5rem; letter-spacing:-1.5px;
          text-transform:uppercase;">
        MASUKKAN<br><span style="color:#ff6b35;">PIN AKSES</span>
      </h1>
      <p style="font-family:'JetBrains Mono',monospace; font-size:0.75rem;
          color:#555; letter-spacing:1px; margin-bottom:2.5rem;">
        // Masukkan PIN untuk melanjutkan
      </p>
    </div>
    """, unsafe_allow_html=True)

    pin_input = st.text_input("PIN", type="password", placeholder="", label_visibility="collapsed")

    if st.button("AKSES →"):
        if pin_input:
            st.session_state.pin_submitted = True
            st.rerun()
        else:
            st.warning("Masukkan PIN terlebih dahulu.")

    st.markdown("""
    <div style="text-align:center; margin-top:3rem;">
      <p style="font-family:'JetBrains Mono',monospace; font-size:0.65rem;
          color:#333; letter-spacing:1px;">
        © 2025 Isfan Fajar Anugrah &nbsp;·&nbsp; All Rights Reserved
      </p>
    </div>
    """, unsafe_allow_html=True)

# ── HALAMAN 2: PRANK ──
else:
    st.markdown("""
    <div style="text-align:center; padding-top:2rem;">
      <div style="display:inline-block; background:#ff6b35; border:3px solid #f0f0f0;
          padding:6px 18px; margin-bottom:1.5rem; box-shadow:4px 4px 0px #f0f0f0;">
        <span style="font-family:'JetBrains Mono',monospace; font-size:11px;
            font-weight:800; color:#f0f0f0; letter-spacing:2px;">
          ⚡ FPK CONVERTER &nbsp;·&nbsp; V1.0
        </span>
      </div>
      <h1 style="font-family:'Space Grotesk',sans-serif; font-size:2.8rem; font-weight:800;
          color:#f0f0f0; line-height:1.15; margin:0 0 1.5rem; letter-spacing:-1.5px;
          text-transform:uppercase;">
        APLIKASI INI<br>
        <span style="color:#ff6b35; border-bottom:5px solid #ff6b35; padding-bottom:2px;">
          TIDAK DAPAT
        </span><br>DIAKSES
      </h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#1a1a1a; border:3px solid #333; border-left:5px solid #ff6b35;
        padding:1.2rem 1.5rem; margin-bottom:1.5rem; box-shadow:4px 4px 0px #333;">
      <p style="font-family:'JetBrains Mono',monospace; font-size:0.72rem;
          color:#888; margin:0 0 0.5rem; letter-spacing:1px;">// NOTICE</p>
      <p style="font-family:'Space Grotesk',sans-serif; font-size:0.95rem;
          color:#cccccc; margin:0; line-height:1.7; font-weight:500;">
        Aplikasi ini merupakan karya pribadi pengembangnya dan tidak lagi dapat diakses.
        Silakan hubungi pengembang atau <strong style="color:#ff6b35;">bangun sistem Anda sendiri.</strong>
      </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="display:flex; justify-content:center; gap:1rem; margin-bottom:2rem; flex-wrap:wrap;">
      <div style="background:#111; border:2px solid #222; padding:0.7rem 1.2rem;
          box-shadow:3px 3px 0px #222; text-align:center; min-width:90px;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:9px;
            color:#555; letter-spacing:2px; margin-bottom:4px;">STATUS</div>
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem;
            color:#ff4444; font-weight:800;">LOCKED</div>
      </div>
      <div style="background:#111; border:2px solid #222; padding:0.7rem 1.2rem;
          box-shadow:3px 3px 0px #222; text-align:center; min-width:90px;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:9px;
            color:#555; letter-spacing:2px; margin-bottom:4px;">ACCESS</div>
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem;
            color:#ff6b35; font-weight:800;">DENIED</div>
      </div>
      <div style="background:#111; border:2px solid #222; padding:0.7rem 1.2rem;
          box-shadow:3px 3px 0px #222; text-align:center; min-width:90px;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:9px;
            color:#555; letter-spacing:2px; margin-bottom:4px;">VERSION</div>
        <div style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem;
            color:#ffd700; font-weight:800;">V1.0</div>
      </div>
    </div>

    <div style="display:flex; align-items:center; gap:1rem; margin:0.5rem 0 1.2rem;">
      <div style="flex:1; height:2px; background:#1a1a1a;"></div>
      <span style="font-family:'JetBrains Mono',monospace; font-size:9px;
          color:#444; letter-spacing:2px; white-space:nowrap;">// CARA MANUAL</span>
      <div style="flex:1; height:2px; background:#1a1a1a;"></div>
    </div>

    <div style="background:#111; border:3px solid #333; border-left:5px solid #ffd700;
        padding:1.4rem 1.5rem; margin-bottom:1rem; box-shadow:5px 5px 0px #ffd700;">
      <p style="font-family:'JetBrains Mono',monospace; font-size:0.72rem;
          color:#ffd700; margin:0 0 0.4rem; letter-spacing:1px;">🎬 PANDUAN VENDOR</p>
      <p style="font-family:'Space Grotesk',sans-serif; font-size:1rem;
          font-weight:700; color:#f0f0f0; margin:0 0 0.4rem;">
        Video Tutorial Manual FPK BPJS
      </p>
      <p style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem;
          color:#888; margin:0 0 1rem; line-height:1.6;">
        Inilah proses yang selama ini digantikan oleh aplikasi ini.
        Tanpa otomasi, setiap klaim harus dikerjakan manual seperti di video berikut.
      </p>
      <div style="background:#0d0d0d; border:2px solid #222; border-left:3px solid #444;
          padding:0.8rem 1rem; margin-bottom:0.8rem;">
        <p style="font-family:'JetBrains Mono',monospace; font-size:0.68rem;
            color:#555; margin:0 0 4px; letter-spacing:1px;">// TANPA APLIKASI INI</p>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.82rem;
            color:#666; margin:0; line-height:1.8;">
          ✗ &nbsp;Buka PDF satu per satu<br>
          ✗ &nbsp;Salin No.SEP secara manual<br>
          ✗ &nbsp;Input ke Excel satu per satu<br>
          ✗ &nbsp;Hitung nominal secara manual<br>
          ✗ &nbsp;Potensi salah input &amp; duplikat
        </p>
      </div>
      <div style="background:#0d0d0d; border:2px solid #1a3a1a; border-left:3px solid #00c47a;
          padding:0.8rem 1rem; margin-bottom:1.2rem;">
        <p style="font-family:'JetBrains Mono',monospace; font-size:0.68rem;
            color:#00c47a; margin:0 0 4px; letter-spacing:1px;">// DENGAN APLIKASI INI (dulu)</p>
        <p style="font-family:'Space Grotesk',sans-serif; font-size:0.82rem;
            color:#666; margin:0; line-height:1.8;">
          ✓ &nbsp;Upload PDF → otomatis terbaca<br>
          ✓ &nbsp;No.SEP &amp; nominal terekstrak otomatis<br>
          ✓ &nbsp;Deteksi duplikat otomatis<br>
          ✓ &nbsp;CSV siap pakai dalam hitungan detik<br>
          ✓ &nbsp;Riwayat &amp; rekap tersimpan otomatis
        </p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── TULISAN SEBELUM VIDEO ──
    st.markdown("""
    <div style="background:#0d0d0d; border:2px solid #1a1a1a; border-left:4px solid #ff6b35;
        padding:1.1rem 1.4rem; margin-bottom:1rem;">
      <p style="font-family:'JetBrains Mono',monospace; font-size:0.68rem;
          color:#ff6b35; margin:0 0 0.6rem; letter-spacing:1px;">// PESAN DARI DEVELOPER</p>
      <p style="font-family:'Space Grotesk',sans-serif; font-size:0.95rem;
          font-weight:600; color:#f0f0f0; margin:0 0 0.6rem; line-height:1.7;">
        Cape kan ngerjain ini manual satu-satu? 😄
      </p>
      <p style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem;
          color:#777; margin:0 0 0.6rem; line-height:1.8;">
        Bayangin ada <span style="color:#ff6b35; font-weight:700;">8 PDF susulan</span> masuk sekaligus —
        buka satu-satu, salin No.SEP satu-satu, input ke Excel satu-satu, hitung nominal satu-satu.
        Itu baru <em>sekali batch.</em>
      </p>
      <p style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem;
          color:#777; margin:0 0 0.6rem; line-height:1.8;">
        Aplikasi ini memproses 8 PDF itu dalam
        <span style="color:#00c47a; font-weight:700;">hitungan detik.</span>
        Hasilnya? Sama persis dengan manual — tapi tanpa capek, tanpa salah input, tanpa drama.
      </p>
      <p style="font-family:'Space Grotesk',sans-serif; font-size:0.85rem;
          color:#555; margin:0; line-height:1.8;">
        Tapi ya — sekarang bukan urusan developer lagi.
        Selamat menikmati video tutorialnya. 🙂
      </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <iframe
        src="https://drive.google.com/file/d/1MfjZGjYAel_XrnY-3R_q8KUlMCKYmcNj/preview"
        width="100%"
        height="480"
        frameborder="0"
        allowfullscreen
    ></iframe>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔒 LOGOUT →"):
        st.session_state.pin_submitted = False
        st.rerun()

    st.markdown("""
    <div style="text-align:center; padding:1.5rem 1rem 1rem; margin-top:0.5rem;
        border-top:2px solid #1a1a1a;">
      <p style="font-family:'JetBrains Mono',monospace; font-size:0.65rem;
          color:#333; letter-spacing:1px; margin:0;">
        © 2025 Isfan Fajar Anugrah &nbsp;·&nbsp; All Rights Reserved<br>
        Dilarang digandakan atau digunakan tanpa izin tertulis dari pemilik
      </p>
    </div>
    """, unsafe_allow_html=True)

import streamlit as st
import google.generativeai as genai

# !!! Kunci Bisnis Anda (PASTIKAN SUDAH DIGANTI DENGAN DATA ASLI) !!!
PASSWORD_BULAN_INI = "SAKTI30JUTA" 
LINK_BELI = "https://link-pembelian-anda.com/belisekarang" 
# ---

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Magic Copywriter PRO - The Strategist", page_icon="💡")

st.title("💡 Magic Copywriter PRO - Strategist Mode")
st.write("Dibutuhkan akses premium untuk menggunakan tool ini.")

# --- SIDEBAR & AUTHENTICATION ---
with st.sidebar:
    st.header("Login Akses")
    akses_key = st.text_input("Masukkan Password Akses Premium", type="password")
    st.info("Password akan ganti setiap bulan!")

# --- CEK AKSES ---
if akses_key == PASSWORD_BULAN_INI:
    # --- ISI APLIKASI (HANYA MUNCUL JIKA AKSES BENAR) ---
    
    st.subheader("🛠️ Konfigurasi AI (Admin)")
    # Asumsi Anda menanggung biaya API dengan 1 Kunci Utama
    API_KEY_ADMIN = st.text_input("Masukkan Google API Key Anda", type="password", help="Kunci ini hanya terlihat oleh Anda/Admin.") 
    
    st.subheader("🎯 Strategi & Target")
    
    # Fitur Baru: Memilih Kerangka Marketing
    framework = st.radio("Pilih Kerangka Copywriting", 
                         ["AIDA (Attention, Interest, Desire, Action)", 
                          "PAS (Problem, Agitate, Solve)"], 
                         horizontal=True)

    pain_point = st.text_input("Masalah Utama Pelanggan (Pain Point)", "Contoh: Sulit tidur nyenyak karena stres pekerjaan.")
    
    col1, col2 = st.columns(2)
    with col1:
        nama_produk = st.text_input("Nama Produk", placeholder="Contoh: Kopi Santai")
    with col2:
        target_action = st.text_input("Aksi yang Diinginkan (CTA)", "Contoh: Beli Sekarang / Daftar Free Trial")

    deskripsi = st.text_area("Fitur/Manfaat Produk", placeholder="Kopi tanpa kafein, mengandung lavender, menenangkan pikiran, membuat tidur cepat.")
    
    platform = st.selectbox("Untuk Platform Apa?", ["WhatsApp (Personal)", "TikTok (Viral)", "Instagram (Estetik)", "Facebook Ads"])


    if st.button("BUAT COPYWRITING SAKTI 🚀"):
        if not API_KEY_ADMIN:
            st.error("⚠️ Masukkan API Key Admin di atas dulu!")
        elif not nama_produk or not pain_point:
            st.warning("⚠️ Nama produk dan Masalah Utama Pelanggan (Pain Point) wajib diisi.")
        else:
            try:
                genai.configure(api_key=API_KEY_ADMIN)
                model = genai.GenerativeModel('gemini-pro')
                
                # --- PROMPT LEBIH CANGGIH ---
                prompt = f"""
                Bertindaklah sebagai Copywriter Profesional yang ahli dalam kerangka {framework} dan psikologi penjualan.
                Buatkan 3 variasi konten promosi yang sangat persuasif berdasarkan data berikut:
                
                - Kerangka: {framework}
                - Masalah Utama: {pain_point}
                - Produk: {nama_produk} ({deskripsi})
                - Aksi yang diinginkan (CTA): {target_action}
                - Target Platform: {platform}
                
                Gunakan gaya bahasa yang sesuai target pasar UMKM Indonesia, menyentuh emosi, dan langsung memicu klik/pembelian.
                Berikan heading untuk setiap variasi: [Variasi 1], [Variasi 2], [Variasi 3].
                """
                # --- END PROMPT CANGGIH ---
                
                with st.spinner('Sedang meracik mantra penjualan Strategis...'):
                    response = model.generate_content(prompt)
                    st.success("✅ Nih, Copywriting Strategis Kamu Siap!")
                    st.markdown(response.text)
                    
            except Exception as e:
                st.error(f"Error: {e}. Cek API Key kamu bener gak?")
                
else:
    # --- PESAN JIKA AKSES SALAH/KOSONG ---
    st.error("🚫 Akses Ditolak. Ini adalah fitur premium.")
    st.subheader("Ingin Akses Premium? Beli Sekarang!")
    st.markdown(f"Untuk mendapatkan password bulanan, Anda harus membeli langganan. Klik link di bawah:")
    st.markdown(f"[**🔥 Beli Akses Premium di SINI!**]({LINK_BELI})")
    st.warning("Jika sudah beli dan password salah, hubungi CS.")

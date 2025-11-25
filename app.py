import streamlit as st
import google.generativeai as genai

# !!! Kunci Bisnis Anda (PASTIKAN SUDAH DIGANTI DENGAN DATA ASLI) !!!
PASSWORD_BULAN_INI = "SAKTI30JUTA" 
LINK_BELI = "https://wa.me/0855850621804" 
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
    API_KEY_ADMIN = st.text_input("Masukkan Google API Key Anda", type="password", help="Kunci ini hanya terlihat oleh Anda/Admin.") 
    
    st.subheader("🎯 Strategi & Target")
    
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
                model = genai.GenerativeModel('gemini-2.5-flash') # Model yang sudah terbukti berhasil
                
                # --- PROMPT AKHIR: COPY + SARAN STRATEGIS (Lebih Agresif) ---
                prompt = f"""
                Anda adalah Konsultan Pemasaran Digital sekaligus Copywriter kelas dunia.
                Tugas Anda SANGAT PENTING: menghasilkan konten promosi DAN saran strategis.
                
                [DATA INPUT]
                - Kerangka: {framework}
                - Masalah Utama: {pain_point}
                - Produk: {nama_produk} ({deskripsi})
                - Aksi yang diinginkan (CTA): {target_action}
                - Target Platform: {platform}
                
                [INSTRUKSI OUTPUT WAJIB]
                1. Hasilkan 3 variasi konten promosi yang sangat persuasif (sesuai kerangka).
                2. Hasilkan 3 poin analisis dan saran strategis bagaimana meningkatkan konversi dari konten di atas.
                
                FORMAT OUTPUT WAJIB HARUS SEPERTI INI (Gunakan Markdown Header):
                                
                ## 1. Hasil Generasi Copywriting (3 Variasi)
                [Tulis 3 variasi di sini, gunakan emoji yang relevan]
                                
                ---
                                
                ## 2. Saran Strategi AI untuk Konversi (3 Poin)
                [Tulis 3 poin analisis dan strategi di sini, jangan kosongkan bagian ini!]
                """
                # --- END PROMPT CANGGIH ---
                
                with st.spinner('Sedang meracik strategi dan mantra penjualan...'):
                    response = model.generate_content(prompt)
                    st.success("✅ Nih, Copywriting dan Strategi Pemasaran kamu Siap!")
                    st.markdown(response.text)
                    
            except Exception as e:
                st.error(f"Error: {e}. Terjadi masalah saat memanggil AI. Coba masukkan API Key lagi.")
                
else:
    # --- PESAN JIKA AKSES SALAH/KOSONG ---
    st.error("🚫 Akses Ditolak. Ini adalah fitur premium.")
    st.subheader("Ingin Akses Premium? Beli Sekarang!")
    st.markdown(f"Untuk mendapatkan password bulanan, Anda harus membeli langganan. Klik link di bawah:")
    st.markdown(f"[**🔥 Beli Akses Premium di SINI!**](https://wa.me/0855850621804)")
    st.warning("Jika sudah beli dan password salah, hubungi CS.")

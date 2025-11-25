import streamlit as st
import google.generativeai as genai

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Magic Copywriter", page_icon="🤖")

st.title("🤖 Magic Copywriter - Tool Affiliate")
st.write("Masukkan detail produk, biarkan AI yang jualan!")

# --- KOLOM INPUT ---
with st.sidebar:
    st.header("Kunci Rahasia")
    api_key = st.text_input("Masukkan Google API Key", type="password")
    st.caption("Ambil gratis di: aistudio.google.com")

nama_produk = st.text_input("Nama Produk", placeholder="Contoh: Kopi Diet")
deskripsi = st.text_area("Deskripsi Produk", placeholder="Kopi hijau penurun berat badan...")
platform = st.selectbox("Untuk Platform Apa?", ["WhatsApp (Personal)", "TikTok (Viral)", "Instagram (Estetik)", "Shopee (Deskripsi)"])

# --- LOGIKA TOMBOL ---
if st.button("BUAT KATA-KATA SAKTI 🚀"):
    if not api_key:
        st.error("⚠️ Masukkan API Key dulu di menu sebelah kiri/atas!")
    elif not nama_produk:
        st.warning("⚠️ Nama produk jangan kosong dong.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = f"""
            Bertindaklah sebagai Copywriter kelas dunia.
            Buatkan 2 variasi copywriting untuk produk: {nama_produk}.
            Deskripsi: {deskripsi}.
            Target Platform: {platform}.
            Gunakan Bahasa Indonesia yang menarik, persuasive, dan gunakan emoji.
            """
            
            with st.spinner('Sedang meracik mantra penjualan...'):
                response = model.generate_content(prompt)
                st.success("✅ Nih, Copas Aja:")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Error: {e}. Cek API Key kamu bener gak?")

import time
import streamlit as st

st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-UvXeM8HbeDkp85VZmo06sKz2olT8gjUI5cXlKIHdHFQvFYy6cH775d7w_kXrWJXveOU4r1q4ekR9llbWp4hpIsfzyDSClHJouC6hK8rMYdLXBKtin1GNhnR9z0qRldWRptRrfn1Sh-ei2WXAjUjbhVb332YnY8bdbUg4vG2PHXsbDHTomrehZkfs9ghK/s1200/Untitled-1.jpg", caption=None, width=700, use_column_width="never", clamp=False, channels="RGB", output_format="auto")

st.write("""
        Program Hitung Gaji PT. Sejahtera adalah solusi perangkat lunak canggih yang dirancang khusus untuk mengelola dan menghitung penggajian karyawan secara efisien dan akurat.
        """)



class Karyawan:
        
        def __init__(self, nama, jam_kerja_per_hari, jumlah_hari_kerja, jabatan, berkeluarga=False, kendaraan_pribadi=False):
                self.nama = nama
                self.jam_kerja_per_hari = jam_kerja_per_hari
                self.jumlah_hari_kerja = jumlah_hari_kerja
                self.jabatan = jabatan
                self.tarif_perjam = 0
                self.bonus = 0
                self.tunjangan_berkeluarga = 0
                self.tunjangan_kendaraan_pribadi = 0
                self.berkeluarga = berkeluarga
                self.kendaraan_pribadi = kendaraan_pribadi
                self.pajak = 0 

        def hitung_gaji(self):
                if self.jabatan.lower() == "manager operasional":
                        self.tarif_perjam = 30000
                elif self.jabatan.lower() == "manager personality":
                        self.tarif_perjam = 34000
                elif self.jabatan.lower() == "manager pemasaran":
                        self.tarif_perjam = 34500
                elif self.jabatan.lower() == "manager pabrik":
                        self.tarif_perjam = 35500
                elif self.jabatan.lower() == "manager sdm":
                        self.tarif_perjam = 34200
                elif self.jabatan.lower() == "administrasi":
                        self.tarif_perjam = 35000
                else:
                        return None

                gaji = self.tarif_perjam * (self.jam_kerja_per_hari * self.jumlah_hari_kerja)

                if self.jumlah_hari_kerja > 24:
                        self.bonus = 500000
                        gaji += self.bonus

                if self.berkeluarga:
                        self.tunjangan_berkeluarga = 0.2 * gaji
                        gaji += self.tunjangan_berkeluarga

                if self.kendaraan_pribadi:
                        self.tunjangan_kendaraan_pribadi = 0.1 * gaji
                        gaji += self.tunjangan_kendaraan_pribadi
                
                if gaji > 3500000 :
                        self.pajak = 0.1 * gaji
                        gaji -= self.pajak
                


                return gaji

def main():
        
        jabatan = None

        while jabatan is None:
                
                nama = st.text_input("Masukkan Nama Anda: ",placeholder="masukan nama...")
                jabatan = st.selectbox('Masukan Jabatan Anda: ',('Manager Operasional', 'Manager Personality', 'Manager Pemasaran','Manager Pabrik','Manager SDM','Administrasi'))
                jam_kerja_per_hari = st.number_input("Masukkan Jumlah Jam Kerja per Hari: ")
                jumlah_hari_kerja = st.number_input("Masukkan Jumlah Hari Kerja dalam Sebulan: ")
                berkeluarga = st.checkbox("Sudah Berkeluarga")
                kendaraan_pribadi = st.checkbox("Menggunakan Kendaraan Pribadi")
                
                
                karyawan = Karyawan(nama, jam_kerja_per_hari, jumlah_hari_kerja, jabatan, berkeluarga, kendaraan_pribadi)

                
                gaji = karyawan.hitung_gaji()

                
                if st.button("Hitung") and gaji is not None:
                        with st.spinner('Mohon Ditunggu'):
                                time.sleep(2)
                                st.success(f"""Halo {karyawan.nama} Gaji Anda sebagai Staff {karyawan.jabatan} adalah sebesar : Rp{gaji:,.2f}""")
                else:
                        st.info("Klik Hitung Untuk Menghitung Gaji Anda")

                st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2GcBk6-DJjfj_WKv2FiGo0B2Y0hyphenhyphen3Fize1eTd5dx6H_4E0rc4en4qdrN2n2epvSH3ZwH8UkuDbqhZ9ASpyBxziXJQkeYPWHBM7xxg2P7vquTshR8D0NzWpdw2TZOZEttiMWKyQy-fEsH8qAcR82xzoipjx0AFLJDwvoFu6WMKksue0O-49HGyLWQF0BF8/s1200/2.jpg", caption=None, width=700, use_column_width="never", clamp=False, channels="RGB", output_format="auto")

if __name__ == "__main__":
        main()



**1. Citra 1 (UJI CITRA: 01 – High Quality Enhanced)**

**Karakteristik Area Hasil Segmentasi**
**Area Dekan (Ada TTD)**	

Status	SIGNATURE PRESENT
Foreground Pixels	43678 / 520515
Kepadatan Piksel	0.0839
Komponen Terhubung	50

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Menghasilkan garis tanda tangan yang bersih
Otsu: Mengisolasi stroke tanda tangan secara utuh dan tebal.
Adaptive: Memisahkan detail tepi garis tanda tangan dan teks.

- Metode Morfologi
Opening: Mereduksi noise mikro tanpa merusak struktur huruf/tanda tangan. 
Closing: Menyambungkan goresan pena yang terputus menjadi lebih padat. 
Morphology final: Menghasilkan binary mask tanda tangan yang padat, utuh, dan solid. 


**Area Blank (Tanpa TTD)**

Status	SIGNATURE ABSENT
Foreground Pixels	253 / 260400
Kepadatan Piksel	0.0010
Komponen Terhubung	2

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Latar belakang bersih, tetapi noda/titik kertas ikut terdeteksi.
Otsu: Latar belakang dominan hitam dengan sedikit bintik terisolasi.
Adaptive: Menghasilkan noise bintik-bintik halus (salt-and-pepper).

- Metode Morfologi
Opening: Menghapus noise salt-and-pepper hasil Adaptive Thresholding 
Closing: Memadatkan sisa bintik terisolasi tanpa memunculkan noise baru
Morphology final: Menyisakan area murni latar belakang hitam (background = 0).

**2. Citra 2 UJI CITRA: 02 - Low Contrast**

**Karakteristik Area Hasil Segmentasi**
**Area Dekan (Ada TTD)**	

Status	SIGNATURE PRESENT
Foreground Pixels	43940 / 520515
Kepadatan Piksel	0.0844
Komponen Terhubung	50

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Beberapa garis tipis pada tanda tangan tampak sedikit memudar/terputus karena perbedaan intensitas tinta dan kertas yang tipis. 
Otsu: Menyesuaikan batas secara otomatis; garis tanda tangan terpotong lebih sedikit dibanding Global Thresh. 
Adaptive: Paling unggul menangkap seluruh detail tepi garis tanda tangan dan teks halus meski kontrasnya rendah. 

- Metode Morfologi
Opening: Mereduksi bintik mikro di sekitar garis tanda tangan tanpa mengikis kerapatan huruf. 
Closing: Menyambungkan kembali celah atau segmen garis tanda tangan yang terputus akibat kontras rendah.
Morphology final: Menghasilkan binary mask tanda tangan yang padat, utuh, dan solid. 


**Area Blank (Tanpa TTD)**
Status	SIGNATURE ABSENT
Foreground Pixels	255 / 260400
Kepadatan Piksel	0.0010
Komponen Terhubung	2

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Latar belakang bersih hitam, namun bintik noda fisik pada kertas tetap terdeteksi. 
Otsu: MLatar belakang dominan hitam bersih dengan hanya bintik noda terisolasi yang tersisa
Adaptive: Memunculkan salt-and-pepper noise (bintik-bintik putih halus) di seluruh latar belakang polos.

- Metode Morfologi
Opening: Menghapus seluruh salt-and-pepper noise hasil Adaptive Thresholding secara sempurna.
Closing: Memadatkan bintik noda fisik tersisa tanpa menambah noise baru pada latar belakang
Morphology final: Menghasilkan latar belakang murni hitam bersih (hanya menyisakan titik noda fisik mikro). 

**3. Citra 3 (UJI CITRA: 03 - Blurred)**

**Karakteristik Area Hasil Segmentasi**
**Area Dekan (Ada TTD)**

Status	SIGNATURE PRESENT
Foreground Pixels	63212 / 520515
Kepadatan Piksel	0.1214
Komponen Terhubung	34

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Mengisolasi tanda tangan dan teks cukup baik, namun tepi garis sedikit membesar/pelebaran akibat efek blur.
Otsu: Menghasilkan garis tanda tangan yang tebal, padat, dan terisolasi secara utuh 
Adaptive: Menangkap detail transisi batas tepi tulisan, tetapi menghasilkan tepi garis yang sedikit lebih kasar.

- Metode Morfologi
Opening: Menghaluskan tepi goresan (smoothing) dan mereduksi noise mikro pada batas garis.   
Closing: Menyambungkan celah mikro dan memadatkan interior garis tanda tangan yang melemah akibat efek kabur.   
Morphology final: Menghasilkan binary mask tanda tangan yang solid, terhubung, dan utuh.

**Area Blank (Tanpa TTD)**	
Status	SIGNATURE ABSENT
Foreground Pixels	350 / 260400
Kepadatan Piksel	0.0013
Komponen Terhubung	2

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Latar belakang hitam bersih, menyisakan bintik noda fisik mikro.
Otsu: Latar belakang hitam bersih
Adaptive: Memunculkan sedikit noise bintik halus di latar belakang polos.

- Metode Morfologi
Opening: Menghapus bintik-bintik noise halus latar belakang hasil Adaptive Thresh.   
Closing: Memadatkan noda fisik mikro tersisa.
Morphology final: Menyisakan latar belakang murni hitam pekat.

**4. Citra 4 (UJI CITRA: 04 - High Noise)**
   
**Karakteristik Area Hasil Segmentasi**	
**Area Dekan (Ada TTD)**

Status	SIGNATURE PRESENT
Foreground Pixels	43059 / 520515
Kepadatan Piksel	0.0827
Komponen Terhubung	56

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Mengisolasi tanda tangan dengan baik.   
Otsu: Menghasilkan garis tanda tangan yang tebal dan utuh
Adaptive: Menangkap detail garis, tetapi memunculkan noise salt-and-pepper sangat padat.

- Metode Morfologi
Opening: Berhasil menghilangkan noise mikro di sekitar tanda tangan.
Closing: Menyambungkan celah garis tanda tangan yang terputus.   
Morphology final: Menghasilkan binary mask tanda tangan yang sangat bersih, padat, dan utuh.

**Area Blank (Tanpa TTD)**
Status	SIGNATURE ABSENT
Foreground Pixels	247 / 260400
Kepadatan Piksel	0.0009
Komponen Terhubung	2

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Latar belakang bersih hitam, menyisakan bintik fisik kertas.
Otsu: Menghasilkan latar belakang dominan hitam bersih.
Adaptive: Seluruh area latar belakang tertutup bintik-bintik noise putih yang sangat tinggi.   

- Metode Morfologi
Opening: Menghapus hampir seluruh noise salt-and-pepper hasil Adaptive Thresh
Closing: Memadatkan sisa bintik noda fisik.      
Morphology final: MMenyisakan latar belakang murni hitam (background = 0).   

**5. Citra 5 (UJI CITRA: 05 - Low Resolution)**

**Karakteristik Area Hasil Segmentasi**
**Area Dekan (Ada TTD)**	

Status	SIGNATURE PRESENT
Foreground Pixels	48364 / 520515
Kepadatan Piksel	0.0929
Komponen Terhubung	52

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Tanda tangan terdeteksi, namun garis agak tipis/patah akibat aliasing piksel
Otsu: Mampu mempertahankan ketebalan garis tanda tangan dengan baik
Adaptive: Menangkap tepi piksel lebih detail, tetapi tepi garis terlihat agak kasar (jagged).

- Metode Morfologi
Opening: Menghaluskan tepi garis (smoothing) dan mereduksi noise mikro
Closing: Menyambung dan menebalkan kembali piksel-piksel garis yang terpisah.   
Morphology final: Menghasilkan bentuk biner tanda tangan yang utuh dan solid.

**Area Blank (Tanpa TTD)**	
Status	SIGNATURE ABSENT
Foreground Pixels	269 / 260400
Kepadatan Piksel	0.0010
Komponen Terhubung	2

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: enghapus hampir seluruh noise salt-and-pepper hasil Adaptive Thresh
Otsu: Mampu mempertahankan ketebalan garis tanda tangan dengan baik
Adaptive: Menangkap tepi piksel lebih detail, tetapi tepi garis terlihat agak kasar (jagged).

- Metode Morfologi
Opening: Menghapus noise bintik-bintik halus latar belakang
Closing: Memadatkan bintik noda kecil.  
Morphology final: Menghasilkan latar belakang yang bersih dari noise.

**6. Citra 6 (UJI CITRA: 06 - Faded/Underexposed)**

**Karakteristik Area Hasil Segmentasi**
**Area Dekan (Ada TTD)**

Status	SIGNATURE PRESENT
Foreground Pixels	43789 / 520515
Kepadatan Piksel	0.0841
Komponen Terhubung	50

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: GAGAL TOTAL (Hitam Pekat): Tanda tangan dan teks hilang sepenuhnya
Otsu: SANGAT BAIK: Mampu mengadaptasi histogram gelap dan mengisolasi tanda tangan secara sempurna.   
Adaptive: Menangkap detail tanda tangan dan teks dengan jelas meski kondisi gelap

- Metode Morfologi
Opening: Membersihkan noise mikro di sekitar teks dan tanda tangan
Closing: Menyambungkan bagian garis tanda tangan yang pudar (faded).   
Morphology final: Menghasilkan binary mask tanda tangan yang padat, utuh, dan terhubung.

Area Blank (Tanpa TTD)	
Status	SIGNATURE ABSENT
Foreground Pixels	254 / 260400
Kepadatan Piksel	0.0010
Komponen Terhubung	2

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Latar belakang hitam pekat.   
Otsu: Latar belakang hitam bersih.
Adaptive: Menghasilkan noise bintik yang sangat minim

- Metode Morfologi
Opening: Menghapus bintik-bintik noise tersisa.
Closing: Memadatkan bintik kecil terisolasi.
Morphology final: Latar belakang menjadi murni hitam

**7. Citra 7 (UJI CITRA: 07 - Color Shift**)

**Karakteristik Area Hasil Segmentasi**
**Area Dekan (Ada TTD)**

Status	SIGNATURE PRESENT
Foreground Pixels	43870 / 520515
Kepadatan Piksel	0.0843
Komponen Terhubung	50

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Mengisolasi tanda tangan dengan bersih karena kontras luminansi tinta tetap terjaga.     
Otsu: Menghasilkan garis tanda tangan yang padat, jelas, dan utuh.
Adaptive: Menangkap detail tepi goresan tanda tangan dengan sangat tajam

- Metode Morfologi
Opening: Mereduksi noise mikro di sekitar tepi tulisan tanpa mengurangi ketebalan huruf.
Closing: Menyambungkan kembali celah garis halus pada goresan tanda tangan
Morphology final: Menghasilkan binary mask tanda tangan yang solid dan utuh

Area Blank (Tanpa TTD)	
Status	SIGNATURE ABSENT
Foreground Pixels	253 / 260400
Kepadatan Piksel	0.0010
Komponen Terhubung	2

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: MLatar belakang bersih hitam, menyisakan bintik noda fisik mikro pada kertas.     
Otsu: Latar belakang hitam bersih dari noise
Adaptive: Memunculkan sedikit salt-and-pepper noise halus di latar belakang polos.   

- Metode Morfologi
Opening: menghapus seluruh bintik-bintik noise halus hasil Adaptive Thresh
Closing: Memadatkan sisa bintik fisik tanpa menambah noise baru.   
Morphology final: Menyisakan latar belakang murni hitam bersih.

**8. Citra 8 (08_JPEGCompression_Artifacts)**
   
**Karakteristik Area Hasil Segmentasi**
**Area Dekan (Ada TTD)**

Status	SIGNATURE PRESENT
Foreground Pixels	43998 / 520515
Kepadatan Piksel	0.0849
Komponen Terhubung	49

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Mampu memisahkan tanda tangan dari latar belakang cukup baik     
Otsu: Mengisolasi goresan tanda tangan secara tebal dan stabil.   
Adaptive: Memunculkan sedikit salt-and-pepper noise halus di latar belakang polos

- Metode Morfologi
Opening: Menghilangkan noise artefak kompresi di sekitar tepi batas tanda tangan.
Closing: Menutup celah kecil pada garis akibat hilangnya detail frekuensi tinggi pada JPEG
Morphology final: Menghasilkan binary mask tanda tangan yang terhubung rapi dan bersih.

**Area Blank (Tanpa TTD)**
Status	SIGNATURE ABSENT
Foreground Pixels	253 / 260400
Kepadatan Piksel	0.0010
Komponen Terhubung	2

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Latar belakang hitam bersih.     
Otsu: Latar belakang hitam bersih hanya menyisakan bintik noda fisik
Adaptive: Menghasilkan bintik noise mikro di area latar belakang.   

- Metode Morfologi
Opening: Menghapus bintik-bintik noise halus pada latar belakang.
Closing: Memadatkan bintik kecil tersisa.   
Morphology final: Latar belakang menjadi murni hitam bersih.

**9. Citra 9 (09_CombinedDegradation)**
    
**Karakteristik Area Hasil Segmentasi**
**Area Dekan (Ada TTD)**

Status	SIGNATURE PRESENT
Foreground Pixels	43998 / 520515
Kepadatan Piksel	0.0903
Komponen Terhubung	52

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Memisahkan tanda tangan dengan baik meski terdapat kombinasi degradasi
Otsu: SANGAT OPTIMAL: Menghasilkan mask tanda tangan yang paling utuh dan tebal
Adaptive: Menangkap detail struktur garis, tetapi memunculkan bintik noise latar belakang

- Metode Morfologi
Opening: Membersihkan noise akumulatif di sekitar goresan TTD dan teks
Closing: Menyambungkan segmen-segmen garis yang terputus akibat akumulasi degradasi
Morphology final: Menghasilkan binary mask tanda tangan yang solid, utuh, dan presisi

**Area Blank (Tanpa TTD)**	
Status	SIGNATURE ABSENT
Foreground Pixels	261 / 260400
Kepadatan Piksel	0.0010
Komponen Terhubung	2

**Analisis Perbandingan Komparatif**
- Metode Thresholding
Global: Latar belakang hitam bersih dengan bintik noda fisik mikro.   
Otsu: Latar belakang sangat bersih.
Adaptive: Memunculkan bintik-bintik noise di area polos

- Metode Morfologi
Opening: Menghapus seluruh noise bintik halus pada latar belakang.   
Closing: Memadatkan titik noda fisik mikro.
Morphology final: Area murni latar belakang hitam pekat

# Literature GAP Matrix untuk Fisheries Briefing Assistant Timor-Leste

Prototipe tugas Introduction to Generative AI. Python 3.10+; mode demo hanya membutuhkan standard library.

## Status hasil

Matriks laporan disusun melalui telaah literatur berbantuan AI yang memerlukan verifikasi kelompok dan penelusuran sumber resmi pada 29 Oktober 2026. **Bukan hasil eksekusi LLM lokal.** Korpus bawaan berisi delapan catatan kurasi sekunder dengan DOI, URL, dan penunjuk bagian. Korpus bukan salinan full text artikel. Dua artikel domain bukan penelitian RAG dan diberi kategori terpisah.

Mode demo menjalankan chunking dan BM25, merekam bukti yang ditemukan, lalu mengekspor kolom kurasi. Mode generate menjalankan retrieval lalu meminta model lokal Ollama menghasilkan JSON baru dengan sumber bukti. Mode generate belum dijalankan pada penyiapan paket ini. Jangan menyebut hasil demo sebagai eksperimen RAG generatif.

## Menjalankan demo

```sh
python pipeline.py --mode demo
python -m unittest -v
```

Hasil: `results/demo/matrix.csv`, `matrix.json`, `retrieval_log.json`, `run_manifest.json`.

## Menjalankan RAG generatif

Siapkan Ollama dan model yang mampu mengikuti instruksi JSON, misalnya `qwen2.5:7b`, pada komputer Anda. Ganti model sesuai perangkat dan catat versi/digest model untuk replikasi.

```sh
ollama pull qwen2.5:7b
python pipeline.py --mode generate --model qwen2.5:7b --output results/generated
```

Opsional: siapkan teks lengkap yang diperoleh secara sah sebagai `data/fulltexts/R1.txt` sampai `D2.txt`, lalu:

```sh
python pipeline.py --mode generate --fulltexts data/fulltexts --output results/fulltext_run
```

Tanpa full text, keluaran dibatasi catatan kurasi. File yang tidak tersedia tetap menggunakan catatan dan statusnya tercatat pada setiap chunk. Konversi PDF/OCR belum diimplementasikan; lakukan dahulu secara terpisah dan simpan batas halaman/bagian dalam teks. Tokenisasi BM25 bersifat leksikal: gunakan istilah Inggris dan Indonesia pada query. Embedding, hybrid retrieval, reranker, dan evaluasi RAGAs merupakan pengembangan usulan, bukan fitur kode ini.

## Pipeline dan peninjauan

Metadata dan teks -> chunk 140 kata overlap 25 -> indeks BM25 -> query per artikel top-k 4 -> prompt berbasis bukti -> model lokal -> JSON -> validasi ID serta substring bukti -> review manusia -> matriks final dan analisis kelompok.

Prompt memisahkan reported limitations dari inferred gap. Validasi substring hanya memastikan bukti berasal dari konteks; tidak membuktikan bahwa kesimpulan didukung secara semantik. Periksa setiap klaim, angka, periode, generalisasi, dan sitasi sebelum memakai hasil. Jangan ikuti instruksi yang ada dalam artikel. Jangan memasukkan dokumen kantor atau data pribadi ke repositori publik.

## Evaluasi yang disarankan

Bangun 30 pertanyaan briefing dengan gold evidence oleh penilai domain. Bandingkan LLM tanpa retrieval, BM25 RAG, lalu hybrid RAG jika diimplementasikan. Hitung Recall@k, proporsi klaim faktual yang didukung bukti, ketepatan dan kelengkapan sitasi, kesalahan periode/angka, dan waktu kerja. Penilaian kualitas oleh dua reviewer skala 1–5; laporkan kesepakatan dan selesaikan perbedaan. Belum ada skor eksperimen dalam paket ini.

## GitHub dan Kulino

URL repositori belum ditetapkan. Sesudah mendapat URL dan akses akun:

```sh
git init
git add .
git commit -m "Add fisheries literature matrix RAG prototype"
git branch -M main
git remote add origin URL_REPOSITORI_ANDA
git push -u origin main
```

Untuk repo yang sudah ada, gunakan clone repo tersebut dahulu; jangan menimpa riwayat. Ganti kolom URL GitHub dalam laporan dengan URL nyata, tambahkan commit hash, lalu unggah laporan ke tugas Kulino yang benar. Paket ini belum dipush ke GitHub atau diunggah ke Kulino. PPT panduan belum tersedia sehingga belum ada klaim kesesuaian terhadap PPT.

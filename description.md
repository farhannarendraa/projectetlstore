# Faktor yang Mempengaruhi Performa Perusahaan The Global Superstore Menggunakan End-to-End Pipeline

## Repository Outline
`Repository ini menjelaskan proses End-to-End pipeline menggunakan ETL (Extract, Load, Transform) kemudian dilakukan visualisasi menggunakan Elasticsearch dan Kibana`

Contoh:
```
1. project_m3 - Proses otomatisasi ETL (Extract, Load, dan Transform)
2. P2M3_Farhan_Narendra_Achyara_GX.ipynb - Notebook yang berisi validasi data setelah proses ETL menggunakan package Great Expectation
3. P2M3_Farhan_Narendra_Achyara_conceptual.txt - Teks untuk menjawab pertanyaan konsep terkait data engineering.
4. gx - Kumpulan tools untuk validasi data di notebook P2M3_Farhan_Narendra_Achyara_GX.ipynb.
5. P2M3_Farhan_Narendra_Achyara_ddl.sql - SQL tool untuk memasukkan data ke PostrgreSQL yang ada di docker. 
6. images - kumpulan gambar dari aplikasi Kibana yang berisi hasil visualisasi dan insight.
```

## Problem Background
`Sebuah toko store bernama The Global Superstore telah mengumpulkan data transaksi penjualan dari sebuah toko ritel global yang mencakup berbagai wilayah di dunia, termasuk Amerika Serikat, EMEA, APAC, Afrika, dan Amerika Latin. Data ini mencatat detail pesanan dari tahun 2011 hingga 2014, termasuk informasi tentang produk, pelanggan, pengiriman, profit, biaya pengiriman, dan prioritas pesanan untuk berbagai kategori produk seperti furniture, office supplies, dan teknologi`

## Project Output
`Tujuan dari proyek ini adalah melakukan visualisasi data menggunakan elasticsearch dan kibana dan disampaikan pada pihak The Global Superstore sebagai data analyst. Laporan ini akan berisi analisis mendalam mengenai karakteristik produk yang paling diminati oleh pelanggan baik dari segi kategori, region, maupun segmen pelanggan. Selain itu, laporan ini tidak hanya mengidentifikasi preferensi pelanggan, tetapi juga memberikan rekomendasi strategis kepada tim pemasaran, penjualan, dan operasional untuk meningkatkan penjualan, efisiensi biaya, dan profitabilitas secara keseluruhan.`

## Data
`Data yang digunakan adalah database dari Kaggle berupa csv hasil record perusahaan The Global Superstore.`
`Kolom yang digunakan dalam analisis adalah:`

## Method
`Metode yang digunakan adalah proses ETL menggunakan apache airflow untuk otomatisasi kodingan dari pengambilan database dari PostgreSQL, kemudian dilakukan cleaning data di Python, dan load data menggunakan Elasticsearch. Kemudian validasi data menggunakan Great Expectation`

## Stacks
`Bahasa pemrograman yang digunakan adalah Python dengan package great expectation`

## Reference
- [Price Elasticity of Demand: Meaning, Types, and Factors That Impact It](https://www.investopedia.com/terms/p/priceelasticity.asp)
- [Global Super Store Dataset](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset)

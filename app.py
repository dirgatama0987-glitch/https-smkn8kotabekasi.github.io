from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SMKN 8 Kota Bekasi</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f6fb;
            color: #172033;
        }

        header {
            background: linear-gradient(135deg, #071b3a, #0759a6);
            color: white;
            padding: 30px 20px;
            text-align: center;
        }

        header h1 {
            font-size: 34px;
            margin: 10px 0;
        }

        nav {
            background: #082b50;
            padding: 14px;
            text-align: center;
        }

        nav a {
            display: inline-block;
            color: white;
            text-decoration: none;
            margin: 6px 10px;
            font-size: 14px;
        }

        .hero {
            padding: 65px 20px;
            text-align: center;
            background: linear-gradient(135deg, #dcecff, #ffffff);
        }

        .hero h2 {
            font-size: 30px;
            color: #073c78;
        }

        .hero p {
            line-height: 1.7;
        }

        .button {
            display: inline-block;
            background: #0759a6;
            color: white;
            padding: 13px 22px;
            border-radius: 8px;
            text-decoration: none;
            margin-top: 12px;
        }

        .container {
            max-width: 1000px;
            margin: auto;
            padding: 25px 18px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
        }

        .card {
            background: white;
            padding: 22px;
            border-radius: 12px;
            box-shadow: 0 3px 12px #00000010;
        }

        .card h3 {
            color: #0759a6;
        }

        footer {
            background: #082b50;
            color: white;
            text-align: center;
            padding: 25px 15px;
            margin-top: 30px;
        }
    </style>
</head>
<body>

<header>
    <h1>SMKN 8 KOTA BEKASI</h1>
    <p>Sekolah Menengah Kejuruan Kota Bekasi</p>
</header>

<nav>
    <a href="/">Beranda</a>
    <a href="/spmb">Info SPMB</a>
    <a href="/info">Info</a>
    <a href="/keahlian">Program Keahlian</a>
    <a href="/gallery">Gallery</a>
    <a href="/admin">Admin</a>
</nav>

<section class="hero">
    <h2>Selamat Datang di SMKN 8 Kota Bekasi</h2>
    <p>
        Website informasi sekolah untuk mengenal program keahlian,
        kegiatan, berita, dan informasi penerimaan peserta didik baru.
    </p>
    <a class="button" href="/spmb">Informasi SPMB</a>
</section>

<main class="container">
    <h2>Jelajahi Website Sekolah</h2>

    <div class="cards">
        <div class="card">
            <h3>Informasi SPMB</h3>
            <p>Informasi penerimaan peserta didik baru.</p>
            <a href="/spmb">Selengkapnya</a>
        </div>

        <div class="card">
            <h3>Program Keahlian</h3>
            <p>Kenali enam program keahlian di sekolah.</p>
            <a href="/keahlian">Lihat program</a>
        </div>

        <div class="card">
            <h3>Berita Sekolah</h3>
            <p>Informasi dan kegiatan terbaru sekolah.</p>
            <a href="/info">Lihat informasi</a>
        </div>

        <div class="card">
            <h3>Galeri Sekolah</h3>
            <p>Kenali fasilitas dan lingkungan sekolah.</p>
            <a href="/gallery">Lihat galeri</a>
        </div>
    </div>
</main>

<footer>
    <p>Website SMKN 8 Kota Bekasi</p>
    <p>Informasi sekolah dalam satu tempat.</p>
</footer>

</body>
</html>
"""

@app.route("/")
def beranda():
    return render_template_string(HTML)

@app.route("/<halaman>")
def halaman(halaman):
    return render_template_string(
        HTML.replace(
            "Selamat Datang di SMKN 8 Kota Bekasi",
            halaman.replace("-", " ").title()
        )
    )

if __name__ == "__main__":
    app.run(debug=True)

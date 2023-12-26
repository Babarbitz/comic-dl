pkgname=get-comics
pkgrel=1
pkgver=0.1.4
conflicts=('get-comics')
pkgdesc="Downloads albumart for MPD"
arch=('x86_64')
url="https://github.com/Babarbitz/get-comics"
license=('GPL3')
depends=('python' 'mpd' 'python-beautifulsoup4' 'python-mpd2' 'python-requests' 'python-tqdm')
makedepends=('python-build'
             'python-installer'
             'python-wheel')
source=("https://github.com/Babarbitz/get-comics/archive/v${pkgver}.tar.gz")
sha256sums=('SKIP')
build() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

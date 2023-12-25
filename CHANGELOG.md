# CHANGELOG



## v0.1.2 (2023-12-25)

### Chore

* chore: Removed setup.py ([`517bd0f`](https://github.com/Babarbitz/comic-dl/commit/517bd0f4bebb8bc59fbfbcfdcf7f19864474c526))

### Fix

* fix: fix several bugs in download method ([`2be6fd9`](https://github.com/Babarbitz/comic-dl/commit/2be6fd9416faceb014f6a4f0cf0bd2805232da5c))

### Refactor

* refactor: Added pagination parsing/tests ([`5282807`](https://github.com/Babarbitz/comic-dl/commit/52828072cd6d574d154127d31de59da3d3146157))

* refactor: search now uses _makeSearchUrl ([`f96623d`](https://github.com/Babarbitz/comic-dl/commit/f96623d32761095ef7c30ea9da3a892ed711944a))

* refactor: Added _makeSearchUrl

Better for unit testing search urls ([`e85eef2`](https://github.com/Babarbitz/comic-dl/commit/e85eef293c42143778cc9f866cf6009966dbd2e0))

* refactor: Moved search functions to new file

The search function is being broken down into smaller chunks to allow
for better integration/unit testing. ([`578c850`](https://github.com/Babarbitz/comic-dl/commit/578c85045f2f10f1737fbaecc802f16041a78568))


## v0.1.1 (2023-07-25)

### Fix

* fix: Add __future__ import to sample test ([`87a8d02`](https://github.com/Babarbitz/comic-dl/commit/87a8d024184aeeaaf587051413c35aee954abb0e))


## v0.1.0 (2023-07-25)

### Chore

* chore: Removed __version__ from __init__.py ([`a43bb2a`](https://github.com/Babarbitz/comic-dl/commit/a43bb2a42f4576aad415fd111325d60f35c8e59e))

### Feature

* feat: Testing version incrementation ([`9f37714`](https://github.com/Babarbitz/comic-dl/commit/9f37714a9d5e73322b988a950a9256a8d89e4dce))

### Unknown

* bug: Testing semantic-release auto versioning ([`60b5516`](https://github.com/Babarbitz/comic-dl/commit/60b5516020a0786159d7a2a4648c124e8e7dd155))

* Repo refactor

- chore: Updated repo name to get-comics ([`3414bb7`](https://github.com/Babarbitz/comic-dl/commit/3414bb73429244adada1bc69343a17b6e353f152))

* python pre-commit support

add: Python pre-commit config to run linting on the pre commit hook ([`6070cd2`](https://github.com/Babarbitz/comic-dl/commit/6070cd24fc66fdac2e266aa1e00851138e09408b))

* Removed Test.py

chore: Removed test.py so it is no longer tracked in vc ([`b0e361f`](https://github.com/Babarbitz/comic-dl/commit/b0e361f22a6ca5c01a14dbfec9175b1f9c51564c))

* Removed todo.org ([`3a0a919`](https://github.com/Babarbitz/comic-dl/commit/3a0a919efbe896aaf1273da804f7eb1c841b6eda))

* Added TODO to readme ([`daf92da`](https://github.com/Babarbitz/comic-dl/commit/daf92da392cacfc8f5c95505f29fd78c535493ed))

* Create README.md

Added base readme for the project ([`2b09f00`](https://github.com/Babarbitz/comic-dl/commit/2b09f0053bb8bfbffa27e33bd8a5725b6c603c04))

* Removed comments from bin file ([`3ceb87c`](https://github.com/Babarbitz/comic-dl/commit/3ceb87c728db267eb8b0c5888866633006794f30))

* Initial commit

- Added basic implementation of comic-dl
  - Users can search and download comics (only ones avaialbe from &#34;main
    server&#34; currently)
- Added license ([`4e5b47a`](https://github.com/Babarbitz/comic-dl/commit/4e5b47a75429d77af9b860ccb60982801772ebc3))

* Initial commit ([`0a47fcb`](https://github.com/Babarbitz/comic-dl/commit/0a47fcba5056a349a3532ee07e39f0354bfe153e))

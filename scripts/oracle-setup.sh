#!/usr/bin/env bash
# Set up a self-contained Amber "oracle": everything needed to verify and re-run an
# Amber bundle of the OIDEli corpus entry, installed under ONE directory, no root,
# no changes to ~/.bashrc, ~/.local or anything outside that directory.
#
#   bash oracle-setup.sh                # installs under ~/amber-oracle
#   ORACLE=/scratch/amber bash oracle-setup.sh
#   rm -rf ~/amber-oracle               # removes all of it
#
# Afterwards:  source ~/amber-oracle/env.sh
#
# Installs: uv, Witness v0.12.0 (checksum-verified), OCaml 4.14.2 built from the
# tagged source (~10 min), ProVerif 2.05 from the official tarball (SHA-256 checked against the
# corpus entry), and darnit-amber from the darnit PR #678 branch at a pinned commit.
# Needs on the machine: git, gcc, make, curl, tar, python3, openssl.
set -euo pipefail

ORACLE="${ORACLE:-$HOME/amber-oracle}"
WITNESS_VERSION="0.12.0"
OCAML_VERSION="4.14.2"
OCAML_COMMIT="8eb41f72ded84df884c3671734c947f612091f84"   # the 4.14.2 tag
PROVERIF_URL="https://bblanche.gitlabpages.inria.fr/proverif/proverif2.05.tar.gz"
PROVERIF_SHA256="4871f53c32ab4a04669a060c4886ba5d9080496963fb980a9a62d2c429ceabc4"
PROVERIF_BANNER="Proverif 2.05. Cryptographic protocol verifier, by Bruno Blanchet, Vincent Cheval, and Marc Sylvestre"
DARNIT_REPO="https://github.com/darnitdevorg/darnit.git"
DARNIT_PR=678
DARNIT_COMMIT="fbdf9a2"   # head of PR #678 when this script was written

step() { printf '\n==> %s\n' "$*"; }
have() { [ -x "$ORACLE/bin/$1" ]; }

mkdir -p "$ORACLE"/{bin,src,store}
export PATH="$ORACLE/bin:$PATH"
export UV_PYTHON_INSTALL_DIR="$ORACLE/python"   # if uv must fetch a Python, it goes here too

for t in git gcc make curl tar python3 openssl; do
  command -v "$t" >/dev/null || { echo "missing: $t" >&2; exit 1; }
done

step "uv"
if ! have uv; then
  curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="$ORACLE/bin" UV_NO_MODIFY_PATH=1 sh
fi
uv --version

step "Witness v$WITNESS_VERSION"
if ! have witness; then
  (
    cd "$ORACLE/src"
    base="https://github.com/in-toto/witness/releases/download/v$WITNESS_VERSION"
    curl -fsSLO "$base/witness_${WITNESS_VERSION}_linux_amd64.tar.gz"
    curl -fsSLO "$base/witness_${WITNESS_VERSION}_checksums.txt"
    sha256sum --ignore-missing -c "witness_${WITNESS_VERSION}_checksums.txt"
    tar xzf "witness_${WITNESS_VERSION}_linux_amd64.tar.gz" witness
    mv witness "$ORACLE/bin/witness"
  )
fi
witness version | head -1

step "OCaml $OCAML_VERSION from source (github.com/ocaml/ocaml tag $OCAML_VERSION; compiles in 5-10 minutes)"
if [ ! -x "$ORACLE/ocaml/bin/ocamlopt" ]; then
  (
    cd "$ORACLE/src"
    rm -rf ocaml
    git clone -q --depth 1 --branch "$OCAML_VERSION" https://github.com/ocaml/ocaml.git ocaml
    cd ocaml
    test "$(git rev-parse HEAD)" = "$OCAML_COMMIT" || { echo "ocaml tag $OCAML_VERSION is not commit $OCAML_COMMIT" >&2; exit 1; }
    ./configure --prefix="$ORACLE/ocaml" --disable-ocamldoc --disable-debugger >configure.log 2>&1 || { tail -20 configure.log; exit 1; }
    make -j"$(nproc)" world.opt >build.log 2>&1 || { tail -20 build.log; exit 1; }
    make install >install.log 2>&1 || { tail -20 install.log; exit 1; }
  )
fi
export PATH="$ORACLE/ocaml/bin:$PATH"
ocamlopt -version

step "ProVerif 2.05 (official tarball, SHA-256 checked)"
if ! have proverif; then
  (
    cd "$ORACLE/src"
    curl -fsSLO "$PROVERIF_URL"
    echo "$PROVERIF_SHA256  proverif2.05.tar.gz" | sha256sum -c
    rm -rf proverif2.05
    tar xzf proverif2.05.tar.gz
    cd proverif2.05
    ./build -nointeract >build.log 2>&1 || { tail -20 build.log; exit 1; }
    cp proverif "$ORACLE/bin/proverif"
  )
fi
proverif -help 2>&1 | head -1 | grep -Fx "$PROVERIF_BANNER" || { echo "unexpected proverif banner" >&2; exit 1; }

step "darnit + darnit-amber (PR #$DARNIT_PR at $DARNIT_COMMIT)"
if [ ! -d "$ORACLE/darnit/.git" ]; then
  git clone -q "$DARNIT_REPO" "$ORACLE/darnit"
fi
(
  cd "$ORACLE/darnit"
  git fetch -q origin "+refs/pull/$DARNIT_PR/head:pr-$DARNIT_PR"
  git checkout -q "$DARNIT_COMMIT"
  uv sync -q
  ln -sf "$ORACLE/darnit/.venv/bin/darnit-amber" "$ORACLE/bin/darnit-amber"
  ln -sf "$ORACLE/darnit/.venv/bin/darnit" "$ORACLE/bin/darnit"
)
darnit-amber --help | head -1

step "signing key for this machine (ed25519; the public half is what you hand to others)"
mkdir -p "$ORACLE/keys"
if [ ! -f "$ORACLE/keys/oracle.key" ]; then
  openssl genpkey -algorithm ed25519 -out "$ORACLE/keys/oracle.key"
  openssl pkey -in "$ORACLE/keys/oracle.key" -pubout -out "$ORACLE/keys/oracle.pub"
  chmod 600 "$ORACLE/keys/oracle.key"
fi

cat > "$ORACLE/env.sh" <<EOF
# source this file: puts the Amber oracle tools first on PATH, nothing else
export PATH="$ORACLE/bin:$ORACLE/ocaml/bin:\$PATH"
export UV_PYTHON_INSTALL_DIR="$ORACLE/python"
EOF

step "done"
cat <<EOF
Installed under $ORACLE:
  $(uv --version)
  $(witness version | head -1)
  ocaml $(ocamlopt -version) (built from source), proverif 2.05
  darnit-amber from $DARNIT_REPO PR #$DARNIT_PR @ $(git -C "$ORACLE/darnit" rev-parse --short HEAD)

Use:    source $ORACLE/env.sh
Remove: rm -rf $ORACLE
EOF

{
  description = "PlayPalace dev environment";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";

  outputs = { self, nixpkgs }:
    let
      systems = [
        "x86_64-linux"
      ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
    in {
      devShells = forAllSystems (system:
        let
          pkgs = import nixpkgs { inherit system; };
          python = pkgs.python313;
          pyPkgs = pkgs.python313Packages;

          pypiSrc = { pname, version, sha256, srcPname ? pname }:
            pkgs.fetchPypi {
              pname = srcPname;
              inherit version;
              sha256 = sha256;
            };

          platform-utils = pyPkgs.buildPythonPackage {
            pname = "platform_utils";
            version = "1.6.0";
            src = pypiSrc {
              pname = "platform_utils";
              version = "1.6.0";
              sha256 = "sha256-kg11Xhks6KzQllzoiEXFuO8UdFETs+THVvhzdKNeQbA=";
            };
            propagatedBuildInputs = [ pyPkgs.platformdirs ];
            pyproject = true;
            build-system = [ pyPkgs.hatchling ];
            nativeBuildInputs = [ pyPkgs.hatchling ];
            pythonImportsCheck = [];
            doCheck = false;
          };

          libloader = pyPkgs.buildPythonPackage {
            pname = "libloader";
            version = "1.4.3";
            src = pypiSrc {
              pname = "libloader";
              version = "1.4.3";
              sha256 = "sha256-nFax7i6GbjFMNdEJXR47mcHHYuiaJ78myYvWXVj04YI=";
            };
            pyproject = true;
            build-system = [ pyPkgs.hatchling ];
            nativeBuildInputs = [ pyPkgs.hatchling ];
            pythonImportsCheck = [];
            doCheck = false;
          };

          accessible-output2 = pyPkgs.buildPythonPackage {
            pname = "accessible-output2";
            version = "0.17";
            src = pypiSrc {
              pname = "accessible_output2";
              version = "0.17";
              sha256 = "sha256-WS2ij7u9U46B7NFyNqrvPFuGze6Pvz9vK4uBvOvZk4k=";
            };
            propagatedBuildInputs = [ libloader platform-utils ];
            format = "setuptools";
            doCheck = false;
          };

          sound-lib = pyPkgs.buildPythonPackage {
            pname = "sound-lib";
            version = "0.83";
            src = pypiSrc {
              pname = "sound_lib";
              version = "0.83";
              sha256 = "sha256-ysXjESGSz50TrIgP72+CyhNGtt7M+Asv+ha3t5ICHwQ=";
            };
            propagatedBuildInputs = [ libloader platform-utils ];
            format = "setuptools";
            doCheck = false;
          };

          websockets = pyPkgs.buildPythonPackage {
            pname = "websockets";
            version = "16.0";
            src = pypiSrc {
              pname = "websockets";
              version = "16.0";
              sha256 = "sha256-X2JhpeVujVxCpEl7Nk6iTZTZVj6PvUTnisQIecYBebU=";
            };
            format = "setuptools";
            postPatch = ''
              substituteInPlace pyproject.toml \
                --replace 'license = "BSD-3-Clause"' 'license = { text = "BSD-3-Clause" }'
            '';
            doCheck = false;
          };

          pythonEnv = python.withPackages (ps: with ps; [
            pip
            setuptools
            wheel
            virtualenv
            wxpython
            websockets
            accessible-output2
            sound-lib
            platformdirs
            platform-utils
            libloader
          ]);

          runtimeLibs = with pkgs; [ gtk3 portaudio libsndfile openal speechd alsa-lib ];

          mkDevShell = extraHook:
            pkgs.mkShell {
              name = "playpalace-devshell";
              packages = with pkgs; [
                bashInteractive
                glibcLocales
                pythonEnv
                uv
                gcc
                pkg-config
                xorg.xorgserver
                dbus
                pulseaudio
                espeak
              ] ++ runtimeLibs;

              buildInputs = runtimeLibs;

              LOCALE_ARCHIVE = "${pkgs.glibcLocales}/lib/locale/locale-archive";
              LANG = "C.UTF-8";
              LC_ALL = "C.UTF-8";

              shellHook = ''
                export UV_SYSTEM_PYTHON=1
                export PLAYPALACE_NIX=1
                echo "PlayPalace Development Environment (flakes)"
                echo "========================================="
                echo "Python: $(python --version 2>/dev/null)"
                echo "uv: $(uv --version 2>/dev/null)"
                echo ""
                echo "Common commands:"
                echo "  nix develop . --command bash"
                echo "  ./scripts/run_server.sh"
                echo "  ./scripts/run_client.sh"
                ${extraHook}
              '';
            };
        in {
          default = mkDevShell "";
          server = mkDevShell ''
            echo "Tip: run ./scripts/nix_server_pytest.sh for server tests."
          '';
          client = mkDevShell ''
            echo "Tip: run ./scripts/nix_client_pytest.sh for client tests."
          '';
        });
    };
}

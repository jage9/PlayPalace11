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
          python = pkgs.python311;
          pyPkgs = pkgs.python311Packages;
          hatchVcs = pyPkgs."hatch-vcs";

          mkSetuptools = { pname, version, srcPname ? pname, sha256, propagatedBuildInputs ? [], postPatch ? "" }:
            pyPkgs.buildPythonPackage {
              inherit pname version propagatedBuildInputs;
              format = "setuptools";
              inherit postPatch;
              src = pkgs.fetchPypi {
                pname = srcPname;
                inherit version;
                sha256 = sha256;
              };
              doCheck = false;
            };

          mkPyproject = { pname, version, sha256, buildInputs ? [], propagatedBuildInputs ? [], srcPname ? pname }:
            pyPkgs.buildPythonPackage {
              inherit pname version propagatedBuildInputs;
              pyproject = true;
              build-system = buildInputs;
              nativeBuildInputs = buildInputs;
              src = pkgs.fetchPypi {
                pname = srcPname;
                inherit version;
                sha256 = sha256;
              };
              pythonImportsCheck = [];
              doCheck = false;
            };

          platform-utils = mkPyproject {
            pname = "platform_utils";
            version = "1.6.0";
            sha256 = "sha256-kg11Xhks6KzQllzoiEXFuO8UdFETs+THVvhzdKNeQbA=";
            propagatedBuildInputs = [ pyPkgs.platformdirs ];
            buildInputs = [ pyPkgs.hatchling ];
          };

          libloader = mkPyproject {
            pname = "libloader";
            version = "1.4.3";
            sha256 = "sha256-nFax7i6GbjFMNdEJXR47mcHHYuiaJ78myYvWXVj04YI=";
            buildInputs = [ pyPkgs.hatchling ];
          };

          accessible-output2 = mkSetuptools {
            pname = "accessible-output2";
            srcPname = "accessible_output2";
            version = "0.17";
            sha256 = "sha256-WS2ij7u9U46B7NFyNqrvPFuGze6Pvz9vK4uBvOvZk4k=";
            propagatedBuildInputs = [ libloader platform-utils ];
          };

          sound-lib = mkSetuptools {
            pname = "sound-lib";
            srcPname = "sound_lib";
            version = "0.83";
            sha256 = "sha256-ysXjESGSz50TrIgP72+CyhNGtt7M+Asv+ha3t5ICHwQ=";
            propagatedBuildInputs = [ libloader platform-utils ];
          };

          websockets = mkSetuptools {
            pname = "websockets";
            version = "16.0";
            sha256 = "sha256-X2JhpeVujVxCpEl7Nk6iTZTZVj6PvUTnisQIecYBebU=";
            postPatch = ''
              substituteInPlace pyproject.toml \
                --replace 'license = "BSD-3-Clause"' 'license = { text = "BSD-3-Clause" }'
            '';
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
                pythonEnv
                uv
                gcc
                pkg-config
                xorg.xorgserver
                dbus
                pulseaudio
                espeak
              ];

              buildInputs = runtimeLibs;
              LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath runtimeLibs;

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
                echo "  ./run_server.sh"
                echo "  ./run_client.sh"
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

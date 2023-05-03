# The flake file is the entry point for nix commands
{
  description = "An example flake";

  # Inputs are how Nix can use code from outside the flake during evaluation.
  inputs.devshell.url = "github:numtide/devshell";
  inputs.flake-compat.url = "github:edolstra/flake-compat";
  inputs.flake-compat.flake = false;

  # Outputs are the public-facing interface to the flake.
  outputs = inputs @ {
    self,
    devshell,
    flake-parts,
    nixpkgs,
    ...
  }:
    flake-parts.lib.mkFlake
    {
      inherit self inputs;
    }
    {
      imports = [
        inputs.devshell.flakeModule
        inputs.flake-parts.flakeModules.easyOverlay
      ];

      systems = ["x86_64-linux" "aarch64-linux"];

      perSystem = {
        self',
        final,
        pkgs,
        ...
      }: {
        overlayAttrs.flagbot-pygments = final.python3Packages.buildPythonPackage {
          pname = "pygments-flagbot";
          version = "0.0.1";
          src = ../flagbot-pygments;
          buildInputs = [pkgs.python3Packages.pygments];
        };
        overlayAttrs.pygments = pkgs.python3Packages.pygments.overrideAttrs (old: {propagatedBuildInputs = old.propagatedBuildInputs ++ [final.flagbot-pygments];});
        devshells.default = {
          name = "fridays-meetings";

          devshell.packages = ["texlive.combined.scheme-full" "latexrun" final.pygments];

          commands = [
            {
              command = "task";
              package = "go-task";
            }
          ];
        };
      };
    };
}

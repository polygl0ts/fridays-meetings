{
  texlive,
  mkShell,
  latexrun,
  inputs,
  system,
  ...
}: let
  inherit (inputs.self.packages.${system}) pygments;
in
  mkShell {
    packages = [texlive.combined.scheme-full latexrun pygments];
  }

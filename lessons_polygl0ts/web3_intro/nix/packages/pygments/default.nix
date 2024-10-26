{
  python3Packages,
  inputs,
  system,
  ...
}: let
  inherit (inputs.self.packages.${system}) flagbot-pygments;
in
  python3Packages.pygments.overrideAttrs (old: {propagatedBuildInputs = old.propagatedBuildInputs ++ [flagbot-pygments];})

{
  inputs.nixpkgs.url = "nixpkgs/nixos-24.05";
  inputs.snowfall-lib.url = "github:snowfallorg/lib";
  inputs.snowfall-lib.inputs.nixpkgs.follows = "nixpkgs";
  inputs.flagbot-pygments.url = "path:../flagbot-pygments";
  inputs.flagbot-pygments.flake = false;

  outputs = inputs:
    inputs.snowfall-lib.mkFlake {
      inherit inputs;
      src = ./.;
      snowfall.root = ./nix;
    };
}
